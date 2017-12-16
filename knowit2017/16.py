visitors = [int(x) for x in open("prisoners.txt").readlines()]
has_visited = {}
lamp = False
c = 0
visits = 0

for visitor in visitors:
	visits += 1

	if visitor in has_visited:
		continue

	if visitor == 1:
		if lamp:
			lamp = False
			c += 1

		if c == 99:
			break
	elif lamp is False:
		lamp = True
		has_visited[visitor] = True

print(visits, c)
