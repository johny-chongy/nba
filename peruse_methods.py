import csv
from datetime import datetime

"""
validate_file takes in a file type and makes sure that a filename matches
inputs:
    file_type | str
    file_name | name of file being validated
output:
    boolean
"""
def validate_file(file_type, file_name):
    for i in range(len(file_name)-1,-1,-1):
        if file_name[i] == '.':
            return file_name[i+1::].lower() == file_type.lower()
    raise ValueError("invalid file name input (needs .__ format)")


"""
peruse_csv validates filepath as csv and then iterates through rows if necessary
input:
    csv_file_path | str
"""
def peruse_csv(csv_file_path):
    if not validate_file('csv', csv_file_path):
        print(f"{csv_file_path} is not a .csv file")
        return
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

"""
count_b2b peruses through csv schedule file and returns a dictionary summarizing findings
input:
    csv_file_path | str

output:
    output | obj

    {"Los Angeles Lakers: {b2bs: 15, home_games: 15, away_games: 87}, ...}
"""
def count_b2b(csv_file_path):
    if not validate_file('csv', csv_file_path):
        print(f"{csv_file_path} is not a .csv file")
        return

    output, date_tracker = {}, {}

    def run_team(team_data):
        #create required variables
        home_team, away_team = team_data['Home Team'], team_data['Away Team']
        date_str = team_data['Date']
        date_original = datetime.strptime(date_str, '%d/%m/%Y %H:%M').strftime('%m/%d/%Y')
        date_val = datetime.strptime(date_original, '%m/%d/%Y')

        #check if team names haven't been visited yet
        if home_team not in output:
            output[home_team] = {'team_name': home_team, 'b2bs':0, 'home_games':0, 'away_games':0}
        if away_team not in output:
            output[away_team] = {'team_name': away_team, 'b2bs':0, 'home_games':0, 'away_games':0}

        #update number of home and away games
        output[home_team]['home_games'] += 1
        output[away_team]['away_games'] += 1

        #check if it's a b2b game and update data
        if (date_val-date_tracker.get(home_team, date_val)).days == 1:
            output[home_team]['b2bs'] += 1
        if (date_val-date_tracker.get(away_team, date_val)).days == 1:
            output[away_team]['b2bs'] += 1

        date_tracker[home_team] = date_val
        date_tracker[away_team] = date_val

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            run_team(row)
        return output

"""
write csv takes in file_destination and data to write a csv file
input:
    file_destination | str, file path including desination
    data | obj in format of {title1: {data1}, title2: {data2}, ...}
"""
def write_csv(file_destination, data):
    field_names = list(data[0].keys())
    with open(file_destination, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)