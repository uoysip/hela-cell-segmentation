# HeLa Cell Image Segmentation

Using the [U-Net Convolutional Network](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) and Keras to perform image segmentation on HeLa cells.

<p align="center">
  <img src="https://i.imgur.com/ZxUefqK.png" alt="U-Net Architecture" width="706" height="461"/>
</p>

## Requirements

### Python Dependencies

Tested with Python 3.7:

```bash
pip3 install keras tensorflow numpy scikit-image
```

### Dataset

**Note:** This repository already contains the required images/labels for training.

The dataset was acquired from the [Cell Tracking Challenge website](http://celltrackingchallenge.net/2d-datasets/ "Cell Tracking Challenge"), the training dataset [DIC-C2DH-HeLa.zip](http://data.celltrackingchallenge.net/training-datasets/DIC-C2DH-HeLa.zip "DIC-C2DH-HeLa.zip dataset") was used on the U-Net model.


## Usage

Run the `main.py` file or use the `train.ipynb` file with Jupyter Notebook (Recommended). The predicted images are within `./data/results/`

## Credits

Based on the [U-Net implementation by zhixuhao](https://github.com/zhixuhao/unet "Github - zhixuhao unet").

## License

This project is released under the MIT license, see the LICENSE file for details.
