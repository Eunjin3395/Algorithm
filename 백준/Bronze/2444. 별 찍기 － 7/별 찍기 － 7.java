import java.io.*;
import java.util.*;

public class Main {
    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < N - i; j++) {
                sb.append(" ");
            }
            for (int j = 0; j < i * 2 - 1; j++) {
                sb.append("*");
            }
            sb.append("\n");
        }

        for (int i = N - 1; i > 0; i--) {
            for (int j = 0; j < N - i; j++) {
                sb.append(" ");
            }
            for (int j = 0; j < i * 2 - 1; j++) {
                sb.append("*");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}