import os
import numpy as np
from matplotlib import pyplot as plt
from s3_upload import upload_file_to_s3
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io

def split_image(ds, fn) -> None:
    x_size, y_size = ds.RasterXSize, ds.RasterYSize
    xoff, yoff, xcount, ycount = (0, 0, 512, 512)
    rgb_weights = [0.2989, 0.5870, 0.1140]
    threshold_value = 0.85
    white_value = 0.5
    # local_imgs_dir = f'local_images/{fn}'
    
    # if not os.path.exists(local_imgs_dir):
    #     print("creating dir", local_imgs_dir)
    #     os.makedirs(local_imgs_dir)

    while xoff + xcount < x_size:
        while yoff + ycount < y_size:               
            # produces a (3, x, y) matrix
            ds_array = ds.ReadAsArray(xoff, yoff, xcount, ycount)

            # transforms (3, x, y) matrix to (x, y, 3)
            ds_array = np.moveaxis(ds_array, 0, -1)
            greyscale_image = np.uint8(np.dot(ds_array[...,:3], rgb_weights))
            bin_array = np.where(greyscale_image > threshold_value*255, 255, 0)
            
            if np.mean(bin_array) < white_value*255: 
                # plt.imshow(bin_array, vmin=0, vmax=255, cmap="gray")
                # plt.show()
                # save_path = os.path.join(f'local_images', fn, f'{fn}_{xoff}_{yoff}.png')
                # plt.imsave(save_path, ds_array)
                
                # render figure onto canvas
                # canvas = FigureCanvas(ds_array)

                # prepare in-memory binary stream buffer (think of this as a txt file but purely in memory)
                # imdata = io.BytesIO() 
                
                # writes canvas object as a png file to the buffer.
                # canvas.print_png(imdata)  


                file_name = f'{fn}/{fn}_{xoff}_{yoff}.png'
                upload_file_to_s3(ds_array, file_name)

            yoff += ycount

        xoff += xcount
        yoff = 0
