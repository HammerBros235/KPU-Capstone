#2개의 그래프를 그림. 매초 업데이트되며 마지막 몇개의 수치만 그래프에 표현 됨. 전 수치는 저장하지 않고 있음.
#그래프1: 정중앙 주시?0:1
#그래프2: 정중앙 주시 수치 평균

from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections

#gaze_centered: 0/1
#gaze_centered_avg: avg
def my_function(i):
    global cnt , gaze, graph_self

    gaze_centered.popleft()
    gaze_centered.append(gaze.is_center())

    if gaze.is_center()==None :
            tmp = gaze_centered_avg[-1] * cnt 

    else :
            tmp = gaze_centered_avg[-1] * cnt + gaze.is_center()

    cnt += 1
    avg = tmp/cnt
    gaze_centered_avg.popleft()
    gaze_centered_avg.append(avg)
    
    graph_self.ax.cla()
    graph_self.ax1.cla()

    graph_self.ax.plot(gaze_centered, c='#EC5E29')
    graph_self.ax.scatter(len(gaze_centered)-1, gaze_centered[-1], c='#EC5E29')
    graph_self.ax.text(len(gaze_centered)-1, gaze_centered[-1]+2, "{}%".format(gaze_centered[-1]))

    graph_self.ax.set_xticks(np.arange(-1,10,2))
    graph_self.ax.set_xticklabels(np.arange(10,-1,-2))
    graph_self.ax.set_xlabel('Seconds')
    graph_self.ax.set_title('gaze_centered %\n')
    graph_self.ax.set_ylim(0,100)

    # remove spines
    graph_self.ax.spines['left'].set_visible(False)
    graph_self.ax.spines['right'].set_visible(False)
    graph_self.ax.spines['top'].set_visible(False)

    # grid
    graph_self.ax.set_axisbelow(True)
    graph_self.ax.yaxis.grid(linestyle='dashed', alpha=0.8)

    graph_self.ax1.plot(gaze_centered_avg, c='#1787AD')
    graph_self.ax1.scatter(len(gaze_centered_avg)-1, gaze_centered_avg[-1], c='#1787AD')
    graph_self.ax1.text(len(gaze_centered_avg)-1, gaze_centered_avg[-1]+2, "{}%".format(gaze_centered_avg[-1]))

    graph_self.ax1.set_xticks(np.arange(-1,10,2))
    graph_self.ax1.set_xticklabels(np.arange(10,-1,-2))
    graph_self.ax1.set_xlabel('Seconds')
    graph_self.ax1.set_title('gaze_centered_avg %\n')
    graph_self.ax1.set_ylim(0,100)
    # remove spines
    graph_self.ax1.spines['left'].set_visible(False)
    graph_self.ax1.spines['right'].set_visible(False)
    graph_self.ax1.spines['top'].set_visible(False)

    # grid
    graph_self.ax1.set_axisbelow(True)
    graph_self.ax1.yaxis.grid(linestyle='dashed', alpha=0.8)

