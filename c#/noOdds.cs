        public static int[] NoOdds(int[] arr)
        {
            List<int> even = new List<int>();

            for (int i = 0; i < arr.Length; i++) {
                if (arr[i] % 2 == 0) {

                        even.Add(arr[i]);

                }

            }


            return even.ToArray();
            
        }