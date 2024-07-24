import os
import shutil
import time


def get_format_str(group_type = 1):
    default = "%Y-%m-%d"
    if group_type == 1:
        return "%Y-%m-%d"
    elif group_type == 2:
        return "%Y-%m"
    return default


def organize_files(source_dir, target_dir, group_type = 1):
    files = os.listdir(source_dir)
    if len(files) == 0:
        return 1
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        # 获取文件的拍摄日期（如果存在）或者修改日期
        date_str = None
        stat = os.stat(filepath)
        if stat:
            date_str = time.strftime(get_format_str(group_type), time.localtime(stat.st_mtime))
            dest_dir = os.path.join(target_dir, date_str)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(filepath, dest_dir)

    return 0


# 测试函数
# source_directory = '/Users/shangjianguo/codes/python-tools/test_files'
# target_directory = '/Users/shangjianguo/codes/python-tools/test_files_dest'
# organize_files(source_directory, target_directory)