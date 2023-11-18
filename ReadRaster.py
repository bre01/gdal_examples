import os
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
path_rsimg=input("enter the input filename");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_rsimg=dir_path+"/"+path_rsimg;

dset = gdal.Open(path_rsimg)
### 获得栅格数组尺寸
x_size, y_size, num_band = dset.RasterXSize, dset.RasterYSize, dset.RasterCount  ## 获取影像尺寸、波段数信息
print('xsize: %.0f, ysize: %.0f, num_band: %.0f' % (x_size, y_size, num_band))
### 获得波段数组
print(str(dset.RasterCount)," bands");
num=input("input the band you wanna show")
num=int(num)
band = dset.GetRasterBand(num)        ### 获取影像某一个波段
band_array = band.ReadAsArray()     ### 将影像读入为np.array()格式
print('shape of array:', band_array.shape)
### 获得地理转换参数
geo_trans = dset.GetGeoTransform()  ### 获取地理转换参数：（左上角坐标x, 像元宽度，行旋转参数，左上角坐标y, 列旋转参数，像元高度）
print('geo_transform:', geo_trans)
### 获得投影信息
proj = dset.GetProjection()         ### 获取影像投影
print('projection:', proj)
plt.figure()
plt.imshow(band_array, vmax=4000, vmin=0, cmap='gray')
plt.show();
