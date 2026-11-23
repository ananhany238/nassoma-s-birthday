# pip install pillow pillow-avif-plugin
from PIL import Image
import os
sizes = {"discoball": 400, "gracie": 600, "taylor": 600, "jane": 600}
for f in os.listdir("images"):
    name, ext = os.path.splitext(f)
    if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".avif"):
        continue
    im = Image.open(f"images/{f}")
    im.thumbnail((sizes.get(name, 800),) * 2)
    if ext.lower() in (".jpg", ".jpeg"):
        im.convert("RGB").save(f"images/{f}", quality=75, optimize=True)
    else:
        im.save(f"images/{f}", quality=75)