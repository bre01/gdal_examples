
import os
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
path_rsimg=input("enter the input filename");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_rsimg=dir_path+"/"+path_rsimg;

dset = gdal.Open(path_rsimg)

x_size, y_size, num_band = dset.RasterXSize, dset.RasterYSize, dset.RasterCount  
print('xsize: %.0f, ysize: %.0f, num_band: %.0f' % (x_size, y_size, num_band))
dset.GetGeoTransform()
print(str(dset.RasterCount)," bands");
num=input("input the band you wanna save")
num=int(num)
band = dset.GetRasterBand(num)        
band_array = band.ReadAsArray()     
print('shape of array:', band_array.shape)

geo_trans = dset.GetGeoTransform()  
print('geo_transform:', geo_trans)

proj = dset.GetProjection()         
print('projection:', proj)






out_name=input("enter the output filename");
out_dir= os.path.dirname(os.path.realpath(__file__))
driver = gdal.GetDriverByName('GTiff')
out_name=out_dir+"/"+out_name;
dset_mosaic = driver.Create(out_name, 
                            xsize =x_size,
                            ysize = y_size,
                            bands=1,
                            eType=gdal.GDT_Int16)
dset_mosaic.SetGeoTransform(dset.GetGeoTransform())
dset_mosaic.SetProjection(dset.GetProjection())
band=dset_mosaic.GetRasterBand(1)
band.WriteArray(band_array)
print("done")
