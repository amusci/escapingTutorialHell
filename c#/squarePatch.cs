    public static int[,] SquarePatch(int n) 
    /*

    Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.

    */
    {
        
        int[,] matrix = new int[n, n];

        for(int i = 0; i < n; i++)
        {

            for (int j = 0; j < n; j++)
            {

                matrix[i,j] = n;

            }

        }

        return matrix;
        
        
    }