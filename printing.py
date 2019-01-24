import os


import reports


filename = "game_stat.txt"


def display_count_games():
    """Display how many games are in the file."""
    numbers_of_games = reports.count_games(filename)
    print("Total games in {}: {}\n" .format(filename, numbers_of_games))


def display_decide():
    """Display if there is game from a given year."""
    year = int(input("Enter the searched year: "))
    value = reports.decide(filename, year)
    if value is True:
        print(
            "We have a game from {} year in {}\n" .format(
                str(year), filename))
    else:
        print(
            "Sorry, we don't have game from {} year in {}\n".format(
                str(year), filename))


def display_get_latest():
    """Display the newest title of game."""
    latest_game = reports.get_latest(filename)
    print("Title of latest game: {}\n" .format(latest_game))


def display_count_by_genre():
    """Display how many games is by genre."""
    genre = input("Please. give me a genre of game: ")
    genres = reports.count_by_genre(filename, genre)
    print("We have {} games from {} genre.\n" .format(genres, genre))


def display_get_line_number_by_title():
    """Display the line number of the given game (by title)."""
    title = input("Please provide title of the game: ")
    line_number = reports.get_line_number_by_title(filename, title)
    print("The number of line in {} is {}\n" .format(filename, line_number))


def display_sort_abc():
    """Display titles of games in alphabetical order."""
    sorted_games = reports.sort_abc(filename)
    print("List of games in alphabetical order: ")
    [print(game_title) for game_title in sorted_games]
    print()


def display_get_genres():
    """Display a list of all genres without duplicates."""
    game_genres = reports.get_genres(filename)
    [print(genre) for genre in game_genres]
    print()


def display_when_was_top_sold_fps():
    """Display release date of the top sold "First-person shooter"."""
    genre = input("Please, give me a searched genre game: ")
    top_game = reports.when_was_top_sold_fps(filename, genre)
    print("The top sold {} genre was released in: {}\n" .format(genre, top_game))


def choose_option():
    """
    Display menu with options.
    :return: user option
    """
    print("1. how many games are in the file."
          "\n2. is there a game from a given year."
          "\n3. the latest game."
          "\n4. how many games do we have by genre."
          "\n5. line number of the given game (by title)"
          "\n6. alphabetical ordered list of the titles"
          "\n7. all genres without duplicates"
          "\n8. release date of the top sold game (by genre)"
          "\n9. Exit")

    option = input("\nDisplay: ")
    return option


def main():
    os.system('clear')
    while True:
        option = choose_option()
        os.system('clear')

        if option == "1":
            display_count_games()
        elif option == "2":
            display_decide()
        elif option == "3":
            display_get_latest()
        elif option == "4":
            display_count_by_genre()
        elif option == "5":
            display_get_line_number_by_title()
        elif option == "6":
            display_sort_abc()
        elif option == "7":
            display_get_genres()
        elif option == "8":
            display_when_was_top_sold_fps()
        elif option == "9":
            break


if __name__ == "__main__":
    main()
