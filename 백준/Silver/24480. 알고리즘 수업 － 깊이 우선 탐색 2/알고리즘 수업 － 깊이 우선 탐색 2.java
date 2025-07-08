import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Integer>[] adj_list;
    static int[] visited;
    static int order = 1;

    public void dfs(int node){
        visited[node]=order;
        order++;
        for (int next : adj_list[node]){
            if (visited[next]==0){
                dfs(next);
            }
        }

    }

    public void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        adj_list = new ArrayList[N+1]; // ArrayList를 N+1개 갖고 있는 adj_list 초기화
        visited = new int[N+1];

        for (int i=1;i<=N;i++){ // 각 인덱스별 ArrayList 초기화
            adj_list[i] = new ArrayList<>();
        }

        for (int i =0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            adj_list[u].add(v);
            adj_list[v].add(u);
        }

        // 각 인접리스트 내림차순 정렬
        for (int i = 1; i<=N;i++){
            Collections.sort(adj_list[i],Collections.reverseOrder());
        }

        // dfs
        dfs(R);

        for(int i = 1; i<=N;i++){
            sb.append(visited[i]).append('\n');
        }
        
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception{
        new Main().solve();
    }
}
