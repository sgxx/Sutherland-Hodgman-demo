#coding=utf-8

#@time:2019/3/27 8:23
#@author: Sheng Guangxiao

import matplotlib.pyplot as plt
import numpy as np

width=100
height=100

def pointInRec(p):
    if 0<=p[0]<=width and 0<=p[1]<=height:
        return True
    return False

# Thanks to Paul Draper at
# http://stackoverflow.com/questions/20677795/find-the-point-of-intersecting-lines
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return 99999,99999

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def calcIntersection(p0,p1,tempRecIndex):
    # print('p0,p1',p0,p1,tempRecIndex)

    pb1 = [p0, p1]
    pb2 = [[0,0],[width,0]]
    x,y=line_intersection(pb1, pb2)

    result=(None,None,None)

    currentDiff=4

    if min(p0[0],p1[0])<=x<=max(p0[0],p1[0]) and min(p0[1],p1[1])<=y<=max(p0[1],p1[1]) and 0<=x<=width and 0<=y<=height:
        if result[0] is None and not (x==p0[0] and y==p0[1]) and not (x==p1[0] and y==p1[1]):
            result=(x,y,1)
            currentDiff=(1-tempRecIndex)%4

    pb2 = [[width, 0], [width, height]]
    x, y = line_intersection(pb1, pb2)

    if min(p0[0],p1[0])<=x<=max(p0[0],p1[0]) and min(p0[1],p1[1])<=y<=max(p0[1],p1[1]) and 0<=x<=width and 0<=y<=height:
        if result[0] is None and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result =(x, y, 2)
        if (2-tempRecIndex)%4<currentDiff and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result=(x,y,2)
            currentDiff=(2-tempRecIndex)%4

    pb2 = [[width, height], [0, height]]
    x, y = line_intersection(pb1, pb2)

    if min(p0[0],p1[0])<=x<=max(p0[0],p1[0]) and min(p0[1],p1[1])<=y<=max(p0[1],p1[1]) and 0<=x<=width and 0<=y<=height:
        if result[0] is None and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result =(x, y, 3)
        if (3-tempRecIndex)%4<currentDiff and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result=(x,y,3)
            currentDiff=(3-tempRecIndex)%4

    pb2 = [[0, height], [0, 0]]
    x, y = line_intersection(pb1, pb2)

    if min(p0[0], p1[0]) <= x <= max(p0[0], p1[0]) and min(p0[1], p1[1]) <= y <= max(p0[1], p1[1]) and 0<=x<=width and 0<=y<=height:
        if result[0] is None and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result =(x, y, 4)
        if (4-tempRecIndex)%4<currentDiff and not (x == p0[0] and y == p0[1]) and not (x == p1[0] and y == p1[1]):
            result=(x,y,4)

    return result

def somepointInRec(pointList):
    for point in pointList:
        if 0<=point[0]<=width and 0<=point[1]<=height:
            return True
    return False

def entireInRec(pointList,tempRecIndex):
    i=-1

    while i<len(pointList):
        if calcIntersection(pointList[i],pointList[i+1],tempRecIndex)[0] is not None:
            return True
        i+=1
    return False

