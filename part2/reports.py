filename = "game_stat.txt"


def read_data_from_file(filename):
    """
    Read data about games from indicated file.
    :param filename: Text file where include information about games.
    :return: List of games
    """
    with open(filename) as file_object:
        games = file_object.readlines()
    return games


def get_most_played(filename):
    """
    Find the title of the most played game (i.e. sold the most copies).
    :param filename: Text file where include information about games.
    :return: Title of the game.
    """
    games = read_data_from_file(filename)

    list_of_games = [game.rstrip().split("\t") for game in games]
    sold_copies = [(float(shooter[1])) for shooter in list_of_games]
    index_top_sold_game = sold_copies.index(max(sold_copies))

    return list_of_games[index_top_sold_game][0]


def sum_sold(filename):
    """
    Find how many copies have been sold in total.
    :param filename: Text file where include information about games.
    :return: Number of copies.
    """
    games = read_data_from_file(filename)

    total_sum = sum([float(game.rstrip().split("\t")[1]) for game in games])
    return total_sum


def get_selling_avg(filename):
    """
    Find average selling.
    :param filename: Text file where include information about games.
    :return: Number of average sold copy.
    """
    games = read_data_from_file(filename)
    total_sum = sum_sold(filename)

    average_sell = total_sum / len(games)
    return average_sell


def count_longest_title(filename):
    """
    Find how many characters long have the longest title.
    :param filename: Text file where include information about games.
    :return: Number of length title.
    """
    games = read_data_from_file(filename)

    games_titles = [game.rstrip().split("\t")[0] for game in games]
    longest_title = max([len(title) for title in games_titles])
    return longest_title


def get_date_avg(filename):
    """
    Find the average of the release dates.
    :param filename: Text file where include information about games.
    :return: Average year.
    """
    games = read_data_from_file(filename)

    games_dates = [int(game.rstrip().split("\t")[2]) for game in games]
    average_year = round(sum(games_dates) / len(games_dates))
    return average_year


def get_game(filename, title):
    """
    Find properties searched game.
    :param filename: Text file where include information about games.
    :param title: Title of searched game.
    :return: List with information about game.
    """
    games = read_data_from_file(filename)

    all_info_about_game = [game.rstrip().split("\t") for game in games if game.split("\t")[0] == title][0]

    for i in range(len(all_info_about_game)):
        if all_info_about_game[i].isdigit():
            all_info_about_game[i] = int(all_info_about_game[i])
        elif "." in all_info_about_game[i]:
            all_info_about_game[i] = float(all_info_about_game[i])

    return all_info_about_game


def count_grouped_by_genre(filename):
    """
    Find how many games are there grouped by genre.
    :param filename: Text file where include information about games.
    :return: Dictionary with {genre:number}
    """
    games = read_data_from_file(filename)
    games_genres = [game.rstrip().split("\t")[3] for game in games]
    genre_dict = {}

    for genre in games_genres:
        genre_dict[genre] = genre_dict.get(genre, 0) + 1

    return genre_dict


def get_date_ordered(filename):
    """
    Find ordered list of the games by date and alphabet order.
    :param filename: Text file where include information about games.
    :return: list with sorted titles.
    """
    games = read_data_from_file(filename)
    order = sorted([game.rstrip().split("\t") for game in games], key=lambda x: (int(x[2]), [-ord(c.lower()) for c in x[0]]), reverse=True)
    ordered_titles = [game[0] for game in order]

    return ordered_titles
