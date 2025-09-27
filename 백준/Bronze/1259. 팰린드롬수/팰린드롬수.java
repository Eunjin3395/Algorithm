import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] input = br.readLine().split("");
            if ("0".equals(input[0])) {
                break;
            }

            int L = input.length;
            boolean isPalindrom = true;
            for (int i = 0; i < L / 2; i++) {
                if (!input[i].equals(input[L - i - 1])) {
                    isPalindrom = false;
                    break;
                }
            }

            if (isPalindrom) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }

        }
    }
}