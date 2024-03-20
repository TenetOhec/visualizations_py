import os

def rename_files(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)
    print(files)

    for file_name in files:
        # 构建旧文件名的完整路径
        old_file_path = os.path.join(directory, file_name)

        # 判断文件是否为文件夹
        if os.path.isdir(old_file_path):
            # 如果是文件夹，递归调用本函数
            rename_files(old_file_path)
            continue

        # 去掉文件名中的【海量资源：666java.com】
        new_file_name = file_name.replace("【海量 资源：666java.com】", "")

        # 构建新文件名的完整路径
        new_file_path = os.path.join(directory, new_file_name)

        # 重命名文件
        os.rename(old_file_path, new_file_path)

        print(f"文件已重命名：{file_name} -> {new_file_name}")

# 调用函数来重命名指定目录中的文件
rename_files("/Volumes/My Passport/java 黑马入门/04阶段四：热门框架/01第一章：1-Spring框架/day02_Spring框架/03-讲义")
