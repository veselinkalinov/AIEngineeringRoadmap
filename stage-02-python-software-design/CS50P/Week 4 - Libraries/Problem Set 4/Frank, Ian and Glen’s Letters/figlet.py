import sys

# pyrefly: ignore [missing-import]
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = None

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid font")

    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

text = input("Input: ")

if font:
    figlet.setFont(font=font)

print(figlet.renderText(text))
