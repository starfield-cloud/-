import matplotlib.font_manager as fm

# 获取所有字体列表
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 打印所有字体路径
for font in font_list:
    print(font)