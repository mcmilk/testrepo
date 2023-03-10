

## Sanity Tests Ubuntu 20.04

No errors within these testings :thumbsup:
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
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_children (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_dryrun (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_verbose (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_001_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:12] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/setup (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arcstat_001_pos (run as runner) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/arc_summary_001_pos (run as runner) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/sparse_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_none (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_userobj_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_readonly_pool (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_004_pos (run as root) [00:00] [PASS]
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

## Sanity Tests Ubuntu 22.04

No errors within these testings :thumbsup:
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:11] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_location (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_noop (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_recursive (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_encryptionroot (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cache_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/canmount_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/checksum_001_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_encrypted_unloaded (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_print_repairing (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_multiple_copies (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:07] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_trim/zpool_trim_online_offline (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:08] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:07] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_004_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/clone_001_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/sparse_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/sparse/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_suid_sgid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/suid_write_to_none (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/suid/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/truncate_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/truncate/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_userobj_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_readonly_pool (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_004_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Functional Tests Ubuntu 20.04

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
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><small><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
02:50:38.85 SUCCESS: set_tunable32 TXG_HISTORY 100
02:50:38.86 SUCCESS: mkdir -p /var/tmp/bakdev_import-test
02:50:38.86 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk0
02:50:38.87 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk1
02:50:38.87 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk2
02:50:38.87 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk3
02:50:38.88 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk4
02:50:38.88 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk5
02:50:38.89 NOTE: test_replace_vdev: pool '/var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1', replace /var/tmp/dev_import-test/disk1 by /var/tmp/dev_import-test/disk2.
02:50:38.95 SUCCESS: zpool create testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:50:38.99 SUCCESS: zfs create testpool1/ds1
02:50:39.08 SUCCESS: zpool sync testpool1
02:50:39.12 SUCCESS: zfs create testpool1/ds2
02:50:39.20 SUCCESS: zpool sync testpool1
02:50:39.24 SUCCESS: zfs create testpool1/ds3
02:50:39.33 SUCCESS: zpool sync testpool1
02:50:39.34 SUCCESS: generate_data testpool1 /var/tmp/md5sums.624635
02:50:40.24 SUCCESS: write_some_data testpool1 15
02:50:40.28 SUCCESS: zpool sync testpool1
02:50:40.31 SUCCESS: zpool sync testpool1
02:50:40.35 SUCCESS: zpool sync testpool1
02:50:40.38 SUCCESS: zpool sync testpool1
02:50:40.41 SUCCESS: zpool sync testpool1
02:50:40.45 SUCCESS: zpool sync testpool1
02:50:40.48 SUCCESS: zpool sync testpool1
02:50:40.51 SUCCESS: zpool sync testpool1
02:50:40.55 SUCCESS: zpool sync testpool1
02:50:40.58 SUCCESS: zpool sync testpool1
02:50:40.61 SUCCESS: zpool sync testpool1
02:50:40.62 SUCCESS: sync_some_data_a_few_times testpool1
02:50:43.23 SUCCESS: zfs snapshot -r testpool1@snap1
02:50:43.33 SUCCESS: overwrite_data testpool1 
02:50:43.43 SUCCESS: zpool export testpool1
02:50:43.62 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:50:43.62 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 1
02:50:43.68 SUCCESS: zpool replace testpool1 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk2
02:50:43.70 SUCCESS: pool_is_replacing testpool1
02:50:49.86 SUCCESS: zpool export testpool1
02:50:49.86 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:50:50.06 SUCCESS: zpool import -d /var/tmp/dev_import-test -o readonly=on -T 53 testpool1
02:50:50.11 SUCCESS: check_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
02:50:50.19 SUCCESS: verify_data_md5sums /var/tmp/md5sums.624635
02:50:50.23 SUCCESS: zpool export testpool1
02:50:50.85 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
02:50:50.95 SUCCESS: overwrite_data testpool1 
02:50:54.07 SUCCESS: wait_for_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk2
02:50:54.13 SUCCESS: zpool export testpool1
02:50:54.14 SUCCESS: mv /var/tmp/dev_import-test/disk2 /var/tmp/bakdev_import-test/
02:50:54.49 cannot import 'testpool1': one or more devices is currently unavailable
02:50:54.49 ERROR: zpool import -d /var/tmp/dev_import-test -T 53 testpool1 exited 1
02:50:54.49 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:50:54.49 =================================================================
02:50:54.49  Tailing last 200 lines of zfs_dbgmsg log
02:50:54.49 =================================================================
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 10, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 11, unflushed_allocs 0, unflushed_frees 6656, appended 32 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 12, unflushed_allocs 0, unflushed_frees 4608, appended 24 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 13, unflushed_allocs 0, unflushed_frees 3072, appended 32 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 14, unflushed_allocs 0, unflushed_frees 3072, appended 32 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 7, unflushed_allocs 16896, unflushed_frees 1581056, appended 56 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 7, unflushed_allocs 3072, unflushed_frees 1056768, appended 32 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 10, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 11, unflushed_allocs 0, unflushed_frees 1024, appended 16 bytes
02:50:54.50 1678243854   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 9, unflushed_allocs 0, unflushed_frees 1024, appended 16 bytes
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): UNLOADING
02:50:54.50 1678243854   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool1' gethrtime 3879021851400
02:50:54.50 1678243854   spa.c:6288:spa_tryimport(): spa_tryimport: importing testpool1, max_txg=53
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load($import, config trusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa $import. txg 53
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=53
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load($import, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load($import, config untrusted): UNLOADING
02:50:54.50 1678243854   spa.c:6145:spa_import(): spa_import: importing testpool1, max_txg=53 (RECOVERY MODE)
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config trusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 53
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=53
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 52
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 50
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 50)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=50
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 49
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 47
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 47)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=47
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 46
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 44
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 44)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=44
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 43
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 41
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 41)
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=41
02:50:54.50 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 40
02:50:54.50 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 38
02:50:54.50 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 38)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=38
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 37
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 35
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 35)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=35
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 34
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 32
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 32)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=32
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 31
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 29
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 29)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=29
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 28
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 26
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 26)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=26
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 25
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 23
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 23)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=23
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 22
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 22
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 22)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=22
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 21
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 21
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 21)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=21
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 20
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 20
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 20)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=20
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 19
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 17
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 17)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=17
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 16
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 16
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 16)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=16
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 15
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 13
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 13)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=13
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 12
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 12
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 12)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=12
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 11
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 9
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 9)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=9
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 8
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 8
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 8)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=8
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 7
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 5
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 5)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=5
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 4
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 4
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 4)
02:50:54.51 1678243854   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=4
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 3
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
02:50:54.51 1678243854   spa_misc.c:402:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: no valid uberblock found
02:50:54.51 1678243854   spa_misc.c:416:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
02:50:54.51 =================================================================
02:50:54.51  End of zfs_dbgmsg log
02:50:54.51 =================================================================
02:50:54.51 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:50:54.51 =================================================================
02:50:54.51  Tailing last 200 lines of dmesg log
02:50:54.51 =================================================================
02:50:54.52 [ 2562.980917] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 2563.481891] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_001_pos
02:50:54.52 [ 2564.566965] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_002_pos
02:50:54.52 [ 2564.590310] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_003_pos
02:50:54.52 [ 2564.802545] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_004_neg
02:50:54.52 [ 2565.050732] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_005_neg
02:50:54.52 [ 2565.173564] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_006_pos
02:50:54.52 [ 2566.426087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_007_pos
02:50:54.52 [ 2566.552165] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/zfs_unshare_008_pos
02:50:54.52 [ 2566.738287] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/cleanup
02:50:54.52 [ 2566.971961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/setup
02:50:54.52 [ 2567.472184] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_001_pos
02:50:54.52 [ 2568.049445] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 2569.089156] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_002_pos
02:50:54.52 [ 2569.165408] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_003_pos
02:50:54.52 [ 2579.733243] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_004_pos
02:50:54.52 [ 2590.740404] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_005_pos
02:50:54.52 [ 2602.021427] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_006_neg
02:50:54.52 [ 2602.201889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_007_neg
02:50:54.52 [ 2602.338668] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/cleanup
02:50:54.52 [ 2602.624620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/setup
02:50:54.52 [ 2602.900194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq
02:50:54.52 [ 2605.467155] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_getsubopt
02:50:54.52 [ 2605.505658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/cleanup
02:50:54.52 [ 2605.739909] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zhack/zhack_label_checksum
02:50:54.52 [ 2606.200739] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/setup
02:50:54.52 [ 2606.731989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_001_neg
02:50:54.52 [ 2607.296780] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_002_pos
02:50:54.52 [ 2612.147024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_003_pos
02:50:54.52 [ 2612.886896] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_colors
02:50:54.52 [ 2613.349448] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/cleanup
02:50:54.52 [ 2613.644678] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup
02:50:54.52 [ 2613.683517] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_001_pos
02:50:54.52 [ 2620.090346] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_002_pos
02:50:54.52 [ 2620.889301] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_003_pos
02:50:54.52 [ 2621.405652] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos
02:50:54.52 [ 2621.824903] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 2622.329828]  zd0: p1 p9
02:50:54.52 [ 2623.801413] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_006_pos
02:50:54.52 [ 2624.542176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_007_neg
02:50:54.52 [ 2625.013056] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_008_neg
02:50:54.52 [ 2625.389478] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg
02:50:54.52 [ 2628.300842] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos
02:50:54.52 [ 2668.686947] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add-o_ashift
02:50:54.52 [ 2679.526436] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_prop_ashift
02:50:54.52 [ 2701.312818] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_dryrun_output
02:50:54.52 [ 2702.305721] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup
02:50:54.52 [ 2702.345414] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup
02:50:54.52 [ 2702.383992] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_nested_replacing_spare
02:50:54.52 [ 2708.053269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup
02:50:54.52 [ 2708.092160] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup
02:50:54.52 [ 2708.607945] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg
02:50:54.52 [ 2709.143321] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/attach-o_ashift
02:50:54.52 [ 2729.799943] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/cleanup
02:50:54.52 [ 2730.076970] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/setup
02:50:54.52 [ 2730.360647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_001_pos
02:50:54.52 [ 2745.066879] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_002_neg
02:50:54.52 [ 2745.588184] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_003_neg
02:50:54.52 [ 2746.814268] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_readonly
02:50:54.52 [ 2747.298570] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/cleanup
02:50:54.52 [ 2747.526004] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/setup
02:50:54.52 [ 2747.569394] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_001_pos
02:50:54.52 [ 2751.340000] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_002_pos
02:50:54.52 [ 2753.941906] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_003_pos
02:50:54.52 [ 2756.249841] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_004_pos
02:50:54.52 [ 2757.191204] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_005_pos
02:50:54.52 [ 2763.201240] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos
02:50:54.52 [ 2780.212432] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg
02:50:54.52 [ 2782.498646] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos
02:50:54.52 [ 2784.265754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_009_neg
02:50:54.52 [ 2790.167520] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_010_neg
02:50:54.52 [ 2790.702672] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_011_neg
02:50:54.52 [ 2791.338475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_012_neg
02:50:54.52 [ 2791.377649] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_014_neg
02:50:54.52 [ 2791.614465] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 2792.165136] EXT4-fs (zd0): mounting ext2 file system using the ext4 subsystem
02:50:54.52 [ 2792.166252] EXT4-fs (zd0): mounted filesystem without journal. Opts: (null). Quota mode: none.
02:50:54.52 [ 2792.166260] ext2 filesystem being mounted at /mnt supports timestamps until 2038 (0x7fffffff)
02:50:54.52 [ 2792.345064] Adding 51196k swap on /mnt/tmpfile.354845.  Priority:-3 extents:2 across:57344k SSFS
02:50:54.52 [ 2792.597661] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg
02:50:54.52 [ 2792.826261] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 2793.272683] Adding 102396k swap on /dev/zd0.  Priority:-3 extents:1 across:102396k SSFS
02:50:54.52 [ 2794.513786] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg
02:50:54.52 [ 2794.850746] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos
02:50:54.52 [ 2796.443502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos
02:50:54.52 [ 2796.624841] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos
02:50:54.52 [ 2796.999859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos
02:50:54.52 [ 2805.536512] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos
02:50:54.52 [ 2806.426316] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_023_neg
02:50:54.52 [ 2823.171039] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_024_pos
02:50:54.52 [ 2882.315053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted
02:50:54.52 [ 2888.040150] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_crypt_combos
02:50:54.52 [ 2902.222941] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos
02:50:54.52 [ 2930.716205] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos
02:50:54.52 [ 2948.265397] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos
02:50:54.52 [ 2957.374967] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos
02:50:54.52 [ 3092.872660] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos
02:50:54.52 [ 3093.952273] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos
02:50:54.52 [ 3095.899263] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos
02:50:54.52 [ 3096.908377] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg
02:50:54.52 [ 3098.033171] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos
02:50:54.52 [ 3100.169956] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos
02:50:54.52 [ 3101.533616] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos
02:50:54.52 [ 3102.773041] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos
02:50:54.52 [ 3104.025695] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos
02:50:54.52 [ 3116.631970] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift
02:50:54.52 [ 3158.723617] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname
02:50:54.52 [ 3183.819915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output
02:50:54.52 [ 3183.937725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup
02:50:54.52 [ 3185.927908] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos
02:50:54.52 [ 3186.456959] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3186.940486]  zd0: p1 p9
02:50:54.52 [ 3188.587710] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos
02:50:54.52 [ 3188.985708] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3189.747207] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg
02:50:54.52 [ 3189.849215] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup
02:50:54.52 [ 3190.391198] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg
02:50:54.52 [ 3190.638830] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup
02:50:54.52 [ 3190.932195] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup
02:50:54.52 [ 3191.241818] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3191.749370] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear
02:50:54.52 [ 3192.687886] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_cliargs
02:50:54.52 [ 3217.591402] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow
02:50:54.52 [ 3218.512843] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname
02:50:54.52 [ 3220.520320] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_errors
02:50:54.52 [ 3231.920280] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_duplicates
02:50:54.52 [ 3233.131663] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear_retained
02:50:54.52 [ 3235.028074] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup
02:50:54.52 [ 3235.259489] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/setup
02:50:54.52 [ 3235.620902] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_001_pos
02:50:54.52 [ 3235.645100] loop3: detected capacity change from 0 to 2097152
02:50:54.52 [ 3236.435933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_002_pos
02:50:54.52 [ 3274.737523] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_003_neg
02:50:54.52 [ 3274.761547] loop3: detected capacity change from 0 to 2097152
02:50:54.52 [ 3275.576501] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_004_pos
02:50:54.52 [ 3278.030343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_005_pos
02:50:54.52 [ 3278.076419] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/cleanup
02:50:54.52 [ 3279.344022] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/setup
02:50:54.52 [ 3279.671448] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_001_pos
02:50:54.52 [ 3279.847213] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_002_pos
02:50:54.52 [ 3279.992183] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg
02:50:54.52 [ 3280.133143] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos
02:50:54.52 [ 3281.592995] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup
02:50:54.52 [ 3281.655798] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup
02:50:54.52 [ 3281.957895] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos
02:50:54.52 [ 3282.004590] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos
02:50:54.52 [ 3282.343392] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos
02:50:54.52 [ 3283.732386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg
02:50:54.52 [ 3283.785371] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos
02:50:54.52 [ 3283.999540] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup
02:50:54.52 [ 3284.228059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup
02:50:54.52 [ 3284.694459] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3285.202144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg
02:50:54.52 [ 3285.531216] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos
02:50:54.52 [ 3285.708003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup
02:50:54.52 [ 3285.926149] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup
02:50:54.52 [ 3286.254646] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos
02:50:54.52 [ 3294.534112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos
02:50:54.52 [ 3303.386344] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos
02:50:54.52 [ 3304.011118] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos
02:50:54.52 [ 3312.879486] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos
02:50:54.52 [ 3321.770694] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos
02:50:54.52 [ 3330.520313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos
02:50:54.52 [ 3343.090688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos
02:50:54.52 [ 3356.990237] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg
02:50:54.52 [ 3361.782420] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos
02:50:54.52 [ 3368.632651] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg
02:50:54.52 [ 3375.913842] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos
02:50:54.52 [ 3407.255914] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg
02:50:54.52 [ 3478.656934] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos
02:50:54.52 [ 3482.219422] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos
02:50:54.52 [ 3484.926365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos
02:50:54.52 [ 3495.711763] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos
02:50:54.52 [ 3509.676086] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos
02:50:54.52 [ 3521.238458] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg
02:50:54.52 [ 3539.707009] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos
02:50:54.52 [ 3558.269020] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos
02:50:54.52 [ 3601.804290] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos
02:50:54.52 [ 3662.723969] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos
02:50:54.52 [ 3662.767516] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos
02:50:54.52 [ 3671.198652] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos
02:50:54.52 [ 3674.708010] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted
02:50:54.52 [ 3675.705485] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load
02:50:54.52 [ 3678.168310] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3
02:50:54.52 [ 3679.915951] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3680.705255] debugfs: Directory 'zd16' with parent 'block' already present!
02:50:54.52 [ 3681.246927] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4
02:50:54.52 [ 3693.203226] debugfs: Directory 'zd0' with parent 'block' already present!
02:50:54.52 [ 3694.099880] debugfs: Directory 'zd16' with parent 'block' already present!
02:50:54.52 [ 3695.222691] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added
02:50:54.52 [ 3700.748430] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed
02:50:54.52 [ 3718.262372] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced
02:50:54.52 [ 3761.318818] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached
02:50:54.52 [ 3763.123453] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached
02:50:54.52 [ 3768.772214] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed
02:50:54.52 [ 3773.415273] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device
02:50:54.52 [ 3775.378405] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing
02:50:54.52 [ 3784.893163] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed
02:50:54.52 [ 3788.093202] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed
02:50:54.52 [ 3864.163039] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced
02:50:54.52 =================================================================
02:50:54.52  End of dmesg log
02:50:54.52 =================================================================
02:50:54.52 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:50:54.52 NOTE: Performing local cleanup via log_onexit (custom_cleanup)
02:50:54.52 SUCCESS: set_zfs_txg_timeout 5
02:50:54.54 SUCCESS: rm -rf /var/tmp/bakdev_import-test
02:50:54.55 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
02:50:54.56 SUCCESS: eval zinject -c all > /dev/null
02:50:54.58 NOTE: Pool does not exist. (testpool1)
02:50:54.58 SUCCESS: rm -f /var/tmp/cachefile.624635 /var/tmp/cachefile.624635.bkp /var/tmp/cachefile.624635.bkp2 /var/tmp/md5sums.624635 /var/tmp/md5sums.624635.2
02:50:54.62 SUCCESS: rm -rf /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk3 /var/tmp/dev_import-test/disk4 /var/tmp/dev_import-test/disk5
02:50:54.62 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk0
02:50:54.63 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk1
02:50:54.63 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk2
02:50:54.63 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk3
02:50:54.64 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk4
02:50:54.64 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk5
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
02:11:19.81 ASSERTION: CS-UN FS: lookup succeeds if (case=same)
02:11:19.85 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:19.89 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.90 SUCCESS: create_file FïLëNÄmë
02:11:19.90 SUCCESS: lookup_file FïLëNÄmë
02:11:19.90 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:19.91 SUCCESS: lookup_file fïlënämë exited 1
02:11:19.91 SUCCESS: lookup_file FïLëNÄmë
02:11:19.91 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:19.92 SUCCESS: lookup_file fïlënämë exited 1
02:11:19.92 SUCCESS: create_file FÏLËNÄMË
02:11:19.93 SUCCESS: lookup_file FïLëNÄmë exited 1
02:11:19.93 SUCCESS: lookup_file FÏLËNÄMË
02:11:19.93 SUCCESS: lookup_file fïlënämë exited 1
02:11:19.94 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:11:19.94 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:19.94 =================================================================
02:11:19.94  Tailing last 200 lines of zfs_dbgmsg log
02:11:19.94 =================================================================
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 32, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 28160, unflushed_frees 24576, appended 160 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 33 create testpool/testfs (id 114)  
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 33, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22528, unflushed_frees 23552, appended 104 bytes
02:11:19.95 1678241471   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 34, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 42496, unflushed_frees 46592, appended 128 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 35 set testpool/testfs (id 114) mountpoint=/var/tmp/testdir
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 35, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 46592, appended 160 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 36, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 22528, appended 96 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 37 destroy testpool/testfs (id 114) (bptree, mintxg=1)
02:11:19.95 1678241471   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241471   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 37; err=0
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 37, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29696, unflushed_frees 25088, appended 136 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 124)  
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 43008, appended 112 bytes
02:11:19.95 1678241471   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 27648, appended 96 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 124) mountpoint=/var/tmp/testdir
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 47616, appended 144 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 30720, appended 120 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 124) (bptree, mintxg=1)
02:11:19.95 1678241471   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241471   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22528, unflushed_frees 18944, appended 104 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 165)  
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 44032, appended 120 bytes
02:11:19.95 1678241471   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 47616, appended 128 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 165) mountpoint=/var/tmp/testdir
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 28160, appended 120 bytes
02:11:19.95 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 30208, appended 144 bytes
02:11:19.95 1678241471   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 165) (bptree, mintxg=1)
02:11:19.95 1678241471   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241471   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
02:11:19.95 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 25600, appended 136 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 176)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 25600, appended 88 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 49152, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 176) mountpoint=/var/tmp/testdir
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 48640, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 266)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 25088, appended 112 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 27136, appended 136 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 266) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 34816, appended 128 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 25600, appended 128 bytes
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 37888, unflushed_frees 45568, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 176) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33792, unflushed_frees 45568, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 189)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29696, appended 112 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 47104, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 189) mountpoint=/var/tmp/testdir
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 49664, appended 176 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 278)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 25600, appended 128 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46592, unflushed_frees 28160, appended 136 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 278) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 53760, unflushed_frees 36864, appended 136 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 120 bytes
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 48128, appended 144 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 189) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 48128, appended 152 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 204)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26624, unflushed_frees 32256, appended 88 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 48640, appended 120 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 204) mountpoint=/var/tmp/testdir
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 51200, appended 168 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 214)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 26624, appended 120 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45568, unflushed_frees 28672, appended 136 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 214) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 36352, appended 120 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 27136, appended 136 bytes
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 47104, appended 160 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 204) (bptree, mintxg=1)
02:11:19.95 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47104, appended 152 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 291)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31744, appended 104 bytes
02:11:19.95 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 48640, appended 128 bytes
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 291) mountpoint=/var/tmp/testdir
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 51200, appended 168 bytes
02:11:19.95 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241472   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 300)  
02:11:19.95 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 27136, appended 104 bytes
02:11:19.95 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48128, unflushed_frees 29696, appended 128 bytes
02:11:19.95 1678241473   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 300) (bptree, mintxg=1)
02:11:19.95 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55296, unflushed_frees 38400, appended 104 bytes
02:11:19.95 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29184, appended 112 bytes
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 49664, appended 144 bytes
02:11:19.95 1678241473   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 291) (bptree, mintxg=1)
02:11:19.95 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 144 bytes
02:11:19.95 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241473   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 311)  
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 104 bytes
02:11:19.95 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 50688, appended 128 bytes
02:11:19.95 1678241473   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 311) mountpoint=/var/tmp/testdir
02:11:19.95 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53760, appended 176 bytes
02:11:19.95 1678241474   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241474   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 128 bytes
02:11:19.95 1678241476   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 38400, appended 144 bytes
02:11:19.95 1678241477   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 38400, appended 192 bytes
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 24064, appended 80 bytes
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485888, unflushed_frees 47104, appended 264 bytes
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 337920, unflushed_frees 48128, appended 208 bytes
02:11:19.95 1678241478   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 311) (bptree, mintxg=1)
02:11:19.95 1678241478   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241478   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:19.95 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241478   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 324)  
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 631296, appended 280 bytes
02:11:19.95 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:19.95 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:19.95 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:19.95 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:19.95 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:19.95 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:19.95 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:19.95 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:19.95 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:19.95 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:19.95 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:19.95 =================================================================
02:11:19.95  End of zfs_dbgmsg log
02:11:19.95 =================================================================
02:11:19.95 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:19.96 =================================================================
02:11:19.96  Tailing last 200 lines of dmesg log
02:11:19.96 =================================================================
02:11:19.96 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:19.96 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:19.96 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:19.96 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:19.96 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:19.96 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:19.96 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:19.96 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:19.96 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:19.96 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:19.96 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:19.96 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:19.96 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:19.96 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:19.96 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:19.96 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:19.96 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:19.96 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:19.96 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:19.96 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:19.96 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:19.96 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:19.96 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:19.96 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:19.96 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:19.96 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:19.96 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:19.96 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:19.96 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:19.96 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:19.96 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:19.96 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:19.96 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:19.96 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:19.96 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:19.96 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:19.96 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:19.96 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:19.96 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:19.96 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:19.96 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:19.96 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:19.96 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:19.96 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:19.96 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:19.96 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:19.96 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:19.96 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:19.96 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:19.96 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:19.96 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:19.96 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:19.96 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:19.96 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:19.96 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:19.96 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:19.96 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:19.96 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:19.96 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:19.96 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:19.96 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:19.96 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:19.96 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:19.96 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:19.96 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:19.96 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:19.96 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:19.96 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:19.96 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:19.96 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:19.96 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:19.96 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:19.96 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:19.96 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:19.96 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:19.96 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:19.96 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:19.96 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:19.96 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:19.96 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:19.96 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:19.96 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:19.96 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:19.96 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:19.96 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:19.96 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:19.96 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:19.96 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:19.96 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:19.96 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:19.96 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:19.97 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:19.97 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:19.97 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:19.97 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:19.97 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:19.97 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:19.97 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:19.97 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:19.97 =================================================================
02:11:19.97  End of dmesg log
02:11:19.97 =================================================================
02:11:19.97 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:19.97 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:20.06 SUCCESS: zfs destroy -f testpool/testfs
02:11:20.06 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
02:11:20.09 ASSERTION: CS-UN FS: delete succeeds if (case=same)
02:11:20.13 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:20.18 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.18 SUCCESS: create_file FïLëNÄmë
02:11:20.19 SUCCESS: delete_file FïLëNÄmë
02:11:20.19 SUCCESS: lookup_any exited 1
02:11:20.20 SUCCESS: create_file FïLëNÄmë
02:11:20.20 SUCCESS: delete_file FÏLËNÄMË exited 1
02:11:20.21 SUCCESS: create_file FïLëNÄmë
02:11:20.21 SUCCESS: delete_file fïlënämë exited 1
02:11:20.22 SUCCESS: create_file FïLëNÄmë
02:11:20.22 ERROR: delete_file FïLëNÄmë exited 1
02:11:20.22 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:20.22 =================================================================
02:11:20.22  Tailing last 200 lines of zfs_dbgmsg log
02:11:20.22 =================================================================
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 124)  
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 43008, appended 112 bytes
02:11:20.24 1678241471   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 27648, appended 96 bytes
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 124) mountpoint=/var/tmp/testdir
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 47616, appended 144 bytes
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 30720, appended 120 bytes
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 124) (bptree, mintxg=1)
02:11:20.24 1678241471   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241471   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22528, unflushed_frees 18944, appended 104 bytes
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 165)  
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 44032, appended 120 bytes
02:11:20.24 1678241471   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 47616, appended 128 bytes
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 165) mountpoint=/var/tmp/testdir
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 28160, appended 120 bytes
02:11:20.24 1678241471   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 30208, appended 144 bytes
02:11:20.24 1678241471   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 165) (bptree, mintxg=1)
02:11:20.24 1678241471   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241471   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
02:11:20.24 1678241471   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 25600, appended 136 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 176)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 25600, appended 88 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 49152, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 176) mountpoint=/var/tmp/testdir
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 48640, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 266)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 25088, appended 112 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 27136, appended 136 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 266) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 34816, appended 128 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 25600, appended 128 bytes
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 37888, unflushed_frees 45568, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 176) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33792, unflushed_frees 45568, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 189)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29696, appended 112 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 47104, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 189) mountpoint=/var/tmp/testdir
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 49664, appended 176 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 278)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 25600, appended 128 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46592, unflushed_frees 28160, appended 136 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 278) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 53760, unflushed_frees 36864, appended 136 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 120 bytes
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 48128, appended 144 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 189) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 48128, appended 152 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 204)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26624, unflushed_frees 32256, appended 88 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 48640, appended 120 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 204) mountpoint=/var/tmp/testdir
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 51200, appended 168 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 214)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 26624, appended 120 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45568, unflushed_frees 28672, appended 136 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 214) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 36352, appended 120 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 27136, appended 136 bytes
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 47104, appended 160 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 204) (bptree, mintxg=1)
02:11:20.24 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47104, appended 152 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 291)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31744, appended 104 bytes
02:11:20.24 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 48640, appended 128 bytes
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 291) mountpoint=/var/tmp/testdir
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 51200, appended 168 bytes
02:11:20.24 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241472   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 300)  
02:11:20.24 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 27136, appended 104 bytes
02:11:20.24 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48128, unflushed_frees 29696, appended 128 bytes
02:11:20.24 1678241473   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 300) (bptree, mintxg=1)
02:11:20.24 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55296, unflushed_frees 38400, appended 104 bytes
02:11:20.24 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29184, appended 112 bytes
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 49664, appended 144 bytes
02:11:20.24 1678241473   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 291) (bptree, mintxg=1)
02:11:20.24 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 144 bytes
02:11:20.24 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241473   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 311)  
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 104 bytes
02:11:20.24 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 50688, appended 128 bytes
02:11:20.24 1678241473   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 311) mountpoint=/var/tmp/testdir
02:11:20.24 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53760, appended 176 bytes
02:11:20.24 1678241474   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241474   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 128 bytes
02:11:20.24 1678241476   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 38400, appended 144 bytes
02:11:20.24 1678241477   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 38400, appended 192 bytes
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 24064, appended 80 bytes
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485888, unflushed_frees 47104, appended 264 bytes
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 337920, unflushed_frees 48128, appended 208 bytes
02:11:20.24 1678241478   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 311) (bptree, mintxg=1)
02:11:20.24 1678241478   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241478   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:20.24 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241478   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 324)  
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 631296, appended 280 bytes
02:11:20.24 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:20.24 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:20.24 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:20.24 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:20.24 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:20.24 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:20.24 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:20.24 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:20.24 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:20.24 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 152 bytes
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41472, appended 160 bytes
02:11:20.24 1678241480   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:11:20.24 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:20.24 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
02:11:20.24 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:20.24 1678241480   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 249)  
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 176 bytes
02:11:20.24 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:20.24 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 168 bytes
02:11:20.24 1678241480   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 249) mountpoint=/var/tmp/testdir
02:11:20.24 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 144 bytes
02:11:20.24 =================================================================
02:11:20.24  End of zfs_dbgmsg log
02:11:20.24 =================================================================
02:11:20.24 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:20.24 =================================================================
02:11:20.24  Tailing last 200 lines of dmesg log
02:11:20.24 =================================================================
02:11:20.25 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:20.25 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:20.25 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:20.25 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:20.25 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:20.25 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:20.25 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:20.25 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:20.25 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:20.25 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:20.25 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:20.25 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:20.25 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:20.25 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:20.25 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:20.25 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:20.25 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:20.25 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:20.25 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:20.25 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:20.25 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:20.25 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:20.25 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:20.25 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:20.25 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:20.25 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:20.25 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:20.25 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:20.25 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:20.25 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:20.25 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:20.25 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:20.25 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:20.25 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:20.25 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:20.25 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:20.25 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:20.25 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:20.25 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:20.25 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:20.25 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:20.25 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:20.25 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:20.25 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:20.25 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:20.25 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:20.25 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:20.25 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:20.25 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:20.25 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:20.25 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:20.25 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:20.25 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:20.25 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:20.25 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:20.25 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:20.25 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:20.25 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:20.25 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:20.25 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:20.25 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:20.25 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:20.25 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:20.25 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:20.25 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:20.25 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:20.25 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:20.25 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:20.25 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:20.25 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:20.25 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:20.25 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:20.25 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:20.25 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:20.25 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:20.25 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:20.25 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:20.25 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:20.25 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:20.25 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:20.25 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:20.25 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:20.25 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:20.25 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:20.25 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:20.25 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:20.25 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:20.25 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:20.25 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:20.25 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:20.25 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:20.25 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:20.25 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:20.25 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:20.25 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:20.25 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:20.25 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:20.25 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:20.25 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:20.25 [ 1004.197669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:20.25 =================================================================
02:11:20.25  End of dmesg log
02:11:20.25 =================================================================
02:11:20.25 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:20.25 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:20.34 SUCCESS: zfs destroy -f testpool/testfs
02:11:20.34 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
02:11:22.93 ASSERTION: CM-not-UN FS: CI lookup succeeds only if (norm=same)
02:11:22.97 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.01 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.01 SUCCESS: create_file FïLëNÄmë
02:11:23.02 SUCCESS: lookup_file_ci FïLëNÄmë
02:11:23.02 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:11:23.02 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:23.02 =================================================================
02:11:23.02  Tailing last 200 lines of zfs_dbgmsg log
02:11:23.02 =================================================================
02:11:23.03 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45568, unflushed_frees 28672, appended 136 bytes
02:11:23.03 1678241472   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 214) (bptree, mintxg=1)
02:11:23.03 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 36352, appended 120 bytes
02:11:23.03 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 27136, appended 136 bytes
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 47104, appended 160 bytes
02:11:23.03 1678241472   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 204) (bptree, mintxg=1)
02:11:23.03 1678241472   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241472   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47104, appended 152 bytes
02:11:23.03 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241472   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 291)  
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31744, appended 104 bytes
02:11:23.03 1678241472   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 48640, appended 128 bytes
02:11:23.03 1678241472   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 291) mountpoint=/var/tmp/testdir
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 51200, appended 168 bytes
02:11:23.03 1678241472   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241472   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 300)  
02:11:23.03 1678241472   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 27136, appended 104 bytes
02:11:23.03 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48128, unflushed_frees 29696, appended 128 bytes
02:11:23.03 1678241473   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 300) (bptree, mintxg=1)
02:11:23.03 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55296, unflushed_frees 38400, appended 104 bytes
02:11:23.03 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29184, appended 112 bytes
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 49664, appended 144 bytes
02:11:23.03 1678241473   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 291) (bptree, mintxg=1)
02:11:23.03 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 144 bytes
02:11:23.03 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241473   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 311)  
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 104 bytes
02:11:23.03 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 50688, appended 128 bytes
02:11:23.03 1678241473   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 311) mountpoint=/var/tmp/testdir
02:11:23.03 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53760, appended 176 bytes
02:11:23.03 1678241474   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241474   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 128 bytes
02:11:23.03 1678241476   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 38400, appended 144 bytes
02:11:23.03 1678241477   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 38400, appended 192 bytes
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 24064, appended 80 bytes
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485888, unflushed_frees 47104, appended 264 bytes
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 337920, unflushed_frees 48128, appended 208 bytes
02:11:23.03 1678241478   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 311) (bptree, mintxg=1)
02:11:23.03 1678241478   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241478   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:23.03 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241478   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 324)  
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 631296, appended 280 bytes
02:11:23.03 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:23.03 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:23.03 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:23.03 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:23.03 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:23.03 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:23.03 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:23.03 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:23.03 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 152 bytes
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41472, appended 160 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:11:23.03 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 249)  
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 176 bytes
02:11:23.03 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 168 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 249) mountpoint=/var/tmp/testdir
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 144 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 38912, appended 176 bytes
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 40448, appended 184 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 249) (bptree, mintxg=1)
02:11:23.03 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 96 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 351)  
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 144 bytes
02:11:23.03 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 49664, appended 136 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 351) mountpoint=/var/tmp/testdir
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 37888, appended 144 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 39936, appended 160 bytes
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43008, appended 152 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 351) (bptree, mintxg=1)
02:11:23.03 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28160, appended 96 bytes
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 362)  
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 58880, appended 160 bytes
02:11:23.03 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 52224, appended 144 bytes
02:11:23.03 1678241480   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 362) mountpoint=/var/tmp/testdir
02:11:23.03 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39936, appended 144 bytes
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 176 bytes
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 43008, appended 144 bytes
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 362) (bptree, mintxg=1)
02:11:23.03 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 88 bytes
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 371)  
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 58368, appended 176 bytes
02:11:23.03 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 51712, appended 168 bytes
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 371) mountpoint=/var/tmp/testdir
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39424, appended 136 bytes
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 168 bytes
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43520, appended 160 bytes
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 371) (bptree, mintxg=1)
02:11:23.03 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29184, appended 88 bytes
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 379)  
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
02:11:23.03 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 136 bytes
02:11:23.03 1678241481   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 379) mountpoint=/var/tmp/testdir
02:11:23.03 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 40448, appended 136 bytes
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 41984, appended 144 bytes
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 44544, appended 144 bytes
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 379) (bptree, mintxg=1)
02:11:23.03 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 406)  
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 59904, appended 176 bytes
02:11:23.03 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 53760, appended 192 bytes
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 406) mountpoint=/var/tmp/testdir
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41472, appended 152 bytes
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 42496, appended 168 bytes
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 44032, appended 168 bytes
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 406) (bptree, mintxg=1)
02:11:23.03 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.03 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 521)  
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 59904, appended 144 bytes
02:11:23.03 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.03 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 53248, appended 144 bytes
02:11:23.03 1678241482   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 521) mountpoint=/var/tmp/testdir
02:11:23.03 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 41472, appended 144 bytes
02:11:23.04 =================================================================
02:11:23.04  End of zfs_dbgmsg log
02:11:23.04 =================================================================
02:11:23.04 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:23.04 =================================================================
02:11:23.04  Tailing last 200 lines of dmesg log
02:11:23.04 =================================================================
02:11:23.05 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:23.05 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:23.05 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:23.05 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:23.05 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:23.05 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:23.05 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:23.05 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:23.05 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:23.05 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:23.05 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:23.05 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:23.05 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:23.05 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:23.05 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:23.05 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:23.05 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:23.05 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:23.05 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:23.05 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:23.05 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:23.05 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:23.05 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:23.05 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:23.05 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:23.05 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:23.05 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:23.05 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:23.05 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:23.05 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:23.05 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:23.05 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:23.05 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:23.05 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:23.05 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:23.05 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:23.05 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:23.05 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:23.05 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:23.05 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:23.05 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:23.05 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:23.05 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:23.05 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:23.05 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:23.05 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:23.05 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:23.05 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:23.05 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:23.05 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:23.05 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:23.05 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:23.05 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:23.05 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:23.05 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:23.05 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:23.05 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:23.05 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:23.05 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:23.05 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:23.05 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:23.05 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:23.05 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:23.05 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:23.05 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:23.05 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:23.05 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:23.05 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:23.05 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:23.05 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:23.05 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:23.05 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:23.05 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:23.05 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:23.05 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:23.05 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:23.05 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:23.05 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:23.05 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:23.05 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:23.05 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:23.05 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:23.05 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:23.05 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:23.05 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:23.05 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:23.05 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:23.05 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:23.05 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:23.05 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:23.05 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:23.05 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:23.05 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:23.05 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:23.05 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:23.05 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:23.05 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:23.05 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:23.05 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:23.05 [ 1004.197669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:23.05 [ 1004.479235] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:11:23.05 [ 1004.859900] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:11:23.05 [ 1005.490416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:11:23.05 [ 1005.863997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:11:23.05 [ 1006.522071] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:11:23.05 [ 1007.031270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:11:23.05 =================================================================
02:11:23.05  End of dmesg log
02:11:23.05 =================================================================
02:11:23.05 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:23.05 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:23.14 SUCCESS: zfs destroy -f testpool/testfs
02:11:23.14 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
02:11:23.59 ASSERTION: CM-UN FS: lookup succeeds if (case=same)
02:11:23.63 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:23.68 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.68 SUCCESS: create_file FïLëNÄmë
02:11:23.68 SUCCESS: lookup_file FïLëNÄmë
02:11:23.69 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:23.69 SUCCESS: lookup_file fïlënämë exited 1
02:11:23.70 SUCCESS: lookup_file FïLëNÄmë
02:11:23.70 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:11:23.70 SUCCESS: lookup_file fïlënämë exited 1
02:11:23.71 SUCCESS: create_file FÏLËNÄMË
02:11:23.71 SUCCESS: lookup_file FïLëNÄmë exited 1
02:11:23.72 SUCCESS: lookup_file FÏLËNÄMË
02:11:23.72 SUCCESS: lookup_file fïlënämë exited 1
02:11:23.72 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:11:23.72 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:23.73 =================================================================
02:11:23.73  Tailing last 200 lines of zfs_dbgmsg log
02:11:23.73 =================================================================
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55296, unflushed_frees 38400, appended 104 bytes
02:11:23.74 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29184, appended 112 bytes
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 49664, appended 144 bytes
02:11:23.74 1678241473   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 291) (bptree, mintxg=1)
02:11:23.74 1678241473   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241473   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 144 bytes
02:11:23.74 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241473   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 311)  
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 104 bytes
02:11:23.74 1678241473   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241473   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 50688, appended 128 bytes
02:11:23.74 1678241473   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 311) mountpoint=/var/tmp/testdir
02:11:23.74 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53760, appended 176 bytes
02:11:23.74 1678241474   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241474   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 128 bytes
02:11:23.74 1678241476   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 38400, appended 144 bytes
02:11:23.74 1678241477   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 38400, appended 192 bytes
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 24064, appended 80 bytes
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485888, unflushed_frees 47104, appended 264 bytes
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 337920, unflushed_frees 48128, appended 208 bytes
02:11:23.74 1678241478   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 311) (bptree, mintxg=1)
02:11:23.74 1678241478   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241478   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:23.74 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241478   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 324)  
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 631296, appended 280 bytes
02:11:23.74 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:23.74 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:23.74 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:23.74 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:23.74 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:23.74 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:23.74 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:23.74 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:23.74 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 152 bytes
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41472, appended 160 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:11:23.74 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 249)  
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 176 bytes
02:11:23.74 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 168 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 249) mountpoint=/var/tmp/testdir
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 144 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 38912, appended 176 bytes
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 40448, appended 184 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 249) (bptree, mintxg=1)
02:11:23.74 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 96 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 351)  
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 144 bytes
02:11:23.74 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 49664, appended 136 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 351) mountpoint=/var/tmp/testdir
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 37888, appended 144 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 39936, appended 160 bytes
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43008, appended 152 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 351) (bptree, mintxg=1)
02:11:23.74 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28160, appended 96 bytes
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 362)  
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 58880, appended 160 bytes
02:11:23.74 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 52224, appended 144 bytes
02:11:23.74 1678241480   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 362) mountpoint=/var/tmp/testdir
02:11:23.74 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39936, appended 144 bytes
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 176 bytes
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 43008, appended 144 bytes
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 362) (bptree, mintxg=1)
02:11:23.74 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 88 bytes
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 371)  
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 58368, appended 176 bytes
02:11:23.74 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 51712, appended 168 bytes
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 371) mountpoint=/var/tmp/testdir
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39424, appended 136 bytes
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 168 bytes
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43520, appended 160 bytes
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 371) (bptree, mintxg=1)
02:11:23.74 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29184, appended 88 bytes
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 379)  
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
02:11:23.74 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 136 bytes
02:11:23.74 1678241481   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 379) mountpoint=/var/tmp/testdir
02:11:23.74 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 40448, appended 136 bytes
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 41984, appended 144 bytes
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 44544, appended 144 bytes
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 379) (bptree, mintxg=1)
02:11:23.74 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 406)  
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 59904, appended 176 bytes
02:11:23.74 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 53760, appended 192 bytes
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 406) mountpoint=/var/tmp/testdir
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41472, appended 152 bytes
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 42496, appended 168 bytes
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 44032, appended 168 bytes
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 406) (bptree, mintxg=1)
02:11:23.74 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 521)  
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 59904, appended 144 bytes
02:11:23.74 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 53248, appended 144 bytes
02:11:23.74 1678241482   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 521) mountpoint=/var/tmp/testdir
02:11:23.74 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 41472, appended 144 bytes
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 60928, unflushed_frees 44032, appended 168 bytes
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 46080, appended 168 bytes
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 521) (bptree, mintxg=1)
02:11:23.74 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 31744, appended 96 bytes
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 417)  
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 60928, appended 192 bytes
02:11:23.74 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 54784, appended 200 bytes
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 417) mountpoint=/var/tmp/testdir
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 41984, appended 152 bytes
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 61440, unflushed_frees 43520, appended 192 bytes
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 47104, appended 192 bytes
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 417) (bptree, mintxg=1)
02:11:23.74 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.74 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 33280, appended 120 bytes
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 535)  
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 61440, appended 200 bytes
02:11:23.74 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.74 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 55808, appended 200 bytes
02:11:23.74 1678241483   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 535) mountpoint=/var/tmp/testdir
02:11:23.74 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 43520, appended 152 bytes
02:11:23.74 =================================================================
02:11:23.74  End of zfs_dbgmsg log
02:11:23.74 =================================================================
02:11:23.74 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:23.74 =================================================================
02:11:23.74  Tailing last 200 lines of dmesg log
02:11:23.74 =================================================================
02:11:23.75 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:23.75 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:23.75 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:23.75 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:23.75 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:23.75 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:23.75 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:23.75 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:23.75 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:23.75 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:23.75 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:23.75 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:23.75 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:23.75 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:23.75 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:23.75 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:23.75 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:23.75 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:23.75 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:23.75 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:23.75 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:23.75 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:23.75 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:23.75 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:23.75 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:23.75 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:23.75 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:23.75 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:23.75 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:23.75 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:23.75 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:23.75 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:23.75 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:23.75 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:23.75 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:23.75 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:23.75 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:23.75 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:23.75 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:23.75 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:23.75 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:23.75 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:23.75 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:23.75 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:23.75 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:23.75 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:23.75 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:23.75 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:23.75 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:23.75 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:23.75 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:23.75 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:23.75 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:23.75 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:23.75 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:23.75 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:23.75 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:23.75 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:23.75 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:23.75 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:23.75 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:23.75 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:23.75 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:23.75 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:23.75 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:23.75 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:23.75 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:23.75 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:23.75 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:23.75 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:23.75 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:23.75 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:23.75 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:23.75 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:23.75 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:23.75 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:23.75 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:23.75 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:23.75 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:23.75 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:23.75 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:23.75 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:23.75 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:23.75 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:23.75 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:23.75 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:23.75 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:23.75 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:23.75 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:23.75 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:23.75 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:23.75 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:23.75 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:23.75 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:23.75 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:23.75 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:23.75 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:23.75 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:23.75 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:23.75 [ 1004.197669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:23.75 [ 1004.479235] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:11:23.75 [ 1004.859900] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:11:23.75 [ 1005.490416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:11:23.75 [ 1005.863997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:11:23.75 [ 1006.522071] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:11:23.75 [ 1007.031270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:11:23.75 [ 1007.278811] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:11:23.75 [ 1007.699194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:11:23.75 =================================================================
02:11:23.75  End of dmesg log
02:11:23.75 =================================================================
02:11:23.75 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:23.75 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:23.84 SUCCESS: zfs destroy -f testpool/testfs
02:11:23.85 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
02:11:23.88 ASSERTION: CM-UN FS: CI lookup succeeds using any name form
02:11:23.92 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:23.96 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.96 SUCCESS: create_file FïLëNÄmë
02:11:23.97 SUCCESS: lookup_file_ci FïLëNÄmë
02:11:23.97 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:11:23.97 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:23.97 =================================================================
02:11:23.97  Tailing last 200 lines of zfs_dbgmsg log
02:11:23.97 =================================================================
02:11:23.98 1678241473   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53760, appended 176 bytes
02:11:23.98 1678241474   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.98 1678241474   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 128 bytes
02:11:23.98 1678241476   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 38400, appended 144 bytes
02:11:23.98 1678241477   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 38400, appended 192 bytes
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 24064, appended 80 bytes
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485888, unflushed_frees 47104, appended 264 bytes
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 337920, unflushed_frees 48128, appended 208 bytes
02:11:23.98 1678241478   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 311) (bptree, mintxg=1)
02:11:23.98 1678241478   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.98 1678241478   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 72 bytes
02:11:23.98 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.98 1678241478   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 324)  
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 631296, appended 280 bytes
02:11:23.98 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.98 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:23.98 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:23.98 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:23.98 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.98 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:23.98 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:23.98 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:23.98 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.98 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:23.98 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:23.98 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.98 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:23.99 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:23.99 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:23.99 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:23.99 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:23.99 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:23.99 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:23.99 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:23.99 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:23.99 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 152 bytes
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41472, appended 160 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:11:23.99 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 249)  
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 176 bytes
02:11:23.99 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 168 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 249) mountpoint=/var/tmp/testdir
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 144 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 38912, appended 176 bytes
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 40448, appended 184 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 249) (bptree, mintxg=1)
02:11:23.99 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 96 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 351)  
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 144 bytes
02:11:23.99 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 49664, appended 136 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 351) mountpoint=/var/tmp/testdir
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 37888, appended 144 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 39936, appended 160 bytes
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43008, appended 152 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 351) (bptree, mintxg=1)
02:11:23.99 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28160, appended 96 bytes
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 362)  
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 58880, appended 160 bytes
02:11:23.99 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 52224, appended 144 bytes
02:11:23.99 1678241480   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 362) mountpoint=/var/tmp/testdir
02:11:23.99 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39936, appended 144 bytes
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 176 bytes
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 43008, appended 144 bytes
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 362) (bptree, mintxg=1)
02:11:23.99 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 88 bytes
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 371)  
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 58368, appended 176 bytes
02:11:23.99 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 51712, appended 168 bytes
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 371) mountpoint=/var/tmp/testdir
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39424, appended 136 bytes
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 168 bytes
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43520, appended 160 bytes
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 371) (bptree, mintxg=1)
02:11:23.99 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29184, appended 88 bytes
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 379)  
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
02:11:23.99 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 136 bytes
02:11:23.99 1678241481   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 379) mountpoint=/var/tmp/testdir
02:11:23.99 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 40448, appended 136 bytes
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 41984, appended 144 bytes
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 44544, appended 144 bytes
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 379) (bptree, mintxg=1)
02:11:23.99 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 406)  
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 59904, appended 176 bytes
02:11:23.99 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 53760, appended 192 bytes
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 406) mountpoint=/var/tmp/testdir
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41472, appended 152 bytes
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 42496, appended 168 bytes
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 44032, appended 168 bytes
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 406) (bptree, mintxg=1)
02:11:23.99 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 521)  
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 59904, appended 144 bytes
02:11:23.99 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 53248, appended 144 bytes
02:11:23.99 1678241482   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 521) mountpoint=/var/tmp/testdir
02:11:23.99 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 41472, appended 144 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 60928, unflushed_frees 44032, appended 168 bytes
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 46080, appended 168 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 521) (bptree, mintxg=1)
02:11:23.99 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 31744, appended 96 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 417)  
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 60928, appended 192 bytes
02:11:23.99 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 54784, appended 200 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 417) mountpoint=/var/tmp/testdir
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 41984, appended 152 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 61440, unflushed_frees 43520, appended 192 bytes
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 47104, appended 192 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 417) (bptree, mintxg=1)
02:11:23.99 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 33280, appended 120 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 535)  
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 61440, appended 200 bytes
02:11:23.99 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 55808, appended 200 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 535) mountpoint=/var/tmp/testdir
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 43520, appended 152 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 62464, unflushed_frees 44544, appended 200 bytes
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 46592, appended 208 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 535) (bptree, mintxg=1)
02:11:23.99 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:23.99 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 32768, appended 96 bytes
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 545)  
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46080, unflushed_frees 62464, appended 176 bytes
02:11:23.99 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:23.99 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 56320, appended 176 bytes
02:11:23.99 1678241483   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 545) mountpoint=/var/tmp/testdir
02:11:23.99 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 44032, appended 160 bytes
02:11:23.99 =================================================================
02:11:23.99  End of zfs_dbgmsg log
02:11:23.99 =================================================================
02:11:23.99 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:23.99 =================================================================
02:11:23.99  Tailing last 200 lines of dmesg log
02:11:23.99 =================================================================
02:11:24.00 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:24.00 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:24.00 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:24.00 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:24.00 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:24.00 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:24.00 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:24.00 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:24.00 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:24.00 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:24.00 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:24.00 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:24.00 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:24.00 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:24.00 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:24.00 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:24.00 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:24.00 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:24.00 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:24.00 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:24.00 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:24.00 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:24.00 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:24.00 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:24.00 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:24.00 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:24.00 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:24.00 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:24.00 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:24.00 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:24.00 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:24.00 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:24.00 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:24.00 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:24.00 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:24.00 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:24.00 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:24.00 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:24.00 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:24.00 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:24.00 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:24.00 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:24.00 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:24.00 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:24.00 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:24.00 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:24.00 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:24.00 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:24.00 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:24.00 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:24.00 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:24.00 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:24.00 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:24.00 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:24.00 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:24.00 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:24.00 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:24.00 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:24.00 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:24.00 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:24.00 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:24.00 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:24.00 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:24.00 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:24.00 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:24.00 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:24.00 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:24.00 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:24.00 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:24.00 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:24.00 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:24.00 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:24.00 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:24.00 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:24.00 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:24.00 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:24.00 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:24.00 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:24.00 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:24.00 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:24.00 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:24.00 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:24.00 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:24.00 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:24.00 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:24.00 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:24.00 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:24.00 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:24.00 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:24.00 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:24.00 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:24.00 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:24.00 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:24.00 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:24.00 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:24.00 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:24.00 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:24.00 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:24.00 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:24.00 [ 1004.197669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:24.00 [ 1004.479235] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:11:24.00 [ 1004.859900] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:11:24.00 [ 1005.490416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:11:24.00 [ 1005.863997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:11:24.00 [ 1006.522071] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:11:24.00 [ 1007.031270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:11:24.00 [ 1007.278811] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:11:24.00 [ 1007.699194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:11:24.00 [ 1007.980941] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
02:11:24.00 =================================================================
02:11:24.00  End of dmesg log
02:11:24.00 =================================================================
02:11:24.00 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:24.00 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:24.09 SUCCESS: zfs destroy -f testpool/testfs
02:11:24.09 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
02:11:24.13 ASSERTION: CM-UN FS: delete succeeds if (case=same)
02:11:24.17 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:24.22 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.23 SUCCESS: create_file FïLëNÄmë
02:11:24.24 SUCCESS: delete_file FïLëNÄmë
02:11:24.24 SUCCESS: lookup_any exited 1
02:11:24.24 SUCCESS: create_file FïLëNÄmë
02:11:24.25 SUCCESS: delete_file FÏLËNÄMË exited 1
02:11:24.25 SUCCESS: create_file FïLëNÄmë
02:11:24.26 SUCCESS: delete_file fïlënämë exited 1
02:11:24.26 SUCCESS: create_file FïLëNÄmë
02:11:24.27 ERROR: delete_file FïLëNÄmë exited 1
02:11:24.27 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:11:24.27 =================================================================
02:11:24.27  Tailing last 200 lines of zfs_dbgmsg log
02:11:24.27 =================================================================
02:11:24.28 1678241478   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241478   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:24.28 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 632320, appended 296 bytes
02:11:24.28 1678241478   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 324) mountpoint=/var/tmp/testdir
02:11:24.28 1678241478   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35328, appended 144 bytes
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37888, appended 192 bytes
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 39936, appended 176 bytes
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 324) (bptree, mintxg=1)
02:11:24.28 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 88 bytes
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 232)  
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 53760, appended 160 bytes
02:11:24.28 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 48128, appended 152 bytes
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 232) mountpoint=/var/tmp/testdir
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 37888, appended 152 bytes
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 39936, appended 144 bytes
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 232) (bptree, mintxg=1)
02:11:24.28 1678241479   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241479   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 96 bytes
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 338)  
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55296, appended 144 bytes
02:11:24.28 1678241479   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241479   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 128 bytes
02:11:24.28 1678241479   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:11:24.28 1678241479   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 144 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 152 bytes
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41472, appended 160 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:11:24.28 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 249)  
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 176 bytes
02:11:24.28 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 168 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 249) mountpoint=/var/tmp/testdir
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 37376, appended 144 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 38912, appended 176 bytes
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 40448, appended 184 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 249) (bptree, mintxg=1)
02:11:24.28 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 96 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 351)  
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39424, unflushed_frees 56320, appended 144 bytes
02:11:24.28 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 49664, appended 136 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 351) mountpoint=/var/tmp/testdir
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 37888, appended 144 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 39936, appended 160 bytes
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43008, appended 152 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 351) (bptree, mintxg=1)
02:11:24.28 1678241480   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241480   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28160, appended 96 bytes
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 362)  
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 58880, appended 160 bytes
02:11:24.28 1678241480   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241480   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 52224, appended 144 bytes
02:11:24.28 1678241480   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 362) mountpoint=/var/tmp/testdir
02:11:24.28 1678241480   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39936, appended 144 bytes
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 176 bytes
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 43008, appended 144 bytes
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 362) (bptree, mintxg=1)
02:11:24.28 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 88 bytes
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 371)  
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 58368, appended 176 bytes
02:11:24.28 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 51712, appended 168 bytes
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 371) mountpoint=/var/tmp/testdir
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39424, appended 136 bytes
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 168 bytes
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43520, appended 160 bytes
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 371) (bptree, mintxg=1)
02:11:24.28 1678241481   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241481   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29184, appended 88 bytes
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 379)  
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
02:11:24.28 1678241481   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241481   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 136 bytes
02:11:24.28 1678241481   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 379) mountpoint=/var/tmp/testdir
02:11:24.28 1678241481   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 40448, appended 136 bytes
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 41984, appended 144 bytes
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 44544, appended 144 bytes
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 379) (bptree, mintxg=1)
02:11:24.28 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 406)  
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 59904, appended 176 bytes
02:11:24.28 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 53760, appended 192 bytes
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 406) mountpoint=/var/tmp/testdir
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41472, appended 152 bytes
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 42496, appended 168 bytes
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 44032, appended 168 bytes
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 406) (bptree, mintxg=1)
02:11:24.28 1678241482   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241482   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 521)  
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 59904, appended 144 bytes
02:11:24.28 1678241482   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241482   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 53248, appended 144 bytes
02:11:24.28 1678241482   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 521) mountpoint=/var/tmp/testdir
02:11:24.28 1678241482   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 41472, appended 144 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 60928, unflushed_frees 44032, appended 168 bytes
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 46080, appended 168 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 521) (bptree, mintxg=1)
02:11:24.28 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 31744, appended 96 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 417)  
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 60928, appended 192 bytes
02:11:24.28 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51200, unflushed_frees 54784, appended 200 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 417) mountpoint=/var/tmp/testdir
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 41984, appended 152 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 61440, unflushed_frees 43520, appended 192 bytes
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 47104, appended 192 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 417) (bptree, mintxg=1)
02:11:24.28 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 33280, appended 120 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 535)  
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 61440, appended 200 bytes
02:11:24.28 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50176, unflushed_frees 55808, appended 200 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 535) mountpoint=/var/tmp/testdir
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 43520, appended 152 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 62464, unflushed_frees 44544, appended 200 bytes
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 46592, appended 208 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 535) (bptree, mintxg=1)
02:11:24.28 1678241483   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241483   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 32768, appended 96 bytes
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 545)  
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46080, unflushed_frees 62464, appended 176 bytes
02:11:24.28 1678241483   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241483   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52736, unflushed_frees 56320, appended 176 bytes
02:11:24.28 1678241483   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 545) mountpoint=/var/tmp/testdir
02:11:24.28 1678241483   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 44032, appended 160 bytes
02:11:24.28 1678241484   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 169, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 62976, unflushed_frees 46080, appended 184 bytes
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 170, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 53760, unflushed_frees 49152, appended 176 bytes
02:11:24.28 1678241484   spa_history.c:297:spa_history_log_sync(): txg 171 destroy testpool/testfs (id 545) (bptree, mintxg=1)
02:11:24.28 1678241484   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:11:24.28 1678241484   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 171; err=0
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 171, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 33792, appended 104 bytes
02:11:24.28 1678241484   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:11:24.28 1678241484   spa_history.c:297:spa_history_log_sync(): txg 172 create testpool/testfs (id 558)  
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 172, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46592, unflushed_frees 62976, appended 160 bytes
02:11:24.28 1678241484   spa_history.c:329:spa_history_log_sync(): ioctl create
02:11:24.28 1678241484   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 173, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 57344, appended 144 bytes
02:11:24.28 1678241484   spa_history.c:297:spa_history_log_sync(): txg 174 set testpool/testfs (id 558) mountpoint=/var/tmp/testdir
02:11:24.28 1678241484   metaslab.c:3926:metaslab_flush(): flushing: txg 174, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 45056, appended 136 bytes
02:11:24.28 =================================================================
02:11:24.28  End of zfs_dbgmsg log
02:11:24.28 =================================================================
02:11:24.29 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:11:24.29 =================================================================
02:11:24.29  Tailing last 200 lines of dmesg log
02:11:24.29 =================================================================
02:11:24.30 [  360.997417] loop0: detected capacity change from 0 to 6291456
02:11:24.30 [  361.024278] loop1: detected capacity change from 0 to 6291456
02:11:24.30 [  361.051724] loop2: detected capacity change from 0 to 6291456
02:11:24.30 [  361.227008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:11:24.30 [  397.554096] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:11:24.30 [  398.451961] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:11:24.30 [  399.101314] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:11:24.30 [  399.684261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:11:24.30 [  402.446777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:11:24.30 [  402.566058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:11:24.30 [  402.654950] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:11:24.30 [  402.763799] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:11:24.30 [  402.833735] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:11:24.30 [  403.239854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:11:24.30 [  405.910754] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:11:24.30 [  406.032592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:11:24.30 [  406.124053] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:11:24.30 [  406.229874] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:11:24.30 [  406.301097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:11:24.30 [  406.720121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:11:24.30 [  406.765982] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:11:24.30 [  409.236097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:11:24.30 [  415.643144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:11:24.30 [  416.566889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:11:24.30 [  417.125387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:11:24.30 [  417.937241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:11:24.30 [  418.230925] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:11:24.30 [  428.560059] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:11:24.30 [  429.169036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:11:24.30 [  436.925772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:11:24.30 [  437.606984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:11:24.30 [  437.892264] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:11:24.30 [  564.929088] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:11:24.30 [  581.383112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:11:24.30 [  581.467671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:11:24.30 [  581.753534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:11:24.30 [  581.868755] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:11:24.30 [  581.909483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:11:24.30 [  582.152507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:11:24.30 [  582.420170] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:11:24.30 [  583.069144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:11:24.30 [  583.373511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:11:24.30 [  583.829563] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:11:24.30 [  583.963662] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:11:24.30 [  584.189978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:24.30 [  584.421386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:11:24.30 [  594.955821] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:11:24.30 [  601.417638] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:11:24.30 [  608.005753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:11:24.30 [  618.670753] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:24.30 [  618.898865] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:11:24.30 [  619.135449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:11:24.30 [  629.675011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:11:24.30 [  640.336764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:11:24.30 [  640.564121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:11:24.30 [  640.592255] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:11:24.30 [  642.137197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:11:24.30 [  644.248198] debugfs: Directory 'zd0' with parent 'block' already present!
02:11:24.30 [  644.873915] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:11:24.30 [  646.644223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:11:24.30 [  647.233030] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:11:24.30 [  653.767343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:11:24.30 [  659.482647] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:11:24.30 [  659.834527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:11:24.30 [  661.896984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:11:24.30 [  661.922013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:11:24.30 [  701.192888] loop3: detected capacity change from 0 to 8
02:11:24.30 [  701.642701] audit: type=1400 audit(1678241177.521:101): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=46040 comm="apparmor_parser"
02:11:24.30 [  701.661294] audit: type=1400 audit(1678241177.541:102): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=46040 comm="apparmor_parser"
02:11:24.30 [  843.160775] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:11:24.30 [  846.306365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:11:24.30 [  849.609075] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:11:24.30 [  862.851583] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:11:24.30 [  872.764003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:11:24.30 [  883.172596] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:11:24.30 [  884.759658] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:11:24.30 [  886.515921] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:11:24.30 [  908.279262] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:11:24.30 [  909.052997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:11:24.30 [  913.571852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:11:24.30 [  932.415892] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:11:24.30 [  933.158343] loop3: detected capacity change from 0 to 524288
02:11:24.30 [  933.432888] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:11:24.30 [  943.518985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:11:24.30 [  943.895947] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 3842823860920699493), resetting them to the default (8388608)
02:11:24.30 [  986.005890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:11:24.30 [  986.352989] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:11:24.30 [  986.439823] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:11:24.30 [  988.491335] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:11:24.30 [  990.488209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:11:24.30 [  992.562794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:11:24.30 [  994.115452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:11:24.30 [  994.186403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:11:24.30 [  994.378424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:11:24.30 [  994.983502] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:11:24.30 [  997.269490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:11:24.30 [ 1002.981682] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:11:24.30 [ 1003.489526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:11:24.30 [ 1003.912080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:11:24.30 [ 1004.197669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:11:24.30 [ 1004.479235] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:11:24.30 [ 1004.859900] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:11:24.30 [ 1005.490416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:11:24.30 [ 1005.863997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:11:24.30 [ 1006.522071] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:11:24.30 [ 1007.031270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:11:24.30 [ 1007.278811] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:11:24.30 [ 1007.699194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:11:24.30 [ 1007.980941] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
02:11:24.30 [ 1008.228657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete
02:11:24.30 =================================================================
02:11:24.30  End of dmesg log
02:11:24.30 =================================================================
02:11:24.30 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:11:24.30 NOTE: Performing local cleanup via log_onexit (cleanup)
02:11:24.39 SUCCESS: zfs destroy -f testpool/testfs
02:11:24.39 SUCCESS: rm -rf /var/tmp/testdir
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
</pre></small></details>
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_010_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_deeply_nested (run as root) [01:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_003_pos (run as root) [00:17] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_001_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_005_neg (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_016_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_clone_livelist (run as root) [01:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_changes (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_timestamp (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_types (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_mangle (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_001_pos (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_002_pos (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_005_neg (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_008_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_009_pos (run as root) [01:27] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_001_pos (run as root) [00:54] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_007_pos (run as root) [00:07] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/compression_001_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_001_neg (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/ro_props_001_pos (run as root) [01:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_004_neg (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_wait/zfs_wait_deleteq (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos (run as root) [00:40] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_009_neg (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_023_neg (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_024_pos (run as root) [00:59] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_crypt_combos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos (run as root) [02:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg (run as root) [01:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4 (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed (run as root) [01:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:15] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_attach_detach_add_remove (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_fault_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_import_export (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_split (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_suspend_resume (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_unsupported_vdevs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_checksums (run as root) [00:21] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace_prop_ashift (run as root) [01:23] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_resilver (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_003_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_004_pos (run as root) [01:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_007_pos (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_008_pos (run as root) [01:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_discard (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_freeing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_multiple (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove_cancel (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_basic (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace_cancel (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_rebuild (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_resilver (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_basic (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos (run as root) [02:07] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive (run as root) [03:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos (run as root) [00:42] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_children (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.terminate_by_signal (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_edonr_test (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_sha2_test (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_skein_test (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_blake3_test (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_001_pos (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_002_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_004_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/setup (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/setup (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_001_pos (run as runner) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc_disabled (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted_no_compressed_arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cp_files_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/crtime_001_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/ctime_001_pos (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_ratelimit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_sync (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_zio (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/setup (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_002_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_005_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_007_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_010_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_011_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_012_neg (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_003_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/async_destroy_001_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_009_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_002_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_003_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_010_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/inherit_001_pos (run as root) [01:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_008_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_009_pos (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/sync (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/psync (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/posixaio (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/mmap (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_limit (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_001 (run as root) [00:19] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_seek_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_sync_001_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_write_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [01:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [01:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [03:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:44] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [04:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [04:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_invalid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_lun_expsz (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_open (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_ro_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_vdev_add (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zdb (run as root) [01:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zhack_feat (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_001_pos (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_002_neg (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
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

<pre>

Tests with results other than PASS that are expected:
    FAIL casenorm/mixed_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_none_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_lookup (https://github.com/openzfs/zfs/issues/7633)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
</pre>
<details><summary>Error Listings</summary><small><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
02:01:57.43 ASSERTION: CS-UN FS: lookup succeeds if (case=same)
02:01:57.46 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:01:57.50 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.50 SUCCESS: create_file FïLëNÄmë
02:01:57.51 SUCCESS: lookup_file FïLëNÄmë
02:01:57.51 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:01:57.51 SUCCESS: lookup_file fïlënämë exited 1
02:01:57.51 SUCCESS: lookup_file FïLëNÄmë
02:01:57.52 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:01:57.52 SUCCESS: lookup_file fïlënämë exited 1
02:01:57.52 SUCCESS: create_file FÏLËNÄMË
02:01:57.53 SUCCESS: lookup_file FïLëNÄmë exited 1
02:01:57.53 SUCCESS: lookup_file FÏLËNÄMË
02:01:57.53 SUCCESS: lookup_file fïlënämë exited 1
02:01:57.53 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:01:57.53 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:01:57.54 =================================================================
02:01:57.54  Tailing last 200 lines of zfs_dbgmsg log
02:01:57.54 =================================================================
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 32, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22016, unflushed_frees 17408, appended 80 bytes
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 33 create testpool/testfs (id 121)  
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 33, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29696, unflushed_frees 43008, appended 136 bytes
02:01:57.55 1678240909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 34, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 42496, unflushed_frees 47104, appended 144 bytes
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 35 set testpool/testfs (id 121) mountpoint=/var/tmp/testdir
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 35, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 23552, unflushed_frees 27648, appended 120 bytes
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 36, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 47104, unflushed_frees 29696, appended 144 bytes
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 37 destroy testpool/testfs (id 121) (bptree, mintxg=1)
02:01:57.55 1678240909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 37; err=0
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 37, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 29184, unflushed_frees 24576, appended 128 bytes
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 262)  
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 23552, unflushed_frees 23552, appended 104 bytes
02:01:57.55 1678240909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 42496, unflushed_frees 47104, appended 136 bytes
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 262) mountpoint=/var/tmp/testdir
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 47104, appended 152 bytes
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 23552, appended 112 bytes
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 262) (bptree, mintxg=1)
02:01:57.55 1678240909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 24576, appended 128 bytes
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 274)  
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 43008, appended 128 bytes
02:01:57.55 1678240909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 28160, appended 104 bytes
02:01:57.55 1678240909   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 274) mountpoint=/var/tmp/testdir
02:01:57.55 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 47104, appended 168 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 30720, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 274) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 18944, appended 88 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 158)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 31744, unflushed_frees 44544, appended 128 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 48640, appended 136 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 158) mountpoint=/var/tmp/testdir
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29696, appended 128 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 284)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 32256, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 27648, appended 128 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 284) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 20480, appended 96 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 39936, appended 176 bytes
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 46080, appended 152 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 158) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 26624, appended 152 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 294)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 25600, unflushed_frees 43520, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 43520, appended 136 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 294) mountpoint=/var/tmp/testdir
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31232, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 173)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 32256, appended 168 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 28160, appended 136 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 173) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 104 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 41472, appended 184 bytes
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47104, appended 160 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 294) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 185)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 26624, unflushed_frees 44032, appended 136 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 44544, appended 136 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 185) mountpoint=/var/tmp/testdir
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 32256, appended 128 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 305)  
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 33792, appended 160 bytes
02:01:57.55 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 29184, appended 144 bytes
02:01:57.55 1678240910   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 305) (bptree, mintxg=1)
02:01:57.55 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 88 bytes
02:01:57.55 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 41472, appended 184 bytes
02:01:57.55 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 47616, appended 160 bytes
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 185) (bptree, mintxg=1)
02:01:57.55 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 28160, appended 144 bytes
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 318)  
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 28160, unflushed_frees 44032, appended 136 bytes
02:01:57.55 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 45568, appended 128 bytes
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 318) mountpoint=/var/tmp/testdir
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 33280, appended 136 bytes
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 327)  
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 34816, appended 160 bytes
02:01:57.55 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 30208, appended 144 bytes
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 327) (bptree, mintxg=1)
02:01:57.55 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 24576, appended 88 bytes
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 44544, appended 168 bytes
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 50176, appended 152 bytes
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 318) (bptree, mintxg=1)
02:01:57.55 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 136 bytes
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 338)  
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46080, appended 120 bytes
02:01:57.55 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 46592, appended 136 bytes
02:01:57.55 1678240911   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:01:57.55 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 34816, appended 128 bytes
02:01:57.55 1678240912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240912   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 35840, appended 144 bytes
02:01:57.55 1678240913   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 188416, unflushed_frees 37888, appended 136 bytes
02:01:57.55 1678240915   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24064, appended 80 bytes
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 486400, unflushed_frees 42496, appended 280 bytes
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 486912, unflushed_frees 47104, appended 328 bytes
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 96 bytes
02:01:57.55 1678240916   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:01:57.55 1678240916   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240916   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 191488, unflushed_frees 44032, appended 232 bytes
02:01:57.55 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240916   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 349)  
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 632320, appended 344 bytes
02:01:57.55 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:01:57.55 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:01:57.55 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:01:57.55 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:01:57.55 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:01:57.55 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.55 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:01:57.55 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.55 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:01:57.55 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:01:57.55 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:01:57.55 =================================================================
02:01:57.55  End of zfs_dbgmsg log
02:01:57.55 =================================================================
02:01:57.55 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:01:57.55 =================================================================
02:01:57.55  Tailing last 200 lines of dmesg log
02:01:57.55 =================================================================
02:01:57.56 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:01:57.56 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:01:57.56 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:01:57.56 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:01:57.56 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:01:57.56 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:01:57.56 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:01:57.56 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:01:57.56 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:01:57.56 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:01:57.56 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:01:57.56 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:01:57.56 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:01:57.56 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:01:57.56 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:01:57.56 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:01:57.56 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:01:57.56 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:01:57.56 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:01:57.56 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:01:57.56 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:01:57.56 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:01:57.56 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:01:57.56 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:01:57.56 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:01:57.56 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:01:57.56 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:01:57.56 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:01:57.56 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:01:57.56 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:01:57.56 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:01:57.56 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:01:57.56 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:01:57.56 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:01:57.56 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:01:57.56 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:01:57.56 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:01:57.56 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:01:57.56 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:01:57.56 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:01:57.56 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:01:57.56 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:01:57.56 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:01:57.56 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:01:57.56 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:01:57.56 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:01:57.56 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:01:57.56 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:01:57.56 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:01:57.56 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:01:57.56 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:01:57.56 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:01:57.56 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:01:57.56 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:01:57.56 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:01:57.56 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:01:57.56 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:01:57.56 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:01:57.56 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:01:57.56 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:01:57.56 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:01:57.56 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:01:57.56 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:01:57.56 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:01:57.56 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:01:57.56 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:01:57.56 [  817.131032] loop3: detected capacity change from 0 to 8
02:01:57.56 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:01:57.56 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:01:57.56 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:01:57.56 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:01:57.56 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:01:57.56 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:01:57.56 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:01:57.56 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:01:57.56 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:01:57.56 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:01:57.56 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:01:57.56 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:01:57.56 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:01:57.56 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:01:57.56 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:01:57.56 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:01:57.56 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:01:57.56 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:01:57.56 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:01:57.56 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:01:57.56 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:01:57.56 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:01:57.56 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:01:57.56 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:01:57.56 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:01:57.56 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:01:57.56 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:01:57.56 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:01:57.56 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:01:57.56 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:01:57.56 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:01:57.56 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:01:57.56 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:01:57.56 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:01:57.56 =================================================================
02:01:57.56  End of dmesg log
02:01:57.56 =================================================================
02:01:57.56 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:01:57.56 NOTE: Performing local cleanup via log_onexit (cleanup)
02:01:57.65 SUCCESS: zfs destroy -f testpool/testfs
02:01:57.65 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
02:01:57.68 ASSERTION: CS-UN FS: delete succeeds if (case=same)
02:01:57.72 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:01:57.76 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.76 SUCCESS: create_file FïLëNÄmë
02:01:57.76 SUCCESS: delete_file FïLëNÄmë
02:01:57.77 SUCCESS: lookup_any exited 1
02:01:57.77 SUCCESS: create_file FïLëNÄmë
02:01:57.77 SUCCESS: delete_file FÏLËNÄMË exited 1
02:01:57.78 SUCCESS: create_file FïLëNÄmë
02:01:57.78 SUCCESS: delete_file fïlënämë exited 1
02:01:57.79 SUCCESS: create_file FïLëNÄmë
02:01:57.79 ERROR: delete_file FïLëNÄmë exited 1
02:01:57.79 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:01:57.79 =================================================================
02:01:57.79  Tailing last 200 lines of zfs_dbgmsg log
02:01:57.79 =================================================================
02:01:57.80 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240909   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 262)  
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 23552, unflushed_frees 23552, appended 104 bytes
02:01:57.80 1678240909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 42496, unflushed_frees 47104, appended 136 bytes
02:01:57.80 1678240909   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 262) mountpoint=/var/tmp/testdir
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 47104, appended 152 bytes
02:01:57.80 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 23552, appended 112 bytes
02:01:57.80 1678240909   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 262) (bptree, mintxg=1)
02:01:57.80 1678240909   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240909   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 24576, appended 128 bytes
02:01:57.80 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240909   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 274)  
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 43008, appended 128 bytes
02:01:57.80 1678240909   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240909   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 28160, appended 104 bytes
02:01:57.80 1678240909   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 274) mountpoint=/var/tmp/testdir
02:01:57.80 1678240909   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 47104, appended 168 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 30720, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 274) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 18944, appended 88 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 158)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 31744, unflushed_frees 44544, appended 128 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 48640, appended 136 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 158) mountpoint=/var/tmp/testdir
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29696, appended 128 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 284)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 32256, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 27648, appended 128 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 284) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 20480, appended 96 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 39936, appended 176 bytes
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 46080, appended 152 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 158) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 26624, appended 152 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 294)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 25600, unflushed_frees 43520, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 43520, appended 136 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 294) mountpoint=/var/tmp/testdir
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31232, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 173)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 32256, appended 168 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 28160, appended 136 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 173) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 104 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 41472, appended 184 bytes
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47104, appended 160 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 294) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 185)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 26624, unflushed_frees 44032, appended 136 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 44544, appended 136 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 185) mountpoint=/var/tmp/testdir
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 32256, appended 128 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 305)  
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 33792, appended 160 bytes
02:01:57.80 1678240910   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 29184, appended 144 bytes
02:01:57.80 1678240910   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 305) (bptree, mintxg=1)
02:01:57.80 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 88 bytes
02:01:57.80 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 41472, appended 184 bytes
02:01:57.80 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 47616, appended 160 bytes
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 185) (bptree, mintxg=1)
02:01:57.80 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 28160, appended 144 bytes
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 318)  
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 28160, unflushed_frees 44032, appended 136 bytes
02:01:57.80 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 45568, appended 128 bytes
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 318) mountpoint=/var/tmp/testdir
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 33280, appended 136 bytes
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 327)  
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 34816, appended 160 bytes
02:01:57.80 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 30208, appended 144 bytes
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 327) (bptree, mintxg=1)
02:01:57.80 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 24576, appended 88 bytes
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 44544, appended 168 bytes
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 50176, appended 152 bytes
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 318) (bptree, mintxg=1)
02:01:57.80 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 136 bytes
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 338)  
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46080, appended 120 bytes
02:01:57.80 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 46592, appended 136 bytes
02:01:57.80 1678240911   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:01:57.80 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 34816, appended 128 bytes
02:01:57.80 1678240912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240912   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 35840, appended 144 bytes
02:01:57.80 1678240913   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 188416, unflushed_frees 37888, appended 136 bytes
02:01:57.80 1678240915   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24064, appended 80 bytes
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 486400, unflushed_frees 42496, appended 280 bytes
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 486912, unflushed_frees 47104, appended 328 bytes
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 96 bytes
02:01:57.80 1678240916   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:01:57.80 1678240916   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240916   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 191488, unflushed_frees 44032, appended 232 bytes
02:01:57.80 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240916   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 349)  
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 632320, appended 344 bytes
02:01:57.80 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:01:57.80 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:01:57.80 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:01:57.80 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:01:57.80 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:01:57.80 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:01:57.80 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39424, appended 136 bytes
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27136, appended 112 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 212) (bptree, mintxg=1)
02:01:57.80 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:01:57.80 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 20 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 40960, appended 136 bytes
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 375)  
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 56832, appended 168 bytes
02:01:57.80 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:01:57.80 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 120 bytes
02:01:57.80 1678240917   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 375) mountpoint=/var/tmp/testdir
02:01:57.80 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 61952, appended 184 bytes
02:01:57.80 =================================================================
02:01:57.80  End of zfs_dbgmsg log
02:01:57.80 =================================================================
02:01:57.80 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:01:57.81 =================================================================
02:01:57.81  Tailing last 200 lines of dmesg log
02:01:57.81 =================================================================
02:01:57.81 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:01:57.81 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:01:57.81 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:01:57.81 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:01:57.81 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:01:57.81 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:01:57.81 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:01:57.81 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:01:57.81 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:01:57.81 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:01:57.81 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:01:57.81 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:01:57.81 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:01:57.81 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:01:57.81 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:01:57.81 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:01:57.81 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:01:57.81 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:01:57.81 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:01:57.81 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:01:57.81 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:01:57.81 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:01:57.81 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:01:57.81 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:01:57.81 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:01:57.81 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:01:57.81 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:01:57.81 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:01:57.81 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:01:57.81 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:01:57.81 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:01:57.81 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:01:57.81 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:01:57.81 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:01:57.81 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:01:57.81 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:01:57.81 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:01:57.81 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:01:57.81 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:01:57.81 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:01:57.81 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:01:57.81 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:01:57.81 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:01:57.81 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:01:57.81 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:01:57.81 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:01:57.81 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:01:57.81 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:01:57.81 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:01:57.81 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:01:57.81 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:01:57.81 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:01:57.81 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:01:57.81 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:01:57.81 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:01:57.81 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:01:57.81 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:01:57.81 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:01:57.81 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:01:57.81 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:01:57.81 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:01:57.81 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:01:57.81 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:01:57.81 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:01:57.81 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:01:57.81 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:01:57.81 [  817.131032] loop3: detected capacity change from 0 to 8
02:01:57.81 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:01:57.81 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:01:57.81 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:01:57.81 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:01:57.81 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:01:57.81 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:01:57.81 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:01:57.81 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:01:57.81 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:01:57.81 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:01:57.81 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:01:57.81 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:01:57.81 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:01:57.81 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:01:57.81 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:01:57.81 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:01:57.81 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:01:57.81 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:01:57.81 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:01:57.81 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:01:57.81 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:01:57.81 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:01:57.81 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:01:57.81 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:01:57.81 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:01:57.81 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:01:57.81 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:01:57.81 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:01:57.81 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:01:57.81 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:01:57.81 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:01:57.81 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:01:57.81 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:01:57.81 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:01:57.81 [ 1099.175454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:01:57.81 =================================================================
02:01:57.81  End of dmesg log
02:01:57.81 =================================================================
02:01:57.82 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:01:57.82 NOTE: Performing local cleanup via log_onexit (cleanup)
02:01:57.90 SUCCESS: zfs destroy -f testpool/testfs
02:01:57.91 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
02:01:59.99 ASSERTION: CM-not-UN FS: CI lookup succeeds only if (norm=same)
02:02:00.03 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.07 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.07 SUCCESS: create_file FïLëNÄmë
02:02:00.07 SUCCESS: lookup_file_ci FïLëNÄmë
02:02:00.08 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:02:00.08 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:02:00.08 =================================================================
02:02:00.08  Tailing last 200 lines of zfs_dbgmsg log
02:02:00.08 =================================================================
02:02:00.09 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:02:00.09 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 29184, appended 144 bytes
02:02:00.09 1678240910   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 305) (bptree, mintxg=1)
02:02:00.09 1678240910   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240910   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
02:02:00.09 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 88 bytes
02:02:00.09 1678240910   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:02:00.09 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 41472, appended 184 bytes
02:02:00.09 1678240910   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 47616, appended 160 bytes
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 185) (bptree, mintxg=1)
02:02:00.09 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 28160, appended 144 bytes
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 318)  
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 28160, unflushed_frees 44032, appended 136 bytes
02:02:00.09 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 45568, appended 128 bytes
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 318) mountpoint=/var/tmp/testdir
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 33280, appended 136 bytes
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 327)  
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 34816, appended 160 bytes
02:02:00.09 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 30208, appended 144 bytes
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 327) (bptree, mintxg=1)
02:02:00.09 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 24576, appended 88 bytes
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 44544, appended 168 bytes
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 50176, appended 152 bytes
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 318) (bptree, mintxg=1)
02:02:00.09 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 136 bytes
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 338)  
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46080, appended 120 bytes
02:02:00.09 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 46592, appended 136 bytes
02:02:00.09 1678240911   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:02:00.09 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 34816, appended 128 bytes
02:02:00.09 1678240912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240912   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 35840, appended 144 bytes
02:02:00.09 1678240913   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 188416, unflushed_frees 37888, appended 136 bytes
02:02:00.09 1678240915   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24064, appended 80 bytes
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 486400, unflushed_frees 42496, appended 280 bytes
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 486912, unflushed_frees 47104, appended 328 bytes
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 96 bytes
02:02:00.09 1678240916   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:02:00.09 1678240916   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240916   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 191488, unflushed_frees 44032, appended 232 bytes
02:02:00.09 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240916   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 349)  
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 632320, appended 344 bytes
02:02:00.09 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:02:00.09 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:02:00.09 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:02:00.09 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:02:00.09 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:02:00.09 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:02:00.09 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39424, appended 136 bytes
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27136, appended 112 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 212) (bptree, mintxg=1)
02:02:00.09 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 20 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 40960, appended 136 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 375)  
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 56832, appended 168 bytes
02:02:00.09 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 120 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 375) mountpoint=/var/tmp/testdir
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 61952, appended 184 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39936, appended 168 bytes
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27648, appended 120 bytes
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 375) (bptree, mintxg=1)
02:02:00.09 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 41984, appended 128 bytes
02:02:00.09 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240917   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 228)  
02:02:00.09 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 56832, appended 144 bytes
02:02:00.09 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37888, appended 144 bytes
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 228) mountpoint=/var/tmp/testdir
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 61440, appended 200 bytes
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40448, appended 152 bytes
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 112 bytes
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 228) (bptree, mintxg=1)
02:02:00.09 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 144 bytes
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 389)  
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58368, appended 184 bytes
02:02:00.09 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 389) mountpoint=/var/tmp/testdir
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 192 bytes
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 41984, appended 184 bytes
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29696, appended 88 bytes
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 389) (bptree, mintxg=1)
02:02:00.09 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 120 bytes
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 239)  
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 58368, appended 184 bytes
02:02:00.09 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.09 1678240918   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 239) mountpoint=/var/tmp/testdir
02:02:00.09 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 62976, appended 200 bytes
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58880, unflushed_frees 41984, appended 192 bytes
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29696, appended 96 bytes
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 239) (bptree, mintxg=1)
02:02:00.09 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 44032, appended 144 bytes
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 407)  
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58880, appended 152 bytes
02:02:00.09 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 40448, appended 104 bytes
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 407) mountpoint=/var/tmp/testdir
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 63488, appended 200 bytes
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60416, unflushed_frees 41472, appended 152 bytes
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 29696, appended 96 bytes
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 407) (bptree, mintxg=1)
02:02:00.09 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 44544, appended 136 bytes
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 248)  
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60416, appended 144 bytes
02:02:00.09 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41472, appended 128 bytes
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 248) mountpoint=/var/tmp/testdir
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65024, appended 200 bytes
02:02:00.09 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 44032, appended 152 bytes
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 32256, appended 120 bytes
02:02:00.09 1678240919   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 248) (bptree, mintxg=1)
02:02:00.09 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.09 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:02:00.09 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 144 bytes
02:02:00.09 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.09 1678240920   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 516)  
02:02:00.09 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 60928, appended 136 bytes
02:02:00.09 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.09 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.09 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41984, appended 128 bytes
02:02:00.09 1678240920   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 516) mountpoint=/var/tmp/testdir
02:02:00.09 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65536, appended 192 bytes
02:02:00.09 =================================================================
02:02:00.09  End of zfs_dbgmsg log
02:02:00.09 =================================================================
02:02:00.09 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:02:00.09 =================================================================
02:02:00.09  Tailing last 200 lines of dmesg log
02:02:00.09 =================================================================
02:02:00.10 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:02:00.10 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:02:00.10 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:02:00.10 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:02:00.10 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:02:00.10 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:02:00.10 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:02:00.10 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:02:00.10 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:02:00.10 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:02:00.10 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:02:00.10 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:02:00.10 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:02:00.10 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:02:00.10 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:02:00.10 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:02:00.10 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:02:00.10 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:02:00.10 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:02:00.10 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:02:00.10 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:02:00.10 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:02:00.10 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:02:00.10 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:02:00.10 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:02:00.10 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:02:00.10 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:02:00.10 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:02:00.10 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:02:00.10 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:02:00.10 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:02:00.10 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:02:00.10 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:02:00.10 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:02:00.10 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:02:00.10 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:02:00.10 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:02:00.10 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:02:00.10 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:02:00.10 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:02:00.10 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:02:00.10 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:02:00.10 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:02:00.10 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:02:00.10 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.10 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:02:00.10 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:02:00.10 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:02:00.10 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:02:00.10 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.10 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.10 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:02:00.10 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:02:00.10 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.10 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:02:00.10 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:02:00.10 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:02:00.10 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:02:00.10 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:02:00.10 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:02:00.10 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:02:00.10 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:02:00.10 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:02:00.10 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:02:00.10 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:02:00.10 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:02:00.10 [  817.131032] loop3: detected capacity change from 0 to 8
02:02:00.10 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:02:00.10 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:02:00.10 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:02:00.10 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:02:00.10 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:02:00.10 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:02:00.10 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:02:00.10 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:02:00.10 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:02:00.10 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:02:00.10 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:02:00.10 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:02:00.10 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:02:00.10 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:02:00.10 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:02:00.10 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:02:00.10 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:02:00.10 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:02:00.10 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:02:00.10 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:02:00.10 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:02:00.10 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:02:00.10 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:02:00.10 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:02:00.10 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:02:00.10 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:02:00.10 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:02:00.10 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:02:00.10 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:02:00.10 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:02:00.10 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:02:00.10 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:02:00.10 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:02:00.10 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:02:00.10 [ 1099.175454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:02:00.10 [ 1099.432083] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:02:00.10 [ 1099.752526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:02:00.10 [ 1100.246575] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:02:00.10 [ 1100.563020] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:02:00.10 [ 1101.084277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:02:00.10 [ 1101.494390] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:02:00.10 =================================================================
02:02:00.10  End of dmesg log
02:02:00.10 =================================================================
02:02:00.10 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:02:00.10 NOTE: Performing local cleanup via log_onexit (cleanup)
02:02:00.19 SUCCESS: zfs destroy -f testpool/testfs
02:02:00.19 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
02:02:00.56 ASSERTION: CM-UN FS: lookup succeeds if (case=same)
02:02:00.60 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:00.64 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.64 SUCCESS: create_file FïLëNÄmë
02:02:00.65 SUCCESS: lookup_file FïLëNÄmë
02:02:00.65 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:02:00.65 SUCCESS: lookup_file fïlënämë exited 1
02:02:00.65 SUCCESS: lookup_file FïLëNÄmë
02:02:00.66 SUCCESS: lookup_file FÏLËNÄMË exited 1
02:02:00.66 SUCCESS: lookup_file fïlënämë exited 1
02:02:00.66 SUCCESS: create_file FÏLËNÄMË
02:02:00.66 SUCCESS: lookup_file FïLëNÄmë exited 1
02:02:00.67 SUCCESS: lookup_file FÏLËNÄMË
02:02:00.67 SUCCESS: lookup_file fïlënämë exited 1
02:02:00.67 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
02:02:00.67 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:02:00.67 =================================================================
02:02:00.67  Tailing last 200 lines of zfs_dbgmsg log
02:02:00.67 =================================================================
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 24576, appended 88 bytes
02:02:00.69 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 44544, appended 168 bytes
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 50176, appended 152 bytes
02:02:00.69 1678240911   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 318) (bptree, mintxg=1)
02:02:00.69 1678240911   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240911   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 136 bytes
02:02:00.69 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240911   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 338)  
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46080, appended 120 bytes
02:02:00.69 1678240911   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240911   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 46592, appended 136 bytes
02:02:00.69 1678240911   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 338) mountpoint=/var/tmp/testdir
02:02:00.69 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 34816, appended 128 bytes
02:02:00.69 1678240912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240912   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 35840, appended 144 bytes
02:02:00.69 1678240913   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 188416, unflushed_frees 37888, appended 136 bytes
02:02:00.69 1678240915   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24064, appended 80 bytes
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 486400, unflushed_frees 42496, appended 280 bytes
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 486912, unflushed_frees 47104, appended 328 bytes
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 96 bytes
02:02:00.69 1678240916   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:02:00.69 1678240916   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240916   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 191488, unflushed_frees 44032, appended 232 bytes
02:02:00.69 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240916   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 349)  
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 632320, appended 344 bytes
02:02:00.69 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:02:00.69 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:02:00.69 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:02:00.69 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:02:00.69 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:02:00.69 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:02:00.69 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39424, appended 136 bytes
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27136, appended 112 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 212) (bptree, mintxg=1)
02:02:00.69 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 20 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 40960, appended 136 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 375)  
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 56832, appended 168 bytes
02:02:00.69 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 120 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 375) mountpoint=/var/tmp/testdir
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 61952, appended 184 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39936, appended 168 bytes
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27648, appended 120 bytes
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 375) (bptree, mintxg=1)
02:02:00.69 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 41984, appended 128 bytes
02:02:00.69 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240917   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 228)  
02:02:00.69 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 56832, appended 144 bytes
02:02:00.69 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37888, appended 144 bytes
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 228) mountpoint=/var/tmp/testdir
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 61440, appended 200 bytes
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40448, appended 152 bytes
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 112 bytes
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 228) (bptree, mintxg=1)
02:02:00.69 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 144 bytes
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 389)  
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58368, appended 184 bytes
02:02:00.69 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 389) mountpoint=/var/tmp/testdir
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 192 bytes
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 41984, appended 184 bytes
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29696, appended 88 bytes
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 389) (bptree, mintxg=1)
02:02:00.69 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 120 bytes
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 239)  
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 58368, appended 184 bytes
02:02:00.69 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.69 1678240918   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 239) mountpoint=/var/tmp/testdir
02:02:00.69 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 62976, appended 200 bytes
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58880, unflushed_frees 41984, appended 192 bytes
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29696, appended 96 bytes
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 239) (bptree, mintxg=1)
02:02:00.69 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 44032, appended 144 bytes
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 407)  
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58880, appended 152 bytes
02:02:00.69 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 40448, appended 104 bytes
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 407) mountpoint=/var/tmp/testdir
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 63488, appended 200 bytes
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60416, unflushed_frees 41472, appended 152 bytes
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 29696, appended 96 bytes
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 407) (bptree, mintxg=1)
02:02:00.69 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 44544, appended 136 bytes
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 248)  
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60416, appended 144 bytes
02:02:00.69 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41472, appended 128 bytes
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 248) mountpoint=/var/tmp/testdir
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65024, appended 200 bytes
02:02:00.69 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 44032, appended 152 bytes
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 32256, appended 120 bytes
02:02:00.69 1678240919   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 248) (bptree, mintxg=1)
02:02:00.69 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:02:00.69 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 144 bytes
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 516)  
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 60928, appended 136 bytes
02:02:00.69 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41984, appended 128 bytes
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 516) mountpoint=/var/tmp/testdir
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65536, appended 192 bytes
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44032, appended 136 bytes
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 516) (bptree, mintxg=1)
02:02:00.69 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 46080, appended 144 bytes
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 529)  
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 61440, appended 144 bytes
02:02:00.69 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 42496, appended 120 bytes
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 529) mountpoint=/var/tmp/testdir
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 66048, appended 200 bytes
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44544, appended 144 bytes
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 529) (bptree, mintxg=1)
02:02:00.69 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.69 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 46592, appended 144 bytes
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 425)  
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 61440, appended 144 bytes
02:02:00.69 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.69 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 42496, appended 120 bytes
02:02:00.69 1678240920   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 425) mountpoint=/var/tmp/testdir
02:02:00.69 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 66048, appended 216 bytes
02:02:00.69 =================================================================
02:02:00.69  End of zfs_dbgmsg log
02:02:00.69 =================================================================
02:02:00.69 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:02:00.69 =================================================================
02:02:00.69  Tailing last 200 lines of dmesg log
02:02:00.69 =================================================================
02:02:00.70 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:02:00.70 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:02:00.70 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:02:00.70 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:02:00.70 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:02:00.70 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:02:00.70 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:02:00.70 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:02:00.70 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:02:00.70 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:02:00.70 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:02:00.70 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:02:00.70 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:02:00.70 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:02:00.70 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:02:00.70 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:02:00.70 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:02:00.70 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:02:00.70 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:02:00.70 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:02:00.70 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:02:00.70 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:02:00.70 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:02:00.70 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:02:00.70 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:02:00.70 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:02:00.70 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:02:00.70 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:02:00.70 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:02:00.70 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:02:00.70 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:02:00.70 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:02:00.70 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:02:00.70 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:02:00.70 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:02:00.70 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:02:00.70 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:02:00.70 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:02:00.70 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:02:00.70 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:02:00.70 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:02:00.70 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:02:00.70 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:02:00.70 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:02:00.70 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.70 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:02:00.70 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:02:00.70 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:02:00.70 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:02:00.70 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.70 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.70 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:02:00.70 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:02:00.70 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.70 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:02:00.70 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:02:00.70 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:02:00.70 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:02:00.70 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:02:00.70 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:02:00.70 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:02:00.70 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:02:00.70 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:02:00.70 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:02:00.70 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:02:00.70 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:02:00.70 [  817.131032] loop3: detected capacity change from 0 to 8
02:02:00.70 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:02:00.70 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:02:00.70 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:02:00.70 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:02:00.70 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:02:00.70 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:02:00.70 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:02:00.70 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:02:00.70 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:02:00.70 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:02:00.70 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:02:00.70 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:02:00.70 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:02:00.70 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:02:00.70 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:02:00.70 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:02:00.70 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:02:00.70 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:02:00.70 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:02:00.70 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:02:00.70 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:02:00.70 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:02:00.70 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:02:00.70 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:02:00.70 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:02:00.70 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:02:00.70 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:02:00.70 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:02:00.70 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:02:00.70 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:02:00.70 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:02:00.70 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:02:00.70 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:02:00.70 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:02:00.70 [ 1099.175454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:02:00.70 [ 1099.432083] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:02:00.70 [ 1099.752526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:02:00.70 [ 1100.246575] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:02:00.70 [ 1100.563020] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:02:00.70 [ 1101.084277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:02:00.70 [ 1101.494390] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:02:00.70 [ 1101.716503] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:02:00.70 [ 1102.060224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:02:00.70 =================================================================
02:02:00.70  End of dmesg log
02:02:00.70 =================================================================
02:02:00.70 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:02:00.70 NOTE: Performing local cleanup via log_onexit (cleanup)
02:02:00.79 SUCCESS: zfs destroy -f testpool/testfs
02:02:00.79 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
02:02:00.82 ASSERTION: CM-UN FS: CI lookup succeeds using any name form
02:02:00.86 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:00.89 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.89 SUCCESS: create_file FïLëNÄmë
02:02:00.90 SUCCESS: lookup_file_ci FïLëNÄmë
02:02:00.90 ERROR: lookup_file_ci FÏLËNÄMË exited 1
02:02:00.90 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:02:00.90 =================================================================
02:02:00.90  Tailing last 200 lines of zfs_dbgmsg log
02:02:00.90 =================================================================
02:02:00.91 1678240911   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 34816, appended 128 bytes
02:02:00.91 1678240912   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240912   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 35840, appended 144 bytes
02:02:00.91 1678240913   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 188416, unflushed_frees 37888, appended 136 bytes
02:02:00.91 1678240915   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 24064, appended 80 bytes
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 486400, unflushed_frees 42496, appended 280 bytes
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 486912, unflushed_frees 47104, appended 328 bytes
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 20992, unflushed_frees 19456, appended 96 bytes
02:02:00.91 1678240916   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 338) (bptree, mintxg=1)
02:02:00.91 1678240916   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240916   dsl_scan.c:3492:dsl_process_async_destroys(): freed 131594 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 191488, unflushed_frees 44032, appended 232 bytes
02:02:00.91 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240916   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 349)  
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 632320, appended 344 bytes
02:02:00.91 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:02:00.91 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:02:00.91 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:02:00.91 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:02:00.91 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:02:00.91 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:02:00.91 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39424, appended 136 bytes
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27136, appended 112 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 212) (bptree, mintxg=1)
02:02:00.91 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 20 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 40960, appended 136 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 375)  
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 56832, appended 168 bytes
02:02:00.91 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 120 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 375) mountpoint=/var/tmp/testdir
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 61952, appended 184 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39936, appended 168 bytes
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27648, appended 120 bytes
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 375) (bptree, mintxg=1)
02:02:00.91 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 41984, appended 128 bytes
02:02:00.91 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240917   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 228)  
02:02:00.91 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 56832, appended 144 bytes
02:02:00.91 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37888, appended 144 bytes
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 228) mountpoint=/var/tmp/testdir
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 61440, appended 200 bytes
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40448, appended 152 bytes
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 112 bytes
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 228) (bptree, mintxg=1)
02:02:00.91 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 144 bytes
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 389)  
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58368, appended 184 bytes
02:02:00.91 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 389) mountpoint=/var/tmp/testdir
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 192 bytes
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 41984, appended 184 bytes
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29696, appended 88 bytes
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 389) (bptree, mintxg=1)
02:02:00.91 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 120 bytes
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 239)  
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 58368, appended 184 bytes
02:02:00.91 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:00.91 1678240918   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 239) mountpoint=/var/tmp/testdir
02:02:00.91 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 62976, appended 200 bytes
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58880, unflushed_frees 41984, appended 192 bytes
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29696, appended 96 bytes
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 239) (bptree, mintxg=1)
02:02:00.91 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 44032, appended 144 bytes
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 407)  
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58880, appended 152 bytes
02:02:00.91 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 40448, appended 104 bytes
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 407) mountpoint=/var/tmp/testdir
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 63488, appended 200 bytes
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60416, unflushed_frees 41472, appended 152 bytes
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 29696, appended 96 bytes
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 407) (bptree, mintxg=1)
02:02:00.91 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 44544, appended 136 bytes
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 248)  
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60416, appended 144 bytes
02:02:00.91 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41472, appended 128 bytes
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 248) mountpoint=/var/tmp/testdir
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65024, appended 200 bytes
02:02:00.91 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 44032, appended 152 bytes
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 32256, appended 120 bytes
02:02:00.91 1678240919   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 248) (bptree, mintxg=1)
02:02:00.91 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:02:00.91 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 144 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 516)  
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 60928, appended 136 bytes
02:02:00.91 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41984, appended 128 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 516) mountpoint=/var/tmp/testdir
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65536, appended 192 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44032, appended 136 bytes
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 516) (bptree, mintxg=1)
02:02:00.91 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 46080, appended 144 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 529)  
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 61440, appended 144 bytes
02:02:00.91 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 42496, appended 120 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 529) mountpoint=/var/tmp/testdir
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 66048, appended 200 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44544, appended 144 bytes
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 529) (bptree, mintxg=1)
02:02:00.91 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 46592, appended 144 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 425)  
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 61440, appended 144 bytes
02:02:00.91 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 42496, appended 120 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 425) mountpoint=/var/tmp/testdir
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 66048, appended 216 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 62464, unflushed_frees 45056, appended 160 bytes
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 33280, appended 96 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 425) (bptree, mintxg=1)
02:02:00.91 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:00.91 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 47104, appended 136 bytes
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 437)  
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 62464, appended 192 bytes
02:02:00.91 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:00.91 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 43520, appended 120 bytes
02:02:00.91 1678240920   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 437) mountpoint=/var/tmp/testdir
02:02:00.91 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 66560, appended 200 bytes
02:02:00.91 =================================================================
02:02:00.91  End of zfs_dbgmsg log
02:02:00.91 =================================================================
02:02:00.91 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:02:00.92 =================================================================
02:02:00.92  Tailing last 200 lines of dmesg log
02:02:00.92 =================================================================
02:02:00.92 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:02:00.92 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:02:00.92 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:02:00.92 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:02:00.92 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:02:00.92 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:02:00.92 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:02:00.92 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:02:00.92 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:02:00.92 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:02:00.92 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:02:00.92 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:02:00.92 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:02:00.92 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:02:00.92 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:02:00.92 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:02:00.92 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:02:00.92 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:02:00.92 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:02:00.92 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:02:00.92 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:02:00.92 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:02:00.92 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:02:00.92 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:02:00.92 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:02:00.92 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:02:00.92 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:02:00.92 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:02:00.92 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:02:00.92 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:02:00.92 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:02:00.92 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:02:00.92 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:02:00.92 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:02:00.92 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:02:00.92 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:02:00.92 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:02:00.92 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:02:00.92 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:02:00.92 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:02:00.92 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:02:00.92 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:02:00.92 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:02:00.92 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:02:00.92 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.92 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:02:00.92 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:02:00.92 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:02:00.92 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:02:00.92 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.92 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:00.92 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:02:00.92 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:02:00.92 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:00.92 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:02:00.92 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:02:00.92 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:02:00.92 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:02:00.92 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:02:00.92 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:02:00.92 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:02:00.92 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:02:00.92 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:02:00.92 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:02:00.92 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:02:00.92 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:02:00.92 [  817.131032] loop3: detected capacity change from 0 to 8
02:02:00.92 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:02:00.92 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:02:00.92 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:02:00.92 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:02:00.92 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:02:00.92 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:02:00.92 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:02:00.92 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:02:00.92 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:02:00.92 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:02:00.92 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:02:00.92 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:02:00.92 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:02:00.92 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:02:00.92 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:02:00.92 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:02:00.92 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:02:00.92 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:02:00.92 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:02:00.92 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:02:00.92 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:02:00.92 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:02:00.92 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:02:00.92 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:02:00.92 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:02:00.92 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:02:00.92 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:02:00.92 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:02:00.92 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:02:00.92 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:02:00.92 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:02:00.92 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:02:00.92 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:02:00.92 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:02:00.92 [ 1099.175454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:02:00.92 [ 1099.432083] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:02:00.92 [ 1099.752526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:02:00.92 [ 1100.246575] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:02:00.92 [ 1100.563020] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:02:00.92 [ 1101.084277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:02:00.92 [ 1101.494390] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:02:00.92 [ 1101.716503] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:02:00.92 [ 1102.060224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:02:00.92 [ 1102.316278] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
02:02:00.93 =================================================================
02:02:00.93  End of dmesg log
02:02:00.93 =================================================================
02:02:00.93 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:02:00.93 NOTE: Performing local cleanup via log_onexit (cleanup)
02:02:01.01 SUCCESS: zfs destroy -f testpool/testfs
02:02:01.02 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
02:02:01.04 ASSERTION: CM-UN FS: delete succeeds if (case=same)
02:02:01.08 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:01.12 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.12 SUCCESS: create_file FïLëNÄmë
02:02:01.12 SUCCESS: delete_file FïLëNÄmë
02:02:01.13 SUCCESS: lookup_any exited 1
02:02:01.13 SUCCESS: create_file FïLëNÄmë
02:02:01.13 SUCCESS: delete_file FÏLËNÄMË exited 1
02:02:01.14 SUCCESS: create_file FïLëNÄmë
02:02:01.14 SUCCESS: delete_file fïlënämë exited 1
02:02:01.14 SUCCESS: create_file FïLëNÄmë
02:02:01.15 ERROR: delete_file FïLëNÄmë exited 1
02:02:01.15 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
02:02:01.15 =================================================================
02:02:01.15  Tailing last 200 lines of zfs_dbgmsg log
02:02:01.15 =================================================================
02:02:01.16 1678240916   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240916   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:01.16 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35328, appended 144 bytes
02:02:01.16 1678240916   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 349) mountpoint=/var/tmp/testdir
02:02:01.16 1678240916   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 644608, appended 488 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37376, appended 200 bytes
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26112, appended 104 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 349) (bptree, mintxg=1)
02:02:01.16 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49664, unflushed_frees 41472, appended 152 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 360)  
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 55808, appended 136 bytes
02:02:01.16 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 112 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 360) mountpoint=/var/tmp/testdir
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 60416, appended 200 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 38400, appended 128 bytes
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 27136, appended 104 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 360) (bptree, mintxg=1)
02:02:01.16 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 41472, appended 144 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 212)  
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 55808, appended 128 bytes
02:02:01.16 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 36864, appended 112 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 212) mountpoint=/var/tmp/testdir
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 60416, appended 192 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39424, appended 136 bytes
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27136, appended 112 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 212) (bptree, mintxg=1)
02:02:01.16 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 20 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 40960, appended 136 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 375)  
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 56832, appended 168 bytes
02:02:01.16 1678240917   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 37888, appended 120 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 375) mountpoint=/var/tmp/testdir
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 61952, appended 184 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 39936, appended 168 bytes
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 27648, appended 120 bytes
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 375) (bptree, mintxg=1)
02:02:01.16 1678240917   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240917   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 41984, appended 128 bytes
02:02:01.16 1678240917   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240917   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 228)  
02:02:01.16 1678240917   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 56832, appended 144 bytes
02:02:01.16 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37888, appended 144 bytes
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 228) mountpoint=/var/tmp/testdir
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 61440, appended 200 bytes
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 40448, appended 152 bytes
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 112 bytes
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 228) (bptree, mintxg=1)
02:02:01.16 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 144 bytes
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 389)  
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58368, appended 184 bytes
02:02:01.16 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 389) mountpoint=/var/tmp/testdir
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 192 bytes
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 41984, appended 184 bytes
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29696, appended 88 bytes
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 389) (bptree, mintxg=1)
02:02:01.16 1678240918   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240918   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 120 bytes
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 239)  
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 58368, appended 184 bytes
02:02:01.16 1678240918   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240918   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 120 bytes
02:02:01.16 1678240918   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 239) mountpoint=/var/tmp/testdir
02:02:01.16 1678240918   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 62976, appended 200 bytes
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58880, unflushed_frees 41984, appended 192 bytes
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 29696, appended 96 bytes
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 239) (bptree, mintxg=1)
02:02:01.16 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53248, unflushed_frees 44032, appended 144 bytes
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 407)  
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 58880, appended 152 bytes
02:02:01.16 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 40448, appended 104 bytes
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 407) mountpoint=/var/tmp/testdir
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 63488, appended 200 bytes
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60416, unflushed_frees 41472, appended 152 bytes
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 29696, appended 96 bytes
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 407) (bptree, mintxg=1)
02:02:01.16 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 44544, appended 136 bytes
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 248)  
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60416, appended 144 bytes
02:02:01.16 1678240919   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41472, appended 128 bytes
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 248) mountpoint=/var/tmp/testdir
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65024, appended 200 bytes
02:02:01.16 1678240919   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 44032, appended 152 bytes
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 32256, appended 120 bytes
02:02:01.16 1678240919   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 248) (bptree, mintxg=1)
02:02:01.16 1678240919   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240919   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
02:02:01.16 1678240919   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 144 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 516)  
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 60928, appended 136 bytes
02:02:01.16 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 41984, appended 128 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 516) mountpoint=/var/tmp/testdir
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 65536, appended 192 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44032, appended 136 bytes
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 516) (bptree, mintxg=1)
02:02:01.16 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 46080, appended 144 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 529)  
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 61440, appended 144 bytes
02:02:01.16 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 42496, appended 120 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 529) mountpoint=/var/tmp/testdir
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 66048, appended 200 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 61440, unflushed_frees 44544, appended 144 bytes
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 32256, appended 104 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 529) (bptree, mintxg=1)
02:02:01.16 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 46592, appended 144 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 425)  
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 61440, appended 144 bytes
02:02:01.16 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 42496, appended 120 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 425) mountpoint=/var/tmp/testdir
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 66048, appended 216 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 62464, unflushed_frees 45056, appended 160 bytes
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 33280, appended 96 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 425) (bptree, mintxg=1)
02:02:01.16 1678240920   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240920   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 47104, appended 136 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 437)  
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 62464, appended 192 bytes
02:02:01.16 1678240920   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 43520, appended 120 bytes
02:02:01.16 1678240920   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 437) mountpoint=/var/tmp/testdir
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 66560, appended 200 bytes
02:02:01.16 1678240920   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
02:02:01.16 1678240920   metaslab.c:3926:metaslab_flush(): flushing: txg 169, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 63488, unflushed_frees 46080, appended 184 bytes
02:02:01.16 1678240921   metaslab.c:3926:metaslab_flush(): flushing: txg 170, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 34816, appended 96 bytes
02:02:01.16 1678240921   spa_history.c:297:spa_history_log_sync(): txg 171 destroy testpool/testfs (id 437) (bptree, mintxg=1)
02:02:01.16 1678240921   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
02:02:01.16 1678240921   dsl_scan.c:3492:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 171; err=0
02:02:01.16 1678240921   metaslab.c:3926:metaslab_flush(): flushing: txg 171, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 49152, appended 144 bytes
02:02:01.16 1678240921   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
02:02:01.16 1678240921   spa_history.c:297:spa_history_log_sync(): txg 172 create testpool/testfs (id 450)  
02:02:01.16 1678240921   metaslab.c:3926:metaslab_flush(): flushing: txg 172, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 63488, appended 152 bytes
02:02:01.16 1678240921   spa_history.c:329:spa_history_log_sync(): ioctl create
02:02:01.16 1678240921   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
02:02:01.16 1678240921   metaslab.c:3926:metaslab_flush(): flushing: txg 173, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 45056, appended 120 bytes
02:02:01.16 1678240921   spa_history.c:297:spa_history_log_sync(): txg 174 set testpool/testfs (id 450) mountpoint=/var/tmp/testdir
02:02:01.16 1678240921   metaslab.c:3926:metaslab_flush(): flushing: txg 174, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 68096, appended 200 bytes
02:02:01.16 =================================================================
02:02:01.16  End of zfs_dbgmsg log
02:02:01.16 =================================================================
02:02:01.16 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
02:02:01.16 =================================================================
02:02:01.16  Tailing last 200 lines of dmesg log
02:02:01.16 =================================================================
02:02:01.17 [  480.950348] loop0: detected capacity change from 0 to 6291456
02:02:01.17 [  480.974542] loop1: detected capacity change from 0 to 6291456
02:02:01.17 [  481.001434] loop2: detected capacity change from 0 to 6291456
02:02:01.17 [  481.171806] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup
02:02:01.17 [  509.368744] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode
02:02:01.17 [  510.114585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode
02:02:01.17 [  510.647138] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup
02:02:01.17 [  511.160113] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup
02:02:01.17 [  512.964178] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos
02:02:01.17 [  513.064176] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos
02:02:01.17 [  513.139859] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos
02:02:01.17 [  513.234305] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos
02:02:01.17 [  513.289715] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup
02:02:01.17 [  513.696832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup
02:02:01.17 [  515.237011] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos
02:02:01.17 [  515.340209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos
02:02:01.17 [  515.420933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos
02:02:01.17 [  515.522385] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos
02:02:01.17 [  515.580779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup
02:02:01.17 [  516.011725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup
02:02:01.17 [  516.053047] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos
02:02:01.17 [  518.528082] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg
02:02:01.17 [  524.907090] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
02:02:01.17 [  525.777224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
02:02:01.17 [  526.342839] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
02:02:01.17 [  527.052929] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
02:02:01.17 [  527.321688] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
02:02:01.17 [  537.630951] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
02:02:01.17 [  538.186801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
02:02:01.17 [  545.894293] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
02:02:01.17 [  546.535058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
02:02:01.17 [  546.796425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
02:02:01.17 [  679.309774] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
02:02:01.17 [  696.014490] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
02:02:01.17 [  696.090981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
02:02:01.17 [  696.365435] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
02:02:01.17 [  696.462469] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
02:02:01.17 [  696.498367] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
02:02:01.17 [  696.726481] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
02:02:01.17 [  696.976114] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
02:02:01.17 [  697.615024] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
02:02:01.17 [  697.921299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
02:02:01.17 [  698.363365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
02:02:01.17 [  698.464521] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
02:02:01.17 [  698.699403] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:01.17 [  698.924460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
02:02:01.17 [  709.433676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
02:02:01.17 [  715.869543] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
02:02:01.17 [  722.418607] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
02:02:01.17 [  733.043608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:01.17 [  733.269401] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
02:02:01.17 [  733.508977] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
02:02:01.17 [  744.013707] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
02:02:01.17 [  754.650201] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
02:02:01.17 [  754.883426] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
02:02:01.17 [  754.908487] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
02:02:01.17 [  756.489808] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
02:02:01.17 [  758.584881] debugfs: Directory 'zd0' with parent 'block' already present!
02:02:01.17 [  759.171684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
02:02:01.17 [  760.897676] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
02:02:01.17 [  761.470683] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
02:02:01.17 [  766.868431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
02:02:01.17 [  772.484025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
02:02:01.17 [  772.811493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
02:02:01.17 [  774.781777] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
02:02:01.17 [  774.804600] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
02:02:01.17 [  817.131032] loop3: detected capacity change from 0 to 8
02:02:01.17 [  817.530764] audit: type=1400 audit(1678240636.020:106): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79216 comm="apparmor_parser"
02:02:01.17 [  817.547265] audit: type=1400 audit(1678240636.036:107): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79216 comm="apparmor_parser"
02:02:01.17 [  817.936277] audit: type=1400 audit(1678240636.424:108): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=79237 comm="apparmor_parser"
02:02:01.17 [  817.937494] audit: type=1400 audit(1678240636.424:109): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=79237 comm="apparmor_parser"
02:02:01.17 [  955.553197] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
02:02:01.17 [  958.070761] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
02:02:01.17 [  961.705449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
02:02:01.17 [  975.177642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
02:02:01.17 [  985.042329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
02:02:01.17 [  995.508610] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
02:02:01.17 [  997.070629] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
02:02:01.17 [  998.758657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
02:02:01.17 [ 1020.095926] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
02:02:01.17 [ 1020.790620] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
02:02:01.17 [ 1025.361837] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
02:02:01.17 [ 1044.242608] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
02:02:01.17 [ 1045.036681] loop3: detected capacity change from 0 to 524288
02:02:01.17 [ 1045.323399] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
02:02:01.17 [ 1055.507308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
02:02:01.17 [ 1055.626324] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 2254695028571926023), resetting them to the default (8388608)
02:02:01.17 [ 1081.716533] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
02:02:01.17 [ 1082.102087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
02:02:01.17 [ 1082.171981] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
02:02:01.17 [ 1084.218759] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
02:02:01.17 [ 1086.268905] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
02:02:01.17 [ 1088.341363] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
02:02:01.17 [ 1089.859300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
02:02:01.17 [ 1089.924962] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
02:02:01.17 [ 1090.111313] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
02:02:01.17 [ 1090.667475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
02:02:01.17 [ 1092.814496] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
02:02:01.17 [ 1098.178813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
02:02:01.17 [ 1098.578697] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
02:02:01.17 [ 1098.925181] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
02:02:01.17 [ 1099.175454] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
02:02:01.17 [ 1099.432083] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
02:02:01.17 [ 1099.752526] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
02:02:01.17 [ 1100.246575] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
02:02:01.17 [ 1100.563020] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
02:02:01.17 [ 1101.084277] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
02:02:01.17 [ 1101.494390] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
02:02:01.17 [ 1101.716503] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
02:02:01.17 [ 1102.060224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
02:02:01.17 [ 1102.316278] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
02:02:01.17 [ 1102.541840] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete
02:02:01.17 =================================================================
02:02:01.17  End of dmesg log
02:02:01.17 =================================================================
02:02:01.17 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
02:02:01.18 NOTE: Performing local cleanup via log_onexit (cleanup)
02:02:01.26 SUCCESS: zfs destroy -f testpool/testfs
02:02:01.26 SUCCESS: rm -rf /var/tmp/testdir
</pre></small></details>
<details><summary>All Tests</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_002_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos (run as root) [02:12] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive (run as root) [03:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos (run as root) [00:26] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.list_children (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/tst.terminate_by_signal (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/channel_program/synctask_core/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_edonr_test (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_sha2_test (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_skein_test (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_blake3_test (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_001_pos (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_002_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_004_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/misc/setup (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/setup (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_001_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_002_pos (run as runner) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_003_pos (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_004_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_005_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_007_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_008_neg (run as runner) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/cleanup (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_compressed_arc_disabled (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted_no_compressed_arc (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cp_files_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/crtime_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/crtime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/ctime_001_pos (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/ctime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_ratelimit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_sync (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_zio (run as root) [00:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/setup (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_003_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_007_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_010_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_012_neg (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_003_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/async_destroy_001_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_001_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_009_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_002_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_003_pos (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/inherit_001_pos (run as root) [01:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_008_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_009_pos (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/sync (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/psync (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/posixaio (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/mmap (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_limit (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/link_count/link_count_001 (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_mixed (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_read_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_seek_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_sync_001_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_write_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [02:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [02:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [02:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_invalid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_lun_expsz (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_open (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_rewind (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_ro_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_vdev_add (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zdb (run as root) [01:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zhack_feat (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_002_neg (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [00:57] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
</pre></details>
