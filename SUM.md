
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
