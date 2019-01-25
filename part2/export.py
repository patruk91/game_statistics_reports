import os


import reports


filename = "game_stat.txt"
exported_file = "exported_answers.txt"


def export_to_file(data_from_user):
    """Export data from other functions to a file"""
    with open(exported_file, "a") as file_object:
        file_object.write(data_from_user)


def export_get_most_played():
    """Export to file: the title of the most played game (sold the most copies)."""
    title_game = reports.get_most_played(filename)
    message = "Title of most played game in {}: {}\n" .format(
        filename, title_game)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_sum_sold():
    """Export to file: how many copies have been sold in total."""
    sold_games = reports.sum_sold(filename)
    message = "Total sold copies from {} file is: {} millions\n" .format(
        filename, sold_games)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_selling_avg():
    """Export to file: average selling."""
    average_sell = reports.get_selling_avg(filename)
    message = "Average selling in {} is: {} per game\n" .format(
        filename, average_sell)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_count_longest_title():
    """Export to file: how many characters long have the longest title."""
    longest_title = reports.count_longest_title(filename)
    message = "The longest title in {} has a {} characters\n" .format(
        filename, longest_title)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_date_avg():
    """Export to file: the average of the release dates."""
    average_date = reports.get_date_avg(filename)
    message = "The average date for all games in {} is: {}\n" .format(
        filename, average_date)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_game():
    """Export to file: properties of searched game."""
    title = input("Please give me a title searched game: ")
    info_about_game = reports.get_game(filename, title)
    message = "Properties of the game: {}\n" .format(info_about_game)
    export_to_file(message)
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_count_grouped_by_genre():
    """Export to file: how many games are there grouped by genre."""
    dict_of_genre = reports.count_grouped_by_genre(filename)
    print("Game grouped by genre:\n")
    for genre, value in dict_of_genre.items():
        export_to_file("{}: {}\n" .format(genre, value))
    print("DATA TRANSFERRED TO A FILE: exported_answers.txt!\n")


def export_get_date_ordered():
    """Export to file: ordered list of the games by date and alphabet order."""
    ordered_games = reports.get_date_ordered(filename)
    print("Ordered games by date and by alphabet:")
    for title in ordered_games:
        export_to_file(title + "\n")


def choose_option():
    """
    Display menu with options.
    :return: user option
    """
    print("1. title of most played game"
          "\n2. how many copies have been sold in total"
          "\n3. average selling"
          "\n4. how many characters long is the longest title"
          "\n5. average of the release dates"
          "\n6. properties of the game"
          "\n7. how many games are grouped by genre"
          "\n8. ordered titles of games by date and alphabet"
          "\n9. Exit")

    option = input("\nexport: ")
    return option


def main():
    os.system('clear')
    while True:
        option = choose_option()
        os.system('clear')

        if option == "1":
            export_get_most_played()
        elif option == "2":
            export_sum_sold()
        elif option == "3":
            export_get_selling_avg()
        elif option == "4":
            export_count_longest_title()
        elif option == "5":
            export_get_date_avg()
        elif option == "6":
            export_get_game()
        elif option == "7":
            export_count_grouped_by_genre()
        elif option == "8":
            export_get_date_ordered()
        elif option == "9":
            break


if __name__ == "__main__":
    main()
