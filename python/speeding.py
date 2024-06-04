'''One cause for speeding is the desire to shorten the time spent traveling.
In long distance trips, speeding does save an appreciable amount of time.
However, the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.'''

def time_saved(s_lim, s_avg, d):
    speed_limit = d / s_lim
    speeding = d / s_avg

    return round((speed_limit - speeding) * 60,1)