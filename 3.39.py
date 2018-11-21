print("MUHAMMAD SOHAIB - 18B-054-CS - section A")

print("\t\t\t PROBLEMS: 3.39")
def collision(x1,y1,r1,x2,y2,r2):
    import math
    c_dist =((x2 - x1)**2 + (y1 - y2)**2)
    if c_dist <= (r1+r2)**2:
        return True
    else:
        return False
