import arcpy
from net_ops import *

#path = r'C:\Users\Dim\Dropbox\sharing\NTUA\ECE\julie-nick-babis\180_askiseis\Data'
path = r'C:\Users\Dim\Documents\GitHub\GIS_SCRIPTS\Data'
arcpy.env.workspace = path

feature_list = arcpy.ListFeatureClasses()
print feature_list

x = Network_Operations(path)

print 'x is ' + str(x)

airport = r'C:\Users\Dim\Documents\GitHub\GIS_SCRIPTS\Data\ne_50m_airports\ne_50m_airports.shp'
countries = r'C:\Users\Dim\Documents\GitHub\GIS_SCRIPTS\Data\ne_50m_admin_0_countries\ne_50m_admin_0_countries.shp'

outpath = r'C:\Users\Dim\Documents\GitHub\GIS_SCRIPTS\Data\outputs'

arcpy.MakeFeatureLayer_management(airport, 'points_layer')
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "name" = 'Mexico' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'airports_in_mexico')