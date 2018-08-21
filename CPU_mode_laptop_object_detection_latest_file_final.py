import os,time

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import clear_output
import matplotlib.image as mpimg
from PIL import Image
from pathlib import Path
import datetime
from PIL import Image,ImageTk
import io
import tkinter
import subprocess



# Root directory of the project
ROOT_DIR = os.path.abspath("../")
print(ROOT_DIR)

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
print(os.path.abspath(visualize.__file__))
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
import coco

#%matplotlib inline 

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'gas cylinder',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'gas cylinder', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']
               

########################################################### RAV camera image path here IMAGE_DIR #########################################      
IMAGE_DIR = './PythonCode/PythonClientGPSMapping/GPSMappings/Images/Images1/Camera1'
path_to_watch = IMAGE_DIR
before = [f.name for f in os.scandir(path_to_watch)]
#path_to_watch_2 = IMAGE_DIR_2
#before_2 = [f.name for f in os.scandir(path_to_watch_2)]

to_be_analysed = []
analysed =[]
info_list = []
print("monitoring folder ",IMAGE_DIR)
while 1:
    time.sleep (10)
    after = [f.name for f in os.scandir(path_to_watch)]
    added = [f for f in after if not f in before]
    
    
    if added: 
        print("Images Added: ", ", ", list(added))
        # i=0
        for file in os.listdir(IMAGE_DIR):
            all_files = [os.path.join(os.path.dirname(os.path.abspath(__file__)),IMAGE_DIR,i) for i in os.listdir(IMAGE_DIR)] #path to find latest file has to be in a different format with \\ rather than \ in DEFAULT IMAGE_DIR
            to_be_analysed = [file for file in all_files if not file in analysed]
            #Will only check for latest file if there any files to be analysed
            if to_be_analysed:
                latest_image_path = max(to_be_analysed , key=os.path.getctime) #taking the latest file in for detection 
                print("latest_image_path is ",latest_image_path )
                #time.sleep(5)
                image_name = os.path.basename(latest_image_path)
                converted_files = os.listdir(os.path.join(ROOT_DIR, "Converted_images"))
                   
                while True:
                    try:
                        im = Image.open(os.path.join(IMAGE_DIR, image_name))
                        break
                    except PermissionError:
                        continue
                    break
                rgb_im = im.convert('RGB')
#        ###########################################################Raw_image path here################################################## 
#                    Pass in the same paths  to both rgb_im_save and skimage.io.imread
                rgb_im.save('./RCode./ShinyApp/Data/Images/Raw.jpg')
                image = skimage.io.imread('./RCode/ShinyApp/Data/Images/Raw.jpg')
                results = model.detect([image], verbose=1) # Visualize results
                clear_output()
                print("Printing results")
                r = results[0]
                visualize.display_instances(ROOT_DIR, image_name, image, r['rois'], r['masks'],r['class_ids'], class_names, r['scores'])
                converted_image_path= (os.path.join(ROOT_DIR,"Converted_images\masked_"+image_name))
                converted_image = Image.open(converted_image_path)
    ##############################################################Processed image path here ###########################################            
                converted_image_rgb = converted_image.convert('RGB')
                rgb_im.save('./RCode/ShinyApp/Data/Images/mostRecentImageRaw.jpg')
                converted_image_rgb.crop((215, 203, 1424, 1412)).save('./RCode/ShinyApp/Data/Images/mostRecentImageProcessed.jpg')
                #print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                print(datetime.datetime.now())
                # Appending classnames, probabilities to list
                info_list.append([class_names[i] for i in r['class_ids']])
                info_list.append(r['scores'])
                info_list.append(image_name)
                info_list.append(str(datetime.datetime.now()))
                filename = 'logs_new.txt'
                buffsize=1
                file = open(filename,"a+",buffsize)
                for item in info_list:
                    file.write("%s\n" % item) 
                file.write("\n")
                analysed.append(latest_image_path)    

			# i=i+1   
	#root.mainloop()
    before = after
    
