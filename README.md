# ROCSAFE Technology Demo Code

ROCSAFE (**R**emotely **O**perated **CBRNe** **S**cene **A**ssessment and **F**orensic **E**xamination) is an EU horizon 2020 project that contains Aritificial Intelligence components. This repo contains:

- A release of a virtual environment which has developed for the project for simulation purposes. This was written using Unreal Engine version 4.16 and can be downloaded from the [releases page](https://github.com/ROCSAFE/CBRNeVirtualEnvMultiRobot/releases).
- A user interface and associated code which allows the user to use/test the technologies developed.

This demo is meant to be self-contained and so contains more code than is necessary.

## Requirements

In order to ensure that the code runs without issues, please check you have the following requirements:

- Windows 10+
- Python 3.5+
- Pip 18.0+
- R 3.5.0 +
- RStudio 1.0.153+
- JRE 1.8 (included in the JavaRuntime folder)
- ElasticSearch 6.3.0+ (Inlcluded in the elasticsearch-oss-6.3.0 folder)
- Kibana 6.3.0+ (Inlcluded in the elasticsearch-oss-6.3.0 folder)
- blog (bayesian reasoning programming language, included in BlogRuntime)

**Note:** This software was developed and tested using Windows 10, with Linux support planned. If you would like to use a virtualenv/pipenv rather than your base installation of python, you will need to modify start_up.bat and one_drone.bat, two_drone.bat, three_drone.bat.

We recommend the following config:

- Windows 10+
- Python 3.5
- Pip 18.0
- R 3.5.0
- RStudio 1.0.153
- JRE 1.8
- ElasticSearch 6.3.0

##How to use the user interface

## What's going on under the hood

##How can I extend/modify the code in this repo
