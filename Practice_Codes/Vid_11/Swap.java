import java.util.Arrays;


public class Swap {
    public static void main(String[] args) {
        //Int (pass by value)
        int a = 100;
        int b = 2;

        swap(a,b);
        System.out.println("In main: " + a + " " + b);

        //Array (pass by reference)
        int[] arr = {1, 2, 3, 4};

        change(arr);
        System.out.println("In main: " + Arrays.toString(arr));
    }

    static void swap(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
        System.out.println("In function (swapped): " + x + " " + y);
    }

    static void change(int[] nums) {
        nums[0] = 100;
        System.out.println("In function: " + Arrays.toString(nums));
    }
}