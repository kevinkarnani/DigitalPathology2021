from matplotlib import pyplot as plt
import pandas as pd
import os

def download_file_from_s3(image_folder, bucket):
    images = []
    local_imgs_dir = f'local_images/{image_folder}'

    if not os.path.exists(local_imgs_dir):
        os.makedirs(local_imgs_dir)

    for x in bucket.objects.all():
        if f'Preprocessing/{image_folder}' in x.key:
            images.append(x.key)

    images.sort(key=lambda x: x[1])

    for image in images:
        # df = pd.read_csv(image, header=None)
        df = pd.read_csv(image)
        ds_array = df.to_numpy()
        x_size = ds_array.shape[0]
        ds_array = ds_array.reshape((x_size, x_size, 3))
        plt.imshow(ds_array, vmin=0, vmax=255, cmap="gray")
        plt.show()
        # save_path = os.path.join(f'local_images', image_folder, f'{image}.png')
        # plt.imsave(save_path, ds_array)
    
