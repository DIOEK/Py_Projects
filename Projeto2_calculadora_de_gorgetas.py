"""Another simple project, a tip calculator. What's nice about these tiny scripts is that thay may be recicled
 later and turned into classes with little effort."""



food_bill = float(input("Please, inform the price of your food bill"))
percentage = int(input("What tip percentage would you like to give? 10, 12 or 15? "))
number_people = int(input("Inform how many people are there to split the bill? "))
appllied_tip_percentage = ((percentage/100)*food_bill)
total_price = ((food_bill + appllied_tip_percentage)/ number_people)

print(f"Each person should pay: ${total_price}")




