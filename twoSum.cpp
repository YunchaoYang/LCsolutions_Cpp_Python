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
 vector是一个十分有用的容器,它能够像容器一样存放各种类型的对象
 基本函数实现 (1)头文件#include<vector>.
(2)创建vector对象，vector<int> vec;
(3)尾部插入数字：vec.push_back(a);
(4)使用下标访问元素，cout<<vec[0]<<endl;记住下标是从0开始的。
(5)使用迭代器访问元素.
vector<int>::iterator it;
for(it=vec.begin();it!=vec.end();it++)
    cout<<*it<<endl;
(6)插入元素：vec.insert(vec.begin()+i,a);在第i+1个元素前面插入a;
(7)删除元素：    vec.erase(vec.begin()+2);删除第3个元素
vec.erase(vec.begin()+i,vec.end()+j);删除区间[i,j-1];区间从0开始
(8)向量大小:vec.size();(9)清空:vec.clear();
————————————————

https://blog.csdn.net/duan19920101/java/article/details/50617190
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
