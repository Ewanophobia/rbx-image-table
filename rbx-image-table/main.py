import tkinter as tk
import os

from slpp import SLPP
from PIL import Image
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png .jpeg .jpg")])

return_keyword = "return "

if file_path:
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    image = Image.open(file_path)
    rgba_image = image.convert("RGBA")

    pixels = {}

    for x in range(image.size[0]):
        pixels[x + 1] = {}

        for y in range(image.size[1]):
            red, green, blue = image.getpixel((x, y))
            pixels[x + 1][y + 1] = f"Color3.new({ red / 255 }, { green / 255 }, { blue / 255 })"

    lua = SLPP()
    encoded = lua.encode(pixels)
    dequotationed = encoded.replace('"', "")

    file = filedialog.asksaveasfile(mode = "w", defaultextension = ".lua")

    if file is None:
        exit("User cancelled dialog")

    file.write(return_keyword + dequotationed)
    file.close()

    exit("Done!")
else:
    exit("You must select a file!")