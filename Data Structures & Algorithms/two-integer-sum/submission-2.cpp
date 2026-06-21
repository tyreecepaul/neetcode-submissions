class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prevNums;

        for (int i = 0; i < nums.size(); i++) {
            int comp = target - nums[i];
            if (prevNums.find(comp) != prevNums.end()) {
                return {prevNums[comp], i};
            }
            prevNums.insert({nums[i], i});
        }
        return {};
    }
};
