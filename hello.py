from PIL import Image, ImageFilter

before = Image.open("audirs5.jpeg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpeg")