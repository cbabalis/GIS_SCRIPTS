import arcpy

arcpy.env.workspace = "C:/data"
in_features = "dromoi_florinas.shp"
point_features = "events.shp"
new_feature_class =  "new_lines.shp"
searchRadius = "40 Meters"

arcpy.splitLineAtPoint_management(in_features,
		point_features, new_feature_class, searchRadius)