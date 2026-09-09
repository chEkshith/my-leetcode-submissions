class Solution {
    public boolean isPowerOfThree(int n) {
        for(int i=0;i<=19;i++)
        {
            int r=(int) Math.pow(3,i);
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