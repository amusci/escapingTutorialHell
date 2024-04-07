    public static string NSidedShape(int n)
    /* Create a function that takes a base number and an exponent number and returns the calculation. */
    {

      switch(n)
      {
        case 1:
          return "circle";
        case 2:
          return "semi-circle";
        case 3:
          return "triangle";
        case 4:
          return "square";
        case 5:
          return "pentagon";
        case 6:
          return "hexagon";
        case 7:
          return "heptagon";
        case 8:
          return "octagon";
        case 9:
         return "nonagon";
        case 10:
          return "decagon";
      }

      return "Not 1-10";

      

    }