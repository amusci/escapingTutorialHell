	  public static string Stutter(string word)
    /*Write a function that stutters a word as if someone is struggling to read it.
    
    The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.*/
		{

      string start = word[0].ToString() + word[1];

      return start + "... " + start + "... " +word + "?";
			
		}