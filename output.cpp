#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int n = s.length();
    int a[n];
    int k = 0;
    for(int i=0;i<n;i++)
    {
        if(s[i]!='+')
        {
            a[k] = s[i]-'0';
            k++;
        }
    }
    sort(a,a+k);
    for(int i=0;i<k;i++)
    {
        if(i==k-1)
            cout<<a[i];
        else
            cout<<a[i]<<"+";
    }
    return 0;
}