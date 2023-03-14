#include <bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>

using namespace std;

// ordered_set
using namespace __gnu_pbds;
template<class T>
using opset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

#define pb              push_back
#define ppb             pop_back
#define eb              emplace_back
#define int             long long
#define ub              upper_bound
#define lb              lower_bound
#define v(T)            vector<T>
#define p(T1, T2)       pair<T1, T2>
#define pq(T)           priority_queue<T>
#define ump(T1, T2)     unordered_map<T1, T2>
#define f(i, a, b)      for (int i = a; i < b; i++)
#define rf(i, a, b)     for(int i = a; i >= b; i--)
#define fv(i, vec)      for (auto &i : vec)
#define fj(i, a, b, j)  for (int i = a; i < b; i+=j)
#define fc(i, a, b)     for (char i = a; i <= b; i++)
#define ln              "\n"
#define inarr(v, n)     f(i, 0, n) cin >> v[i];
#define outarr(v)       fv(i, v) cout << i << ' '; cout << ln;
#define all(x)          (x).begin(), (x).end()
#define rall(x)         (x).rbegin(), (x).rend()
#define fastio          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define ff              first
#define ss              second
#define setbit(x)       __builtin_popcount(x)
#define setbitll(x)     __builtin_popcountll(x)
#define sq(x) ((x)*(x))

void solve(){
    int n;
    cin >> n;

    v(string) s(n);
    inarr(s, n);

    ump(string, v(string)) mp;
    f(i, 0, n){
        string tmp(s[i]);
        sort(all(tmp));
        mp[tmp].pb(s[i]);
    }

    fv(i, mp){
        fv(j, i.ss)
            cout << j << " ";
        cout << ln;
    }
}

signed main(){
    fastio;

    int tc; 
    cin >> tc;

    while(tc--){
        solve();
    }
}
