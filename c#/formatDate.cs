    public static string FormatDate(string date) 
    /*Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.*/
    {
      string[] split = date.Split('/');
      return ($"{split[2]}{split[1]}{split[0]}");

    }