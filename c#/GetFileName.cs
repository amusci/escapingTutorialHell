using System;
using System.IO;
    public static string GetFilename(string path)
    /*Create a function that returns the selected filename from a path. Include the extension in your answer.*/
    {

      string fileName = Path.GetFileName(path);
      return fileName;
    }