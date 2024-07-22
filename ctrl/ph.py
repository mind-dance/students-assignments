import re

def get_user_input(template):
    """
    提示用户输入模板中所有占位符的值并返回填充后的字符串。
    """
    # 查找模板中的所有占位符，形如'${...}'
    placeholders = re.findall(r'\$\{([^}]*)\}', template)
    
    # 提示用户输入每个占位符的值
    values = {ph: input(f"请输入{ph}的值: ") for ph in placeholders}
    
    # 将占位符替换为用户输入的值
    filled_template = template
    for ph, val in values.items():
        filled_template = filled_template.replace("${" + ph + "}", val)
    print(filled_template, template)
    return filled_template

# 示例模板，用户可以自由更改
# template = input("请输入模板，例如：${id}-${name}-实验报告${exp_id}: ")
template = "${id}-${name}-实验报告${exp_id}"

# 使用函数并打印结果
result = get_user_input(template)
print("生成的字符串为:", result)
