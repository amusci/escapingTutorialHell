        public static int square_areas_difference(int radius)
        
        {
            /* Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

            Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.
            */

            double lengthBigSquare = 2 * radius;

            double areaBigSquare = Math.Pow(2 * radius, 2);

            double areaSmallSquare = Math.Pow(radius, 2) + Math.Pow(radius, 2);

            return (int)(areaBigSquare - areaSmallSquare);

        }