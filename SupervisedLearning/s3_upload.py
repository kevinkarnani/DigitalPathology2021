import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import logging

def upload_file_to_s3(file_name):
    """Upload a file to an S3 bucket

    :param file_name: file name of image to upload
    :return: True if file was uploaded, else False
    """

    folder = 'Preprocessing'

    # A low-level client representing Amazon Simple Storage Service (S3)
    s3_client = boto3.client('s3',
                            aws_access_key_id='ASIAWJQCCJF2KI2SKIPX',
                            aws_secret_access_key='9Tpaq/t6rLe2wQ2N9kyuktMvYnfcqkPWVrExsuzp',
                            aws_session_token='IQoJb3JpZ2luX2VjEH4aCXVzLWVhc3QtMSJHMEUCIG4SVQCpUZChaC0Rcx6QJfDZ/BBUGONjjLRzY3pqORQIAiEAicGt8/rDnq+uniyNbDcfkJfauEuHoOQwjGpC6yZ+kRcqkwMIlv//////////ARAAGgw0MzI3MjIyOTkyNTIiDLAuXfMTnMPn6ydxOyrnAurBtyLB/prghseE2u7spx8Vb6lNsRF87hWZCTYbCri200jtnkWi/Gp5v+GpDN4Wv35bpU5ja+CBSxIjlpq3NMbmuXsq90fHC2gk8ejQasD3aR86BCUtWx4LgW7RBBzcotbpLtV+b9DE9eaW74HTYA8mKCrB5jsqVHX3V9RJJwpGyWNWfJW0eoNfBIKJf9nBhRu2sdCOdj+BXY1atPMk5ltr7qUNzOb08toZkJyqFKzTLEJbgjwoL/ivr12rm3AvMmkrnvRLbDU1vBNz16JvUoT59SP3iE3DalCEtFJR84LVimiSUxeHx9sc4mpcT0MFXSlw+UHTq4SCh7UPfirioVlV2vigfIsJ92jDLmyN2oxKxwkfMfu3ICeO7vRE3kss5Lo75ebrWTMI7gn57qRkEUXB45rt+aev1ZGjm390yf6ZCh/N4zTjegjsXKlJMWxkwtJMbHbUMExCzE6AmdHvweABaDZpSpzGMMDzjI8GOqYBMoA8DfKYMCQglWU/8RScI1xEzH/nwt2fCB7O2L6G+oumABTQNXtc4bRiVRoPV1w1EUPXD8lWLZJPqgwlvox64x778AWw41UDOProGbwJ97prWp9lRlCiPe8WJD31H7X3EjDbi+zXacGxkTvj6VRWticG1Y1SVxw3VC3ER7lxbbELCgVj9ynzLpkaDqqbWckcMlz9QTWuIOcKawdQKPbd1CB2ks3CMw==')
    # Upload the file
    try:
        s3_client.upload_file(Filename=f'local_images/{file_name}', Bucket='digpath-data', Key=f'{folder}/{file_name}')
        print(file_name, "uploaded successfully")
    except ClientError as e:
        logging.error(e)
        return False
    except NoCredentialsError:
        print("Credentials not available or expired")
        return False

    return True

# def upload_file_to_s3(ds_array, file_name):
#     """Upload a file to an S3 bucket

#     :param ds_array: Image/File to upload
#     :param file_name: Uploaded file name
#     :param bucket: Bucket to upload to
#     :return: True if file was uploaded, else False
#     """

#     folder = 'Preprocessing'

#     # A low-level client representing Amazon Simple Storage Service (S3)
#     s3_client = boto3.client('s3',
#                             aws_access_key_id='ASIAWJQCCJF2M4DSCAOJ',
#                             aws_secret_access_key='ZdbQLhsa/K7mNyUgHLa6fziBKj1J0phNo/gSaSR6',
#                             aws_session_token='IQoJb3JpZ2luX2VjEB4aCXVzLWVhc3QtMSJHMEUCIQDuYEWSY2S5E6sR/Hjcf43m8CqOSFnFWIDYQpsm6VOMUwIgDL74ub56nR6shT5JfNkFvPOe1yXzBlG6pvp1g6fSIZ8qigMINxAAGgw0MzI3MjIyOTkyNTIiDAzJlf3vf5vcoo42pyrnAkObLWWmx2VEm5/VtwadyN9KDR0enQqE/ddbrlfq1Kv9XmqswqQXqNxEmjqYD8FXFr3SoI6iqAEOcf5k3ebBM+rFTMHeS/Lad2n4X9WdzeXQpXqqCcRs5Z1wG3wUojAXCS1O9inAi60QMsqarri4NANGsKcNNP7rUiwgnLw4C7BCpoK0w/uHC00mQbkEniBlIrfxrlDGSZbyKDJOrxi5h8KSs9OA9ELnt7sR13i4OJ09MHuRwL26AE2ex6hPb0JwvQOk8Twjio1Xmh169F3cLqMboPoQqavKhwK5P4hR8US00V2SI34GL03ifN940/XdhKtFfiphxBJSHh3oNV5bd25Nbj2BOYn03L/j8zMasp7SWk9oaOtqpGHieuDm6bS/mUc+gAtDLuM6a49MfhA49XM/3hvKMs/JW8xhnRqWBJS+LC+qzOqKOAaHFN8V+gDnZFWCYbXk0t7j8TouxpTRitEqay7185nRMJzy944GOqYBY8xl9SJRYnHrcbjUKKuflRGK2QFJdePueIM9WZT5a4QnxukYNBft4hOnXMY2lj74bxqjS3KUjrer4bKeG351CAaXC1/mPth32VkKnrg/ntn1cL/DGgDBKed7+m1hcBq9t+4BAeZTT3WZzLrM4DJ1lSOQIfdByIF2/RlNF2YBjBpI2jM0nRFwUhZeoh0r0QVS7NJvdSV3zzju3GPVt0w8qvxJ0PuDfg==')

#     try:
#         # response = s3_client.upload_file(Filename=ds_array, Bucket=bucket, Key=f'{folder}/{file_name}')
        
#         # df = pd.DataFrame(ds_array.reshape((-1, ds_array.shape[-1])),
#         #                     index=pd.MultiIndex.from_product([range(ds_array.shape[0]), range(ds_array.shape[1])]))

#         x_size = ds_array.shape[0]
#         r = ds_array[0:x_size, 0:x_size, 0]
#         g = ds_array[0:x_size, 0:x_size, 1]
#         b = ds_array[0:x_size, 0:x_size, 2]
#         rgb_i = np.concatenate([r, g, b], axis=1)

#         df = pd.DataFrame(rgb_i)
#         csv_buffer = io.StringIO()
#         df.to_csv(csv_buffer)

#         # s3_client.upload_file(Filename=csv_buffer.getvalue(), Bucket='digpath-data', Key=f'{folder}/{file_name}')

#         s3_client.put_object(Body=csv_buffer.getvalue(), Bucket='digpath-data', Key=f'{folder}/{file_name}')
#         # print(file_name, "uploaded successfull")

#     except ClientError as e:
#         logging.error(e)
#         return False
#     except NoCredentialsError:
#         print("Credentials not available or expired")
#         return False

#     return True



    ## Then after loading the file, using index_col=[0,1], convert to array using:

# >>> df = pd.read_csv(filename, header=None, index_col=[0,1])
# >>> np.array(df.agg(list, 1).groupby(level=0).agg(list).tolist())