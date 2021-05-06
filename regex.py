class Solution:
    def isMatch(self,s: str, p: str) -> bool:
        p_new = [None]
        for x in range(len(p)):
            if p[x] == '*':
                p_new.pop(-1)
                p_new.append(p[x-1:x+1])
            else:
                p_new.append(p[x])
        s = '0' + s
        
        self.memo = [[False for i in range(len(s))] for j in range(len(p_new))]
        self.memo[0][0] = True
        for i, temp in enumerate(p_new):
            if i == 0: continue
            if len(temp) == 2:
                self.memo[i][0] = True
            else:
                break
                
        for col in range(1, len(s)):
            for row in range(1, len(p_new)):
                if len(p_new[row]) > 1 and (p_new[row][0] == s[col] or p_new[row][0] == '.'):
                    if self.memo[row][col-1] or self.memo[row-1][col-1] or self.memo[row-1][col]:
                        self.memo[row][col] = True
                elif len(p_new[row]) > 1:
                    if self.memo[row-1][col]:
                        self.memo[row][col] = True
                elif p_new[row] == s[col] or p_new[row] == '.':
                    if p_new[row] == s[col]:
                        if p_new[:row+1].count(p_new[row]) > s[:col+1].count(p_new[row]):
                            self.memo[row][col] = False
                        elif self.memo[row-1][col-1]:
                            self.memo[row][col] = True

                    if p_new[row] == '.':
                        if p_new[:row+1].count('.') > col:
                            self.memo[row][col] = False
                        elif self.memo[row-1][col-1]:
                            self.memo[row][col] = True
                else:
                    self.memo[row][col] = False
        return self.memo[len(p_new)-1][len(s)-1]
