
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i,j ;       	
        vector<int> result;
        for(i=0; i<nums.size()-1; i++)
        {
            for(j=i+1; j<nums.size(); j++)
            {
                if( nums[i] + nums[j] == target)  
                {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }  
                
            }                       
        }
     return result;    
    }
};

void print_vec(const vector<int>& vec){
for (int ele: vec){
    cout << ele << '\t';
}
}

int main() {

    vector<int> nums = {2,7,5,10};
    int target = 9;
    print_vec(Solution().twoSum(nums, target));

    return 0;
}
