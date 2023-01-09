p1,c1,p2,c2 = map(int,input().split())
equation_pt1 = p1*c1
equation_pt2 = p2*c2
if equation_pt1>equation_pt2:
  print("-1")
elif equation_pt1==equation_pt2:
  print("0")
else:
  print("1")
