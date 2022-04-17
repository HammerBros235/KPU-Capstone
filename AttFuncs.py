#import Point

def shakiness(pD):
    #정도 조정. 임의적으로 10%으로 정함.
    limit = 10
    if (abs(pD.x) > limit or abs(pD.y) > limit or abs(pD.w) > limit or abs(pD.h) > limit):
        print("[Shakiness] 흔들림!")
    else:
        print("[Shakiness] 가만함...")
