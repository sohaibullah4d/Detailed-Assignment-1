print("MUHAMMAD SOHAIB - 18B-054-CS - section A")

print("\t\t\t PROBLEMS: 3.34")
def pay(hourly,hours):
    if hours >= 40:
        sal = 40*hourly 
        Over_time = sal + hourly *(hours - 40) * 1.5
        return Over_time
    else:
        No_Overtime = hours * hourly
        return No_Overtime
