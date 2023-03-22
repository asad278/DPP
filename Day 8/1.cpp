#include<bits/stdc++.h>
using namespace std;

void dfs(int i, vector<bool> &vis, vector<vector<int>> &g){
    vis[i]=true;
    cout << i << " ";
    for(auto it: g[i]){
        if(!vis[it])
            dfs(it, vis, g);
    }
}

void bfs(int i, vector<bool> &vis, vector<vector<int>> &g){
    vis[i]=true;
    queue<int> q;
    q.push(i);

    while(!q.empty()){
        int it = q.front();
        q.pop();

        cout << it << " ";
        for(int u: g[it]){
            if(!vis[u]){
                q.push(u);
                vis[u]=true;
            }
        }
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
    cout << "DFS:\n";
    for(int i=0; i<=n; i++){
        if(!vis[i]){
            dfs(i, vis, g);
            cout << endl;
        }
    }

    for(int i=0; i<=n; i++) vis[i]=false;
    cout << "\nBFS:\n";
    for(int i=0; i<=n; i++){
        if(!vis[i]){
            bfs(i, vis, g);
            cout << endl;
        }
    }
}