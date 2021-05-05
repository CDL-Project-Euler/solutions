public class inle {

    public static void main(String[] arg) {
        final int maximum = Integer.parseInt(arg[0]);
        int total = 0;
        for (int i = 1; i < maximum; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                total += i;
            }
        }
        System.out.println(total);
    }
}