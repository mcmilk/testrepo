
## Sanity Tests Ubuntu 20.04

:bangbang: Logfile Logs-20.04-sanity/testfiles/log not found :bangbang:


## Sanity Tests Ubuntu 22.04

:bangbang: Logfile Logs-22.04-sanity/testfiles/log not found :bangbang:


## Functional Tests Ubuntu 20.04

:bangbang: Tarfile Logs-20.04-functional/part1.tar not found :bangbang:

:bangbang: Logfile testfiles/log not found :bangbang:

:bangbang: Logfile testfiles/log not found :bangbang:

:bangbang: Tarfile Logs-20.04-functional/part5.tar not found :bangbang:

<pre>

Tests with results other than PASS that are expected:
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Functional Tests Ubuntu 22.04

:bangbang: Tarfile Logs-22.04-functional/part4.tar not found :bangbang:

:bangbang: Tarfile Logs-22.04-functional/part5.tar not found :bangbang:

<pre>

Tests with results other than PASS that are expected:
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Sanity Tests Ubuntu 20.04

:bangbang: Logfile Logs-20.04-sanity/testfiles/log not found :bangbang:


## Sanity Tests Ubuntu 22.04

:bangbang: Logfile Logs-22.04-sanity/testfiles/log not found :bangbang:


## Functional Tests Ubuntu 20.04

:bangbang: Tarfile Logs-20.04-functional/part1.tar not found :bangbang:

:bangbang: Logfile testfiles/log not found :bangbang:

:bangbang: Logfile testfiles/log not found :bangbang:

:bangbang: Tarfile Logs-20.04-functional/part5.tar not found :bangbang:

<pre>

Tests with results other than PASS that are expected:
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Functional Tests Ubuntu 22.04

:bangbang: Tarfile Logs-22.04-functional/part4.tar not found :bangbang:

:bangbang: Tarfile Logs-22.04-functional/part5.tar not found :bangbang:

<pre>

