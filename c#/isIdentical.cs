    public static bool isIdentical(string str)
    /*Write a function that returns true if all characters in a string are identical and false otherwise.*/
    {
        int n = str.Length;
        
        for(int i = 0;i < n; i++)
        {
            Console.WriteLine(str[i]);
            if (str[i] != str[0])
                return false;
        }
        return true;
    }