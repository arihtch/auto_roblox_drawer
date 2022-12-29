from PIL import Image
from time import sleep

def convert_rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb



fname = input("Enter file name: ")
try:
    image = Image.open(fname)
except:
    print("Cannot find file? try adding the file extension (.png, .jpeg etc)")
    print("Please close and try again")
    sleep(5)

resized_image = image.resize((32, 32))
rgb_resized_image = resized_image.convert("RGB")
rgb_resized_image_pixel = rgb_resized_image.load()
print(rgb_resized_image_pixel[0.5,0.5])
rgb_resized_image.show()


#
# loops over the image and prints out the hex values
#

for i in range(32):
    for j in range(32):
        rgb_code = rgb_resized_image_pixel[i,j]
        hex_code = convert_rgb_to_hex(rgb_code)
        print(hex_code)






