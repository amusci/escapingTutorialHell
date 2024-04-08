	public static string FizzBuzz(int n)
  /* Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    If the number is a multiple of 3 the output should be "Fizz".
    If the number given is a multiple of 5, the output should be "Buzz".
    If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
    The output should always be a string even if it is not a multiple of 3 or/and 5. */
	{

    if (n % 3 == 0 && n % 5 == 0) 
    {
      return "FizzBuzz";
    }
    else if (n % 3 == 0) 
    {
      return "Fizz";
    }
    else if (n % 5 == 0) 
    {

      return "Buzz";
    }

    else 
    
    {

      return n.ToString();
    }

    }