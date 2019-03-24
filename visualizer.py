# Based on:
# https://github.com/vwrs/dcgan-mnist/blob/master/visualizer.py

# -*- coding: utf-8 -*-
import math
import numpy as np
import sys


def combine_images(generated_images):
    total, width, height, channels = generated_images.shape
    cols = int(math.sqrt(total))
    rows = math.ceil(float(total)/cols)
    combined_image = np.zeros((height*rows, width*cols, channels),
                              dtype=generated_images.dtype)

    for index, image in enumerate(generated_images):
        i = int(index/cols)
        j = index % cols
        combined_image[width*i:width*(i+1), height*j:height*(j+1)] = image[:, :, :]
    return combined_image


def show_progress(e,i,g0,d0,g1,d1):
    sys.stdout.write("\repoch: %d, batch: %d, g_loss: %f, d_loss: %f, g_accuracy: %f, d_accuracy: %f" % (e,i,g0,d0,g1,d1))
    sys.stdout.flush()
