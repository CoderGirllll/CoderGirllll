public class Reverse {
    public static void main(String[] args) {
        int num = 6416321;
        int rev = 0;

        while (num > 0) {
            int digit = num % 10;
            num /= 10;
            rev = (rev * 10) + digit;
        }
    }
}