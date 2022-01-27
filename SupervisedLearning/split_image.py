from matplotlib import pyplot as plt
import numpy as np
import os


def split_image(ds, file_name) -> None:
    """Split a tiff image dataset into tiles (512 x 512) and save it locally

    :param ds: dataset of the image
    :param file_name: name of the file (image)
    :return: void
    """
    
    x_size, y_size             = ds.RasterXSize, ds.RasterYSize
    xoff, yoff, xcount, ycount = (0, 0, 512, 512)
    rgb_weights                = [0.2989, 0.5870, 0.1140]
    light_pink                 = (255, 213, 234)
    light_purple               = (176, 100, 147)
    purple                     = (125, 58, 102)
    red                        = (190, 72, 107)

    threshold_value            = 0.85
    white_value                = 0.5
    local_imgs_dir             = f'local_images/{file_name}'
    
    if not os.path.exists(local_imgs_dir):
        print("creating dir", local_imgs_dir)
        os.makedirs(local_imgs_dir)

    while xoff + xcount < x_size:
        while yoff + ycount < y_size:               
            # produces a (3, x, y) matrix
            ds_array = ds.ReadAsArray(xoff, yoff, xcount, ycount)

            # transforms (3, x, y) matrix to (x, y, 3)
            ds_array = np.moveaxis(ds_array, 0, -1)
            isInColorRange = color_range(red=ds_array[..., 0], green=ds_array[..., 1], blue=ds_array[..., 2])

            #... - everything from the third column
            # convert rgb image to grayscale
            greyscale_image = np.uint8(np.dot(ds_array[...,:3], rgb_weights))

            # if pixel is > 85% white, make it white, else make it black
            bin_image = np.where(greyscale_image > threshold_value*255, 255, 0)
            
            # if average of binary image is less than 50% white, then create tile of image
            if np.mean(bin_image) < white_value*255:
                plt.imshow(ds_array)
                print("RGB Values: ")
                print("Red mean:", np.mean(ds_array[..., 0]))
                print("Green mean:", np.mean(ds_array[..., 1]))
                print("Blue mean:", np.mean(ds_array[..., 2]))

                isInColorRange(light_pink, "light pink")
                isInColorRange(light_purple, "light purple")
                isInColorRange(purple, "purple")
                isInColorRange(red, "red")

                # if isInColorRange(light_pink) or isInColorRange(light_purple) or isInColorRange(purple) or isInColorRange(red):
                    # save_path = os.path.join('local_images', file_name, f'{file_name}_{xoff}_{yoff}.png')
                    # plt.imsave(save_path, ds_array)

            yoff += ycount

        xoff += xcount
        yoff = 0


def color_range(red, green, blue):
    def color(ranges_tuple, message):
        red_mean = np.mean(red)
        green_mean = np.mean(green)
        blue_mean = np.mean(blue)

        if (((0.95*ranges_tuple[0] <= red_mean and red_mean <= 1.05*ranges_tuple[0]) and
            (0.95*ranges_tuple[1] <= green_mean and green_mean <= 1.05*ranges_tuple[1]) and
            (0.95*ranges_tuple[2] <= blue_mean and blue_mean <= 1.05*ranges_tuple[2]))):
            print(message)

        # if majority of red, green, and blue channels are within +- 5% of range
        # print((0.95*ranges_tuple[0] <= red_mean or red_mean <= 1.05*ranges_tuple[0]) and
        #     (0.95*ranges_tuple[1] <= green_mean or green_mean <= 1.05*ranges_tuple[1]) and
        #     (0.95*ranges_tuple[2] <= blue_mean or blue_mean <= 1.05*ranges_tuple[2]))
        # return ((0.95*ranges_tuple[0] <= red_mean or red_mean <= 1.05*ranges_tuple[0]) and
        #     (0.95*ranges_tuple[1] <= green_mean or green_mean <= 1.05*ranges_tuple[1]) and
        #     (0.95*ranges_tuple[2] <= blue_mean or blue_mean <= 1.05*ranges_tuple[2]))
    
    return color
