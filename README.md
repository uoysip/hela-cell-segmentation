# HeLa Cell Image Segmentation

Using the [U-Net Convolutional Network](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) and Keras to perform image segmentation on HeLa cells. Based on the [U-Net implementation by zhixuhao](https://github.com/zhixuhao/unet "Github - zhixuhao unet").

<p align="center">
  <img src="https://i.imgur.com/ZxUefqK.png" alt="U-Net Architecture" width="706" height="461"/>
</p>

## Requirements

### Python Dependencies

Tested with Python 3.7:

```bash
pip3 install keras tensorflow-gpu numpy scikit-image
```

**Note:** replace `tensorflow-gpu` with `tensorflow` if training on the CPU.

### Dataset

**Note:** This repository already contains the required images/labels for training.

The dataset was acquired from the [Cell Tracking Challenge website](http://celltrackingchallenge.net/2d-datasets/ "Cell Tracking Challenge"), the training dataset [DIC-C2DH-HeLa.zip](http://data.celltrackingchallenge.net/training-datasets/DIC-C2DH-HeLa.zip "DIC-C2DH-HeLa.zip dataset") was used on the U-Net model.
