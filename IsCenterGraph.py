#에니메이션 작동하지 않을 경우 -> `%matplotlib qt` 실행.
#혹은 Tools > Preferences > IPython Console > Graphics > Backend: "Inline" -> "Automatic"

#2개의 그래프를 그림. 매초 업데이트되며 마지막 몇개의 수치만 그래프에 표현 됨. 전 수치는 저장하지 않고 있음.
#그래프1: 정중앙 주시?0:1
#그래프2: 정중앙 주시 수치 평균

from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections

gaze = GazeTracking()

#gaze_centered: 0/1
#gaze_centered_avg: avg
def my_function(i):
    gaze_centered.popleft()
    gaze_centered.append(gaze.is_center())

    tmp = gaze_centered_avg[-1] * cnt + gaze.is_center()
    cnt += 1
    avg = tmp/cnt
    gaze_centered_avg.popleft()
    gaze_centered_avg.append(avg)
    
    ax.cla()
    ax1.cla()

    ax.plot(gaze_centered, c='#EC5E29')
    ax.scatter(len(gaze_centered)-1, gaze_centered[-1], c='#EC5E29')
    ax.text(len(gaze_centered)-1, gaze_centered[-1]+2, "{}%".format(gaze_centered[-1]))

    ax.set_xticks(np.arange(-1,10,2))
    ax.set_xticklabels(np.arange(10,-1,-2))
    ax.set_xlabel('Seconds')
    ax.set_title('gaze_centered %\n')
    ax.set_ylim(0,100)

    # remove spines
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # grid
    ax.set_axisbelow(True)
    ax.yaxis.grid(linestyle='dashed', alpha=0.8)

    ax1.plot(gaze_centered_avg, c='#1787AD')
    ax1.scatter(len(gaze_centered_avg)-1, gaze_centered_avg[-1], c='#1787AD')
    ax1.text(len(gaze_centered_avg)-1, gaze_centered_avg[-1]+2, "{}%".format(gaze_centered_avg[-1]))

    ax1.set_xticks(np.arange(-1,10,2))
    ax1.set_xticklabels(np.arange(10,-1,-2))
    ax1.set_xlabel('Seconds')
    ax1.set_title('gaze_centered_avg %\n')
    ax1.set_ylim(0,100)
    # remove spines
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    # grid
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(linestyle='dashed', alpha=0.8)
    
gaze_centered = collections.deque(np.zeros(10))
gaze_centered_avg = collections.deque(np.zeros(10))
cnt = 0

fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')

ax = plt.subplot(121)
ax1 = plt.subplot(122)

ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')

animation = FuncAnimation(plt.gcf(), my_function, interval=1000)

plt.show()
