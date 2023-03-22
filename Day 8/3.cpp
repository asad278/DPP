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

    vector<int> color(n+1, -1);
    bool bi=true;
    for(int i=0; i<n; i++){
        if(color[i]==-1){
            queue<int> q;
            q.push(i);
            color[i]=0;
            
            while(!q.empty()){
                int it = q.front();
                q.pop();
        
                for(int u: g[it]){
                    if(color[u]==-1){
                        color[u] = !color[it];
                        q.push(u);
                    }
                    else if(color[it]==color[u]){
                        bi = false;
                        break;
                    }
                }
        
                if(!bi) break;
            }
        }
    }

    cout << (bi? "Bipartite" : "Non-Bipartite");
}
