import numpy as np
import math
import geopy.distance

def main(coords, n):
 
  
  distMatrix = matr(coords,n)
  cityPathMatrix = [[0] * n for k in range(n+1)]
  minPath, minIndex, cityPath = algorithm(distMatrix, n, cityPathMatrix)
  print("City Path: \nStarting City: " + str(coords[minIndex * 3 + 2]))
  for i in range(n):
    temp = cityPathMatrix[minIndex][i]
    print("cityNo: " + str(temp) +" "+ str(coords[temp*3+2]))
  print("The minimum cycle through all " + str(n) + 
  " US cities is: " + str(minPath) + " kilometers")
  print("The starting and ending city is: " + str(coords[(minIndex*3) + 2]))
  
  print("done\n")


"""
Paramaters:
  coords: An array of coordinates
  n: number of cities
This method creates a matrix of size nxn and creates values using the distanceCalc method
Each row and column is a city and the value in each row and column is the distance from a city to another

"""
def matr(coords,n):
  Matrix = [ [0] * n for k in range(n)]
  i = 0
  j = 0
  xValue = 0 
  yValue = 1
  xFixed = 0
  yFixed = 1
  for i in range(n):
    xValue = 0
    yValue = 1
    for j in range(n):
      if i == j:
        Matrix[int(i)][int(j)] = 0
        #do nothing
      else:
        dist = distanceCalc(coords[int(xFixed)], coords[int(yFixed)], coords[int(xValue)], coords[int(yValue)])
        Matrix[int(i)][int(j)] = dist
      xValue += 3
      yValue += 3
    xFixed +=3
    yFixed +=3
  return Matrix

"""
Paramaters:
  matrix: a distance matrix
  n: number of cities
  cityMatrix: the matrix of the n number of paths by cities.
This function finds the minimum path for each city being the starting city.
find the minValue and minIndex of the city after the starting city
update the visited list for the city found
"""
def algorithm(matrix, n, cityMatrix):
  pathArray = [] #append to the end of pathArray
  visitedList= [False] * n
  visitedCt = 1
  for i in range(n):
    #resetting visitedList
    visitedCt = 0 
    k = 0
    for k in range(n):
      visitedList[k] = False
      if i == k:
        visitedList[k] = True    
    minPath = 0
    minValue, minIndex = newMin(matrix, i, n, visitedList) 
    visitedList[minIndex] = True
    visitedCt +=1
    minPath += minValue
    cityMatrix[i][0] = i
    for j in range(n-1):
      
      if j != i:
        minValue, minNext = newMin(matrix, minIndex, n, visitedList)
        minPath += minValue
        cityMatrix[i][j] = minNext
        visitedList[minNext] = True
        visitedCt +=1
    # once the algorithim is finished, replaces last value with return to starting city
    j +=1
    minPath += matrix[minNext][i]
    cityMatrix[i][j] = i
    pathArray.append(minPath)
  print(pathArray)
  return min(pathArray), pathArray.index(min(pathArray)), cityMatrix


"""
Finds the distance using coordinates
"""
def distanceCalc(lat1, long1, lat2, long2):
  city1 = (lat1,long1)
  city2 = (lat2,long2)
  distance = geopy.distance.vincenty(city1, city2).km
  return distance

"""
Paramaters:
  matrix: distance matrix
  startPos: starting city index
  n: number of cities
  visited: boolean value. returns true if the city has already been visited
Finds the minimum value of a column. 
"""
def newMin(matrix, startPos, n, visited):
  #this function find a minimum value that hasn't been visited yet
  #forward declared variables
  
  i = 0
  compareVal = 0
  minVal = 0
  minIndex = 0

  while(i < n):
    if(matrix[startPos][i] == 0):
      #if 0, move to the next city
      pass
    elif (visited[i] == False):
      if (minVal == 0):
        #if minvalue has no value and the city hasn't been visited, use it for comparison
        minVal = matrix[startPos][i]
        minIndex = i
      elif (matrix[startPos][i] < minVal):
        #If the city is closer, set it to minVal
        minVal = matrix[startPos][i]
        minIndex = i
      else:
        pass
    else:
      pass
    i += 1
  
  return minVal, minIndex
"""
n = the total number of cities to be visited
coords = the list of cooridantes and city names to be visited
"""
n = 48

# only using the continental US states
coords = [
32.361538,-86.279118, "Montgomery",
#58.301935, -134.41974, "Juneau",
33.448457,-112.073844,"Phoenix",
34.736009,-92.331122,"Little Rock",
38.555605,-121.468926,"Sacramento",
39.7391667,-104.984167,"Denver",
41.767,-72.677,"Hartford",
39.161921,-75.526755,"Dover",
30.4518,-84.27277,"Tallahassee",
33.76,-84.39,"Atlanta",
#21.30895,-157.826182,"Honolulu",
43.613739,-116.237651,"Boise",
39.78325,-89.650373,"Springfield",
39.190942,-86.147685,"Indianapolis",
41.590939,-93.620866,"Des Moines",
39.04,-95.69,"Topkea",
38.197274,-84.86311,"Frankfort",
30.45809,-91.140229,"Baton Rouge",
44.323535,-69.765261,"Augusta",
38.972945,-76.501157,"Annapolis",
42.2352,-71.0275,"Boston",
42.7335,-84.5467,"Lansing",
44.95,-93.094,"Saint Paul",
32.32,-90.207,"Jackson",
38.572954,-92.189283,"Jefferson City",
49.595805,-112.027031,"Helana",
40.809868,-96.675345,"Lincoln",
39.160949,-119.753877,"Carson City",
43.220093,-71.549127,"Concord",
40.221741,-74.756138,"Trenton",
35.667231,-105.964575,"Santa Fe",
42.659829,-73.781339,"Albany",
35.771,-78.638,"Raleigh",
48.813343,-100.779004,"Bismarck",
39.962245,-83.000647,"Columbus",
35.482309,-97.534994,"Oklahoma City",
44.931109,-123.029159,"Salem",
40.269789,-76.875613,"Harrisburg",
41.82355,-71.422132,"Providence",
34,-81.035,"Columbia",
44.367966,-100.336378,"Pierre",
36.165,-86.784,"Nashville",
30.266667,-97.75,"Austin",
40.7547,-111.892622,"Salt Lake City",
44.26639,-72.57194,"Montpleier",
37.54,-77.46,"Richmond",
47.042418,-122.893077,"Olympia",
38.349497,-81.633294,"Charleston",
43.074722,-89.384444,"Madison",
41.145548,-104.802042,"Cheyenne"]

main(coords, n)
