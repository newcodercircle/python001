import random
import string
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def gen_verify_code() -> (BytesIO, str):
    """
    生成一个验证码
    """
    # 定义图像颜色模型
    mode = "RGB"
    # 定义图像尺寸
    size = (200, 100)
    # 定义背景色
    bg_color = (random_color(), random_color(), random_color())
    # 创建图像
    image = Image.new(mode=mode, size=size, color=bg_color)
    # 创建画布
    image_draw = ImageDraw.Draw(image, mode=mode)
    # 创建字体,第一个参数是字体，第二个参数是字体大小
    image_font = ImageFont.truetype(font="./Peralta-Regular.ttf", size=80)
    # 创建一个验证码
    verify_code = random_code()
    # 生成验证码
    # fill_color = (255,255,255)
    for i in range(4):
        fill_color = (random_color(), random_color(), random_color())
        image_draw.text(
            xy=(50 * i, 0), text=verify_code[i], font=image_font, fill=fill_color
        )
    # 加入干扰点
    for i in range(5000):
        fill_color = (random_color(), random_color(), random_color())
        xy = (random.randrange(200), random.randrange(100))
        image_draw.point(xy=xy, fill=fill_color)
    # 保存图像
    fp = BytesIO()
    image.save(fp, "png")
    with open("res.png", "wb") as f:
        f.write(fp.getvalue())
    return fp.getvalue(), verify_code


def random_color():
    """随机获取颜色"""
    return random.randrange(256)


def random_code():
    """随机获取验证码"""
    # 增加了生成数字验证码的概率
    verify_code = "".join(
        random.choice(
            string.ascii_uppercase + string.digits * 10 + string.ascii_lowercase
        )
        for _ in range(4)
    )
    return verify_code


print(gen_verify_code())
