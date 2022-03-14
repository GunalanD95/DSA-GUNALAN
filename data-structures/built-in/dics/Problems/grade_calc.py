# Program to create grade calculator in Python

'''
10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works

1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"

'''

jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }
tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }


# Method 1
def grade_cal(dic):
    for i in dic:
        if i == 'assignment':
            ass  = (0.1 * float(sum((dic[i])))) / len(dic[i])
        elif i == 'test':
            test  = (0.7 * float(sum(dic[i]))) / len(dic[i])  
        elif i == 'lab':
            lab  =  (0.2 * float(sum(dic[i]) )) / len(dic[i])
    total = ass + test + lab
    
    if total >=90:
        print(dic['name'], "got A")
    elif total >=80:
        print(dic['name'], "got B")
    elif total >=70:
        print(dic['name'], "got C")
    elif total >=60:
        print(dic['name'], "got D")
    else:
        print(dic['name'], "got E")
    
    return total


print(grade_cal(jack))
print(grade_cal(james))
print(grade_cal(dylan))
print(grade_cal(jess))
print(grade_cal(tom))