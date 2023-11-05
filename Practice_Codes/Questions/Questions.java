import java.util.Scanner;

public class Questions {
    public static void main(String[] args) {
        // Area of Circle
        double pi = Math.PI;
        System.out.print("Enter the radius: ");
        Scanner in = new Scanner(System.in);
        float r = in.nextFloat();
        System.out.println("Area of circle with radius " + r + " is " + (pi * r * r));


        // Area of Rectangle
        System.out.print("Enter length: ");
        float l = in.nextFloat();
        System.out.print("Enter breadth: ");
        float b = in.nextFloat();
        System.out.println("Area of rectangle is " + (l * b));


        // Perimeter of Equilateral Triangle
        System.out.print("Enter a side of triangle: ");
        float t = in.nextFloat();
        System.out.println("Perimeter of equilateral triangle is " + (t * 3));


        // Perimeter of Circle
        System.out.print("Enter the radius: ");
        float R = in.nextFloat();
        System.out.println("Perimeter of circle is " + (2 * pi * R));


        // Input a number and print all the factors of that number
        System.out.print("Enter a number: ");
        int n = in.nextInt();
        System.out.print("Factors of " + n + " are ");
        for (int i = 1; i < n; i++) {
            if (n%i == 0) {
                System.out.print(i + ",");
            };
        };
        System.out.println(n);
    

        //Factorial Program
        System.out.print("Enter a number: ");
        int N = in.nextInt();
        int fact = 1;
        for (int i = 1; i <= N; i++) {
            fact *= i;
        };
        System.out.println("Factorial of " + N + " is " + fact);
    }
}