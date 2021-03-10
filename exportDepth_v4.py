# This script exports a SCALED DENSE depth map, after MESH stage has been completed, and a scale has been entered.
# If no scale is entered, depth maps have relative scale.
# Exported depth maps are the same size as the original images in the chunk, but compressed. 
# This level of compression does not affect the accuracy needed for color correciton.
# Derya Akkaynak

import Metashape
import os

# General setup
app = Metashape.app
chunk = app.document.chunk

# Set output folder
outputFolder = app.getExistingDirectory("Select Output Folder")

# Is the model scaled? If not assign scale of 1
if chunk.transform.scale is None:
    scale = 1
else:
	scale = chunk.transform.scale
		
# Export depth maps for all aligned cameras in chunk
for camera in chunk.cameras:

	# If camera is aligned
    if camera.transform:

        # Determine depth and compression 
        depth = chunk.model.renderDepth(camera.transform, camera.sensor.calibration)
        depth = depth * scale
        depth = depth.convert(" ","F16")
        compression = Metashape.ImageCompression()
        compression.tiff_compression = Metashape.ImageCompression().TiffCompressionDeflate

	    # Save depth to specified folder
        outputPath = os.path.join(outputFolder, camera.label + "_depth" + ".tif")
        depth.save(outputPath, compression = compression)
