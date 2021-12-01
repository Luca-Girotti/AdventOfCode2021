depths = [int(a) for a in open("Day1.txt").readlines()]
#part 1
print(sum((1 if b>a else 0) for a,b in zip(depths[:-1],depths[1:])))
#part 2
windows = [sum(depths[i:i+3]) for i in range(len(depths))]
print(sum((1 if b>a else 0) for a,b in zip(windows[:-1],windows[1:])))