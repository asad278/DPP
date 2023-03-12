#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &arr, int st, int e){
    int p = arr[st], cnt=0;
    for(int i=st+1; i<=e; i++){
        if(arr[i]<=p)
            cnt++;
    }
 
    int idx = st+cnt;
    swap(arr[idx], arr[st]);
 
    int i=st, j=e;
    while(i<idx and j>idx){
        while(arr[i]<=p) i++;
        while(arr[j]>p) j--;
 
        if(i<idx and j>idx)
            swap(arr[i++], arr[j--]);
    }
 
    return idx;
}

void quickSort(vector<int> &arr, int lo, int hi){
    jump:
    if(lo < hi){
        int pi = partition(arr, lo, hi);
        quickSort(arr, lo, pi-1);
        lo = pi+1;
        hi = hi;
        goto jump;
    }
}

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;

        vector<int> arr(n);
        for(int i=0; i<n; i++)
            cin >> arr[i];
        
        quickSort(arr, 0, n-1);

        for(int i=0; i<n; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
}
