# begin with an s
# for each group on consecutive repeating chars
#   if group length is 1, append to char s
#   o/w appeand to char followed by group's length

# compresed string s should NOT be returned separetely
# stored in input char array chars
# input lengths 10 or longer will be split into multiple chars in chars
# e.g. 10 represented as ["1", "0"]

# k is length of compreseded string s 
# modify first k chars of chars array and return k

"""
example 1:
Input: chars = ["a","a","a","a","a","a","a","a","a","a","a"]
- compressed string is "a11" (len == 3), 
- for which first 3 chars of the input array should be ["a", "1", "1"]
Output: 3

example 2: 
Input: chars = ["A"]
- compresed: "A" (not "A1" since its by itself)
- first 1 chars of input array should be ["A"]
Output: 1 

example 3:
Input: chars = ["1","1","2"]
- compressed: "122" (two 1's and one 2)
- length of 3, so first 3 should be ["1", "2", "2"]
Output: 3

psuedocode:
init compressed string
int cnt

# getting the compressed form
str prev character being comapred to (initalise as first value in chars)
loop over the chars array (starting from 1 since 0 is initalised)
    check whether the existing is == prev
        if true
            cnt++
        else:
            turn prev and cnt into compressed form
            append it to the compressed string
            reset cnt to 0
            set prev == to current iteration in loop

# replace the values
k = len(compressed) this is our return and our loop iteration
(we could convert into a list but then using extra space)
for i, c in enumerate(compressed)
    chars[i] = c

return k
"""

"""
example 1:
Input: chars = ["a","a","a","a","a","a","a","a","a","a","a"]
- compressed string is "a11" (len == 3), 
- for which first 3 chars of the input array should be ["a", "1", "1"]
Output: 3

compressed = ""
cnt = 1
prev = a

i = 1

class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = ""
        cnt = 1
        prev = chars[0]
    
        # compressing string
        for i in range(1, len(chars)):
            if chars[i] != prev:    # compressing
                temp = prev + str(cnt) if cnt not in [0, 1] else prev
                compressed += temp
                cnt = 0
                prev = chars[i]
            cnt += 1
        
        # compresse remaining
        temp = prev + str(cnt) if cnt != 1 else prev
        compressed += temp
        print(compressed)

        k = len(compressed)     # defn k

        for i, c in enumerate(compressed):
            chars[i] = c ### check for string in case error
        
        return k
"""

class Solution:
    def compress(self, chars):
        n = len(chars)
        k = i = 0

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            i = j
        return k




