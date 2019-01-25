import os


import reports


filename = "game_stat.txt"

git 
def display_get_most_played():
    title_game = reports.get_most_played(filename)
    print("Title of most played game in {}: {}\n" .format(filename, title_game))


def display_sum_sold():
    sold_games = reports.sum_sold(filename)
    print("Total sold copies from {} file is: {} millions\n" .format(filename, sold_games))


def display_get_selling_avg():
    average_sell = reports.get_selling_avg(filename)
    print("Average selling in {} is: {} per game\n" .format(filename, average_sell))


def display_count_longest_title():
    longest_title = reports.count_longest_title(filename)
    print("The longest title in {} has a {} characters\n" .format(filename, longest_title))


def display_get_date_avg():
    average_date = reports.get_date_avg(filename)
    print("The average date for all games in {} is: {}\n" .format(filename, average_date))


def display_get_game():
    title = input("Please give me a title searched game: ")
    info_about_game = reports.get_game(filename, title)
    print("Properties of the game: {}\n" .format(info_about_game))


def display_count_grouped_by_genre():
    dict_of_genre = reports.count_grouped_by_genre(filename)
    print("Game grouped by genre:")
    for genre, value in dict_of_genre.items():
        print("{}: {}" .format(genre, value))
    print()


def display_get_date_ordered():
    ordered_games = reports.get_date_ordered(filename)
    print("Ordered games by date and by alphabet:")
    for title in ordered_games:
        print(title)
    print()


def choose_option():
    print("1. title of most played game"
          "\n2. how many copies have been sold in total"
          "\n3. average selling"
          "\n4. how many characters long is the longest title"
          "\n5. average of the release dates"
          "\n6. properties of the game"
          "\n7. how many games are grouped by genre"
          "\n8. ordered titles of games by date and alphabet"
          "\n9. Exit")

    option = input("\nDisplay: ")
    return option


def main():
    os.system('clear')
    while True:
        option = choose_option()
        os.system('clear')

        if option == "1":
            display_get_most_played()
        elif option == "2":
            display_sum_sold()
        elif option == "3":
            display_get_selling_avg()
        elif option == "4":
            display_count_longest_title()
        elif option == "5":
            display_get_date_avg()
        elif option == "6":
            display_get_game()
        elif option == "7":
            display_count_grouped_by_genre()
        elif option == "8":
            display_get_date_ordered()
        elif option == "9":
            break


if __name__ == "__main__":
    main()
