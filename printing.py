import os


import reports


filename = "game_stat.txt"


def display_count_games():
    numbers_of_games = reports.count_games(filename)
    print("Total games in {}: {}\n" .format(filename, numbers_of_games))


def display_decide():
    year = int(input("Enter the searched year: "))
    value = reports.decide(filename, year)
    if value is True:
        print("We have a game from {} year in {}\n" .format(str(year), filename))
    else:
        print("Sorry, we don't have game from {} year in {}\n".format(str(year), filename))


def display_get_latest():
    latest_game = reports.get_latest(filename)
    print("Title of latest game: {}\n" .format(latest_game))


def display_count_by_genre():
    genre = input("Please. give me a genre of game: ")
    genres = reports.count_by_genre(filename, genre)
    print("We have {} games from {} genre.\n" .format(genres, genre))


def display_get_line_number_by_title():
    title = input("Please provide title of the game: ")
    line_number = reports.get_line_number_by_title(filename, title)
    print("The number of line in {} is {}\n" .format(filename, line_number))


def display_sort_abc():
    sorted_games = reports.sort_abc(filename)
    print("List of games in alphabetical order: ")
    [print(game_title) for game_title in sorted_games]
    print()


def display_get_genres():
    game_genres = reports.get_genres(filename)
    [print(genre) for genre in game_genres]
    print()


def display_when_was_top_sold_fps():
    genre = input("Please, give me a searched genre game: ")
    top_game = reports.when_was_top_sold_fps(filename, genre)
    print("The top sold {} genre was released in: {}\n" .format(genre, top_game))


def choose_option():
    print("1. how many games are in the file.")
    print("2. is there a game from a given year.")
    print("3. the latest game.")
    print("4. how many games do we have by genre.")
    print("5. line number of the given game (by title)")
    print("6. alphabetical ordered list of the titles")
    print("7. all genres without duplicates")
    print("8. release date of the top sold game (by genre)")
    print("9. Exit")

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
