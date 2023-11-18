*WriteVector*  
    Read A shapefile specified by the file_name 
    Show some basic info like feature counts and fields counts.   
    printing the fields name then ask a *index* of a field to write into a newly created shapefile
    If input index is emptySpace ,then write all fileds. 



```python 


import os 
from osgeo import ogr
path_kunming=input("enter the input filename: ");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_kunming=dir_path+"/"+path_kunming;
path_kunming_out_1=input("enter the output filename: ");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_kunming_out_1=dir_path+"/"+path_kunming_out_1;
print("Output file: ",path_kunming_out_1)


field_name = 'dt_name'
in_ds = ogr.Open(path_kunming, 0)    
in_layer = in_ds.GetLayer()             

driver = ogr.GetDriverByName('ESRI Shapefile')   
ds_out = driver.CreateDataSource(path_kunming_out_1)  
layer_out = ds_out.CreateLayer('kunming_districts_dtname', geom_type=ogr.wkbPolygon, srs=in_layer.GetSpatialRef())
field_defn = ogr.FieldDefn(field_name, ogr.OFTString)   


fea_defn = layer_out.GetLayerDefn()  

fields = []
num_field = in_layer.GetFeature(0).GetFieldCount()   
fea = in_layer.GetFeature(0)
for i in range(0, num_field):
    field = fea.GetFieldDefnRef(i).name
    fields.append(field)

print()
print(fields)



field_index=input("input the field index you wanna save ")



if field_index == " ":
    for i in range(num_field):
        field_name = fields[i]
        field_defn = ogr.FieldDefn(field_name, ogr.OFTString) 
        layer_out.CreateField(field_defn)    

    for i in range(in_layer.GetFeatureCount()):
        in_fea = in_layer.GetFeature(i)
        in_geo = in_fea.geometry()
        fea_out = ogr.Feature(fea_defn)
        fea_out.SetGeometry(in_geo)
        print(2)
        for h in range(num_field):
            field_name = fields[h]
            
            field_value = in_fea.GetField(field_name)
            fea_out.SetField(h, field_value)
        layer_out.CreateFeature(fea_out)
    print("wrote all fields successfully")
else:
    layer_out.CreateField(field_defn)    
    field_name = fields[int(field_index)]
    for i in range(in_layer.GetFeatureCount()):
        in_fea = in_layer.GetFeature(i)
        in_geo = in_fea.geometry()
        fea_out = ogr.Feature(fea_defn)
        fea_out.SetGeometry(in_geo)
        field_value = in_fea.GetField(field_name)
        print(field_value)
        fea_out.SetField(0, field_value)
        layer_out.CreateFeature(fea_out)
    print("wrote ",field_name," field successfully")
ds_out = None

```

**Usage**: *Save specific field*
```bash
$ python write.py 
enter the input filename: KunmingProjectedUtm.shp
enter the output filename: newOut.shp
Output file :/Users/bre/source/Open-source-GIS-Course/第4章-矢量数据处理-10课时/newOut.shp
['dt_adcode', 'dt_name', 'ct_adcode', 'ct_name', 'pr_adcode', 'pr_name', 'cn_adcode', 'cn_name']
input the field index you wanna save 1
wrote  dt_name  field successfully

```
**Usage**: *show all fields*
```bash
$ python write.py 
enter the input filename: KunmingProjectedUtm.shp
enter the output filename: newOut.shp
Output file :/Users/bre/source/Open-source-GIS-Course/第4章-矢量数据处理-10课时/newOut.shp
['dt_adcode', 'dt_name', 'ct_adcode', 'ct_name', 'pr_adcode', 'pr_name', 'cn_adcode', 'cn_name']
input the field index you wanna save  
wrote  all fields successfully

```

