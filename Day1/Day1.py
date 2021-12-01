with open("Day1.txt",'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    #part 1
    print(len([x for e,x in enumerate(data) if data[e-1] < x ]))
    #part 2
    print(len([x for e,x in enumerate(data) if e > 2 and sum(data[e-3:e]) < sum(data[e-2:e+1])]))