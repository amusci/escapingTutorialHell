    public static string Repeat(string str, int num)
    /*Create a function that repeats each character in a string n times.*/
    {
        string ans = "";
        for (int i = 0; i < str.Length; i++)
        {
            for (int j = 0; j < num; j++) {

                ans += str[i];
            }
        }

        return ans;

    }