#그래프 그리는 함수 정의

import matplotlib.pyplot 
import numpy as np



def live_plotter(x_vec,y1_data,line1,graphW,plt,identifier='',pause_time=1):
    
    # after the figure, axis, and line are created, we only need to update the y-data
    graphW.line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=graphW.line1.axes.get_ylim()[0] or np.max(y1_data)>=graphW.line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    #plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return graphW.line1,