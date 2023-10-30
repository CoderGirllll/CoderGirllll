public class Main {
    public static void main(String[] args) {
        //if-else statements:
        int sal = 24500;
        if (sal > 10000) {
            sal += 2000;
        }
        else if (sal > 20000) {
            sal += 3000;
        }
        else {
            sal += 1000;
        }

        System.out.println(sal);

        //for loop:
        for (int i = 0; i < 5; i++) {
            System.out.println(i + 1);
        }

        //while loop:
        int j = 0;
        while (j < 5) {
            System.out.println(j + 1);
            j++;
        }

        //do-while loop:
        int n = 1;
        do {
            System.out.println(n);
            n++;
        } while (n <= 5);
    }
}