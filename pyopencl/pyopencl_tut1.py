import numpy

import pyopencl as cl
import pyopencl.array as cl_array
from pyopencl.elementwise import ElementwiseKernel

ctx = cl.create_some_context()
print(ctx)
queue = cl.CommandQueue(ctx)

#a_gpu = cl_array.to_device()