if __name__ == '__main__':

    recList=[[0,0],[width,0],[width,height],[0,height],[0,0]]

    x=[x[0] for x in recList]
    y=[x[1] for x in recList]

    # pointList1=[[50,50],[110,50],[50,110],[50,50]]
    # pointList1=[[50,50],[120,110],[-20,110],[50,50]]
    # pointList1=[[50,-10],[110,50],[50,110],[-10,50],[50,-10]]
    # pointList1=[[50,-100],[150,50],[60,200],[40,200],[20,150],[0,-50],[50,-100]]
    # pointList1=[[50,0],[0,-100],[100,-100],[50,0]]
    # pointList1=[[0,10],[0,-100],[50,-100],[50,50],[0,10]]
    pointList1=[[40,50],[-100,-50],[10,-50],[160,50],[40,50]]

    x1=[x[0] for x in pointList1]
    y1=[x[1] for x in pointList1]

    newList=[]

    i=0

    lengthRec=4
    lengthPolygon=len(pointList1)

    lastPoint=""
    firstPoint=""
    firstI=0
    firstTmpRecIndex=0

    tempRecIndex = 0

    if somepointInRec(pointList1):
        if pointInRec(pointList1[i]):
            firstPoint = pointList1[i]
            firstI=i

            newList.append(pointList1[i])
            lastPoint=pointList1[i]
            i+=1

        else:
            while not pointInRec(pointList1[i]):
                i+=1

            firstPoint = pointList1[i]
            firstI=i

            newList.append(pointList1[i])
            lastPoint=pointList1[i]
            i+=1

    else:
        if entireInRec(pointList1,1):
            while True:
                calcResult=calcIntersection(pointList1[i%len(pointList1)],pointList1[(i+1)%len(pointList1)],1)

                if calcResult[0] is not None:
                    i+=1
                    newList.append([calcResult[0],calcResult[1]])
                    lastPoint=[calcResult[0],calcResult[1]]

                    firstPoint = [calcResult[0],calcResult[1]]
                    firstTmpRecIndex=calcResult[2]
                    firstI=i

                    tempRecIndex=calcResult[2]

                    break

                i+=1
        else:
            raise Exception("多边形和多边形之间完全不相交")

    print('newList',newList)

    i0=i

    lastPointInside=True

    while i<i0+lengthPolygon:
        point=pointList1[i%lengthPolygon]
        # print('i',i,i%lengthPolygon)
        print('newList',newList,lastPointInside,pointInRec(point),lastPoint,point,tempRecIndex)

        deathloop=False

        if lastPointInside:
            if pointInRec(point):
                print('add5',point)
                newList.append(point)
                lastPoint=point

                lastPointInside=True
            else:
                calcResult=calcIntersection(lastPoint,point,tempRecIndex)
                print('calcResult',calcResult,lastPoint,point)
                if [calcResult[0],calcResult[1]] in newList:
                    if len(newList)==1:
                        calcResult = calcIntersection(lastPoint, point, tempRecIndex+1)
                        print('some',calcResult)
                        if tempRecIndex != 0:
                            # tempRecIndex+=1
                            while calcResult[2] != tempRecIndex:
                                # print('calcResult',calcResult)
                                print('add333')
                                newList.append(recList[tempRecIndex])
                                tempRecIndex = 1 + (tempRecIndex) % 4
                        else:
                            tempRecIndex=calcResult[2]


                if calcResult[0] is not None:
                    tempRecIndex=calcResult[2]
                    print('add4',calcResult,lastPoint,point)
                    newList.append([calcResult[0],calcResult[1]])

                    lastPoint=point
                else:
                    lastPoint=point

                lastPointInside = False

        else:
            if pointInRec(point):
                calcResult = calcIntersection(lastPoint, point,tempRecIndex)

                if tempRecIndex!=0:
                    while calcResult[2]!=tempRecIndex:
                        # print('calcResult',calcResult)
                        print('add3')
                        newList.append(recList[tempRecIndex])
                        tempRecIndex=1+(tempRecIndex)%4

                # print('calcResult',calcResult)
                print('add2',point)
                newList.append([calcResult[0], calcResult[1]])

                newList.append(point)
                lastPoint = point

                lastPointInside=True
            else:
                while True:
                    point=pointList1[i%lengthPolygon]
                    calcResult = calcIntersection(lastPoint, point,tempRecIndex)

                    if calcResult[0] is not None:

                        if tempRecIndex != 0:
                            # tempRecIndex+=1
                            print('current',tempRecIndex,calcResult[2])
                            while calcResult[2] != tempRecIndex:
                                # print('calcResult',calcResult)
                                print('add999',newList)
                                newList.append(recList[tempRecIndex])
                                tempRecIndex = 1 + (tempRecIndex) % 4
                        else:
                            tempRecIndex=calcResult[2]

                        if [calcResult[0],calcResult[1]] not in newList:
                            tempRecIndex = calcResult[2]
                            print('add1',newList,lastPoint,point)
                            newList.append([calcResult[0], calcResult[1]])
                            lastPoint = [calcResult[0], calcResult[1]]
                            lastPointInside=True
                            i-=1
                            break

                    else:
                        lastPointInside=False
                        lastPoint=point
                        break

        i+=1

    if len(newList)==1:
        calcResult = calcIntersection(pointList1[(firstI-1)%lengthPolygon], pointList1[(firstI)%lengthPolygon], firstTmpRecIndex + 1)
        print('some', calcResult,pointList1[(firstI-1)%lengthPolygon], pointList1[(firstI)%lengthPolygon])
        if tempRecIndex != 0:
            # tempRecIndex+=1
            while calcResult[2] != tempRecIndex:
                # print('calcResult',calcResult)
                print('add3')
                newList.append(recList[tempRecIndex])
                tempRecIndex = 1 + (tempRecIndex) % 4

        newList.append([calcResult[0],calcResult[1]])

    if newList[-1]!=firstPoint:
        newList.append(firstPoint)
        print('add final',firstPoint)
    x2=[x[0] for x in newList]
    y2=[x[1] for x in newList]

    print(newList)

    plt.plot(x,y)
    plt.plot(x1,y1,color='red')
    plt.plot(x2,y2,color='black',linewidth='5')
    plt.show()

