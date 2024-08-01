class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int x = nums1[0];
        int y = nums2[0];
        for(int n : nums1){
            if(n < x) x = n;
        }
        for(int n : nums2){
            if(n < y) y = n;
        }
        return y - x;
    }
}