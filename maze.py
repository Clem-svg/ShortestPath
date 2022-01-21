def neighbours(maze,node):
    i,j=node
    output=[]
    if 0<=i-1<len(maze) and maze[i-1][j]!='0':
        output.append((i-1,j))
    if 0<=i+1<len(maze) and maze[i+1][j]!='0':
        output.append((i+1,j))
    if 0<=j+1<len(maze) and maze[i][j+1]!='0':
        output.append((i,j+1))
    if 0<=j-1<len(maze) and maze[i][j-1]!='0':
        output.append((i,j-1))
    return output
        

def path_finder(maze):
    maze=maze.split('\n')
    visited={(0,0)}
    queue=[[(0,0),0]]

    while queue:
        current=queue.pop(0)
        if current[0]==(len(maze)-1,len(maze)-1):
            return current[1]
        for neighbour in neighbours(maze,current[0]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour,current[1]+1])
    return False


map = "\n".join([
"11111",
"11001",
"01101",
"01111",
"11011",
])

print(path_finder(map))
