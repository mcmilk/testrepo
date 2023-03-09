
## Summary for Logs-20.04-functional

<pre>

Tests with results other than PASS that are expected:
    FAIL casenorm/mixed_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_none_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_lookup (https://github.com/openzfs/zfs/issues/7633)
    FAIL cli_root/zpool_import/import_rewind_device_replaced (Arbitrary pool rewind is not guaranteed)
    SKIP cli_root/zpool_import/zpool_import_missing_003_pos (https://github.com/openzfs/zfs/issues/6839)
    SKIP crtime/crtime_001_pos (Kernel statx(2) system call required on Linux)
    SKIP rsend/rsend_008_pos (https://github.com/openzfs/zfs/issues/6066)
    FAIL vdev_zaps/vdev_zaps_007_pos (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
02:52:21.13 SUCCESS: set_tunable32 TXG_HISTORY 100
02:52:21.13 SUCCESS: mkdir -p /var/tmp/bakdev_import-test
02:52:21.13 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk0
02:52:21.14 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk1
02:52:21.14 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk2
02:52:21.15 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk3
02:52:21.15 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk4
02:52:21.16 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk5
02:52:21.16 NOTE: test_replace_vdev: pool '/var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1', replace /var/tmp/dev_import-test/disk1 by /var/tmp/dev_import-test/disk2.
02:52:21.23 SUCCESS: zpool create testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:52:21.27 SUCCESS: zfs create testpool1/ds1
02:52:21.36 SUCCESS: zpool sync testpool1
02:52:21.40 SUCCESS: zfs create testpool1/ds2
02:52:21.49 SUCCESS: zpool sync testpool1
02:52:21.52 SUCCESS: zfs create testpool1/ds3
02:52:21.61 SUCCESS: zpool sync testpool1
02:52:21.62 SUCCESS: generate_data testpool1 /var/tmp/md5sums.627850
02:52:22.54 SUCCESS: write_some_data testpool1 15
02:52:22.58 SUCCESS: zpool sync testpool1
02:52:22.61 SUCCESS: zpool sync testpool1
02:52:22.64 SUCCESS: zpool sync testpool1
02:52:22.67 SUCCESS: zpool sync testpool1
02:52:22.70 SUCCESS: zpool sync testpool1
02:52:22.74 SUCCESS: zpool sync testpool1
02:52:22.77 SUCCESS: zpool sync testpool1
02:52:22.80 SUCCESS: zpool sync testpool1
02:52:22.83 SUCCESS: zpool sync testpool1
02:52:22.86 SUCCESS: zpool sync testpool1
02:52:22.89 SUCCESS: zpool sync testpool1
02:52:22.89 SUCCESS: sync_some_data_a_few_times testpool1
02:52:25.52 SUCCESS: zfs snapshot -r testpool1@snap1
02:52:25.61 SUCCESS: overwrite_data testpool1 
02:52:25.72 SUCCESS: zpool export testpool1
02:52:25.91 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:52:25.91 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 1
02:52:25.97 SUCCESS: zpool replace testpool1 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk2
02:52:25.99 SUCCESS: pool_is_replacing testpool1
02:52:32.15 SUCCESS: zpool export testpool1
02:52:32.15 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:52:32.35 SUCCESS: zpool import -d /var/tmp/dev_import-test -o readonly=on -T 53 testpool1
02:52:32.40 SUCCESS: check_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:52:32.48 SUCCESS: verify_data_md5sums /var/tmp/md5sums.627850
02:52:32.52 SUCCESS: zpool export testpool1
02:52:33.10 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:52:33.20 SUCCESS: overwrite_data testpool1 
02:52:36.32 SUCCESS: wait_for_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk2
02:52:36.39 SUCCESS: zpool export testpool1
02:52:36.39 SUCCESS: mv /var/tmp/dev_import-test/disk2 /var/tmp/bakdev_import-test/
02:52:36.75 cannot import 'testpool1': one or more devices is currently unavailable
02:52:36.75 ERROR: zpool import -d /var/tmp/dev_import-test -T 53 testpool1 exited 1
02:52:36.75 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:52:36.75 =================================================================
02:52:36.75  Tailing last 200 lines of zfs_dbgmsg log
02:52:36.75 =================================================================
02:52:36.77 1678330356   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 3, unflushed_allocs 0, unflushed_frees 3159040, appended 24 bytes
02:52:36.77 1678330356   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 14, unflushed_allocs 0, unflushed_frees 1024, appended 16 bytes
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): UNLOADING
02:52:36.77 1678330356   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool1' gethrtime 3622862014700
02:52:36.77 1678330356   spa.c:6288:spa_tryimport(): spa_tryimport: importing testpool1, max_txg=53
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa $import. txg 53
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=53
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load($import, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): UNLOADING
02:52:36.77 1678330356   spa.c:6145:spa_import(): spa_import: importing testpool1, max_txg=53 (RECOVERY MODE)
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 53
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=53
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 52
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 50
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 50)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=50
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 49
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 47
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 47)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=47
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 46
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 44
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 44)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=44
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 43
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 41
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 41)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=41
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 40
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 38
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 38)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=38
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 37
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 35
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 35)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=35
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 34
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 32
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 32)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=32
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 31
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 29
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 29)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=29
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 28
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 26
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 26)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=26
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 25
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 23
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 23)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=23
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 22
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 22
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 22)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=22
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 21
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 21
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 21)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=21
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 20
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 20
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 20)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=20
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 19
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 17
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 17)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=17
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 16
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 16
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 16)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=16
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 15
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 13
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 13)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=13
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 12
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 12
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 12)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=12
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 11
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 9
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 9)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=9
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 8
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 8
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 8)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=8
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 7
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 6
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 6)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=6
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 5
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 5
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 5)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=5
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 4
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 4
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 4)
02:52:36.77 1678330356   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=4
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 3
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:52:36.77 1678330356   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: no valid uberblock found
02:52:36.77 1678330356   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:52:36.78 =================================================================
02:52:36.78  End of zfs_dbgmsg log
02:52:36.78 =================================================================
02:52:36.78 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:52:36.78 =================================================================
02:52:36.78  Tailing last 200 lines of dmesg log
02:52:36.78 =================================================================
02:52:36.79 [ 3033.789735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg
02:52:36.79 [ 3033.926623] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos
02:52:36.79 [ 3035.373260] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup
02:52:36.79 [ 3035.434238] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup
02:52:36.79 [ 3035.744990] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos
02:52:36.79 [ 3035.791109] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos
02:52:36.79 [ 3036.130813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos
02:52:36.79 [ 3037.477893] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg
02:52:36.79 [ 3037.529523] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos
02:52:36.79 [ 3037.741024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup
02:52:36.79 [ 3037.966245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup
02:52:36.79 [ 3038.430905] debugfs: Directory 'zd0' with parent 'block' already present!
02:52:36.79 [ 3038.862782] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg
02:52:36.79 [ 3039.185934] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos
02:52:36.79 [ 3039.363136] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup
02:52:36.79 [ 3039.588056] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup
02:52:36.79 [ 3039.925884] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos
02:52:36.79 [ 3048.236253] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos
02:52:36.79 [ 3056.727640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos
02:52:36.79 [ 3057.361720] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos
02:52:36.79 [ 3066.239369] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos
02:52:36.79 [ 3075.147727] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos
02:52:36.79 [ 3084.319012] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos
02:52:36.79 [ 3097.009834] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos
02:52:36.79 [ 3110.879667] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg
02:52:36.79 [ 3115.741364] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos
02:52:36.79 [ 3122.591225] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg
02:52:36.79 [ 3129.200483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos
02:52:36.79 [ 3160.831327] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg
02:52:36.79 [ 3229.116447] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos
02:52:36.79 [ 3232.553977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos
02:52:36.79 [ 3235.645030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos
02:52:36.79 [ 3246.141638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos
02:52:36.79 [ 3260.055002] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos
02:52:36.79 [ 3272.188725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg
02:52:36.79 [ 3290.568415] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos
02:52:36.79 [ 3309.190454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos
02:52:36.79 [ 3353.322631] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos
02:52:36.79 [ 3414.284278] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos
02:52:36.79 [ 3414.327958] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos
02:52:36.79 [ 3422.950462] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos
02:52:36.79 [ 3426.378852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted
02:52:36.79 [ 3427.367331] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load
02:52:36.79 [ 3429.774413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3
02:52:36.79 [ 3431.534006] debugfs: Directory 'zd0' with parent 'block' already present!
02:52:36.79 [ 3432.490300] debugfs: Directory 'zd16' with parent 'block' already present!
02:52:36.79 [ 3433.163074] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4
02:52:36.79 [ 3438.045004] debugfs: Directory 'zd0' with parent 'block' already present!
02:52:36.79 [ 3438.937381] debugfs: Directory 'zd16' with parent 'block' already present!
02:52:36.79 [ 3439.981277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added
02:52:36.79 [ 3445.551885] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed
02:52:36.79 [ 3466.104046] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced
02:52:36.79 [ 3509.225306] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached
02:52:36.79 [ 3511.054153] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached
02:52:36.79 [ 3516.691180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed
02:52:36.79 [ 3521.326669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device
02:52:36.79 [ 3523.268722] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing
02:52:36.79 [ 3532.717213] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed
02:52:36.79 [ 3535.869754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed
02:52:36.79 [ 3607.998603] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced
02:52:36.79 =================================================================
02:52:36.79  End of dmesg log
02:52:36.79 =================================================================
02:52:36.79 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:52:36.79 NOTE: Performing local cleanup via log_onexit (custom_cleanup)
02:52:36.79 SUCCESS: set_zfs_txg_timeout 5
02:52:36.81 SUCCESS: rm -rf /var/tmp/bakdev_import-test
02:52:36.81 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:52:36.83 SUCCESS: eval zinject -c all > /dev/null
02:52:36.84 NOTE: Pool does not exist. (testpool1)
02:52:36.84 SUCCESS: rm -f /var/tmp/cachefile.627850 /var/tmp/cachefile.627850.bkp /var/tmp/cachefile.627850.bkp2 /var/tmp/md5sums.627850 /var/tmp/md5sums.627850.2
02:52:36.88 SUCCESS: rm -rf /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk3 /var/tmp/dev_import-test/disk4 /var/tmp/dev_import-test/disk5
02:52:36.89 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk0
02:52:36.89 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk1
02:52:36.89 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk2
02:52:36.90 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk3
02:52:36.90 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk4
02:52:36.91 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk5
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
02:11:49.26 ASSERTION: CS-UN FS: lookup succeeds if (case=same)
02:11:49.31 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:49.36 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.36 SUCCESS: create_file FïLëNÄmë
02:11:49.37 SUCCESS: lookup_file FïLëNÄmë
02:11:49.37 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:49.38 SUCCESS: lookup_file fïlënämë exited 1
02:11:49.38 SUCCESS: lookup_file FïLëNÄmë
02:11:49.38 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:49.39 SUCCESS: lookup_file fïlënämë exited 1
02:11:49.39 SUCCESS: create_file FÏLËNÄMË
02:11:49.40 SUCCESS: lookup_file FïLëNÄmë exited 1
02:11:49.40 SUCCESS: lookup_file FÏLËNÄMË
02:11:49.40 SUCCESS: lookup_file fïlënämë exited 1
02:11:49.41 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:11:49.41 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:49.41 =================================================================
02:11:49.41  Tailing last 200 lines of zfs_dbgmsg log
02:11:49.41 =================================================================
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 32, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22016, unflushed_frees 17408, appended 96 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 33 create testpool/testfs (id 149)  
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 33, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 43008, appended 128 bytes
02:11:49.43 1678327899   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 34, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 47104, appended 128 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 35 set testpool/testfs (id 149) mountpoint=/var/tmp/testdir
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 35, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 27648, appended 112 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 36, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 47616, unflushed_frees 30208, appended 144 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 37 destroy testpool/testfs (id 149) (bptree, mintxg=1)
02:11:49.43 1678327899   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327899   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 37; err=0
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 37, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 29184, unflushed_frees 25088, appended 144 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 258)  
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 23552, unflushed_frees 24064, appended 88 bytes
02:11:49.43 1678327899   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 47616, appended 144 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 258) mountpoint=/var/tmp/testdir
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 47616, appended 160 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 23552, appended 104 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 258) (bptree, mintxg=1)
02:11:49.43 1678327899   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327899   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30208, unflushed_frees 25600, appended 144 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 267)  
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 31232, unflushed_frees 44032, appended 120 bytes
02:11:49.43 1678327899   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 28672, appended 112 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 267) mountpoint=/var/tmp/testdir
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45056, unflushed_frees 48128, appended 152 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 31232, appended 136 bytes
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 267) (bptree, mintxg=1)
02:11:49.43 1678327899   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327899   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 19456, appended 112 bytes
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327899   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 277)  
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 32768, unflushed_frees 45056, appended 128 bytes
02:11:49.43 1678327899   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327899   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
02:11:49.43 1678327899   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 48640, appended 152 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 277) mountpoint=/var/tmp/testdir
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29696, appended 120 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 286)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 32768, appended 128 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 28160, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 286) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 20480, appended 104 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40960, unflushed_frees 39936, appended 168 bytes
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 46080, appended 152 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 277) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 26624, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 170)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 25600, unflushed_frees 43008, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 43520, appended 152 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 170) mountpoint=/var/tmp/testdir
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 31232, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 178)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 32256, appended 152 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 27648, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 178) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22528, appended 96 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40960, unflushed_frees 41984, appended 168 bytes
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47616, appended 160 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 170) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 299)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 27136, unflushed_frees 43520, appended 136 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 44544, appended 152 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 299) mountpoint=/var/tmp/testdir
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 32256, appended 144 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 191)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 34304, appended 168 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 29696, appended 160 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 191) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22528, appended 112 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 42496, unflushed_frees 41472, appended 176 bytes
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 47616, appended 160 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 299) (bptree, mintxg=1)
02:11:49.43 1678327900   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327900   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 28160, appended 160 bytes
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 202)  
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 28160, unflushed_frees 44544, appended 136 bytes
02:11:49.43 1678327900   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327900   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 45568, appended 136 bytes
02:11:49.43 1678327900   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 202) mountpoint=/var/tmp/testdir
02:11:49.43 1678327900   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 136 bytes
02:11:49.43 1678327901   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327901   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 211)  
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 34816, appended 160 bytes
02:11:49.43 1678327901   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327901   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 30208, appended 152 bytes
02:11:49.43 1678327901   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 211) (bptree, mintxg=1)
02:11:49.43 1678327901   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327901   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 24064, appended 80 bytes
02:11:49.43 1678327901   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 44032, appended 176 bytes
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 168 bytes
02:11:49.43 1678327901   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 202) (bptree, mintxg=1)
02:11:49.43 1678327901   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327901   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 128 bytes
02:11:49.43 1678327901   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327901   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 317)  
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46080, appended 128 bytes
02:11:49.43 1678327901   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327901   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 46592, appended 136 bytes
02:11:49.43 1678327901   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 317) mountpoint=/var/tmp/testdir
02:11:49.43 1678327901   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 34304, appended 128 bytes
02:11:49.43 1678327902   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327902   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 36352, appended 144 bytes
02:11:49.43 1678327904   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 189440, unflushed_frees 38400, appended 136 bytes
02:11:49.43 1678327906   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24576, appended 88 bytes
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 488448, unflushed_frees 43008, appended 256 bytes
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 488960, unflushed_frees 47616, appended 288 bytes
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 317) (bptree, mintxg=1)
02:11:49.43 1678327908   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327908   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 192512, unflushed_frees 44032, appended 192 bytes
02:11:49.43 1678327908   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 225)  
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 31232, unflushed_frees 634368, appended 304 bytes
02:11:49.43 1678327908   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327908   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 128 bytes
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 225) mountpoint=/var/tmp/testdir
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 647168, appended 440 bytes
02:11:49.43 1678327908   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56320, unflushed_frees 37888, appended 208 bytes
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 225) (bptree, mintxg=1)
02:11:49.43 1678327908   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327908   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 136 bytes
02:11:49.43 1678327908   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 238)  
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 56320, appended 160 bytes
02:11:49.43 1678327908   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327908   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 120 bytes
02:11:49.43 1678327908   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 238) mountpoint=/var/tmp/testdir
02:11:49.43 1678327908   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 59904, appended 184 bytes
02:11:49.43 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56320, unflushed_frees 37888, appended 144 bytes
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 104 bytes
02:11:49.43 1678327909   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 238) (bptree, mintxg=1)
02:11:49.43 1678327909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.43 1678327909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 128 bytes
02:11:49.43 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.43 1678327909   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 250)  
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 56320, appended 168 bytes
02:11:49.43 1678327909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.43 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 112 bytes
02:11:49.43 1678327909   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 250) mountpoint=/var/tmp/testdir
02:11:49.43 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 176 bytes
02:11:49.44 =================================================================
02:11:49.44  End of zfs_dbgmsg log
02:11:49.44 =================================================================
02:11:49.44 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:49.44 =================================================================
02:11:49.44  Tailing last 200 lines of dmesg log
02:11:49.44 =================================================================
02:11:49.45 [  799.147307] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:49.45 [  800.188706] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:49.45 [  800.829753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:49.45 [  801.712728] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:49.45 [  802.043506] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:49.45 [  812.411134] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:49.45 [  813.086032] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:49.45 [  821.220439] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:49.45 [  822.005064] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:49.45 [  822.315758] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:49.45 [  957.829958] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:49.45 [  974.747554] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:49.45 [  974.849019] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:49.45 [  975.157521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:49.45 [  975.284934] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:49.45 [  975.328165] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:49.45 [  975.614364] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:49.45 [  975.902212] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:49.45 [  976.641525] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:49.45 [  976.972422] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:49.45 [  977.441532] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:49.45 [  977.586548] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:49.45 [  977.870885] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:49.45 [  978.112529] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:49.45 [  988.769458] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:49.45 [  995.335728] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:49.45 [ 1002.062764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:49.45 [ 1012.864483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:49.45 [ 1013.124523] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:49.45 [ 1013.363976] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:49.45 [ 1024.012827] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:49.45 [ 1034.824512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:49.45 [ 1035.097151] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:49.45 [ 1035.126568] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:49.45 [ 1036.801300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:49.45 [ 1039.005095] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:49.45 [ 1039.709241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:49.45 [ 1041.617047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:49.45 [ 1042.331055] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:49.45 [ 1049.452554] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:49.45 [ 1055.503554] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:49.45 [ 1055.899135] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:49.45 [ 1058.167373] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:49.45 [ 1058.194158] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:49.45 [ 1239.362111] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:49.45 [ 1242.366892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:49.45 [ 1247.015100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:49.45 [ 1259.636500] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:49.45 [ 1269.594710] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:49.45 [ 1280.043538] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:49.45 [ 1281.619624] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:49.45 [ 1283.398419] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:49.45 [ 1305.262851] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:49.45 [ 1306.129113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:49.45 [ 1310.697959] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:49.45 [ 1329.694996] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:49.45 [ 1330.418868] loop3: detected capacity change from 0 to 524288
02:11:49.45 [ 1330.670174] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:49.45 [ 1340.857664] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:49.45 [ 1341.153951] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2956359696140590617), resetting them to the default (8388608)
02:11:49.45 [ 1378.446794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:49.45 [ 1378.884622] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:49.45 [ 1379.002889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:49.45 [ 1381.085775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:49.45 [ 1383.114750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:49.45 [ 1385.212848] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:49.45 [ 1386.922957] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:49.45 [ 1387.000676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:49.45 [ 1387.198290] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:49.45 [ 1387.900955] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:49.45 [ 1390.550506] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:49.45 [ 1397.523907] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:49.45 [ 1398.081797] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:49.45 [ 1398.549761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:49.45 =================================================================
02:11:49.45  End of dmesg log
02:11:49.45 =================================================================
02:11:49.45 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:49.46 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:49.56 SUCCESS: zfs destroy -f testpool/testfs
02:11:49.56 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
02:11:49.59 ASSERTION: CS-UN FS: delete succeeds if (case=same)
02:11:49.64 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:49.69 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.69 SUCCESS: create_file FïLëNÄmë
02:11:49.70 SUCCESS: delete_file FïLëNÄmë
02:11:49.70 SUCCESS: lookup_any exited 1
02:11:49.71 SUCCESS: create_file FïLëNÄmë
02:11:49.71 SUCCESS: delete_file FÏLËNÄMË exited 1
02:11:49.72 SUCCESS: create_file FïLëNÄmë
02:11:49.72 SUCCESS: delete_file fïlënämë exited 1
02:11:49.73 SUCCESS: create_file FïLëNÄmë
02:11:49.73 ERROR: delete_file FïLëNÄmë exited 1
02:11:49.74 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:49.74 =================================================================
02:11:49.74  Tailing last 200 lines of zfs_dbgmsg log
02:11:49.74 =================================================================
02:11:49.74 timestamp    message 
02:11:49.74 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56320, unflushed_frees 38912, appended 160 bytes
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 112 bytes
02:11:49.74 1678327909   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 250) (bptree, mintxg=1)
02:11:49.74 1678327909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:49.74 1678327909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50176, unflushed_frees 40960, appended 144 bytes
02:11:49.74 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:49.74 1678327909   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 335)  
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 56320, appended 128 bytes
02:11:49.74 1678327909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:49.74 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 112 bytes
02:11:49.74 1678327909   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 335) mountpoint=/var/tmp/testdir
02:11:49.74 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 60928, appended 184 bytes
02:11:49.76 =================================================================
02:11:49.76  End of zfs_dbgmsg log
02:11:49.76 =================================================================
02:11:49.76 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:49.76 =================================================================
02:11:49.76  Tailing last 200 lines of dmesg log
02:11:49.76 =================================================================
02:11:49.77 [ 1398.883649] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:49.77 =================================================================
02:11:49.77  End of dmesg log
02:11:49.77 =================================================================
02:11:49.77 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:49.77 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:49.88 SUCCESS: zfs destroy -f testpool/testfs
02:11:49.88 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
02:11:52.70 ASSERTION: CM-not-UN FS: CI lookup succeeds only if (norm=same)
02:11:52.75 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:52.80 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.80 SUCCESS: create_file FïLëNÄmë
02:11:52.81 SUCCESS: lookup_file_ci FïLëNÄmë
02:11:52.81 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:11:52.81 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:52.81 =================================================================
02:11:52.81  Tailing last 200 lines of zfs_dbgmsg log
02:11:52.81 =================================================================
02:11:52.82 timestamp    message 
02:11:52.82 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 57344, unflushed_frees 38912, appended 128 bytes
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 27648, appended 88 bytes
02:11:52.82 1678327909   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 335) (bptree, mintxg=1)
02:11:52.82 1678327909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 42496, appended 128 bytes
02:11:52.82 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327909   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 344)  
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 57344, appended 184 bytes
02:11:52.82 1678327909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 38912, appended 112 bytes
02:11:52.82 1678327909   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 344) mountpoint=/var/tmp/testdir
02:11:52.82 1678327909   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 200 bytes
02:11:52.82 1678327910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40448, appended 208 bytes
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 104 bytes
02:11:52.82 1678327910   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 344) (bptree, mintxg=1)
02:11:52.82 1678327910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 43520, appended 136 bytes
02:11:52.82 1678327910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327910   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 402)  
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 58368, appended 152 bytes
02:11:52.82 1678327910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 39424, appended 120 bytes
02:11:52.82 1678327910   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 402) mountpoint=/var/tmp/testdir
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 62976, appended 192 bytes
02:11:52.82 1678327910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40960, appended 144 bytes
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28672, appended 88 bytes
02:11:52.82 1678327910   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 402) (bptree, mintxg=1)
02:11:52.82 1678327910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:11:52.82 1678327910   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 43008, appended 128 bytes
02:11:52.82 1678327911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327911   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 413)  
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
02:11:52.82 1678327911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 39936, appended 112 bytes
02:11:52.82 1678327911   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 413) mountpoint=/var/tmp/testdir
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 62976, appended 208 bytes
02:11:52.82 1678327911   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 59904, unflushed_frees 41472, appended 152 bytes
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:52.82 1678327911   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 413) (bptree, mintxg=1)
02:11:52.82 1678327911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 45056, appended 136 bytes
02:11:52.82 1678327911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327911   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 357)  
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 59904, appended 152 bytes
02:11:52.82 1678327911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41472, appended 128 bytes
02:11:52.82 1678327911   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 357) mountpoint=/var/tmp/testdir
02:11:52.82 1678327911   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 65024, appended 208 bytes
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 59904, unflushed_frees 42496, appended 152 bytes
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 30208, appended 112 bytes
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 357) (bptree, mintxg=1)
02:11:52.82 1678327912   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327912   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 45056, appended 144 bytes
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 427)  
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 59904, appended 192 bytes
02:11:52.82 1678327912   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 40960, appended 128 bytes
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 427) mountpoint=/var/tmp/testdir
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 64000, appended 200 bytes
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 43520, appended 192 bytes
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 31744, appended 112 bytes
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 427) (bptree, mintxg=1)
02:11:52.82 1678327912   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:52.82 1678327912   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 136 bytes
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 373)  
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 60928, appended 144 bytes
02:11:52.82 1678327912   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:52.82 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 42496, appended 136 bytes
02:11:52.82 1678327912   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 373) mountpoint=/var/tmp/testdir
02:11:52.82 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 66048, appended 208 bytes
02:11:52.83 =================================================================
02:11:52.83  End of zfs_dbgmsg log
02:11:52.83 =================================================================
02:11:52.83 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:52.83 =================================================================
02:11:52.83  Tailing last 200 lines of dmesg log
02:11:52.83 =================================================================
02:11:52.84 [ 1399.200935] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:11:52.84 [ 1399.616060] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:11:52.84 [ 1400.294868] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:11:52.84 [ 1400.714238] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:11:52.84 [ 1401.431822] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:11:52.84 [ 1401.992923] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:11:52.84 =================================================================
02:11:52.84  End of dmesg log
02:11:52.84 =================================================================
02:11:52.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:52.84 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:52.95 SUCCESS: zfs destroy -f testpool/testfs
02:11:52.95 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
02:11:53.46 ASSERTION: CM-UN FS: lookup succeeds if (case=same)
02:11:53.51 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:53.55 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:53.56 SUCCESS: create_file FïLëNÄmë
02:11:53.56 SUCCESS: lookup_file FïLëNÄmë
02:11:53.57 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:53.57 SUCCESS: lookup_file fïlënämë exited 1
02:11:53.57 SUCCESS: lookup_file FïLëNÄmë
02:11:53.58 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:53.58 SUCCESS: lookup_file fïlënämë exited 1
02:11:53.59 SUCCESS: create_file FÏLËNÄMË
02:11:53.59 SUCCESS: lookup_file FïLëNÄmë exited 1
02:11:53.59 SUCCESS: lookup_file FÏLËNÄMË
02:11:53.60 SUCCESS: lookup_file fïlënämë exited 1
02:11:53.60 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:11:53.60 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:53.61 =================================================================
02:11:53.61  Tailing last 200 lines of zfs_dbgmsg log
02:11:53.61 =================================================================
02:11:53.61 timestamp    message 
02:11:53.61 1678327912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:53.61 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44544, appended 160 bytes
02:11:53.61 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 31744, appended 104 bytes
02:11:53.61 1678327912   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 373) (bptree, mintxg=1)
02:11:53.61 1678327912   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:53.61 1678327912   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:11:53.61 1678327912   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 46592, appended 144 bytes
02:11:53.61 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:53.61 1678327913   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 440)  
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 61440, appended 176 bytes
02:11:53.61 1678327913   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:53.61 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 42496, appended 120 bytes
02:11:53.61 1678327913   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 440) mountpoint=/var/tmp/testdir
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 65536, appended 200 bytes
02:11:53.61 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61952, unflushed_frees 44544, appended 168 bytes
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 32768, appended 112 bytes
02:11:53.61 1678327913   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 440) (bptree, mintxg=1)
02:11:53.61 1678327913   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:53.61 1678327913   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 47104, appended 136 bytes
02:11:53.61 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:53.61 1678327913   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 514)  
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 61952, appended 184 bytes
02:11:53.61 1678327913   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:53.61 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 43008, appended 128 bytes
02:11:53.61 1678327913   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 514) mountpoint=/var/tmp/testdir
02:11:53.61 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 66560, appended 216 bytes
02:11:53.62 =================================================================
02:11:53.62  End of zfs_dbgmsg log
02:11:53.62 =================================================================
02:11:53.62 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:53.62 =================================================================
02:11:53.62  Tailing last 200 lines of dmesg log
02:11:53.62 =================================================================
02:11:53.63 [ 1402.269960] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:11:53.63 [ 1402.748082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:11:53.63 =================================================================
02:11:53.63  End of dmesg log
02:11:53.63 =================================================================
02:11:53.63 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:53.63 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:53.74 SUCCESS: zfs destroy -f testpool/testfs
02:11:53.75 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
02:11:53.78 ASSERTION: CM-UN FS: CI lookup succeeds using any name form
02:11:53.82 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:53.88 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:53.88 SUCCESS: create_file FïLëNÄmë
02:11:53.88 SUCCESS: lookup_file_ci FïLëNÄmë
02:11:53.89 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:11:53.89 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:53.89 =================================================================
02:11:53.89  Tailing last 200 lines of zfs_dbgmsg log
02:11:53.89 =================================================================
02:11:53.90 timestamp    message 
02:11:53.90 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 64000, unflushed_frees 45056, appended 200 bytes
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 35328, appended 120 bytes
02:11:53.90 1678327913   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 514) (bptree, mintxg=1)
02:11:53.90 1678327913   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:53.90 1678327913   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 49152, appended 168 bytes
02:11:53.90 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:53.90 1678327913   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 525)  
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 64000, appended 152 bytes
02:11:53.90 1678327913   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:53.90 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 45056, appended 136 bytes
02:11:53.90 1678327913   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 525) mountpoint=/var/tmp/testdir
02:11:53.90 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59392, unflushed_frees 68608, appended 216 bytes
02:11:53.91 =================================================================
02:11:53.91  End of zfs_dbgmsg log
02:11:53.91 =================================================================
02:11:53.91 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:53.91 =================================================================
02:11:53.91  Tailing last 200 lines of dmesg log
02:11:53.91 =================================================================
02:11:53.92 [ 1403.065485] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
02:11:53.92 =================================================================
02:11:53.92  End of dmesg log
02:11:53.92 =================================================================
02:11:53.92 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:53.92 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:54.02 SUCCESS: zfs destroy -f testpool/testfs
02:11:54.03 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
02:11:54.06 ASSERTION: CM-UN FS: delete succeeds if (case=same)
02:11:54.11 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:54.16 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:54.16 SUCCESS: create_file FïLëNÄmë
02:11:54.17 SUCCESS: delete_file FïLëNÄmë
02:11:54.17 SUCCESS: lookup_any exited 1
02:11:54.17 SUCCESS: create_file FïLëNÄmë
02:11:54.18 SUCCESS: delete_file FÏLËNÄMË exited 1
02:11:54.19 SUCCESS: create_file FïLëNÄmë
02:11:54.19 SUCCESS: delete_file fïlënämë exited 1
02:11:54.20 SUCCESS: create_file FïLëNÄmë
02:11:54.20 ERROR: delete_file FïLëNÄmë exited 1
02:11:54.20 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:54.20 =================================================================
02:11:54.20  Tailing last 200 lines of zfs_dbgmsg log
02:11:54.20 =================================================================
02:11:54.21 timestamp    message 
02:11:54.21 1678327913   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:54.21 1678327913   metaslab.c:3926:metaslab_flush(): flushing: txg 169, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 64000, unflushed_frees 46592, appended 152 bytes
02:11:54.21 1678327914   metaslab.c:3926:metaslab_flush(): flushing: txg 170, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 34304, appended 120 bytes
02:11:54.21 1678327914   spa_history.c:297:spa_history_log_sync(): txg 171 destroy testpool/testfs (id 525) (bptree, mintxg=1)
02:11:54.21 1678327914   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:54.21 1678327914   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 171; err=0
02:11:54.21 1678327914   metaslab.c:3926:metaslab_flush(): flushing: txg 171, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 48640, appended 144 bytes
02:11:54.21 1678327914   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:54.21 1678327914   spa_history.c:297:spa_history_log_sync(): txg 172 create testpool/testfs (id 456)  
02:11:54.21 1678327914   metaslab.c:3926:metaslab_flush(): flushing: txg 172, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 64000, appended 152 bytes
02:11:54.21 1678327914   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:54.21 1678327914   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:54.21 1678327914   metaslab.c:3926:metaslab_flush(): flushing: txg 173, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 45056, appended 136 bytes
02:11:54.21 1678327914   spa_history.c:297:spa_history_log_sync(): txg 174 set testpool/testfs (id 456) mountpoint=/var/tmp/testdir
02:11:54.21 1678327914   metaslab.c:3926:metaslab_flush(): flushing: txg 174, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 67584, appended 216 bytes
02:11:54.22 =================================================================
02:11:54.22  End of zfs_dbgmsg log
02:11:54.22 =================================================================
02:11:54.22 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:54.22 =================================================================
02:11:54.22  Tailing last 200 lines of dmesg log
02:11:54.22 =================================================================
02:11:54.23 [ 1403.346537] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete
02:11:54.23 =================================================================
02:11:54.23  End of dmesg log
02:11:54.23 =================================================================
02:11:54.23 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:54.23 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:54.34 SUCCESS: zfs destroy -f testpool/testfs
02:11:54.34 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:11] [FAIL]
02:33:00.16 SUCCESS: zpool create -f testpool mirror loop0 loop1
02:33:00.16 ASSERTION: Per-vdev ZAPs persist correctly on the original pool after split.
02:33:02.74 SUCCESS: eval zdb -PC testpool > /var/tmp/testdir/vz007
02:33:02.75 SUCCESS: grep -q com.delphix:has_per_vdev_zaps /var/tmp/testdir/vz007
02:33:10.60 SUCCESS: zpool split testpool testpool2 loop1
02:33:10.76 ERROR: eval zdb -PC testpool > /var/tmp/testdir/vz007 exited 2
02:33:10.77 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:33:10.77 =================================================================
02:33:10.77  Tailing last 200 lines of zfs_dbgmsg log
02:33:10.77 =================================================================
02:33:10.77 1678329168   spa.c:8409:spa_async_request(): spa=$import async request task=2048
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADED
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): UNLOADING
02:33:10.77 1678329168   spa.c:6291:spa_tryimport(): spa_tryimport: importing testpool
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADING
02:33:10.77 1678329168   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa $import. txg 22
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=22
02:33:10.77 1678329168   spa.c:8409:spa_async_request(): spa=$import async request task=2048
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADED
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): UNLOADING
02:33:10.77 1678329168   spa.c:6143:spa_import(): spa_import: importing testpool
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): LOADING
02:33:10.77 1678329168   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa testpool. txg 22
02:33:10.77 1678329168   spa_misc.c:416:spa_load_note(): spa_load(testpool, config untrusted): using uberblock with txg=22
02:33:10.77 1678329169   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): read 1 log space maps (1 total blocks - blksz = 131072 bytes) in 0 ms
02:33:10.77 1678329169   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2458376379400
02:33:10.77 1678329169   spa.c:8409:spa_async_request(): spa=testpool async request task=1
02:33:10.77 1678329169   spa.c:8409:spa_async_request(): spa=testpool async request task=2048
02:33:10.77 1678329169   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): LOADED
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458377 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458377 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458377 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   spa_history.c:306:spa_history_log_sync(): txg 24 open pool version 5000; software version 99363f5; uts fv-az208-825 5.15.0-1033-azure #40~20.04.1-Ubuntu SMP Tue Jan 24 16:06:28 UTC 2023 x86_64
02:33:10.77 1678329169   metaslab.c:3926:metaslab_flush(): flushing: txg 24, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 10240, unflushed_frees 28160, appended 72 bytes
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 0, smp_length 216, unflushed_allocs 0, unflushed_frees 9728, freed 0, defer 9728 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268160512, max size error 268144128, old_weight 6c0000000000001, new_weight 6c0000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 1, smp_length 144, unflushed_allocs 3072, unflushed_frees 30720, freed 0, defer 9728 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268160512, max size error 268144128, old_weight 6c0000000000001, new_weight 6c0000000000001
02:33:10.77 1678329169   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 2, smp_length 128, unflushed_allocs 3072, unflushed_frees 30720, freed 0, defer 9728 + 0, unloaded time 2458383 ms, loading_time 0 ms, ms_max_size 268180480, max size error 268164096, old_weight 6c0000000000001, new_weight 6c0000000000001
02:33:10.77 1678329169   spa.c:8409:spa_async_request(): spa=testpool async request task=32
02:33:10.77 1678329169   spa_history.c:306:spa_history_log_sync(): txg 26 import pool version 5000; software version 99363f5; uts fv-az208-825 5.15.0-1033-azure #40~20.04.1-Ubuntu SMP Tue Jan 24 16:06:28 UTC 2023 x86_64
02:33:10.77 1678329169   metaslab.c:3926:metaslab_flush(): flushing: txg 26, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 3072, unflushed_frees 30720, appended 88 bytes
02:33:10.77 1678329171   spa_history.c:293:spa_history_log_sync(): command: zpool import testpool
02:33:10.77 1678329171   metaslab.c:3926:metaslab_flush(): flushing: txg 28, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 2048, unflushed_frees 30720, appended 80 bytes
02:33:10.77 1678329171   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
02:33:10.77 1678329171   metaslab.c:3926:metaslab_flush(): flushing: txg 29, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 12800, appended 32 bytes
02:33:10.77 1678329171   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
02:33:10.77 1678329171   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 3, unflushed_allocs 17408, unflushed_frees 0, appended 56 bytes
02:33:10.77 1678329171   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2461017385500
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 99363f5; uts fv-az208-825 5.15.0-1033-azure #40~20.04.1-Ubuntu SMP Tue Jan 24 16:06:28 UTC 2023 x86_64
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
02:33:10.77 1678329171   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
02:33:10.77 1678329171   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2461195691300
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461195 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461195 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461198 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461206 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329171   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 34816, unflushed_frees 0, appended 24 bytes
02:33:10.77 1678329172   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool loop0
02:33:10.77 1678329172   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 0, appended 64 bytes
02:33:10.77 1678329172   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 0, appended 64 bytes
02:33:10.77 1678329172   metaslab.c:3926:metaslab_flush(): flushing: txg 10, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 17408, appended 104 bytes
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329172   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2461381 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329177   spa_history.c:293:spa_history_log_sync(): command: zpool add -f testpool loop1
02:33:10.77 1678329177   metaslab.c:3926:metaslab_flush(): flushing: txg 11, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 15872, unflushed_frees 12800, appended 72 bytes
02:33:10.77 1678329177   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 11, spa testpool, vdev_id 1, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2466562 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329179   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
02:33:10.77 1678329179   metaslab.c:3926:metaslab_flush(): flushing: txg 13, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 5120, unflushed_frees 14848, appended 64 bytes
02:33:10.77 1678329179   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
02:33:10.77 1678329179   metaslab.c:3926:metaslab_flush(): flushing: txg 22, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 17408, unflushed_frees 15872, appended 88 bytes
02:33:10.77 1678329179   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2469170075000
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 99363f5; uts fv-az208-825 5.15.0-1033-azure #40~20.04.1-Ubuntu SMP Tue Jan 24 16:06:28 UTC 2023 x86_64
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
02:33:10.77 1678329180   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
02:33:10.77 1678329180   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2469486173200
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469486 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469486 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469487 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2469497 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329180   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 33792, unflushed_frees 0, appended 32 bytes
02:33:10.77 1678329180   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool mirror loop0 loop1
02:33:10.77 1678329180   metaslab.c:3926:metaslab_flush(): flushing: txg 6, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 0, appended 64 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 13, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 0, appended 72 bytes
02:33:10.77 1678329190   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': txg 13, spa testpool, DTL old object 0, new object 76
02:33:10.77 1678329190   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): LOADING
02:33:10.77 1678329190   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': best uberblock found for spa testpool2. txg 6
02:33:10.77 1678329190   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): using uberblock with txg=6
02:33:10.77 1678329190   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from cabe0e05e91ef6 to fb2b6c492e0b30 for pool testpool2 dataset id 48
02:33:10.77 1678329190   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): read 3 log space maps (3 total blocks - blksz = 131072 bytes) in 0 ms
02:33:10.77 1678329190   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 91e85eef2b83d4 to 790cee90a6861 for pool testpool2 dataset id 54
02:33:10.77 1678329190   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 91e85eef2b83d4 to da15d73cc905ba for pool testpool2 dataset id 54
02:33:10.77 1678329190   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 91e85eef2b83d4 to f719681d3c4171 for pool testpool2 dataset id 54
02:33:10.77 1678329190   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool2' gethrtime 2479914659200
02:33:10.77 1678329190   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2479914 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329190   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2479914 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329190   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2479915 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 7, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 0, appended 72 bytes
02:33:10.77 1678329190   spa.c:8409:spa_async_request(): spa=testpool2 async request task=1
02:33:10.77 1678329190   spa.c:8409:spa_async_request(): spa=testpool2 async request task=2048
02:33:10.77 1678329190   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): LOADED
02:33:10.77 1678329190   spa_history.c:306:spa_history_log_sync(): txg 8 open pool version 5000; software version 99363f5; uts fv-az208-825 5.15.0-1033-azure #40~20.04.1-Ubuntu SMP Tue Jan 24 16:06:28 UTC 2023 x86_64
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 13824, unflushed_frees 20992, appended 112 bytes
02:33:10.77 1678329190   spa_history.c:306:spa_history_log_sync(): txg 14 detach vdev=/dev/loop1
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 16384, appended 112 bytes
02:33:10.77 1678329190   spa_history.c:306:spa_history_log_sync(): txg 9 split from pool testpool
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 2048, unflushed_frees 17920, appended 80 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 0, unflushed_frees 19456, appended 56 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 3, unflushed_allocs 20992, unflushed_frees 0, appended 48 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 4, unflushed_allocs 20992, unflushed_frees 0, appended 48 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 5, unflushed_allocs 20480, unflushed_frees 0, appended 48 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 6656, appended 40 bytes
02:33:10.77 1678329190   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
02:33:10.77 1678329190   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): UNLOADING
02:33:10.77 1678329190   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool2' gethrtime 2479954177400
02:33:10.78 =================================================================
02:33:10.78  End of zfs_dbgmsg log
02:33:10.78 =================================================================
02:33:10.78 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:33:10.78 =================================================================
02:33:10.78  Tailing last 200 lines of dmesg log
02:33:10.78 =================================================================
02:33:10.79 [ 2371.919626] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos
02:33:10.79 [ 2372.437025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos
02:33:10.79 [ 2372.847637] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos
02:33:10.79 [ 2373.721141] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg
02:33:10.79 [ 2374.033032] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos
02:33:10.79 [ 2375.422432] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos
02:33:10.79 [ 2377.417445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted
02:33:10.79 [ 2380.670990] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted
02:33:10.79 [ 2388.176765] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709
02:33:10.79 [ 2389.287213] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
02:33:10.79 [ 2389.992581] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/setup
02:33:10.79 [ 2396.091723] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos
02:33:10.79 [ 2397.298096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos
02:33:10.79 [ 2398.270058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos
02:33:10.79 [ 2398.991640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos
02:33:10.79 [ 2399.719095] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos
02:33:10.79 [ 2400.609696] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
02:33:10.79 [ 2401.301681] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup
02:33:10.79 [ 2401.327770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos
02:33:10.79 [ 2409.221817] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos
02:33:10.79 [ 2428.066645] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos
02:33:10.79 [ 2441.620085] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos
02:33:10.79 [ 2450.395916] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos
02:33:10.79 [ 2461.475106] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos
02:33:10.79 [ 2469.651945] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos
02:33:10.79 =================================================================
02:33:10.79  End of dmesg log
02:33:10.79 =================================================================
02:33:10.79 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:33:10.79 NOTE: Performing local cleanup via log_onexit (cleanup)
02:33:10.85 SUCCESS: zpool destroy -f testpool
02:33:10.86 SUCCESS: rm -f /var/tmp/testdir/vz007
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_002_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_006_pos (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_pos (run as root) [02:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_block_size_histogram (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_checksum (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_display_block (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_encrypted (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_neg (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_pos (run as root) [00:53] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_objset_id (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress_zstd (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover_2 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_010_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_deeply_nested (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_003_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_004_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_006_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_008_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_010_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_crypt_combos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_dryrun (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_nomount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_verbose (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_and_disable (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_races (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_dedup (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_001_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_005_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_013_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_015_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_016_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_clone_livelist (run as root) [01:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_changes (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_timestamp (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_types (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_mangle (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_001_pos (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_002_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_005_neg (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_008_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_009_pos (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/zfs_ids_to_path_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_002_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_location (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_noop (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_recursive (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_fail (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_mountpoints (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_test_race (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/zfs_program_json (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_encryptionroot (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/zfs_written_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_override (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_aliases (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-wR-encrypted-mix (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_corrective (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_compressed_corrective (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_002_pos (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_014_neg (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_encrypted_child (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_to_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_nounmount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_001_pos (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_007_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_sparse (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send-b (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_skip_missing (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/checksum_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/compression_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/reservation_001_neg (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/share_mount_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/snapdir_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/onoffs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_001_neg (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/ro_props_001_pos (run as root) [01:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_concurrent_shares (run as root) [01:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_005_neg (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_009_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_006_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_all_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_nested (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_002_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_004_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_005_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_getsubopt (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zhack/zhack_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_colors (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add-o_ashift (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_prop_ashift (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/attach-o_ashift (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_readonly (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_005_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_014_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_023_neg (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_024_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_crypt_combos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos (run as root) [02:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift (run as root) [00:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_cliargs (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_errors (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_duplicates (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear_retained (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg (run as root) [01:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos (run as root) [00:44] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4 (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed (run as root) [01:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_attach_detach_add_remove (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_fault_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_import_export (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_split (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_suspend_resume (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_unsupported_vdevs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_checksums (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_initialized (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace-o_ashift (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace_prop_ashift (run as root) [01:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_restart (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_encrypted_unloaded (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_print_repairing (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_multiple_copies (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_encryption (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_resilver (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_features_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_001_pos (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_002_pos (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_004_pos (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_007_pos (run as root) [00:53] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_008_pos (run as root) [01:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_discard (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_freeing (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_multiple (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove_cancel (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_basic (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace_cancel (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_rebuild (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_resilver (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_basic (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos (run as root) [02:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/file_append (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive (run as root) [03:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/setup (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.args_to_lua (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.divide_by_zero (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.exists (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.integer_illegal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.integer_overflow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.language_functions_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.language_functions_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.large_prog (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.libraries (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.memory_limit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nested_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nested_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nvlist_to_lua (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.recursive_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.recursive_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_large (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_nvlist_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_nvlist_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_recursive_table (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.stack_gsub (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.timeout (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.destroy_fs (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.destroy_snap (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_count_and_limit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_index_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_number_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_string_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_type (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_userquota (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_written (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.inherit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_bookmarks (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_children (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_clones (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_holds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_snapshots (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_system_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_user_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.parse_args_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_conflict (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_multiple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_simple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.rollback_mult (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.rollback_one (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.set_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_destroy (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_recursive (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_simple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.bookmark.create (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.bookmark.copy (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.terminate_by_signal (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_edonr_test (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_sha2_test (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_skein_test (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_blake3_test (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_001_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_002_pos (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_004_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/setup (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zdb_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_allow_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_clone_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_create_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_destroy_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_get_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_inherit_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_mount_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_promote_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_receive_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_rename_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_rollback_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_send_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_set_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_share_001_neg (run as runner) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_snapshot_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_unallow_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_unmount_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_unshare_001_neg (run as runner) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_upgrade_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_add_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_attach_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_clear_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_create_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_destroy_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_detach_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_export_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_get_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_history_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_import_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_import_002_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_offline_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_online_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_remove_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_replace_001_neg (run as runner) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_scrub_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_set_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_status_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_upgrade_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arcstat_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arc_summary_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arc_summary_002_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_wait_privilege (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zilstat_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/setup (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_001_pos (run as runner) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_002_pos (run as runner) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_003_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_004_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_005_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_007_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_008_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_002_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_003_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_004_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_005_pos (run as runner) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_disable (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_homedir (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_searchpath (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/zpool_list_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/zpool_list_002_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/zpool_status_003_pos (run as runner) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/zpool_status_-c_disable (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/zpool_status_-c_homedir (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/zpool_status_-c_searchpath (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_001_pos (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_002_pos (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc_disabled (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted_no_compressed_arc (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cp_files_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/crtime_001_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/ctime_001_pos (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_ratelimit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_sync (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_zio (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/setup (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_002_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_003_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_004_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_005_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_007_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_010_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_011_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_012_neg (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_007_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_008_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_punch-hole (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/async_destroy_001_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_001_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_009_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_002_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_003_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_010_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/inherit_001_pos (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_008_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_009_pos (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/sync (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/psync (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/posixaio (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/mmap (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_limit (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_001 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_root_inode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/log_spacemap/log_spacemap_import_logs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_mixed (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_seek_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_sync_001_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_write_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [01:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [01:59] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [02:57] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [02:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_invalid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_lun_expsz (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_open (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_rewind (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_ro_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_vdev_add (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zdb (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zhack_feat (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_001_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_002_neg (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_007_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_008_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_012_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_013_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_019_pos (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_020_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_021_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_022_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_024_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_025_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_026_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_027_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_028_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_029_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_030_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_ratio (run as root) [00:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_props (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_incremental (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstream_recompress (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_lz4_disabled (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_lz4_disabled (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_mixed_compression (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_stream_size_estimate (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_embedded_blocks (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_resume (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-cpL_varied_recsize (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_incremental (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_files (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_encrypted_files (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_spill_block (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_hole_birth (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_doall (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_spill_block (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_ashift (run as root) [01:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_large_blocks (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_001_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_002_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_003_pos (run as root) [01:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_004_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_005_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_006_pos (run as root) [04:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_007_pos (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_011_neg (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_012_neg (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_014_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_015_neg (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_001 (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_002 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_volume (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_016_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/clone_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/sparse_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/stat_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_none (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_zil_replay (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_integrity (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_config (run as root) [00:59] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_trim_integrity (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_integrity (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_config (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_l2arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_timestamps (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_userobj_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_readonly_pool (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_007_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709 (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:11] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_002_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_012_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_compat (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/zpool_influxdb (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/zvol_ENOSPC_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_hierarchy (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_rename_inuse (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_snapdev (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_trim (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_volmode (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_zil (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/zvol_stress (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Summary for Logs-22.04-functional
<pre>

Tests with results other than PASS that are expected:
    FAIL cli_root/zpool_import/import_rewind_device_replaced (Arbitrary pool rewind is not guaranteed)
    SKIP cli_root/zpool_import/zpool_import_missing_003_pos (https://github.com/openzfs/zfs/issues/6839)
    SKIP rsend/rsend_008_pos (https://github.com/openzfs/zfs/issues/6066)
    FAIL vdev_zaps/vdev_zaps_007_pos (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
02:55:08.93 SUCCESS: set_tunable32 TXG_HISTORY 100
02:55:08.93 SUCCESS: mkdir -p /var/tmp/bakdev_import-test
02:55:08.94 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk0
02:55:08.94 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk1
02:55:08.94 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk2
02:55:08.95 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk3
02:55:08.95 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk4
02:55:08.95 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk5
02:55:08.95 NOTE: test_replace_vdev: pool '/var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1', replace /var/tmp/dev_import-test/disk1 by /var/tmp/dev_import-test/disk2.
02:55:09.01 SUCCESS: zpool create testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:55:09.05 SUCCESS: zfs create testpool1/ds1
02:55:09.13 SUCCESS: zpool sync testpool1
02:55:09.17 SUCCESS: zfs create testpool1/ds2
02:55:09.25 SUCCESS: zpool sync testpool1
02:55:09.29 SUCCESS: zfs create testpool1/ds3
02:55:09.38 SUCCESS: zpool sync testpool1
02:55:09.38 SUCCESS: generate_data testpool1 /var/tmp/md5sums.668945
02:55:10.29 SUCCESS: write_some_data testpool1 15
02:55:10.33 SUCCESS: zpool sync testpool1
02:55:10.36 SUCCESS: zpool sync testpool1
02:55:10.38 SUCCESS: zpool sync testpool1
02:55:10.41 SUCCESS: zpool sync testpool1
02:55:10.44 SUCCESS: zpool sync testpool1
02:55:10.47 SUCCESS: zpool sync testpool1
02:55:10.50 SUCCESS: zpool sync testpool1
02:55:10.53 SUCCESS: zpool sync testpool1
02:55:10.56 SUCCESS: zpool sync testpool1
02:55:10.59 SUCCESS: zpool sync testpool1
02:55:10.62 SUCCESS: zpool sync testpool1
02:55:10.62 SUCCESS: sync_some_data_a_few_times testpool1
02:55:13.47 SUCCESS: zfs snapshot -r testpool1@snap1
02:55:13.56 SUCCESS: overwrite_data testpool1 
02:55:13.66 SUCCESS: zpool export testpool1
02:55:13.85 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:55:13.85 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 1
02:55:13.91 SUCCESS: zpool replace testpool1 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk2
02:55:13.93 SUCCESS: pool_is_replacing testpool1
02:55:20.08 SUCCESS: zpool export testpool1
02:55:20.08 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:55:20.29 SUCCESS: zpool import -d /var/tmp/dev_import-test -o readonly=on -T 53 testpool1
02:55:20.33 SUCCESS: check_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:55:20.41 SUCCESS: verify_data_md5sums /var/tmp/md5sums.668945
02:55:20.44 SUCCESS: zpool export testpool1
02:55:21.03 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:55:21.12 SUCCESS: overwrite_data testpool1 
02:55:24.22 SUCCESS: wait_for_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk2
02:55:24.28 SUCCESS: zpool export testpool1
02:55:24.28 SUCCESS: mv /var/tmp/dev_import-test/disk2 /var/tmp/bakdev_import-test/
02:55:24.65 cannot import 'testpool1': one or more devices is currently unavailable
02:55:24.65 ERROR: zpool import -d /var/tmp/dev_import-test -T 53 testpool1 exited 1
02:55:24.65 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:55:24.66 =================================================================
02:55:24.66  Tailing last 200 lines of zfs_dbgmsg log
02:55:24.66 =================================================================
02:55:24.67 1678330524   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 1, unflushed_allocs 2048, unflushed_frees 1024, appended 40 bytes
02:55:24.67 1678330524   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 3, unflushed_allocs 4608, unflushed_frees 4608, appended 64 bytes
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): UNLOADING
02:55:24.67 1678330524   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool1' gethrtime 3832906735300
02:55:24.67 1678330524   spa.c:6288:spa_tryimport(): spa_tryimport: importing testpool1, max_txg=53
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa $import. txg 53
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=53
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load($import, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): UNLOADING
02:55:24.67 1678330524   spa.c:6145:spa_import(): spa_import: importing testpool1, max_txg=53 (RECOVERY MODE)
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 53
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=53
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 52
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 50
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 50)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=50
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 49
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 47
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 47)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=47
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 46
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 44
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 44)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=44
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 43
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 41
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 41)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=41
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 40
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 38
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 38)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=38
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 37
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 35
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 35)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=35
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 34
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 32
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 32)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=32
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 31
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 29
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 29)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=29
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 28
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 26
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 26)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=26
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 25
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 23
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 23)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=23
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 22
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 22
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 22)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=22
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 21
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 21
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 21)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=21
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 20
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 20
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 20)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=20
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 19
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 17
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 17)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=17
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 16
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 16
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 16)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=16
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 15
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 13
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 13)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=13
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 12
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 12
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 12)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=12
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 11
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 9
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 9)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=9
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 8
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 8
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 8)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=8
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 7
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 6
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 6)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=6
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 5
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 5
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 5)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=5
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 4
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 4
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 4)
02:55:24.67 1678330524   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=4
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 3
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:55:24.67 1678330524   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: no valid uberblock found
02:55:24.67 1678330524   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:55:24.68 =================================================================
02:55:24.68  End of zfs_dbgmsg log
02:55:24.68 =================================================================
02:55:24.68 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:55:24.68 =================================================================
02:55:24.68  Tailing last 200 lines of dmesg log
02:55:24.68 =================================================================
02:55:24.69 [ 3219.787845] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg
02:55:24.69 [ 3219.920173] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos
02:55:24.69 [ 3221.313277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup
02:55:24.69 [ 3221.375588] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup
02:55:24.69 [ 3221.662988] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos
02:55:24.69 [ 3221.707509] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos
02:55:24.69 [ 3221.961319] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos
02:55:24.69 [ 3223.196825] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg
02:55:24.69 [ 3223.244871] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos
02:55:24.69 [ 3223.430075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup
02:55:24.69 [ 3223.649950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup
02:55:24.69 [ 3224.100771] debugfs: Directory 'zd0' with parent 'block' already present!
02:55:24.69 [ 3224.494929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg
02:55:24.69 [ 3224.809926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos
02:55:24.69 [ 3224.977312] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup
02:55:24.69 [ 3225.195055] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup
02:55:24.69 [ 3225.501936] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos
02:55:24.69 [ 3233.827173] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos
02:55:24.69 [ 3243.072127] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos
02:55:24.69 [ 3243.702122] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos
02:55:24.69 [ 3253.158877] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos
02:55:24.69 [ 3264.554700] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos
02:55:24.69 [ 3275.943398] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos
02:55:24.69 [ 3288.398279] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos
02:55:24.69 [ 3301.947440] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg
02:55:24.69 [ 3309.191029] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos
02:55:24.69 [ 3313.903149] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg
02:55:24.69 [ 3322.551804] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos
02:55:24.69 [ 3352.317144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg
02:55:24.69 [ 3424.684494] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos
02:55:24.69 [ 3428.299107] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos
02:55:24.69 [ 3433.569280] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos
02:55:24.69 [ 3441.890084] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos
02:55:24.69 [ 3456.186125] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos
02:55:24.69 [ 3470.377217] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg
02:55:24.69 [ 3490.045370] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos
02:55:24.69 [ 3509.919573] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos
02:55:24.69 [ 3556.549992] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos
02:55:24.69 [ 3617.658182] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos
02:55:24.69 [ 3617.694829] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos
02:55:24.69 [ 3626.709710] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos
02:55:24.69 [ 3630.047074] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted
02:55:24.69 [ 3631.902062] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load
02:55:24.69 [ 3636.018136] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3
02:55:24.69 [ 3640.922366] debugfs: Directory 'zd0' with parent 'block' already present!
02:55:24.69 [ 3642.581564] debugfs: Directory 'zd16' with parent 'block' already present!
02:55:24.69 [ 3643.016416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4
02:55:24.69 [ 3647.685739] debugfs: Directory 'zd0' with parent 'block' already present!
02:55:24.69 [ 3650.295354] debugfs: Directory 'zd16' with parent 'block' already present!
02:55:24.69 [ 3651.345557] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added
02:55:24.69 [ 3655.631067] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed
02:55:24.69 [ 3675.951116] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced
02:55:24.69 [ 3718.607475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached
02:55:24.69 [ 3720.305998] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached
02:55:24.69 [ 3725.852785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed
02:55:24.69 [ 3730.121956] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device
02:55:24.69 [ 3732.031454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing
02:55:24.69 [ 3740.869162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed
02:55:24.69 [ 3743.848053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed
02:55:24.69 [ 3817.973121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced
02:55:24.69 =================================================================
02:55:24.69  End of dmesg log
02:55:24.69 =================================================================
02:55:24.69 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:55:24.69 NOTE: Performing local cleanup via log_onexit (custom_cleanup)
02:55:24.70 SUCCESS: set_zfs_txg_timeout 5
02:55:24.72 SUCCESS: rm -rf /var/tmp/bakdev_import-test
02:55:24.72 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:55:24.73 SUCCESS: eval zinject -c all > /dev/null
02:55:24.75 NOTE: Pool does not exist. (testpool1)
02:55:24.75 SUCCESS: rm -f /var/tmp/cachefile.668945 /var/tmp/cachefile.668945.bkp /var/tmp/cachefile.668945.bkp2 /var/tmp/md5sums.668945 /var/tmp/md5sums.668945.2
02:55:24.79 SUCCESS: rm -rf /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk3 /var/tmp/dev_import-test/disk4 /var/tmp/dev_import-test/disk5
02:55:24.79 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk0
02:55:24.79 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk1
02:55:24.79 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk2
02:55:24.80 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk3
02:55:24.80 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk4
02:55:24.80 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk5
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:14] [FAIL]
02:31:41.45 SUCCESS: zpool create -f testpool mirror loop0 loop1
02:31:41.46 ASSERTION: Per-vdev ZAPs persist correctly on the original pool after split.
02:31:45.03 SUCCESS: eval zdb -PC testpool > /var/tmp/testdir/vz007
02:31:45.03 SUCCESS: grep -q com.delphix:has_per_vdev_zaps /var/tmp/testdir/vz007
02:31:55.78 SUCCESS: zpool split testpool testpool2 loop1
02:31:55.96 ERROR: eval zdb -PC testpool > /var/tmp/testdir/vz007 exited 2
02:31:55.96 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:31:55.97 =================================================================
02:31:55.97  Tailing last 200 lines of zfs_dbgmsg log
02:31:55.97 =================================================================
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADED
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): UNLOADING
02:31:55.97 1678329086   spa.c:6291:spa_tryimport(): spa_tryimport: importing testpool
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADING
02:31:55.97 1678329086   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa $import. txg 23
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=23
02:31:55.97 1678329086   spa.c:8409:spa_async_request(): spa=$import async request task=2048
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADED
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): UNLOADING
02:31:55.97 1678329086   spa.c:6143:spa_import(): spa_import: importing testpool
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): LOADING
02:31:55.97 1678329086   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa testpool. txg 23
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load(testpool, config untrusted): using uberblock with txg=23
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): read 1 log space maps (1 total blocks - blksz = 131072 bytes) in 0 ms
02:31:55.97 1678329086   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2410880764300
02:31:55.97 1678329086   spa.c:8409:spa_async_request(): spa=testpool async request task=1
02:31:55.97 1678329086   spa.c:8409:spa_async_request(): spa=testpool async request task=2048
02:31:55.97 1678329086   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): LOADED
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410881 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410881 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410881 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   spa_history.c:306:spa_history_log_sync(): txg 25 open pool version 5000; software version 99363f5; uts fv-az341-569 5.15.0-1033-azure #40-Ubuntu SMP Mon Jan 23 20:36:59 UTC 2023 x86_64
02:31:55.97 1678329086   metaslab.c:3926:metaslab_flush(): flushing: txg 25, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 11264, unflushed_frees 13824, appended 64 bytes
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 0, smp_length 200, unflushed_allocs 0, unflushed_frees 10752, freed 0, defer 0 + 10752, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268354560, max size error 268346880, old_weight 6c0000000000001, new_weight 6c0000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 1, smp_length 128, unflushed_allocs 3072, unflushed_frees 16384, freed 0, defer 0 + 10752, unloaded time 2410887 ms, loading_time 0 ms, ms_max_size 268354560, max size error 268346880, old_weight 6c0000000000001, new_weight 6c0000000000001
02:31:55.97 1678329086   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 2, smp_length 120, unflushed_allocs 3072, unflushed_frees 16384, freed 0, defer 0 + 10752, unloaded time 2410888 ms, loading_time 0 ms, ms_max_size 268374528, max size error 268366848, old_weight 6c0000000000001, new_weight 6c0000000000001
02:31:55.97 1678329086   spa.c:8409:spa_async_request(): spa=testpool async request task=32
02:31:55.97 1678329086   spa_history.c:306:spa_history_log_sync(): txg 27 import pool version 5000; software version 99363f5; uts fv-az341-569 5.15.0-1033-azure #40-Ubuntu SMP Mon Jan 23 20:36:59 UTC 2023 x86_64
02:31:55.97 1678329086   metaslab.c:3926:metaslab_flush(): flushing: txg 27, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 3072, unflushed_frees 16384, appended 80 bytes
02:31:55.97 1678329090   spa_history.c:293:spa_history_log_sync(): command: zpool import testpool
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 29, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 2048, unflushed_frees 16384, appended 72 bytes
02:31:55.97 1678329090   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 30, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 13824, appended 32 bytes
02:31:55.97 1678329090   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 3, unflushed_allocs 17408, unflushed_frees 0, appended 56 bytes
02:31:55.97 1678329090   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2414508513900
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 99363f5; uts fv-az341-569 5.15.0-1033-azure #40-Ubuntu SMP Mon Jan 23 20:36:59 UTC 2023 x86_64
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
02:31:55.97 1678329090   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
02:31:55.97 1678329090   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2414691797500
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414692 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414692 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414693 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414703 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 34816, unflushed_frees 0, appended 24 bytes
02:31:55.97 1678329090   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool loop0
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 6, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 0, appended 56 bytes
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 0, appended 64 bytes
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 24064, unflushed_frees 17408, appended 120 bytes
02:31:55.97 1678329090   metaslab.c:3926:metaslab_flush(): flushing: txg 10, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 15872, unflushed_frees 12800, appended 104 bytes
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329090   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2414880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329095   spa_history.c:293:spa_history_log_sync(): command: zpool add -f testpool loop1
02:31:55.97 1678329095   metaslab.c:3926:metaslab_flush(): flushing: txg 11, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 14336, unflushed_frees 12800, appended 88 bytes
02:31:55.97 1678329095   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 11, spa testpool, vdev_id 1, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2419893 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
02:31:55.97 1678329101   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 17408, unflushed_frees 16384, appended 96 bytes
02:31:55.97 1678329101   spa_misc.c:416:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
02:31:55.97 1678329101   metaslab.c:3926:metaslab_flush(): flushing: txg 23, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 17408, unflushed_frees 15872, appended 104 bytes
02:31:55.97 1678329101   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2425602961800
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 99363f5; uts fv-az341-569 5.15.0-1033-azure #40-Ubuntu SMP Mon Jan 23 20:36:59 UTC 2023 x86_64
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
02:31:55.97 1678329101   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
02:31:55.97 1678329101   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2425916550600
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425916 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425916 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425917 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2425928 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329101   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 33792, unflushed_frees 0, appended 32 bytes
02:31:55.97 1678329101   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool mirror loop0 loop1
02:31:55.97 1678329101   metaslab.c:3926:metaslab_flush(): flushing: txg 6, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 0, appended 56 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 0, appended 64 bytes
02:31:55.97 1678329115   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': txg 14, spa testpool, DTL old object 0, new object 78
02:31:55.97 1678329115   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): LOADING
02:31:55.97 1678329115   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': best uberblock found for spa testpool2. txg 6
02:31:55.97 1678329115   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): using uberblock with txg=6
02:31:55.97 1678329115   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from bd48b82d0b68e6 to 3e0382b3d5e20a for pool testpool2 dataset id 48
02:31:55.97 1678329115   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): read 3 log space maps (3 total blocks - blksz = 131072 bytes) in 0 ms
02:31:55.97 1678329115   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 20b92c1c2fccb6 to 4c19a0867b168a for pool testpool2 dataset id 54
02:31:55.97 1678329115   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 20b92c1c2fccb6 to f2356be7567e27 for pool testpool2 dataset id 54
02:31:55.97 1678329115   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 20b92c1c2fccb6 to b44adeeef01367 for pool testpool2 dataset id 54
02:31:55.97 1678329115   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool2' gethrtime 2440228936600
02:31:55.97 1678329115   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2440229 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329115   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2440229 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329115   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2440229 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 7, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 0, appended 64 bytes
02:31:55.97 1678329115   spa.c:8409:spa_async_request(): spa=testpool2 async request task=1
02:31:55.97 1678329115   spa.c:8409:spa_async_request(): spa=testpool2 async request task=2048
02:31:55.97 1678329115   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): LOADED
02:31:55.97 1678329115   spa_history.c:306:spa_history_log_sync(): txg 8 open pool version 5000; software version 99363f5; uts fv-az341-569 5.15.0-1033-azure #40-Ubuntu SMP Mon Jan 23 20:36:59 UTC 2023 x86_64
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 13312, unflushed_frees 20992, appended 112 bytes
02:31:55.97 1678329115   spa_history.c:306:spa_history_log_sync(): txg 15 detach vdev=/dev/loop1
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 15, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 22016, unflushed_frees 16384, appended 120 bytes
02:31:55.97 1678329115   spa_history.c:306:spa_history_log_sync(): txg 9 split from pool testpool
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 2048, unflushed_frees 16384, appended 72 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 0, unflushed_frees 17920, appended 48 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 3, unflushed_allocs 19968, unflushed_frees 0, appended 48 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 4, unflushed_allocs 19968, unflushed_frees 0, appended 48 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 5, unflushed_allocs 19456, unflushed_frees 0, appended 48 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 6144, appended 48 bytes
02:31:55.97 1678329115   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
02:31:55.97 1678329115   spa_misc.c:416:spa_load_note(): spa_load(testpool2, config trusted): UNLOADING
02:31:55.97 1678329115   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool2' gethrtime 2440265730200
02:31:55.98 =================================================================
02:31:55.98  End of zfs_dbgmsg log
02:31:55.98 =================================================================
02:31:55.98 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:31:55.98 =================================================================
02:31:55.98  Tailing last 200 lines of dmesg log
02:31:55.98 =================================================================
02:31:55.99 [ 2290.764528] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos
02:31:55.99 [ 2291.307422] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos
02:31:55.99 [ 2291.745322] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos
02:31:55.99 [ 2292.688137] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg
02:31:55.99 [ 2293.016716] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos
02:31:55.99 [ 2296.375205] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos
02:31:55.99 [ 2299.082756] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted
02:31:55.99 [ 2305.839520] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted
02:31:55.99 [ 2316.036726] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709
02:31:55.99 [ 2318.004111] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
02:31:55.99 [ 2318.759121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/setup
02:31:55.99 [ 2323.561044] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos
02:31:55.99 [ 2324.858495] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos
02:31:55.99 [ 2325.677843] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos
02:31:55.99 [ 2326.443847] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos
02:31:55.99 [ 2327.210323] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos
02:31:55.99 [ 2328.150947] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
02:31:55.99 [ 2330.404081] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup
02:31:55.99 [ 2330.427603] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos
02:31:55.99 [ 2341.227779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos
02:31:55.99 [ 2366.949581] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos
02:31:55.99 [ 2385.356757] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos
02:31:55.99 [ 2400.004717] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos
02:31:55.99 [ 2414.982816] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos
02:31:55.99 [ 2426.103081] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos
02:31:55.99 =================================================================
02:31:55.99  End of dmesg log
02:31:55.99 =================================================================
02:31:55.99 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:31:55.99 NOTE: Performing local cleanup via log_onexit (cleanup)
02:31:56.06 SUCCESS: zpool destroy -f testpool
02:31:56.06 SUCCESS: rm -f /var/tmp/testdir/vz007
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_002_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_006_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_pos (run as root) [02:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_block_size_histogram (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_checksum (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_display_block (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_encrypted (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_neg (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_pos (run as root) [00:57] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_objset_id (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress_zstd (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover_2 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_010_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_deeply_nested (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_003_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_004_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_006_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_008_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_010_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_crypt_combos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_dryrun (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_nomount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_verbose (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_and_disable (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_races (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_dedup (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_005_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_013_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_015_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_016_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_clone_livelist (run as root) [01:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_changes (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_timestamp (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_types (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_mangle (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_001_pos (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_002_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_005_neg (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_008_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_009_pos (run as root) [01:22] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/zfs_ids_to_path_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_002_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_location (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_noop (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_recursive (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_fail (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_mountpoints (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_test_race (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/zfs_program_json (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_encryptionroot (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/zfs_written_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_property/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_override (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_aliases (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-wR-encrypted-mix (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_corrective (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_compressed_corrective (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_002_pos (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_014_neg (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_encrypted_child (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_to_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_nounmount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_001_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_007_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_sparse (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send-b (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_skip_missing (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/checksum_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/compression_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/reservation_001_neg (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/share_mount_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/snapdir_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/onoffs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_001_neg (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_002_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/ro_props_001_pos (run as root) [01:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_concurrent_shares (run as root) [01:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_005_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_009_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_all_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_nested (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_002_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_003_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_004_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_005_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_getsubopt (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zhack/zhack_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_colors (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add-o_ashift (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_prop_ashift (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/attach-o_ashift (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_readonly (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_005_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_014_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_023_neg (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_024_pos (run as root) [00:56] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_crypt_combos (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos (run as root) [04:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_cliargs (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_errors (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_duplicates (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear_retained (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg (run as root) [01:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3 (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4 (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_attach_detach_add_remove (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_fault_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_import_export (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_split (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_suspend_resume (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_unsupported_vdevs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_checksums (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_initialized (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace-o_ashift (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace_prop_ashift (run as root) [01:22] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_restart (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_encrypted_unloaded (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_print_repairing (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_multiple_copies (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_encryption (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_resilver (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_005_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_features_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_001_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_002_pos (run as root) [01:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_004_pos (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_007_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_008_pos (run as root) [01:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_discard (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_freeing (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_multiple (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove_cancel (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_basic (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace_cancel (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_rebuild (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_resilver (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_basic (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [00:53] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_limit (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_001 (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_root_inode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/log_spacemap/log_spacemap_import_logs (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_mixed (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_seek_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_sync_001_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_write_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [02:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:44] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [03:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [02:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_invalid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_lun_expsz (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_open (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_ro_rewind (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_vdev_add (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zdb (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zhack_feat (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_001_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_002_neg (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_007_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_008_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_012_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_013_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_019_pos (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_020_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_021_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_022_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_024_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_025_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_026_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_027_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_028_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_029_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_030_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_ratio (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_props (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_incremental (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstream_recompress (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_lz4_disabled (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_lz4_disabled (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_mixed_compression (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_stream_size_estimate (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_embedded_blocks (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_resume (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-cpL_varied_recsize (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_incremental (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_files (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_encrypted_files (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_spill_block (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_hole_birth (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_doall (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_spill_block (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_ashift (run as root) [01:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_large_blocks (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_001_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_002_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_003_pos (run as root) [01:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_004_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_005_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_006_pos (run as root) [04:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_007_pos (run as root) [01:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_011_neg (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_012_neg (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_014_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_015_neg (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_001 (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_002 (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_volume (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_016_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/clone_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/sparse_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/stat_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/stat/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_none (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_zil_replay (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_integrity (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_config (run as root) [00:56] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_trim_integrity (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_integrity (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_config (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_l2arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_timestamps (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_userobj_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_readonly_pool (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_002_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_004_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_007_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709 (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:14] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_002_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_012_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_compat (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/zpool_influxdb (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/zvol_ENOSPC_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_hierarchy (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_rename_inuse (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_snapdev (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_trim (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_volmode (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_zil (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/zvol_stress (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Summary for Logs-20.04-sanity
<pre>

Tests with results other than PASS that are expected:

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.args_to_lua (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.divide_by_zero (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.exists (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.integer_illegal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.integer_overflow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.language_functions_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.language_functions_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.large_prog (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.libraries (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.memory_limit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nested_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nested_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.nvlist_to_lua (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.recursive_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.recursive_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_large (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_nvlist_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_nvlist_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.return_recursive_table (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.stack_gsub (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/tst.timeout (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/lua_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.destroy_fs (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.destroy_snap (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_count_and_limit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_index_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_number_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_string_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_type (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_userquota (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.get_written (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.inherit (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_bookmarks (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_children (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_clones (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_holds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_snapshots (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_system_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_user_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.parse_args_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_conflict (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_multiple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.promote_simple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.rollback_mult (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.rollback_one (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.set_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_destroy (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_recursive (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.snapshot_simple (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.bookmark.create (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.bookmark.copy (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_dryrun (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_verbose (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_013_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_location (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_noop (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_recursive (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_fail (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_mountpoints (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_test_race (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/zfs_program_json (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_encryptionroot (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_encrypted_child (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_to_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_nounmount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/zfs_reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/checksum_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/compression_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/share_mount_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/snapdir_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/onoffs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_getsubopt (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_colors (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_014_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/zpool_online_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_online/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/zpool_remove_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_encrypted_unloaded (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_print_repairing (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_multiple_copies (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_attach_detach_add_remove (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_rate_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_secure (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_split (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_start_and_cancel_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/setup (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zdb_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_allow_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_clone_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_create_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_destroy_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_get_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_inherit_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_mount_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_promote_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_receive_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_rename_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_rollback_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_send_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_set_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_snapshot_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_unallow_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_unmount_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zfs_upgrade_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_add_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_attach_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_clear_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_create_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_destroy_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_detach_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_export_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_get_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_history_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_offline_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_online_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_remove_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_scrub_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_set_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_status_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_upgrade_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arcstat_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arc_summary_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arc_summary_002_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zpool_wait_privilege (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/zilstat_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_001_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_002_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_003_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_004_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_disable (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_homedir (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/zpool_iostat_-c_searchpath (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_iostat/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/zpool_list_001_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/zpool_list_002_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zpool_list/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_zstd_bswap (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_root_inode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/log_spacemap/log_spacemap_import_logs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/migration_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/migration/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/clone_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/rollback_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/sparse_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_none (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_userobj_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_readonly_pool (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_compat (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/zpool_influxdb (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zpool_influxdb/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/zvol_ENOSPC_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_ENOSPC/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Summary for Logs-22.04-sanity
<pre>

Tests with results other than PASS that are expected:

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/append/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/append/cleanup (run as root) [00:00] [PASS]
</pre></details>
