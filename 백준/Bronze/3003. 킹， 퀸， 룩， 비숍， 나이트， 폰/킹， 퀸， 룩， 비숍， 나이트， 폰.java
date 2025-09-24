import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int[] origin = {1, 1, 2, 2, 2, 8};

        int[] answer = new int[6];
        for (int i = 0; i < 6; i++) {
            int curr = Integer.parseInt(input[i]);
            answer[i] = origin[i] - curr;
        }

        for (int i = 0; i < 6; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}