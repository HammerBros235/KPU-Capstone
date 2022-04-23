from Point import Point

#화면크기: 720p
pScreenX = 1280
pScreenY = 720

#차이% 계산
def pDiff(p1, p2):
    pD = p1 - p2
    return Point(round(pD[0]/pScreenX, 4), round(pD[1]/pScreenY, 4), round(pD[2]/pScreenX, 4), round(pD[3]/pScreenY, 4))

def shakiness(pD):
    #정도 조정. 임의적으로 10%으로 정함.
    limit = 0.01 * 10
    #print("[pDiff] " + str(pD))
    if (pD !=None):
        if (abs(pD.x) > limit or abs(pD.y) > limit or abs(pD.w) > limit or abs(pD.h) > limit):
            return "over"
            #print("[Shakiness] 흔들림!")
        else:
            return "under"
            #print("[Shakiness] OK...")
    else:
	return "None"
