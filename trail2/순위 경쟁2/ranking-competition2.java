import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static String[] c;
    static int[] s;
    static String winner = "A B";
    static int[] p = {0, 0};
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine().trim());
        c = new String[N];
        s = new int[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            c[i] = st.nextToken();
            s[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            int k = (c[i].equals("A")) ? 0 : 1;
            p[k] += s[i];
            String temp_winner = compare(p[0], p[1]);
            if (winner != temp_winner) {
                result++;
            }
            winner = temp_winner;
        }

        System.out.println(result);
    }
    static String compare(int a_s, int b_s) {
        String result;
        if (a_s > b_s) {
            result = "A";
        } else if (a_s < b_s) {
            result = "B";
        } else {
            result = "A B";
        }

        return result;
    }
}