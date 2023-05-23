def solution(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num_dic = {}
    num = 0
    
    for i in range(len(nums)):
        num_dic[nums[i]] = numbers[i]
        
    ans,temp = '',''
    
    for char in s:
        if char in numbers:
            ans+=char
        else:
            temp+=char
        if temp in num_dic:
            ans+=num_dic[temp]
            temp = ''
    
    return int(ans)