import logging
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import io
import pandas as pd
import numpy as np


def upload_file_to_s3(ds_array, file_name):
    """Upload a file to an S3 bucket

    :param ds_array: Image/File to upload
    :param file_name: Uploaded file name
    :param bucket: Bucket to upload to
    :return: True if file was uploaded, else False
    """

    folder = 'Preprocessing'

    # A low-level client representing Amazon Simple Storage Service (S3)
    s3_client = boto3.client('s3',
                            aws_access_key_id='ASIAWJQCCJF2LQ5AACMK',
                            aws_secret_access_key='eQvkBpvVZWubkZaa2mw6dy/z4RmtMfqD0L7BidD9',
                            aws_session_token='IQoJb3JpZ2luX2VjECgaCXVzLWVhc3QtMSJIMEYCIQCUcL8A6x12qc6ikPT1Un5g4ecwlOQiORRzs/zram1FoQIhAJtCX3utLBnSXc6nGTJiK8eDXusN/oZuyq/NzBqI5fRJKokDCCEQABoMNDMyNzIyMjk5MjUyIgx0uzNI6q1yQQAC46kq5gLvq8IqU5/zmnnQ1cxCycQP2PxGjo5rk0LFLTf7cK6sFMf61qCTL0HkdOfhrYr5jH9PGA9/20fQfLrEEzSndIPz6SvZzQnX5ffB5fkpmifmM0rk7iqGaRxgiKa9/PN0xVDMcOWDIWBKfUe36O6jmjHF4PACAGxPiD5ZWapIk1lm3C/fkASUAvAgCVqXX+sTXvnYGs0HNBuPJ7ZGpjuT3HQIrwDM2lPnH8BtmD+3KGWxKPPt1mJG2ezkJIBLZqo/Al4AYOocVL7QHqPYROVRbEz2mOsqxVsUXgCkqrG+oiQUAulezRVXJNYsimkaZ78Rc8dz39QdOLQUxDagu1SryLqnWzeXOWjAL8Q+AW8PfvWLRF/7Ea5Bi/yOITSOrZlSOP8pcDEVnQFDov80odHDU5yLBHXGzWcJklUuZQ8Bee7CuyrKWcD/Xj0Uc2CKaYM6EI9R7/tVdrxeq5bUmOhKwL40lMoI6LxkMLnLiY4GOqUBtmtlc+heq1QU1FyZCF0cU72S3VkOuHkSOCk/u3NK/G5Ry04ZE/BQsb+YXRFD48tdyro1RGRMFidadP+x9pLzQsUfmU765TqfG0y6TpP3wPO/Pp2MuW461DLJhbOw3nT7H76TbgghK5W1h8X9ARnGB3yEPB5bZcv0zgtuyYG4Knc8gylKGYKvkKg2AK1nhj0DWKULqRqNJbOOkMsgNcL8KjeQRjXn')

    try:
        # response = s3_client.upload_file(Filename=ds_array, Bucket=bucket, Key=f'{folder}/{file_name}')
        
        # df = pd.DataFrame(ds_array.reshape((-1, ds_array.shape[-1])),
        #                     index=pd.MultiIndex.from_product([range(ds_array.shape[0]), range(ds_array.shape[1])]))

        x_size = ds_array.shape[0]
        r = ds_array[0:x_size, 0:x_size, 0]
        g = ds_array[0:x_size, 0:x_size, 1]
        b = ds_array[0:x_size, 0:x_size, 2]
        rgb_i = np.concatenate([r, g, b], axis=1)

        df = pd.DataFrame(rgb_i)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer)

        # s3_client.upload_file(Filename=csv_buffer.getvalue(), Bucket='digpath-data', Key=f'{folder}/{file_name}')

        s3_client.put_object(Body=csv_buffer.getvalue(), Bucket='digpath-data', Key=f'{folder}/{file_name}')
        print(file_name, "uploaded successfull")

    except ClientError as e:
        logging.error(e)
        return False
    except NoCredentialsError:
        print("Credentials not available or expired")
        return False

    return True



    ## Then after loading the file, using index_col=[0,1], convert to array using:

# >>> df = pd.read_csv(filename, header=None, index_col=[0,1])
# >>> np.array(df.agg(list, 1).groupby(level=0).agg(list).tolist())