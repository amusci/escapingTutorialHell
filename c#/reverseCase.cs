    public static string ReverseCase(string str)
    /* Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa. */ 
    
    {
        char[] charArray = str.ToCharArray();
        ;

        for (int i = 0; i < charArray.Length; i++) 
        {

            if (char.IsLower(charArray[i])) {

                charArray[i] = char.ToUpper(charArray[i]);

            }

            else if (char.IsUpper(charArray[i])) {

                charArray[i] = char.ToLower(charArray[i]);

            }
        }

        return new string (charArray);

        }