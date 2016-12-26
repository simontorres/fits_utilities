import matplotlib.pyplot as plt
import sys
import numpy as np

# no_chunks = int(81)
memlim = np.linspace(1e6, 16e9)
file_sizes = np.linspace(5e7, 2e8, 50)
xs = int(1986)
ys = int(4081)

for size in file_sizes:
    for lim in memlim:
        no_chunks = max(1 , int(size / lim))
        # print no_chunks
        try:
            xstep = max(1, int(xs / no_chunks))
            ystep = max(1, int(ys / (1 + no_chunks - int(xs / xstep))))
            # print xstep, ystep
        except ZeroDivisionError:
            print('ZeroDivisionError')
            print('File Size %s MB' % float(float(size) / 1.e6))
            print('Memory Limit %s MB' % float(float(lim)/1.e6))
            print('xstep %s no_chunks %s xs/xstep %s'%(xstep, no_chunks, xs/xstep))
            print(' ')




