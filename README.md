# ROCSAFE Technology Demo Code

ROCSAFE (**R**emotely **O**perated **CBRNe** **S**cene **A**ssessment and **F**orensic **E**xamination) is an EU horizon 2020 project that contains Aritificial Intelligence components. This repo contains:

- A release of a virtual environment which has developed for the project for simulation purposes. This was written using Unreal Engine version 4.16 and can be downloaded from the [releases page](https://github.com/NUIG-ROCSAFE/CBRNeVirtualEnvironment/releases).
- A user interface and associated code which allows the user to use/test the technologies developed.
- A data gathering pipeline which can be used to generate images and other data related in the scene and store them in a pre-defined format


## Requirements

In order to ensure that the code runs without issues, please check you have the following requirements:

- Windows 10+
- Python 3.5+
- Pip 18.0+
- R 3.5.0 +
- RStudio 1.0.153+
- JRE 1.8
- ElasticSearch 6.3.0
- BLOG (bayesian reasoning programming language, can be downloaded [here](https://bayesianlogic.github.io/pages/download.html)
- MaskRCNN (https://github.com/matterport/Mask_RCNN)

**Note:** This software was developed and tested using Windows 10, with Linux support planned. If you would like to use a virtualenv/pipenv rather than your base installation of python, you will need to modify start_up.bat and one_drone.bat, two_drone.bat, three_drone.bat.

We recommend the following config:

- Windows 10
- Python 3.5
- Pip 18.0
- R 3.5.0
- RStudio 1.0.153
- JRE 1.8
- ElasticSearch 6.3.0
- BLOG 0.9

## How to use the user interface
In Rstudio, once you have run Dependencies.R, open server.R. In the top right corner of the editor click run app.

## What's going on under the hood

## How can I extend/modify the code in this repo 
