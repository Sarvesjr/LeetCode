class Solution{
    public double myPow(double x, int n){

        long N = Math.abs((long)n);
        double res = helper(x, N);

        if(n >= 0){
            return res;
        }
        else{
            return 1 / res;
        }
    }

    public double helper(double x, long n) {

        if(x == 0){
            return 0;
        }
        if(n == 0){
            return 1;
        }

        double res = helper(x * x, n / 2);
        if(n % 2 == 1){
            return res * x;
        }
        else{
            return res;
        }
    }
}