#!/usr/bin/env python
# coding: utf-8

# https://hatarilabs.com/ih-en/how-to-convert-a-raster-to-contours-with-python-and-gdal-tutorial

# This code is how we can convert dem to contour line 20 meters

# Protogeros Michalis Geographer


import numpy as np
from osgeo import osr
from osgeo import ogr
from osgeo import gdal


# open tif file and select band

# In[16]:


rasterDs = gdal.Open("corfu_dem.tif")
rasterBand = rasterDs.GetRasterBand(1)
proj = osr.SpatialReference(wkt=rasterDs.GetProjection())


# get elevation as a numpy array

# In[17]:


elevArray = rasterBand.ReadAsArray()


# In[23]:


print(elevArray[:4,:4])


# difine not a number

# In[24]:


demNan = -32766


# GET DEM MAX AND MIN

# In[25]:


demMax = elevArray.max()
demMin = elevArray[elevArray!= demNan].min()
print("Max elevation is..... ",demMax,"Min elevation is....",demMin)


# In[31]:


contourPath = ("contours.shp")
contourDs = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource(contourPath)

#define layer name and spatial 
contourShp = contourDs.CreateLayer('contour', proj)

#define fields of id and elev
fieldDef = ogr.FieldDefn("ID", ogr.OFTInteger)
contourShp.CreateField(fieldDef)
fieldDef = ogr.FieldDefn("elev", ogr.OFTReal)
contourShp.CreateField(fieldDef)

#Write shapefile using noDataValue
#ContourGenerate(Band srcBand, double contourInterval, double contourBase, int fixedLevelCount, int useNoData, double noDataValue, 
#                Layer dstLayer, int idField, int elevField
gdal.ContourGenerate(rasterBand, 20.0, 900.0, [], 1, -32766., 
                     contourShp, 0, 1)

contourDs.Destroy()


# In[ ]:





# In[ ]:




