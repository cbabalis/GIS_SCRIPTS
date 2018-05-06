import arcpy
from net_ops import *

path = r'C:\Users\Dim\Dropbox\sharing\NTUA\ECE\julie-nick-babis\180_askiseis\Data'
arcpy.env.workspace = path

feature_list = arcpy.ListFeatureClasses()
print feature_list

x = Network_Operations(path)

print 'x is ' + str(x)