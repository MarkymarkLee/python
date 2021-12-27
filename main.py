student = []
scoreboard = {}
subject = ["m","c","e"]

cur = ""

while True:

	s = input("input score or name (type 'p' to print score, type 'stop' to end the program): ")

	if s=="stop":
		break

	elif s=="p":
		for name in student:
			print(name,scoreboard[name])
	
	elif s=="pp":
		print(scoreboard)

	elif s.isdigit():
		sub = input("input the subject:")
		for i in range(len(subject)):
			if sub==subject[i]:
				scoreboard[cur][i] = int(s)
		
	else:
		appeared = False
		for name in student:
			if s==name:
				appeared = True
				break

		if not appeared:
			student.append(s);
			scoreboard[s] = [0,0,0]

		cur = s
