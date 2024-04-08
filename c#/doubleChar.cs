    public static string DoubleChar(string str) 
    /*Create a function that takes an array as an argument and returns true or false depending on whether the average of all elements in the array is a whole number or not.*/
    {
      string result = "";

      foreach (char c in str)
      {
        result += c;
        result += c;

      }
      return result;
    }