#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    // 读取矩阵
    vector<vector<int>> useTime(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> useTime[i][j];
        }
    }
    
    int k;
    cin >> k;
    k--; // 转换为0-based索引
    
    // 计算每个服务的入度（依赖数量）
    vector<int> indegree(n, 0);
    // 记录依赖关系
    vector<vector<int>> dependencies(n);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && useTime[i][j] == 1) {
                dependencies[j].push_back(i); // j被i依赖
                indegree[i]++;
            }
        }
    }
    
    // 每个服务的最早完成时间
    vector<int> completionTime(n, 0);
    
    // 拓扑排序队列
    queue<int> q;
    
    // 初始化：没有依赖的服务可以立即开始
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
            completionTime[i] = useTime[i][i]; // 只有自身启动时间
        }
    }
    
    // 拓扑排序
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        
        // 更新所有依赖curr的服务
        for (int dep : dependencies[curr]) {
            // dep的最早完成时间 = max(当前值, curr的完成时间 + dep自身时间)
            int candidateTime = completionTime[curr] + useTime[dep][dep];
            if (candidateTime > completionTime[dep]) {
                completionTime[dep] = candidateTime;
            }
            
            // 减少入度
            indegree[dep]--;
            if (indegree[dep] == 0) {
                q.push(dep);
            }
        }
    }
    
    // 输出服务k的最早完成时间
    cout << completionTime[k] << endl;
    
    return 0;
}