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
        g[v].push_back(u);
    }

    bool cycle=false;
    vector<bool> vis(n+1, false);
    for(int i=0; i<n; i++){
        if(!vis[i]){
            queue<int> q;
            q.push(i);
            vis[i] = true;
            vector<int> par(n+1, -1);
            
            while(!q.empty()){
                int it = q.front();
                q.pop();
        
                for(int u: g[it]){
                    if(!vis[u]){
                        vis[u] = true;
                        q.push(u);
                        par[u] = it;
                    }
                    else if(par[it]!=u)
                        cycle = true;
                }
            }
        }
    }

    cout << (cycle? "Cyclic Graph" : "Acyclic Graph");
}
