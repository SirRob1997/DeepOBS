# -*- coding: utf-8 -*-

import tensorflow as tf

DATA_DIR = "data_deepobs/tensorflow"
TF_FLOAT_DTYPE = tf.float32


def get_data_dir():
    return DATA_DIR


def set_data_dir(data_dir):
    """Sets the data directory for the TensorFlow runs.

    Args:
        data_dir (str): Path to the data folder.
    """
    global DATA_DIR
    DATA_DIR = data_dir


def get_float_dtype():
    return TF_FLOAT_DTYPE


def set_float_dtype(dtype):
    global TF_FLOAT_DTYPE
    TF_FLOAT_DTYPE = dtype
