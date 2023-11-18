*ReadVector.py*  
    Read A shapefile specified by the file_name 
    Show some basic info like feature counts and fields counts.   
    printing the fields name then ask a *index* of a field to display its property.   
    If input index is emptySpace ,then show all fileds.  
    
```python

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
```
**Usage**: *show specific field* 
```bash
$ python read.py
enter the path: KunmingProjectedUtm.shp
Number of feature:  14
Number of fields: 8

['dt_adcode', 'dt_name', 'ct_adcode', 'ct_name', 'pr_adcode', 'pr_name','cn_adcode', 'cn_name']
input the field index you wanna show 1
Feature 0 dt_name 五华区
Feature 1 dt_name 盘龙区
Feature 2 dt_name 官渡区
Feature 3 dt_name 西山区
Feature 4 dt_name 东川区
Feature 5 dt_name 呈贡区
Feature 6 dt_name 晋宁区
Feature 7 dt_name 富民县
Feature 8 dt_name 宜良县
Feature 9 dt_name 石林彝族自治县
Feature 10 dt_name 嵩明县
Feature 11 dt_name 禄劝彝族苗族自治县
Feature 12 dt_name 寻甸回族彝族自治县
Feature 13 dt_name 安宁市

```
**Usage**: *show all fields*
```bash
$ python read.py
enter the path: KunmingProjectedUtm.shp
Number of feature:  14
Number of fields: 8
['dt_adcode', 'dt_name', 'ct_adcode', 'ct_name', 'pr_adcode', 'pr_name', 'cn_adcode', 'cn_name']
input the field index you wanna show  
Feature 0 dt_adcode 530102
Feature 1 dt_adcode 530103
Feature 2 dt_adcode 530111
Feature 3 dt_adcode 530112
Feature 4 dt_adcode 530113
Feature 5 dt_adcode 530114
Feature 6 dt_adcode 530115
Feature 7 dt_adcode 530124
Feature 8 dt_adcode 530125
Feature 9 dt_adcode 530126
Feature 10 dt_adcode 530127
Feature 11 dt_adcode 530128
Feature 12 dt_adcode 530129
Feature 13 dt_adcode 530181
Feature 0 dt_name 五华区
Feature 1 dt_name 盘龙区
Feature 2 dt_name 官渡区
Feature 3 dt_name 西山区
Feature 4 dt_name 东川区
Feature 5 dt_name 呈贡区
Feature 6 dt_name 晋宁区
Feature 7 dt_name 富民县
Feature 8 dt_name 宜良县
Feature 9 dt_name 石林彝族自治县
Feature 10 dt_name 嵩明县
Feature 11 dt_name 禄劝彝族苗族自治县
Feature 12 dt_name 寻甸回族彝族自治县
Feature 13 dt_name 安宁市
Feature 0 ct_adcode 530100
Feature 1 ct_adcode 530100
Feature 2 ct_adcode 530100
Feature 3 ct_adcode 530100
Feature 4 ct_adcode 530100
Feature 5 ct_adcode 530100
Feature 6 ct_adcode 530100
Feature 7 ct_adcode 530100
Feature 8 ct_adcode 530100
Feature 9 ct_adcode 530100
Feature 10 ct_adcode 530100
Feature 11 ct_adcode 530100
Feature 12 ct_adcode 530100
Feature 13 ct_adcode 530100
Feature 0 ct_name 昆明市
Feature 1 ct_name 昆明市
Feature 2 ct_name 昆明市
Feature 3 ct_name 昆明市
Feature 4 ct_name 昆明市
Feature 5 ct_name 昆明市
Feature 6 ct_name 昆明市
Feature 7 ct_name 昆明市
Feature 8 ct_name 昆明市
Feature 9 ct_name 昆明市
Feature 10 ct_name 昆明市
Feature 11 ct_name 昆明市
Feature 12 ct_name 昆明市
Feature 13 ct_name 昆明市
Feature 0 pr_adcode 530000
Feature 1 pr_adcode 530000
Feature 2 pr_adcode 530000
Feature 3 pr_adcode 530000
Feature 4 pr_adcode 530000
Feature 5 pr_adcode 530000
Feature 6 pr_adcode 530000
Feature 7 pr_adcode 530000
Feature 8 pr_adcode 530000
Feature 9 pr_adcode 530000
Feature 10 pr_adcode 530000
Feature 11 pr_adcode 530000
Feature 12 pr_adcode 530000
Feature 13 pr_adcode 530000
Feature 0 pr_name 云南省
Feature 1 pr_name 云南省
Feature 2 pr_name 云南省
Feature 3 pr_name 云南省
Feature 4 pr_name 云南省
Feature 5 pr_name 云南省
Feature 6 pr_name 云南省
Feature 7 pr_name 云南省
Feature 8 pr_name 云南省
Feature 9 pr_name 云南省
Feature 10 pr_name 云南省
Feature 11 pr_name 云南省
Feature 12 pr_name 云南省
Feature 13 pr_name 云南省
Feature 0 cn_adcode 100000
Feature 1 cn_adcode 100000
Feature 2 cn_adcode 100000
Feature 3 cn_adcode 100000
Feature 4 cn_adcode 100000
Feature 5 cn_adcode 100000
Feature 6 cn_adcode 100000
Feature 7 cn_adcode 100000
Feature 8 cn_adcode 100000
Feature 9 cn_adcode 100000
Feature 10 cn_adcode 100000
Feature 11 cn_adcode 100000
Feature 12 cn_adcode 100000
Feature 13 cn_adcode 100000
Feature 0 cn_name 中华人民共和国
Feature 1 cn_name 中华人民共和国
Feature 2 cn_name 中华人民共和国
Feature 3 cn_name 中华人民共和国
Feature 4 cn_name 中华人民共和国
Feature 5 cn_name 中华人民共和国
Feature 6 cn_name 中华人民共和国
Feature 7 cn_name 中华人民共和国
Feature 8 cn_name 中华人民共和国
Feature 9 cn_name 中华人民共和国
Feature 10 cn_name 中华人民共和国
Feature 11 cn_name 中华人民共和国
Feature 12 cn_name 中华人民共和国
Feature 13 cn_name 中华人民共和国
```


