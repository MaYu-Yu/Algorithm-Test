package myPackage;

public class Main {
	public static void main(String[] args) {
		int arr[] = {8,9,2,10,3,4,6,7,5,1};
		Sort s = new Sort();
		System.out.println("Origin Arr : ");
		s.print(arr);
		
		s.mergeSort(arr);
		System.out.println("Sorted Arr : ");
		s.print(arr);
	}
}
