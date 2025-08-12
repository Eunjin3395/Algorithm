import java.io.*;
import java.util.*;

public class Main {

    private int N;
    private int[][] adj;
    private boolean[][] visited;

    private void bfs(int start) {
        Deque<Integer> q = new ArrayDeque<>();
        q.add(start);

        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nxt = 0; nxt < N; nxt++) {
                if (adj[node][nxt] == 1 && !visited[start][nxt]) {
                    q.add(nxt);
                    visited[start][nxt] = true;
                }
            }
        }
    }

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());

        adj = new int[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                adj[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 각 노드에 대해 bfs 실행
        for (int i = 0; i < N; i++) {
            bfs(i);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(visited[i][j] ? 1 : 0);
                if (j + 1 < N) sb.append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}