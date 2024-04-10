        public static string SubReddit(string link)
        /*Create a function to extract the name of the subreddit from its URL.*/
        {

            string[] site = link.TrimEnd('/').Split('/');

            return site[site.Length - 1];


        }