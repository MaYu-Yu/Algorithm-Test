package myPackage;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays; 
import org.junit.jupiter.api.Test;
class SortTest {

	@Test
	void test() {
		Sort s = new Sort();
		int arr[] = new int[10];
		for(int times=0;times<10;times++){
			for(int i=0;i<10;i++){
				arr[i] = (int)(Math.random()*(1000));
			}
			int[] temp = Arrays.copyOf(arr, 10); 
			int[] sort_arr = Arrays.copyOf(arr, 10); 
			s.bubbleSort(sort_arr); // ·Ç½T±Æ§Ç
			
			s.selectionSort(temp);
			assertArrayEquals(temp, sort_arr);
			temp = Arrays.copyOf(arr, 10); 
			
			s.insertSort(temp);
			assertArrayEquals(temp, sort_arr);
			temp = Arrays.copyOf(arr, 10); 
			
			s.shellSort(temp);
			assertArrayEquals(temp, sort_arr);
			temp = Arrays.copyOf(arr, 10); 
			
			s.mergeSort(temp);
			assertArrayEquals(temp, sort_arr);
			temp = Arrays.copyOf(arr, 10); 
			
			s.quickSort(temp);
			assertArrayEquals(temp, sort_arr);
			temp = Arrays.copyOf(arr, 10); 
			
			s.countSort(temp);
			assertArrayEquals(temp, sort_arr);
			
			System.out.println("****** Origin Array ******");
			s.print(arr);
			System.out.println("****** Sorted Array ******");
			s.print(temp);
			
		}

	}
}
