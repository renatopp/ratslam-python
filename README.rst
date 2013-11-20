========================
RATSLAM (PYTHON VERSION)
========================

This is a full Ratslam implementation in python. This implementation is based 
on Milford's original implementation [1]_ in matlab, and Christine Lee's python 
implementation [2]_. The original data movies can also be found in [1]_.


Dependences
-----------

The only dependence for this package is Numpy [3]_, thus it does not handle how
to open and manage the movie and image files. For this, I strongly recommend 
the use of OpenCV [4]_.


Profiling
---------
A profile utility is provided with this package in the 'profiling' directory,
it is ready to use the RunSnakeRun [5]_ and Line Profiler [6]_.


.. [1] https://wiki.qut.edu.au/display/cyphy/RatSLAM+MATLAB
.. [2] https://github.com/coxlab/ratslam-python
.. [3] http://www.numpy.org/
.. [4] http://opencv.org/
.. [5] http://www.vrplumber.com/programming/runsnakerun/
.. [6] http://pythonhosted.org/line_profiler/