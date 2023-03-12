#!/usr/bin/env bash

wget https://repo.almalinux.org/almalinux/8/cloud/aarch64/images/AlmaLinux-8-GenericCloud-latest.aarch64.qcow2

##
git clone https://github.com/qemu/qemu
cd qemu
time ./configure
time make -j4
real	6m0.573s @ apple M1
user	15m5.704s
sys	2m8.890s

real	22m35.652s @ amd (9485)
user	78m30.826s
sys	9m57.635s


##

brew install axel cdrtools qemu libvirt virt-manager
sudo ln -s /opt/homebrew/var/lib/libvirt /var/lib/libvirt
echo 'uri = "qemu:///system"' >> /opt/homebrew/etc/libvirt/libvirt.conf
brew services restart libvirt

sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist
sudo /usr/libexec/locate.updatedb

sudo /opt/homebrew/sbin/virtlogd -d
sudo /opt/homebrew/sbin/virtqemud -d
sudo /opt/homebrew/sbin/virtstoraged -d

qemu-system-aarch64 -m 2048 -accel hvf -cpu host \
 -drive file=/usr/local/share/qemu/edk2-aarch64-code.fd,if=pflash,format=raw,readonly=on \
 -drive file=ovmf_vars.fd,if=pflash,format=raw \
 -drive if=none,file=VMDISK,format=qcow2,id=hd0 \
 -device virtio-blk-device,drive=hd0,serial="dummyserial"  \
 -device virtio-net-device,netdev=net0 \
 -serial telnet::4444,server,nowait  \
 -netdev user,id=net0 \
 -vga none \
 -machine virt

exit

#################################################################
# 2) start qemu with some operating system, init via cloud-init #
#################################################################

OS="$1"
ID="$2"
PAT="$3"
REPO="$4"

# valid ostypes: virt-install --os-variant list
OSv=$OS

case "$OS" in
  almalinux8)
    OSNAME="AlmaLinux 8"
    URL="https://repo.almalinux.org/almalinux/8/cloud/x86_64/images/AlmaLinux-8-GenericCloud-latest.x86_64.qcow2"
    ;;
  almalinux9)
    OSNAME="AlmaLinux 9"
    URL="https://repo.almalinux.org/almalinux/9/cloud/x86_64/images/AlmaLinux-9-GenericCloud-latest.x86_64.qcow2"
    ;;
  archlinux)
    OSNAME="Archlinux"
    URL="https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2"
    ;;
  centos-stream8)
    OSNAME="CentOS Stream 8"
    URL="https://cloud.centos.org/centos/8-stream/x86_64/images/CentOS-Stream-GenericCloud-8-latest.x86_64.qcow2"
    ;;
  centos-stream9)
    OSNAME="CentOS Stream 9"
    URL="https://cloud.centos.org/centos/9-stream/x86_64/images/CentOS-Stream-GenericCloud-9-latest.x86_64.qcow2"
    ;;
  debian11)
    OSNAME="Debian 11"
    URL="https://cloud.debian.org/images/cloud/bullseye/latest/debian-11-generic-amd64.qcow2"
    ;;
  debian12)
    OSNAME="Debian 12"
    URL="https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.qcow2"
    ;;
  fedora38)
    OSNAME="Fedora 38"
    URL="https://download.fedoraproject.org/pub/fedora/linux/releases/38/Cloud/x86_64/images/Fedora-Cloud-Base-38-1.6.x86_64.qcow2"
    ;;
  fedora39)
    OSNAME="Fedora 39"
    OSv="fedora38"
    URL="https://download.fedoraproject.org/pub/fedora/linux/releases/39/Cloud/x86_64/images/Fedora-Cloud-Base-39-1.5.x86_64.qcow2"
    ;;
  freebsd13)
    OSNAME="FreeBSD 13"
    OSv="freebsd13.0"
    URL="https://download.freebsd.org/ftp/snapshots/amd64"
    # freebsd images don't include cloud-init :(
    # -> workaround: provide own images base on this url:
    URL="https://openzfs.de/freebsd/amd64-freebsd-13.2.qcow2"
    BASH="/usr/local/bin/bash"
    ;;
  freebsd14)
    OSNAME="FreeBSD 14"
    OSv="freebsd13.0"
    URL="https://openzfs.de/freebsd/amd64-freebsd-14.0.qcow2"
    BASH="/usr/local/bin/bash"
    ;;
  freebsd15)
    OSNAME="FreeBSD 15"
    OSv="freebsd13.0"
    URL="https://openzfs.de/freebsd/amd64-freebsd-15.0.qcow2"
    BASH="/usr/local/bin/bash"
    ;;
  ubuntu22)
    OSNAME="Ubuntu 22.04"
    OSv="ubuntu22.04"
    URL="https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img"
    ;;
  ubuntu24)
    OSNAME="Ubuntu 24.04"
    OSv="ubuntu24.04"
    URL="https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img"
    ;;
  *)
    echo "Wrong value for variable OS!"
    exit 111
    ;;
