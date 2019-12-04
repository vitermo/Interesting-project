from PIL import Image

IMG = '/Users/vitermo/Downloads/335d5b227c935f4db7a5f08d47752609.jpeg'
WIDTH=60
HEIGHT=45

# 字符画所用的字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha=256):
    # 判断alpha 值，如果alpha值为0的时候表示图片中该位置为空白
    if alpha == 0:
        return " "
    # 获取字符集的长度，这里为70
    length = len(ascii_char)

    # 将RGB 值转为灰度值gray，灰度值范围为0-255
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)

    # 灰度值范围为0-255，而字符集只有70
    # 需要进行如下处理才能将灰度值映射道指定的字符上
    unit = (256.0 + 1) / length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # 打开图片并调整宽和高
    img = Image.open(IMG)
    img = img.resize((WIDTH,HEIGHT),Image.NEAREST)

    # 初始化输出的字符串
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'

    print(txt)
    # 写入文件
    with open("output.txt", 'w') as f:
        f.write(txt)



