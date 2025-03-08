def get_style(style_name):
    with open(f"./styles/{style_name}.qss", "r",encoding='utf-8') as f:
        return f.read()
