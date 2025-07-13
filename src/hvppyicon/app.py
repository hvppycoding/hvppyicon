import sys
import argparse
import re

from PIL import Image, ImageDraw, ImageFont

def parse_rgba(value: str):
    """
    문자열을 RGBA 튜플로 변환.
    예: 'rgba(255,115,105,255)' → (255, 115, 105, 255)
    """
    if isinstance(value, tuple):
        return value
    rgba_match = re.match(r'rgba?\s*\(\s*(\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+))?\s*\)', value, re.IGNORECASE)
    if rgba_match:
        r, g, b, a = rgba_match.groups()
        return (int(r), int(g), int(b), int(a) if a is not None else 255)
    raise ValueError(f"Invalid RGBA format: {value}")

def rgb_to_hex(rgb):
    return "".join("{:02x}".format(v) for v in rgb)

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

def run(**kwargs):
    text: str = kwargs.get("text", "A")
    bg_color_input = kwargs.get("bg_color", "default").lower()
    font_color_input = kwargs.get("font_color", "rgba(255,255,255,255)")
    output: str = kwargs.get("output", "")
    user_yoffset: int = kwargs.get("yoffset", 0)
    default_offset: int = -12
    yoffset = default_offset + user_yoffset

    # 기본 색상 맵
    default_colors = {
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

    # 배경색 파싱
    try:
        background_color = parse_rgba(bg_color_input)
    except Exception:
        background_color = default_colors.get(bg_color_input, default_colors["default"])

    # 텍스트 색 파싱
    try:
        text_color = parse_rgba(font_color_input)
    except Exception:
        text_color = (255, 255, 255, 255)

    width, height = 280, 280
    corner_radius = 48
    font_size = 256

    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        (0, 0, width, height),
        radius=corner_radius,
        fill=background_color
    )

    try:
        with importlib_resources.path("hvppyicon.assets", "Helvetica-Bold-Font.ttf") as p:
            font_file = str(p)
        font = ImageFont.truetype(font_file, font_size)
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    draw.text((text_x, text_y + yoffset), text, fill=text_color, font=font)

    if output:
        image.save(output, format="PNG")
    else:
        filename = f"hvppyicon_{text}_{width}x{height}_{rgb_to_hex(background_color)}.png"
        image.save(filename, format="PNG")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-bg", "--bg-color", type=str, help="Background color (name or rgba format)")
    parser.add_argument("-fc", "--font-color", type=str, help="Font color (rgba format)")
    parser.add_argument("character", type=str, help="Enter a character")
    parser.add_argument("--yoffset", type=int, default=0, help="Enter y-offset of the text")
    parser.add_argument("-o", "--output", type=str, help="Enter the output filename")
    
    args = parser.parse_args()
    run(
        bg_color=args.bg_color,
        font_color=args.font_color,
        text=args.character,
        output=args.output,
        yoffset=args.yoffset,
    )

if __name__ == "__main__":
    main()