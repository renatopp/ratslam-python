Timer unit: 3.09291e-07 s

File: ratslam2\_globals.py
Function: compare_segments at line 79
Total time: 0.0143502 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    79                                           @profile
    80                                           def compare_segments(seg1, seg2, slen):
    81         3           53     17.7      0.1      cwl = seg1.size
    82                                           
    83         3           13      4.3      0.0      mindiff = 1e10
    84         3           14      4.7      0.0      minoffset = 0
    85                                           
    86         3           48     16.0      0.1      diffs = np.zeros(slen)
    87                                           
    88       306         1267      4.1      2.7      for offset in xrange(slen+1):
    89       303         1315      4.3      2.8          e = (cwl-offset)
    90                                           
    91       303         6251     20.6     13.5          cdiff = np.abs(seg1[offset:cwl] - seg2[:e])
    92       303        12607     41.6     27.2          cdiff = np.sum(cdiff)/e
    93                                           
    94       303         1633      5.4      3.5          if cdiff < mindiff:
    95         3           12      4.0      0.0              mindiff = cdiff
    96         3           12      4.0      0.0              minoffset = offset
    97                                           
    98       303         6222     20.5     13.4          cdiff = np.abs(seg1[:e] - seg2[offset:cwl])
    99       303        12686     41.9     27.3          cdiff = np.sum(cdiff)/e
   100                                           
   101       303         1592      5.3      3.4          if cdiff < mindiff:
   102       300         1305      4.3      2.8              mindiff = cdiff
   103       300         1355      4.5      2.9              minoffset = -offset
   104                                           
   105         3           12      4.0      0.0      return minoffset, mindiff

