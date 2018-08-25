import os
import csv

dates = []
revenue = []

budget = os.path.join("Resources", "budget_data.csv")
with open(budget, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        dates.append(row[0])
        revenue.append(row[1])    

number_of_months = len(dates)
        
total_revenue = 0
i = 0
for i in range(number_of_months):
    total_revenue = total_revenue + int(revenue[i])
          
mth_chng = []
a = 0
b = 0
for a in range(0, number_of_months):
  if a == 0:
    mth_chng.append(0)
  else: 
    mth_chng.append(int(revenue[a])-int(revenue[b]))
    b += 1        

sum_mth_chng = 0
x = 0 
for x in range(number_of_months):
    sum_mth_chng = sum_mth_chng + int(mth_chng[x])
    avg_mth_chng = int(sum_mth_chng)/int(number_of_months - 1)

    max_rev_chng = max(mth_chng)
    max_index = mth_chng.index(max_rev_chng)
    max_date = dates[max_index]

    min_rev_chng = min(mth_chng)
    min_index = mth_chng.index(min_rev_chng)
    min_date = dates[min_index]        
        
print(f"Financial Analysis")
print(f"--------------------------------------------")
print(f"Total Months: " + str(number_of_months))
print(f"Total Revenue: $" + str(total_revenue))
print(f"Average Revenue Change: $" + str(avg_mth_chng))
print(f"Greatest Increase in Revenue: " + max_date + " ($" + str(max_rev_chng) + ")")
print(f"Greatest Decrease in Revenue: " + min_date + " ($" + str(min_rev_chng) + ")")

with open("pybank_output.txt", "w") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"---------------------------", file=text_file)
    print(f"Total Months: " + str(number_of_months), file=text_file)
    print(f"Total: $" + str(total_revenue), file=text_file)
    print(f"Average Change: $" + str(avg_mth_chng), file=text_file)
    print(f"Greatest Increase in Profits: " + max_date + " ($" + str(max_rev_chng) + ")", file=text_file)
    print(f"Greatest Decrease in Profits: " + min_date + " ($" + str(min_rev_chng) + ")", file=text_file)