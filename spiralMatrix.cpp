/*
Input = 5

Output:
1	  2	  3  	4	  5	
16	17	18	19	6	
15	24	25	20	7	
14	23	22	21	8	
13	12	11	10	9

To get the reverse, initialize count to n*n in the begining. 
Also replace 'count=count+1' with 'count=count-1'

*/
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,j,count=0,k=0;
	int a[10][10];
	cin>>n;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			a[i][j]=0;
		}
	}
	i=0;
	j=0;
	while(count<n*n)
	{
		for(j=0+k;j<n-k;j++)
		{
			count=count+1;
			a[i][j]=count;
		}
		j=j-1;
		for(i=0+k+1;i<n-k;i++)
		{
			count=count+1;
			a[i][j]=count;
		}
		i=i-1;
		for(j=j-1;j>=0+k;j--)
		{
			count=count+1;
			a[i][j]=count; 

		}
		j=j+1;
		for(i=i-1;i>=0+k+1;i--)
		{
			count=count+1;
			a[i][j]=count;
		}
		k=k+1;
		i=k;
		j=k;

	}
	cout<<"Square"<<endl;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cout<<a[i][j]<<"\t";
		}
		cout<<endl;
	}
}
