def longestValidParentheses(s: str) -> int:
    if s == "": return 0
    if s == "()": return 2
    if len(s) == 2 or len(s) == 1: return 0
    
    ret = 0
    memo = [0 for i in range(len(s))]
    for i in range(1,len(s)):
        if s[i] == '(':
            continue
        if s[i-1] == '(':
            memo[i] = memo[i-2]+2
            ret = max(ret, memo[i])
            continue
        index = i -1
        while memo[index]!= 0:
            index = index - memo[index]
        if index < 0 : continue
        if s[index] == '(':
            memo[i] = i-index+1+memo[index-1]
            ret = max(ret, memo[i])
    return ret
print(longestValidParentheses("(()))())("))
