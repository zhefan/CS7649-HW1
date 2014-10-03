import sys

def printAdj(x1,y1, x2,y2):
	sys.stdout.write("         ")
	sys.stdout.write("(adj c" + str(x1) + str(y1) + " c" + str(x2) + str(y2) + ") ")
	sys.stdout.write("(adj c" + str(x2) + str(y2) + " c" + str(x1) + str(y1) + ")\n")
	
def printCollinear(x1,y1, x2,y2, x3,y3):
	sys.stdout.write("         ")
	sys.stdout.write("(collinear c" + str(x1) + str(y1) + " c" + str(x2) + str(y2) + " c" + str(x3) + str(y3) + ") ")
	sys.stdout.write("(collinear c" + str(x3) + str(y3) + " c" + str(x2) + str(y2) + " c" + str(x1) + str(y1) + ")\n")

world = [[-1,0,0],
		 [2,1,0],
		 [0,-1,3]
		];
'''

world = [[2,1,0,3]
		];
'''
				
print "(define (problem sokoban)"
print "  (:domain sokoban-domain)"

# Generate objects
sys.stdout.write("  (:objects")
for x in range(len(world)):
	for y in range(len(world[x])):
		if world[x][y] != -1:
			sys.stdout.write(" c" + str(x) + str(y))
print ")"

sys.stdout.write("  (:init \n" )
# Generate predicates for objects based on cell content
for x in range(len(world)):
	for y in range(len(world[x])):
		if world[x][y] != -1:
			sys.stdout.write("         ")
		if world[x][y] == 3 or world[x][y] == 0:
			sys.stdout.write("(not (hasAgent c" + str(x) + str(y) + ") ) ")
			sys.stdout.write("(not (hasBlock c" + str(x) + str(y) + ") )\n")
		elif world[x][y] == 2:
			sys.stdout.write("     (hasAgent c" + str(x) + str(y) + ")   ")
			sys.stdout.write("(not (hasBlock c" + str(x) + str(y) + ") )\n")
		elif world[x][y] == 1:
			sys.stdout.write("(not (hasAgent c" + str(x) + str(y) + ") ) ")
			sys.stdout.write("     (hasBlock c" + str(x) + str(y) + ")\n")
		
# generate spatial relationship between cells
for x in range(len(world)):
	for y in range(len(world[x])):
		if world[x][y] == -1: continue
		if x < len(world)-1:
			if world[x+1][y] != -1:
				printAdj(x,y,x+1,y)
			if y < len(world[x])-1:
				if world[x][y+1] != -1:
					printAdj(x,y,x,y+1)
		else:
			if y < len(world[x])-1:
				if world[x][y+1] != -1:
					printAdj(x,y,x,y+1)

# generate collinear relationships (sort of hack-y...)			
for x in range(len(world)):
	for y in range(len(world[x])):
		if world[x][y] == -1: continue
		if x < len(world)-2:
			if world[x+1][y] != -1 and world[x+2][y] != -1:
				printCollinear(x,y,x+1,y,x+2,y)
			if y < len(world[x])-2:
				if world[x][y+1] != -1 and world[x][y+2] != -1:
					printCollinear(x,y,x,y+1,x,y+2)
		else:
			if y < len(world[x])-2:
				if world[x][y+1] != -1 and world[x][y+2] != -1:
					printCollinear(x,y,x,y+1,x,y+2)
		
print "  )"

# Generate objects
sys.stdout.write("  (:goal")
for x in range(len(world)):
	for y in range(len(world[x])):
		if world[x][y] == 3:
			sys.stdout.write(" (hasBlock c" + str(x) + str(y) + ")")
print ")"


print ")" # close domain problem file

# template
'''
for x in range(0, len(world)):
	for y in range(0, len(world[x])):
		if world[x][y] == 3:
			print "Goal!"
		elif world[x][y] == 2:
			print "Agent!"
		elif world[x][y] == 1:
			print "Block"
		elif world[x][y] == 0:
			print "Clear"
		elif world[x][y] == -1:
			print "Wall"
'''
	
