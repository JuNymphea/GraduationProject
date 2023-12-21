import os
import shutil

# 源文件夹和目标文件夹
source_folder = "/home/ruiboming/source/sbpku/PNGcityscapes"
destination_folder = "/home/ruiboming/source/sbpku/SegEx"

# 获取源文件夹中所有的 .png 文件
image_files = [f for f in os.listdir(source_folder) if f.endswith(".png")]

# 限制复制的数量
num_images_to_copy = 200
image_files_to_copy = image_files[:num_images_to_copy]

# 确保目标文件夹存在，如果不存在就创建它
os.makedirs(destination_folder, exist_ok=True)

# 复制文件并按顺序重命名
for index, image_file in enumerate(image_files_to_copy, start=1):
    source_path = os.path.join(source_folder, image_file)
    destination_path = os.path.join(destination_folder, f"{index}.png")
    shutil.copyfile(source_path, destination_path)

