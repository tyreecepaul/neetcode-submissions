class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> dict;
        for (int i = 0; i < nums.size(); i++) {
            if (dict.count(nums[i])) {
                return true;
            }
            dict.insert({nums[i], 1});
        }
        return false;
    }
};