public class inle {

    public static void main(String[] arg) {
        int a = 1;
        int b = 1;
        int total = 0;
        while (b < 4000000) {
            if (b % 2 == 0) {
                total += b;
            }
            b = a + b;
            a = b - a;
        }
        System.out.println(total);
    }
}