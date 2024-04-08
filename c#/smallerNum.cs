	public static string smallerNum(string n1, string n2)
    /*Create a function that returns the smaller number.*/
    {
      int num1 = Convert.ToInt32(n1);
      int num2 = Convert.ToInt32(n2); 

      if (num1 < num2) {
        return n1;
      }
      else {

        return n2;
      }

    }