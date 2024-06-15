#!/usr/bin/env python3

#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"), version 1.0.
# You may only use this file in accordance with the terms of version
# 1.0 of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source.  A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

#
# Copyright (c) 2017 by Delphix. All rights reserved.
# Copyright (c) 2018 by Lawrence Livermore National Security, LLC.
#
# This script must remain compatible with Python 3.6+.
#

import os
import re
import sys
import argparse

#
# This script parses the stdout of zfstest, which has this format:
#
# Test: /path/to/testa (run as root) [00:00] [PASS]
# Test: /path/to/testb (run as jkennedy) [00:00] [PASS]
# Test: /path/to/testc (run as root) [00:00] [FAIL]
# [...many more results...]
#
# Results Summary
# FAIL      22
# SKIP      32
# PASS    1156
#
# Running Time:   02:50:31
# Percent passed: 95.5%
# Log directory:  /var/tmp/test_results/20180615T205926
#

#
# Common generic reasons for a test or test group to be skipped.
#
# Some test cases are known to fail in ways which are not harmful or dangerous.
# In these cases simply mark the test as a known failure until it can be
# updated and the issue resolved.  Note that it's preferable to open a unique
# issue on the GitHub issue tracker for each test case failure.
#
known_reason = 'Known issue'

#
# Some tests require that a test user be able to execute the zfs utilities.
# This may not be possible when testing in-tree due to the default permissions
# on the user's home directory.  When testing this can be resolved by granting
# group read access.
#
# chmod 0750 $HOME
#
exec_reason = 'Test user execute permissions required for utilities'

#
# Some tests require that the kernel supports renameat2 syscall.
#
renameat2_reason = 'Kernel renameat2 support required'

#
# Some tests require the O_TMPFILE flag which was first introduced in the
# 3.11 kernel.
#
tmpfile_reason = 'Kernel O_TMPFILE support required'

#
# Some tests require the statx(2) system call on Linux which was first
# introduced in the 4.11 kernel.
#
statx_reason = 'Kernel statx(2) system call required on Linux'

#
# Some tests require that the lsattr utility support the project id feature.
#
project_id_reason = 'lsattr with set/show project ID required'

#
# Some tests require that the kernel support user namespaces.
#
user_ns_reason = 'Kernel user namespace support required'

#
# Some rewind tests can fail since nothing guarantees that old MOS blocks
# are not overwritten.  Snapshots protect datasets and data files but not
# the MOS.  Reasonable efforts are made in the test case to increase the
# odds that some txgs will have their MOS data left untouched, but it is
# never a sure thing.
#
rewind_reason = 'Arbitrary pool rewind is not guaranteed'

#
# Some tests require a minimum version of the fio benchmark utility.
# Older distributions such as CentOS 6.x only provide fio-2.0.13.
#
fio_reason = 'Fio v2.3 or newer required'

#
# Some tests require that the DISKS provided support the discard operation.
# Normally this is not an issue because loop back devices are used for DISKS
# and they support discard (TRIM/UNMAP).
#
trim_reason = 'DISKS must support discard (TRIM/UNMAP)'

#
# Some tests on FreeBSD require the fspacectl(2) system call and the
# truncate(1) utility supporting the -d option.  The system call was first
# introduced in FreeBSD version 1400032.
#
fspacectl_reason = 'fspacectl(2) and truncate -d support required'

#
# Some tests are not applicable to a platform or need to be updated to operate
# in the manor required by the platform.  Any tests which are skipped for this
# reason will be suppressed in the final analysis output.
#
na_reason = "Not applicable"

#
# Some test cases doesn't have all requirements to run on Github actions CI.
#
ci_reason = 'CI runner doesn\'t have all requirements'

#
# Idmapped mount is only supported in kernel version >= 5.12
#
idmap_reason = 'Idmapped mount needs kernel 5.12+'

#
# copy_file_range() is not supported by all kernels
#
cfr_reason = 'Kernel copy_file_range support required'

if sys.platform.startswith('freebsd'):
    cfr_cross_reason = 'copy_file_range(2) cross-filesystem needs FreeBSD 14+'
else:
    cfr_cross_reason = 'copy_file_range(2) cross-filesystem needs kernel 5.3+'

