#include <iostream>
using namespace std;

int main(){
	int arr[100];int n;
	cout<<"enter n : ";
	cin>>n;
	for (int i=0;i<n;i++)
	{
		int o;
		cout<<"enter element: ";
		cin>>o;
		arr[i]=o;
	}
		
		
		
	for (int i=1;i<n;i++)
	{
		int k = arr[i];
		int j=i-1;
		
		while (k<arr[j]&&j>=0)
		{
			arr[j+1]=arr[j];
			--j;
				
		}	
		arr[j+1]=k;
	
	}
	
	
	
	
	cout<<"\ninsertion sorted : \n";
	for (int j=0;j<n;j++)
	{
		cout<<arr[j]<<" ";
	}
	
	
    return 0;
}
