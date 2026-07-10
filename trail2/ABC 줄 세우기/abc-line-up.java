import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static char[] people;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        people = new char[N];
        for (int i = 0; i < N; i++) {
            people[i] = st.nextToken().charAt(0);
        }
        
        solve();
    }

    public static void solve() {
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - i - 1; j++) {
                if (people[j] > people[j + 1]) {
                    swap(people, j, j + 1);
                    result++;
                }
            }
        }
        System.out.print(result);
    }

    public static void swap(char[] arr, int a, int b) {
        char temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}