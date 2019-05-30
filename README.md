# Plex Playlist Sorter
Version: 1.1

URL: https://github.com/uswemar/PlexPlaylistSorter

Python Version: 3.7

Author: uswemar (http://reddit.com/u/swemar | https://github.com/uswemar)


# Disclaimer:
Use with care! The code is rough. Really rough. This is my first Python script and I wrote
it after sitting through a couple of hours of 'Python for Beginners' tutorials. There
is almost no error handling and it WILL write (if selected) a Plex Playlist to your account.
Even as a beginner I can see many things that can be improved in the code, but hey, it works.

# What does it do: 
Sorts (and creates a copy of) an existing [movie] playlist (in ascending or descending order) on your Plex Server/Account
by either (1) Critic Rating, (2) Audience Rating, or (3) Combined Rating, depending on user input/choice.

# Before use: 
You need to change a couple of variables, starting with the PLEX_SERVER_URL (line 46)
and the PLEX_TOKEN (line 47) --OR-- you can choose to use a config.ini file in which case you need to
either store the file in the default location (~/.config/plexapi/config.ini) or update the PLEX_CONFIG_PATH
variable (line 47) to where you have saved it i.e. "config.ini" if it's in the same folder as this script.

For more information on how to structure your config.ini file check out the "Configuration" section in
https://buildmedia.readthedocs.org/media/pdf/python-plexapi/stable/python-plexapi.pdf
How to find your Plex token:
https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

# Why:
I created this because I wanted to sort my movie playlist by rating and there was no option in Plex
to do so. I was aware of Python and the Plex API so I knew it could be done but I had no 
practical knowledge of either so I scoured the web for instructions and/or finished solutions.
After searching around endlessly online for a finished solution/script I confronted my laziness
and decided to learn the basics of Python and create my own script. This was the result. Fin.
