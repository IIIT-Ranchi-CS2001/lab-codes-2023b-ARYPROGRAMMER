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

	int arr[50];
	
	for (int i=0;i<51;i++)
	{
		arr[i]=i*10-i/2;
	}
	int n=50;
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			if (arr[i]<arr[j])
			{
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
	
	cout<<"\nbubble sorted : \n";
	for (int j=0;j<n;j++)
	{
		cout<<arr[j]<<" ";
	}
	
	
    return 0;
}
