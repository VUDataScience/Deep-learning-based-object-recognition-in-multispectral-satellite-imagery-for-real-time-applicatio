## Deep learning based object recognition in multispectral satellite imagery for real-time applications

### Dataset

The dataset used in these experiments was created from an open-source raw satellite imagery database SpaceNet with
high-resolution imagery taken by DigitalGlobe WorldView-3 satellite.
A total of 125 high resolution (30cm per pixel) RGB-PanSharpen geotiffs satellite images equivalent to 50 km2
AOI of Paris, Shanghai, Las Vegas, and Khartoum were used for this dataset. 

A total of 350 hours of professional annotation work has been conducted to prepare a high-quality set with 80,316
labelled objects. Images were annotated using QGIS geospatial imagery software. Labelling and polygon coordinate
generation has been manually completed by multiple professional annotators and quality cross-checked.
We are publishing our in-house developed, proprietary dataset with labelled polygons online to enable further
development in this field.

### Repository structure

- Annotations directory
    - img[1-125]_coordinates.csv - every file contains coordinates of objects. Every line holds a polygon of
      coordinates for single vehicle. Coordinates are relative to image top left corner. Example:
      ```
      [491 784],[510 777],[515 782],[496 789],[491 784]
      ```

    - combined_polygons_125.csv - file contains all objects coordinates for every image. Single line represents:
      ```
      Image ID, Class type, WKT multipolygon.
      ```
      Well-known text (WKT) is a text markup language for representing vector geometry objects on a map.
      Objects are described in WGS84 reference coordinate system.

    - grid_sizes_125.csv - file holds data about images and describes maximum and minimum coordinates for every image.
      Single line represents: 
      ```
      Image ID, X minimum, X maximum, Y minimum, Y maximum
      ```
      Objects are described in WGS84 reference coordinate system.

- Images directory - it contains 125 satellite images (size 1300x1300 px, 30cm per pixel). 
