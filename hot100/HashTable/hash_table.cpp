#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class SimpleHashTable {
private:
    static const int TABLE_SIZE = 1000;
    vector<pair<int, int>> table[TABLE_SIZE];  // 使用链地址法解决冲突
    
    int hashFunction(int key) {
        return abs(key) % TABLE_SIZE;
    }
    
public:
    void insert(int key, int value) {
        int index = hashFunction(key);
        table[index].push_back({key, value});
    }
    
    bool find(int key, int& value) {
        int index = hashFunction(key);
        for (const auto& pair : table[index]) {
            if (pair.first == key) {
                value = pair.second;
                return true;
            }
        }
        return false;
    }
};

int main() {
    // 创建一个电话簿：key=姓名，value=电话号码
    unordered_map<string, string> phonebook;
    
    // 添加联系人
    phonebook["Alice"] = "13800138000";
    phonebook["Bob"] = "13900139000";
    phonebook["Charlie"] = "13700137000";
    
    // 用户想要查找Alice的电话号码
    string name = "Alice";  // key
    
    // 查找
    if (phonebook.find(name) != phonebook.end()) {
        string phoneNumber = phonebook[name];  // value
        cout << name << " 的电话是：" << phoneNumber << endl;
        // 输出：Alice 的电话是：13800138000
    }
    
    // 用户想要Bob的电话
    cout << "Bob的电话:" << phonebook["Bob"] << endl;
    // 输出：Bob的电话：13900139000
    
    return 0;
}
