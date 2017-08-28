#!/usr/bin/env python
# Author: Guy Sherman
# Copyright 2017 Guy Sherman
# License: GPL v2
# GIMP plugin to automate the use of the gimp image registration plugin https://sourceforge.net/projects/gimp-image-reg/

from gimpfu import *

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)


def align_all_layers(img,  drw):
    num_iterations = 1536
    accuracy = 6
    matching_area = 0
    transformation_model = 0
    interpolation = 2
    clip_results = 0
    layers = img.layers
    num_layers = len(layers)
    bottom_layer = layers[num_layers - 1]
    for layer in layers:
        if layer != bottom_layer:
            pdb.gimp_image_reg(img, layer, bottom_layer, matching_area, transformation_model, num_iterations, accuracy, interpolation, clip_results)
    

register(
    "python-fu-align-all-layers",
    "Automate aligning layers with gimp image registration.",
    "Automate aligning layers with gimp image registration.",
    "Guy Sherman",
    "Guy Sherman",
    "2017",
    "<Image>/Image/Align All Layers",
    "RGB*, GRAY*",
    [],
    [],
    align_all_layers)

main()