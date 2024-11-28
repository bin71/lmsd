import numpy as np

points = {
    'P1': np.array([2, 10]),
    'P2': np.array([2, 5]),
    'P3': np.array([8, 4]),
    'P4': np.array([5, 8]),
    'P5': np.array([7, 5]),
    'P6': np.array([6, 4]),
    'P7': np.array([1, 2]),
    'P8': np.array([4, 9])
}

m1 = np.array([2, 10])  
m2 = np.array([5, 8])   
m3 = np.array([1, 2]) 

def euclidean(p1, p2):
  return np.sqrt(np.sum((p1-p2)**2))


while(True):
  clusters = {'1':[], '2':[], '3':[]}

  for p in points:
    dist_m1 = euclidean(points[p],m1)
    dist_m2 = euclidean(points[p],m2)
    dist_m3 = euclidean(points[p],m3)

    if dist_m1 < dist_m2 and dist_m1 < dist_m3:
      clusters['1'].append(p)
    elif dist_m2 < dist_m1 and dist_m2 < dist_m3:
      clusters['2'].append(p)
    else:
      clusters['3'].append(p)

  prev_m1 = m1.copy()
  prev_m2 = m2.copy()
  prev_m3 = m3.copy()

  new_m1 = np.mean([points[a] for a in clusters['1']], axis = 0) if clusters['1'] else m1
  new_m2 = np.mean([points[a] for a in clusters['2']], axis = 0) if clusters['2'] else m2
  new_m3 = np.mean([points[a] for a in clusters['3']], axis = 0) if clusters['3'] else m3

  if np.allclose(new_m1, prev_m1) and np.allclose(new_m2, prev_m2) and np.allclose(new_m3, prev_m3):
    break

  m1 = new_m1
  m2 = new_m2
  m3 = new_m3

if 'P6' in clusters['1']:
  print("P6 is in cluster 1") 
elif 'P6' in clusters['2']:
  print("P6 is in cluster 2")
else :
  print("P6 is in cluster 3")

print("Population of cluster 3 is:", len(clusters['3']))

print("Updated values of m1, m2 and m3 are: ", m1, m2, m3)


