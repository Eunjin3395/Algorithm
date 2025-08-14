import java.io.*;
import java.util.*;

public class Main {
    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Set<Integer> S = new HashSet<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if ("add".equals(cmd)) {
                int x = Integer.parseInt(st.nextToken());
                S.add(x);
            } else if ("remove".equals(cmd)) {
                int x = Integer.parseInt(st.nextToken());
                S.remove(x);
            } else if ("check".equals(cmd)) {
                int x = Integer.parseInt(st.nextToken());
                if (S.contains(x)) {
                    sb.append(1);
                    sb.append("\n");
                } else {
                    sb.append(0);
                    sb.append("\n");
                }
            } else if ("toggle".equals(cmd)) {
                int x = Integer.parseInt(st.nextToken());
                if (S.contains(x)) {
                    S.remove(x);
                } else {
                    S.add(x);
                }
            } else if ("all".equals(cmd)) {
                for (int j = 1; j < 21; j++) {
                    S.add(j);
                }
            } else {
                S = new HashSet<>();
            }
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}