#
# These tests are known to fail, thus we use this list to prevent these
# failures from failing the job as a whole; only unexpected failures
# bubble up to cause this script to exit with a non-zero exit status.
#
# Format: { 'test-name': ['expected result', 'issue-number | reason'] }
#
# For each known failure it is recommended to link to a GitHub issue by
# setting the reason to the issue number.  Alternately, one of the generic
# reasons listed above can be used.
#
known = {
    'casenorm/mixed_none_lookup_ci': ['FAIL', 7633],
    'casenorm/mixed_formd_lookup_ci': ['FAIL', 7633],
    'cli_root/zpool_import/import_rewind_device_replaced':
        ['FAIL', rewind_reason],
    'cli_user/misc/zfs_share_001_neg': ['SKIP', na_reason],
    'cli_user/misc/zfs_unshare_001_neg': ['SKIP', na_reason],
    'pool_checkpoint/checkpoint_discard_busy': ['SKIP', 12053],
    'privilege/setup': ['SKIP', na_reason],
    'refreserv/refreserv_004_pos': ['FAIL', known_reason],
    'rootpool/setup': ['SKIP', na_reason],
    'rsend/rsend_008_pos': ['SKIP', 6066],
    'vdev_zaps/vdev_zaps_007_pos': ['FAIL', known_reason],
}

if sys.platform.startswith('freebsd'):
    known.update({
        'cli_root/zfs_receive/receive-o-x_props_override':
            ['FAIL', known_reason],
        'cli_root/zpool_resilver/zpool_resilver_concurrent':
            ['SKIP', na_reason],
        'cli_root/zpool_wait/zpool_wait_trim_basic': ['SKIP', trim_reason],
        'cli_root/zpool_wait/zpool_wait_trim_cancel': ['SKIP', trim_reason],
        'cli_root/zpool_wait/zpool_wait_trim_flag': ['SKIP', trim_reason],
        'cli_root/zfs_unshare/zfs_unshare_008_pos': ['SKIP', na_reason],
        'cp_files/cp_files_002_pos': ['SKIP', na_reason],
        'link_count/link_count_001': ['SKIP', na_reason],
        'mmap/mmap_sync_001_pos': ['SKIP', na_reason],
        'rsend/send_raw_ashift': ['SKIP', 14961],
    })
elif sys.platform.startswith('linux'):
    known.update({
        'casenorm/mixed_formd_lookup': ['FAIL', 7633],
        'casenorm/mixed_formd_delete': ['FAIL', 7633],
        'casenorm/sensitive_formd_lookup': ['FAIL', 7633],
        'casenorm/sensitive_formd_delete': ['FAIL', 7633],
        'removal/removal_with_zdb': ['SKIP', known_reason],
        'cli_root/zfs_unshare/zfs_unshare_002_pos': ['SKIP', na_reason],
    })


