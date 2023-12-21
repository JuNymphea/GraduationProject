import os

# 指定保存文件夹路径
output_folder = "PNGcityscapes"

# 确保保存文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# prompt 模板
prompt_templates = [
    "a photo of a {} the urban street"
]
# 从txt文件中取出prompt
folder = "cityscapes"

files = [f for f in os.listdir(folder) if f.endswith('.txt')]
print(files)

for file_name in files:
    file_path = os.path.join(folder, file_name)

    with open(file_path, "r") as file:
        for line in file:

            for template in prompt_templates:
                prompt = template.format(line)
                
            print(prompt)

