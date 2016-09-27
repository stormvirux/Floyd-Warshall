import sys



def pathshortest(path,pathMatrix,i,j):
		
	if i == j:
		path.append(i)	
	elif pathMatrix[i][j] is None:
		print "No path exists"       		
		return []
   	
	else:
   		pathshortest(path,pathMatrix, i, pathMatrix[i][j])
       		path.append(j)
	return path
	

graphFile = open("grafo.txt")

size = graphFile.readline() 						
size = int(size) 							
graphMatrix = [[]] * size
pathMatrix = [[0 for x in range(size)] for x in range(size)] 
						

for i in range(size):
	graphMatrix[i] = graphFile.readline()
	graphMatrix[i] = graphMatrix[i].lower().replace(' ', '').replace('\n', '')
	graphMatrix[i] = graphMatrix[i].split(',')

graphFile.close()

for i in range(size):
	for j in range(size):
		if graphMatrix[i][j] == 'n':
			graphMatrix[i][j] = sys.maxint
			pathMatrix[i][j] = None
		else:
			graphMatrix[i][j] = int(graphMatrix[i][j])
			pathMatrix[i][j] = i

resultMatrix = graphMatrix
		


for k in range(size):
	for i in range(size):
		for j in range(size):
			if (resultMatrix[i][j] > resultMatrix[i][k] + resultMatrix[k][j]):
				resultMatrix[i][j] = resultMatrix[i][k] + resultMatrix[k][j]
				pathMatrix[i][j] = pathMatrix[k][j]

resultFile = open("resultado.txt", 'w')


for i in range(size):
	resultFile.write(str(resultMatrix[i]).strip('[]') + '\n')

resultFile.close()

while True:
	u = raw_input("\n\nEnter Soursce Node:")
	v = raw_input("\n\nEnter Destination Node:")
	print "The shortest path is through \n"
	path = []
	pathfinal = pathshortest(path,pathMatrix,int(u)-1,int(v)-1)
	print map(lambda x:x+1, pathfinal)
	print "The shortest distance is \n"
	print resultMatrix[int(u)-1][int(v)-1]
	exit = raw_input("\n\nDo you want to exit[Y or y]")
	if exit == 'Y' or exit == 'y':
		break

	
