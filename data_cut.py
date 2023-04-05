import czifile
import numpy as np
import tifffile

czi_data = czifile.imread(r'D:\2PM_2023\segmentation\data\2023_03_03__115-1.czi')

print(czi_data.shape)

img = czi_data[0,0,0,0,1,17000:17000+512,12000:12000+512,0]
print(img.shape)

# 将CZI数据保存为TIFF文件
# tifffile.imwrite(r'D:\2PM_2023\segmentation\data\microglia.tif', czi_data)

tifffile.imwrite(r'D:\2PM_2023\segmentation\data\microglia_cut1.tif', img)
# czifile.imsave(r'D:\2PM_2023\segmentation\data\microglia.tif', czi_data)