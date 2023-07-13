//{ Driver Code Starts
// Initial Template for C++

#include<iostream>
#include<conio.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int nCr(int n, int r){
        if (r>n){
            return 0;
        }
        // code here
        long long combination = factorial(n)/(factorial(n-r)*factorial(r));
        return combination%1000000007;
    }
    long long factorial(int n){
        return (n<2) ? 1 : n*factorial(n-1);
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, r;
        cin>>n>>r;
        
        Solution ob;
        cout<<ob.nCr(n, r)<<endl;
        getche();
    }
    return 0;
}
// } Driver Code Ends
//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
#define MAX 1000

// } Driver Code Ends
class Solution
{
    public:
    /*You are required to complete this method*/
    int findK(int a[MAX][MAX],int n,int m,int k)
    {
        int v, w = k, x=0, y=0, X0=0, Y0=0, X1=n-1, Y1=m-1;
        char direction1 = 'h',direction2 = '+';//h for horizontal v for vertical
        while(w>0){
            v=a[y][x];
            w--;
            if (direction1=='h'){
                if (x==X1){
                    direction1='v';
                    X1--;
                }
                else if(direction2=='+'){
                    x++;
                }
                else if(direction2=='-'){
                    x--;
                
                }
                else if(x==X0){
                    direction1 = 'v';
                    X0++;
                }
            }
            else if(direction1=='v'){
                if (y==Y1){
                    direction1='h';
                    Y1--;
                    direction2='+';
                }
                else if(direction2=='+'){
                    y++;
                }
                else if(direction2=='-'){
                    y--;
                }
                else if(y==Y0){
                    direction1 = 'h';
                    Y0++;
                    direction2='-';
                }
            }
        }
        return v;
    }
};





//{ Driver Code Starts.
int main()
{
    int T;
    cin>>T;
  
    while(T--)
    {
        int n,m;
        int k=0;
        //cin>>k;
        cin>>n>>m>>k;
        int a[MAX][MAX];
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }
        Solution ob;
        cout<<ob.findK(a,n,m,k)<<endl;
        
       
    }
}
// } Driver Code Ends