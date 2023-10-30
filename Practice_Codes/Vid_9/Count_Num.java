public class Count_Num {
    public static void main(String[] args) {
        int n = 49792;

        int count = 0;
        while (n > 0) {
            int digit = n % 10;
            if (digit == 9) {
                count++;
            }
            n /= 10;
        }
    }
}