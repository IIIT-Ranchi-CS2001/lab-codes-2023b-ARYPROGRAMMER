#include <iostream>
using namespace std;

int main(){
//	int arr[100];int n;
//	cout<<"enter n : ";
//	cin>>n;
//	for (int i=0;i<n;i++)
//	{
//		int o;
//		cout<<"enter element: ";
//		cin>>o;
//		arr[i]=o;
//	}
	long long int arr[10000];
	
	for (long long int i=0;i<10000;i++)
	{
		arr[i]=i*10-i/2;
	}
	
	long long int n=10000;	
	long long int loc;
	long long int min;
	
	for (long long int i=0;i<n;i++)
	{
		min=arr[i];
		loc=i;
		for (int j=i+1;j<n;j++)
		{
			if (arr[j]<min)
			{
				min = arr[j];
				loc=j;
			}
		}
		int temp=arr[i];
		arr[i]=min;
		arr[loc]=temp;
	}
	
	
	
	
	
	
	cout<<"\nselection sorted : \n";
	for (int j=0;j<n;j++)
	{
		cout<<arr[j]<<" ";
	}
	
	
    return 0;
}
