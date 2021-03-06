import math
import heapq

### this is a helper function that converts a string containing latitude or longitude
## represented as degrees.minutes.seconds (e.g. 37.47.44N) into a float.
def convertLatLong(str) :
    deg, minutes,seconds = str[:-1].split('.',2)
    minutes = float(minutes) + (float(seconds) / 60.0)
    deg = float(deg) + (minutes/ 60.0)
    return deg

def convertDegDis(deg):
    return float(deg)*40076/360

def eu_dist(a, b):
    "Euclidean distance between two vertices."
    diffx = (convertLatLong(a.lat) - convertLatLong(b.lat))
    diffy = (convertLatLong(a.longitude) - convertLatLong(b.longitude))
    return convertDegDis(math.sqrt(diffx**2 + diffy**2))

def f(current_state, goal_vertex):
    current_vertex = current_state.vertex
    g = current_state.cost
    h = eu_dist(current_vertex, goal_vertex)
    return g + h


class SearchQueue :
    def __init__(self, goal=None) :
        self.q = []
        self.goal_vertex = goal
        self.mincost = float('inf')

    def insert(self, item) :
        pass
    def pop(self) :
        pass
    def isEmpty(self) :
        return self.q == []

### you complete this.
class BFSQueue(SearchQueue) :

    def insert(self, item):
        self.q.append(item)
        return True

    def pop(self):
        return self.q.pop(0)

### you complete this.
class DFSQueue(SearchQueue) :

    def insert(self, item):
        self.q.append(item)
        return True

    def pop(self):
        return self.q.pop(-1)

### you complete this
class AStarQueue(SearchQueue) :

    def insert(self, item):
        qitem = (f(item, self.goal_vertex), item)
        heapq.heappush(self.q, qitem)

    def pop(self):
        return heapq.heappop(self.q)[1]
