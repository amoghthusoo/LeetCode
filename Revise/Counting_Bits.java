 class Solution {
    public int[] countBits(int n) {
        
        if(n == 0){
            int ans[] = {0}; 
            return  ans;
        }

        int ans[] = new int[n + 1];
        ans[0] = 0;
        ans[1] = 1;

        int last_index;
        if(n % 2 == 0){
            last_index = n/2;
        }
        else{
            last_index = (n - 1)/2;
        }

        int i = 1;
        while(i <= last_index){

            try{
                ans[i * 2] = ans[i];
                ans[i * 2 + 1] = ans[i] + 1;
            }
            catch(Exception e){
            }
            i++;
        }
        return ans;
    }
}