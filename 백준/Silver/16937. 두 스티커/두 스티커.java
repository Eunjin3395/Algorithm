import java.io.*;
import java.util.*;

public class Main {
    static int H, W, N;
    static int[][] sticker;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(br.readLine());

        sticker = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            sticker[i][0] = Integer.parseInt(st.nextToken());
            sticker[i][1] = Integer.parseInt(st.nextToken());
        }
        int maxArea = 0;

        for (int i = 0; i < N; i++) {
            if (sticker[i][0] > H && sticker[i][1] > W) continue;
            for (int j = i + 1; j < N; j++) {
                if (sticker[j][0] > H && sticker[j][1] > W) continue;
                maxArea = Math.max(maxArea, getStickerArea(sticker[i], sticker[j]));
            }
        }

        System.out.println(maxArea);
    }

    // 최대 너비 계산
    static int getStickerArea(int[] s1, int[] s2) {
        int max = 0;
        int[][] stickers = {
                {s1[0], s1[1]}, {s1[1], s1[0]},
                {s2[0], s2[1]}, {s2[1], s2[0]}  
        };

        for (int k = 0; k < 2; k++) {
            for (int l = 2; l < 4; l++) {
                int x1 = stickers[k][0], y1 = stickers[k][1];
                int x2 = stickers[l][0], y2 = stickers[l][1];

                max = getMax(max, x1, y1, x2, y2, x1 * y1, x2 * y2);

                max = getMax(max, y1, x1, y2, x2, x1 * y1, x2 * y2);
            }
        }

        return max;
    }

    private static int getMax(int max, int x1, int y1, int x2, int y2, int i, int i2) {
        if (x1 <= H && y1 <= W) {
            // 첫 번째 스티커를 붙이고, 남은 아래 부분에 두번째 스티커가 들어가는 경우
            if (x2 <= H && y2 <= W - y1) {
                max = Math.max(max, i + i2);
            }
            // 첫 번째 스티커를 붙이고, 남은 오른쪽 부분에 두번째 스티커가 들어가는 경우
            if (x2 <= H - x1 && y2 <= W) {
                max = Math.max(max, i + i2);
            }
        }
        return max;
    }

}