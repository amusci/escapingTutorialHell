    public static string Reverse(string str) 
    /*Create a function that takes a string as its argument and returns the string in reversed order*/
    {
      char[] charArray = str.ToCharArray();
      Array.Reverse(charArray);
      return new string(charArray);
    }