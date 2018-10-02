## This directory containing data collected by the RAV while surveying the scene.
- GPSCoords: The GPS waypoints that were visited by each RAV. This contains RecordedGPSCoords (relative to AirSim home position) and RecordedGPSCoordsRelative (relative to NUIG position). Default file name in these directory is RecordedGPSCoordsAgent<agent number>.txt

- JPGImagesWithExif: Processed JPG images collected by the RAV with exif data attached. This directory contains subdirectory named JPGImagesRAV<rav number>. The images recorded from each camera on the RAV are recorded in the subdirectories Camera<camera number>. Within each of these directory are images named image_<image number>.jpg.

- PNGImages: Raw png images gathered by RAVS. This directory contains subdirectory named ImagesRAV<rav number>. The images recorded from each camera on the RAV are recorded in the subdirectories Camera<camera number>. Within each of these directory are images named image_<image number>.jpg.