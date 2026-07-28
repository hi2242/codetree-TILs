import java.io.*;
import java.util.*;

public class Main {
    public static class GameResult {
        char c;
        int s;
        GameResult() {}
        GameResult(char c, int s) {
            this.c = c;
            this.s = s;
        }
        @Override
        public String toString() {
            return c + " " + s;
        }
    }

    public static int N;
    public static List<GameResult> gameResultList = new ArrayList<>();
    public static Set<Character> honorList = new HashSet<>();
    public static Map<Character, Integer> pointList = new HashMap<>();
    public static int answer;

    static {
        honorList.add('A');
        honorList.add('B');
        honorList.add('C');
        pointList.put('A', 0);
        pointList.put('B', 0);
        pointList.put('C', 0);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            gameResultList.add(new GameResult(st.nextToken().charAt(0), Integer.parseInt(st.nextToken())));
        }

        
        for (int i = 0; i < N; i++) {
            calcGame(gameResultList.get(i));
            
            pickTop();
        }
        sb.append(answer);
        System.out.println(sb);
    }

    public static void calcGame(GameResult result) {
        int currPoint = pointList.get(result.c);
        pointList.put(result.c, currPoint + result.s);
    }

    public static void pickTop() {
        int maxValue = Collections.max(pointList.values());
        Set<Character> copyHonorList = new HashSet<>(honorList);
        for (int i = 65; i < 68; i++) {
            if (pointList.get((char) i) == maxValue) {
                honorList.add((char) i);
            } else {
                honorList.remove((char) i);
            }
        }
        if (!copyHonorList.equals(honorList)) {
            answer++;
        }
    }
}