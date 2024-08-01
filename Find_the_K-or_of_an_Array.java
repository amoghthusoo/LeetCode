class Solution {
    public int findKOr(int[] nums, int k) {
        
        int[] bin_arr = new int[31];

        int i = 0;
        while(i < nums.length){

            int num = nums[i];
            int j = 30;

            while(num != 0){
                bin_arr[j] += num % 2;
                num /= 2;
                
                j--;
            }

            i++;
        }

        int out_num = 0;
        i = 30;
        while(i >= 0){
            
            if(bin_arr[i] >= k){
                out_num += (int)Math.pow(2, (30 - i));
            }

            i--;
        }

        return out_num;
    }
}