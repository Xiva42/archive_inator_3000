#################################################### Module Imports ###############################################
from modules import functions as f


###################################################################################################################
#################################################### Constants ####################################################
###################################################################################################################
# Different web address roots.
IMDB_MOVIE_ROOT_ADDRESS = "https://www.imdb.com/title/"
IMDB_API_TITLE_ROOT_ADRESS = "https://api.imdbapi.dev/titles/"

# GUI related constants.
APPLICATION_THEME = "DarkGrey9"
# Colors
COLOR_RED = "Red"
COLOR_LIGHT_GREEN = "LightGreen"
COLOR_GOLD = "Gold"
###################################################################################################################
#################################################### Variables ####################################################
###################################################################################################################
debug = 0

###################################################################################################################
#################################################### lists ########################################################
###################################################################################################################
# Lists
    # This list will contain the output message and will be joined with \t in the end.
output = []
    # This list contains all the super_genres that will be added to the output list.
final_super_genres = []


###################################################################################################################
#################################################### Dictionaries #################################################
###################################################################################################################
# This dictionary contains the order of data in the output as keys and the relative extract function as the value.
extracton_order = {"title":f.extract_title, "runtime":f.extract_runtime, "super_genres":f.extract_super_genres, "location":f.extract_location, "imdb_link":f.extract_link}
# This dictionary contains all the super_genres as the key and its sub_genre relatives as its values.
                                # Super Genres      # Sub Genres
super_and_sub_genre_relation =  {"Action"           : ("Action", "Action Epic", "B-Action", "Car Action", "Disaster", "Martial Arts", "One-Person Army Action", "Superhero", "Sword & Sandal", "War", "War Epic", "Gun Fu", "Kung Fu", "Samurai", "Wuxia"),
                                "Adventure"         : ("Adventure", "Desert Adventure", "Dinosaur Adventure", "Adventure Epic", "Globetrotting Adventure", "Jungle Adventure", "Mountain Adventure", "Quest", "Road Trip", "Sea Adventure", "Swashbuckler", "Teen Adventure", "Urban Adventure"),
                                "Spy"               : ("Spy"),
                                "Animation"         : ("Animation", "Adult Animation", "Computer Animation", "Hand-Drawn Animation", "Stop Motion Animation"),
                                "Anime"             : ("Anime", "Isekai", "Iyashikei", "Josei", "Mecha", "Seinen", "Shōnen", "Shōjo", "Slice of Life"),
                                "Comedy"            : ("Comedy", "Buddy Comedy", "Buddy Cop", "Dark Comedy", "Farce", "High-Concept Comedy", "Mockumentary", "Parody", "Quirky Comedy", "Raunchy Comedy", "Satire", "Screwball Comedy", "Sitcom", "Sketch Comedy", "Slapstick", "Stand-Up", "Stoner Comedy", "Teen Comedy"),
                                "Con"               : ("Caper", "Heist"),
                                "Crime"             : ("Crime", "Caper", "Cop Drama", "Drug Crime", "Film Noir", "Gangster", "Heist", "Police Procedural", "True Crime"),
                                "Disaster"          : ("Disaster"),
                                "Documentary"       : ("Documentary", "Crime Documentary", "Docuseries", "Faith & Spirituality Documentary", "Food Documentary", "History Documentary", "Military Documentary", "Music Documentary", "Nature Documentary", "Political Documentary", "Science & Technology Documentary", "Sports Documentary", "Travel Documentary"),
                                "Drama"             : ("Drama", "Biography", "Coming-of-Age", "Costume Drama", "Docudrama", "Epic", "Financial Drama", "History", "Legal Drama", "Medical Drama", "Period Drama", "Political Drama", "Prison Drama", "Psychological Drama", "Showbiz Drama", "Soap Opera", "Teen Drama", "Tragedy", "Workplace Drama", "Korean Drama", "Telenovela", "Cop Drama"),
                                "Dystopia"          : ("Dystopian Sci-Fi", "Cyberpunk"),
                                "Epic"              : ("Epic", "Action Epic", "War Epic", "Historical Epic", "Fantasy Epic", "Romantic Epic", "Sci-Fi Epic", "Western Epic"),
                                "Fantasy"           : ("Fantasy", "Dark Fantasy", "Fantasy Epic", "Fairy Tale", "Supernatural Fantasy", "Sword & Sorcery", "Teen Fantasy"),
                                "Gangster"          : ("Gangster"),
                                "Holiday"           : ("Holiday", "Holiday Animation", "Holiday Comedy", "Holiday Family", "Holiday Romance"),
                                "Horror"            : ("Horror", "B-Horror", "Body Horror", "Folk Horror", "Found Footage Horror", "Monster Horror", "Psychological Horror", "Slasher Horror", "Splatter Horror", "Supernatural Horror", "Teen Horror", "Vampire Horror", "Werewolf Horror", "Witch Horror", "Zombie Horror"),
                                "Music"             : ("Music", "Concert"),
                                "Musical"           : ("Musical", "Classic Musical", "Jukebox Musical", "Pop Musical", "Rock Musical"),
                                "Mystery"           : ("Mystery", "Bumbling Detective", "Cozy Mystery", "Hard-boiled Detective", "Suspense Mystery", "Whodunnit"),
                                "One-Man-Army"      : ("One-Person Army Action"),
                                "Romance"           : ("Romance", "Dark Romance", "Romantic Epic", "Feel-Good Romance", "Romantic Comedy", "Steamy Romance", "Teen Romance", "Tragic Romance"),
                                "Sci-Fi"            : ("Sci-Fi", "Alien Invasion", "Artificial Intelligence", "Cyberpunk", "Kaiju", "Space Sci-Fi", "Steampunk", "Time Travel"),
                                "Superhero"         : ("Superhero"),
                                "Sport"             : ("Sport", "Baseball", "Basketball", "Boxing", "Extreme Sport", "Football", "Motorsport", "Soccer", "Water Sport"),
                                "Swashbuckler"      : ("Swashbuckler"),
                                "Time Travel"       : ("Time Travel"),
                                "Thriller"          : ("Thriller", "Conspiracy Thriller", "Cyber Thriller", "Erotic Thriller", "Giallo", "Legal Thriller", "Political Thriller", "Psychological Thriller", "Serial Killer", "Spy", "Survival"),
                                "Vampire"           : ("Vampire Horror"),
                                "War"               : ("War", "War Epic"),
                                "Western"           : ("Western", "Classical Western", "Contemporary Western", "Western Epic", "Spaghetti Western")
                                }
# This dictionary keeps track of which super_genres already has been added to the final_genres list, to avoid duplicates.
already_added_super_genre =     {
                                "Action"            : False,
                                "Adventure"         : False,
                                "Spy"               : False,
                                "Animation"         : False,
                                "Anime"             : False,
                                "Comedy"            : False,
                                "Con"               : False,
                                "Crime"             : False,
                                "Disaster"          : False,
                                "Documentary"       : False,
                                "Drama"             : False,
                                "Dystopia"          : False,
                                "Epic"              : False,
                                "Fantasy"           : False,
                                "Gangster"          : False,
                                "Holiday"           : False,
                                "Horror"            : False,
                                "Music"             : False,
                                "Musical"           : False,
                                "Mystery"           : False,
                                "One-Man-Army"      : False,
                                "Romance"           : False,
                                "Sci-Fi"            : False,
                                "Superhero"         : False,
                                "Sport"             : False,
                                "Swashbuckler"      : False,
                                "Time Travel"       : False,
                                "Thriller"          : False,
                                "Vampire"           : False,
                                "War"               : False,
                                "Western"           : False
                                }
