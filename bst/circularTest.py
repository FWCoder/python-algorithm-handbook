
import math
def solution(S, X, Y):
    # write your code in Python 3.6
    if len(S) != len(X) or len(X) != len(Y):
        return 0
        
    points = {}
    maxRad = 0
    idx = 0
    
    while idx < len(S):
        x = int(X[idx])
        y = int(Y[idx])
        letter = S[idx]
        dist = math.sqrt(x*x + y*y)
        if not letter in points:
            points[letter] = dist
        else:
            if maxRad < dist:
                maxRad = dist
        idx = idx + 1

    newPoints = {}
    for k in points.keys():
        if points.get(k) < maxRad:
            newPoints[k] = points.get(k)

    return len(newPoints.keys())

S = "ABDCA"
X = [2, -1, -4, -3, 3]
Y = [2, -2, 4, 1, -3]

print (solution(S, X, Y))
    