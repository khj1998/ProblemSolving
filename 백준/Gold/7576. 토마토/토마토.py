import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [-1,1,0,0],[0,0,-1,1]

def get_solution():
   ans = -1

   while q:
      x,y,days = q.popleft()

      for i in range(4):
         px = x+dx[i]
         py = y+dy[i]

         if 0<=px<N and 0<=py<M:
            if check[px][py] != -1:
               continue
            if box[px][py] == 0:
               box[px][py] = 1
               check[px][py] = days+1
               q.append((px,py,days+1))

   for i in range(N):
      for j in range(M):
         if box[i][j] == 0:
            return -1

   for i in range(len(check)):
      ans = max(ans,max(check[i]))

   return ans

if __name__=="__main__":
   q = deque()
   M,N = map(int,input().split())
   check = [[-1]*M for _ in range(N)]

   days = 0
   box = []

   for _ in range(N):
      box.append(list(map(int,input().split())))

   for i in range(N):
      for j in range(M):
         if box[i][j] == 1:
            q.append((i,j,0))
            check[i][j] = 0

   ans = get_solution()
   print(ans)