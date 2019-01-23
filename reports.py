file_name = "game_stat.txt"


def count_games(file_name):
    """
    Calculate how many games are in the file.
    :param file_name: Text file where include information about games.
    :return: Total amount games in file_name.
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
    return len(games)


def decide(file_name, year):
    """
    Return if there is game from a given year.
    :param file_name: Text file where include information about games.
    :param year: Game release year.
    :return: Boolean value: True if game exists, or False if not.
    """
    with open(file_name) as file_object:
        for line in file_object:
            if str(year) in line:
                return True
    return False


def get_latest(file_name):
    """
    Return the newest title of game.
    :param file_name: Text file where include information about games.
    :return: Title of the game.
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
    years = [int(game.rstrip().split("\t")[2]) for game in games]
    indices = years.index(max(years))

    return games[indices].split("\t")[0]


def count_by_genre(file_name, genre):
    """
    Calculate how many games is by genre.
    :param file_name: Text file where include information about games.
    :param genre: Type/genre of the game.
    :return: Amount of games, searched by genre.
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
    genres = [game.rstrip().split("\t")[3] for game in games]

    return genres.count(genre)
