class Solution {

    boolean isprime(int n){

        if(n < 2){
            return false;
        }

        if(n == 2){
            return true;
        }

        int i = 2;
        while(i <= (int)Math.sqrt(n)){

            if(n % i == 0){
                return false;
            }

            i++;
        }

        return true;
    }

    public int diagonalPrime(int[][] nums) {
        
        int largest_prime = 0;

        int i = 0;
        while(i < nums.length){
            if(isprime(nums[i][i]) && nums[i][i] > largest_prime){
                largest_prime = nums[i][i];
            }

            i++;
        }

        i = 0;
        int j = nums.length - 1;

        while(i < nums.length){

            if(isprime(nums[i][j]) && nums[i][j] > largest_prime){
                largest_prime = nums[i][j];
            }

            i++;
            j--;
        }

        return largest_prime;
    }
}