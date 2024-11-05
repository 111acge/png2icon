from PIL import Image
import os


def convert_png_to_ico(png_path, ico_path):
    # 打开PNG图片
    img = Image.open(png_path)

    # 确保图片是正方形的
    width, height = img.size
    size = max(width, height)
    new_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    new_img.paste(img, ((size - width) // 2, (size - height) // 2))

    # 调整大小为标准图标尺寸（例如32x32）
    icon_sizes = [(32, 32)]
    img.save(ico_path, format='ICO', sizes=icon_sizes)


# 转换图片
png_path = r'C:/Users/29193/OneDrive/图片/market.png'
ico_path = r'C:/Users/29193/OneDrive/图片/market.ico'
convert_png_to_ico(png_path, ico_path)