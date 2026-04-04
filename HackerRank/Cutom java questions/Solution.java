package hackerrank.custom;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Read five values for the integer array
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }

        // 2. Read the two limits
        int limit1 = sc.nextInt();
        int limit2 = sc.nextInt();

        int sum = 0;
        int count = 0;

        // 3. Find values greater than limit1 and less than limit2
        for (int value : arr) {
            if (value > limit1 && value < limit2) {
                sum += value;
                count++;
            }
        }

        // 4. Calculate and print the average (of int data type)
        if (count > 0) {
            int average = sum / count;
            System.out.println(average);
        }

        sc.close();
    }
}