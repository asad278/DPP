#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n+1);
    for(int i=0; i<m; i++){
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
    }

    vector<int> indeg(n+1, 0);
    for(int i=0; i<n; i++){
        for(auto it: g[i])
            indeg[it]++;
    }

    queue<int> q;
    for(int i=0; i<n; i++){
        if(indeg[i]==0)
            q.push(i);
    }

    vector<int> topo;
    while(!q.empty()){
        int it = q.front();
        q.pop();
        topo.push_back(it);

        for(int i: g[it]){
            indeg[i]--;
            if(indeg[i]==0)
                q.push(i);
        }
    }

    for(int i: topo)
        cout << i << " ";
}
