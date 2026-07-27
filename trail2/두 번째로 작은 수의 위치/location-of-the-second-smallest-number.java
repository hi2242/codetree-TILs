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
    public static int[] nums;
    public static int smallestValue = Integer.MAX_VALUE;
    public static Point secondPoint;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            smallestValue = Math.min(smallestValue, nums[i]);
        }
        secondPoint = new Point();
        for (int i = 0; i < N; i++) {
            if (smallestValue < nums[i] && secondPoint.v > nums[i]) {
                secondPoint.v = nums[i];
                secondPoint.i = i;
            }
        }
        int flag = 0;
        for (int i = 0; i < N; i++) {
            if (secondPoint.v == nums[i]) {
                flag++;
            }
        }
        secondPoint.i = (flag > 1) ? -1 : secondPoint.i + 1;
        System.out.println(secondPoint.i);
    }
}