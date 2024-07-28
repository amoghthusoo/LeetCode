class Solution {

    static int abs(int x){
        if(x >= 0){
            return x;
        }
        else{
            return -x;
        }
    }

    public int minTimeToVisitAllPoints(int[][] points) {
        
        int time = 0;

        int i = 0;
        while(i < points.length - 1){

            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i + 1][0];
            int y2 = points[i + 1][1];

            int d1 = x2 - x1;
            int d2 = y2 - y1;

            int d1_abs = abs(d1);
            int d2_abs = abs(d2);

            if(d1_abs <= d2_abs){
                
                time += d1_abs;

                if(d2 >= 0){
                    time += abs(y2 - y1 - d1_abs);
                }
                else{
                    time += abs(y2 - y1 + d1_abs);
                }
            }

            else{
                time += d2_abs;

                if(d1 >= 0){
                    time += abs(x2 - x1 - d2_abs);
                }
                else{
                    time += abs(x2 - x1 + d2_abs);
                }
            }

            i++;
        }
        return time;
    }
}