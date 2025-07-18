import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String string = st.nextToken();
        Set<String> set = new HashSet<>();

        for (int i = 0; i < string.length(); i++) {
            for (int j = i + 1; j <= string.length(); j++) {
                set.add(string.substring(i, j));
            }
        }

        System.out.println(set.size());
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}