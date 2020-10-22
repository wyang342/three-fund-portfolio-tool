# initializing global variables
three_fund = ["US stocks", "International stocks", "Bonds"]
percentages = [0, 0, 0]
initial_amounts = [0, 0, 0]
money_to_add = 0


def input_percentages():
    while True:
        # input percentages of each fund. breaks if not a number.
        for (index, fund) in enumerate(three_fund):
            print("\nWhat is the percent of " + fund + "?")
            try:
                to_add = float(input("Please enter a number:"))
            except:
                print("Please enter a number. Starting over.")
                break
            percentages[index] = to_add
        return
    return


def input_initial_amounts():
    while True:
        # input initial amounts for each fund. breaks if not a number.
        for (index, fund) in enumerate(three_fund):
            print("\nWhat is the dollar amount already invested in " + fund + "?")
            try:
                to_add = float(input("Please enter a number:"))
            except:
                print("Please enter a number. Starting over.")
                break
            initial_amounts[index] = to_add
        return
    return


def input_money_to_add():
    while True:
        print("How much money will you add?")
        try:
            money_to_add = float(input("Please enter a number:"))
        except:
            print("Please enter a number. Starting over.")
            break
    return


def function():
    while True:
        input_percentages()
        [us_percentage, int_percentage, bond_percentage] = percentages

        # checking if percentages add up to 100
        total_percentage = 0
        for percentage in percentages:
            total_percentage += percentage
        if total_percentage != 100:
            print("The numbers you provided don't add up to 100. Starting over.")
            continue

        # getting initial total amount
        input_initial_amounts()
        [us_initial, int_initial, bonds_initial] = initial_amounts
        total_initial = us_initial + int_initial + bonds_initial

        input_money_to_add()

        # getting the final total amount
        total_final = total_initial + money_to_add

        us_to_invest = us_percentage * 0.01 * total_final - us_initial
        int_to_invest = int_percentage * 0.01 * total_final - int_initial
        bonds_to_invest = bond_percentage * 0.01 * total_final - bonds_initial

        print("You need to invest {} in US stocks, {} in international stocks, and {} in bonds.".format(us_to_invest,
                                                                                                        int_to_invest,
                                                                                                        bonds_to_invest))


function()
