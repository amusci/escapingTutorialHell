        public static bool IsPalindrome(string str) 

        /* 
        A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward, such as madam or kayak.

        Write a function that takes a string and determines whether it's a palindrome or not.
        
        The function should return a boolean (true or false value).
        */

        {

            string cleanedString = Regex.Replace(str, @"[\s\p{P}]+", "");
            return cleanedString.ToLower().SequenceEqual(cleanedString.ToLower().Reverse());

        }