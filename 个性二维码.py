from MyQR import myqr

# 黑白二维码
# myqr.run(
#     words='https://github.com/vitermo/-',
#     picture = '/Users/vitermo/Downloads/d0811f38c6ab6c1055a006522e20db0a.jpg',
#     save_name = '潮女妖.png'
# )

# 彩色二维码
# myqr.run(
#     words='https://github.com/vitermo/-',
#     picture = '/Users/vitermo/Downloads/d0811f38c6ab6c1055a006522e20db0a.jpg',
#     colorized=True,
#     save_name = '潮女妖1.png'
# )

# 动态二维码

myqr.run(
    words='https://github.com/vitermo/-',
    picture = '/Users/vitermo/Downloads/96faf04f1ead5e399e11994c33409fa0.gif',
    colorized=True,
    save_name = '动态.gif'
)