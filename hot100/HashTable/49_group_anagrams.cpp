#include<iostream>
#include<unordered_map>
#include<vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        
        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (const auto& pair : groups) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};

// 测试函数
int main() {
    Solution sol;
    
    // 测试示例1
    vector<string> strs1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
    auto result1 = sol.groupAnagrams(strs1);
    
    cout << "Test 1:" << endl;
    for (const auto& group : result1) {
        cout << "[";
        bool first = true;
        // 使用范围for循环，完全避免索引
        for (const auto& word : group) {
            if (!first) cout << ",";
            cout << word;
            first = false;
        }
        cout << "]" << endl;
    }
    
    return 0;
}
