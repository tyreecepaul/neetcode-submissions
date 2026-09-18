"""
reorganise string s.t. two adjacent characters are not the same

brute force:
- counter that counts number of elements in each string
- sort this counter
- then decrement downwards

edge case:
- "aaaa" -> not possible
return "" -> keeping track of the prev value used and checking if the only available option is that value

"axyy"
{"a": 0, "x": 0, "y": 1}
res = "yaxy"

"abbcccddd":
{"a": 1, "b": 1, "c": 1, "d": 1}
res = "dcdcbdcba"

"abbccdddd":
{"a": 0, "b": 0, "c": 0, "d": 0}
res = "dcdbdcdba"

approach:
- counter
- check what the largest value in that counter is
- decrement, add to string, set that as prev
- next time, check prev value when checking for largest value in that counter, 
    - if prev hit, then move onto 2nd largest and set that as the next prev
    - if there is no other values that can be set other than prev, return ""

class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        res = []
        prev = None

        while any(cnt.values()):    # checks that at least one value in dict is not 0
            candidates = [k for k, v in cnt.items() if k != prev and v > 0]

            if not candidates:
                return ""
            max_char = max(candidates, key=lambda k: cnt[k])

            prev = max_char
            cnt[max_char] -= 1
            res.append(max_char)

        return "".join(res)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None        
        res = []

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        
        return "".join(res)