esac

IMG="/mnt/original.qcow2"
DISK="/mnt/openzfs.qcow2"

echo "Loading image $URL ..."
sudo axel -q "$URL" -o "$IMG" || exit 111

# we use zstd for faster IO on the testing runner
echo "Converting image ..."
sudo qemu-img convert -f qcow2 -O qcow2 -c -o compression_type=zstd,preallocation=off $IMG $DISK || exit 111
sudo rm -f /mnt/original.qcow2 || exit 111

echo "Resizing image to 60GiB ..."
sudo qemu-img resize $DISK 60G || exit 111

PUBKEY=`sudo cat /root/.ssh/id_ed25519.pub`
cat <<EOF > /tmp/user-data
#cloud-config

fqdn: $OS

users:
- name: root
  shell: $BASH
- name: zfs
  sudo: ALL=(ALL) NOPASSWD:ALL
  shell: $BASH
  ssh_authorized_keys:
    - $PUBKEY

growpart:
  mode: auto
  devices: ['/']
  ignore_growroot_disabled: false

write_files:
  - content: |
      #!/usr/bin/env bash

      cd \$HOME
      exec 2>stderr-init.log
      echo "$OSNAME" > /var/tmp/osname.txt

      # download github action runner package
      function download_action_runner() {
        REL="2.312.0"
        URL="https://github.com/actions/runner/releases"
        while :; do
          # https://github.com/actions/runner/releases/download/v2.305.0/actions-runner-linux-arm64-2.305.0.tar.gz
          curl -s -o ghar.tgz -L "\$URL/download/v\$REL/actions-runner-linux-\$1-\$REL.tar.gz"
          [[ \$? == 0 ]] && break
          sleep 5
        done
        tar xzf ./ghar.tgz

        # in case sth. is missing /TR
        sudo ./bin/installdependencies.sh
      }

      # download github-act-runner package
      function download_act_runner() {
        REL="v0.6.7"
        URL="https://github.com/ChristopherHX/github-act-runner/releases"
        TGZ="download/\$REL/binary-\$1.tar.gz"
        while :; do
          curl -s -o gar.tgz -L "\$URL/\$TGZ"
          [[ \$? == 0 ]] && break
          sleep 5
        done
        tar xzf ./gar.tgz
      }

      case $OS in
      debian*|ubuntu*)
        export DEBIAN_FRONTEND="noninteractive"
        sudo systemctl stop unattended-upgrades
        sudo systemctl disable unattended-upgrades
        download_action_runner "x64"
        ;;
      freebsd*)
        export ASSUME_ALWAYS_YES="YES"
        yes | sudo pkg update
        download_act_runner "freebsd-amd64"
        ;;
      *)
        download_action_runner "x64"
        ;;
      esac

      # start action runner
      ./config.sh \
        --name "$ID" \
        --labels "$ID" \
        --replace \
        --ephemeral \
        --unattended \
        --pat "$PAT" \
        --url "$REPO"
      exec /tmp/runner-start.sh
    path: /tmp/runner-init.sh
    permissions: '0755'
  - content: |
      #!/usr/bin/env bash

      exec 2>\$HOME/stderr-start.log
      cd \$HOME

      sudo rm -f /tmp/runner-init.sh
      sudo rm -rf /var/lib/cloud/instance/*
      # start tests
      ./run.sh
      sudo poweroff -f
    path: /tmp/runner-start.sh
    permissions: '0755'

runcmd:
  - sudo -u zfs /tmp/runner-init.sh
EOF

# we could extend this with more virtual disks for example /TR
echo "Starting machine for runner $ID ..."
sudo virt-install \
  --os-variant $OSv \
  --name "openzfs" \
  --cpu host-passthrough \
  --vcpus=4,sockets=1 \
  --memory 10240 \
  --graphics none \
  --network bridge=virbr0,model=virtio \
  --cloud-init user-data=/tmp/user-data \
  --disk $DISK,format=qcow2,bus=virtio \
  --import --noautoconsole

#--qemu-commandline='-M highmem=off -netdev vmnet-shared,id=net0 -device virtio-net-device,netdev=net0,mac=NN:NN:NN:NN:NN:NN' \
#--network user

sudo rm -f /tmp/user-data
echo "Starting $ID -> result=$?"
