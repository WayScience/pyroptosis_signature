#!/usr/bin/env python
# coding: utf-8

# # Create LoadData with illumination correction functions csv for CellProfiler

# ## Import libraries

# In[1]:


import os
import pathlib

import sys
sys.path.append("../../utils")
import loaddata_utils as ld


# ## Set paths
# 
# **Note:** All paths must be absolute since CellProfiler will need to find the images based on your local machine. Please change the `/home/jenna` part of the path to reflect your machine.

# In[2]:


index_directory = pathlib.Path("/home/jenna/Interstellar_Project/0.wave1_data/0.download_data/70117_20230118MM1_AbTest_V2__2023-01-25T16_44_54-Measurement1/Images")
config_path = pathlib.Path("/home/jenna/Interstellar_Project/0.wave1_data/1.cellprofiler_ic_processing/config.yml")
path_to_output = pathlib.Path("/home/jenna/Interstellar_Project/0.wave1_data/1.cellprofiler_ic_processing/wave1_loaddata.csv")
illum_directory = pathlib.Path("/home/jenna/Interstellar_Project/0.wave1_data/1.cellprofiler_ic_processing/illum_directory")
plate_id = "70117_20230118MM1_AbTest_V2"
illum_output_path = pathlib.Path("/home/jenna/Interstellar_Project/0.wave1_data/2.cellprofiler_analysis/wave1_loaddata_with_illum.csv")


# ## Create the LoadData csv with illum correction functions

# In[3]:


ld.create_loaddata_illum_csv(index_directory, config_path, path_to_output, illum_directory, plate_id, illum_output_path)

