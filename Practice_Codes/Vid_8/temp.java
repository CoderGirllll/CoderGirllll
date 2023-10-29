import java.util.Scanner;

public class temp {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter the temperature in C: ");
        float c = in.nextFloat();
        float f = (c * 9/5) + 32;
        System.out.println(f);
    }
}