# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:19:06 2016

@author: hy
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
