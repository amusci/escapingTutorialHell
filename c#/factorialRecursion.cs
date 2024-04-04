    public static int Factorial(int num)

    {
        if (num == 1) 
        {
            return 1;
        }

        num = num * Factorial(num - 1);
        return num;

    }