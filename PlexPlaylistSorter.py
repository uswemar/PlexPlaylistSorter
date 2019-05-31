"""

Name: Plex Playlist Sorter
Version: 1.2.0
URL: https://github.com/uswemar/PlexPlaylistSorter
Python Version: 3.7

Author: uswemar (http://reddit.com/u/swemar | https://github.com/uswemar)


Disclaimer:
Use with caution! The code is rough. Really rough. This is my first Python script and I wrote
it after sitting through a couple of hours of 'Python for Beginners' tutorials. There
is almost no error handling and it WILL write (if selected) a Plex Playlist to your account.
Even as a beginner I can see many things that can be improved in the code, but hey, it works.

What does it do:
Sorts (and creates a copy of) an existing [movie] playlist (in ascending or descending order) on your Plex Server/Account
by either (1) Critic Rating, (2) Audience Rating, or (3) Combined Rating, depending on user input/choice.

Before use:
You need to change a couple of variables, starting with the PLEX_SERVER_URL (line 50)
and the PLEX_TOKEN (line 51) --OR-- you can choose to use a config.ini file in which case you need to
either store the file in the default location (~/.config/plexapi/config.ini) or update the PLEX_CONFIG_PATH
variable (line 52) to where you have saved it i.e. "config.ini" if it's in the same folder as this script.

For more information on how to structure your config.ini file check out the "Configuration" section in
https://buildmedia.readthedocs.org/media/pdf/python-plexapi/stable/python-plexapi.pdf
How to find your Plex token:
https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

Why:
I created this because I wanted to sort my movie playlist by rating and there was no option in Plex
to do so. I was aware of Python and the Plex API so I knew it could be done but I had no
practical knowledge of either so I scoured the web for instructions and/or finished solutions.
After searching around endlessly online for a finished solution/script I confronted my laziness
and decided to learn the basics of Python and create my own script. This was the result. Fin.

"""

import requests
import os
from plexapi.utils import choose
from plexapi.server import PlexServer
from plexapi.config import PlexConfig

# Global variables
#
# EDIT THE PARAMS BELOW BEFORE USE
PLEX_SERVER_URL = ""  # Leave blank if you're using a config.ini file
PLEX_TOKEN = ""  # Leave blank if you're using a config.ini file
PLEX_CONFIG_PATH = "config.ini"  # Leave blank if it's in the default directory

# DO NOT EDIT ANYTHING BELOW THIS LINE
if PLEX_CONFIG_PATH:
    CONFIG = PlexConfig(os.environ.get("PLEXAPI_CONFIG_PATH", os.path.expanduser(PLEX_CONFIG_PATH)))
if not PLEX_SERVER_URL:
    PLEX_SERVER_URL = CONFIG.data['auth'].get('server_baseurl')
if not PLEX_TOKEN:
    PLEX_TOKEN = CONFIG.data['auth'].get('server_token')


def create_Playlist(plex, plist, title="Sorted Playlist", list_type=6, is_dry_run=False):
    """
    Function: create_Playlist()

    Will create a new, sorted, playlist in Plex based on the following params:

    :param plex: Plex Server Object
    :param title: Default value = "Sorted Playlist"
    :param list_type: Default value = 6 (Combined Rating, Descending Sort)
    :param is_dry_run: Default value = False (True if you want a dry-run)
    :return: A sorted playlist, saved on your Plex account.
    """

    # Variables
    #
    # to_sort = Dictionary to sort combined movie object & rating in.
    # combined_rating = Combined Critic + Audience rating.
    # critic_rating = Critic rating.
    # audience_rating = Audience rating.
    # sort_order = True for descending sort (Default), False for Ascending sort
    to_sort = dict()
    combined_rating = 0
    critic_rating = 0
    audience_rating = 0
    sort_order = True

    for i in plist:
        # Check if ratings exist. If they do not, set the value to 0 to avoid NoneType errors.
        #
        # Change Log v1.2.0:
        #   Optimized this part of the code.
        critic_rating = round(float(0 if i.rating is None else i.rating), 2)
        audience_rating = round(float(0 if i.audienceRating is None else i.audienceRating), 2)

        # Combine the critic & audience ratings into a combined rating score
        combined_rating = critic_rating + audience_rating

        # Set list type and sorting order based on user input (see function get_Input())
        if list_type == 1:
            to_sort.update({i: critic_rating})
            sort_order = False
        elif list_type == 2:
            to_sort.update({i: critic_rating})
            sort_order = True
        elif list_type == 3:
            to_sort.update({i: audience_rating})
            sort_order = False
        elif list_type == 4:
            to_sort.update({i: audience_rating})
            sort_order = True
        elif list_type == 5:
            to_sort.update({i: combined_rating})
            sort_order = False
        elif list_type == 6:
            to_sort.update({i: combined_rating})
            sort_order = True
        else:
            # If a value other than 1-6 was entered, select default value (6)
            # TODO: Fix this in the get_Input() function to limit to 1-6 only.
            print("No valid sort preference stated: Creating a combined rating playlist in descending order")
            to_sort.update({i: combined_rating})
            sort_order = True

    # Sort the playlist/dictionary by rating
    to_sort = sorted(to_sort.items(), reverse=sort_order, key=lambda x: x[1])

    # Add the sorted playlist/dictionary element to a new list[]
    # TODO: Optimize/Merge this part
    final_list = []
    for elem in to_sort:
        final_list.append(elem[0])

    # Grab the movie item details from Plex based on ID (PlexAPI.ratingKey) and put the object into a new list[]
    new_list = []
    for o in final_list:
        y = plex.fetchItem(o.ratingKey)
        new_list.append(y)

    # Check if dry_run is set to True or not.
    # If True, only output the results.
    # If False, create the new playlist in Plex.
    if is_dry_run:
        print("")
        print("##### Dry-run #####")
        print(f"Title: {title}")
        print(f"Type: {list_type}")
        print("Result:")
        print(to_sort)
    else:
        print(f"A new playlist called {title} has been created and saved.")
        plex.createPlaylist(title, new_list)


