import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);
        int answer = 1;

        for (int i = 0; i < K; i++) {
            answer *= N;
            N -= 1;
        }

        for (int k = K; k > 0; k--) {
            answer /= k;
        }

        System.out.println(answer);

    }
}