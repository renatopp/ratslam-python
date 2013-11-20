# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - rppereira@inf.ufrgs.br
# =============================================================================
# Copyright (c) 2013 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

import cv2
import numpy as np
import ratslam

'''
Utility for profiling.

Use it with RunSnakeRun [1]_ and Line Profiler [2]_.

**RunSnakeRun:**

 - For RunSnakeRun, just run this file and open the ratslam.profile file into 
   the program. I suggest you to backup the profile file in order to not 
   override it when running the line profiler.

**Line Profiler:**

 - For Line Profiler, first insert the @profile decoration into some point of
   the code, put a break point into the main loop if needed, and finally, run::

    $ kernprof.py -l profiling.py && python -m line_profiler profiling.py.lprof 


.. [1] http://www.vrplumber.com/programming/runsnakerun/
.. [2] http://pythonhosted.org/line_profiler/
'''

def main():
    data = r'D:\Bkp\ratslam\data\stlucia_testloop.avi'

    video = cv2.VideoCapture(data)
    slam = ratslam.Ratslam()
    
    loop = 0
    _, frame = video.read()
    while True:
        loop += 1
        _, frame = video.read()
        if frame is None: break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        slam.digest(img)
        
        # break

        if loop%100 == 0: print '%0.2f%%'%(100*loop/1000.)

import cProfile
command = """main()"""
cProfile.runctx(command, globals(), locals(), filename="ratslam.profile" )