	public static string ReverseCapitalize(string str) 
    /*Create a function that takes a string of lowercase characters and returns that string reversed and in upper case. */
    {
        char[] charArray = str.ToCharArray();

        Array.Reverse(charArray);

        return new string(charArray).ToUpper();
		
	}