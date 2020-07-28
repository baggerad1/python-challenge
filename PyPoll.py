import csv

total_votes = 0


candidate_list = []

candidate_name = []


candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []


with open('election.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate_list.append(str(row[2]))
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

    candidate_vote_percent[0] = round(
        100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(
        100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(
        100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(
        100 * (candidate_vote[3] / total_votes), 4)

    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
        candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
        candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
        candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
        candidate_winner = candidate_name[3]

    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    print(
        f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
    print(
        f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
    print(
        f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
    print(
        f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
    print("-----------------------------")
    print(f"Winner: {candidate_winner}")

    csvfile.close()
file = open("output.txt", "w")

file.write("Financial Analysis" + "\n")

file.write(
    "...................................................................................." + "\n")

file.write("Election Results")
file.write("\n")
file.write("------------------------")
file.write("\n")
file.write(f"Total Votes: {total_votes}")
file.write("\n")
file.write(
    f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
file.write("\n")
file.write(
    f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
file.write("\n")
file.write(
    f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
file.write("\n")
file.write(
    f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
file.write("\n")
file.write("-----------------------------")
file.write("\n")
file.write(f"Winner: {candidate_winner}")
file.write("\n")
