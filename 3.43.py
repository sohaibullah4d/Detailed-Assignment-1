print("MUHAMMAD SOHAIB - 18B-054-CS - section A")

print("\t\t\t PROBLEMS: 3.43")
def hit(x1,y1,r1,x2,y2):
    import math
    dist = ((x2 - x1)**2 + (y1 - y2)**2)
    if dist <= (r1**2):
        return True
    else:
        return False
