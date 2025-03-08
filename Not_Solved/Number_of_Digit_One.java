public class Number_of_Digit_One{
    
    static int getLen(int n){

        int count = 0;
        while(n != 0){
            n /= 10;
            count++;
        }
        return count;
    }
    
    public static void main(String[] args) {
        int n = 13;
        int len = getLen(n);
        int count = (int)((len - 1) * Math.pow(10, len - 2));
        for(int i = (int)(Math.pow(10, len - 1)) ; i <= n; i++){
            int temp = i;
            while(temp != 0){
                if(temp % 10 == 1) count++;
                temp /= 10;
            }
        }
        System.out.println(count);
    }
}