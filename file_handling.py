import os

def save_game_play_history(game_history):
    # Find the highest numbered game history file
    history_files = [f for f in os.listdir() if f.startswith("game_history_") and f.endswith(".txt")]
    max_number = 0
    for file in history_files:
        try:
            number = int(file.split("_")[2].split(".")[0])
            if number > max_number:
                max_number = number
        except ValueError:
            continue
    
    # Generate the next number for the new filename
    next_number = max_number + 1
    file_name = f"game_history_{next_number}.txt"
    
    # Save to a new text file
    with open(file_name, "w") as file:
        file.write(game_history + "\n")
    
    # Update HTML file with the new history file
    update_html()

def update_html():
    # HTML file to display game history
    html_file = "view_history.html"
    
    # Collect all game history files
    history_files = [f for f in os.listdir() if f.startswith("game_history_") and f.endswith(".txt")]
    
    # Latest game histories from the text files
    history_content = ""
    for history_file in sorted(history_files, key=lambda x: int(x.split("_")[2].split(".")[0])):
        with open(history_file, "r") as file:
            history_content += f"<h2>{history_file}</h2>\n<pre>{file.read()}</pre>\n"
    
    # Update the HTML file
    with open(html_file, "w") as file:
        file.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Game History</title>
</head>
<body>
    <h1>Game History</h1>
    {history_content}
</body>
</html>
        """)

def view_game_play_history():
    # Opens the HTML file to display game history
    html_file = "view_history.html"
    if os.path.isfile(html_file):
        os.system(f"start {html_file}")  
    else:
        print("No history file found.")
