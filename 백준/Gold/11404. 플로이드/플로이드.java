import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1000000000;

    public static void print(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        // matrix 초기화 및 입력
        int[][] dist = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i != j) {
                    dist[i][j] = INF;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            dist[a - 1][b - 1] = Math.min(dist[a - 1][b - 1], c);
        }

        // 플로이드 워셜
        for (int mid = 0; mid < N; mid++) {
            for (int start = 0; start < N; start++) {
                for (int end = 0; end < N; end++) {
                    if (dist[start][mid] == INF || dist[mid][end] == INF) {
                        continue;
                    }
                    dist[start][end] = Math.min(dist[start][end], dist[start][mid] + dist[mid][end]);
                }
            }
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (dist[i][j] == INF) {
                    sb.append(0).append(' ');
                } else {
                    sb.append(dist[i][j]).append(' ');
                }
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}