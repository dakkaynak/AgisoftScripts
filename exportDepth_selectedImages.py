# This script exports a SCALED DENSE depth map, after MESH stage has been completed, and a scale has been entered.
# It is practically the same as the exportDepth_v4, which exports depth for each "camera" in Agisoft as a compressed tiff file, 
# but it works for a range of cameras specified by the user, instead of all cameras.

# Derya Akkaynak August 28, 2020
import Metashape

chunk = Metashape.app.document.chunk # active chunk
scale = chunk.transform.scale

#############################################################

# Here you can specify the cameras for which you want to export depth
cameraNames = ['T_S03447','T_S03448','T_S03497']

##############################################################


cameraList = list()
for camera in chunk.cameras:
	thisLabel = camera.label
	cameraList.append(thisLabel)
        

for counter, value in enumerate(cameraNames):
	
	cameraLabel = cameraNames[counter]
	index = cameraList.index(cameraLabel)
	camera = chunk.cameras[index]
	depth = chunk.model.renderDepth(camera.transform, camera.sensor.calibration)
	depth = depth * scale
	depth = depth.convert(" ","F16")
	compr = Metashape.ImageCompression()
	compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
	
	####### Remember to update the path below to which you want to export the depth maps ########
	depth.save("/Users/deryaakkaynak/Desktop/depth" + camera.label + ".tif", compression = compr)

						