import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inp = br.readLine().split(" ");
        int A = Integer.parseInt(inp[0]);
        int B = Integer.parseInt(inp[1]);

        // A 집합 초기화
        Set<Integer> partA = new HashSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < A; i++) {
            Integer x = Integer.parseInt(st.nextToken());
            partA.add(x);
        }

        // B 집합 초기화
        Set<Integer> partB = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < B; i++) {
            Integer x = Integer.parseInt(st.nextToken());
            partB.add(x);
        }

        // 차집합 크기 계산
        for (Integer a : partA) {
            if (partB.contains(a)) {
                A -= 1;
            }
        }
        for (Integer b : partB) {
            if (partA.contains(b)) {
                B -= 1;
            }
        }

        System.out.println(A + B);

    }

}
