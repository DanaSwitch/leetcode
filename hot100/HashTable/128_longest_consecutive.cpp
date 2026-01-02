#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <climits>
#include <chrono>

using namespace std;
using namespace chrono;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());//将nuns转化为hash集合
        int longestStreak = 0;
        
        for (int num : numSet) {
            // 只有当 num-1 不在集合中时，才作为序列的起点
            if (numSet.find(num - 1) == numSet.end()) {
            //begin() → 指向第一个元素, end() → 不指向任何有效元素，它是一个哨兵位置，表示“已经遍历完所有元素了”    
                int currentNum = num;
                int currentStreak = 1;
                
                // 向后查找连续的数字
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum++;
                    currentStreak++;
                }
                
                // 更新最长序列长度
                longestStreak = max(longestStreak, currentStreak);
            }
        }
        
        return longestStreak;
    }
};

// 简单的测试函数
void test() {
    Solution sol;
    
    cout << "=== Longest Consecutive Sequence Tests ===" << endl << endl;
    
    // 测试用例 1
    {
        vector<int> nums = {100, 4, 200, 1, 3, 2};
        int result = sol.longestConsecutive(nums);
        cout << "Test 1: ";
        cout << (result == 4 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 4)" << endl;
    }
    
    // 测试用例 2
    {
        vector<int> nums = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        int result = sol.longestConsecutive(nums);
        cout << "Test 2: ";
        cout << (result == 9 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 9)" << endl;
    }
    
    // 测试用例 3
    {
        vector<int> nums = {1, 0, 1, 2};
        int result = sol.longestConsecutive(nums);
        cout << "Test 3: ";
        cout << (result == 3 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 3)" << endl;
    }
    
    // 测试用例 4: 空数组
    {
        vector<int> nums = {};
        int result = sol.longestConsecutive(nums);
        cout << "Test 4: ";
        cout << (result == 0 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 0)" << endl;
    }
    
    // 测试用例 5: 单个元素
    {
        vector<int> nums = {5};
        int result = sol.longestConsecutive(nums);
        cout << "Test 5: ";
        cout << (result == 1 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 1)" << endl;
    }
    
    // 测试用例 6: 重复元素
    {
        vector<int> nums = {1, 2, 2, 3, 3, 3, 4};
        int result = sol.longestConsecutive(nums);
        cout << "Test 6: ";
        cout << (result == 4 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 4)" << endl;
    }
    
    // 性能测试
    cout << endl << "=== Performance Test ===" << endl;
    {
        vector<int> nums;
        // 生成10000个数字的乱序数组
        for (int i = 0; i < 10000; i++) {
            nums.push_back(i);
        }
        // 打乱顺序
        random_shuffle(nums.begin(), nums.end());
        
        auto start = high_resolution_clock::now();
        int result = sol.longestConsecutive(nums);
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start);
        
        cout << "Large array (10000 elements): ";
        cout << (result == 10000 ? "PASS" : "FAIL");
        cout << " (got " << result << ", expected 10000)";
        cout << " | Time: " << duration.count() << " ms" << endl;
    }
    
    cout << endl << "=== All Tests Completed ===" << endl;
}

int main() {
    test();
    return 0;
}