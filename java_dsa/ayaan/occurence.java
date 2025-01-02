package dsa;

public class occurence {
	public static int occurrenceOf(int[] arr,int num) {
		int occurrence = 0;
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] == num) {
				occurrence++;
			}
		}
		return occurrence; 
	}

	public static void main(String[] args) {
		int[] arr = {21,67,45,21,33,67,21,89}; 
		int num = 21;
				; 
		int count = occurrenceOf(arr, 21);
		System.out.println(num+" occurres "+ count+" times.");

	}

}
