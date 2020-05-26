/*
First attempt for the twoSum problem in Leetcode.
Use Brute force iterator method in for loop.
Y. Yang
To learn:
1) basic grammar  
2) nested loop
3) vector class template: 
 (1) member types: 
 (2) Member functions:
 基本函数实现 (1) 构造函数 (2)增加函数 (3) 删除函数 遍历函数

  https://www.runoob.com/w3cnote/cpp-vector-container-analysis.html
*/
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
