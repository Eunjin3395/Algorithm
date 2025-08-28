import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        int[] sorted = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr[i] = sorted[i] = x;
        }

        // arr 정렬
        Arrays.sort(sorted);

        HashMap<Integer, Integer> map = new HashMap<>();
        int rank = 0;
        for (int val : sorted) {
            if (!map.containsKey(val)) {
                map.put(val, rank);
                rank++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int val : arr) {
            rank = map.get(val);
            sb.append(rank).append(" ");
        }

        System.out.println(sb);
    }
}