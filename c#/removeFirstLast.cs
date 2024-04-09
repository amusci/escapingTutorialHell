    public static string RemoveFirstLast(string str)
    /*Create a function that removes the first and last characters from a string.*/
    {
      if (str.Length <= 2) {

        return str;

      }
      
      string middle = str.Substring(1, str.Length - 2);
      return middle;

    }