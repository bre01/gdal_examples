#KunmingProjectedUtm.shp
import os 
from osgeo import ogr
path_kunming=input("enter the input filename");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_kunming=dir_path+"/"+path_kunming;
path_kunming_out_1=input("enter the output filename");
dir_path = os.path.dirname(os.path.realpath(__file__))
path_kunming_out_1=dir_path+"/"+path_kunming_out_1;
print(path_kunming_out_1)


field_name = 'dt_name'
in_ds = ogr.Open(path_kunming, 0)    # 0是只读，1是可写
in_layer = in_ds.GetLayer()             # 获取矢量文件图层Layer
## 定义写出文件
driver = ogr.GetDriverByName('ESRI Shapefile')   ## 文件驱动（用于写出文件）
ds_out = driver.CreateDataSource(path_kunming_out_1)  ## 创建数据源DataSource
layer_out = ds_out.CreateLayer('kunming_districts_dtname', geom_type=ogr.wkbPolygon, srs=in_layer.GetSpatialRef())
field_defn = ogr.FieldDefn(field_name, ogr.OFTString)   ## 定义属性字段
#layer_out.CreateField(field_defn)    ## 在写出图层中新建属性字段
# fea_defn = layer_out.GetFeature(0).GetDefnRef()    ## layer_out没有要素，故.GetFeature(0)会报错
fea_defn = layer_out.GetLayerDefn()  ## 获得要素定义（即图层定义）
### 创建要素（将复制‘昆明市边界_wgs84.shp’文件中要素)
fields = []
num_field = in_layer.GetFeature(0).GetFieldCount()   ## 统计属性个数
fea = in_layer.GetFeature(0)
for i in range(0, num_field):
    field = fea.GetFieldDefnRef(i).name
    fields.append(field)

print()
print(fields)



field_index=input("input the field index you wanna save ")
#field_name = 'dt_name'


if field_index == " ":
    for i in range(num_field):
        field_name = fields[i]
        field_defn = ogr.FieldDefn(field_name, ogr.OFTString) 
        layer_out.CreateField(field_defn)    ## 在写出图层中新建属性字段

    for i in range(in_layer.GetFeatureCount()):
        in_fea = in_layer.GetFeature(i)
        in_geo = in_fea.geometry()
        fea_out = ogr.Feature(fea_defn)
        fea_out.SetGeometry(in_geo)
        print(2)
        for h in range(num_field):
            field_name = fields[h]
            #layer_out.CreateField(field_defn)    ## 在写出图层中新建属性字段
            field_value = in_fea.GetField(field_name)
            fea_out.SetField(h, field_value)
        layer_out.CreateFeature(fea_out)
    print("write all fields successfully")
else:
    layer_out.CreateField(field_defn)    ## 在写出图层中新建属性字段
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
    print("write ",field_name," field successfully")
ds_out = None
#KunmingProjectedUtm.shp