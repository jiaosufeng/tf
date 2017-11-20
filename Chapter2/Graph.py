# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:27:55 2017

@author: hanqiangfei
"""

"Operations in a Computational Graph"

#1.we load TensorFlow and create a session
import tensorflow as tf
#warning: here is Session, not session
sess =tf.Session()

#2.we declare our tensors and placeholders. Here we will create a numpy array to feed into our operation:
import numpy as np
x_vals=np.array([1.0,3.0,5.0,7.0,9.0])
x_data=tf.placeholder(tf.float32)
m_const=tf.constant(3.0)

my_product=tf.mul(x_data,m_const)

for x_val in x_vals:
    print(sess.run(my_product,feed_dict={x_data:x_val}))
