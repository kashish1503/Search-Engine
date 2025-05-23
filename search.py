
def req_points1(list,q,d,req):                # function for making BST
    for i in list:
        if(i[1]>=q[1]-d and i[1]<=q[1]+d):
            req.append(i)

def query(x1,x2,y1,y2,root, div, dir,req):
    if(root.left==None and (root.val[0]>=x1 and root.val[0]<=x2) and (root.val[1]>=y1 and root.val[1]<=y2)):
        req.append(root.val)
        return
    elif root.left==None:
        return
    node = root.val
    if node[0] <= x1:
        query(x1,x2,y1,y2,root.right,div, dir,req)
    if node[0] > x2:
        query(x1,x2,y1,y2,root.left,div, dir,req)
    elif x1 < node[0] <= x2:
        if div == 0:
            div = 1
            dir=0
            query(x1,x2,y1,y2,root.left,div, dir,req)
            dir = 1
            query(x1,x2,y1,y2,root.right,div, dir,req)
        else:
            if dir == 0:
                query(x1,x2,y1,y2,root.left,div, dir,req)
                q=((x1+x2)/2,(y1+y2)/2)
                req_points1(root.right.y_as,q,(x2-x1)/2,req)
            else:
                query(x1, x2, y1, y2, root.right, div, dir, req)
                q = ((x1 + x2) / 2, (y1 + y2) / 2)
                req_points1(root.left.y_as, q, (x2 - x1) / 2, req)

class Node1:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.y_as=None

class rangetree:
    def __init__(self,list):
            center_val = len(list[0]) // 2        # index of mid value
            root = Node1(list[0][center_val])
            self.val = root.val                     # self.val root of rangetree not actual
            self.left = root.left
            self.right = root.right
            self.y_as = root.y_as
            y_assoc=list[1]
            self.y_as = y_assoc
            left_half=[[],[]]
            right_half=[[],[]]
            left_half[0] = list[0][:center_val]
            right_half[0] = list[0][center_val:]
            for d in list[1]:
                if(d[0] < list[0][center_val][0]):
                    left_half[1].append(d)
                else:
                    right_half[1].append(d)
            if center_val > 0:
                self.left = rangetree(left_half)
            if(len(list[0])-center_val-1) > 0:
                self.right = rangetree(right_half)
            elif(len(list[0])-center_val-1) == 0 and len(list[0]) != 1:
                self.right = Node1(list[0][center_val])
                self.right.y_as = [self.right.val]


class PointDatabase:
    def __init__(self,pointlist):
           if len(pointlist) != 0:
               combined = [[]]
               pointlist.sort(key=lambda x: x[0])
               for i in pointlist:
                   combined[0].append(i)
               pointlist.sort(key=lambda x: x[1])
               combined.append(pointlist)
               rangeTree = rangetree(combined)
               self.val = rangeTree.val
               self.left = rangeTree.left
               self.right = rangeTree.right
               self.y_as = rangeTree.y_as
           else:
               self.val = None

    def searchNearby(self,q,d):
        list=[]
        if self.val != None:
            query(q[0]-d,q[0]+d,q[1]-d,q[1]+d,self,0,2,list)
            return list
        else:
            return []

# pointDbObject = PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10), (9, 2), (10, 5)])
# print(pointDbObject.searchNearby((5,5), 1))
# print(pointDbObject.searchNearby((10,2), 1.5))
# print(pointDbObject.searchNearby((4,8), 2))

