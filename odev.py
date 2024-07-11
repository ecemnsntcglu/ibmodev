import math

points = [(3,4),(5,12),(7,24),(8,15)]

def euclideanDistance(p1,p2):
  return math.sqrt((p1[0]-p2[0])**2 + (p2[1]-p1[1])**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        
        min_distance = min(distances)

print("noktalar:", points)
print("mesafe:", distances)
print("min mesafe:", min_distance)


