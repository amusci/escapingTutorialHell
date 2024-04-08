    public static int CountDs(string str)
    /*Create a function that counts how many D's are in a sentence.*/
    {
        int count = 0;
        foreach (char c in str)
        {
            if (c == 'D' || c == 'd') {
                count++;
            }
        }
        return count;
    }