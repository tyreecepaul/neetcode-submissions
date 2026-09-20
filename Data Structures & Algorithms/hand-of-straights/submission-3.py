"""
return whether we can split a ground of cards into groupSize hands with each hand being a straight (consecutive order)

e.g. hand = [1, 2, 4, 2, 3, 5, 3, 4], groupSize = 4
output: true ([1, 2, 3, 4], [2, 3, 4, 5])

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4
Output: false (closest we can get is [1, 2, 3, 4] and [3, 5, 6, 7])

observations:
- len(hands) % groupSize == 0? -> if this is not met, we can return False
- sorting (giving consecutive order)

-> [1, 2, 3, 4, 2, 3, 4, 5] (a lot of overlap when sorted [1, 2, 2, 3, 3, 4, 4, 5])

approach 1: sort then count
-> sort them initially
-> create hands that are of size == groupSize
-> select the 0th index and move on, if we have a duplicate then skip to next index
-> continue until no hands are left

def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    pot = hand[:]
    pot.sort()
    group = []
    
    i = 0
    while pot:
        # reset the pot
        if len(group) == groupSize:
            group = []
            i = 0

        # keep iterating until we value we want
        while pot[i] == group[-1]:
            i += 1

        if pot[i] != group[-1] + 1:
            return False
        temp = pot.pop(i)
        group.append(temp)
        del temp
        
        i += 1
    
    return True
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True