#
# These tests may occasionally fail or be skipped.  We want there failures
# to be reported but only unexpected failures should bubble up to cause
# this script to exit with a non-zero exit status.
#
# Format: { 'test-name': ['expected result', 'issue-number | reason'] }
#
# For each known failure it is recommended to link to a GitHub issue by
# setting the reason to the issue number.  Alternately, one of the generic
# reasons listed above can be used.
#
maybe = {
    'append/threadsappend_001_pos': ['FAIL', 6136],
    'chattr/setup': ['SKIP', exec_reason],
    'crtime/crtime_001_pos': ['SKIP', statx_reason],
    'cli_root/zdb/zdb_006_pos': ['FAIL', known_reason],
    'cli_root/zfs_destroy/zfs_destroy_dev_removal_condense':
        ['FAIL', known_reason],
    'cli_root/zfs_get/zfs_get_004_pos': ['FAIL', known_reason],
    'cli_root/zfs_get/zfs_get_009_pos': ['SKIP', 5479],
    'cli_root/zfs_rollback/zfs_rollback_001_pos': ['FAIL', known_reason],
    'cli_root/zfs_rollback/zfs_rollback_002_pos': ['FAIL', known_reason],
    'cli_root/zfs_share/zfs_share_concurrent_shares': ['FAIL', known_reason],
    'cli_root/zfs_snapshot/zfs_snapshot_002_neg': ['FAIL', known_reason],
    'cli_root/zfs_unshare/zfs_unshare_006_pos': ['SKIP', na_reason],
    'cli_root/zpool_add/zpool_add_004_pos': ['FAIL', known_reason],
    'cli_root/zpool_destroy/zpool_destroy_001_pos': ['SKIP', 6145],
    'cli_root/zpool_import/zpool_import_missing_003_pos': ['SKIP', 6839],
    'cli_root/zpool_initialize/zpool_initialize_import_export':
        ['FAIL', 11948],
    'cli_root/zpool_labelclear/zpool_labelclear_removed':
        ['FAIL', known_reason],
    'cli_root/zpool_trim/setup': ['SKIP', trim_reason],
    'cli_root/zpool_upgrade/zpool_upgrade_004_pos': ['FAIL', 6141],
    'delegate/setup': ['SKIP', exec_reason],
    'fallocate/fallocate_punch-hole': ['SKIP', fspacectl_reason],
    'history/history_004_pos': ['FAIL', 7026],
    'history/history_005_neg': ['FAIL', 6680],
    'history/history_006_neg': ['FAIL', 5657],
    'history/history_008_pos': ['FAIL', known_reason],
    'history/history_010_pos': ['SKIP', exec_reason],
    'io/mmap': ['SKIP', fio_reason],
    'largest_pool/largest_pool_001_pos': ['FAIL', known_reason],
    'mmp/mmp_on_uberblocks': ['FAIL', known_reason],
    'pam/setup': ['SKIP', "pamtester might be not available"],
    'pool_checkpoint/checkpoint_discard_busy': ['FAIL', 11946],
    'projectquota/setup': ['SKIP', exec_reason],
    'removal/removal_condense_export': ['FAIL', known_reason],
    'renameat2/setup': ['SKIP', renameat2_reason],
    'reservation/reservation_008_pos': ['FAIL', 7741],
    'reservation/reservation_018_pos': ['FAIL', 5642],
    'snapshot/clone_001_pos': ['FAIL', known_reason],
    'snapshot/snapshot_009_pos': ['FAIL', 7961],
    'snapshot/snapshot_010_pos': ['FAIL', 7961],
    'snapused/snapused_004_pos': ['FAIL', 5513],
    'tmpfile/setup': ['SKIP', tmpfile_reason],
    'trim/setup': ['SKIP', trim_reason],
    'upgrade/upgrade_projectquota_001_pos': ['SKIP', project_id_reason],
    'user_namespace/setup': ['SKIP', user_ns_reason],
    'userquota/setup': ['SKIP', exec_reason],
    'vdev_zaps/vdev_zaps_004_pos': ['FAIL', known_reason],
    'zvol/zvol_ENOSPC/zvol_ENOSPC_001_pos': ['FAIL', 5848],
}

if sys.platform.startswith('freebsd'):
    maybe.update({
        'cli_root/zfs_copies/zfs_copies_002_pos': ['FAIL', known_reason],
        'cli_root/zfs_inherit/zfs_inherit_001_neg': ['FAIL', known_reason],
        'cli_root/zpool_import/zpool_import_012_pos': ['FAIL', known_reason],
        'delegate/zfs_allow_003_pos': ['FAIL', known_reason],
        'inheritance/inherit_001_pos': ['FAIL', 11829],
        'pool_checkpoint/checkpoint_big_rewind': ['FAIL', 12622],
        'pool_checkpoint/checkpoint_indirect': ['FAIL', 12623],
        'resilver/resilver_restart_001': ['FAIL', known_reason],
        'snapshot/snapshot_002_pos': ['FAIL', '14831'],
        'bclone/bclone_crossfs_corner_cases': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_corner_cases_limited':
            ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_data': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_embedded': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_hole': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_all': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_checksum': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_compress': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_copies': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_recordsize': ['SKIP', cfr_cross_reason],
        'bclone/bclone_prop_sync': ['SKIP', cfr_cross_reason],
        'block_cloning/block_cloning_cross_enc_dataset':
            ['SKIP', cfr_cross_reason],
        'block_cloning/block_cloning_copyfilerange_cross_dataset':
            ['SKIP', cfr_cross_reason]
    })
