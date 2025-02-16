from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено!")
        self.original.show()

    def black_white(self):
        bw_image = self.original.convert('L')
        self.changed.append(bw_image)
        bw_image.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.show()

        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.' + temp_filename[1]
        rotated.save(new_filename)

    def do_cropped(self):
        box = (250,100,600,400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.show()

        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.' + temp_filename[1]
        cropped.save(new_filename)

my_image = ImageEditor('forest.png')
my_image.open()
my_image.black_white()
my_image.do_left()
my_image.do_cropped()