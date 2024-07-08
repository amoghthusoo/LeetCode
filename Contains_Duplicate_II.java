class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
           
        int i = 0;
        while(i < nums.length){

            int j = i + 1;

            while(j <= i + k && j < nums.length){

                if(nums[i] == nums[j] && j - i <= k){
                    return true;
                }

                j++;
            }

            i++;
        }

        return false;
    }
}