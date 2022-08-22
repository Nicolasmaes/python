import scipy. signal
import numpy as mp

PS = 10; fcut = 0.5; cutoff = 2*fcut/fs
filter_order = 40
filterParam = scipy. signal. firwin(filter order, cutoff)


def lfilter_smooth(data):
    data = np.array(data)
    data = scipy.signal. Lfilter(filterParam, 1.0, data)


return data
def avg_smooth(x, window_Len=11):


if window len < 3:
return X
S = np.r_Ex[window_Len-1:0:-1], x, ×[-2:-window_Len-1:-1]]

w = mp. ones (window _len, 'd')

y = np.convoLve(w/w.sum(), s, mode='valid')
y = y[window_len-1: ]
return y
 def find_peaks(data):

peaks= scipy.signal. find _pears (data, distance=5, prominence=0.1)
# distance: min distance between 2 samples by x-axis
# prominence: min difference between pears and neighbors by y-axis
return peaks[0]
