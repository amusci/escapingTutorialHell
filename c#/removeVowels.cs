    public static string RemoveVowels(string str) 
    /* Create a function that takes a string and returns a new string with all vowels removed.*/
    {
        StringBuilder result = new StringBuilder();
        char[] vowels = ['a','e','i','o','u'];

        foreach (char c in str) {

            if (Array.IndexOf(vowels, c) == -1) {

                result.Append(c);

                
            }


        

      
    }

    return result.ToString();
        
    }