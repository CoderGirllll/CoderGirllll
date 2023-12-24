import java.util.Arrays;


public class Shadowing {
    static int x = 27; //this will be shadowed at line 8
    public static void main(String[] args) {
        System.out.println(x); // 27
        int x; // declaration os x for main function/ method
        //System.out.println(x); // Scope will begin after the initialisation of variable 'x'
        x = 37;
        System.out.println(x); // 37
        trial();
        fun(7,2,5,8,2,8,3,0);
    }

    static void trial() {
        System.out.println(x);
    }

    static void fun(int ...v) {
        System.out.println(Arrays.toString(v));
    }
}