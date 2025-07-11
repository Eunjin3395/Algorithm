import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Set<String> set = new HashSet<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String stats = st.nextToken();
            if (stats.equals("enter")) {
                set.add(name);
            } else {
                set.remove(name);
            }
        }

        List<String> result = new ArrayList<>(set);
        result.sort(Collections.reverseOrder());

        for (String name : result) {
            sb.append(name).append('\n');
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}