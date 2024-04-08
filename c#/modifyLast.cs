    public static string ModifyLast(string str, int n)
    /*Create a function which makes the last character of a string repeat n number of times.*/
    {
      char c = str[str.Length - 1];
      string repeated = new string(c, n - 1);
      
      return str + repeated;
    }