with open('Day7.txt','r') as infile:
    crabs = [int(x) for x in infile.read().strip().split(',')]
cost1 = float('inf')
cost2 = float('inf')
for y in range(min(crabs),max(crabs)):
    cost1 = min(cost1,sum([abs(x-y) for x in crabs]))
    cost2 = min(cost2,sum([(abs(x-y)*(abs(x-y)+1)//2) for x in crabs]))
print(cost1,cost2)