# DEPRECATED

Please consider checking out [Digital Pathology](https://github.com/orgs/Digital-Pathology/repositories) to find the fully functional tools and models.

# DigitalPathology2021

This repo has multiple tools, utilities, and sub-projects that the 2021-2022 Digital Pathology team worked on throughout their senior design series. The material in this repo was largely designed for use on AWS Sagemaker.

## CustomDatasets

Note: This requires using OpenSlideStartupScript for use on AWS Sagemaker Studio.

This is a module for use with PyTorch's models - it offers an interface for accessing very large tif biomedical slides stored on S3. Please see ExampleCustomDatasetUse.ipynb for details on the use of this module.

It was developed using the following resources:
- [PyTorch Custom Datasets](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)
- [Amazon S3 API Documentation](https://s3fs.readthedocs.io/en/latest/api.html)
- [OpenSlide for Python Documentation](https://openslide.org/api/python/)

## OpenSlideStartupScript

This script is for use as a Python instance startup script on AWS Sagemaker Studio Python Notebooks. With respect to using them in development, select the aptly-named startup script upon initializing your notebook instances "adins-test-startup-thing". This is necessary for using OpenSlide, a requirement for using CustomDatasets.
