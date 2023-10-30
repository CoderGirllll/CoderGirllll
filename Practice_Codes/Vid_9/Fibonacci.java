import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int i = in.nextInt();
        int p = 0;
        int n = 1;
        int count = 2;

        while (count <= i) {
            int temp = n;
            n += p;
            p = temp;
            count++;
        }
    }
}