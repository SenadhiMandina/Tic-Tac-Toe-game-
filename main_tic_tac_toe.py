import os
from game_controller import play_game
from file_handling import save_game_play_history, update_html

def view_game_history_console():
    # Collect all game history files
    history_files = [f for f in os.listdir() if f.startswith("game_history_") and f.endswith(".txt")]
    
    if not history_files:
        print("No game history found.")
        return
    
    # Display each game history file's content
    for history_file in sorted(history_files, key=lambda x: int(x.split("_")[2].split(".")[0])):
        with open(history_file, "r") as file:
            print(f"\n{history_file}:\n{file.read()}")

def view_game_play_history():
    # Opens the HTML file to display game history
    html_file = "view_history.html"
    if os.path.isfile(html_file):
        os.system(f"start {html_file}")  
    else:
        print("No history file found.")

def start():
    # Start the game and direct user choices
    player1_wins = 0
    player2_wins = 0
    draws = 0

    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. Save Game History")
        print("3. View Game History in Console")
        print("4. View Game History in Browser")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player1_wins, player2_wins, draws = play_game(player1_wins, player2_wins, draws)
        elif choice == '2':
            game_history = f"Player 1 (O) wins: {player1_wins}, Player 2 (X) wins: {player2_wins}, Draws: {draws}"
            save_game_play_history(game_history)
            print("Game history saved successfully.")
        elif choice == '3':
            view_game_history_console()
        elif choice == '4':
            update_html()
            view_game_play_history()
        elif choice == '5':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    start()
