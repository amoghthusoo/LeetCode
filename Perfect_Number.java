class Perfect_Number {
    public boolean checkPerfectNumber(int num) {
        
        int sum = 0;

        for(int i = 1; i <= num / 2; i++){

            if(num % i == 0){
                sum += i;
            }
        }

        if(sum == num){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args) {
        
        int num = 28;
        Perfect_Number obj = new Perfect_Number();
        boolean out = obj.checkPerfectNumber(num);
        System.out.println(out);
    }
}