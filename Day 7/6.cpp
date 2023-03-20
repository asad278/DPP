class Solution {
  public:
    Node *mapPar(Node *node, map<Node*, Node*> &par, int tar){
        queue<Node*> q;
        q.push(node);
        Node *pos;
        while(!q.empty()){
            Node *curr = q.front();
            q.pop();
            if(curr->data == tar) pos=curr;
            if(curr->left){
                par[curr->left] = curr;
                q.push(curr->left);
            }
            if(curr->right){
                par[curr->right] = curr;
                q.push(curr->right);
            }
        }
        
        return pos;
    }
    
    int mxDist(map<Node*, Node*> &par, Node* start){
        queue<Node*> q;
        q.push(start);
        map<Node*, int> vis;
        vis[start]=1;
        int mx=0;
        while(!q.empty()){
            int sz = q.size();
            bool found=false;
            for(int i=0; i<sz; i++){
                Node *node = q.front();
                q.pop();
                
                if(node->left and !vis[node->left]){
                    found=true;
                    vis[node->left]=1;
                    q.push(node->left);
                }
                if(node->right and !vis[node->right]){
                    found=true;
                    vis[node->right]=1;
                    q.push(node->right);
                }
                
                if(par[node] and !vis[par[node]]){
                    found=true;
                    vis[par[node]]=1;
                    q.push(par[node]);
                }
            }
            
            if(found) mx++;
        }
        
        return mx;
    }
    
    int minTime(Node* root, int tar) {
        map<Node*, Node*> par;
        Node* start = mapPar(root, par, tar);
        return mxDist(par, start);
    }
};
