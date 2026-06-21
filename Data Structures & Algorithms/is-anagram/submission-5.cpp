class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> sDict;
        unordered_map<char, int> tDict;
        for (int i = 0; i < s.length(); i++) {
            sDict[s[i]]++;
            tDict[t[i]]++;
        }
        return sDict == tDict;
    }
};
