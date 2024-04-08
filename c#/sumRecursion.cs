  public static int Sum(int n) 
  /*Write a function that recursively finds the sum of the first n natural numbers.*/
	{

    if (n == 1 || n == 0) {

      return 1;
    }


    return n + Sum(n -1); 

		
	}