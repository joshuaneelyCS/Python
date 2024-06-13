from byuimage import Image
import sys
print(sys.argv)

# def calc_pay(rate, hours):
#     return rate * hours
#
# rate = float(sys.argv[1])
# hours = float(sys.argv[2])
#
# print(calc_pay(rate, hours))

# takes in

#validates command
def validate_commands(list):
    # validates whether it has a function and an argument
    if list[1] == '-d' and list[2]:
        return 1
    elif list[1] == '-k' and type(float(list[4])) == float:
        return 2
    elif list[1] == '-s' and list[2]:
        return 3
    elif list[1] == '-g' and list[2]:
        return 4
    elif list[1] == '-b' and list[7]:
        return 5
    elif list[1] == '-f' and list[3]:
        return 6
    elif list[1] == '-m' and list[3]:
        return 7
    elif list[1] == '-c' and list[7]:
        return 8
    elif list[1] == '-y' and list[6]:
        return 9
    return False

# displays the image
def  test_image_display(list):
    if validate_commands(list):
        myImage = Image(list[2])
        myImage.show()

#darkens the image
def darken(list):
    print(list)
    if validate_commands(list) == 2:
        #assign image
        myImage = Image(list[2])
        #make a new image
        newImage = Image.blank(myImage.width, myImage.height)
        for y in range(myImage.height):
            for x in range(myImage.width):
                pixel = myImage.get_pixel(x, y)
                new_pixel = newImage.get_pixel(x, y)

                scale = 1 - float(list[4])
                if x == 0 and y == 0:
                    print(pixel.red)
                    print(scale)
                    print("hi" + str(new_pixel.red))
                new_pixel.red = pixel.red * (scale)
                new_pixel.green = pixel.green * (scale)
                new_pixel.blue = pixel.blue * (scale)
        newImage.show()
        newImage.save(list[3])

def sepia(list):
    if validate_commands(list) == 3:
        # assign image
        myImage = Image(list[2])
        # make a new image
        newImage = Image.blank(myImage.width, myImage.height)
        for y in range(myImage.height):
            for x in range(myImage.width):
                pixel = myImage.get_pixel(x, y)
                new_pixel = newImage.get_pixel(x, y)
                true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
                true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
                true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
                if true_red > 255:
                    true_red = 255
                if true_green > 255:
                    true_green = 255
                if true_blue > 255:
                    true_blue = 255
                new_pixel.red = true_red
                new_pixel.green = true_green
                new_pixel.blue = true_blue
        newImage.show()
        newImage.save(str(list[3]))

def grayscale(list):
    if validate_commands(list) == 4:
        # assign image
        myImage = Image(list[2])
        # make a new image
        newImage = Image.blank(myImage.width, myImage.height)
        for y in range(myImage.height):
            for x in range(myImage.width):
                pixel = myImage.get_pixel(x, y)
                new_pixel = newImage.get_pixel(x, y)
                average = (pixel.red + pixel.green + pixel.blue) / 3
                new_pixel.red = average
                new_pixel.blue = average
                new_pixel.green = average
                if x == 99 and y == 0:
                    print(f"red:{pixel.red} green:{pixel.green} blue:{pixel.blue}")
                    print(average)
        newImage.show()
        newImage.save(list[3])

def make_borders(list):
    if validate_commands(list) == 5:
        # assign image
        myImage = Image(list[2])
        # make a new image
        thickness = int(list[4])
        red = float(list[5])
        green = float(list[6])
        blue = float(list[7])
        newImage = Image.blank(myImage.width+(thickness*2), myImage.height+(thickness*2))

        for y in range(-thickness, thickness):
            for x in range(newImage.width):
                border_pixel = newImage.get_pixel(x,y)
                border_pixel.red = red
                border_pixel.green = green
                border_pixel.blue = blue

        for x in range(-thickness, thickness):
            for y in range(newImage.height):
                border_pixel = newImage.get_pixel(x,y)
                border_pixel.red = red
                border_pixel.green = green
                border_pixel.blue = blue

        for y in range(myImage.height):
            for x in range(myImage.width):
                pixel = myImage.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x+thickness,y+thickness)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue

        newImage.show()
        newImage.save(list[3])

def flipped(list):
    if validate_commands(list) == 6:
        filename2 = Image(list[2])
        new_image = Image.blank(filename2.width, filename2.height)
        for y in range(filename2.height):
            for x in range(filename2.width):
                pixel = filename2.get_pixel(x,(-1*(y+1)))
                new_pixel = new_image.get_pixel(x,y)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue
        new_image.show()
        new_image.save(list[3])

def mirror(list):
    if validate_commands(list) == 7:
        filename2 = Image(list[2])
        new_image = Image.blank(filename2.width, filename2.height)
        for y in range(filename2.height):
            for x in range(filename2.width):
                pixel = filename2.get_pixel((-1*(x+1)),y)
                new_pixel = new_image.get_pixel(x,y)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue
        new_image.show()
        new_image.save(list[3])

def collage(list):
    if validate_commands(list) == 8:
        image_1 = Image(list[2])
        image_2 = Image(list[3])
        image_3 = Image(list[4])
        image_4 = Image(list[5])
        thickness = int(list[7])
        total_width = image_1.width + image_2.width + (3 * thickness)
        total_height = image_1.height + image_3.height + (3 * thickness)
        newImage = Image.blank(total_width, total_height)
        for y in range(total_height):
            for x in range(total_width):
                pixel = newImage.get_pixel(x,y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0

        #inserts image 1
        for y in range(image_1.height):
            for x in range(image_1.width):
                pixel = image_1.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x+thickness,y+thickness)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue

        for y in range(image_2.height):
            for x in range(image_2.width):
                pixel = image_2.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x + image_1.width + (thickness * 2), y + thickness)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue

        for y in range(image_3.height):
            for x in range(image_3.width):
                pixel = image_3.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x + thickness, y + (thickness * 2) + image_1.height)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue

        for y in range(image_4.height):
            for x in range(image_4.width):
                pixel = image_4.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x + image_1.width + (thickness * 2), y + (thickness*2) + image_1.height)
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue

        newImage.show()
        newImage.save(list[6])

def detect_green(pixel, factor, threshold):
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False
def green_screen(list):
    if validate_commands(list) == 9:
        foregroundImage = Image(list[2])
        backgroundImage = Image(list[3])
        newImage = Image.blank(foregroundImage.width, foregroundImage.height)
        factor = float(list[6])
        threshold = float(list[5])
        for y in range(foregroundImage.height):
            for x in range(backgroundImage.width):
                for_pixel = foregroundImage.get_pixel(x,y)
                new_pixel = newImage.get_pixel(x, y)
                if detect_green(for_pixel, factor, threshold):
                    back_pixel = backgroundImage.get_pixel(x, y)
                    new_pixel.red = back_pixel.red
                    new_pixel.green = back_pixel.green
                    new_pixel.blue = back_pixel.blue
                else:
                    new_pixel.red = for_pixel.red
                    new_pixel.green = for_pixel.green
                    new_pixel.blue = for_pixel.blue
        newImage.show()
        newImage.save(list[4])

# shows the image
test_image_display(sys.argv)
darken(sys.argv)
sepia(sys.argv)
grayscale(sys.argv)
make_borders(sys.argv)
flipped(sys.argv)
mirror(sys.argv)
collage(sys.argv)
green_screen(sys.argv)

if __name__ == "__main__":
    pass