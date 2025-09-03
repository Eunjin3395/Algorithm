import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int paperNum = Integer.parseInt(br.readLine());
        int[][] white = new int[100][100];

        for (int i = 0; i < paperNum; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 색종이 붙이기
            for(int j=0; j<10; j++){
                for(int k=0; k<10; k++){
                    white[x+j][y+k] = 1;
                }
            }
        }

        int[][] d = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int round = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if(white[i][j]==1){
                    for(int k=0; k<d.length; k++){
                        int x = d[k][0];
                        int y = d[k][1];
                        if(i+x <0 || i+x > 99 || j+y<0 || j+y>99){
                            round++;
                        } else if(white[i+x][j+y]==0){
                            round++;
                        }
                    }
                }
            }
        }
        System.out.println(round);
    }
}