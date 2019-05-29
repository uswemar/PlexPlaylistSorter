# Plex Playlist Sorter
Version: 1.0

URL: https://github.com/uswemar/PlexPlaylistSorter

Python Version: 3.7

Coded By: uswemar (http://reddit.com/u/swemar | https://github.com/uswemar)


# Disclaimer:
Use with care! The code is rough. Really rough. This is my first Python script and I wrote
it after sitting through a couple of hours of 'Python for Beginners' tutorials. There
is almost no error handling and it WILL write (if selected) a Plex Playlist to your account.
Even as a beginner I can see many things that can be improved in the code, but hey, it works.

# What does it do: 
Sorts an existing [movie] playlist (in ascending or descending order) on your Plex Server/Account
by either (1) Critic Rating, (2) Audience Rating, or (3) Combined Rating, depending on user input/choice.

# Before use: 
You need to change a couple of variables, starting with the PLEX_SERVER_URL (line 178)
and the PLEX_TOKEN (line 180). Additionally, you need to change 'plist[0].items()' (line 60)
to match the index of the (original/source) playlist you want to sort i.e. if you only have
one playlist it would be 'plist[0].items()' and if you have three playlists and you want to
sort the third one it would be 'plist[2].items()' and so on. You get the point.

# Why:
I created this because I wanted to sort my movie playlist by rating and there was no option in Plex
to do so. I was aware of Python and the Plex API so I knew it could be done but I had no 
practical knowledge of either so I scoured the web for instructions and/or finished solutions.
After searching around endlessly online for a finished solution/script I confronted my laziness
and decided to learn the basics of Python and create my own script. This was the result. Fin.
