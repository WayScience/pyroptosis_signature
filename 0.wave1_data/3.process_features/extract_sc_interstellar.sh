#!/bin/bash

# convert the notebook into a python and run the notebook
jupyter nbconvert --to python \
        --FilesWriter.build_directory=scripts/ \
        --execute extract_sc_interstellar.ipynb
