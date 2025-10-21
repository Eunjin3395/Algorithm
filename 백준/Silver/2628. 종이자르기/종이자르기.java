import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int C = Integer.parseInt(br.readLine());
        List<Integer> hor = new ArrayList<>(); // 가로
        List<Integer> ver = new ArrayList<>(); // 세로

        hor.add(0);
        hor.add(M);
        ver.add(0);
        ver.add(N);

        for (int i = 0; i < C; i++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            if (cmd == 0) {
                hor.add(x);
            } else {
                ver.add(x);
            }
        }
        Collections.sort(hor);
        Collections.sort(ver);

//        System.out.println(hor);
//        System.out.println(ver);

        int mxr = 0;
        int mxc = 0;

        for (int i = 1; i < hor.size(); i++) {
            mxr = Math.max(mxr, hor.get(i) - hor.get(i - 1));
        }
        for (int i = 1; i < ver.size(); i++) {
            mxc = Math.max(mxc, ver.get(i) - ver.get(i - 1));
        }

        System.out.println(mxr * mxc);

    }
}