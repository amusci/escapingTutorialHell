        public static int NumberOfDays(int[] coordinates) 
        /* Captain Hook and his crew are currently resting at Origin Shore. They are about to embark on their next adventure to an undisclosed location (x, y) to find treasure.

        Captain Hook's ship can only move exactly north, south, east or west. It takes exactly 1 day for the ship to travel 1 unit in one of the four cardinal directions.

        After every 5 days, the crew will take one day of rest.

        Given the location of the treasure, find out how long it takes for Captain Hook and his crew to find the treasure. The ship is currently at coordinate (0, 0). */

        {
            int total = Math.Abs(coordinates[0]) + Math.Abs(coordinates[1]);
            int restDays = total / 5;

            if (total % 5 != 0) {
                Console.WriteLine(restDays + " before ");
                restDays ++;
                Console.WriteLine(restDays);


            }


            return total + restDays - 1;
                
        }