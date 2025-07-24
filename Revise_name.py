import re

def to_valid_folder_name(name: str) -> str:
    name = name.strip()
    # 将所有非法字符（包括 -）替换为 _
    name = re.sub(r'[^A-Za-z0-9_]', '_', name)
    # 合并连续多个 _
    name = re.sub(r'_+', '_', name)
    # 如果以数字开头，加前缀 _
    if re.match(r'^[0-9]', name):
        name = '_' + name
    return name

model_name = "Qwen2.5-7B-Instruct"
name_identifier = to_valid_folder_name(model_name)
print(name_identifier)  