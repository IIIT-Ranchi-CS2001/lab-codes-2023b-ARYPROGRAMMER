#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &vec, int low, int high) {


    int pivot = vec[low];

 
    int i = (high +1);

    for (int j = high; j >= low + 1; j--) {

      
        if (vec[j] >= pivot) {
            i--;
            swap(vec[i], vec[j]);
        }
    }

    swap(vec[i -1], vec[low]);


    return (i - 1);
}

void quickSort(vector<int> &vec, int low, int high) {


    if (low < high) {


        int p = partition(vec, low, high);


        quickSort(vec, low, p - 1);
        quickSort(vec, p + 1, high);
    }
}

int main() {
	int n;
	cout<<"enter length : ";
	cin>>n;
	cout<<"input :";
    vector<int> vec(n);
    for (int i=0;i<n;i++)
    {
    	cin>>vec[i];
	}
    int N = n;
    cout << "Unsorted Array: \n";
    for (auto i : vec) {
        cout << i << " ";
    }
    cout << endl;

    quickSort(vec, 0, N - 1);

    cout << "Sorted Array QUICKSORT 2: \n";
    for (auto i : vec) {
        cout << i << " ";
    }
    return 0;
}

