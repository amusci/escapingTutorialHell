    public static string ReverseAndNot(int i)
    /*
    Write a function that takes an integer i and returns a string with the integer backwards followed by the original integer.

    To illustrate:

    "123"

    We reverse "123" to get "321" and then add "123" to the end, resulting in "321123".
    */

        {

            return string.Concat(i.ToString().OrderByDescending(x => x)) + i.ToString();
			
		}