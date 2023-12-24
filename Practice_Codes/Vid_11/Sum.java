//Functions in java (especially in classes) are called methods.
import java.util.Scanner;


public class Sum {
    public static void main(String[] args) {
        sum();
        System.out.println(sum2(5, 6));
    }

    /*
          Syntax for functions in java:
          access modifier return_type name (arguments/parameters) {
            //body
            return statement;
          }
        */

        static void sum() {
            Scanner in = new Scanner(System.in);
            System.out.print("Enter 1st number: ");
            int num1 = in.nextInt();
            System.out.print("Enter 2nd number: ");
            int num2 = in.nextInt();
            int sum = num1 + num2;
            System.out.println("Sum = " + sum);
        }

        static int sum2(int a, int b) {
            return a + b;
        }
}