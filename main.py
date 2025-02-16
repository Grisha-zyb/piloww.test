from PIL import Image, ImageFilter

with Image.open('forest.png') as photo:
   # photo.show()
    print(photo.size)
    print(photo.format)
    print(photo.mode)

    #photo = photo.convert("1")
    #photo.show()

    #photo = photo.transpose(Image.FLIP_LEFT_RIGHT)
    #photo = photo.transpose(Image.ROTATE_180)
    #photo = photo.filter(ImageFilter.BLUR)
    #photo = photo.filter(ImageFilter.SHARPEN)
    #photo = photo.filter(ImageFilter.DETAIL)
    #photo = photo.filter(ImageFilter.EMBOSS)
    #photo = photo.filter(ImageFilter.CONTOUR)

    
    photo.show()