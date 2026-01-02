/**
 * LeetCode 1. 两数之和
 * 给定一个整数数组 nums 和一个整数目标值 target，
 * 请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
 * 假设每种输入只会对应一个答案，并且不能使用两次相同的元素。
 * 可以按任意顺序返回答案。
 */

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    /**
     * 使用哈希表查找两数之和的索引
     * 时间复杂度：O(n)，空间复杂度：O(n)
     * 
     * @param nums 输入数组
     * @param target 目标值
     * @return 两个数的索引组成的vector
     */
    vector<int> twoSum(vector<int>& nums, int target) {
        // 创建哈希表，key存储数组元素的值，value存储对应的索引
        unordered_map<int, int> numMap;
        
        // 遍历数组
        for (int i = 0; i < nums.size(); i++) {
            // 计算当前元素需要的补数
            int complement = target - nums[i];
            
            // 检查补数是否已经在哈希表中
            if (numMap.find(complement) != numMap.end()) {
                // 找到答案，返回两个索引
                return {numMap[complement], i};
            }
            
            // 将当前元素及其索引存入哈希表
            // key = nums[i] (数组元素的值)
            // value = i (元素在数组中的索引)
            numMap[nums[i]] = i;
        }
        
        // 根据题目假设，这里不会执行到（每个输入都有解）
        return {};
    }
};


//官方题解
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};


/**
 * 测试函数
 */
int main() {
    Solution solution;
    
    cout << "=== LeetCode 1. 两数之和 测试 ===" << endl;
    
    // 测试用例1：示例1
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = solution.twoSum(nums1, target1);
    cout << "测试用例1：" << endl;
    cout << "输入: nums = [2, 7, 11, 15], target = 9" << endl;
    cout << "输出: [" << result1[0] << ", " << result1[1] << "]" << endl;
    cout << "解释: nums[" << result1[0] << "] + nums[" << result1[1] 
         << "] = " << nums1[result1[0]] << " + " << nums1[result1[1]] 
         << " = " << target1 << endl;
    cout << endl;
    
    // 测试用例2：示例2
    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> result2 = solution.twoSum(nums2, target2);
    cout << "测试用例2：" << endl;
    cout << "输入: nums = [3, 2, 4], target = 6" << endl;
    cout << "输出: [" << result2[0] << ", " << result2[1] << "]" << endl;
    cout << "解释: nums[" << result2[0] << "] + nums[" << result2[1] 
         << "] = " << nums2[result2[0]] << " + " << nums2[result2[1]] 
         << " = " << target2 << endl;
    cout << endl;
    
    // 测试用例3：有重复元素
    vector<int> nums3 = {3, 3};
    int target3 = 6;
    vector<int> result3 = solution.twoSum(nums3, target3);
    cout << "测试用例3：" << endl;
    cout << "输入: nums = [3, 3], target = 6" << endl;
    cout << "输出: [" << result3[0] << ", " << result3[1] << "]" << endl;
    cout << "解释: nums[" << result3[0] << "] + nums[" << result3[1] 
         << "] = " << nums3[result3[0]] << " + " << nums3[result3[1]] 
         << " = " << target3 << endl;
    cout << endl;
    
    // 测试用例4：更大的数组
    vector<int> nums4 = {1, 5, 8, 12, 20, 30};
    int target4 = 28;
    vector<int> result4 = solution.twoSum(nums4, target4);
    cout << "测试用例4：" << endl;
    cout << "输入: nums = [1, 5, 8, 12, 20, 30], target = 28" << endl;
    cout << "输出: [" << result4[0] << ", " << result4[1] << "]" << endl;
    cout << "解释: nums[" << result4[0] << "] + nums[" << result4[1] 
         << "] = " << nums4[result4[0]] << " + " << nums4[result4[1]] 
         << " = " << target4 << endl;
    
    return 0;
}