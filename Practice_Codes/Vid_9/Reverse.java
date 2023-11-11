public class Reverse {
    public static void main(String[] args) {
        int num = 6416321;
        int rev = 0;
        System.out.println(num);

        while (num > 0) {
            int digit = num % 10;
            num /= 10;
            rev = (rev * 10) + digit;
        }
        System.out.println(rev);
    }
}