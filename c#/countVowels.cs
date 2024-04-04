    using System;
    
    public static int CountVowels(string str) 
    {

        int count = 0;

        char[] vowels = {'a','e','i','o','u'};

        foreach (char c in str)
        
        { 
            if (Array.IndexOf(vowels, char.ToLower(c)) != -1) {

                count ++;
            }


        }

        return count;
      
    }