def write_csv():
    """

    UNRELEASED
    TODO: Add function to output results as a .csv

    import csv

    output_path = "path/output.csv" # r"win"
    file = open(output_path, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Title", "Rating", etc])

    for o in range(len(list)):
        obj = list[o]
        writer.writerow([obj[0], obj[1], etc])
    """

def set_ssl_params():
    """
    Function: set_ssl_params

    If your Plex server uses HTTPS it may be necessary to turn of verification and to disable warnings
    so not to get an SSL error. This function will do that and return the session to be passed to PlexServer()
    in the connect() function.

    :return: session
    """

    session = requests.Session()
    session.verify = False
    requests.packages.urllib3.disable_warnings()
    return session


def connect(ssl=False):
    """

    Function: connect()

    Will create and connect to a new Plex (Server) object which will be used in the rest of the script.

    :param ssl: Default value = False (Will disable SSL verification if True, might be needed if you use HTTPS)
    :return: plex (object)
    """

    # Checks if ssl is set to True or False and connects to the Plex Server.
    # If True, disables SSL verification and warnings.
    # If False (default), simply connects using baseurl and token.
    if ssl:
        session = set_ssl_params()
        plex = PlexServer(PLEX_SERVER_URL, PLEX_TOKEN, session)
    else:
        plex = PlexServer(PLEX_SERVER_URL, PLEX_TOKEN)

    return plex


def get_Input(plex):
    """
    Function: get_Input()

    Will prompt the user for input to select (1) Title, (2) List and Sort Type, and (3) Create/Save or Dry Run.

    :return: title (string)
    :return: list_type (integer)
    :return: is_dry_run (boolean)
    """

    # Asks user for the title of the new (to be sorted) playlist
    title = input("Title of the new playlist: ")

    # Get a list[] of your playlists from Plex
    plists = plex.playlists()

    # Select the playlist you want to sort
    plist_to_sort = choose("Select playlist to sort", plists, "title")
    plist = plist_to_sort.items()

    # Prints out available options for sorting methods
    print("""
    1: Critic rating, ascending order
    2: Critic rating, descending order
    3: Audience rating, ascending order
    4: Audience rating, descending order
    5: Combined rating, ascending order
    6: Combined rating, descending order
    """)

    # Checks if the option entered is a number (integer) or not
    # TODO: Fix so that ONLY 1-6 can be selected.
    while True:
        try:
            list_type = int(input("Select a list & sorting type (1-6): "))
        except ValueError:
            print("You need to enter a number between 1-6. Try again.")
        else:
            break

    # Print out if user wants to run a test (dry-run) or create & save a new playlist in their Plex account.
    print("""
    1: Create a new playlist & save it
    2: Dry-run only, no changes will be made
    """)

    # Checks if user wants run a test (dry-run) or not
    # TODO: Same as above, fix so that ONLY 1-2 can be selected.
    while True:
        try:
            dry_num = int(input("Select mode (1-2): "))
        except ValueError:
            print("You need to enter a number between 1-2. Try again.")
        else:
            break

    if dry_num == 1:
        is_dry_run = False
    elif dry_num == 2:
        is_dry_run = True
    else:
        # If neither 1 or 2 is selected, use default value (dry-run) to prevent changes to the Plex server/account
        print("Invalid response. Default (dry-run) mode selected.")
        is_dry_run = True

    return plist, title, list_type, is_dry_run


def main():
    """

    Function: main()

    Will connect to the Plex server, get user input, and eventually create a playlist or do a dry run.

    """

    # True = Disable SSL verification when creating a connection. Might be needed if using HTTPS and connection fails.
    # If set to False or left blank () it will connect to the Plex server using the url and token only.
    plex = connect(True)

    # Get user input variable from get_Input() function
    plist, title, list_type, is_dry_run = get_Input(plex)

    # Pass the above variables to the create_Playlist() function
    create_Playlist(plex, plist, title, list_type, is_dry_run)


if __name__ == "__main__":
    main()
