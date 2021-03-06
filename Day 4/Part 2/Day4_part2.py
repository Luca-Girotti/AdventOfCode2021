def checkWin(l, m):
	a = [[l[i][j] in m for j in range(5)] for i in range(5)]
	b = [[a[j][i] for j in range(5)] for i in range(5)]
	for i in range(5):
		if sum(a[i]) == 5 or sum(b[i]) == 5:
			return True
	return False

inputFile = open('Day4.txt', 'r')
data = inputFile.read().splitlines()

moves = map(int, data[0].split(','))
boards = []
for l in data[1:]:
	if not l:
		boards.append([])
		continue
	boards[-1].append(list(map(int, l.split())))

m = set()
res = -1
for move in moves:
	m.add(move)
	nextBoards = []
	for board in boards:
		if not checkWin(board, m):
			nextBoards.append(board)
	if len(nextBoards) == 0:
		res = 0
		for i in boards[0]:
			for j in i:
				if j not in m:
					res += j
		res *= move
		break
	boards = nextBoards
print(res)
inputFile.close()