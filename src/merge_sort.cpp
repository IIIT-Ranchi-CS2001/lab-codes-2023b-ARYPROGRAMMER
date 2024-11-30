#include <iostream>
using namespace std;


void printArray(int * arr, int length) {
    for (int i = 0; i < length; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


void merge(int * arr, int low, int mid, int high) {
    int i, j, k;
    i = low;
    j = mid + 1;
    k = low;


    int temp[20];

    while (i <= mid && j <= high) {
 
        if (arr[i] < arr[j]) {
            temp[k] = arr[i];
            i++;
        } else {
            temp[k] = arr[j];
            j++;
        }
        k++;
    }

 
    while (i <= mid) {
        temp[k] = arr[i];
        i++;
        k++;
    }

  
    while (j <= high) {
        temp[k] = arr[j];
        j++;
        k++;
    }


    for (int i = low; i <= high; i++) {
        arr[i] = temp[i];
    }
}


void mergeSort(int * arr, int low, int high) {
    int mid;
    if (low < high) {
      
        mid = (low + high) / 2;


        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);

        merge(arr, low, mid, high);
    }
}

int main() {
    
    int n;
	cout<<"enter length : ";
	cin>>n;
	cout<<"input :";
    int arr[n]; 
    for (int i=0;i<n;i++)
    {-
    	cin>>arr[i];
	}
   


    int length = n;

    cout << "Array before : ";
    printArray(arr, length);


    mergeSort(arr, 0, length - 1);


    cout << "Array, after MERGE SORT: ";
    printArray(arr, length);
    return 0;
}


