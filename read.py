path=input("enter the path: ")
import os 
from osgeo import ogr
dir_path = os.path.dirname(os.path.realpath(__file__))
path_kunming=dir_path+"/"+path;
ds = ogr.Open(path_kunming, 0)    # 0是只读，1是可写
layer = ds.GetLayer(0)            # 获取矢量文件Layer
num_fea = layer.GetFeatureCount()   ## 统计要素个数
print('Number of feature: ', num_fea)
num_field = layer.GetFeature(0).GetFieldCount()   ## 统计属性个数
print('Number of fields:', num_field)




fields = []
fea = layer.GetFeature(0)
for i in range(0, num_field):
    field = fea.GetFieldDefnRef(i).name
    fields.append(field)

print()
print(fields)

field_index=input("input the field index you wanna show ")
#field_name = 'dt_name'

#fea = layer.GetFeature(0)
#print('Filed value:\n', fea.GetField(field_name))
if(field_index==" "):
  for i in range(num_field):
    field_name=fields[i];
    for i in range(layer.GetFeatureCount()):   ##
      fea = layer.GetFeature(i)
      print('Feature '+str(i)+" "+ field_name+" "+ fea.GetField(field_name))
else:
  field_name=fields[int(field_index)]
  for i in range(layer.GetFeatureCount()):   ##
    fea = layer.GetFeature(i)
    print('Feature '+str(i)+" "+ field_name+" "+ fea.GetField(field_name))

    
  




### 获得所有要素的字段值
#for i in range(layer.GetFeatureCount()):   ##
#  fea = layer.GetFeature(i)
#  print('Feature '+str(i)+" "+ field_name+" "+ fea.GetField(field_name))