elif sys.platform.startswith('linux'):
    maybe.update({
        'bclone/bclone_crossfs_corner_cases': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_corner_cases_limited':
            ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_data': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_embedded': ['SKIP', cfr_cross_reason],
        'bclone/bclone_crossfs_hole': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_all': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_checksum': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_compress': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_copies': ['SKIP', cfr_cross_reason],
        'bclone/bclone_diffprops_recordsize': ['SKIP', cfr_cross_reason],
        'bclone/bclone_prop_sync': ['SKIP', cfr_cross_reason],
        'bclone/bclone_samefs_corner_cases': ['SKIP', cfr_reason],
        'bclone/bclone_samefs_corner_cases_limited': ['SKIP', cfr_reason],
        'bclone/bclone_samefs_data': ['SKIP', cfr_reason],
        'bclone/bclone_samefs_embedded': ['SKIP', cfr_reason],
        'bclone/bclone_samefs_hole': ['SKIP', cfr_reason],
        'block_cloning/block_cloning_clone_mmap_cached': ['SKIP', cfr_reason],
        'block_cloning/block_cloning_clone_mmap_write':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_copyfilerange':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_copyfilerange_cross_dataset':
            ['SKIP', cfr_cross_reason],
        'block_cloning/block_cloning_copyfilerange_fallback':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_copyfilerange_fallback_same_txg':
            ['SKIP', cfr_cross_reason],
        'block_cloning/block_cloning_copyfilerange_partial':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_cross_enc_dataset':
            ['SKIP', cfr_cross_reason],
        'block_cloning/block_cloning_disabled_copyfilerange':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_lwb_buffer_overflow':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_replay':
            ['SKIP', cfr_reason],
        'block_cloning/block_cloning_replay_encrypted':
            ['SKIP', cfr_reason],
        'cli_root/zfs_rename/zfs_rename_002_pos': ['FAIL', known_reason],
        'cli_root/zpool_reopen/zpool_reopen_003_pos': ['FAIL', known_reason],
        'cp_files/cp_files_002_pos': ['SKIP', cfr_reason],
        'fault/auto_online_002_pos': ['FAIL', 11889],
        'fault/auto_replace_001_pos': ['FAIL', 14851],
        'fault/auto_spare_002_pos': ['FAIL', 11889],
        'fault/auto_spare_multiple': ['FAIL', 11889],
        'fault/auto_spare_shared': ['FAIL', 11889],
        'fault/decompress_fault': ['FAIL', 11889],
        'idmap_mount/idmap_mount_001': ['SKIP', idmap_reason],
        'idmap_mount/idmap_mount_002': ['SKIP', idmap_reason],
        'idmap_mount/idmap_mount_003': ['SKIP', idmap_reason],
        'idmap_mount/idmap_mount_004': ['SKIP', idmap_reason],
        'idmap_mount/idmap_mount_005': ['SKIP', idmap_reason],
        'io/io_uring': ['SKIP', 'io_uring support required'],
        'limits/filesystem_limit': ['SKIP', known_reason],
        'limits/snapshot_limit': ['SKIP', known_reason],
        'mmp/mmp_active_import': ['FAIL', known_reason],
        'mmp/mmp_exported_import': ['FAIL', known_reason],
        'mmp/mmp_inactive_import': ['FAIL', known_reason],
        'zvol/zvol_misc/zvol_misc_fua': ['SKIP', 14872],
        'zvol/zvol_misc/zvol_misc_snapdev': ['FAIL', 12621],
        'zvol/zvol_misc/zvol_misc_trim': ['SKIP', 14872],
        'zvol/zvol_misc/zvol_misc_volmode': ['FAIL', known_reason],
    })

# Not all Github actions runners have scsi_debug module, so we may skip
#   some tests which use it.
if os.environ.get('CI') == 'true':
    known.update({
        'cli_root/zpool_expand/zpool_expand_001_pos': ['SKIP', ci_reason],
        'cli_root/zpool_expand/zpool_expand_003_neg': ['SKIP', ci_reason],
        'cli_root/zpool_expand/zpool_expand_005_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/setup': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_001_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_002_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_003_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_004_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_005_pos': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_006_neg': ['SKIP', ci_reason],
        'cli_root/zpool_reopen/zpool_reopen_007_pos': ['SKIP', ci_reason],
        'cli_root/zpool_split/zpool_split_wholedisk': ['SKIP', ci_reason],
        'fault/auto_offline_001_pos': ['SKIP', ci_reason],
        'fault/auto_online_001_pos': ['SKIP', ci_reason],
        'fault/auto_online_002_pos': ['SKIP', ci_reason],
        'fault/auto_replace_001_pos': ['SKIP', ci_reason],
        'fault/auto_replace_002_pos': ['SKIP', ci_reason],
        'fault/auto_spare_ashift': ['SKIP', ci_reason],
        'fault/auto_spare_shared': ['SKIP', ci_reason],
        'procfs/pool_state': ['SKIP', ci_reason],
    })

    maybe.update({
        'events/events_002_pos': ['FAIL', 11546],
    })


