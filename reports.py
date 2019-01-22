file_name = "game_stat.txt"


def count_games(file_name):
    """
    Calculate how many games are in the file.
    :param file_name: Text file where included informations about games.
    :return: Total amount games in file_name.
    """
    with open(file_name) as file_object:
        games = file_object.readlines()
    return len(games)



