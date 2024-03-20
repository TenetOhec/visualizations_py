import os
from tqdm import tqdm

def list_dir(directory):
    # 获取当前目录下的文件
    files = os.listdir(directory)

    for file_name in tqdm(files, desc="重命名进度", unit="文件"):
        # 获得旧文件的完整路径
        old_file_path = os.path.join(directory, file_name)

        # 判断是否文件夹,是则递归
        if os.path.isdir(old_file_path):
            list_dir(old_file_path)
            continue
        # 去掉文件名中的【海量资源：666java.com】
        new_file_name = file_name.replace("【海量 资源：666java.com】", "")

        # 构建新文件名的完整路径
        new_file_path = os.path.join(directory, new_file_name)

        # 重命名文件
        os.rename(old_file_path, new_file_path)

        print(f"文件已重命名：{file_name} -> {new_file_name}")


# 执行操作
list_dir("/Volumes/My Passport/java 黑马入门/06阶段六：服务框架基础")