def process_results(pathname):
    try:
        f = open(pathname)
    except IOError as e:
        print('Error opening file:', e)
        sys.exit(1)

    prefix = '/zfs-tests/tests/(?:functional|perf/regression)/'
    pattern = \
        r'^Test(?:\s+\(\S+\))?:' + \
        rf'\s*\S*{prefix}(\S+)' + \
        r'\s*\(run as (\S+)\)\s*\[(\S+)\]\s*\[(\S+)\]'
    pattern_log = r'^\s*Log directory:\s*(\S*)'

    d = {}
    logdir = 'Could not determine log directory.'
    for line in f.readlines():
        m = re.match(pattern, line)
        if m and len(m.groups()) == 4:
            d[m.group(1)] = m.group(4)
            continue

        m = re.match(pattern_log, line)
        if m:
            logdir = m.group(1)

    return d, logdir


class ListMaybesAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest="SUPPRESS",
                 default="SUPPRESS",
                 help="list flaky tests and exit"):
        super(ListMaybesAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        for test in maybe:
            print(test)
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze ZTS logs')
    parser.add_argument('logfile')
    parser.add_argument('--list-maybes', action=ListMaybesAction)
    parser.add_argument('--no-maybes', action='store_false', dest='maybes')
    args = parser.parse_args()

    results, logdir = process_results(args.logfile)

    if not results:
        print("\n\nNo test results were found.")
        print("Log directory:", logdir)
        sys.exit(0)

    expected = []
    unexpected = []
    all_maybes = True

    for test in list(results.keys()):
        if results[test] == "PASS":
            continue

        setup = test.replace(os.path.basename(test), "setup")
        if results[test] == "SKIP" and test != setup:
            if setup in known and known[setup][0] == "SKIP":
                continue
            if setup in maybe and maybe[setup][0] == "SKIP":
                continue

        if (test in known and results[test] in known[test][0]):
            expected.append(test)
        elif test in maybe and results[test] in maybe[test][0]:
            if results[test] == 'SKIP' or args.maybes:
                expected.append(test)
            elif not args.maybes:
                unexpected.append(test)
        else:
            unexpected.append(test)
            all_maybes = False

    print("\nTests with results other than PASS that are expected:")
    for test in sorted(expected):
        issue_url = 'https://github.com/openzfs/zfs/issues/'

        # Include the reason why the result is expected, given the following:
        # 1. Suppress test results which set the "Not applicable" reason.
        # 2. Numerical reasons are assumed to be GitHub issue numbers.
        # 3. When an entire test group is skipped only report the setup reason.
        if test in known:
            if known[test][1] == na_reason:
                continue
            elif isinstance(known[test][1], int):
                expect = f"{issue_url}{known[test][1]}"
            else:
                expect = known[test][1]
        elif test in maybe:
            if isinstance(maybe[test][1], int):
                expect = f"{issue_url}{maybe[test][1]}"
            else:
                expect = maybe[test][1]
        elif setup in known and known[setup][0] == "SKIP" and setup != test:
            continue
        elif setup in maybe and maybe[setup][0] == "SKIP" and setup != test:
            continue
        else:
            expect = "UNKNOWN REASON"
        print(f"    {results[test]} {test} ({expect})")

    print("\nTests with result of PASS that are unexpected:")
    for test in sorted(known.keys()):
        # We probably should not be silently ignoring the case
        # where "test" is not in "results".
        if test not in results or results[test] != "PASS":
            continue
        print(f"    {results[test]} {test} (expected {known[test][0]})")

    print("\nTests with results other than PASS that are unexpected:")
    for test in sorted(unexpected):
        expect = "PASS" if test not in known else known[test][0]
        print(f"    {results[test]} {test} (expected {expect})")

    if len(unexpected) == 0:
        sys.exit(0)
    elif not args.maybes and all_maybes:
        sys.exit(2)
    else:
        sys.exit(1)
