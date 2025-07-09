import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N;
    public static int M;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int[] dy = {1, 0, -1, 0};
    public static int[] dx = {0, 1, 0, -1};

    public int bfs(int start_y, int start_x) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{start_y, start_x}); // y,x
        visited[start_y][start_x] = true;

        int cnt = 0;

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int y = node[0];
            int x = node[1];
            cnt++;

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= ny && ny < N && 0 <= nx && nx < M) {
                    if ((!visited[ny][nx]) && graph[ny][nx] == 1) {
                        visited[ny][nx] = true;
                        q.offer(new int[]{ny, nx});
                    }
                }
            }
        }
        return cnt;
    }

    public void solve() throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        // 연결 요소의 개수, 최다 노드 개수 구하기
        // 변수 초기화
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        visited = new boolean[N][M];

        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(bf.readLine());
            for (int x = 0; x < M; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 0;
        int mx = 0;

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (!visited[y][x] && graph[y][x] == 1) {
                    int c = bfs(y, x);
                    cnt++;
                    mx = Math.max(mx, c);
                }
            }
        }

        System.out.println(cnt);
        System.out.println(mx);
    }

    public static void main(String args[]) throws Exception {
        new Main().solve();
    }
}