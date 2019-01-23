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


def get_line_number_by_title(file_name, title):
    """
    Find the line number of the given game (by title).
    :param file_name: Text file where include information about games.
    :param title: Title of the game.
    :return: Line number from the file.
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
        line_number = [(index + 1) for index, game in enumerate(games) if title in game]
        if len(line_number) != 0:
            return line_number[0]
        else:
            raise ValueError("Could not find {} in {}".format(title, file_name))


def sort_abc(file_name):
    """
    Return titles of games in alphabetical order.
    :param file_name: Text file where include information about games.
    :return: Sorted game titles.
    """

    with open(file_name) as file_object:
        games = file_object.readlines()
    games_titles = [game.rstrip().split("\t")[0] for game in games]
    i = 0

    while i < len(games_titles):
        for index in range(len(games_titles) - 1):
            if games_titles[index] > games_titles[index + 1]:
                temp = games_titles[index]
                games_titles[index] = games_titles[index + 1]
                games_titles[index + 1] = temp
        i += 1
    return games_titles


def get_genres(file_name):
    """
    Return a list of all genres without duplicates.
    :param file_name: Text file where include information about games.
    :return: list of genres
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
    games_genres = set([game.rstrip().split("\t")[3] for game in games])
    games_genres = list(sorted(games_genres))

    return games_genres

