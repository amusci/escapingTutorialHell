    public static string count_all(string txt) 
    /* Write a function that takes a string and calculates the number of letters and digits within it.
    Return the result as anonymous type in string format.*/
    {	 	

        int digCount = 0;
        int letterCount = 0;

        char[] charArray = txt.ToCharArray();

        foreach(char c in charArray)

        {
            if (Char.IsDigit(c))
            {
                digCount++;


            }

            else if (Char.IsLetter(c))
            {

                letterCount++;



            }

        }

        var result = new { LETTERS = letterCount, DIGITS = digCount };
        string resultString = result.ToString();
        
        return resultString;



			
    }