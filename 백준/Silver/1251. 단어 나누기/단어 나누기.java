import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public void solve() throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String input = bf.readLine();
        int N = input.length();

        List<String> answers = new ArrayList<>();

        for (int i=1;i<N-1;i++){
            for (int j=i+1;j<N;j++){
                String part1 = new StringBuilder(input.substring(0,i)).reverse().toString();
                String part2 = new StringBuilder(input.substring(i,j)).reverse().toString();
                String part3 = new StringBuilder(input.substring(j,N)).reverse().toString();

                String combined = part1+part2+part3;
                answers.add(combined);
            }
        }

        Collections.sort(answers);
        System.out.println(answers.get(0));

    }
    public static void main(String[] args) throws Exception{
        new Main().solve();
    }
}