Tests with results other than PASS that are expected:
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
02:46:03.34 ASSERTION: Verify refreservation is limited by available space.
02:46:03.38 SUCCESS: zfs create testpool/testfs/subfs
02:46:03.40 SUCCESS: zfs set quota=25M testpool
02:46:03.42 SUCCESS: zfs set refreservation=15M testpool
02:46:03.46 SUCCESS: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.84 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10255360 bytes: Disk quota exceeded
02:46:03.84 ERROR: mkfile 10255360 /var/tmp/testdir/subfs/testfile exited 1
02:46:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:46:03.84 =================================================================
02:46:03.84  Tailing last 200 lines of zfs_dbgmsg log
02:46:03.84 =================================================================
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30208, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
02:46:03.86 1678243562   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 169472, appended 112 bytes
02:46:03.86 1678243562   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
02:46:03.86 1678243562   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43008, unflushed_frees 41472, appended 144 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 35328, appended 136 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 37888, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 104 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38400, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 120 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 128 bytes
02:46:03.86 1678243562   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39936, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39936, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 39936, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40960, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435712, unflushed_frees 41984, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 41984, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34304, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 42496, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 34816, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 174592, appended 120 bytes
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
02:46:03.86 1678243563   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 408)  
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 300)  
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 43008, appended 88 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 280) refreservation=0
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 280) (bptree, mintxg=1)
02:46:03.86 1678243563   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:46:03.86 1678243563   dsl_scan.c:3492:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 69120, appended 192 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 448)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 91136, appended 256 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 46592, unflushed_frees 54784, appended 136 bytes
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 448) mountpoint=/var/tmp/testdir
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66048, unflushed_frees 22100992, appended 1336 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 362)  
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 70144, unflushed_frees 51712, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:329:spa_history_log_sync(): ioctl create
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 47104, unflushed_frees 41472, appended 120 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 73216, unflushed_frees 55808, appended 160 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
02:46:03.86 1678243563   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 362) refreservation=10255360
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 68608, unflushed_frees 55808, appended 176 bytes
02:46:03.86 1678243563   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10255360 testpool/testfs/subfs
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 43008, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 43520, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37376, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 44544, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 37888, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438272, unflushed_frees 45568, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45056, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 45568, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 38912, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 46080, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 46080, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 37888, appended 72 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47616, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39424, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 47616, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40448, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 48640, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 41472, appended 80 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49664, appended 112 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 49152, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49152, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 40960, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 49664, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49152, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41472, appended 88 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50176, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50176, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 144 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 444416, unflushed_frees 50688, appended 136 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 50688, appended 120 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 42496, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443904, unflushed_frees 51200, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 50688, appended 104 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 41984, appended 96 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 445440, unflushed_frees 50688, appended 128 bytes
02:46:03.86 1678243563   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 51200, appended 104 bytes
02:46:03.86 =================================================================
02:46:03.86  End of zfs_dbgmsg log
02:46:03.86 =================================================================
02:46:03.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:46:03.86 =================================================================
02:46:03.86  Tailing last 200 lines of dmesg log
02:46:03.86 =================================================================
02:46:03.87 [  465.486119] loop0: detected capacity change from 0 to 6291456
02:46:03.87 [  465.515847] loop1: detected capacity change from 0 to 6291456
02:46:03.87 [  465.544705] loop2: detected capacity change from 0 to 6291456
02:46:03.87 [  465.728011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
02:46:03.87 [  465.753492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
02:46:03.87 [  467.890653] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
02:46:03.87 [  770.215671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
02:46:03.87 [  833.384512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
02:46:03.87 [  895.623445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
02:46:03.87 [  895.647073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
02:46:03.87 [  896.109093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
02:46:03.87 [  897.554866] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
02:46:03.87 [  902.180245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
02:46:03.87 [  903.485640] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
02:46:03.87 [  904.767760] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
02:46:03.87 [  916.513856] loop3: detected capacity change from 0 to 8
02:46:03.87 [  916.979703] audit: type=1400 audit(1678242494.820:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=27634 comm="apparmor_parser"
02:46:03.87 [  916.998425] audit: type=1400 audit(1678242494.840:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=27634 comm="apparmor_parser"
02:46:03.87 [  959.952451] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
02:46:03.87 [  967.160615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
02:46:03.87 [  973.558172] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
02:46:03.87 [  975.833785] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
02:46:03.87 [  984.310880] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
02:46:03.87 [  986.623896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
02:46:03.87 [  988.261605] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
02:46:03.87 [  989.400361] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
02:46:03.87 [  992.156770] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
02:46:03.87 [ 1053.183539] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
02:46:03.87 [ 1056.365048] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
02:46:03.87 [ 1058.487269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
02:46:03.87 [ 1059.189615] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
02:46:03.87 [ 1059.273749] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.606162] debugfs: Directory 'zd0' with parent 'block' already present!
02:46:03.87 [ 1069.815041] debugfs: Directory 'zd16' with parent 'block' already present!
02:46:03.87 [ 1069.994652] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.359143] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1080.692135] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.038244] debugfs: Directory 'zd32' with parent 'block' already present!
02:46:03.87 [ 1091.280524] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
02:46:03.87 [ 1091.520895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
02:46:03.87 [ 1091.544314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
02:46:03.87 [ 1262.791399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
02:46:03.87 [ 1278.416413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
02:46:03.87 [ 1317.844021] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
02:46:03.87 [ 1365.675620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
02:46:03.87 [ 1486.551562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
02:46:03.87 [ 1593.807750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
02:46:03.87 [ 1621.718236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
02:46:03.87 [ 1642.188596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
02:46:03.87 [ 1717.483903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
02:46:03.87 [ 1728.591399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
02:46:03.87 [ 1895.909734] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
02:46:03.87 [ 1905.016050] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
02:46:03.87 [ 1926.760600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
02:46:03.87 [ 1959.730620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
02:46:03.87 [ 1964.518718] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
02:46:03.87 [ 1964.555954] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
02:46:03.87 [ 1964.870180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
02:46:03.87 [ 1967.308791] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
02:46:03.87 [ 1969.334216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
02:46:03.87 [ 1970.975657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
02:46:03.87 [ 1972.850618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
02:46:03.87 [ 1974.606334] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
02:46:03.87 [ 1975.321100] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
02:46:03.87 [ 1975.660245] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
02:46:03.87 [ 1981.509162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
02:46:03.87 [ 1981.760604] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
02:46:03.87 [ 1982.070708] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
02:46:03.87 [ 1982.798272] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
02:46:03.87 [ 1984.485139] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
02:46:03.87 [ 1985.459873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
02:46:03.87 =================================================================
02:46:03.87  End of dmesg log
02:46:03.87 =================================================================
02:46:03.87 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:46:03.87 NOTE: Performing local cleanup via log_onexit (cleanup)
02:46:03.89 SUCCESS: zfs set refreservation=none testpool
02:46:03.96 SUCCESS: zfs destroy -rf testpool/testfs
02:46:03.99 SUCCESS: zfs create testpool/testfs
02:46:04.03 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/setup (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_002_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_003_neg (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/rootpool_007_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rootpool/cleanup (run as root) [00:00] [PASS]
</pre></details>
