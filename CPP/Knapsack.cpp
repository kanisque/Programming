//Knapsack 0/1
#include<bits/stdc++.h>
using namespace std;
int dp[11][11];

int ks(int n,int c[],int w[],int k)
{
    if(n<=0 or k==0)
        return 0;

    if(dp[n][k]!=0)
        return dp[n][k];

    if(w[n-1]>k)
        return ks(n-1,c,w,k);

    int take = ks(n-1,c,w,k-w[n-1]) + c[n-1];
    int leave = ks(n-1,c,w,k);
    int ans=max(take,leave);
    dp[n][k]=ans;
    return ans;
}

int main(){
    int cost[]={1,2,3,1,2,3,5,2,7,1};
    int weight[]={2,1,4,5,2,6,1,3,6,3};
    int kapacity=10;
    int n=sizeof(cost)/sizeof(cost[0]);
    cout<<ks(n,cost,weight,kapacity)<<endl;
return 0;
}
