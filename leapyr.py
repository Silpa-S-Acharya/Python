year=int(input("Enter the current year\t"))
fut=int(input("Enter the future year\t"))
print("The leap years in range are\n" )
for year in range(year,fut+1):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year)



