from PIL import Image


class ImageToPPM:

    def __init__(self, image):
        self.rotation = 90
        self.im = Image.open(image).rotate(self.rotation)
        self.pixels = list(self.im.getdata())
        self.width, self.height = self.im.size
        self.colour_map = {
            0: (255, 255, 255),
            1: (255, 255, 0),
            2: (0, 0, 0),
            3: (128, 255, 0),
            4: (0, 64, 255),
            5: (192, 0, 255),
            6: (255, 128, 0),
            7: (0, 255, 255),
            8: (255, 0, 255)
        }

    def preview_coin(self):
        pixel_string = ''
        for i in range(self.height):
            pixel_line = ''
            for pixel in self.pixels[i * self.width:(i + 1) * self.width]:
                pixel_line = pixel_line + str(pixel)
            pixel_string = pixel_string + pixel_line + '\n'
        return pixel_string

    def output_coin_ppm(self):
        ppm_string = ''
        for i in range(self.height):
            pixel_line = ''
            for pixel in self.pixels[i * self.width:(i + 1) * self.width]:
                pixel_line = pixel_line + str(pixel)
            ppm_string = ppm_string + pixel_line + '.'
        return ppm_string[:-1]

    def image_from_ppm(self, ppm, filename):
        width = 0
        height = 0
        img_data = []
        for i in ppm.split('.'):
            width = len(i)
            height = height + 1
            for s in i:
                img_data.append(int(s))
        z = 0
        img = Image.new('RGB', (height, width))
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = self.colour_map[img_data[z]]
                img.putpixel((x, y), (r, g, b))
                z = z + 1
        img.save(filename, save_all=True, append_images=[img])

    def image_from_ppm_list(self, ppm_list, filename_prefix):
        z = 0
        for x in ppm_list:
            self.image_from_ppm(x, filename_prefix + '-' + str(z) + '.gif')
            z = z + 1
