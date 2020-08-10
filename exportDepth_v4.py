# This script exports a SCALED DENSE depth map, after MESH stage has been completed, and a scale has been entered.

import Metashape


chunk = Metashape.app.document.chunk # active chunk
scale = chunk.transform.scale
for camera in chunk.cameras:
#camera = chunk.cameras[1]
	depth = chunk.model.renderDepth(camera.transform, camera.sensor.calibration)
	depth = depth * scale
	depth = depth.convert(" ","F16")
	#depth = depth.convert("RGB","F16")
	compr = Metashape.ImageCompression()
	compr.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate
	depth.save("/Users/deryaakkaynak/Desktop/depth" + camera.label + ".tif", compression = compr)

						