#tip_calculator
try:  #DO NOT MODIFY
# TODO: Create a function named calculate_tip
    def tip_calculator():

        # TODO: # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
        total_cost = float(input('Excluding the sales tax, enter the cost of the meal: '))
        num_people = int(input('How many diners are splitting the bill? '))
        tip_percentage = float(input('What is the tip percentage? ')) / 100
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
        sales_tax = 10/100 * total_cost
        tip = total_cost * tip_percentage
        total_bill = float(total_cost + tip + sales_tax)


    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to: The amount each person should pay.   
        each_diner_cost = total_bill / num_people
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        bill_output = f'Total bill: ${total_bill:.2f}'
        print(bill_output)
        per_person_share = f'Each person should pay: ${each_diner_cost:.2f}'
        print(per_person_share)
   
    # NOTE: The amounts are displayed with 2 decimals only

except TypeError: # TODO: modify this except to include a Built-in Exception
        print('Your input is invalid.')
        # TODO: Print an statement telling the user their input is invalid 
    
    #return bill_output, per_person_share


#calculate_tip()

    
    
if __name__ == "__main__": # DO NOT MODIFY

    tip_calculator() # DO NOT MODIFY