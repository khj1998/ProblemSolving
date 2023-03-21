import sys
import math
input = sys.stdin.readline

def get_prime(number):
   prime = [True for _ in range(number+1)]
   ans = []

   for i in range(2,int(math.sqrt(number))+1):
      if prime[i] == True:
         j = 2
         while i*j <= number:
            prime[i*j] = False
            j+=1

   for i in range(2,number+1):
      if prime[i] == True:
         ans.append(i)

   return ans

if __name__=="__main__":
   N = int(input())

   if N==1:
      print(0)
      exit(0)

   ans = 0
   array = get_prime(N)

   start_idx,end_idx = 0,0
   length = len(array) - 1
   now_sum = array[0]

   while end_idx<=length:
      if now_sum <= N:
         if now_sum == N:
            ans+=1
         end_idx+=1
         if end_idx >length:
            break
         now_sum += array[end_idx]
      else:
         now_sum -= array[start_idx]
         start_idx += 1

   print(ans)