    public static int Factorial(int num)

    {
        if (num == 1 || num == 0) 
        {
            return 1;
        }

       
        return num * Factorial(num - 1);

    }