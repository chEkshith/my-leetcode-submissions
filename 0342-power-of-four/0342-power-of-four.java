class Solution {
    public boolean isPowerOfFour(int n) {
        for(int i=0;i<=15;i++)
        {
            int r=(int) Math.pow(4,i);
            if(r==n)
            {
                return true;
            }
            else if(r>n)
            {
                break;
            }
        }
        return false;
    }
}