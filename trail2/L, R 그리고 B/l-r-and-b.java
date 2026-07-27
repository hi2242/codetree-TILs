import java.io.*;
import java.util.*;

public class Main {
    public static final int GRID_LENGTH = 10;
    public static final int DIRECTIONS_COUNT = 4;

    public static char[][] grid = new char[GRID_LENGTH][GRID_LENGTH];
    public static final int[] dr = {-1, 0, 1, 0};
    public static final int[] dc = {0, 1, 0, -1};
    public static int sr, sc;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < GRID_LENGTH; i++) {
            String st = br.readLine();
            for (int j = 0; j < GRID_LENGTH; j++) {
                if (st.charAt(j) == 'L') {
                    sr = i;
                    sc = j;
                }
                grid[i][j] = st.charAt(j);
            }
        }

        bfs();
        
    }
    public static void bfs() {
        boolean[][] visited = new boolean[GRID_LENGTH][GRID_LENGTH];
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[] {sr, sc, 0});
        visited[sr][sc] = true;
        while (dq.size() != 0) {
            int[] curr = dq.remove();
            int cr = curr[0], cc = curr[1], cm = curr[2];
            if (grid[cr][cc] == 'R') continue;
            else if (grid[cr][cc] == 'B') {
                System.out.println(cm - 1);
                return;
            }

            for (int i = 0; i < DIRECTIONS_COUNT; i++) {
                int nr = cr + dr[i], nc = cc + dc[i];
                if (isValid(nr, nc) && visited[nr][nc] == false) {
                    visited[nr][nc] = true;
                    dq.offer(new int[] {nr, nc, cm + 1});
                }
            }
        }
    }
    public static boolean isValid(int r, int c) {
        return 0 <= r && r < GRID_LENGTH && 0 <= c && c < GRID_LENGTH;
    }
}