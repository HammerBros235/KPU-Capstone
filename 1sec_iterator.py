import threading
import Point, AttFuncs

def liveShakiness(pA,pB): 
    
    #흔들림 감지 함수. AttFuncs.py에 있음.
    shakiness(pDiff(pA,pB))
    pA = pB
    
    #TODO: pB에다가 매초 새로운 얼굴 좌표 삽입. 클래스는 Point.
    #pB = Point(x,y,w,h)
    pB = Point(100,100,50,50)
    
    #1초마다 반복
    threading.Timer(1.0, printit).start()
