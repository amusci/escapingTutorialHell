    public static int Equal(int a, int b, int c)
    /* Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value. */
        {
        int count = 0;

        
        if (a == b && b == c)
        {
            count = 3;
        }

        
        else if (a == b || a == c || b == c)
        {
            count = 2;
        }


        return count;
        
        }