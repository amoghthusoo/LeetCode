import java.lang.Math;

class Count_Square_Sum_Triples {
    public int countTriples(int n) {

        int count = 0;

        int i = 1;
        while (i <= n) {

            int j = 1;
            while (j <= n) {

                int k = 1;
                while (k <= n) {

                    if (Math.pow(i, 2) + Math.pow(j, 2) == Math.pow(k, 2)) {
                        count += 1;
                    }

                    k += 1;
                }

                j += 1;
            }

            i += 1;
        }

        return count;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        System.out.println(obj.countTriples(250));
    }
}