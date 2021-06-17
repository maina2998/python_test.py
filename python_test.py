y =[]
x =[100,110,120,130,140,150]
for d in x:
    if d * 5:
        y.append(x)
        print(x)
  
def divisible_by_three(n):
    for x in n:
        n = 10
        if x % 3 == 0:
             print("{} is divisible by three".format(x))
        else:
             print("{} is not divisible by three".format(x))


y =[]
def flatten_the_lists(l):
    flist =[]
    flist.extend([l])
    if(type(l)is not list):
        return flist
    else:
        x =[[1,2],[3,4],[5,6]]
        flist=flatten_the_lists(x)
    print(flist)


    

def divisible_by_seven():
    x in range(100,200)
    for y in x:
        if y % 7 != 0:
            print("{} is divisible by 7 ".format(y))
        else:
            print("{} not divisible by 7". format(y))    


def greetings(*args):
    students =[{"age":19, "name":"Eunice"},
    {"age":21, "name":"Agnes"},
    {"age":18, "name":"Teresa"},
    {"age":22, "name":"Asha"}]
    for student in greetings:
        
         print(f"Hello {args.name} , you were born in the year {args.year}")
greetings()    




