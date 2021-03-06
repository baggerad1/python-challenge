import csv


with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    month_count = []
    profit = []
    change_profit = []

    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])


increase = max(change_profit)
decrease = min(change_profit)


month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(
    f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(
    f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

file = open("output.txt", "w")

file.write("Financial Analysis" + "\n")

file.write(
    "...................................................................................." + "\n")

file.write("Financial Analysis")
file.write("\n")
file.write("------------------------")
file.write("\n")
file.write(f"Total Months:{len(month_count)}")
file.write("\n")
file.write(f"Total: ${sum(profit)}")
file.write("\n")
file.write(
    f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
file.write("\n")
file.write(
    f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
file.write("\n")
file.write(
    f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")
