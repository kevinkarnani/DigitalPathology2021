import re
import os
import boto3

def download_file_from_s3(image_folder, bucket):
    """Download a file from a folder in an S3 bucket

    :param image_folder: folder containing preprocessed images for a whole image
    :return: void
    """
    images = []
    image_dir = f'local_images/{image_folder}'

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    s3_client = boto3.client('s3',
        aws_access_key_id='ASIAWJQCCJF2CTJBOUR5',
        aws_secret_access_key='OZraK3lHwqBwVsO6GyaekVqnCTlpQA63AcwJzwqB',
        aws_session_token='IQoJb3JpZ2luX2VjEHoaCXVzLWVhc3QtMSJHMEUCIQD+vn1LyOq/WFHeNFU4MH396OG9lzLPytkig2or6cVQ5QIgO+nNpV1nXW8NXiirk5Bl3nLZTS+H/OVyT/PotnizbHIqkwMIk///////////ARAAGgw0MzI3MjIyOTkyNTIiDKWW1+K06YyRxZcgASrnAjTTwyaMolhKauBvO9hSnMg8Dds4E7EP+vubbVgJ6QMkXdhxIYJWU2aI6oY5PbXhxgWwTuVlzPjd/EueiHxajBGI0gUHYrf5daYzu0HDeEqV7aopFDp5Mzg6FP5XWsTL/EVSPEGp/br16u+WXYlYCQMfYSJz/tDfb95G13Yq8nZOdBvMLXO31fDJZfZWULEvbElBaLcKCi763yH6yaIwJXPCtO+XxV4NM/t9WJKXCWRXqSrdO9bP961Cne+lTc21XYKpP7CC4te/uIja8gcBNHHrtp6NP2MuvPXJc9zXqVkntlMBR/OFfHhTv2P2A8eJqJ+QdJ79yo0EJ9P6TkYXPwL7SbnhpGU4zJnvAnUGCLZHx+N8H+KC+IYQJMUTBs3a5yfS+BtD97m6e0H/8z1gvS5gM+6/tucO8212vocckBvsz7+2snA3lXaK6jg77aBm+J+va+UoyM94c4WZBg1+sZsgKLXjmWNPMPuLjI8GOqYBoc+mlRbk71yoIFP7GSrZkEZ6dHgGelRZpmI0s5tbLoTDclBS56uidzlLtnY6gJI0Hn5Syrlk7sn0NJ5UUZeXvuLPJNZVjiBQO2j7kuCoEBAwf7CdWoWTvvGBNOoOWNRhoiV4El0Szn/DCOwytJ59hotsyQmLhrMiotFoYhG4r2kryLcfoP8WKoY15cVk9OV8zUM7muRPu6jVfH37A/0uEUqwCX8Qtw==')

    for x in bucket.objects.all():
        if f'Preprocessing/{image_folder}' in x.key:
            images.append(x.key)

    images.sort(key=lambda x: x[1])

    for image in images:
        file_name = re.search('([^\/]+$)', image).group()
        save_path = os.path.join('local_images', image_folder, f'{file_name}')
        s3_client.download_file('digpath-data', image, save_path)



# def download_file_from_s3(image_folder, bucket):
#     images = []
#     local_imgs_dir = f'local_images/{image_folder}'

#     if not os.path.exists(local_imgs_dir):
#         os.makedirs(local_imgs_dir)

#     s3_client = boto3.client('s3',
#         aws_access_key_id='ASIAWJQCCJF2M4DSCAOJ',
#         aws_secret_access_key='ZdbQLhsa/K7mNyUgHLa6fziBKj1J0phNo/gSaSR6',
#         aws_session_token='IQoJb3JpZ2luX2VjEB4aCXVzLWVhc3QtMSJHMEUCIQDuYEWSY2S5E6sR/Hjcf43m8CqOSFnFWIDYQpsm6VOMUwIgDL74ub56nR6shT5JfNkFvPOe1yXzBlG6pvp1g6fSIZ8qigMINxAAGgw0MzI3MjIyOTkyNTIiDAzJlf3vf5vcoo42pyrnAkObLWWmx2VEm5/VtwadyN9KDR0enQqE/ddbrlfq1Kv9XmqswqQXqNxEmjqYD8FXFr3SoI6iqAEOcf5k3ebBM+rFTMHeS/Lad2n4X9WdzeXQpXqqCcRs5Z1wG3wUojAXCS1O9inAi60QMsqarri4NANGsKcNNP7rUiwgnLw4C7BCpoK0w/uHC00mQbkEniBlIrfxrlDGSZbyKDJOrxi5h8KSs9OA9ELnt7sR13i4OJ09MHuRwL26AE2ex6hPb0JwvQOk8Twjio1Xmh169F3cLqMboPoQqavKhwK5P4hR8US00V2SI34GL03ifN940/XdhKtFfiphxBJSHh3oNV5bd25Nbj2BOYn03L/j8zMasp7SWk9oaOtqpGHieuDm6bS/mUc+gAtDLuM6a49MfhA49XM/3hvKMs/JW8xhnRqWBJS+LC+qzOqKOAaHFN8V+gDnZFWCYbXk0t7j8TouxpTRitEqay7185nRMJzy944GOqYBY8xl9SJRYnHrcbjUKKuflRGK2QFJdePueIM9WZT5a4QnxukYNBft4hOnXMY2lj74bxqjS3KUjrer4bKeG351CAaXC1/mPth32VkKnrg/ntn1cL/DGgDBKed7+m1hcBq9t+4BAeZTT3WZzLrM4DJ1lSOQIfdByIF2/RlNF2YBjBpI2jM0nRFwUhZeoh0r0QVS7NJvdSV3zzju3GPVt0w8qvxJ0PuDfg==')


#     for x in bucket.objects.all():
#         if f'Preprocessing/{image_folder}' in x.key:
#             images.append(x.key)

#     images.sort(key=lambda x: x[1])
#     print(images[0])

    # for image in images:
    #     save_path = os.path.join(f'local_images', image_folder, f'{}.png')
    #     s3_client.download_file('digpath-data', 'image', 'FILE_NAME')
        
    #     # df = pd.read_csv(image, header=None)
    #     df = pd.read_csv(image)
    #     ds_array = df.to_numpy()
    #     x_size = ds_array.shape[0]
    #     ds_array = ds_array.reshape((x_size, x_size, 3))
    #     plt.imshow(ds_array, vmin=0, vmax=255, cmap="gray")
    #     plt.show()
    #     # save_path = os.path.join(f'local_images', image_folder, f'{image}.png')
    #     # plt.imsave(save_path, ds_array)
    
