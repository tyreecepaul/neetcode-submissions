class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            string = t
            sub_string = s
        else:
            string = s
            sub_string = t

        count = Counter(string)
        for letter in sub_string:
            for count_letter in count:
                if letter == count_letter:
                    count[count_letter] -= 1
        
        return all(value == 0 for value in count.values())