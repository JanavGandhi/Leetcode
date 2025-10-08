class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int ArrayLength = nums.size();
        for (int i = 0;i < ArrayLength;i++){
            for(int j = i+1; j < ArrayLength; j++){
                if (nums[i]+nums[j]==target){
                    return {i,j};
                }
            }
        }
        return {};
    }
};