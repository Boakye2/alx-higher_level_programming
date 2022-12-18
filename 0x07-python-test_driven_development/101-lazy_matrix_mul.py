#!/usr/bin/python3
"""This module contains a function that uses numpy module to
multiply two matrix"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul function that multiplies two matrix using numpy module
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    return numpy.matmul(m_a, m_b)
    
