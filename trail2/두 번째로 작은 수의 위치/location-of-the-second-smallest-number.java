import java.io.*;
import java.util.*;

public class Main {
    public static class Point {
        int v, i;
        Point() {
            v = Integer.MAX_VALUE;
            i = -2;
        }
    }
    public static int N;
    public static List<Integer> nums = new ArrayList<>();
    public static int secondValue;
    public static int answer = -1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums.add(Integer.parseInt(st.nextToken()));
        }
        List<Integer> sortedNums = new ArrayList<>(nums);
        Collections.sort(sortedNums);
        for (int i = 0; i < N; i++) {
            if (sortedNums.get(0) != sortedNums.get(i)) {
                secondValue = sortedNums.get(i);
                break;
            }
        }
        int secondValueCount = Collections.frequency(nums, secondValue);
        System.out.println((secondValueCount == 1) ? nums.indexOf(secondValue) + 1 : -1);
    }
}