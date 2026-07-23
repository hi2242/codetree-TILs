import java.io.*;
import java.util.*;

public class Main {
    // Point: 좌표 + 시간으로 사용할 클래스
    public static class Point {
        int r, c, t, d;

        Point(int r, int c, int t, int d) {
            this.r = r;
            this.c = c;
            this.t = t;
            this.d = d;
        }

        public String toString() {
            return "[" + this.r + ", " + this.c + ", " + this.t + ", " + this.d + "]";
        }
    }

    // 상수화 리스트
    public static final int ELEM_NUMBER = 1;
    public static final int TRAFFIC_LOOP_COUNT = 4;
    public static final int DIRECTION_COUNT = 4;
    // 우: 0, 상: 1, 좌: 2, 하: 3 순서
    public static final int[] dr = {0, -1, 0, 1};
    public static final int[] dc = {1, 0, -1, 0};
    public static final int[][] signal_directions = {
        {},
        {0, 1, 3},
        {1, 2, 0},
        {2, 3, 1},
        {3, 0, 2},
        {0, 1},
        {1, 2},
        {2, 3},
        {3, 0},
        {0, 3},
        {1, 0},
        {2, 1},
        {3, 2}
    };

    // N: 한 변의 교차로 개수
    // T: 이동 가능 시간
    // traffic_grid: 각 교차로 신호 정보
    // visited_grid: 각 교차로 방문 여부
    // curr_signal: curr_T에 맞는 신호 정보
    // valid_directions: 갈 수 있는 방향 리스트
    public static int N, T;
    public static int[][][] traffic_grid;
    public static boolean[][] visited_grid;
    public static int curr_signal;
    public static List<int[]> valid_directions;
    public static void main(String[] args) throws IOException {
        // 입력을 받는 부분
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        traffic_grid = new int[N + 1][N + 1][ELEM_NUMBER];
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                int[] temp = new int[4];
                st = new StringTokenizer(br.readLine());
                for (int i = 0; i < TRAFFIC_LOOP_COUNT; i++) {
                    temp[i] = Integer.parseInt(st.nextToken());
                }
                traffic_grid[r][c] = temp;
            }
        }

        // 초기 세팅 부분
        visited_grid = new boolean[N + 1][N + 1];
        Deque<Point> d = new ArrayDeque<>();
        d.offer(new Point(1, 1, 0, 1));
        visited_grid[1][1] = true;

        // bfs 방식을 통해 탐색
        while (d.size() != 0) {
            Point cp = d.poll();
            // 현재 시간이 총 이동 시간과 같으면 더이상 이동하지 않음
            if (cp.t == T) {
                continue;
            }
            // 현재 시각에 맞는 신호를 반환 받음
            curr_signal = calc_signal(cp.r, cp.c, cp.t);
            // 이동 가능한 방향들을 지나간 교차점으로 취급하고
            // 다시 덱에 넣음
            valid_directions = validate_signal(cp.r, cp.c);
            
            if (cp.d != signal_directions[curr_signal][0]) continue;
            for (int[] dp: valid_directions) {
                Point np = new Point(cp.r + dp[0], cp.c + dp[1], cp.t + 1, dp[2]);
                visited_grid[np.r][np.c] = true;
                d.offer(new Point(np.r, np.c, np.t, dp[2]));
            }
        }
        System.out.println(calc_grid());
    }
    
    // 현재 시간에 맞는 신호를 반환하는 함수
    public static int calc_signal(int r, int c, int t) {
        return traffic_grid[r][c][t % 4];
    }

    // 신호를 통해 이동할 수 있는 방향을 반환하는 함수
    public static List<int[]> validate_signal(int r, int c) {
        List<int[]> valid_directions = new ArrayList<>();
        int[] directions = signal_directions[curr_signal];
        for (int d: directions) {
            int nr = r + dr[d], nc = c + dc[d];
            if (is_valid(nr, nc)) {
                valid_directions.add(new int[] {dr[d], dc[d], d});
            }
        }
        return valid_directions;
    }

    // 유효 범위 내부의 좌표인지 확인해주는 함수
    public static boolean is_valid(int r, int c) {
        return 0 < r && r <= N && 0 < c && c <= N;
    }

    // 지나간 교차점의 개수를 반환하는 함수
    public static int calc_grid() {
        int count = 0;
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                if (visited_grid[r][c] == true) {
                    count++;
                }
            }
        }
        return count;
    }

    // 3차원 배열을 출력해주는 함수
    public static void print_grid(int[][][] grid) {
        for (int[][] row: grid) {
            for (int[] elem: row) {
                System.out.print(Arrays.toString(elem) + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // 2차원 배열을 출력해주는 함수
    public static void print_grid(boolean[][] grid) {
        for (boolean[] row: grid) {
            for (boolean elem: row) {
                System.out.print(elem + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
