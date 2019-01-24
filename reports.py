def read_data_from_file(filename):
    """
    Read data about games from indicated file.
    :param filename: Text file where include information about games.
    :return: List of games
    """
    with open(filename) as file_object:
        games = file_object.readlines()
    return games


def count_games(filename):
    """
    Calculate how many games are in the file.
    :param filename: Text file where include information about games.
    :return: Total amount games in filename.
    """
    games = read_data_from_file(filename)
    return len(games)


def decide(filename, year):
    """
    Return if there is game from a given year.
    :param filename: Text file where include information about games.
    :param year: Game release year.
    :return: Boolean value: True if game exists, or False if not.
    """
    games = read_data_from_file(filename)

    years = [int(game.rstrip().split("\t")[2]) for game in games]
    if year in years:
        return True
    return False


def get_latest(filename):
    """
    Return the newest title of game.
    :param filename: Text file where include information about games.
    :return: Title of the game.
    """
    games = read_data_from_file(filename)

    years = [int(game.rstrip().split("\t")[2]) for game in games]
    indices = years.index(max(years))
    return games[indices].split("\t")[0]


def count_by_genre(filename, genre):
    """
    Calculate how many games is by genre.
    :param filename: Text file where include information about games.
    :param genre: Type/genre of the game.
    :return: Amount of games, searched by genre.
    """
    games = read_data_from_file(filename)

    genres = [game.rstrip().split("\t")[3] for game in games]
    return genres.count(genre)


def get_line_number_by_title(filename, title):
    """
    Find the line number of the given game (by title).
    :param filename: Text file where include information about games.
    :param title: Title of the game.
    :return: Line number from the file.
    """
    games = read_data_from_file(filename)
    line_number = [(index + 1)
                   for index, game in enumerate(games) if title in game]
    if len(line_number) != 0:
        return line_number[0]
    else:
        raise ValueError("Could not find {} in {}".format(title, filename))


def sort_abc(filename):
    """
    Return titles of games in alphabetical order.
    :param filename: Text file where include information about games.
    :return: Sorted game titles.
    """
    games = read_data_from_file(filename)

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


def get_genres(filename):
    """
    Return a list of all genres without duplicates.
    :param filename: Text file where include information about games.
    :return: list of genres
    """
    games = read_data_from_file(filename)

    games_genres = set([game.rstrip().split("\t")[3] for game in games])
    games_genres = list(sorted(games_genres))

    return games_genres


def when_was_top_sold_fps(filename, genre="First-person shooter"):
    """
    Find release date of the top sold "First-person shooter".
    :param filename: Text file where include information about games.
    :param genre: String of searched genre.
    :return: year of top sold game
    """
    games = read_data_from_file(filename)

    games_shooters = [game.rstrip().split("\t")
                      for game in games if genre in game]
    sold_copies = [(float(shooter[1])) for shooter in games_shooters]
    if len(sold_copies) != 0:
        index_top_sold_game = sold_copies.index(max(sold_copies))
    else:
        raise ValueError("Could not find {} in {}".format(genre, filename))

    return int(games_shooters[index_top_sold_game][2])
