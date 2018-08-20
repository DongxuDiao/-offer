# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        n =len(s)
        for i in range(n):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)