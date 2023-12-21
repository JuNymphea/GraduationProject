import torch
import os
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained("/home/ruiboming/.cache/huggingface/hub/models--stabilityai--stable-diffusion-2-1/snapshots/5cae40e6a2745ae2b01ad92ae5043f95f23644d6", torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

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

for file_name in files:
    file_path = os.path.join(folder, file_name)

    with open(file_path, "r") as file:
        for line in file:
            for template in prompt_templates:
                prompt = template.format(line)
       
            image = pipe(prompt).images[0]

            save_path = os.path.join(output_folder, f"{line.strip()}.png")

            image.save(save_path)
