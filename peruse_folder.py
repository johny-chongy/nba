from peruse_methods import peruse_csv, count_b2b, write_csv
from pathlib import Path

ACTIONS = ["print_rows", "count_b2b"]
DECISIONS = {'y': True, 'n': False}

#input desired folder pathway
folder_pathway = input("Enter folder directory: ")
folder = Path(folder_pathway)
print(f"using {folder_pathway} pathway")

#input action item
action = input(f"Input what what you'd like to do: {ACTIONS}")
if action not in ACTIONS:
    raise ValueError("Input is not a valid action")

for file in folder.iterdir():
    if action == "count_b2b":
        teams = count_b2b(f"{folder_pathway}/{file.name}")
        print(teams)
        create_csv = input(f"Would you like to create a csv file for {file.name}? [y/n] ")
        if DECISIONS[create_csv]:
            file_destination = input("Please provide full file destination (with .csv): ")
            write_csv(file_destination, list(teams.values()))
            print(f"Generated csv file at {file_destination}.")

    elif file.is_file():
        print(file.name)

        #executes based on action
        if action == "print_rows":
            peruse_csv(f"{folder_pathway}/{file.name}")
