import numpy as np

points = {
    'P1' : np.array([0.1 , 0.6]),
    'P2' : np.array([0.15, 0.71]),
    'P3' : np.array([0.08, 0.9]),
    'P4' : np.array([0.16, 0.85]),
    'P5' : np.array([0.2, 0.3]),
    'P6' : np.array([0.25, 0.5]),
    'P7' : np.array([0.24, 0.1]),
    'P8' : np.array([0.3, 0.2])
}

m1 = np.array([0.1,0.6])
m2 = np.array([0.3,0.2])

def euclidean(p1, p2):
  return np.sqrt(np.sum((p1-p2)**2))


while(True):
  clusters = {'1':[], '2':[]}

  for p in points:
    dist_m1 = euclidean(points[p],m1)
    dist_m2 = euclidean(points[p],m2)

    if dist_m1 < dist_m2:
      clusters['1'].append(p)
    else:
      clusters['2'].append(p)

  prev_m1 = m1.copy()
  prev_m2 = m2.copy()

  new_m1 = np.mean([points[a] for a in clusters['1']], axis = 0) if clusters['1'] else m1
  new_m2 = np.mean([points[a] for a in clusters['2']], axis = 0) if clusters['2'] else m2

  if np.allclose(new_m1, prev_m1) and np.allclose(new_m2, prev_m2):
    break

  m1 = new_m1
  m2 = new_m2

if 'P6' in clusters['1']:
  print("P6 is in cluster 1") 
else:
  print("P6 is in cluster 2")

print("Population of cluster 2 is:", len(clusters['2']))

print("Updated values of m1 and m2 are: ", m1, m2)


