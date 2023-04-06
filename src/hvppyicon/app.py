import sys

def rgb_to_hex(rgb):
    ret = ""
    for v in rgb:
        ret += "{:02x}".format(v)
    return ret

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    import importlib_resources
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources
    
def run(**kwargs):
    text: str = kwargs.get("text", "A")
    color: str = kwargs.get("color", "default").lower()
    colors = {
        "default": (255, 255, 255, 230),
        "gray": (151, 154, 155, 242),
        "brown": (147, 114, 100, 255),
        "orange": (255, 163, 68, 255),
        "yellow": (255, 220, 73, 255),
        "green": (77, 171, 154, 255),
        "blue": (82, 156, 202, 255),
        "purple": (154, 109, 215, 255),
        "pink": (226, 85, 161, 255),
        "red": (255, 115, 105, 255),
    }
    color_tuple = colors.get(color, colors["default"])
    
    from PIL import Image, ImageDraw, ImageFont

    # 이미지 크기 설정
    width, height = 280, 280
    background_color = color_tuple
    font_file = str(importlib_resources.path("hvppyicon.assets", "Helvetica-Bold-Font.ttf"))
    print(font_file)
    color_in_hex = rgb_to_hex(background_color)
    # 모서리 둥글기 반지름 설정
    corner_radius = 64 - 16

    # 텍스트 색 설정
    text_color = (255, 255, 255, 0)

    font_size = 192 + 32

    offset_y = 0
    offset_x = 0

    # 새 이미지 생성 (RGBA 모드, 지정된 크기, 투명)
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 드로잉 객체 생성
    draw = ImageDraw.Draw(image)

    # 원형 모서리의 원 그리기
    draw.ellipse((0, 0, corner_radius * 2, corner_radius * 2), fill=background_color)
    draw.ellipse((width - corner_radius * 2, 0, width, corner_radius * 2), fill=background_color)
    draw.ellipse((0, height - corner_radius * 2, corner_radius * 2, height), fill=background_color)
    draw.ellipse((width - corner_radius * 2, height - corner_radius * 2, width, height), fill=background_color)

    # 사각형 그리기 (모서리를 제외한 부분)
    draw.rectangle((corner_radius, 0, width - corner_radius, height), fill=background_color)
    draw.rectangle((0, corner_radius, width, height - corner_radius), fill=background_color)

    # 시스템 폰트 사용 (폰트 크기 40)
    font = ImageFont.truetype(font_file, font_size)

    # 텍스트 크기 계산
    #_, _, text_width, text_height = draw.textbbox((0, 0), text, font)
    text_width, text_height = font.getsize(text)
    print(f"text_width: {text_width}, text_height: {text_height}")

    # 텍스트 위치 계산 (이미지 가운데)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # 텍스트 그리기
    draw.text((text_x + offset_x, text_y + offset_y), text, fill=text_color, font=font)

    # 이미지 저장 (투명한 부분 포함)
    image.save(f"hvppyicon_{text}_{width}x{height}_{color_in_hex}.png", format="PNG")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-c", "--color", type=str, help="Enter color name")
    parser.add_argument("character", type=str, help="Enter a character")
    
    args = parser.parse_args()
    
    run(color=args.color, text=args.character)
    