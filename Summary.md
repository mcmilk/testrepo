
## Sanity Tests Ubuntu 20.04

All tests passed :thumbsup:
<details><summary>Full Listing</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:43] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_001_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_002_neg (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/snapshot_count (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_008_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:08] [PASS]
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

All tests passed :thumbsup:
<details><summary>Full Listing</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:30] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_location (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_noop (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_recursive (run as root) [00:08] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_all (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/zfs_unload-key_recursive (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unload-key/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_001_pos (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_015_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_017_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_021_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:08] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/compress_003_pos (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_017_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_018_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_019_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_020_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_021_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_022_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapused/snapused_004_pos (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:11] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/zvol_cli_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_cli/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Functional Tests Ubuntu 20.04

Summary:<pre>

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
    SKIP rsend/rsend_008_pos (https://github.com/openzfs/zfs/issues/6066)
    FAIL vdev_zaps/vdev_zaps_007_pos (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
    SKIP cli_root/zpool_expand/zpool_expand_001_pos (expected PASS)
    SKIP cli_root/zpool_expand/zpool_expand_003_neg (expected PASS)
    SKIP cli_root/zpool_expand/zpool_expand_005_pos (expected PASS)
    SKIP cli_root/zpool_reopen/setup (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_001_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_002_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_003_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_004_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_005_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_006_neg (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_007_pos (expected PASS)
    SKIP cli_root/zpool_split/zpool_split_wholedisk (expected PASS)
    SKIP fault/auto_offline_001_pos (expected PASS)
    SKIP fault/auto_online_001_pos (expected PASS)
    SKIP fault/auto_online_002_pos (expected PASS)
    SKIP fault/auto_replace_001_pos (expected PASS)
    SKIP fault/auto_spare_ashift (expected PASS)
    SKIP fault/auto_spare_shared (expected PASS)
    SKIP procfs/pool_state (expected PASS)
</pre>
<details><summary>Error Listing - with dmesg and dbgmsg</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
16:09:34.70 ASSERTION: CS-UN FS: lookup succeeds if (case=same)
16:09:34.74 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:34.78 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.78 SUCCESS: create_file FïLëNÄmë
16:09:34.78 SUCCESS: lookup_file FïLëNÄmë
16:09:34.79 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:34.79 SUCCESS: lookup_file fïlënämë exited 1
16:09:34.80 SUCCESS: lookup_file FïLëNÄmë
16:09:34.80 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:34.80 SUCCESS: lookup_file fïlënämë exited 1
16:09:34.81 SUCCESS: create_file FÏLËNÄMË
16:09:34.81 SUCCESS: lookup_file FïLëNÄmë exited 1
16:09:34.82 SUCCESS: lookup_file FÏLËNÄMË
16:09:34.82 SUCCESS: lookup_file fïlënämë exited 1
16:09:34.82 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
16:09:34.82 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:34.83 =================================================================
16:09:34.83  Tailing last 200 lines of zfs_dbgmsg log
16:09:34.83 =================================================================
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 32, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22528, unflushed_frees 17920, appended 96 bytes
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 33 create testpool/testfs (id 177)  
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 33, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 43520, appended 136 bytes
16:09:34.84 1678637366   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 34, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 47616, appended 160 bytes
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 35 set testpool/testfs (id 177) mountpoint=/var/tmp/testdir
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 35, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 28160, appended 144 bytes
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 36, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48128, unflushed_frees 30208, appended 152 bytes
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 37 destroy testpool/testfs (id 177) (bptree, mintxg=1)
16:09:34.84 1678637366   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637366   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 37; err=0
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 37, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 29696, unflushed_frees 25088, appended 136 bytes
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 101)  
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 24064, appended 120 bytes
16:09:34.84 1678637366   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 48128, appended 168 bytes
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 101) mountpoint=/var/tmp/testdir
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 48128, appended 176 bytes
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 24064, appended 136 bytes
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 101) (bptree, mintxg=1)
16:09:34.84 1678637366   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637366   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30720, unflushed_frees 26112, appended 144 bytes
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 188)  
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 31232, unflushed_frees 44544, appended 144 bytes
16:09:34.84 1678637366   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637366   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 29184, appended 128 bytes
16:09:34.84 1678637366   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 188) mountpoint=/var/tmp/testdir
16:09:34.84 1678637366   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45568, unflushed_frees 48128, appended 168 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 30720, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 188) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 19968, appended 104 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 115)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 32256, unflushed_frees 45568, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49664, appended 144 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 115) mountpoint=/var/tmp/testdir
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 30208, appended 144 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 199)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 49152, unflushed_frees 32768, appended 144 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 28160, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 199) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 20992, appended 104 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 39936, appended 176 bytes
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 46080, appended 160 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 115) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 26624, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 207)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 26624, unflushed_frees 42496, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 43520, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 207) mountpoint=/var/tmp/testdir
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 31744, appended 144 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 216)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51200, unflushed_frees 33280, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 28672, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 216) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 22016, appended 96 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 41984, appended 176 bytes
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 47616, appended 168 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 207) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 265)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 27648, unflushed_frees 44032, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 44544, appended 144 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 265) mountpoint=/var/tmp/testdir
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 32256, appended 136 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 273)  
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 34816, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 29696, appended 152 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 273) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 23040, appended 112 bytes
16:09:34.84 1678637367   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 42496, appended 168 bytes
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 48640, appended 160 bytes
16:09:34.84 1678637367   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 265) (bptree, mintxg=1)
16:09:34.84 1678637367   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637367   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
16:09:34.84 1678637367   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 30208, appended 152 bytes
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 285)  
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 28672, unflushed_frees 45568, appended 128 bytes
16:09:34.84 1678637368   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 42496, unflushed_frees 46080, appended 136 bytes
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 285) mountpoint=/var/tmp/testdir
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 33792, appended 128 bytes
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 230)  
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 35840, appended 144 bytes
16:09:34.84 1678637368   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 32256, appended 144 bytes
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 230) (bptree, mintxg=1)
16:09:34.84 1678637368   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637368   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 112 bytes
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 45056, appended 176 bytes
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 50176, appended 168 bytes
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 285) (bptree, mintxg=1)
16:09:34.84 1678637368   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637368   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 31232, appended 160 bytes
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 238)  
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 46592, appended 136 bytes
16:09:34.84 1678637368   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637368   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 42496, unflushed_frees 47616, appended 136 bytes
16:09:34.84 1678637368   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 238) mountpoint=/var/tmp/testdir
16:09:34.84 1678637368   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 34304, appended 144 bytes
16:09:34.84 1678637369   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637369   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 36352, appended 144 bytes
16:09:34.84 1678637371   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 189440, unflushed_frees 38912, appended 128 bytes
16:09:34.84 1678637372   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 25088, appended 80 bytes
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 488448, unflushed_frees 43008, appended 248 bytes
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 487936, unflushed_frees 47616, appended 264 bytes
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 21504, unflushed_frees 20992, appended 80 bytes
16:09:34.84 1678637373   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 238) (bptree, mintxg=1)
16:09:34.84 1678637373   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637373   dsl_scan.c:3493:dsl_process_async_destroys(): freed 131594 blocks in 46ms from free_bpobj/bptree on testpool in txg 93; err=0
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 192512, unflushed_frees 46080, appended 176 bytes
16:09:34.84 1678637373   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637373   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 253)  
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 31232, unflushed_frees 633344, appended 272 bytes
16:09:34.84 1678637373   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637373   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 35840, appended 128 bytes
16:09:34.84 1678637373   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 253) mountpoint=/var/tmp/testdir
16:09:34.84 1678637373   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52736, unflushed_frees 645120, appended 400 bytes
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 37888, appended 192 bytes
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 26112, appended 96 bytes
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 253) (bptree, mintxg=1)
16:09:34.84 1678637374   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637374   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 41984, appended 152 bytes
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 306)  
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 56832, appended 144 bytes
16:09:34.84 1678637374   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 38400, appended 128 bytes
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 306) mountpoint=/var/tmp/testdir
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 61952, appended 200 bytes
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 39424, appended 152 bytes
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 128 bytes
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 306) (bptree, mintxg=1)
16:09:34.84 1678637374   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:34.84 1678637374   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 41472, appended 152 bytes
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 317)  
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 55808, appended 176 bytes
16:09:34.84 1678637374   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:34.84 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37376, appended 120 bytes
16:09:34.84 1678637374   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 317) mountpoint=/var/tmp/testdir
16:09:34.84 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 61440, appended 192 bytes
16:09:34.85 =================================================================
16:09:34.85  End of zfs_dbgmsg log
16:09:34.85 =================================================================
16:09:34.85 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:34.85 =================================================================
16:09:34.85  Tailing last 200 lines of dmesg log
16:09:34.85 =================================================================
16:09:34.86 [  314.152809] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
16:09:34.86 [  315.008240] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
16:09:34.86 [  315.535701] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
16:09:34.86 [  316.250165] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
16:09:34.86 [  316.531150] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
16:09:34.86 [  326.838241] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
16:09:34.86 [  327.378098] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
16:09:34.86 [  335.066209] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
16:09:34.86 [  335.682420] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
16:09:34.86 [  335.942013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
16:09:34.86 [  461.023602] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
16:09:34.86 [  477.384439] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
16:09:34.86 [  477.468553] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
16:09:34.86 [  477.742381] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
16:09:34.86 [  477.857667] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
16:09:34.86 [  477.897080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
16:09:34.86 [  478.121162] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
16:09:34.86 [  478.385527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
16:09:34.86 [  479.012644] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
16:09:34.86 [  479.309696] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
16:09:34.86 [  479.759443] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
16:09:34.86 [  479.892185] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
16:09:34.86 [  480.113477] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
16:09:34.86 [  480.342258] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
16:09:34.86 [  490.853188] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
16:09:34.86 [  497.300847] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
16:09:34.86 [  503.866494] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
16:09:34.86 [  514.491907] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
16:09:34.86 [  514.708861] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
16:09:34.86 [  514.941223] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
16:09:34.86 [  525.449044] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
16:09:34.86 [  536.073965] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
16:09:34.86 [  536.294144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
16:09:34.86 [  536.321342] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
16:09:34.86 [  537.865317] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
16:09:34.86 [  539.939617] debugfs: Directory 'zd0' with parent 'block' already present!
16:09:34.86 [  540.501764] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
16:09:34.86 [  542.190985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
16:09:34.86 [  542.767863] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
16:09:34.86 [  549.055252] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
16:09:34.86 [  554.752329] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
16:09:34.86 [  555.090516] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
16:09:34.86 [  557.079554] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
16:09:34.86 [  557.104130] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
16:09:34.86 [  737.774693] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
16:09:34.86 [  740.907520] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
16:09:34.86 [  745.065642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
16:09:34.86 [  756.218642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
16:09:34.86 [  765.922485] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
16:09:34.86 [  776.201470] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
16:09:34.86 [  777.659882] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
16:09:34.86 [  779.344589] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
16:09:34.86 [  800.480450] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
16:09:34.86 [  801.192376] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
16:09:34.86 [  805.460479] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
16:09:34.86 [  824.036530] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
16:09:34.86 [  824.774535] loop3: detected capacity change from 0 to 524288
16:09:34.86 [  825.026266] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
16:09:34.86 [  834.954813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
16:09:34.86 [  835.456339] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 12046678776441442979), resetting them to the default (8388608)
16:09:34.86 [  923.314562] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
16:09:34.86 [  923.654985] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
16:09:34.86 [  923.748194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
16:09:34.86 [  925.750112] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
16:09:34.86 [  927.697778] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
16:09:34.86 [  929.695996] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
16:09:34.86 [  931.162750] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
16:09:34.86 [  931.230202] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
16:09:34.86 [  931.420997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
16:09:34.86 [  931.951257] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
16:09:34.86 [  933.997832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
16:09:34.86 [  939.530087] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
16:09:34.86 [  940.018897] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
16:09:34.86 [  940.419578] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
16:09:34.86 =================================================================
16:09:34.86  End of dmesg log
16:09:34.86 =================================================================
16:09:34.86 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:34.86 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:34.94 SUCCESS: zfs destroy -f testpool/testfs
16:09:34.94 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
16:09:34.97 ASSERTION: CS-UN FS: delete succeeds if (case=same)
16:09:35.01 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:35.05 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:35.05 SUCCESS: create_file FïLëNÄmë
16:09:35.06 SUCCESS: delete_file FïLëNÄmë
16:09:35.06 SUCCESS: lookup_any exited 1
16:09:35.07 SUCCESS: create_file FïLëNÄmë
16:09:35.07 SUCCESS: delete_file FÏLËNÄMË exited 1
16:09:35.08 SUCCESS: create_file FïLëNÄmë
16:09:35.08 SUCCESS: delete_file fïlënämë exited 1
16:09:35.09 SUCCESS: create_file FïLëNÄmë
16:09:35.09 ERROR: delete_file FïLëNÄmë exited 1
16:09:35.09 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:35.09 =================================================================
16:09:35.09  Tailing last 200 lines of zfs_dbgmsg log
16:09:35.09 =================================================================
16:09:35.10 timestamp    message 
16:09:35.10 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:35.10 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 39936, appended 168 bytes
16:09:35.10 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 120 bytes
16:09:35.10 1678637374   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 317) (bptree, mintxg=1)
16:09:35.10 1678637374   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:35.10 1678637374   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
16:09:35.10 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 52224, unflushed_frees 43008, appended 152 bytes
16:09:35.10 1678637374   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:35.10 1678637374   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 399)  
16:09:35.10 1678637374   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 58368, appended 176 bytes
16:09:35.10 1678637375   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:35.10 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:35.10 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 39424, appended 136 bytes
16:09:35.10 1678637375   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 399) mountpoint=/var/tmp/testdir
16:09:35.10 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 62464, appended 224 bytes
16:09:35.11 =================================================================
16:09:35.11  End of zfs_dbgmsg log
16:09:35.11 =================================================================
16:09:35.11 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:35.11 =================================================================
16:09:35.11  Tailing last 200 lines of dmesg log
16:09:35.11 =================================================================
16:09:35.12 [  940.691224] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
16:09:35.12 =================================================================
16:09:35.12  End of dmesg log
16:09:35.12 =================================================================
16:09:35.12 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:35.12 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:35.20 SUCCESS: zfs destroy -f testpool/testfs
16:09:35.20 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
16:09:37.66 ASSERTION: CM-not-UN FS: CI lookup succeeds only if (norm=same)
16:09:37.69 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:37.73 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.74 SUCCESS: create_file FïLëNÄmë
16:09:37.74 SUCCESS: lookup_file_ci FïLëNÄmë
16:09:37.74 ERROR: lookup_file_ci FÏLËNÄMË exited 1
16:09:37.74 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:37.75 =================================================================
16:09:37.75  Tailing last 200 lines of zfs_dbgmsg log
16:09:37.75 =================================================================
16:09:37.75 timestamp    message 
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 39936, appended 192 bytes
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 28672, appended 112 bytes
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 399) (bptree, mintxg=1)
16:09:37.75 1678637375   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637375   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 43520, appended 168 bytes
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 328)  
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 58368, appended 192 bytes
16:09:37.75 1678637375   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 39424, appended 120 bytes
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 328) mountpoint=/var/tmp/testdir
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 61440, appended 208 bytes
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 58368, unflushed_frees 39936, appended 184 bytes
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 88 bytes
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 328) (bptree, mintxg=1)
16:09:37.75 1678637375   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637375   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 51712, unflushed_frees 43520, appended 120 bytes
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 340)  
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 58368, appended 152 bytes
16:09:37.75 1678637375   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637375   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39424, appended 128 bytes
16:09:37.75 1678637375   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 340) mountpoint=/var/tmp/testdir
16:09:37.75 1678637375   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 62976, appended 208 bytes
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 59904, unflushed_frees 41984, appended 168 bytes
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 29696, appended 128 bytes
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 340) (bptree, mintxg=1)
16:09:37.75 1678637376   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637376   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54272, unflushed_frees 45056, appended 160 bytes
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 350)  
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 59904, appended 192 bytes
16:09:37.75 1678637376   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 41472, appended 152 bytes
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 350) mountpoint=/var/tmp/testdir
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 65024, appended 216 bytes
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60416, unflushed_frees 43008, appended 184 bytes
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 31232, appended 120 bytes
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 350) (bptree, mintxg=1)
16:09:37.75 1678637376   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637376   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 45568, appended 152 bytes
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 422)  
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60416, appended 144 bytes
16:09:37.75 1678637376   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637376   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 41984, appended 120 bytes
16:09:37.75 1678637376   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 422) mountpoint=/var/tmp/testdir
16:09:37.75 1678637376   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 66048, appended 200 bytes
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 60928, unflushed_frees 43520, appended 144 bytes
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 30720, appended 112 bytes
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 422) (bptree, mintxg=1)
16:09:37.75 1678637377   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637377   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 54784, unflushed_frees 46080, appended 144 bytes
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 434)  
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 60928, appended 184 bytes
16:09:37.75 1678637377   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 41984, appended 136 bytes
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 434) mountpoint=/var/tmp/testdir
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 65536, appended 208 bytes
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 62464, unflushed_frees 43520, appended 192 bytes
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 31744, appended 112 bytes
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 434) (bptree, mintxg=1)
16:09:37.75 1678637377   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:37.75 1678637377   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 47616, appended 152 bytes
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 444)  
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 62464, appended 176 bytes
16:09:37.75 1678637377   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:37.75 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 43520, appended 128 bytes
16:09:37.75 1678637377   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 444) mountpoint=/var/tmp/testdir
16:09:37.75 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 66560, appended 216 bytes
16:09:37.76 =================================================================
16:09:37.76  End of zfs_dbgmsg log
16:09:37.76 =================================================================
16:09:37.76 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:37.76 =================================================================
16:09:37.76  Tailing last 200 lines of dmesg log
16:09:37.76 =================================================================
16:09:37.77 [  940.950350] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
16:09:37.77 [  941.305175] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
16:09:37.77 [  941.899807] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
16:09:37.77 [  942.252384] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
16:09:37.77 [  942.888957] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
16:09:37.77 [  943.374081] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
16:09:37.77 =================================================================
16:09:37.77  End of dmesg log
16:09:37.77 =================================================================
16:09:37.77 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:37.77 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:37.85 SUCCESS: zfs destroy -f testpool/testfs
16:09:37.86 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
16:09:38.29 ASSERTION: CM-UN FS: lookup succeeds if (case=same)
16:09:38.32 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.36 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.37 SUCCESS: create_file FïLëNÄmë
16:09:38.37 SUCCESS: lookup_file FïLëNÄmë
16:09:38.37 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:38.38 SUCCESS: lookup_file fïlënämë exited 1
16:09:38.38 SUCCESS: lookup_file FïLëNÄmë
16:09:38.38 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:38.39 SUCCESS: lookup_file fïlënämë exited 1
16:09:38.39 SUCCESS: create_file FÏLËNÄMË
16:09:38.40 SUCCESS: lookup_file FïLëNÄmë exited 1
16:09:38.40 SUCCESS: lookup_file FÏLËNÄMË
16:09:38.40 SUCCESS: lookup_file fïlënämë exited 1
16:09:38.41 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
16:09:38.41 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:38.41 =================================================================
16:09:38.41  Tailing last 200 lines of zfs_dbgmsg log
16:09:38.41 =================================================================
16:09:38.42 timestamp    message 
16:09:38.42 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 63488, unflushed_frees 45056, appended 168 bytes
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 33792, appended 104 bytes
16:09:38.42 1678637377   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 444) (bptree, mintxg=1)
16:09:38.42 1678637377   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:38.42 1678637377   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56832, unflushed_frees 47616, appended 160 bytes
16:09:38.42 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:38.42 1678637377   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 457)  
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 63488, appended 152 bytes
16:09:38.42 1678637377   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:38.42 1678637377   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 44544, appended 136 bytes
16:09:38.42 1678637377   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 457) mountpoint=/var/tmp/testdir
16:09:38.42 1678637377   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 68096, appended 232 bytes
16:09:38.42 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 62976, unflushed_frees 45056, appended 168 bytes
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 32768, appended 112 bytes
16:09:38.42 1678637378   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 457) (bptree, mintxg=1)
16:09:38.42 1678637378   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:38.42 1678637378   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57344, unflushed_frees 48128, appended 152 bytes
16:09:38.42 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:38.42 1678637378   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 469)  
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 62976, appended 160 bytes
16:09:38.42 1678637378   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:38.42 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 44544, appended 128 bytes
16:09:38.42 1678637378   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 469) mountpoint=/var/tmp/testdir
16:09:38.42 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 67584, appended 208 bytes
16:09:38.42 =================================================================
16:09:38.42  End of zfs_dbgmsg log
16:09:38.42 =================================================================
16:09:38.43 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:38.43 =================================================================
16:09:38.43  Tailing last 200 lines of dmesg log
16:09:38.43 =================================================================
16:09:38.43 [  943.603577] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
16:09:38.43 [  944.003039] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
16:09:38.43 =================================================================
16:09:38.43  End of dmesg log
16:09:38.43 =================================================================
16:09:38.43 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:38.44 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:38.52 SUCCESS: zfs destroy -f testpool/testfs
16:09:38.52 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
16:09:38.55 ASSERTION: CM-UN FS: CI lookup succeeds using any name form
16:09:38.59 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.63 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.63 SUCCESS: create_file FïLëNÄmë
16:09:38.63 SUCCESS: lookup_file_ci FïLëNÄmë
16:09:38.64 ERROR: lookup_file_ci FÏLËNÄMË exited 1
16:09:38.64 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:38.64 =================================================================
16:09:38.64  Tailing last 200 lines of zfs_dbgmsg log
16:09:38.64 =================================================================
16:09:38.65 timestamp    message 
16:09:38.65 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 64000, unflushed_frees 46080, appended 168 bytes
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 33280, appended 112 bytes
16:09:38.65 1678637378   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 469) (bptree, mintxg=1)
16:09:38.65 1678637378   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:38.65 1678637378   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 47616, appended 144 bytes
16:09:38.65 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:38.65 1678637378   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 370)  
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 64000, appended 184 bytes
16:09:38.65 1678637378   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:38.65 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 45056, appended 128 bytes
16:09:38.65 1678637378   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 370) mountpoint=/var/tmp/testdir
16:09:38.65 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 60928, unflushed_frees 69120, appended 216 bytes
16:09:38.66 =================================================================
16:09:38.66  End of zfs_dbgmsg log
16:09:38.66 =================================================================
16:09:38.66 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:38.66 =================================================================
16:09:38.66  Tailing last 200 lines of dmesg log
16:09:38.66 =================================================================
16:09:38.66 [  944.269386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
16:09:38.66 =================================================================
16:09:38.66  End of dmesg log
16:09:38.66 =================================================================
16:09:38.67 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:38.67 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:38.75 SUCCESS: zfs destroy -f testpool/testfs
16:09:38.75 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
16:09:38.78 ASSERTION: CM-UN FS: delete succeeds if (case=same)
16:09:38.82 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.86 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.87 SUCCESS: create_file FïLëNÄmë
16:09:38.87 SUCCESS: delete_file FïLëNÄmë
16:09:38.87 SUCCESS: lookup_any exited 1
16:09:38.88 SUCCESS: create_file FïLëNÄmë
16:09:38.88 SUCCESS: delete_file FÏLËNÄMË exited 1
16:09:38.89 SUCCESS: create_file FïLëNÄmë
16:09:38.89 SUCCESS: delete_file fïlënämë exited 1
16:09:38.90 SUCCESS: create_file FïLëNÄmë
16:09:38.90 ERROR: delete_file FïLëNÄmë exited 1
16:09:38.91 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:38.91 =================================================================
16:09:38.91  Tailing last 200 lines of zfs_dbgmsg log
16:09:38.91 =================================================================
16:09:38.91 timestamp    message 
16:09:38.91 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 169, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 65024, unflushed_frees 46592, appended 184 bytes
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 170, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 35840, appended 96 bytes
16:09:38.91 1678637378   spa_history.c:297:spa_history_log_sync(): txg 171 destroy testpool/testfs (id 370) (bptree, mintxg=1)
16:09:38.91 1678637378   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:38.91 1678637378   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 171; err=0
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 171, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 50176, appended 144 bytes
16:09:38.91 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:38.91 1678637378   spa_history.c:297:spa_history_log_sync(): txg 172 create testpool/testfs (id 381)  
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 172, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 65024, appended 184 bytes
16:09:38.91 1678637378   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:38.91 1678637378   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 173, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 42496, unflushed_frees 46080, appended 144 bytes
16:09:38.91 1678637378   spa_history.c:297:spa_history_log_sync(): txg 174 set testpool/testfs (id 381) mountpoint=/var/tmp/testdir
16:09:38.91 1678637378   metaslab.c:3926:metaslab_flush(): flushing: txg 174, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 61952, unflushed_frees 69632, appended 224 bytes
16:09:38.92 =================================================================
16:09:38.92  End of zfs_dbgmsg log
16:09:38.92 =================================================================
16:09:38.92 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:38.92 =================================================================
16:09:38.92  Tailing last 200 lines of dmesg log
16:09:38.92 =================================================================
16:09:38.93 [  944.498083] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete
16:09:38.93 =================================================================
16:09:38.93  End of dmesg log
16:09:38.93 =================================================================
16:09:38.93 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:38.93 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:39.02 SUCCESS: zfs destroy -f testpool/testfs
16:09:39.02 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:16] [FAIL]
16:57:56.27 SUCCESS: set_tunable32 TXG_HISTORY 100
16:57:56.27 SUCCESS: mkdir -p /var/tmp/bakdev_import-test
16:57:56.28 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk0
16:57:56.28 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk1
16:57:56.29 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk2
16:57:56.29 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk3
16:57:56.30 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk4
16:57:56.30 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk5
16:57:56.30 NOTE: test_replace_vdev: pool '/var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1', replace /var/tmp/dev_import-test/disk1 by /var/tmp/dev_import-test/disk2.
16:57:56.37 SUCCESS: zpool create testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
16:57:56.41 SUCCESS: zfs create testpool1/ds1
16:57:56.51 SUCCESS: zpool sync testpool1
16:57:56.55 SUCCESS: zfs create testpool1/ds2
16:57:56.64 SUCCESS: zpool sync testpool1
16:57:56.68 SUCCESS: zfs create testpool1/ds3
16:57:56.78 SUCCESS: zpool sync testpool1
16:57:56.78 SUCCESS: generate_data testpool1 /var/tmp/md5sums.628998
16:57:57.76 SUCCESS: write_some_data testpool1 15
16:57:57.80 SUCCESS: zpool sync testpool1
16:57:57.84 SUCCESS: zpool sync testpool1
16:57:57.87 SUCCESS: zpool sync testpool1
16:57:57.91 SUCCESS: zpool sync testpool1
16:57:57.94 SUCCESS: zpool sync testpool1
16:57:57.97 SUCCESS: zpool sync testpool1
16:57:58.01 SUCCESS: zpool sync testpool1
16:57:58.04 SUCCESS: zpool sync testpool1
16:57:58.08 SUCCESS: zpool sync testpool1
16:57:58.11 SUCCESS: zpool sync testpool1
16:57:58.14 SUCCESS: zpool sync testpool1
16:57:58.15 SUCCESS: sync_some_data_a_few_times testpool1
16:58:01.03 SUCCESS: zfs snapshot -r testpool1@snap1
16:58:01.12 SUCCESS: overwrite_data testpool1 
16:58:01.25 SUCCESS: zpool export testpool1
16:58:01.44 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
16:58:01.45 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 1
16:58:01.50 SUCCESS: zpool replace testpool1 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk2
16:58:01.53 SUCCESS: pool_is_replacing testpool1
16:58:07.68 SUCCESS: zpool export testpool1
16:58:07.69 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
16:58:07.90 SUCCESS: zpool import -d /var/tmp/dev_import-test -o readonly=on -T 53 testpool1
16:58:07.96 SUCCESS: check_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
16:58:08.05 SUCCESS: verify_data_md5sums /var/tmp/md5sums.628998
16:58:08.09 SUCCESS: zpool export testpool1
16:58:08.68 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
16:58:08.78 SUCCESS: overwrite_data testpool1 
16:58:11.92 SUCCESS: wait_for_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk2
16:58:11.99 SUCCESS: zpool export testpool1
16:58:11.99 SUCCESS: mv /var/tmp/dev_import-test/disk2 /var/tmp/bakdev_import-test/
16:58:12.34 cannot import 'testpool1': one or more devices is currently unavailable
16:58:12.34 ERROR: zpool import -d /var/tmp/dev_import-test -T 53 testpool1 exited 1
16:58:12.34 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:58:12.34 =================================================================
16:58:12.34  Tailing last 200 lines of zfs_dbgmsg log
16:58:12.34 =================================================================
16:58:12.36 1678640291   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 1, ms_id 3, unflushed_allocs 13824, unflushed_frees 13824, appended 32 bytes
16:58:12.36 1678640291   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool1, vdev_id 0, ms_id 12, unflushed_allocs 0, unflushed_frees 1024, appended 16 bytes
16:58:12.36 1678640291   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config trusted): UNLOADING
16:58:12.36 1678640291   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool1' gethrtime 3885912851500
16:58:12.36 1678640292   spa.c:6319:spa_tryimport(): spa_tryimport: importing testpool1, max_txg=53
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa $import. txg 53
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=53
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load($import, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load($import, config untrusted): UNLOADING
16:58:12.36 1678640292   spa.c:6176:spa_import(): spa_import: importing testpool1, max_txg=53 (RECOVERY MODE)
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config trusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 53
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 53)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=53
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 52
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 50
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 50)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=50
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 49
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 47
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 47)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=47
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 46
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 44
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 44)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=44
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 43
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 41
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 41)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=41
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 40
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 38
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 38)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=38
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 37
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 35
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 35)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=35
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 34
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 32
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 32)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=32
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 31
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 29
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 29)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=29
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 28
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 26
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 26)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=26
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 25
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 23
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 23)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=23
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 22
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 22
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 22)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=22
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 21
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 21
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 21)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=21
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 20
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 20
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 20)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=20
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 19
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 17
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 17)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=17
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 16
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 16
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 16)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=16
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 15
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 13
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 13)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=13
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 12
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 12
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 12)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=12
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 11
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 9
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 9)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=9
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 8
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 8
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 8)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=8
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 7
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 6
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 6)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=6
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 5
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 5
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 5)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=5
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 4
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 4
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (130 > 4)
16:58:12.36 1678640292   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=4
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 3
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:58:12.36 1678640292   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: no valid uberblock found
16:58:12.36 1678640292   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:58:12.37 =================================================================
16:58:12.37  End of zfs_dbgmsg log
16:58:12.37 =================================================================
16:58:12.37 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:58:12.37 =================================================================
16:58:12.37  Tailing last 200 lines of dmesg log
16:58:12.37 =================================================================
16:58:12.38 [ 3268.435751] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg
16:58:12.38 [ 3268.598458] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos
16:58:12.38 [ 3270.130387] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup
16:58:12.38 [ 3270.202492] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup
16:58:12.38 [ 3270.526058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos
16:58:12.38 [ 3270.577093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos
16:58:12.38 [ 3270.960287] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos
16:58:12.38 [ 3272.626091] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg
16:58:12.38 [ 3272.689698] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos
16:58:12.38 [ 3272.951642] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup
16:58:12.38 [ 3273.215093] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup
16:58:12.38 [ 3273.722057] debugfs: Directory 'zd0' with parent 'block' already present!
16:58:12.38 [ 3274.291445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg
16:58:12.38 [ 3274.677343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos
16:58:12.38 [ 3274.889384] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup
16:58:12.38 [ 3275.146654] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup
16:58:12.38 [ 3275.491894] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos
16:58:12.38 [ 3284.298705] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos
16:58:12.38 [ 3293.122633] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos
16:58:12.38 [ 3293.836851] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos
16:58:12.38 [ 3303.183970] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos
16:58:12.38 [ 3312.597275] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos
16:58:12.38 [ 3323.796544] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos
16:58:12.38 [ 3335.488514] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos
16:58:12.38 [ 3349.712452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg
16:58:12.38 [ 3354.608528] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos
16:58:12.38 [ 3361.568537] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg
16:58:12.38 [ 3369.067461] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos
16:58:12.38 [ 3402.850558] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg
16:58:12.38 [ 3478.265751] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos
16:58:12.38 [ 3482.190922] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos
16:58:12.38 [ 3485.207960] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos
16:58:12.38 [ 3495.628372] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos
16:58:12.38 [ 3509.879022] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos
16:58:12.38 [ 3522.203890] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg
16:58:12.38 [ 3536.317668] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos
16:58:12.38 [ 3557.502681] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos
16:58:12.38 [ 3603.128918] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos
16:58:12.38 [ 3665.508748] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos
16:58:12.38 [ 3665.554966] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos
16:58:12.38 [ 3674.946852] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos
16:58:12.38 [ 3678.663448] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted
16:58:12.38 [ 3679.752169] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load
16:58:12.38 [ 3682.218463] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3
16:58:12.38 [ 3684.319470] debugfs: Directory 'zd0' with parent 'block' already present!
16:58:12.38 [ 3685.269481] debugfs: Directory 'zd16' with parent 'block' already present!
16:58:12.38 [ 3685.983013] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4
16:58:12.38 [ 3688.940638] debugfs: Directory 'zd0' with parent 'block' already present!
16:58:12.38 [ 3689.813006] debugfs: Directory 'zd16' with parent 'block' already present!
16:58:12.38 [ 3691.116144] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added
16:58:12.38 [ 3696.892650] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed
16:58:12.38 [ 3714.775270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced
16:58:12.38 [ 3758.456141] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached
16:58:12.38 [ 3760.309425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached
16:58:12.38 [ 3766.193677] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed
16:58:12.38 [ 3771.084886] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device
16:58:12.38 [ 3772.979445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing
16:58:12.38 [ 3783.089998] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed
16:58:12.38 [ 3786.398743] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed
16:58:12.38 [ 3870.705903] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced
16:58:12.38 =================================================================
16:58:12.38  End of dmesg log
16:58:12.38 =================================================================
16:58:12.38 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:58:12.38 NOTE: Performing local cleanup via log_onexit (custom_cleanup)
16:58:12.39 SUCCESS: set_zfs_txg_timeout 5
16:58:12.41 SUCCESS: rm -rf /var/tmp/bakdev_import-test
16:58:12.41 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
16:58:12.43 SUCCESS: eval zinject -c all > /dev/null
16:58:12.45 NOTE: Pool does not exist. (testpool1)
16:58:12.45 SUCCESS: rm -f /var/tmp/cachefile.628998 /var/tmp/cachefile.628998.bkp /var/tmp/cachefile.628998.bkp2 /var/tmp/md5sums.628998 /var/tmp/md5sums.628998.2
16:58:12.50 SUCCESS: rm -rf /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk3 /var/tmp/dev_import-test/disk4 /var/tmp/dev_import-test/disk5
16:58:12.51 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk0
16:58:12.51 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk1
16:58:12.52 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk2
16:58:12.52 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk3
16:58:12.53 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk4
16:58:12.53 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk5
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:11] [FAIL]
16:35:28.42 SUCCESS: zpool create -f testpool mirror loop0 loop1
16:35:28.42 ASSERTION: Per-vdev ZAPs persist correctly on the original pool after split.
16:35:31.04 SUCCESS: eval zdb -PC testpool > /var/tmp/testdir/vz007
16:35:31.04 SUCCESS: grep -q com.delphix:has_per_vdev_zaps /var/tmp/testdir/vz007
16:35:38.93 SUCCESS: zpool split testpool testpool2 loop1
16:35:39.07 ERROR: eval zdb -PC testpool > /var/tmp/testdir/vz007 exited 2
16:35:39.07 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:35:39.08 =================================================================
16:35:39.08  Tailing last 200 lines of zfs_dbgmsg log
16:35:39.08 =================================================================
16:35:39.08 1678638917   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:35:39.08 1678638917   spa.c:8440:spa_async_request(): spa=$import async request task=2048
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): LOADED
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): UNLOADING
16:35:39.08 1678638917   spa.c:6174:spa_import(): spa_import: importing testpool
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): LOADING
16:35:39.08 1678638917   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa testpool. txg 22
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load(testpool, config untrusted): using uberblock with txg=22
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): read 1 log space maps (1 total blocks - blksz = 131072 bytes) in 0 ms
16:35:39.08 1678638917   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:35:39.08 1678638917   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2487923276800
16:35:39.08 1678638917   spa.c:8440:spa_async_request(): spa=testpool async request task=1
16:35:39.08 1678638917   spa.c:8440:spa_async_request(): spa=testpool async request task=2048
16:35:39.08 1678638917   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): LOADED
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487924 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487924 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487924 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   spa_history.c:306:spa_history_log_sync(): txg 24 open pool version 5000; software version 0280905; uts fv-az442-328 5.15.0-1034-azure #41~20.04.1-Ubuntu SMP Sat Feb 11 17:02:42 UTC 2023 x86_64
16:35:39.08 1678638917   metaslab.c:3926:metaslab_flush(): flushing: txg 24, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 11776, unflushed_frees 13824, appended 64 bytes
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 0, smp_length 192, unflushed_allocs 0, unflushed_frees 10752, freed 0, defer 10752 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268354048, max size error 268345344, old_weight 6c0000000000001, new_weight 6c0000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 1, smp_length 120, unflushed_allocs 3584, unflushed_frees 16384, freed 0, defer 10752 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268354048, max size error 268345344, old_weight 6c0000000000001, new_weight 6c0000000000001
16:35:39.08 1678638917   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 24, spa testpool, vdev_id 0, ms_id 2, smp_length 104, unflushed_allocs 3584, unflushed_frees 16384, freed 0, defer 10752 + 0, unloaded time 2487931 ms, loading_time 0 ms, ms_max_size 268374016, max size error 268365312, old_weight 6c0000000000001, new_weight 6c0000000000001
16:35:39.08 1678638917   spa.c:8440:spa_async_request(): spa=testpool async request task=32
16:35:39.08 1678638917   spa_history.c:306:spa_history_log_sync(): txg 26 import pool version 5000; software version 0280905; uts fv-az442-328 5.15.0-1034-azure #41~20.04.1-Ubuntu SMP Sat Feb 11 17:02:42 UTC 2023 x86_64
16:35:39.08 1678638917   metaslab.c:3926:metaslab_flush(): flushing: txg 26, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 3584, unflushed_frees 16384, appended 80 bytes
16:35:39.08 1678638919   spa_history.c:293:spa_history_log_sync(): command: zpool import testpool
16:35:39.08 1678638919   metaslab.c:3926:metaslab_flush(): flushing: txg 28, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 2048, unflushed_frees 16384, appended 64 bytes
16:35:39.08 1678638919   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
16:35:39.08 1678638919   metaslab.c:3926:metaslab_flush(): flushing: txg 29, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 14336, appended 32 bytes
16:35:39.08 1678638919   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
16:35:39.08 1678638919   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 3, unflushed_allocs 17408, unflushed_frees 0, appended 64 bytes
16:35:39.08 1678638919   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2490615285000
16:35:39.08 1678638920   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 0280905; uts fv-az442-328 5.15.0-1034-azure #41~20.04.1-Ubuntu SMP Sat Feb 11 17:02:42 UTC 2023 x86_64
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
16:35:39.08 1678638920   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@block_cloning=enabled
16:35:39.08 1678638920   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2490806100500
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490806 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490806 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490807 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2490828 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 34816, unflushed_frees 0, appended 24 bytes
16:35:39.08 1678638920   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool loop0
16:35:39.08 1678638920   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 0, appended 64 bytes
16:35:39.08 1678638920   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 0, appended 72 bytes
16:35:39.08 1678638920   metaslab.c:3926:metaslab_flush(): flushing: txg 10, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 17408, appended 120 bytes
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491033 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491033 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491033 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491033 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491033 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491034 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491034 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491034 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491034 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638920   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2491034 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638925   spa_history.c:293:spa_history_log_sync(): command: zpool add -f testpool loop1
16:35:39.08 1678638925   metaslab.c:3926:metaslab_flush(): flushing: txg 11, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 15872, unflushed_frees 12800, appended 104 bytes
16:35:39.08 1678638925   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 11, spa testpool, vdev_id 1, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2496235 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
16:35:39.08 1678638928   metaslab.c:3926:metaslab_flush(): flushing: txg 13, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 5120, unflushed_frees 14848, appended 88 bytes
16:35:39.08 1678638928   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
16:35:39.08 1678638928   metaslab.c:3926:metaslab_flush(): flushing: txg 22, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 17408, unflushed_frees 15872, appended 104 bytes
16:35:39.08 1678638928   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2498830540300
16:35:39.08 1678638928   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 0280905; uts fv-az442-328 5.15.0-1034-azure #41~20.04.1-Ubuntu SMP Sat Feb 11 17:02:42 UTC 2023 x86_64
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
16:35:39.08 1678638928   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@block_cloning=enabled
16:35:39.08 1678638928   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2499167360800
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499167 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499167 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499168 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2499180 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638928   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 34816, unflushed_frees 0, appended 32 bytes
16:35:39.08 1678638928   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool mirror loop0 loop1
16:35:39.08 1678638928   metaslab.c:3926:metaslab_flush(): flushing: txg 6, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 0, appended 56 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 0, appended 56 bytes
16:35:39.08 1678638938   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': txg 14, spa testpool, DTL old object 0, new object 142
16:35:39.08 1678638938   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): LOADING
16:35:39.08 1678638938   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': best uberblock found for spa testpool2. txg 6
16:35:39.08 1678638938   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): using uberblock with txg=6
16:35:39.08 1678638938   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 4d467554854a4 to 762b3606cb9470 for pool testpool2 dataset id 48
16:35:39.08 1678638938   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): read 3 log space maps (3 total blocks - blksz = 131072 bytes) in 0 ms
16:35:39.08 1678638938   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:35:39.08 1678638938   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 90c761bcf96d72 to fc7f192ccb6550 for pool testpool2 dataset id 54
16:35:39.08 1678638938   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 90c761bcf96d72 to 2cd9a185ad3d75 for pool testpool2 dataset id 54
16:35:39.08 1678638938   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 90c761bcf96d72 to 9365672d7e8865 for pool testpool2 dataset id 54
16:35:39.08 1678638938   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool2' gethrtime 2509654539100
16:35:39.08 1678638938   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2509654 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638938   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2509654 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638938   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 7, spa testpool2, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2509655 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 7, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 0, appended 56 bytes
16:35:39.08 1678638938   spa.c:8440:spa_async_request(): spa=testpool2 async request task=1
16:35:39.08 1678638938   spa.c:8440:spa_async_request(): spa=testpool2 async request task=2048
16:35:39.08 1678638938   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): LOADED
16:35:39.08 1678638938   spa_history.c:306:spa_history_log_sync(): txg 8 open pool version 5000; software version 0280905; uts fv-az442-328 5.15.0-1034-azure #41~20.04.1-Ubuntu SMP Sat Feb 11 17:02:42 UTC 2023 x86_64
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 13312, unflushed_frees 22016, appended 96 bytes
16:35:39.08 1678638938   spa_history.c:306:spa_history_log_sync(): txg 15 detach vdev=/dev/loop1
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 15, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 17408, appended 112 bytes
16:35:39.08 1678638938   spa_history.c:306:spa_history_log_sync(): txg 9 split from pool testpool
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 2048, unflushed_frees 17408, appended 72 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 0, unflushed_frees 18944, appended 40 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 3, unflushed_allocs 20480, unflushed_frees 0, appended 64 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 4, unflushed_allocs 20480, unflushed_frees 0, appended 64 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 5, unflushed_allocs 19968, unflushed_frees 0, appended 56 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 6144, appended 32 bytes
16:35:39.08 1678638938   metaslab.c:3926:metaslab_flush(): flushing: txg 18, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
16:35:39.08 1678638938   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): UNLOADING
16:35:39.08 1678638938   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool2' gethrtime 2509697722700
16:35:39.09 =================================================================
16:35:39.09  End of zfs_dbgmsg log
16:35:39.09 =================================================================
16:35:39.09 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:35:39.09 =================================================================
16:35:39.09  Tailing last 200 lines of dmesg log
16:35:39.09 =================================================================
16:35:39.10 [ 2393.325902] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos
16:35:39.10 [ 2393.883618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos
16:35:39.10 [ 2394.302650] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos
16:35:39.10 [ 2395.271036] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg
16:35:39.10 [ 2395.607251] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos
16:35:39.10 [ 2400.093177] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos
16:35:39.10 [ 2403.592814] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted
16:35:39.10 [ 2406.989733] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted
16:35:39.10 [ 2414.593689] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709
16:35:39.10 [ 2415.705155] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
16:35:39.10 [ 2416.421793] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/setup
16:35:39.10 [ 2422.372219] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos
16:35:39.10 [ 2424.389445] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos
16:35:39.10 [ 2425.209431] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos
16:35:39.10 [ 2425.995549] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos
16:35:39.10 [ 2426.771952] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos
16:35:39.10 [ 2427.705411] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
16:35:39.10 [ 2429.604362] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup
16:35:39.10 [ 2429.630300] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos
16:35:39.10 [ 2437.596357] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos
16:35:39.10 [ 2456.468904] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos
16:35:39.10 [ 2470.100997] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos
16:35:39.10 [ 2480.912907] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos
16:35:39.10 [ 2491.076547] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos
16:35:39.10 [ 2499.308628] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos
16:35:39.10 =================================================================
16:35:39.10  End of dmesg log
16:35:39.10 =================================================================
16:35:39.10 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:35:39.10 NOTE: Performing local cleanup via log_onexit (cleanup)
16:35:39.17 SUCCESS: zpool destroy -f testpool
16:35:39.18 SUCCESS: rm -f /var/tmp/testdir/vz007
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
16:26:04.39 ASSERTION: Verify refreservation is limited by available space.
16:26:04.43 SUCCESS: zfs create testpool/testfs/subfs
16:26:04.46 SUCCESS: zfs set quota=25M testpool
16:26:04.48 SUCCESS: zfs set refreservation=15M testpool
16:26:04.52 SUCCESS: zfs set refreservation=10259968 testpool/testfs/subfs
16:26:04.63 /var/tmp/testdir/subfs/testfile: initialized 1835008 of 10259968 bytes: Disk quota exceeded
16:26:04.63 ERROR: mkfile 10259968 /var/tmp/testdir/subfs/testfile exited 1
16:26:04.63 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:26:04.63 =================================================================
16:26:04.63  Tailing last 200 lines of zfs_dbgmsg log
16:26:04.63 =================================================================
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 264, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 24064, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 265, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 818688, unflushed_frees 31232, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 266, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 31744, unflushed_frees 31232, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 267, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 24576, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 268, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 687616, unflushed_frees 32256, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 269, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 32256, unflushed_frees 31744, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 270, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24576, unflushed_frees 24576, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 271, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 425472, unflushed_frees 32256, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 272, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 273, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 24576, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 274, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 425472, unflushed_frees 32256, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 275, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 32768, unflushed_frees 32768, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 276, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 25088, appended 72 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 277, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 425984, unflushed_frees 32256, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 278, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33280, unflushed_frees 32768, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 279, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 25088, appended 72 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 280, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427008, unflushed_frees 32768, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 281, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33792, unflushed_frees 33280, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 282, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 25600, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 283, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427008, unflushed_frees 33792, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 284, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33792, unflushed_frees 33792, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 285, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 25600, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 286, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427008, unflushed_frees 33792, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 287, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 33280, unflushed_frees 33792, appended 120 bytes
16:26:04.65 1678638363   spa_history.c:297:spa_history_log_sync(): txg 288 snapshot testpool/testfs@snap (id 336)  
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 288, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 25600, appended 88 bytes
16:26:04.65 1678638363   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
16:26:04.65 1678638363   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 289, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 306688, unflushed_frees 169472, appended 136 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 290, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 54272, unflushed_frees 37888, appended 144 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 291, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 30720, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 292, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 30720, appended 144 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 293, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 33792, appended 136 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 294, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 26624, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 295, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427520, unflushed_frees 33792, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 296, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 34304, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 297, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 27136, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 298, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427520, unflushed_frees 34304, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 299, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 34304, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 300, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 27136, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 301, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 427520, unflushed_frees 34304, appended 136 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 302, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 34304, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 303, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 27136, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 304, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 428032, unflushed_frees 34304, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 305, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34816, unflushed_frees 34304, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 306, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 27136, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 307, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 428032, unflushed_frees 34816, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 308, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35328, unflushed_frees 34816, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 309, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 27648, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 310, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 429056, unflushed_frees 34816, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 311, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35840, unflushed_frees 35328, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 312, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 313, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 429056, unflushed_frees 35840, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 314, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 35840, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 315, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 28160, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 316, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430592, unflushed_frees 35840, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 317, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 36352, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 318, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29696, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 319, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 37376, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 320, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 36864, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 321, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 29184, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 322, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 429568, unflushed_frees 35840, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 323, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 36352, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 324, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28672, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 325, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 429568, unflushed_frees 36352, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 36352, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28672, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 36352, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 36352, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28672, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430592, unflushed_frees 36864, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 36864, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 28672, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430592, unflushed_frees 37376, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37376, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29184, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431104, unflushed_frees 37376, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 72 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431104, unflushed_frees 38400, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 38400, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 30208, appended 80 bytes
16:26:04.65 1678638363   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 365)  
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 168960, appended 112 bytes
16:26:04.65 1678638363   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
16:26:04.65 1678638363   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 136 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 40448, appended 144 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55296, unflushed_frees 46592, appended 168 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 35328, appended 128 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430592, unflushed_frees 36864, appended 120 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 37888, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 72 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431104, unflushed_frees 37376, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37376, appended 96 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 30720, appended 72 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 37888, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38400, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31232, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38912, appended 112 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 104 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 88 bytes
16:26:04.65 1678638363   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 39424, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 80 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39424, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32256, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 39936, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 39936, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 40448, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32768, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 39424, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 31232, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 38912, appended 128 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 39936, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32768, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 40448, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 40448, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32768, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 40448, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 40448, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 40448, appended 136 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40448, appended 128 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 33280, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 136 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 33280, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 41472, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 33280, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41472, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434688, unflushed_frees 41472, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 33792, appended 88 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41472, appended 128 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 96 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 34304, appended 80 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 173056, appended 120 bytes
16:26:04.65 1678638364   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
16:26:04.65 1678638364   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 365)  
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 336)  
16:26:04.65 1678638364   dsl_scan.c:3493:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 88 bytes
16:26:04.65 1678638364   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 43520, unflushed_frees 47616, appended 136 bytes
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 314) refreservation=0
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 314) (bptree, mintxg=1)
16:26:04.65 1678638364   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:26:04.65 1678638364   dsl_scan.c:3493:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 50688, unflushed_frees 67584, appended 192 bytes
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 533)  
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 90112, appended 264 bytes
16:26:04.65 1678638364   spa_history.c:329:spa_history_log_sync(): ioctl create
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 44544, unflushed_frees 53248, appended 128 bytes
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 533) mountpoint=/var/tmp/testdir
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 64000, unflushed_frees 22099968, appended 856 bytes
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 542)  
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 69120, unflushed_frees 50688, appended 168 bytes
16:26:04.65 1678638364   spa_history.c:329:spa_history_log_sync(): ioctl create
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45568, unflushed_frees 39424, appended 112 bytes
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 71168, unflushed_frees 53760, appended 160 bytes
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
16:26:04.65 1678638364   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 542) refreservation=10259968
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 67584, unflushed_frees 54784, appended 160 bytes
16:26:04.65 1678638364   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10259968 testpool/testfs/subfs
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 40960, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48640, unflushed_frees 47616, appended 128 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 48128, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41472, unflushed_frees 41984, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 305664, unflushed_frees 42496, appended 152 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43008, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 36352, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 43520, appended 128 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43520, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 36352, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 43520, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 43520, appended 104 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36352, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 43520, appended 120 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 44032, appended 112 bytes
16:26:04.65 1678638364   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 36864, appended 104 bytes
16:26:04.66 =================================================================
16:26:04.66  End of zfs_dbgmsg log
16:26:04.66 =================================================================
16:26:04.66 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:26:04.66 =================================================================
16:26:04.66  Tailing last 200 lines of dmesg log
16:26:04.66 =================================================================
16:26:04.67 [  411.441092] loop0: detected capacity change from 0 to 6291456
16:26:04.67 [  411.468110] loop1: detected capacity change from 0 to 6291456
16:26:04.67 [  411.500860] loop2: detected capacity change from 0 to 6291456
16:26:04.67 [  411.679252] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
16:26:04.67 [  411.704668] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
16:26:04.67 [  413.747756] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
16:26:04.67 [  716.106323] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
16:26:04.67 [  779.089730] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
16:26:04.67 [  841.332478] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
16:26:04.67 [  841.356393] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
16:26:04.67 [  841.822180] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
16:26:04.67 [  843.336517] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
16:26:04.67 [  847.868689] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
16:26:04.67 [  849.167980] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
16:26:04.67 [  850.483922] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
16:26:04.67 [  902.587907] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
16:26:04.67 [  909.537003] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
16:26:04.67 [  915.751121] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
16:26:04.67 [  917.958489] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
16:26:04.67 [  926.673680] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
16:26:04.67 [  928.920503] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
16:26:04.67 [  930.506602] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
16:26:04.67 [  931.665014] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
16:26:04.67 [  934.430854] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
16:26:04.67 [  994.557686] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
16:26:04.67 [  997.472448] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
16:26:04.67 [  999.601511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
16:26:04.67 [ 1000.294621] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
16:26:04.67 [ 1000.379620] debugfs: Directory 'zd0' with parent 'block' already present!
16:26:04.67 [ 1010.733907] debugfs: Directory 'zd0' with parent 'block' already present!
16:26:04.67 [ 1010.937352] debugfs: Directory 'zd16' with parent 'block' already present!
16:26:04.67 [ 1011.087999] debugfs: Directory 'zd32' with parent 'block' already present!
16:26:04.67 [ 1021.445770] debugfs: Directory 'zd32' with parent 'block' already present!
16:26:04.67 [ 1021.778595] debugfs: Directory 'zd32' with parent 'block' already present!
16:26:04.67 [ 1032.125951] debugfs: Directory 'zd32' with parent 'block' already present!
16:26:04.67 [ 1032.361684] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
16:26:04.67 [ 1032.629432] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
16:26:04.67 [ 1032.654419] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
16:26:04.67 [ 1205.248356] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
16:26:04.67 [ 1216.485323] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
16:26:04.67 [ 1252.089973] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
16:26:04.67 [ 1291.873618] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
16:26:04.67 [ 1417.815008] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
16:26:04.67 [ 1519.920592] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
16:26:04.67 [ 1565.342476] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
16:26:04.67 [ 1585.806046] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
16:26:04.67 [ 1663.202864] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
16:26:04.67 [ 1674.495260] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
16:26:04.67 [ 1844.276123] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
16:26:04.67 [ 1864.536792] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
16:26:04.67 [ 1886.398916] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
16:26:04.67 [ 1919.563507] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
16:26:04.67 [ 1924.393669] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
16:26:04.67 [ 1924.433942] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
16:26:04.67 [ 1924.757511] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
16:26:04.67 [ 1927.563302] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
16:26:04.67 [ 1929.637864] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
16:26:04.67 [ 1931.405342] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
16:26:04.67 [ 1933.281965] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
16:26:04.67 [ 1935.285911] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
16:26:04.67 [ 1936.069049] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
16:26:04.67 [ 1936.441547] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
16:26:04.67 [ 1944.147727] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
16:26:04.67 [ 1944.420758] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
16:26:04.67 [ 1944.744893] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
16:26:04.67 [ 1945.477351] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
16:26:04.67 [ 1947.312134] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
16:26:04.67 [ 1948.346432] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
16:26:04.67 =================================================================
16:26:04.67  End of dmesg log
16:26:04.67 =================================================================
16:26:04.67 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:26:04.67 NOTE: Performing local cleanup via log_onexit (cleanup)
16:26:04.70 SUCCESS: zfs set refreservation=none testpool
16:26:04.77 SUCCESS: zfs destroy -rf testpool/testfs
16:26:04.80 SUCCESS: zfs create testpool/testfs
16:26:04.85 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>Full Listing</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos (run as root) [02:05] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive (run as root) [03:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/setup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos (run as root) [01:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos (run as root) [00:01] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/setup (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/chattr_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/chattr_002_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_edonr_test (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_sha2_test (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_skein_test (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/run_blake3_test (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_001_pos (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/filetest_002_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/checksum/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_002_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/setup (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_001_pos (run as runner) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_user/zfs_list/zfs_list_002_pos (run as runner) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted_no_compressed_arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/compress_004_pos (run as root) [00:17] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/deadman/deadman_zio (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/setup (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_003_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_005_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_006_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_007_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_010_pos (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_012_neg (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_007_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_008_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_002_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/read_dos_attrs_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/write_dos_attrs_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/events_001_pos (run as root) [00:39] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/events_002_pos (run as root) [00:53] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_rc_filter (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_fd_spill (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_cksum_reported (run as root) [00:07] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_cksum_config (run as root) [00:38] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_io_config (run as root) [01:24] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/fadvise_sequential (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_punch-hole (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_prealloc (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_zero-range (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_offline_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_online_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_online_002_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_replace_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_001_pos (run as root) [01:09] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_002_pos (run as root) [00:07] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_multiple (run as root) [03:55] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_ashift (run as root) [00:02] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_shared (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/decrypt_fault (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/decompress_fault (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/scrub_after_resilver (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/zpool_status_-s (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/async_destroy_001_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_009_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_002_pos (run as root) [00:13] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_006_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_008_pos (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_002_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_003_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_010_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_002 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_003 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_004 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_005 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/inherit_001_pos (run as root) [01:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_005_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_008_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inuse/inuse_009_pos (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/sync (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/psync (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/posixaio (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/mmap (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/libaio (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/io_uring (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [00:53] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/largest_pool/largest_pool_001_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_libaio_001_pos (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_thread (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_uberblocks (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_off (run as root) [00:18] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_interval (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_active_import (run as root) [02:56] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_inactive_import (run as root) [01:59] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_exported_import (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_write_uberblocks (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_reset_interval (run as root) [05:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/multihost_history (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_zdb (run as root) [00:34] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_write_distribution (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_hostid (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/umount_unlinked_drain (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [01:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_002_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_006_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_pos (run as root) [02:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_block_size_histogram (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_checksum (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_display_block (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_encrypted (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_neg (run as root) [00:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_pos (run as root) [00:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_objset_id (run as root) [00:22] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress_zstd (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover_2 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_003_neg (run as root) [00:30] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_010_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_deeply_nested (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_001_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_003_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_006_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_010_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_013_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_encrypted (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_crypt_combos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_dryrun (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_nomount (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_verbose (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_and_disable (run as root) [00:53] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_races (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_dedup (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_001_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_005_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_013_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_015_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_016_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_clone_livelist (run as root) [01:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_changes (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_timestamp (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_types (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_mangle (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_001_pos (run as root) [01:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_002_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_005_neg (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_008_pos (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_009_pos (run as root) [01:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/zfs_ids_to_path_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_002_neg (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_file (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_https (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_011_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_012_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_fail (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_mountpoints (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_test_race (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_006_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_008_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_014_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_multi_mount (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/zfs_program_json (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_program/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_promote/zfs_promote_004_pos (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_008_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_012_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_014_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_015_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_016_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_override (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_aliases (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-wR-encrypted-mix (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_corrective (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_compressed_corrective (run as root) [00:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_002_pos (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_014_neg (run as root) [00:25] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_001_pos (run as root) [00:59] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/zfs_rollback_004_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rollback/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_007_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_sparse (run as root) [00:14] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/reservation_001_neg (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/share_mount_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/snapdir_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/onoffs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_001_neg (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/ro_props_001_pos (run as root) [01:51] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_concurrent_shares (run as root) [01:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_005_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_007_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_009_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_012_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_005_neg (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_009_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/setup (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfeature_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_get_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_sysfs_live (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zpool_get_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zpool_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_006_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_all_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_nested (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unshare/setup (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_003_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_004_pos (run as root) [00:11] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool/zpool_002_pos (run as root) [00:05] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add-o_ashift (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_prop_ashift (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_nested_replacing_spare (run as root) [00:05] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/attach-o_ashift (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_clear/zpool_clear_001_pos (run as root) [00:15] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_009_neg (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_023_neg (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_024_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_encrypted (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_crypt_combos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos (run as root) [02:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_cliargs (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_errors (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_duplicates (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear_retained (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_002_pos (run as root) [00:38] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_003_neg (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_004_pos (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_005_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/cleanup (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg (run as root) [01:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3 (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced (run as root) [00:43] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed (run as root) [01:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:16] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_attach_detach_add_remove (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_fault_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_import_export (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_split (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_suspend_resume (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_unsupported_vdevs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_checksums (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_initialized (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_removed (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_valid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_offline/zpool_offline_001_pos (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/setup (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_002_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_003_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_004_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_005_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_006_neg (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_007_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace-o_ashift (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace_prop_ashift (run as root) [01:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_restart (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_004_pos (run as root) [00:02] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_encryption (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_resilver (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_wholedisk (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_005_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_features_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_001_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_002_pos (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_004_pos (run as root) [01:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_007_pos (run as root) [00:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_008_pos (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_discard (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_freeing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_flag (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_multiple (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove_cancel (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace_cancel (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_rebuild (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_resilver (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_basic (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/setup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_basic (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_nounmount (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_short_password (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [01:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [03:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [02:11] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_basic (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_concurrent_readers (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_stale_read (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/pool_state (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/setup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_002_pos (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_004_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_005_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_006_pos (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_007_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_008_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_009_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_001_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_002_pos (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_004_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_003_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/simd/simd_supported (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_001_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_002_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_003_pos (run as root) [01:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_004_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_005_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_006_pos (run as root) [04:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_007_pos (run as root) [01:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_011_neg (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_012_neg (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_014_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_015_neg (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_001 (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_002 (run as root) [00:21] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_014_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_017_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_018_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_015_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_016_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_stat_mode (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_integrity (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_config (run as root) [01:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_trim_integrity (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_integrity (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_config (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_l2arc (run as root) [00:36] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_projectquota_001_pos (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_002 (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_003 (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_004 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_007_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709 (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:05] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:11] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_002_pos (run as root) [00:36] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_rename_inuse (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_snapdev (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_trim (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_volmode (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_zil (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_fua (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/zvol_stress (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid (run as root) [02:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:33] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:22] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_noreplace (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_exchange (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_whiteout (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [00:57] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_008_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_013_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_007_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_008_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_012_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_013_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_019_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_020_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_021_pos (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_022_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_024_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_025_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_026_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_027_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_028_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_029_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_030_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_031_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_ratio (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_props (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_incremental (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstream_recompress (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_lz4_disabled (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_lz4_disabled (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_mixed_compression (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_stream_size_estimate (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_embedded_blocks (run as root) [00:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_resume (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-cpL_varied_recsize (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_incremental (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_files (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_encrypted_files (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_spill_block (run as root) [00:44] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_hole_birth (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_doall (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_spill_block (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_ashift (run as root) [01:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_large_blocks (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_dnode_size (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_files (run as root) [00:21] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
</pre></details>

## Functional Tests Ubuntu 22.04

Summary:<pre>

Tests with results other than PASS that are expected:
    FAIL casenorm/mixed_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_formd_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/mixed_none_lookup_ci (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_delete (https://github.com/openzfs/zfs/issues/7633)
    FAIL casenorm/sensitive_formd_lookup (https://github.com/openzfs/zfs/issues/7633)
    FAIL cli_root/zpool_import/import_rewind_device_replaced (Arbitrary pool rewind is not guaranteed)
    SKIP cli_root/zpool_import/zpool_import_missing_003_pos (https://github.com/openzfs/zfs/issues/6839)
    FAIL refreserv/refreserv_004_pos (Known issue)
    SKIP removal/removal_with_zdb (Known issue)
    SKIP rsend/rsend_008_pos (https://github.com/openzfs/zfs/issues/6066)
    FAIL vdev_zaps/vdev_zaps_007_pos (Known issue)

Tests with result of PASS that are unexpected:

Tests with results other than PASS that are unexpected:
    SKIP cli_root/zpool_expand/zpool_expand_001_pos (expected PASS)
    SKIP cli_root/zpool_expand/zpool_expand_003_neg (expected PASS)
    SKIP cli_root/zpool_expand/zpool_expand_005_pos (expected PASS)
    SKIP cli_root/zpool_reopen/setup (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_001_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_002_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_003_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_004_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_005_pos (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_006_neg (expected PASS)
    SKIP cli_root/zpool_reopen/zpool_reopen_007_pos (expected PASS)
    SKIP cli_root/zpool_split/zpool_split_wholedisk (expected PASS)
    SKIP fault/auto_offline_001_pos (expected PASS)
    SKIP fault/auto_online_001_pos (expected PASS)
    SKIP fault/auto_online_002_pos (expected PASS)
    SKIP fault/auto_replace_001_pos (expected PASS)
    SKIP fault/auto_spare_ashift (expected PASS)
    SKIP fault/auto_spare_shared (expected PASS)
    SKIP procfs/pool_state (expected PASS)
</pre>
<details><summary>Error Listing - with dmesg and dbgmsg</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup (run as root) [00:00] [FAIL]
16:09:03.71 ASSERTION: CS-UN FS: lookup succeeds if (case=same)
16:09:03.74 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:03.78 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.78 SUCCESS: create_file FïLëNÄmë
16:09:03.78 SUCCESS: lookup_file FïLëNÄmë
16:09:03.78 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:03.79 SUCCESS: lookup_file fïlënämë exited 1
16:09:03.79 SUCCESS: lookup_file FïLëNÄmë
16:09:03.79 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:03.79 SUCCESS: lookup_file fïlënämë exited 1
16:09:03.80 SUCCESS: create_file FÏLËNÄMË
16:09:03.80 SUCCESS: lookup_file FïLëNÄmë exited 1
16:09:03.80 SUCCESS: lookup_file FÏLËNÄMË
16:09:03.80 SUCCESS: lookup_file fïlënämë exited 1
16:09:03.81 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
16:09:03.81 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:03.81 =================================================================
16:09:03.81  Tailing last 200 lines of zfs_dbgmsg log
16:09:03.81 =================================================================
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 32, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 29184, unflushed_frees 24576, appended 128 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 33 create testpool/testfs (id 87)  
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 33, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 23040, unflushed_frees 23040, appended 96 bytes
16:09:03.82 1678637336   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 34, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 47616, appended 128 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 35 set testpool/testfs (id 87) mountpoint=/var/tmp/testdir
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 35, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 47104, appended 144 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 36, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 23040, appended 104 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 37 destroy testpool/testfs (id 87) (bptree, mintxg=1)
16:09:03.82 1678637336   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637336   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 37; err=0
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 37, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29184, unflushed_frees 25088, appended 136 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 38 create testpool/testfs (id 99)  
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 38, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 29696, unflushed_frees 43520, appended 112 bytes
16:09:03.82 1678637336   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 24064, unflushed_frees 28160, appended 96 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 40 set testpool/testfs (id 99) mountpoint=/var/tmp/testdir
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 40, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 47104, appended 160 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 41, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 29696, appended 128 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 42 destroy testpool/testfs (id 99) (bptree, mintxg=1)
16:09:03.82 1678637336   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637336   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 42; err=0
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 42, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 22528, unflushed_frees 18432, appended 112 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 43 create testpool/testfs (id 111)  
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 43, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 29696, unflushed_frees 44032, appended 120 bytes
16:09:03.82 1678637336   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 44, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 47616, appended 136 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 45 set testpool/testfs (id 111) mountpoint=/var/tmp/testdir
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 45, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 28160, appended 128 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 46, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48640, unflushed_frees 29696, appended 120 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 47 destroy testpool/testfs (id 111) (bptree, mintxg=1)
16:09:03.82 1678637336   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637336   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 47; err=0
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 47, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 30720, unflushed_frees 25088, appended 120 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 48 create testpool/testfs (id 192)  
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 48, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 25088, appended 104 bytes
16:09:03.82 1678637336   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formC testpool/testfs
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 49, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 48640, appended 136 bytes
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 50 set testpool/testfs (id 192) mountpoint=/var/tmp/testdir
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 50, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 49152, appended 152 bytes
16:09:03.82 1678637336   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637336   spa_history.c:297:spa_history_log_sync(): txg 51 create testpool/testfs/subfs (id 121)  
16:09:03.82 1678637336   metaslab.c:3926:metaslab_flush(): flushing: txg 51, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 25088, appended 104 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 52, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 45056, unflushed_frees 27648, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 53 destroy testpool/testfs/subfs (id 121) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 53; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 53, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 34816, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 54, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 25600, appended 112 bytes
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 55, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38400, unflushed_frees 46080, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 56 destroy testpool/testfs (id 192) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 56; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 56, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34304, unflushed_frees 46080, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 57 create testpool/testfs (id 207)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 57, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25600, unflushed_frees 30208, appended 112 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formD testpool/testfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 58, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 37888, unflushed_frees 47616, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 59 set testpool/testfs (id 207) mountpoint=/var/tmp/testdir
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 59, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 50688, appended 184 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 60 create testpool/testfs/subfs (id 259)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 60, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 25600, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 61, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46592, unflushed_frees 27648, appended 136 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 62 destroy testpool/testfs/subfs (id 259) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 62; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 62, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 53760, unflushed_frees 35840, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 63, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 27136, appended 120 bytes
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 64, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 47616, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 65 destroy testpool/testfs (id 207) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 65; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 65, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 34816, unflushed_frees 47616, appended 160 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 66 create testpool/testfs (id 223)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 66, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26624, unflushed_frees 31744, appended 88 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKC testpool/testfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 67, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39936, unflushed_frees 48128, appended 120 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 68 set testpool/testfs (id 223) mountpoint=/var/tmp/testdir
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 68, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 51200, appended 176 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 69 create testpool/testfs/subfs (id 267)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 69, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 26624, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 70, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 47104, unflushed_frees 29696, appended 136 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 71 destroy testpool/testfs/subfs (id 267) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 71; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 71, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 54272, unflushed_frees 37376, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 72, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28160, appended 136 bytes
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 73, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39936, unflushed_frees 48128, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 74 destroy testpool/testfs (id 223) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 74; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 74, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 35840, unflushed_frees 48128, appended 152 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 75 create testpool/testfs (id 237)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 75, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27648, unflushed_frees 32256, appended 88 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o normalization=formKD testpool/testfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 76, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40448, unflushed_frees 49152, appended 112 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 77 set testpool/testfs (id 237) mountpoint=/var/tmp/testdir
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 77, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 168 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 78 create testpool/testfs/subfs (id 277)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 78, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 27648, appended 112 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o utf8only=off testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 79, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 48128, unflushed_frees 30208, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 80 destroy testpool/testfs/subfs (id 277) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 80; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 80, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 55808, unflushed_frees 37888, appended 128 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy testpool/testfs/subfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 81, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29184, appended 128 bytes
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 82, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 49152, appended 160 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 83 destroy testpool/testfs (id 237) (bptree, mintxg=1)
16:09:03.82 1678637337   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637337   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 83; err=0
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 83, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 49664, appended 168 bytes
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 84 create testpool/testfs (id 289)  
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 84, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29184, unflushed_frees 33792, appended 96 bytes
16:09:03.82 1678637337   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637337   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 85, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 50688, appended 144 bytes
16:09:03.82 1678637337   spa_history.c:297:spa_history_log_sync(): txg 86 set testpool/testfs (id 289) mountpoint=/var/tmp/testdir
16:09:03.82 1678637337   metaslab.c:3926:metaslab_flush(): flushing: txg 86, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53248, appended 200 bytes
16:09:03.82 1678637339   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637339   metaslab.c:3926:metaslab_flush(): flushing: txg 87, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 29184, appended 104 bytes
16:09:03.82 1678637340   metaslab.c:3926:metaslab_flush(): flushing: txg 88, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 188928, unflushed_frees 37888, appended 128 bytes
16:09:03.82 1678637341   metaslab.c:3926:metaslab_flush(): flushing: txg 89, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338432, unflushed_frees 38400, appended 216 bytes
16:09:03.82 1678637342   metaslab.c:3926:metaslab_flush(): flushing: txg 90, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 25088, unflushed_frees 24064, appended 80 bytes
16:09:03.82 1678637342   metaslab.c:3926:metaslab_flush(): flushing: txg 91, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 485376, unflushed_frees 46592, appended 304 bytes
16:09:03.82 1678637342   metaslab.c:3926:metaslab_flush(): flushing: txg 92, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 338944, unflushed_frees 48128, appended 256 bytes
16:09:03.82 1678637342   spa_history.c:297:spa_history_log_sync(): txg 93 destroy testpool/testfs (id 289) (bptree, mintxg=1)
16:09:03.82 1678637342   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637342   dsl_scan.c:3493:dsl_process_async_destroys(): freed 131595 blocks in 48ms from free_bpobj/bptree on testpool in txg 93; err=0
16:09:03.82 1678637342   metaslab.c:3926:metaslab_flush(): flushing: txg 93, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 21504, unflushed_frees 20480, appended 80 bytes
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 94 create testpool/testfs (id 303)  
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 94, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 30208, unflushed_frees 631808, appended 304 bytes
16:09:03.82 1678637343   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 95, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43008, unflushed_frees 633344, appended 344 bytes
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 96 set testpool/testfs (id 303) mountpoint=/var/tmp/testdir
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 96, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 35840, appended 160 bytes
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 97, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 53760, unflushed_frees 37376, appended 184 bytes
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 98, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 39424, appended 176 bytes
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 99 destroy testpool/testfs (id 303) (bptree, mintxg=1)
16:09:03.82 1678637343   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637343   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 99; err=0
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 99, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 25088, appended 96 bytes
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 100 create testpool/testfs (id 316)  
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 100, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 53760, appended 144 bytes
16:09:03.82 1678637343   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=none testpool/testfs
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 101, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 47616, appended 144 bytes
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 102 set testpool/testfs (id 316) mountpoint=/var/tmp/testdir
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 102, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 35840, appended 144 bytes
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 103, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 55808, unflushed_frees 38400, appended 152 bytes
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 104, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 40448, appended 144 bytes
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 105 destroy testpool/testfs (id 316) (bptree, mintxg=1)
16:09:03.82 1678637343   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:03.82 1678637343   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 105; err=0
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 105, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 26624, appended 104 bytes
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 106 create testpool/testfs (id 255)  
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 106, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 55808, appended 184 bytes
16:09:03.82 1678637343   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:03.82 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 107, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 49664, appended 168 bytes
16:09:03.82 1678637343   spa_history.c:297:spa_history_log_sync(): txg 108 set testpool/testfs (id 255) mountpoint=/var/tmp/testdir
16:09:03.82 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 108, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 152 bytes
16:09:03.83 =================================================================
16:09:03.83  End of zfs_dbgmsg log
16:09:03.83 =================================================================
16:09:03.83 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:03.83 =================================================================
16:09:03.83  Tailing last 200 lines of dmesg log
16:09:03.83 =================================================================
16:09:03.84 [  414.937559] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_003_pos
16:09:03.84 [  415.793198] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_004_pos
16:09:03.84 [  416.327212] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_005_pos
16:09:03.84 [  417.031809] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_006_pos
16:09:03.84 [  417.305069] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_007_pos
16:09:03.84 [  427.613637] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_008_pos
16:09:03.84 [  428.163709] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_009_pos
16:09:03.84 [  435.917457] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_010_pos
16:09:03.84 [  436.533190] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_011_neg
16:09:03.84 [  436.784978] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos
16:09:03.84 [  567.576420] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_013_pos
16:09:03.84 [  584.203613] ZTS run /usr/share/zfs/zfs-tests/tests/functional/alloc_class/cleanup
16:09:03.84 [  584.277782] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/setup
16:09:03.84 [  584.526365] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/file_append
16:09:03.84 [  584.619060] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/threadsappend_001_pos
16:09:03.84 [  584.655522] ZTS run /usr/share/zfs/zfs-tests/tests/functional/append/cleanup
16:09:03.84 [  584.871286] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/setup
16:09:03.84 [  585.126862] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_001_pos
16:09:03.84 [  585.762671] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_002_pos
16:09:03.84 [  586.058058] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/dbufstats_003_pos
16:09:03.84 [  586.486548] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/arcstats_runtime_tuning
16:09:03.84 [  586.583911] ZTS run /usr/share/zfs/zfs-tests/tests/functional/arc/cleanup
16:09:03.84 [  586.803792] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
16:09:03.84 [  587.027440] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_001_pos
16:09:03.84 [  597.509714] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_002_neg
16:09:03.84 [  603.934794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_off
16:09:03.84 [  610.464649] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_atime_on
16:09:03.84 [  621.054693] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
16:09:03.84 [  621.267585] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/setup
16:09:03.84 [  621.507588] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos
16:09:03.84 [  631.984973] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on
16:09:03.84 [  642.578025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup
16:09:03.84 [  642.795486] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/setup
16:09:03.84 [  642.819873] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_001_pos
16:09:03.84 [  644.362657] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_002_neg
16:09:03.84 [  646.440971] debugfs: Directory 'zd0' with parent 'block' already present!
16:09:03.84 [  646.962286] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_003_pos
16:09:03.84 [  648.641668] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_004_neg
16:09:03.84 [  649.206031] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_005_neg
16:09:03.84 [  654.572045] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_006_pos
16:09:03.84 [  660.113725] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_007_pos
16:09:03.84 [  660.446829] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/bootfs_008_pos
16:09:03.84 [  662.416022] ZTS run /usr/share/zfs/zfs-tests/tests/functional/bootfs/cleanup
16:09:03.84 [  662.438239] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_positive
16:09:03.84 [  843.204696] ZTS run /usr/share/zfs/zfs-tests/tests/functional/btree/btree_negative
16:09:03.84 [  845.717505] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/setup
16:09:03.84 [  850.247225] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_001_pos
16:09:03.84 [  862.674855] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_002_pos
16:09:03.84 [  872.439416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_003_pos
16:09:03.84 [  882.691065] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_004_neg
16:09:03.84 [  884.254599] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_005_neg
16:09:03.84 [  885.890801] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_006_pos
16:09:03.84 [  907.092996] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_007_neg
16:09:03.84 [  907.741570] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_008_neg
16:09:03.84 [  911.923119] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_009_pos
16:09:03.84 [  930.571424] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_010_pos
16:09:03.84 [  931.282311] loop3: detected capacity change from 0 to 524288
16:09:03.84 [  931.484835] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos
16:09:03.84 [  941.476299] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos
16:09:03.84 [  942.032350] NOTICE: l2arc_write_max or l2arc_write_boost plus the overhead of log blocks (persistent L2ARC, 4337303552 bytes) exceeds the size of the cache device (guid 648152728343572922), resetting them to the default (8388608)
16:09:03.84 [  988.424084] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup
16:09:03.84 [  988.823007] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup
16:09:03.84 [  988.887858] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos
16:09:03.84 [  990.807456] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos
16:09:03.84 [  992.753349] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos
16:09:03.84 [  994.765660] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos
16:09:03.84 [  996.344001] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup
16:09:03.84 [  996.406102] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup
16:09:03.84 [  996.584258] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values
16:09:03.84 [  997.072772] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values
16:09:03.84 [  999.031513] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_create_failure
16:09:03.84 [ 1004.134541] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_lookup
16:09:03.84 [ 1004.536504] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_none_delete
16:09:03.84 [ 1004.862460] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_lookup
16:09:03.84 =================================================================
16:09:03.84  End of dmesg log
16:09:03.84 =================================================================
16:09:03.84 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:03.84 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:03.92 SUCCESS: zfs destroy -f testpool/testfs
16:09:03.92 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete (run as root) [00:00] [FAIL]
16:09:03.95 ASSERTION: CS-UN FS: delete succeeds if (case=same)
16:09:03.99 SUCCESS: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:04.02 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:04.03 SUCCESS: create_file FïLëNÄmë
16:09:04.03 SUCCESS: delete_file FïLëNÄmë
16:09:04.03 SUCCESS: lookup_any exited 1
16:09:04.04 SUCCESS: create_file FïLëNÄmë
16:09:04.04 SUCCESS: delete_file FÏLËNÄMË exited 1
16:09:04.04 SUCCESS: create_file FïLëNÄmë
16:09:04.05 SUCCESS: delete_file fïlënämë exited 1
16:09:04.05 SUCCESS: create_file FïLëNÄmë
16:09:04.05 ERROR: delete_file FïLëNÄmë exited 1
16:09:04.05 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:04.05 =================================================================
16:09:04.05  Tailing last 200 lines of zfs_dbgmsg log
16:09:04.05 =================================================================
16:09:04.06 timestamp    message 
16:09:04.06 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:04.06 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 109, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 39424, appended 192 bytes
16:09:04.06 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 110, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 41984, appended 200 bytes
16:09:04.06 1678637343   spa_history.c:297:spa_history_log_sync(): txg 111 destroy testpool/testfs (id 255) (bptree, mintxg=1)
16:09:04.06 1678637343   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:04.06 1678637343   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 111; err=0
16:09:04.06 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 111, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 104 bytes
16:09:04.06 1678637343   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:04.06 1678637343   spa_history.c:297:spa_history_log_sync(): txg 112 create testpool/testfs (id 397)  
16:09:04.06 1678637343   metaslab.c:3926:metaslab_flush(): flushing: txg 112, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 38912, unflushed_frees 56320, appended 144 bytes
16:09:04.06 1678637344   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:04.06 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=sensitive -o normalization=formD testpool/testfs
16:09:04.06 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 113, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 49664, appended 144 bytes
16:09:04.06 1678637344   spa_history.c:297:spa_history_log_sync(): txg 114 set testpool/testfs (id 397) mountpoint=/var/tmp/testdir
16:09:04.06 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 114, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 37376, appended 152 bytes
16:09:04.07 =================================================================
16:09:04.07  End of zfs_dbgmsg log
16:09:04.07 =================================================================
16:09:04.07 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:04.07 =================================================================
16:09:04.07  Tailing last 200 lines of dmesg log
16:09:04.07 =================================================================
16:09:04.08 [ 1005.106023] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/sensitive_formd_delete
16:09:04.08 =================================================================
16:09:04.08  End of dmesg log
16:09:04.08 =================================================================
16:09:04.08 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:04.08 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:04.16 SUCCESS: zfs destroy -f testpool/testfs
16:09:04.16 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci (run as root) [00:00] [FAIL]
16:09:06.13 ASSERTION: CM-not-UN FS: CI lookup succeeds only if (norm=same)
16:09:06.17 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:06.21 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.21 SUCCESS: create_file FïLëNÄmë
16:09:06.21 SUCCESS: lookup_file_ci FïLëNÄmë
16:09:06.21 ERROR: lookup_file_ci FÏLËNÄMË exited 1
16:09:06.21 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:06.22 =================================================================
16:09:06.22  Tailing last 200 lines of zfs_dbgmsg log
16:09:06.22 =================================================================
16:09:06.22 timestamp    message 
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 115, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 56320, unflushed_frees 38912, appended 144 bytes
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 116, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 40960, appended 152 bytes
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 117 destroy testpool/testfs (id 397) (bptree, mintxg=1)
16:09:06.22 1678637344   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637344   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 117; err=0
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 117, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 27136, appended 96 bytes
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 118 create testpool/testfs (id 411)  
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 118, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 39936, unflushed_frees 56320, appended 184 bytes
16:09:06.22 1678637344   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 119, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46080, unflushed_frees 49664, appended 152 bytes
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 120 set testpool/testfs (id 411) mountpoint=/var/tmp/testdir
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 120, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 37376, appended 136 bytes
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 121, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 57856, unflushed_frees 39936, appended 192 bytes
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 122, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 42496, appended 176 bytes
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 123 destroy testpool/testfs (id 411) (bptree, mintxg=1)
16:09:06.22 1678637344   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637344   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 123; err=0
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 123, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 28672, appended 88 bytes
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 124 create testpool/testfs (id 423)  
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 124, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 40960, unflushed_frees 57856, appended 152 bytes
16:09:06.22 1678637344   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=none testpool/testfs
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 125, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 52736, appended 144 bytes
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 126 set testpool/testfs (id 423) mountpoint=/var/tmp/testdir
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 126, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 40448, appended 144 bytes
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 127, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58368, unflushed_frees 40960, appended 144 bytes
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 128, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 43008, appended 120 bytes
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 129 destroy testpool/testfs (id 423) (bptree, mintxg=1)
16:09:06.22 1678637344   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637344   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 129; err=0
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 129, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 28672, appended 80 bytes
16:09:06.22 1678637344   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637344   spa_history.c:297:spa_history_log_sync(): txg 130 create testpool/testfs (id 435)  
16:09:06.22 1678637344   metaslab.c:3926:metaslab_flush(): flushing: txg 130, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41984, unflushed_frees 58368, appended 136 bytes
16:09:06.22 1678637345   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 51712, appended 136 bytes
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 132 set testpool/testfs (id 435) mountpoint=/var/tmp/testdir
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 132, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 39936, appended 144 bytes
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 133, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 58880, unflushed_frees 41984, appended 136 bytes
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 134, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 43520, appended 128 bytes
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 135 destroy testpool/testfs (id 435) (bptree, mintxg=1)
16:09:06.22 1678637345   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637345   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 135; err=0
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 135, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34304, unflushed_frees 29696, appended 88 bytes
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 136 create testpool/testfs (id 447)  
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 136, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 41472, unflushed_frees 58880, appended 152 bytes
16:09:06.22 1678637345   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=insensitive -o normalization=formD testpool/testfs
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 137, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 52224, appended 136 bytes
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 138 set testpool/testfs (id 447) mountpoint=/var/tmp/testdir
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 138, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 39936, appended 136 bytes
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 139, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 41472, appended 160 bytes
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 140, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 44544, appended 144 bytes
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 141 destroy testpool/testfs (id 447) (bptree, mintxg=1)
16:09:06.22 1678637345   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637345   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 141; err=0
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 141, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 30208, appended 80 bytes
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 142 create testpool/testfs (id 459)  
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 142, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43008, unflushed_frees 59904, appended 160 bytes
16:09:06.22 1678637345   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637345   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 143, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 54272, appended 144 bytes
16:09:06.22 1678637345   spa_history.c:297:spa_history_log_sync(): txg 144 set testpool/testfs (id 459) mountpoint=/var/tmp/testdir
16:09:06.22 1678637345   metaslab.c:3926:metaslab_flush(): flushing: txg 144, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 41984, appended 136 bytes
16:09:06.22 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 145, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 59904, unflushed_frees 43008, appended 152 bytes
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 146, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 45056, appended 128 bytes
16:09:06.22 1678637346   spa_history.c:297:spa_history_log_sync(): txg 147 destroy testpool/testfs (id 459) (bptree, mintxg=1)
16:09:06.22 1678637346   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.22 1678637346   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 147; err=0
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 147, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 30208, appended 96 bytes
16:09:06.22 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.22 1678637346   spa_history.c:297:spa_history_log_sync(): txg 148 create testpool/testfs (id 473)  
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 148, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 59904, appended 152 bytes
16:09:06.22 1678637346   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.22 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 149, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49152, unflushed_frees 53248, appended 136 bytes
16:09:06.22 1678637346   spa_history.c:297:spa_history_log_sync(): txg 150 set testpool/testfs (id 473) mountpoint=/var/tmp/testdir
16:09:06.22 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 150, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 41472, appended 144 bytes
16:09:06.23 =================================================================
16:09:06.23  End of zfs_dbgmsg log
16:09:06.23 =================================================================
16:09:06.23 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:06.23 =================================================================
16:09:06.23  Tailing last 200 lines of dmesg log
16:09:06.23 =================================================================
16:09:06.24 [ 1005.344125] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_lookup
16:09:06.24 [ 1005.637153] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_none_delete
16:09:06.24 [ 1006.104406] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_lookup
16:09:06.24 [ 1006.405748] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/insensitive_formd_delete
16:09:06.24 [ 1006.897094] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup
16:09:06.24 [ 1007.286196] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_lookup_ci
16:09:06.24 =================================================================
16:09:06.24  End of dmesg log
16:09:06.24 =================================================================
16:09:06.24 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:06.24 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:06.32 SUCCESS: zfs destroy -f testpool/testfs
16:09:06.32 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup (run as root) [00:00] [FAIL]
16:09:06.68 ASSERTION: CM-UN FS: lookup succeeds if (case=same)
16:09:06.72 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:06.75 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.75 SUCCESS: create_file FïLëNÄmë
16:09:06.76 SUCCESS: lookup_file FïLëNÄmë
16:09:06.76 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:06.76 SUCCESS: lookup_file fïlënämë exited 1
16:09:06.76 SUCCESS: lookup_file FïLëNÄmë
16:09:06.77 SUCCESS: lookup_file FÏLËNÄMË exited 1
16:09:06.77 SUCCESS: lookup_file fïlënämë exited 1
16:09:06.77 SUCCESS: create_file FÏLËNÄMË
16:09:06.77 SUCCESS: lookup_file FïLëNÄmë exited 1
16:09:06.78 SUCCESS: lookup_file FÏLËNÄMË
16:09:06.78 SUCCESS: lookup_file fïlënämë exited 1
16:09:06.78 ERROR: lookup_file FïLëNÄmë unexpectedly exited 0
16:09:06.78 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:06.78 =================================================================
16:09:06.78  Tailing last 200 lines of zfs_dbgmsg log
16:09:06.78 =================================================================
16:09:06.79 timestamp    message 
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 151, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 60416, unflushed_frees 43008, appended 160 bytes
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 152, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 45056, appended 152 bytes
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 153 destroy testpool/testfs (id 473) (bptree, mintxg=1)
16:09:06.79 1678637346   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.79 1678637346   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 153; err=0
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 153, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 31232, appended 104 bytes
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 154 create testpool/testfs (id 486)  
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 154, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44032, unflushed_frees 60416, appended 144 bytes
16:09:06.79 1678637346   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=none testpool/testfs
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 155, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 54784, appended 128 bytes
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 156 set testpool/testfs (id 486) mountpoint=/var/tmp/testdir
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 156, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 43520, appended 152 bytes
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 157, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 61440, unflushed_frees 44032, appended 160 bytes
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 158, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 45568, appended 144 bytes
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 159 destroy testpool/testfs (id 486) (bptree, mintxg=1)
16:09:06.79 1678637346   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:06.79 1678637346   dsl_scan.c:3493:dsl_process_async_destroys(): freed 18 blocks in 0ms from free_bpobj/bptree on testpool in txg 159; err=0
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 159, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 32256, appended 88 bytes
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 160 create testpool/testfs (id 497)  
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 160, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 61440, appended 168 bytes
16:09:06.79 1678637346   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:06.79 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 161, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 50688, unflushed_frees 54784, appended 152 bytes
16:09:06.79 1678637346   spa_history.c:297:spa_history_log_sync(): txg 162 set testpool/testfs (id 497) mountpoint=/var/tmp/testdir
16:09:06.79 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 162, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 41984, appended 128 bytes
16:09:06.80 =================================================================
16:09:06.80  End of zfs_dbgmsg log
16:09:06.80 =================================================================
16:09:06.80 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:06.80 =================================================================
16:09:06.80  Tailing last 200 lines of dmesg log
16:09:06.80 =================================================================
16:09:06.81 [ 1007.503237] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_none_delete
16:09:06.81 [ 1007.835924] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup
16:09:06.81 =================================================================
16:09:06.81  End of dmesg log
16:09:06.81 =================================================================
16:09:06.81 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:06.81 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:06.89 SUCCESS: zfs destroy -f testpool/testfs
16:09:06.90 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci (run as root) [00:00] [FAIL]
16:09:06.92 ASSERTION: CM-UN FS: CI lookup succeeds using any name form
16:09:06.96 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:07.00 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:07.00 SUCCESS: create_file FïLëNÄmë
16:09:07.00 SUCCESS: lookup_file_ci FïLëNÄmë
16:09:07.00 ERROR: lookup_file_ci FÏLËNÄMË exited 1
16:09:07.00 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:07.01 =================================================================
16:09:07.01  Tailing last 200 lines of zfs_dbgmsg log
16:09:07.01 =================================================================
16:09:07.01 timestamp    message 
16:09:07.01 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 163, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 62464, unflushed_frees 44544, appended 152 bytes
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 164, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 46592, appended 152 bytes
16:09:07.01 1678637346   spa_history.c:297:spa_history_log_sync(): txg 165 destroy testpool/testfs (id 497) (bptree, mintxg=1)
16:09:07.01 1678637346   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:07.01 1678637346   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 165; err=0
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 165, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 33280, appended 88 bytes
16:09:07.01 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:07.01 1678637346   spa_history.c:297:spa_history_log_sync(): txg 166 create testpool/testfs (id 510)  
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 166, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 44544, unflushed_frees 62464, appended 176 bytes
16:09:07.01 1678637346   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:07.01 1678637346   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 167, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 55808, appended 176 bytes
16:09:07.01 1678637346   spa_history.c:297:spa_history_log_sync(): txg 168 set testpool/testfs (id 510) mountpoint=/var/tmp/testdir
16:09:07.01 1678637346   metaslab.c:3926:metaslab_flush(): flushing: txg 168, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 43008, appended 152 bytes
16:09:07.02 =================================================================
16:09:07.02  End of zfs_dbgmsg log
16:09:07.02 =================================================================
16:09:07.02 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:07.02 =================================================================
16:09:07.02  Tailing last 200 lines of dmesg log
16:09:07.02 =================================================================
16:09:07.03 [ 1008.074756] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_lookup_ci
16:09:07.03 =================================================================
16:09:07.03  End of dmesg log
16:09:07.03 =================================================================
16:09:07.03 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:07.03 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:07.11 SUCCESS: zfs destroy -f testpool/testfs
16:09:07.12 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete (run as root) [00:00] [FAIL]
16:09:07.14 ASSERTION: CM-UN FS: delete succeeds if (case=same)
16:09:07.18 SUCCESS: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:07.21 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:07.21 SUCCESS: create_file FïLëNÄmë
16:09:07.22 SUCCESS: delete_file FïLëNÄmë
16:09:07.22 SUCCESS: lookup_any exited 1
16:09:07.22 SUCCESS: create_file FïLëNÄmë
16:09:07.23 SUCCESS: delete_file FÏLËNÄMË exited 1
16:09:07.23 SUCCESS: create_file FïLëNÄmë
16:09:07.23 SUCCESS: delete_file fïlënämë exited 1
16:09:07.24 SUCCESS: create_file FïLëNÄmë
16:09:07.24 ERROR: delete_file FïLëNÄmë exited 1
16:09:07.24 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:09:07.24 =================================================================
16:09:07.24  Tailing last 200 lines of zfs_dbgmsg log
16:09:07.24 =================================================================
16:09:07.25 timestamp    message 
16:09:07.25 1678637347   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 169, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 64000, unflushed_frees 45056, appended 200 bytes
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 170, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 53760, unflushed_frees 48128, appended 184 bytes
16:09:07.25 1678637347   spa_history.c:297:spa_history_log_sync(): txg 171 destroy testpool/testfs (id 510) (bptree, mintxg=1)
16:09:07.25 1678637347   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:09:07.25 1678637347   dsl_scan.c:3493:dsl_process_async_destroys(): freed 19 blocks in 0ms from free_bpobj/bptree on testpool in txg 171; err=0
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 171, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 33792, appended 96 bytes
16:09:07.25 1678637347   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -f testpool/testfs
16:09:07.25 1678637347   spa_history.c:297:spa_history_log_sync(): txg 172 create testpool/testfs (id 522)  
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 172, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 46080, unflushed_frees 64000, appended 200 bytes
16:09:07.25 1678637347   spa_history.c:329:spa_history_log_sync(): ioctl create
16:09:07.25 1678637347   spa_history.c:293:spa_history_log_sync(): command: zfs create -o casesensitivity=mixed -o normalization=formD testpool/testfs
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 173, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 51712, unflushed_frees 57344, appended 168 bytes
16:09:07.25 1678637347   spa_history.c:297:spa_history_log_sync(): txg 174 set testpool/testfs (id 522) mountpoint=/var/tmp/testdir
16:09:07.25 1678637347   metaslab.c:3926:metaslab_flush(): flushing: txg 174, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 45056, appended 152 bytes
16:09:07.26 =================================================================
16:09:07.26  End of zfs_dbgmsg log
16:09:07.26 =================================================================
16:09:07.26 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:09:07.26 =================================================================
16:09:07.26  Tailing last 200 lines of dmesg log
16:09:07.26 =================================================================
16:09:07.27 [ 1008.297097] ZTS run /usr/share/zfs/zfs-tests/tests/functional/casenorm/mixed_formd_delete
16:09:07.27 =================================================================
16:09:07.27  End of dmesg log
16:09:07.27 =================================================================
16:09:07.27 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:09:07.27 NOTE: Performing local cleanup via log_onexit (cleanup)
16:09:07.35 SUCCESS: zfs destroy -f testpool/testfs
16:09:07.35 SUCCESS: rm -rf /var/tmp/testdir
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:16] [FAIL]
16:59:20.39 SUCCESS: set_tunable32 TXG_HISTORY 100
16:59:20.40 SUCCESS: mkdir -p /var/tmp/bakdev_import-test
16:59:20.40 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk0
16:59:20.40 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk1
16:59:20.40 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk2
16:59:20.41 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk3
16:59:20.41 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk4
16:59:20.41 SUCCESS: truncate -s 1073741824 /var/tmp/dev_import-test/disk5
16:59:20.41 NOTE: test_replace_vdev: pool '/var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1', replace /var/tmp/dev_import-test/disk1 by /var/tmp/dev_import-test/disk2.
16:59:20.47 SUCCESS: zpool create testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
16:59:20.51 SUCCESS: zfs create testpool1/ds1
16:59:20.60 SUCCESS: zpool sync testpool1
16:59:20.64 SUCCESS: zfs create testpool1/ds2
16:59:20.73 SUCCESS: zpool sync testpool1
16:59:20.78 SUCCESS: zfs create testpool1/ds3
16:59:20.86 SUCCESS: zpool sync testpool1
16:59:20.87 SUCCESS: generate_data testpool1 /var/tmp/md5sums.625588
16:59:21.76 SUCCESS: write_some_data testpool1 15
16:59:21.80 SUCCESS: zpool sync testpool1
16:59:21.83 SUCCESS: zpool sync testpool1
16:59:21.87 SUCCESS: zpool sync testpool1
16:59:21.90 SUCCESS: zpool sync testpool1
16:59:21.93 SUCCESS: zpool sync testpool1
16:59:21.96 SUCCESS: zpool sync testpool1
16:59:21.99 SUCCESS: zpool sync testpool1
16:59:22.02 SUCCESS: zpool sync testpool1
16:59:22.05 SUCCESS: zpool sync testpool1
16:59:22.08 SUCCESS: zpool sync testpool1
16:59:22.12 SUCCESS: zpool sync testpool1
16:59:22.12 SUCCESS: sync_some_data_a_few_times testpool1
16:59:25.72 SUCCESS: zfs snapshot -r testpool1@snap1
16:59:25.80 SUCCESS: overwrite_data testpool1 
16:59:25.91 SUCCESS: zpool export testpool1
16:59:26.09 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
16:59:26.09 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 1
16:59:26.14 SUCCESS: zpool replace testpool1 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk2
16:59:26.16 SUCCESS: pool_is_replacing testpool1
16:59:32.31 SUCCESS: zpool export testpool1
16:59:32.31 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
16:59:32.53 SUCCESS: zpool import -d /var/tmp/dev_import-test -o readonly=on -T 53 testpool1
16:59:32.57 SUCCESS: check_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1
16:59:32.65 SUCCESS: verify_data_md5sums /var/tmp/md5sums.625588
16:59:32.69 SUCCESS: zpool export testpool1
16:59:33.33 SUCCESS: zpool import -d /var/tmp/dev_import-test testpool1
16:59:33.42 SUCCESS: overwrite_data testpool1 
16:59:36.53 SUCCESS: wait_for_pool_config testpool1 /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk2
16:59:36.60 SUCCESS: zpool export testpool1
16:59:36.60 SUCCESS: mv /var/tmp/dev_import-test/disk2 /var/tmp/bakdev_import-test/
16:59:36.96 cannot import 'testpool1': one or more devices is currently unavailable
16:59:36.96 ERROR: zpool import -d /var/tmp/dev_import-test -T 53 testpool1 exited 1
16:59:36.96 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:59:36.96 =================================================================
16:59:36.96  Tailing last 200 lines of zfs_dbgmsg log
16:59:36.96 =================================================================
16:59:36.98 1678640376   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool1, vdev_id 1, ms_id 9, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
16:59:36.98 1678640376   metaslab.c:3926:metaslab_flush(): flushing: txg 131, spa testpool1, vdev_id 1, ms_id 11, unflushed_allocs 0, unflushed_frees 1024, appended 16 bytes
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config trusted): UNLOADING
16:59:36.98 1678640376   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool1' gethrtime 4080403817200
16:59:36.98 1678640376   spa.c:6319:spa_tryimport(): spa_tryimport: importing testpool1, max_txg=53
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa $import. txg 53
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 53)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load($import, config untrusted): using uberblock with txg=53
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load($import, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load($import, config untrusted): UNLOADING
16:59:36.98 1678640376   spa.c:6176:spa_import(): spa_import: importing testpool1, max_txg=53 (RECOVERY MODE)
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config trusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 53
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 53)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=53
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 52
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 50
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 50)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=50
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 49
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 47
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 47)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=47
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 46
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 44
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 44)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=44
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 43
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 41
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 41)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=41
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 40
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 38
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 38)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=38
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 37
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 35
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 35)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=35
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 34
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 32
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 32)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=32
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 31
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 29
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 29)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=29
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 28
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 26
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 26)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=26
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 25
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 23
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 23)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=23
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 22
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 22
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 22)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=22
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 21
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 21
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 21)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=21
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 20
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 20
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 20)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=20
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 19
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 17
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 17)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=17
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 16
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 16
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 16)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=16
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 15
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 13
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 13)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=13
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 12
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 12
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 12)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=12
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=52]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 11
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 9
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 9)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=9
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 8
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 8
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 8)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=8
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 7
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 6
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 6)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=6
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: couldn't get 'config' value in MOS directory [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 5
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 5
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 5)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=5
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 4
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': best uberblock found for spa testpool1. txg 4
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': label discarded as txg is too large (131 > 4)
16:59:36.98 1678640376   vdev.c:161:vdev_dbgmsg(): file vdev '/var/tmp/dev_import-test/disk0': failed to read label config. Trying again without txg restrictions.
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): using uberblock with txg=4
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: unable to open rootbp in dsl_pool_init [error=5]
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): spa_load_retry: rewind, max txg: 3
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): LOADING
16:59:36.98 1678640376   spa_misc.c:403:spa_load_failed(): spa_load(testpool1, config untrusted): FAILED: no valid uberblock found
16:59:36.98 1678640376   spa_misc.c:417:spa_load_note(): spa_load(testpool1, config untrusted): UNLOADING
16:59:36.99 =================================================================
16:59:36.99  End of zfs_dbgmsg log
16:59:36.99 =================================================================
16:59:36.99 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:59:36.99 =================================================================
16:59:36.99  Tailing last 200 lines of dmesg log
16:59:36.99 =================================================================
16:59:37.00 [ 3435.167898] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_003_neg
16:59:37.00 [ 3435.319720] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/zpool_export_004_pos
16:59:37.00 [ 3436.889602] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_export/cleanup
16:59:37.00 [ 3436.960136] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/setup
16:59:37.00 [ 3437.250797] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_001_pos
16:59:37.00 [ 3437.301283] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_002_pos
16:59:37.00 [ 3437.553727] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_003_pos
16:59:37.00 [ 3439.141022] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_004_neg
16:59:37.00 [ 3439.199520] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/zpool_get_005_pos
16:59:37.00 [ 3439.421891] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_get/cleanup
16:59:37.00 [ 3439.710238] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/setup
16:59:37.00 [ 3440.174015] debugfs: Directory 'zd0' with parent 'block' already present!
16:59:37.00 [ 3440.602316] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_001_neg
16:59:37.00 [ 3440.961552] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/zpool_history_002_pos
16:59:37.00 [ 3441.154819] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_history/cleanup
16:59:37.00 [ 3441.395597] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/setup
16:59:37.00 [ 3441.721499] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos
16:59:37.00 [ 3451.647943] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos
16:59:37.00 [ 3462.342861] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos
16:59:37.00 [ 3463.069963] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos
16:59:37.00 [ 3472.895602] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos
16:59:37.00 [ 3485.127215] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos
16:59:37.00 [ 3497.124236] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos
16:59:37.00 [ 3510.926593] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos
16:59:37.00 [ 3525.957449] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg
16:59:37.00 [ 3533.301074] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos
16:59:37.00 [ 3538.825884] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg
16:59:37.00 [ 3546.454238] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos
16:59:37.00 [ 3579.895706] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg
16:59:37.00 [ 3649.118938] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos
16:59:37.00 [ 3652.872073] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos
16:59:37.00 [ 3658.095877] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos
16:59:37.00 [ 3667.011189] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos
16:59:37.00 [ 3682.086483] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos
16:59:37.00 [ 3698.587798] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg
16:59:37.00 [ 3716.081813] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos
16:59:37.00 [ 3739.402452] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos
16:59:37.00 [ 3788.390984] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos
16:59:37.00 [ 3852.707010] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos
16:59:37.00 [ 3852.744942] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos
16:59:37.00 [ 3863.164283] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos
16:59:37.00 [ 3866.940389] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted
16:59:37.00 [ 3868.930912] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load
16:59:37.00 [ 3873.211992] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3
16:59:37.00 [ 3876.942515] debugfs: Directory 'zd0' with parent 'block' already present!
16:59:37.00 [ 3878.537799] debugfs: Directory 'zd16' with parent 'block' already present!
16:59:37.00 [ 3879.047416] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4
16:59:37.00 [ 3885.356054] debugfs: Directory 'zd0' with parent 'block' already present!
16:59:37.00 [ 3887.929510] debugfs: Directory 'zd16' with parent 'block' already present!
16:59:37.00 [ 3889.242794] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added
16:59:37.00 [ 3893.649630] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed
16:59:37.00 [ 3911.230742] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced
16:59:37.00 [ 3953.806908] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached
16:59:37.00 [ 3955.477386] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached
16:59:37.00 [ 3961.194832] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed
16:59:37.00 [ 3965.534188] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device
16:59:37.00 [ 3967.418046] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing
16:59:37.00 [ 3976.586887] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed
16:59:37.00 [ 3979.702376] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed
16:59:37.00 [ 4064.740033] ZTS run /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced
16:59:37.00 =================================================================
16:59:37.00  End of dmesg log
16:59:37.00 =================================================================
16:59:37.00 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:59:37.00 NOTE: Performing local cleanup via log_onexit (custom_cleanup)
16:59:37.00 SUCCESS: set_zfs_txg_timeout 5
16:59:37.02 SUCCESS: rm -rf /var/tmp/bakdev_import-test
16:59:37.02 SUCCESS: set_tunable32 SCAN_SUSPEND_PROGRESS 0
16:59:37.04 SUCCESS: eval zinject -c all > /dev/null
16:59:37.06 NOTE: Pool does not exist. (testpool1)
16:59:37.06 SUCCESS: rm -f /var/tmp/cachefile.625588 /var/tmp/cachefile.625588.bkp /var/tmp/cachefile.625588.bkp2 /var/tmp/md5sums.625588 /var/tmp/md5sums.625588.2
16:59:37.10 SUCCESS: rm -rf /var/tmp/dev_import-test/disk0 /var/tmp/dev_import-test/disk1 /var/tmp/dev_import-test/disk3 /var/tmp/dev_import-test/disk4 /var/tmp/dev_import-test/disk5
16:59:37.10 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk0
16:59:37.11 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk1
16:59:37.11 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk2
16:59:37.11 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk3
16:59:37.12 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk4
16:59:37.12 SUCCESS: truncate -s 268435456 /var/tmp/dev_import-test/disk5
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:12] [FAIL]
16:38:32.31 SUCCESS: zpool create -f testpool mirror loop0 loop1
16:38:32.31 ASSERTION: Per-vdev ZAPs persist correctly on the original pool after split.
16:38:35.91 SUCCESS: eval zdb -PC testpool > /var/tmp/testdir/vz007
16:38:35.91 SUCCESS: grep -q com.delphix:has_per_vdev_zaps /var/tmp/testdir/vz007
16:38:44.71 SUCCESS: zpool split testpool testpool2 loop1
16:38:44.88 ERROR: eval zdb -PC testpool > /var/tmp/testdir/vz007 exited 2
16:38:44.88 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:38:44.88 =================================================================
16:38:44.88  Tailing last 200 lines of zfs_dbgmsg log
16:38:44.88 =================================================================
16:38:44.89 1678639097   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:38:44.89 1678639097   spa.c:8440:spa_async_request(): spa=$import async request task=2048
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): LOADED
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load($import, config trusted): UNLOADING
16:38:44.89 1678639097   spa.c:6174:spa_import(): spa_import: importing testpool
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): LOADING
16:38:44.89 1678639097   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop0': best uberblock found for spa testpool. txg 23
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load(testpool, config untrusted): using uberblock with txg=23
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): read 1 log space maps (1 total blocks - blksz = 131072 bytes) in 0 ms
16:38:44.89 1678639097   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:38:44.89 1678639097   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2686387808200
16:38:44.89 1678639097   spa.c:8440:spa_async_request(): spa=testpool async request task=1
16:38:44.89 1678639097   spa.c:8440:spa_async_request(): spa=testpool async request task=2048
16:38:44.89 1678639097   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): LOADED
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686389 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686389 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686389 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   spa_history.c:306:spa_history_log_sync(): txg 25 open pool version 5000; software version 0280905; uts fv-az216-255 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:45 UTC 2023 x86_64
16:38:44.89 1678639097   metaslab.c:3926:metaslab_flush(): flushing: txg 25, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 11776, unflushed_frees 13824, appended 64 bytes
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 0, smp_length 208, unflushed_allocs 0, unflushed_frees 10752, freed 0, defer 0 + 10752, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268350976, max size error 268345344, old_weight 6c0000000000001, new_weight 6c0000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 1, smp_length 128, unflushed_allocs 3584, unflushed_frees 16384, freed 0, defer 0 + 10752, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268350976, max size error 268345344, old_weight 6c0000000000001, new_weight 6c0000000000001
16:38:44.89 1678639097   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 25, spa testpool, vdev_id 0, ms_id 2, smp_length 112, unflushed_allocs 3584, unflushed_frees 16384, freed 0, defer 0 + 10752, unloaded time 2686397 ms, loading_time 0 ms, ms_max_size 268370944, max size error 268365312, old_weight 6c0000000000001, new_weight 6c0000000000001
16:38:44.89 1678639097   spa.c:8440:spa_async_request(): spa=testpool async request task=32
16:38:44.89 1678639097   spa_history.c:306:spa_history_log_sync(): txg 27 import pool version 5000; software version 0280905; uts fv-az216-255 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:45 UTC 2023 x86_64
16:38:44.89 1678639097   metaslab.c:3926:metaslab_flush(): flushing: txg 27, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 3584, unflushed_frees 16384, appended 88 bytes
16:38:44.89 1678639100   spa_history.c:293:spa_history_log_sync(): command: zpool import testpool
16:38:44.89 1678639100   metaslab.c:3926:metaslab_flush(): flushing: txg 29, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 2560, unflushed_frees 16384, appended 80 bytes
16:38:44.89 1678639100   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
16:38:44.89 1678639100   metaslab.c:3926:metaslab_flush(): flushing: txg 30, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 14336, appended 32 bytes
16:38:44.89 1678639100   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
16:38:44.89 1678639100   metaslab.c:3926:metaslab_flush(): flushing: txg 39, spa testpool, vdev_id 0, ms_id 3, unflushed_allocs 17408, unflushed_frees 0, appended 56 bytes
16:38:44.89 1678639100   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2690034457000
16:38:44.89 1678639100   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 0280905; uts fv-az216-255 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:45 UTC 2023 x86_64
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
16:38:44.89 1678639100   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@block_cloning=enabled
16:38:44.89 1678639100   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2690211416200
16:38:44.89 1678639100   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690211 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
16:38:44.89 1678639100   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690211 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
16:38:44.89 1678639100   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690212 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690220 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 34816, unflushed_frees 0, appended 32 bytes
16:38:44.89 1678639101   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool loop0
16:38:44.89 1678639101   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 0, appended 56 bytes
16:38:44.89 1678639101   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 27136, unflushed_frees 0, appended 64 bytes
16:38:44.89 1678639101   metaslab.c:3926:metaslab_flush(): flushing: txg 10, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 17408, appended 112 bytes
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639101   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 10, spa testpool, vdev_id 1, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2690443 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639106   spa_history.c:293:spa_history_log_sync(): command: zpool add -f testpool loop1
16:38:44.89 1678639106   metaslab.c:3926:metaslab_flush(): flushing: txg 11, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 15872, unflushed_frees 12288, appended 96 bytes
16:38:44.89 1678639106   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 11, spa testpool, vdev_id 1, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2695619 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639111   spa_history.c:293:spa_history_log_sync(): command: zpool destroy -f testpool
16:38:44.89 1678639111   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 5120, unflushed_frees 14336, appended 72 bytes
16:38:44.89 1678639111   spa_misc.c:417:spa_load_note(): spa_load(testpool, config trusted): UNLOADING
16:38:44.89 1678639111   metaslab.c:3926:metaslab_flush(): flushing: txg 23, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 17408, unflushed_frees 15872, appended 80 bytes
16:38:44.89 1678639111   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool' gethrtime 2701183439400
16:38:44.89 1678639112   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 create pool version 5000; software version 0280905; uts fv-az216-255 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:45 UTC 2023 x86_64
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@async_destroy=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@empty_bpobj=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@lz4_compress=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@multi_vdev_crash_dump=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_histogram=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@enabled_txg=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@hole_birth=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@extensible_dataset=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@embedded_data=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmarks=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@filesystem_limits=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_blocks=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@large_dnode=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@sha512=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@skein=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@edonr=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@userobj_accounting=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@encryption=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@project_quota=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_removal=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@obsolete_counts=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zpool_checkpoint=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@spacemap_v2=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@allocation_classes=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@resilver_defer=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_v2=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redaction_bookmarks=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@redacted_datasets=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@bookmark_written=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@log_spacemap=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@livelist=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@device_rebuild=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zstd_compress=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@draid=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@zilsaxattr=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@head_errlog=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@blake3=enabled
16:38:44.89 1678639112   spa_history.c:306:spa_history_log_sync(): txg 4 set feature@block_cloning=enabled
16:38:44.89 1678639112   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool' gethrtime 2701488669100
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 0, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701489 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 1000000020000000, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 1, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701489 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001e8ba2e9, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 2, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701491 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 100000001d1745d2, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 6, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 7, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 8, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 9, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 4, spa testpool, vdev_id 0, ms_id 10, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2701506 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639112   metaslab.c:3926:metaslab_flush(): flushing: txg 5, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 33792, unflushed_frees 0, appended 32 bytes
16:38:44.89 1678639117   spa_history.c:293:spa_history_log_sync(): command: zpool create -f testpool mirror loop0 loop1
16:38:44.89 1678639117   metaslab.c:3926:metaslab_flush(): flushing: txg 8, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36352, unflushed_frees 0, appended 64 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 14, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 0, appended 80 bytes
16:38:44.89 1678639124   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': txg 14, spa testpool, DTL old object 0, new object 129
16:38:44.89 1678639124   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): LOADING
16:38:44.89 1678639124   vdev.c:161:vdev_dbgmsg(): disk vdev '/dev/loop1': best uberblock found for spa testpool2. txg 8
16:38:44.89 1678639124   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): using uberblock with txg=8
16:38:44.89 1678639124   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 6461db1cd83d5a to b3944ca035686c for pool testpool2 dataset id 48
16:38:44.89 1678639124   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): read 3 log space maps (3 total blocks - blksz = 131072 bytes) in 0 ms
16:38:44.89 1678639124   dprintf: brt.c:875:brt_vdevs_expand(): BRT VDEVs expanded from 0 to 1.
16:38:44.89 1678639124   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 8d9bef98416cea to a782c9d476b1d3 for pool testpool2 dataset id 54
16:38:44.89 1678639124   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 8d9bef98416cea to 962b6b456b11d0 for pool testpool2 dataset id 54
16:38:44.89 1678639124   dsl_dataset.c:726:dsl_dataset_hold_obj(): ds_fsid_guid changed from 8d9bef98416cea to 57ac64e471772b for pool testpool2 dataset id 54
16:38:44.89 1678639124   mmp.c:239:mmp_thread_start(): MMP thread started pool 'testpool2' gethrtime 2713877176900
16:38:44.89 1678639124   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 9, spa testpool2, vdev_id 0, ms_id 3, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2713880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639124   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 9, spa testpool2, vdev_id 0, ms_id 4, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2713880 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639124   metaslab.c:2440:metaslab_load_impl(): metaslab_load: txg 9, spa testpool2, vdev_id 0, ms_id 5, smp_length 0, unflushed_allocs 0, unflushed_frees 0, freed 0, defer 0 + 0, unloaded time 2713881 ms, loading_time 0 ms, ms_max_size 268435456, max size error 268435456, old_weight 700000000000001, new_weight 700000000000001
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 9, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 26112, unflushed_frees 0, appended 80 bytes
16:38:44.89 1678639124   spa.c:8440:spa_async_request(): spa=testpool2 async request task=1
16:38:44.89 1678639124   spa.c:8440:spa_async_request(): spa=testpool2 async request task=2048
16:38:44.89 1678639124   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): LOADED
16:38:44.89 1678639124   spa_history.c:306:spa_history_log_sync(): txg 10 open pool version 5000; software version 0280905; uts fv-az216-255 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:45 UTC 2023 x86_64
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 10, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 13312, unflushed_frees 20992, appended 112 bytes
16:38:44.89 1678639124   spa_history.c:306:spa_history_log_sync(): txg 15 detach vdev=/dev/loop1
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 15, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 23552, unflushed_frees 16384, appended 128 bytes
16:38:44.89 1678639124   spa_history.c:306:spa_history_log_sync(): txg 11 split from pool testpool
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 11, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 2048, unflushed_frees 16384, appended 88 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 2, unflushed_allocs 0, unflushed_frees 17920, appended 64 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 3, unflushed_allocs 19968, unflushed_frees 0, appended 48 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 4, unflushed_allocs 19968, unflushed_frees 0, appended 48 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 5, unflushed_allocs 19456, unflushed_frees 0, appended 48 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 0, unflushed_allocs 0, unflushed_frees 6144, appended 48 bytes
16:38:44.89 1678639124   metaslab.c:3926:metaslab_flush(): flushing: txg 20, spa testpool2, vdev_id 0, ms_id 1, unflushed_allocs 0, unflushed_frees 2048, appended 24 bytes
16:38:44.89 1678639124   spa_misc.c:417:spa_load_note(): spa_load(testpool2, config trusted): UNLOADING
16:38:44.89 1678639124   mmp.c:259:mmp_thread_stop(): MMP thread stopped pool 'testpool2' gethrtime 2713915446400
16:38:44.90 =================================================================
16:38:44.90  End of zfs_dbgmsg log
16:38:44.90 =================================================================
16:38:44.90 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:38:44.90 =================================================================
16:38:44.90  Tailing last 200 lines of dmesg log
16:38:44.90 =================================================================
16:38:44.91 [ 2563.583523] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos
16:38:44.91 [ 2564.221042] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos
16:38:44.91 [ 2564.716797] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos
16:38:44.91 [ 2565.812092] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg
16:38:44.91 [ 2566.198317] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos
16:38:44.91 [ 2570.097268] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos
16:38:44.91 [ 2573.260943] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted
16:38:44.91 [ 2580.127394] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted
16:38:44.91 [ 2590.405900] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709
16:38:44.91 [ 2592.403983] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
16:38:44.91 [ 2593.177110] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/setup
16:38:44.91 [ 2597.992433] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos
16:38:44.91 [ 2599.369128] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos
16:38:44.91 [ 2600.223907] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos
16:38:44.91 [ 2601.062534] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos
16:38:44.91 [ 2601.860307] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos
16:38:44.91 [ 2604.803466] ZTS run /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup
16:38:44.91 [ 2605.566945] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup
16:38:44.91 [ 2605.591525] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos
16:38:44.91 [ 2616.498085] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos
16:38:44.91 [ 2642.199889] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos
16:38:44.91 [ 2660.758261] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos
16:38:44.91 [ 2675.499038] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos
16:38:44.91 [ 2690.525732] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos
16:38:44.91 [ 2701.694345] ZTS run /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos
16:38:44.91 =================================================================
16:38:44.91  End of dmesg log
16:38:44.91 =================================================================
16:38:44.91 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:38:44.91 NOTE: Performing local cleanup via log_onexit (cleanup)
16:38:44.98 SUCCESS: zpool destroy -f testpool
16:38:44.98 SUCCESS: rm -f /var/tmp/testdir/vz007
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
16:25:27.04 ASSERTION: Verify refreservation is limited by available space.
16:25:27.08 SUCCESS: zfs create testpool/testfs/subfs
16:25:27.10 SUCCESS: zfs set quota=25M testpool
16:25:27.13 SUCCESS: zfs set refreservation=15M testpool
16:25:27.16 SUCCESS: zfs set refreservation=10263040 testpool/testfs/subfs
16:25:27.59 /var/tmp/testdir/subfs/testfile: initialized 10223616 of 10263040 bytes: Disk quota exceeded
16:25:27.59 ERROR: mkfile 10263040 /var/tmp/testdir/subfs/testfile exited 1
16:25:27.59 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dbgmsg.ksh)
16:25:27.59 =================================================================
16:25:27.59  Tailing last 200 lines of zfs_dbgmsg log
16:25:27.59 =================================================================
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 326, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 429056, unflushed_frees 35840, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 327, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 35840, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 328, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28160, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 329, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 35840, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 330, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 331, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28160, unflushed_frees 28672, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 332, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 333, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 334, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28160, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 335, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 36864, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 336, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 36864, unflushed_frees 36864, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 337, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 28672, unflushed_frees 28672, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 338, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430080, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 339, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37376, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 340, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 28672, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 341, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 430592, unflushed_frees 36864, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 342, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37376, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 343, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 29696, unflushed_frees 29696, appended 72 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 344, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37376, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 345, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 96 bytes
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 346 snapshot testpool/testfs@snap2 (id 367)  
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 346, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30208, unflushed_frees 29696, appended 80 bytes
16:25:27.61 1678638326   spa_history.c:329:spa_history_log_sync(): ioctl snapshot
16:25:27.61 1678638326   spa_history.c:293:spa_history_log_sync(): command: zfs snapshot testpool/testfs@snap2
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 347, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 311296, unflushed_frees 179712, appended 152 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 348, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 57344, unflushed_frees 48640, appended 168 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 349, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 41984, unflushed_frees 40448, appended 136 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 350, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 175616, unflushed_frees 35328, appended 144 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 351, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 36864, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 352, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 353, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431104, unflushed_frees 37888, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 354, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 355, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 30720, unflushed_frees 30720, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 356, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431104, unflushed_frees 37888, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 357, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 37888, unflushed_frees 37888, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 358, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 30720, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 359, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 37888, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 360, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 37888, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 361, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31232, unflushed_frees 31232, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 362, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 431616, unflushed_frees 38400, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 363, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38400, unflushed_frees 38400, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 364, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 31232, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 365, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432128, unflushed_frees 38400, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 366, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 38912, unflushed_frees 38400, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 367, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 31744, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 368, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 38912, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 369, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39424, unflushed_frees 38912, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 370, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 31744, unflushed_frees 31744, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 371, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433152, unflushed_frees 39424, appended 136 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 372, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 39936, unflushed_frees 39424, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 373, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 31744, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 374, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 432640, unflushed_frees 39936, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 375, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 39936, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 376, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32256, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 377, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 39424, appended 136 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 378, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40448, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 379, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 380, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 40448, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 381, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 40448, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 382, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32256, unflushed_frees 32768, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 383, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 40448, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 384, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40448, unflushed_frees 40448, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 385, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32256, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 386, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40448, appended 136 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 387, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40448, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 388, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 33280, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 389, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40448, appended 136 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 390, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40448, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 391, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32768, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 392, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 433664, unflushed_frees 40960, appended 128 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 393, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41472, unflushed_frees 40960, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 394, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 395, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40448, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 396, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 41472, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 397, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 33280, appended 64 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 398, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 434176, unflushed_frees 40960, appended 104 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 399, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 40960, unflushed_frees 40960, appended 96 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 400, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 32768, unflushed_frees 32768, appended 80 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 401, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 40960, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 402, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 40960, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 403, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33280, unflushed_frees 32768, appended 88 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 404, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 41984, appended 120 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 405, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 41984, unflushed_frees 41984, appended 112 bytes
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 406, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 33792, unflushed_frees 33280, appended 80 bytes
16:25:27.61 1678638326   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap errno: 0
16:25:27.61 1678638326   zcp.c:657:zcp_debug(): txg 407 ZCP: snap: testpool/testfs@snap2 errno: 0
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap (id 339)  
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 407 destroy testpool/testfs@snap2 (id 367)  
16:25:27.61 1678638326   dsl_scan.c:3493:dsl_process_async_destroys(): freed 23 blocks in 0ms from free_bpobj/bptree on testpool in txg 407; err=0
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 407, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 304128, unflushed_frees 173056, appended 120 bytes
16:25:27.61 1678638326   spa_history.c:329:spa_history_log_sync(): ioctl destroy_snaps
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 408, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 52224, unflushed_frees 69632, appended 216 bytes
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 409 set testpool/testfs (id 308) refreservation=0
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 409 destroy testpool/testfs (id 308) (bptree, mintxg=1)
16:25:27.61 1678638326   bptree.c:225:bptree_iterate(): bptree index 0: traversing from min_txg=1 bookmark 0/0/0/0
16:25:27.61 1678638326   dsl_scan.c:3493:dsl_process_async_destroys(): freed 190 blocks in 1ms from free_bpobj/bptree on testpool in txg 409; err=0
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 409, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 44544, unflushed_frees 47616, appended 152 bytes
16:25:27.61 1678638326   spa_history.c:293:spa_history_log_sync(): command: zfs destroy -rf testpool/testfs
16:25:27.61 1678638326   spa_history.c:297:spa_history_log_sync(): txg 410 create testpool/testfs (id 408)  
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 410, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 43520, unflushed_frees 22110208, appended 896 bytes
16:25:27.61 1678638326   spa_history.c:329:spa_history_log_sync(): ioctl create
16:25:27.61 1678638326   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs
16:25:27.61 1678638326   metaslab.c:3926:metaslab_flush(): flushing: txg 411, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 56832, unflushed_frees 72704, appended 192 bytes
16:25:27.61 1678638327   spa_history.c:297:spa_history_log_sync(): txg 412 set testpool/testfs (id 408) mountpoint=/var/tmp/testdir
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 412, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 44544, unflushed_frees 54272, appended 144 bytes
16:25:27.61 1678638327   spa_history.c:293:spa_history_log_sync(): command: zfs set mountpoint=/var/tmp/testdir testpool/testfs
16:25:27.61 1678638327   spa_history.c:297:spa_history_log_sync(): txg 413 create testpool/testfs/subfs (id 416)  
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 413, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 68096, unflushed_frees 50176, appended 152 bytes
16:25:27.61 1678638327   spa_history.c:329:spa_history_log_sync(): ioctl create
16:25:27.61 1678638327   spa_history.c:293:spa_history_log_sync(): command: zfs create testpool/testfs/subfs
16:25:27.61 1678638327   spa_history.c:297:spa_history_log_sync(): txg 414 set testpool (id 54) quota=26214400
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 414, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 64000, unflushed_frees 46080, appended 144 bytes
16:25:27.61 1678638327   spa_history.c:293:spa_history_log_sync(): command: zfs set quota=25M testpool
16:25:27.61 1678638327   spa_history.c:297:spa_history_log_sync(): txg 415 set testpool (id 54) refreservation=15728640
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 415, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 45056, unflushed_frees 39424, appended 88 bytes
16:25:27.61 1678638327   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=15M testpool
16:25:27.61 1678638327   spa_history.c:297:spa_history_log_sync(): txg 416 set testpool/testfs/subfs (id 416) refreservation=10263040
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 416, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 66560, unflushed_frees 53760, appended 136 bytes
16:25:27.61 1678638327   spa_history.c:293:spa_history_log_sync(): command: zfs set refreservation=10263040 testpool/testfs/subfs
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 417, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 136 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 418, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 40448, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 419, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 47104, unflushed_frees 47104, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 420, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47104, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 421, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 34816, unflushed_frees 34816, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 422, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 435200, unflushed_frees 40960, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 423, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 42496, unflushed_frees 41984, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 424, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35840, unflushed_frees 34816, appended 80 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 425, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 41984, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 426, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 42496, unflushed_frees 42496, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 427, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 35328, unflushed_frees 35840, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 428, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 43008, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 429, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 42496, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 430, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 35328, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 431, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436224, unflushed_frees 43520, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 432, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 43520, unflushed_frees 43520, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 433, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36352, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 434, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437248, unflushed_frees 43008, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 435, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 43520, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 436, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36864, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 437, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 436736, unflushed_frees 44032, appended 136 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 438, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 44032, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 439, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36864, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 440, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437760, unflushed_frees 43520, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 441, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 44032, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 442, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36864, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 443, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437760, unflushed_frees 44544, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 444, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44032, unflushed_frees 44544, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 445, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36352, unflushed_frees 36864, appended 80 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 446, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437760, unflushed_frees 44544, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 447, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 44544, unflushed_frees 44032, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 448, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 36864, unflushed_frees 36352, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 449, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 437760, unflushed_frees 44544, appended 136 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 450, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45056, unflushed_frees 44544, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 451, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37888, unflushed_frees 36864, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 452, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 44544, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 453, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45056, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 454, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 37888, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 455, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 438784, unflushed_frees 45568, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 456, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 45568, unflushed_frees 45568, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 457, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 37376, unflushed_frees 37376, appended 80 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 458, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439808, unflushed_frees 45568, appended 136 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 459, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 46592, unflushed_frees 45568, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 460, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38400, unflushed_frees 37376, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 461, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 46592, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 462, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 46592, appended 136 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 463, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38400, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 464, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 47104, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 465, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47616, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 466, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38912, appended 80 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 467, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 439296, unflushed_frees 47104, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 468, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47104, unflushed_frees 47104, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 469, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 38912, unflushed_frees 38912, appended 80 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 470, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440320, unflushed_frees 46080, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 471, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47104, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 472, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 38912, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 473, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 440832, unflushed_frees 47104, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 474, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 47616, unflushed_frees 47616, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 475, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 88 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 476, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441344, unflushed_frees 47616, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 477, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 47616, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 478, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 479, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 48128, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 480, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48128, unflushed_frees 48128, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 481, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39936, appended 64 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 482, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441856, unflushed_frees 48640, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 483, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 48128, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 484, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39424, unflushed_frees 39936, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 485, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 441344, unflushed_frees 48640, appended 120 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 486, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 48640, unflushed_frees 48640, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 487, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 39936, unflushed_frees 39424, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 488, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442368, unflushed_frees 48128, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 489, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 48640, appended 96 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 490, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40448, unflushed_frees 39936, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 491, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49152, appended 128 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 492, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 493, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40448, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 494, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 442880, unflushed_frees 49664, appended 112 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 495, spa testpool, vdev_id 0, ms_id 1, unflushed_allocs 49664, unflushed_frees 49664, appended 104 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 496, spa testpool, vdev_id 0, ms_id 2, unflushed_allocs 40960, unflushed_frees 40960, appended 72 bytes
16:25:27.61 1678638327   metaslab.c:3926:metaslab_flush(): flushing: txg 497, spa testpool, vdev_id 0, ms_id 0, unflushed_allocs 443392, unflushed_frees 49664, appended 104 bytes
16:25:27.62 =================================================================
16:25:27.62  End of zfs_dbgmsg log
16:25:27.62 =================================================================
16:25:27.62 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_dmesg.ksh)
16:25:27.62 =================================================================
16:25:27.62  Tailing last 200 lines of dmesg log
16:25:27.62 =================================================================
16:25:27.64 [  466.770489] loop0: detected capacity change from 0 to 6291456
16:25:27.64 [  466.796492] loop1: detected capacity change from 0 to 6291456
16:25:27.64 [  466.818039] loop2: detected capacity change from 0 to 6291456
16:25:27.64 [  467.005522] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/setup
16:25:27.64 [  467.028343] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg
16:25:27.64 [  469.716710] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos
16:25:27.64 [  773.355273] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos
16:25:27.64 [  836.620831] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos
16:25:27.64 [  899.865217] ZTS run /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup
16:25:27.64 [  899.886698] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup
16:25:27.64 [  900.358217] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed
16:25:27.64 [  901.848661] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents
16:25:27.64 [  906.321765] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted
16:25:27.64 [  907.591609] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature
16:25:27.64 [  908.863703] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded
16:25:27.64 [  973.817031] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes
16:25:27.64 [  980.013493] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_incrementals
16:25:27.64 [  986.238894] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_largeblocks
16:25:27.64 [  988.357269] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_many_clones
16:25:27.64 [  996.692781] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mixed_recsize
16:25:27.64 [  999.065603] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_mounts
16:25:27.64 [ 1000.559731] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_negative
16:25:27.64 [ 1001.668158] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_origin
16:25:27.64 [ 1004.522863] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_panic
16:25:27.64 [ 1065.604123] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_props
16:25:27.64 [ 1069.091194] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_resume
16:25:27.64 [ 1071.310391] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_size
16:25:27.64 [ 1071.992999] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_volume
16:25:27.64 [ 1072.116134] debugfs: Directory 'zd0' with parent 'block' already present!
16:25:27.64 [ 1082.468978] debugfs: Directory 'zd0' with parent 'block' already present!
16:25:27.64 [ 1082.639333] debugfs: Directory 'zd16' with parent 'block' already present!
16:25:27.64 [ 1082.807726] debugfs: Directory 'zd32' with parent 'block' already present!
16:25:27.64 [ 1093.160801] debugfs: Directory 'zd32' with parent 'block' already present!
16:25:27.64 [ 1093.458625] debugfs: Directory 'zd32' with parent 'block' already present!
16:25:27.64 [ 1103.813139] debugfs: Directory 'zd32' with parent 'block' already present!
16:25:27.64 [ 1104.025068] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redacted_send/cleanup
16:25:27.64 [ 1104.277025] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/setup
16:25:27.64 [ 1104.299278] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid
16:25:27.64 [ 1275.823580] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1
16:25:27.64 [ 1293.534270] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2
16:25:27.64 [ 1320.155599] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3
16:25:27.64 [ 1369.001364] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1
16:25:27.64 [ 1498.809430] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2
16:25:27.64 [ 1605.276713] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1
16:25:27.64 [ 1653.566711] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2
16:25:27.64 [ 1680.052816] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3
16:25:27.64 [ 1752.024544] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror
16:25:27.64 [ 1785.040765] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz
16:25:27.64 [ 1952.449135] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1
16:25:27.64 [ 1969.275253] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2
16:25:27.64 [ 1991.159933] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3
16:25:27.64 [ 2024.415666] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe
16:25:27.64 [ 2029.215787] ZTS run /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup
16:25:27.64 [ 2029.254079] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/setup
16:25:27.64 [ 2029.582527] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos
16:25:27.64 [ 2032.500229] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos
16:25:27.64 [ 2034.750996] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos
16:25:27.64 [ 2036.774289] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos
16:25:27.64 [ 2040.253779] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos
16:25:27.64 [ 2042.729475] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg
16:25:27.64 [ 2043.449308] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg
16:25:27.64 [ 2043.902924] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg
16:25:27.64 [ 2049.833080] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup
16:25:27.64 [ 2050.094836] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup
16:25:27.64 [ 2050.417955] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos
16:25:27.64 [ 2051.240425] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos
16:25:27.64 [ 2052.958282] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos
16:25:27.64 [ 2054.010175] ZTS run /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos
16:25:27.65 =================================================================
16:25:27.65  End of dmesg log
16:25:27.65 =================================================================
16:25:27.65 NOTE: Performing test-fail callback (/usr/share/zfs/zfs-tests/callbacks/zfs_mmp.ksh)
16:25:27.65 NOTE: Performing local cleanup via log_onexit (cleanup)
16:25:27.67 SUCCESS: zfs set refreservation=none testpool
16:25:27.73 SUCCESS: zfs destroy -rf testpool/testfs
16:25:27.77 SUCCESS: zfs create testpool/testfs
16:25:27.81 SUCCESS: zfs set mountpoint=/var/tmp/testdir testpool/testfs
</pre></details>
<details><summary>Full Listing</summary><pre>
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/setup (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/dosmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/posixmode (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/acl/off/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/setup (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/posix_004_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix-sa/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/setup (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/posix_004_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/acl/posix/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/alloc_class/alloc_class_012_pos (run as root) [02:10] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/atime_003_pos (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/root_relatime_on (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/atime/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_011_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cache_012_pos (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cache/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cachefile_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cachefile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/case_all_values (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/casenorm/norm_all_values (run as root) [00:01] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/setup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/chattr_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/chattr_002_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/chattr/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/clean_mirror_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/clean_mirror/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/l2arc_encrypted_no_compressed_arc (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/compress_004_pos (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/compression/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cp_files/cp_files_001_pos (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_001_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_003_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_006_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_007_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_009_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_010_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_011_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_allow_012_neg (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_007_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/zfs_unallow_008_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/delegate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_002_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/devices_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/devices/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/read_dos_attrs_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/write_dos_attrs_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/dos_attributes/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/events_001_pos (run as root) [00:39] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/events_002_pos (run as root) [00:52] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_rc_filter (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_fd_spill (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_cksum_reported (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_cksum_config (run as root) [00:38] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/zed_io_config (run as root) [01:24] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/events/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/exec_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/exec/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/fadvise_sequential (run as root) [00:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fadvise/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_punch-hole (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/fallocate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_prealloc (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/fallocate_zero-range (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fallocate/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_offline_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_online_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_online_002_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_replace_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_001_pos (run as root) [01:09] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_002_pos (run as root) [00:07] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_multiple (run as root) [03:49] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_ashift (run as root) [00:02] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/auto_spare_shared (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/decrypt_fault (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/decompress_fault (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/scrub_after_resilver (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/zpool_status_-s (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/fault/cleanup (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/async_destroy_001_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/async_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_001_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_004_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_005_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_009_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_002_pos (run as root) [00:14] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_006_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/large_dnode_008_pos (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/features/large_dnode/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_pool_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/grow/grow_replicas_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_002_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_003_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_009_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/history_010_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/history/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/hkdf/hkdf_test (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_002 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_003 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_004 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/idmap_mount_005 (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/idmap_mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/inheritance/inherit_001_pos (run as root) [01:27] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/libaio (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/io_uring (run as root) [00:06] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/io/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/setup (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_arcstats_pos (run as root) [00:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_mfuonly_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/l2arc_l2miss_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_002_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_003_neg (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_004_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/persist_l2arc_005_pos (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/l2arc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/large_files_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/large_files/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/largest_pool/largest_pool_001_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/many_fds (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/libzfs_input (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/libzfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_count (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/limits/filesystem_limit (run as root) [00:03] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/mmap_libaio_001_pos (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmap/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_thread (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_uberblocks (run as root) [00:11] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_off (run as root) [00:18] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_interval (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_active_import (run as root) [03:10] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_inactive_import (run as root) [01:59] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_exported_import (run as root) [00:09] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_write_uberblocks (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_reset_interval (run as root) [04:47] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/multihost_history (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_on_zdb (run as root) [00:37] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_write_distribution (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/mmp_hostid (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mmp/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umount_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/umountall_001 (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/umount_unlinked_drain (run as root) [00:09] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/mount/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_001_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/mv_files_002_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/random_creation (run as root) [00:54] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/mv_files/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/nestedfs_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nestedfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_002_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_003_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_df (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_ganging (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/enospc_rm (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/no_space/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_copies (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_mtime (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_negative (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_promoted_clone (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_recsize (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_sync (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_varying_compression (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/nopwrite_volume (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/nopwrite/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_002_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_006_pos (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_args_pos (run as root) [03:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_block_size_histogram (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_checksum (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_display_block (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_encrypted (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_label_checksum (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_neg (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_object_range_pos (run as root) [01:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_objset_id (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_decompress_zstd (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zdb/zdb_recover_2 (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/zfs_003_neg (run as root) [00:30] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/zfs_bookmark_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_bookmark/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_child (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_format (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_inherit (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_load (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_location (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_pbkdf2iters (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_change-key/zfs_change-key_clones (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_010_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/zfs_clone_deeply_nested (run as root) [01:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_clone/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_001_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_003_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_005_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/zfs_copies_006_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_copies/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_007_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_008_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_create/zfs_create_010_neg (run as root) [00:03] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_and_disable (run as root) [00:58] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_condense_races (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_clone_livelist_dedup (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_001_pos (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_005_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_009_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_010_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_012_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_013_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_014_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_015_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_016_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_clone_livelist (run as root) [01:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/zfs_destroy_dev_removal_condense (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_destroy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_changes (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_timestamp (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_types (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/zfs_diff_mangle (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_diff/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_001_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_002_pos (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_005_neg (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_008_pos (run as root) [00:32] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_009_pos (run as root) [01:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/zfs_get_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_get/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/zfs_ids_to_path_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_ids_to_path/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_002_neg (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/zfs_inherit_mountpoint (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_inherit/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_load-key/zfs_load-key_all (run as root) [00:09] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_remount (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_fail (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_all_mountpoints (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_test_race (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_006_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_008_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_mount_014_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/zfs_multi_mount (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_mount/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_override (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/receive-o-x_props_aliases (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_to_encrypted (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_incremental (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-e (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_raw_-d (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_from_zstd (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_new_props (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_-wR-encrypted-mix (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_corrective (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/zfs_receive_compressed_corrective (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_receive/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/setup (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_002_pos (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_004_neg (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_005_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_009_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_012_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_rename/zfs_rename_014_neg (run as root) [00:24] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_007_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_encrypted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_raw (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_sparse (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send-b (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_send/zfs_send_skip_missing (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/reservation_001_neg (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/share_mount_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/snapdir_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/onoffs_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/readonly_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/user_property_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/version_001_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_001_neg (run as root) [00:57] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_002_neg (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/property_alias_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/mountpoint_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/ro_props_001_pos (run as root) [01:41] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_keylocation (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/zfs_set_feature_activation (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_011_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_concurrent_shares (run as root) [01:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/setup (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_005_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_007_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_009_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_012_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/zfs_share_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_share/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_004_neg (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_005_neg (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_006_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_007_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/zfs_snapshot_009_pos (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_snapshot/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfeature_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_get_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zfs_sysfs_live (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zpool_get_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/zpool_set_unsupported (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_sysfs/cleanup (run as root) [00:00] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_005_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_all_001_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_nested (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_unmount/zfs_unmount_unload_keys (run as root) [00:08] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_003_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zfs_upgrade/zfs_upgrade_004_pos (run as root) [00:11] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_008_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_009_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_010_pos (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add-o_ashift (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_prop_ashift (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/zpool_add_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/add_nested_replacing_spare (run as root) [00:05] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_add/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/zpool_attach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_attach/attach-o_ashift (run as root) [00:22] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_006_pos (run as root) [00:12] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_001_pos (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_002_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_003_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_draid_004_pos (run as root) [03:55] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_004_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_006_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_007_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_008_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_features_009_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/create-o_ashift (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_tempname (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/zpool_create_dryrun_output (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_create/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_destroy/zpool_destroy_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/zpool_detach_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_detach/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_cliargs (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_follow (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_poolname (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_errors (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_duplicates (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/zpool_events_clear_retained (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_events/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_002_pos (run as root) [00:38] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_003_neg (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_004_pos (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/zpool_expand_005_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_expand/cleanup (run as root) [00:01] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_001_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_002_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_004_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_005_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_007_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_008_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_009_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_010_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_011_neg (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_012_pos (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_013_neg (run as root) [01:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_014_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_015_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_016_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_017_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_001_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_002_neg (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_features_003_pos (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_001_pos (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_002_pos (run as root) [01:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_missing_003_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_rename_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_all_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_encrypted_load (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata3 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/zpool_import_errata4 (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_added (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_removed (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_device_replaced (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_attached (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_mirror_detached (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_paths_changed (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_cachefile_shared_device (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_devices_missing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_paths_changed (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_config_changed (run as root) [01:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/import_rewind_device_replaced (run as root) [00:16] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_import/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_attach_detach_add_remove (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_fault_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_import_export (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_offline_export_import_online (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_online_offline (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_split (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_start_and_cancel_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_suspend_resume (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_unsupported_vdevs (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_checksums (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/zpool_initialize_verify_initialized (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_initialize/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_active (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_labelclear/zpool_labelclear_exported (run as root) [00:04] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_remove/cleanup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/setup (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_001_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_002_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_003_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_004_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_005_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_006_neg (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/zpool_reopen_007_pos (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_reopen/cleanup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/zpool_replace_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace-o_ashift (run as root) [00:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/replace_prop_ashift (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_replace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_bad_args (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/zpool_resilver_restart (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_resilver/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_001_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_004_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_encrypted_unloaded (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_print_repairing (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_offline_device (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/zpool_scrub_multiple_copies (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_scrub/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_002_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_003_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_ashift (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/zpool_set_features (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_set/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_cliargs (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_devices (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_encryption (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_props (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_vdevs (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_resilver (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_dryrun_output (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/zpool_split_wholedisk (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_split/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_004_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_005_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/zpool_status_features_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_status/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_001_pos (run as root) [00:49] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/zpool_sync_002_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_sync/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_002_pos (run as root) [01:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_004_pos (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_007_pos (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_008_pos (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/zpool_upgrade_features_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_upgrade/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_discard (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_freeing (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_initialize_flag (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_multiple (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_no_activity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_remove_cancel (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_basic (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_trim_flag (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/zpool_wait_usage (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/setup (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace_cancel (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_rebuild (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_resilver (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_cancel (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_replace (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_basic (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/zpool_wait_scrub_flag (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/cli_root/zpool_wait/scan/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_001_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_002_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/online_offline_003_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/online_offline/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/setup (run as root) [00:26] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_basic (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_nounmount (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/pam_short_password (run as root) [00:07] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/pam/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/setup (run as root) [00:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_after_rewind (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_big_rewind (run as root) [02:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_capacity (run as root) [00:40] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_conf_change (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_busy (run as root) [03:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_discard_many (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_indirect (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_invalid (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_lun_expsz (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_open (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_removal (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_rewind (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_ro_rewind (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_sm_scale (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_twice (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_vdev_add (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zdb (run as root) [01:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/checkpoint_zhack_feat (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_checkpoint/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_001_pos (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pool_names/pool_names_002_neg (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/poolversion_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/poolversion/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_basic (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_concurrent_readers (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/procfs_list_stale_read (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/pool_state (run as root) [00:00] [SKIP]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/procfs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/setup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectid_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_002_pos (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_004_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_005_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_006_pos (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_007_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_008_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectquota_009_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_001_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_002_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projectspace_004_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/projecttree_003_neg (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/projectquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/pyzfs/pyzfs_unittest (run as root) [01:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_001_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_002_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_003_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_004_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/quota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/quota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_001_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/scrub_mirror_004_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/scrub_mirror/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/simd/simd_supported (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_001_pos (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_002_pos (run as root) [00:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_003_pos (run as root) [01:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_004_pos (run as root) [00:39] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_005_pos (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_006_pos (run as root) [04:38] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_007_pos (run as root) [01:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_008_neg (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_009_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_010_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_011_neg (run as root) [00:37] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_012_neg (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_013_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_014_pos (run as root) [00:20] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_015_neg (run as root) [00:29] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_001 (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/slog/slog_replay_fs_002 (run as root) [00:25] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_015_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/snapshot_016_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/snapshot/cleanup (run as root) [00:00] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_001_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/tmpfile_stat_mode (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/tmpfile/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_integrity (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_config (run as root) [00:56] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/autotrim_trim_integrity (run as root) [00:59] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_integrity (run as root) [00:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_config (run as root) [00:52] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/trim/trim_l2arc (run as root) [00:34] [PASS]
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
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/upgrade_projectquota_001_pos (run as root) [00:12] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/upgrade/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_001 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_002 (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_003 (run as root) [00:03] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/user_namespace_004 (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/user_namespace/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_002_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_003_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_004_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_005_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_006_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_007_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_008_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_009_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_011_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_012_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_001_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_002_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_send_encrypted (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_encrypted_13709 (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/setup (run as root) [00:04] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_001_pos (run as root) [00:01] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_002_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/groupspace_003_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/userquota_013_pos (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/userspace_003_pos (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/userquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_002_pos (run as root) [00:25] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_003_pos (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_004_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_005_pos (run as root) [00:15] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_006_pos (run as root) [00:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/vdev_zaps_007_pos (run as root) [00:12] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/vdev_zaps/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/write_dirs/write_dirs_002_pos (run as root) [00:33] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/xattr/xattr_012_pos (run as root) [00:11] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_rename_inuse (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_snapdev (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_trim (run as root) [01:23] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_volmode (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_zil (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/zvol_misc_fua (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_misc/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/zvol_stress (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_stress/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_002_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/zvol_swap_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/zvol/zvol_swap/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_001_neg (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_002_pos (run as root) [05:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_003_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/raidz_004_pos (run as root) [01:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/raidz/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_compressed (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_deleted (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_disabled_feature (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_embedded (run as root) [01:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redacted_send/redacted_holes (run as root) [00:06] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid1 (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid2 (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid3 (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged1 (run as root) [02:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2 (run as root) [01:46] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare1 (run as root) [00:48] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare2 (run as root) [00:26] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_draid_spare3 (run as root) [01:11] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_mirror (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz (run as root) [02:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz1 (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz2 (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_raidz3 (run as root) [00:33] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/redundancy_stripe (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/redundancy/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_001_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_002_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_003_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_004_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_005_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_006_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_007_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/refquota_008_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refquota/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_001_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_002_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_003_pos (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_004_pos (run as root) [00:00] [FAIL]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_005_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_multi_raidz (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/refreserv_raidz (run as root) [00:47] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/refreserv/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_all_vdev (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_cancel (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_check_space (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_condense_export (run as root) [00:35] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_multiple_indirection (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_nopwrite (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_remap_deadlists (run as root) [00:27] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_resume_export (run as root) [01:30] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_add (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_create_fs (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_errors (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_export (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_ganging (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_faulted (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_remove (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_scrub (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_send_recv (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_snapshot (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_write (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/removal_with_zdb (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_expanded (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_mirror_sanity (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_raidz (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_indirect (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/remove_attach_mirror (run as root) [01:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/removal/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/rename_dirs_001_pos (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rename_dirs/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/setup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_noreplace (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_exchange (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/renameat2_whiteout (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/renameat2/cleanup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/setup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_import (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_multiple (run as root) [00:21] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_rebuild (run as root) [00:31] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/attach_resilver (run as root) [00:19] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/detach (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_disabled_feature (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_multiple (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/rebuild_raidz (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_import (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_rebuild (run as root) [01:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/replace_resilver (run as root) [01:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_001 (run as root) [00:36] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/resilver_restart_002 (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/replacement/scrub_cancel (run as root) [00:15] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_015_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/reservation/reservation_016_pos (run as root) [00:10] [PASS]
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
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/recv_dedup_encrypted_zvol (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_001_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_002_pos (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_003_pos (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_004_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_005_pos (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_006_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_007_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_008_pos (run as root) [00:00] [SKIP]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_009_pos (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_010_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_011_pos (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_012_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_013_pos (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_014_pos (run as root) [00:06] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_016_neg (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_019_pos (run as root) [00:50] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_020_pos (run as root) [00:16] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_021_pos (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_022_pos (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_024_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_025_pos (run as root) [00:13] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_026_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_027_pos (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_028_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_029_neg (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_030_pos (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/rsend_031_pos (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_ratio (run as root) [00:44] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_verify_contents (run as root) [00:04] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_props (run as root) [00:18] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_incremental (run as root) [00:12] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_volume (run as root) [00:02] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstream_recompress (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_zstreamdump (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_lz4_disabled (run as root) [00:09] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_lz4_disabled (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_mixed_compression (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_stream_size_estimate (run as root) [00:08] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_embedded_blocks (run as root) [01:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_resume (run as root) [00:17] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-cpL_varied_recsize (run as root) [00:24] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-c_recv_dedup (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-L_toggle (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_incremental (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_freeobjects (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_hierarchy (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_props (run as root) [00:10] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_truncated_files (run as root) [00:03] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_freeobjects (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_files (run as root) [00:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_encrypted_files (run as root) [00:34] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_spill_block (run as root) [00:42] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_holds (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_hole_birth (run as root) [00:14] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_mixed_raw (run as root) [00:07] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send-wR_encrypted_zvol (run as root) [00:05] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_partial_dataset (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_invalid (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_doall (run as root) [00:00] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_spill_block (run as root) [00:45] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_ashift (run as root) [01:28] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/send_raw_large_blocks (run as root) [00:01] [PASS]
Test: /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/setup (run as root) [00:02] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/send_realloc_dnode_size (run as root) [00:05] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/send_encrypted_files (run as root) [00:19] [PASS]
Test (Linux): /usr/share/zfs/zfs-tests/tests/functional/rsend/cleanup (run as root) [00:00] [PASS]
</pre></details>
