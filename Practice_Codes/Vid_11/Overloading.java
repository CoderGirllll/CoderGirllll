public class Overloading {
    public static void main(String[] args) {
        fun(26);
        fun(161,545);
    }

    static void fun(int x) {
        System.out.println(x);
    }

    static void fun(int x, int y) {
        System.out.println(x + " " + y);
    }

    //Overloading is when two (or more) functions have the same name but different parameters.
}