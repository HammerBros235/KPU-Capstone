import Point

def Shakiness(pD):
    #Boundary percentage. Arbitarily chosen to be 10 for now.
    limit = 10
    if (abs(pD.x) > limit or abs(pD.y) > limit or abs(pD.w) > limit or abs(pD.h) > limit):
        print("[Shakiness] Shaking!")
    else:
        print("[Shakiness] steady...")