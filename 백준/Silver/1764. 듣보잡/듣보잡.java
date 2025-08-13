import java.io.*;
import java.util.*;

public class Main {

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<String> answer = new ArrayList<>();

        // set에 N개의 이름 먼저 저장, M개의 이름에 대해 set에 존재하면 답에 추가
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            set.add(name);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            if (set.contains(name)) {
                answer.add(name);
            }
        }


        System.out.println(answer.size());
        Collections.sort(answer);
        for (String name : answer) {
            System.out.println(name);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}