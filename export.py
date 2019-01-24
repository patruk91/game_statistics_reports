import os


import reports


filename = "game_stat.txt"


def export_to_file(data_from_user):
    with open("exported_answers.txt", "a") as file_object:
        file_object.write(data_from_user)


def export_count_games():
    numbers_of_games = str(reports.count_games(filename)) + "\n"
    message = "Total games in {}: {}".format(filename, numbers_of_games)

    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_decide():
    year = int(input("Enter the searched year: "))
    value = reports.decide(filename, year)
    if value is True:
        message = "We have a game from {} year in {}" .format(str(year), filename)

        export_to_file(message)
        print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")
    else:
        message = "Sorry, we don't have game from {} year in {}".format(str(year), filename)

        export_to_file(message)
        print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_latest():
    latest_game = reports.get_latest(filename)
    message = "Title of latest game: {}" .format(latest_game)

    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_count_by_genre():
    genre = input("Please. give me a genre of game: ")
    genres = reports.count_by_genre(filename, genre)
    message = "We have {} games from {} genre." .format(genres, genre)

    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_line_number_by_title():
    title = input("Please provide title of the game: ")
    line_number = reports.get_line_number_by_title(filename, title)
    message = "The number of line in {} is {}" .format(filename, line_number)

    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_sort_abc():
    sorted_games = reports.sort_abc(filename)
    print("List of games in alphabetical order: ")
    for game_title in sorted_games:
        export_to_file(game_title + "\n")

    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_genres():
    game_genres = reports.get_genres(filename)
    for genre in game_genres:
        export_to_file(genre + "\n")

    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_when_was_top_sold_fps():
    genre = input("Please, give me a searched genre game: ")
    top_game = reports.when_was_top_sold_fps(filename, genre)
    message = "The top sold {} genre was released in: {}" .format(genre, top_game)

    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


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

    option = input("\nExport: ")
    return option


def main():
    os.system('clear')
    while True:
        option = choose_option()
        os.system('clear')

        if option == "1":
            export_count_games()
        elif option == "2":
            export_decide()
        elif option == "3":
            export_get_latest()
        elif option == "4":
            export_count_by_genre()
        elif option == "5":
            export_get_line_number_by_title()
        elif option == "6":
            export_sort_abc()
        elif option == "7":
            export_get_genres()
        elif option == "8":
            export_when_was_top_sold_fps()
        elif option == "9":
            break


if __name__ == "__main__":
    main()
