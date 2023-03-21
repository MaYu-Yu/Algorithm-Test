package myPackage;

import java.util.Collections;

public class Sort {
	public void print(int[] arr) {
		System.out.print("Array : ");
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	public void swapArrElement(int[] arr, int x, int y) {
		int temp = arr[x];
		arr[x] = arr[y];
		arr[y] = temp;
	}

	// 選擇排序
	public void selectionSort(int[] arr) {
		int size = arr.length - 1;
		for (int i = 0; i < size; i++) {
			int mininum = i;
			for (int j = i + 1; j < size + 1; j++) {
				if (arr[mininum] > arr[j])
					mininum = j;
			}
			swapArrElement(arr, i, mininum);
		}
	}

	// 氣泡排序
	public void bubbleSort(int[] arr) {
		int size = arr.length - 1;
		Boolean isChanged = true;
		for(int i = size; isChanged && i > 0; i--) {
			isChanged = false;
			for(int j = 0; j < i; j++) {
				if (arr[j] > arr[j + 1] ) {
					isChanged = true;
					swapArrElement(arr, j, j+1);
				}
			}
		}
	}
	// 插入排序
	public void insertSort(int[] arr) {
		for (int i = 1; i < arr.length; i++) {
			for (int j = i; j > 0 && arr[j - 1] > arr[j]; j--) {
				swapArrElement(arr, j, j - 1);
			}
		}
	}

	// 希爾排序
	public void shellSort(int[] arr) {
		for (int step = arr.length / 2; step > 0; step /= 2) {
			for (int i = step; i < arr.length; i += step) {
				for (int j = i; j >= step &&  arr[j - step] > arr[j]; j -= step) {
					swapArrElement(arr, j, j - step);
				}
			}
		}
	}

	// 歸併排序
	private void merge(int[] arr, int left, int mid, int right) {
		int[] temp = new int[right - left + 1];
		int i = left, j = mid + 1, k = 0;
		while (i <= mid && j <= right) {
			if (arr[i] < arr[j]) {
				temp[k++] = arr[i++];
			} else {
				temp[k++] = arr[j++];
			}
		}
		while (i <= mid)
			temp[k++] = arr[i++];
		while (j <= right)
			temp[k++] = arr[j++];
		for (int n = 0; n < temp.length; n++)
			arr[left + n] = temp[n];
	}

	private void mergeSort(int[] arr, int left, int right) {
		if (left < right) {
			int mid = (left + right) / 2;
			mergeSort(arr, left, mid);
			mergeSort(arr, mid + 1, right);
			merge(arr, left, mid, right);
		}
	}

	public void mergeSort(int[] arr) {
		mergeSort(arr, 0, arr.length - 1);
	}
	// 堆積排序

	void heapify(int arr[], int n, int i) {
		// Find largest among root, left child and right child
		int largest = i;
		int left = 2 * i + 1;
		int right = 2 * i + 2;

		if (left < n && arr[left] > arr[largest])
			largest = left;

		if (right < n && arr[right] > arr[largest])
			largest = right;

		if (largest != i) {
			swapArrElement(arr, i, largest);
			heapify(arr, n, largest);
		}
	}

	public void heapSort(int[] arr) {
		int n = arr.length;
		for (int i = 0; i < n; i++)
			arr[i] = arr[i] * n + i; // stable

		for (int i = n / 2 - 1; i >= 0; i--) {
			heapify(arr, n, i);
		}
		for (int i = n - 1; i >= 0; i--) {
			swapArrElement(arr, 0, i);
			heapify(arr, i, 0);
		}

		for (int i = 0; i < n; i++)
			arr[i] = arr[i] / n; // stable recovery to previous array
	}

	// 快速排序
	private void quickSort(int[] arr, int l, int r) {
		if (l >= r)
			return;
		int target = arr[l];
		int i = l + 1, j = r;
		while (i <= j) {
			while (i <= j && target < arr[j])
				j -= 1;
			while (i <= j && target >= arr[i])
				i += 1;
			if (i < j)
				swapArrElement(arr, i, j);
		}
		swapArrElement(arr, l, j);
		quickSort(arr, l, j - 1);
		quickSort(arr, j + 1, r);
	}

	public void quickSort(int[] arr) {
		quickSort(arr, 0, arr.length - 1);
	}
	
	private int partition(int[] arr, int low, int high)
	{
	    int pivot = arr[high];
	    int i = low - 1;
	 
	    for(int j = low; j < high; j++)
	    {
	        if (arr[j] < pivot)
	        {
	            i++;
	            swapArrElement(arr, i, j);
	        }
	    }
	    swapArrElement(arr, i + 1, high);
	    return i + 1;
	}
	private void quickSort2(int[] arr, int low, int high)
	{
	    if (low < high)
	    {
	        int mid = partition(arr, low, high);
	        quickSort2(arr, low, mid - 1);
	        quickSort2(arr, mid + 1, high);
	    }
	}
	public void quickSort2(int[] arr) {
		quickSort2(arr, 0, arr.length - 1);
	}
	// 計數排序
	public void countSort(int[] arr) {
		int n = arr.length, max = 0;
		int output[] = new int[n];

		for (int i = 0; i < n; ++i) {
			if (arr[i] > max)
				max = arr[i];
		}
		max += 1;
		int count[] = new int[max];
		for (int i = 0; i < max; ++i)
			count[i] = 0;
		for (int i = 0; i < n; ++i)
			++count[arr[i]];
		for (int i = 1; i < max; ++i)
			count[i] += count[i - 1];
		for (int i = n - 1; i >= 0; i--) {
			output[count[arr[i]] - 1] = arr[i];
			--count[arr[i]];
		}
		for (int i = 0; i < n; ++i)
			arr[i] = output[i];
	}
}
