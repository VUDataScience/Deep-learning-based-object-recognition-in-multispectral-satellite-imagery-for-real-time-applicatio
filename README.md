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

- Images directory 
    - img[1-125].tif - 125 raw satellite images (size 1300x1300 px, 30cm per pixel). 
    - img[1-125].png - original .png images created from .tif files
    - img[1-40]_augmented.png - random brightness changes added to images
    <img src="https://user-images.githubusercontent.com/62398522/77831431-d215b780-7137-11ea-816c-98c3bda77b74.png" width="45%"></img> 
    <img src="https://user-images.githubusercontent.com/62398522/77831432-d215b780-7137-11ea-9a9a-6341ff6fe7e7.png" width="45%"></img> 
    - img[41-80]_augmented.png - random noise added to all 3 channels
    <img src="https://user-images.githubusercontent.com/62398522/77831434-d2ae4e00-7137-11ea-9227-535e9f83f9a7.png" width="45%"></img> 
    <img src="https://user-images.githubusercontent.com/62398522/77831435-d2ae4e00-7137-11ea-874b-4b146f468bb5.png" width="45%"></img> 
    - img[81-125]_augmented.png - random noise added on single channel
    <img src="https://user-images.githubusercontent.com/62398522/77831436-d346e480-7137-11ea-8f64-b5ec530e2513.png" width="45%"></img> 
    <img src="https://user-images.githubusercontent.com/62398522/77831428-d17d2100-7137-11ea-98b0-985cdad591bd.png" width="45%"></img> 
    
- References

This data set was derived from SpaceNet 2, Building Detection v2:

    - SpaceNet on Amazon Web Services (AWS). “SpaceNet 2, Building Detection v2” The SpaceNet Catalog. Last modified October 1st, 2018. Accessed on September 1st 2019. https://spacenet.ai/datasets/

- License
    - Data set is licensed under a <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License.</a>

- Citation Instructions

If you are using data from this repository in a paper, please use the following citation:

    - P. Gudžius, O. Kurasova, V. Darulis and E. Filatovas, "VUDataScience," 2020.
    Available: https://github.com/VUDataScience/Deep-learning-based-object-recognition-in-multispectral-satellite-imagery-for-low-latency-applicatio.
