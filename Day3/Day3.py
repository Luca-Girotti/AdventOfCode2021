with open("Day3.txt", "r") as f:
	lines = f.readlines()

def task_1(lines):
	gammaRate = ""
	epRate = ""

	for y in range(12):
		zerotot = 0
		onetot = 0
		for x in range(len(lines)):
			lines[x] = lines[x].strip("\n")
			if lines[x][y] == "0":
				zerotot += 1
			elif lines[x][y] == "1":
				onetot += 1
		if onetot > zerotot:
			gammaRate = gammaRate + "1"
		elif zerotot > onetot:
			gammaRate = gammaRate + "0"

	for bit in gammaRate:
		if bit == "0":
			epRate = epRate + "1"
		elif bit == "1":
			epRate = epRate + "0"
	print(int(epRate, 2) * int(gammaRate, 2))

def task_2(lines):
	def checker(bitty, lines):
		for y in range(12):
			zerotot = 0
			onetot = 0
			for x in range(len(lines)):
				lines[x] = lines[x].strip("\n")
				if lines[x][y] == "0":
					zerotot += 1
				elif lines[x][y] == "1":
					onetot += 1
			if onetot > zerotot or zerotot == onetot:
				lines = [i for i in lines if i[y] == str(bitty)]
				if len(lines) == 1:
					return lines[0]
			elif zerotot > onetot:
				lines = [i for i in lines if i[y] == str(int(not bitty))]
				if len(lines) == 1:
					return lines[0]
	oxyRate = int(checker(1, lines), 2) 
	co2Rate = int(checker(0, lines), 2)
	print(oxyRate * co2Rate)

task_1(lines)
task_2(lines)