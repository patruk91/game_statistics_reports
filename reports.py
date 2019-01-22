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
    Display if there is game from a given year.
    :param file_name: Text file where include information about games.
    :param year: Game release year.
    :return: Boolean value: True if game exists, or False if not.
    """
    with open(file_name) as file_object:
        for line in file_object:
            if str(year) in line:
                return True
    return False
