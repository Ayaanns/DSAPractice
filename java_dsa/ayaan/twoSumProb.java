package dsa;

import java.util.Scanner;

public class twoSumProb {
	public static void twoSum() {
		int arr[]= {1,4,9,3,7,6};
		int n=arr.length;
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the target");
		int target=sc.nextInt();
		
		for(int i=0;i<n;i++) {
			for(int j=i+1;j<n;j++) {
				if (arr[i]+arr[j]==target) {
					System.out.println("["+i+","+j+"]");
					
					break;
				}
			}
		}
		
		
	}

	public static void main(String[] args) {
		twoSum();

	}

}
