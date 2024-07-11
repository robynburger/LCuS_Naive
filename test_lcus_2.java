
import java.util.Arrays;

public class test_lcus_2 {

    static char[] s = "abcdacbdcdab".toCharArray();

    static int gamma(int m, int i) {
        int t = i;
        while (t >= 1 && s[t - 1] != s[m - 1]) {
            t--;
        }
        return t;
    }

    public static void main(String[] args) {
        int[][][][][] f = new int[s.length + 1][s.length + 1][s.length + 1][s.length + 1][s.length + 1]; // f[m,i,k,j,l]
        int[][][][][] d = new int[s.length + 1][s.length + 1][s.length + 1][s.length + 1][s.length + 1]; // d[m,i,k,j,l]


        // compute correct values first
        for (int m = 1; m <= s.length; m++) {
            for (int i = 1; i <= s.length; i++) {
                for (int k = i + 1; k <= s.length; k++) {
                    for (int j = i + 1; j <= k; j++) {
                        for (int l = k + 1; l <= m; l++) {
                            f[m][i][k][j][l] = f[m - 1][i][k][j][l];
                            if (gamma(m, i) >= 1 && gamma(m, k) >= j) {
                                f[m][i][k][j][l] = Math.max(f[m][i][k][j][l], f[m - 1][gamma(m, i) - 1][gamma(m, k) - 1][j][l] + 1);
                            }
                            if (f[m][i][k][j][l] > f[m][i - 1][k][j][l]) {
                                d[m][i][k][j][l] = 1;
                            }
                            if ((i == 4 ) && (k == 8) && (m == 12) && (l == 9))
                                print(f"f[" + m + "][" + j + "][" + i + "][" + k + "][" + l + "] = " )
                            print(f"f[{m}, {j}, {i-1}, {k}, {l}] = {f[m, j, i-1, k, l]}\n")
                        }
                    }
                }
            }
        }

        int[] j_vector = new int[s.length + 1];
        for (int j = 5; j <= 8; j++) {
            j_vector[j] = d[12][4][j][8][9];
            System.out.println("f[12, ")
        }

        System.out.println(Arrays.toString(j_vector));
    }
}