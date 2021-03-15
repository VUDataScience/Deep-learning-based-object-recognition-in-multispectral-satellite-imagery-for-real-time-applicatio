import numpy as np
import pandas as pd
from shapely.wkt import loads as wkt_loads
import csv


GS_s = pd.read_csv('Annotations/grid_sizes_125.csv', names=['ImageId', 'Xmin', 'Xmax', 'Ymin', 'Ymax'], skiprows=1)
DF_s = pd.read_csv('Annotations/combined_polygons_125.csv')
img_size = 1300
annotations_dir = 'Annotations/'

def _get_xmin_xmax_ymin_ymax_spacenet(grid_sizes_panda, imageId):
    xmin, xmax, ymin, ymax = grid_sizes_panda[grid_sizes_panda.ImageId == imageId].iloc[0, 1:].astype(float)
    return (xmin,xmax, ymin, ymax)


def _convert_coordinates_to_raster_spacenet(coords, img_size, xyminmax):
    Xmin, Xmax, Ymin, Ymax = xyminmax
    H, W = img_size
    coords[:, 1] = H - (coords[:, 1] - Ymin)/(Ymax-Ymin)*H
    coords[:, 0] = (coords[:, 0] - Xmin)/(Xmax-Xmin)*W
    coords_int = np.round(coords).astype(np.int32)
    return coords_int


def _get_polygon_list(wkt_list_pandas, imageId, cType):
    df_image = wkt_list_pandas[wkt_list_pandas.ImageId == imageId]
    multipoly_def = df_image[df_image.ClassType == cType].MultipolygonWKT
    polygonList = None
    if len(multipoly_def) > 0:
        assert len(multipoly_def) == 1
        polygonList = wkt_loads(multipoly_def.values[0])
    return polygonList


def _get_and_convert_contours_spacenet(polygonList, raster_img_size, xyminmax):
    perim_list = []
    interior_list = []
    if polygonList is None:
        return None
    for k in range(len(polygonList)):
        poly = polygonList[k]
        perim = np.array(list(poly.exterior.coords))
        perim_c = _convert_coordinates_to_raster_spacenet(perim, raster_img_size, xyminmax)
        if not any(np.array_equal(perim_c, x) for x in perim_list):
            perim_list.append(perim_c)
            for pi in poly.interiors:
                interior = np.array(list(pi.coords))
                interior_c = _convert_coordinates_to_raster_spacenet(interior, raster_img_size, xyminmax)
                interior_list.append(interior_c)
    return perim_list, interior_list


if __name__ == '__main__':
    raster_size = (img_size, img_size)
    class_type = 1
    for i in range(0,125):
        imageId = "img{x}".format(x=i+1)
        ann_file_name = annotations_dir + imageId + '_coordinates.csv'

        with open(ann_file_name, mode='w') as ann_file:
            coords_writer = csv.writer(ann_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
            coords_writer.writerow(['vehicle_coordinates'])
            xyminmax = _get_xmin_xmax_ymin_ymax_spacenet(GS_s, imageId)
            polygon_list = _get_polygon_list(DF_s, imageId, class_type)
            perim_list, interior_list = _get_and_convert_contours_spacenet(polygon_list, raster_size, xyminmax)
            print (imageId)
            for car in perim_list:
                row = [str(point) for point in car]
                coords_writer.writerow(row)

