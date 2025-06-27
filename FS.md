# Übersicht zu Dateisystemen

## [EXT4](https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git/)
- lange Zeit das Standard Dateisystem von Linux, wird zunehmend durch XFS verdrängt
- Journaling, Delayed Allocation, Extents usw. sorgen für mehr Speed als bei EXT3
- keine Prüfsummen für Datenintegrität und ich mag die Codequalität auch nicht

## [XFS](https://git.kernel.org/pub/scm/fs/xfs/xfs-documentation.git/)
- 64-Bit-Journaling-Dateisystem, das als sehr schnell und ausgereift gilt
- wurde 1993 Silicon Graphics (SGI) für sein UNIX-System-V-basiertes Betriebssystem IRIX entwickelt und später für Linux freigegeben
- keine Prüfsummen für Datenintegrität, gute Codequalität

## [BTRFS](https://github.com/btrfs)
- Btrfs ist ein Copy-on-Write (CoW) Dateisystem für Linux, wird durch Oracle entwickelt
- soll ähnliche Features wie ZFS haben bzw. bekommen
- hat Probleme mit RAID5/RAID6 und dadurch einen relativ schlechten Ruf (Probleme werde nicht gefixt)
- ein einfacher Mirror läuft stabil, jedoch hat Redhat den Support dafür eingeschränkt

## [OpenZFS](https://github.com/openzfs/zfs)
- 11.3k stars, 437 watching, 1.9k forks, C 71.8%, Shell 18.8%
- ZFS wurde 2005 durch SUN unter der CDDL freigegeben
- Aufgrund dieser freien Lizenz, welche ähnlich der GPLv2 ist, kann die Codebase nicht in Linux einfließen
- das OpenZFS Projekt entstand 2016
- die Entwicklung wird via LLNL forciert
- es gibt aber auch Firmen wie Klara die Support verkaufen und das Projekt voran treiben
- die Liste der Features ist ziemlich lang
- mehrere vdev's werden zu einem Pool, dieser kann Dateisysteme oder Blockdevices zur Verfügung stellen
- sehr aktives Projekt

## Distributed FileSystems

### [SaunaFS](https://github.com/leil-io/saunafs)
- 81 stars, 6 watching, 6 forks, GPL-3.0 license
- distributed POSIX file system inspired by the Google File System
- chunk-based storage architecture
- segmenting files into 64 MiB chunks subdivided into 64 KiB blocks each with 4 bytes of CRC for data integrity
- Metadata Servers (Master, Shadows, Metaloggers)
- Data Servers (Chunkservers)
- Clients for (supporting multiple operating systems and NFS).

### [Longhorn](https://github.com/longhorn/longhorn)
- 6.8k stars, 98 watching, 642 forks, Apache-2.0 license, Shell 83.4%, Python 12.7%
- distributed block storage system for Kubernetes
- cloud-native storage built using Kubernetes and container primitives
- sehr aktives Projekt

## [dCache](https://github.com/dCache/dcache)
- 302 stars, 29 watching, 142 forks, AGPL v3, Java, 95.2%, JavaScript 2.0%
- dCache is a system for storing and retrieving huge amounts of data
- distributed among a large number of heterogeneous server nodes
- xrootd, pNFS, HSM, etc.

### [Sheepdog](https://github.com/sheepdog/sheepdog)
- 1k stars, 133 watching, 266 forks, GPL-2.0 license, C 79.9%, Assembly 7.0%
- distributed Storage System for KVM / QEMU
- provides highly available block level storage volumes to virtual machines.
- supports advanced volume management features such as snapshot, cloning and thin provisioning
- letzter commit war 2018, daher: **nicht mehr relevant**

### [XtreemFS](https://github.com/xtreemfs/xtreemfs)
- 341 Stars, 36 Watchers, 64 Forks, Custom license like MIT, Java 68.4%, C++ 22.5%
- kaum noch Aktivität
