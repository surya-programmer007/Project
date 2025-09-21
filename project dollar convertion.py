#To convert dolar to other currency
print("Welcome to currency converter")
print("Make sure that this is your currency converter in upto date")#date 2025/09/21
country={
    'IND':88.12,
    'YEN':147.951,
    'EURO':0.85,
    'POUND':0.74,
    'AUS':1.51,
    'CAD':1.37,
    'SGD':1.28,
    'CHF':0.79,
    'MYR':4.20,
    'RMB':7.11 
}
print("1.IND-INDIA\n2.YEN-JAPAN\n3.EURO-EUROPE\n4.POUND-ENGLAND\n5.AUS-AUSTRALIA\n6.CAD-CANADA\n7.SGD-SINGAPORE\n8.CHF-SWITZERLAND\n9.MYR-MALAYSIA\n10.RMB-CHINA")
dollar=float(input("Enter the amount in dollar:"))
choice=input("Enter your choice (Only the code ,IND,YEN ...etc in caps lock):")
if choice in country:
    converted_money=country[choice]*dollar
    print(f"Your {dollar} dollar is equal to {converted_money} {choice}")
else:
    print("The country is not programed sorry for the inconviences") 