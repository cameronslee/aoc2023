with open('input.txt') as f:
  lines = f.readlines()

part1 = 0
board = [[] for j in range(0,len(lines))]

def is_symbol(c):
  return ((not c.isnumeric()) and (not c == '.'))

def in_bounds(i,j,m,n):
  if i < 0 or j < 0 or i >= m or j >= n:
    return False
  return True

def scan(board, m, n, i, j):
  if (in_bounds(i-1,j,m,n) and is_symbol(board[i-1][j]) or 
      in_bounds(i+1,j,m,n) and is_symbol(board[i+1][j]) or 
      in_bounds(i,j-1,m,n) and is_symbol(board[i][j-1]) or 
      in_bounds(i,j+1,m,n) and is_symbol(board[i][j+1]) or 
      in_bounds(i-1,j-1,m,n) and is_symbol(board[i-1][j-1]) or 
      in_bounds(i-1,j+1,m,n) and is_symbol(board[i-1][j+1]) or 
      in_bounds(i+1,j-1,m,n) and is_symbol(board[i+1][j-1]) or 
      in_bounds(i+1,j+1,m,n) and is_symbol(board[i+1][j+1])): 
        return True

def get_num(board,i,j):
  left = j
  right = j
  while left >= 0 and board[i][left].isnumeric():
    left -= 1
  while right < len(board[i]) and board[i][right].isnumeric():
    right += 1

  res = board[i][left+1:right]
  ans = ''.join(res)
  ans = int(ans)

  return ans

def scan2(board, m, n, i, j):
  res = 0
  res2 = []
  if in_bounds(i-1,j,m,n) and board[i-1][j].isnumeric():
    res2.append(get_num(board,i-1,j))

  if in_bounds(i+1,j,m,n) and board[i+1][j].isnumeric():
    res2.append(get_num(board,i+1,j))

  if in_bounds(i,j-1,m,n) and board[i][j-1].isnumeric():
    res2.append(get_num(board,i,j-1))

  if in_bounds(i,j+1,m,n) and board[i][j+1].isnumeric():
    res2.append(get_num(board,i,j+1))

  if in_bounds(i-1,j-1,m,n) and board[i-1][j-1].isnumeric():
    res2.append(get_num(board,i-1,j-1))
    
  if in_bounds(i-1,j+1,m,n) and board[i-1][j+1].isnumeric():
    res2.append(get_num(board,i-1,j+1))

  if in_bounds(i+1,j-1,m,n) and board[i+1][j-1].isnumeric():
    res2.append(get_num(board,i+1,j-1))
    
  if in_bounds(i+1,j+1,m,n) and board[i+1][j+1].isnumeric():
    res2.append(get_num(board,i+1,j+1))

  res2 = list(set(res2))
  res = len(res2)
  
  print("RETURNING", res, res2)

  return res, res2

for i in range(0,len(lines)):
  lines[i] = lines[i].strip('\n')
  for c in lines[i]:
    board[i].append(c)


for i in range(0,len(board)):
  j = 0
  while j < len(board[i]):
    left = j
    right = j
    if board[i][j].isnumeric():
      if scan(board,len(board),len(board[i]),i,j):
        
        while left >= 0 and board[i][left].isnumeric():
          left -= 1
        while right < len(board[i]) and board[i][right].isnumeric():
          right += 1

        res = board[i][left+1:right]
        ans = ''.join(res)
        ans = int(ans)
        print(ans)
        part1 += ans
        j = right
    j += 1

print("PART 1: ", part1)

# gear ratios
part2 = 0

for i in range(0,len(board)):
  j = 0
  while j < len(board[i]):
    if board[i][j] == '*':
      s = scan2(board,len(board),len(board[i]),i,j)
      if s[0] == 2:
        part2 += s[1][0] * s[1][1]
    j += 1
      
print("PART 2: ", part2)
