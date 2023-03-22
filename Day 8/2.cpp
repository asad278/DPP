#include<bits/stdc++.h>
using namespace std;

void dfs(int i, vector<bool> &vis, vector<vector<int>> &g){
    vis[i]=true;
    for(auto it: g[i]){
        if(!vis[it])
            dfs(it, vis, g);
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n+1);
    for(int i=0; i<m; i++){
        int u, v;
        cin >> u >> v;

        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<bool> vis(n+1, false);
    bool cc=true;
    dfs(0, vis, g);
    for(int i=0; i<=n; i++){
        if(!vis[i]){
            cc=false;
            break;
        }
    }

    cout << (cc? "Connected" : "Non-Connected");
}
