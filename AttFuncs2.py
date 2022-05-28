#is_center() 값 기록. 실시간 그래프. 화면 주시 실패.

#from gaze_tracking import GazeTracking
#gaze = GazeTracking()

from pylive import live_plotter
import numpy as np


#값 기록 리스트
lst_cen = []    #is_center()값 기록. (예: [0,0,1,1,1,1,1,0,0,1,1,1])
lst_cen_avg = []    #lst_cen의 평균값 기록. (예: [0, 0.5, 0.33, 0.25])

#Graph
size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.zeros(size)
line1 = []

#화면 주시 실패 설정 값
concentrate_for_secs = 5

#is_center() 값 기록. 실시간 그래프. 집중 안할시 표시 
while True:
    
    ##is_center() 값 기록.
    cen = gaze.is_center()
    #cen = np.random.choice([0,1])  #테스트용 0,1 랜덤 값
    lst_cen.append(cen)
    
    cen_avg = sum(lst_cen) / len(lst_cen)
    lst_cen_avg.append(cen_avg)
        
    
    #실시간 그래프
    y_vec[-1] = lst_cen_avg[-1]
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)
    
    
    #화면 주시 실패 
    if sum(lst_cen[concentrate_for_secs:]) == 0:
        print("5초 이상 화면 주시 실패.")
