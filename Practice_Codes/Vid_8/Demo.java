//Importing the function Scanner, used for reading the given input.
import java.util.Scanner;

public class Demo {
    public static void main(String[] args){
        //"new" is a keyword used to create a new object.
        //System.out.print("Enter:");
        Scanner input = new Scanner(System.in); //System.in is the keyword strokes.
        System.out.println(input.nextInt());
        //nextInt() function is used for printing the next integer.
        //next() function is used for printing the first (0) string.
        //nestLine() function is used for printing the first line.

        //Primitive data types
        int roll_no = 32;
        char alpha = 'r';
        float marks = 46.16f;
        double large_float = 1513.216023;
        long large_Int = 1089460374;
        boolean check = true; //or false
        String line = "Hi, how are you?"; //String is not a primitive dtat type.

        //Type Casting
        int a = (int)(54.45f);

        //While loop
        int c = 1;
        while (c != 5) {
            System.out.println(c);
            c++;
        }

        //For loop
        for(int x = 1; x != 5; x++) {
            System.out.println(x); 
        }
    }
}