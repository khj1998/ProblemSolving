def solution(n, m, x, y, r, c, k):
    ans = ''
    dist = abs(x-r) + abs(y-c)
    another = ''
    
    if dist > k or (k-dist)%2 == 1:
        return "impossible"
    
    down = max(r - x,0)
    left = max(y - c,0)
    right = max(c - y,0)
    up = max(x - r,0)
    pairs = (k-dist)//2
    
    for _ in range(k):
        if (down or pairs) and x < n:
            x+=1
            ans+='d'
            if down:
                down-=1
            else:
                pairs-=1
                up+=1
        elif (left or pairs) and y > 1:
            y-=1
            ans+='l'
            if left:
                left-=1
            else:
                pairs-=1
                right+=1
        elif (right or pairs) and y < m:
            y+=1
            ans+='r'
            if right:
                right-=1
            else:
                pairs-=1
                left+=1
        elif (up or pairs) and x > 1:
            x-=1
            ans += 'u'
            if up:
                up -= 1
            else:
                pairs-=1
                down+=1
            
    return ans