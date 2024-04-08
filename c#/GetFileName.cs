    public static string GetFilename(string path)
    /*Create a function that returns the selected filename from a path. Include the extension in your answer.*/
    {
      string[] split = path.Split('/');

      foreach (string s in split)
      {
        if (s.Contains(".")) {

          return s;

        }
        
        

      }
      return null;

    }