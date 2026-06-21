class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sDict;
        unordered_map<char, int> tDict;
        for (char c : s) {
            sDict[c]++;
        }
        for (char c : t) {
            tDict[c]++;
        }
        return sDict == tDict;
    }
};
