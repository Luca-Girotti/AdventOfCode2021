with open("Day2.txt", "r") as f:
    lines = f.readlines()
def task_1(lines):
    depth = 0
    hori = 0
    for line in lines:
        if "up" in line:
        	depth -= int(line.strip("\n")[-1])
        elif "down" in line:
       		depth += int(line.strip("\n")[-1])	
       	elif "forward" in line:
       		hori += int(line.strip("\n")[-1])

    print(depth * hori)
def task_2(lines):
    depth = 0
    hori = 0
    aim = 0
    for line in lines:
	    if "up" in line:
		    aim -= int(line.strip("\n")[-1])
	    elif "down" in line:
		    aim += int(line.strip("\n")[-1])
	    elif "forward" in line:
		    hori += int(line.strip("\n")[-1])
		    depth += aim * (int(line.strip("\n")[-1]))

    print(hori * depth)

task_1(lines)
task_2(lines)