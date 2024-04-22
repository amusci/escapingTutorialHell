        public static string RemoveSpecialCharacters(string str) 
        /* Create a function that takes a string, removes all "special" characters (e.g. ., !, @, #, $, %, ^, &, \, *, (, )) and returns the new string. The only non-alphanumeric characters allowed are dashes -, underscores _ and spaces. */


        {

            return new string (str.Where(c => char.IsLetterOrDigit(c) || c == ' ' || c == '_' || c == '-').ToArray());
        
        }