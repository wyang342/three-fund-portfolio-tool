# initializing global variables
three_fund = ["US stocks", "International stocks", "Bonds"]


def input_percentages():
    while True:
        # input percentages of each fund. breaks if not a number.
        global percentages
        percentages = []

        for fund in three_fund:
            print("\nWhat is the percent of " + fund + "?")
            try:
                to_add = float(input("Please enter a number:"))
                percentages.append(to_add)
            except:
                print("This is not a number.\nStarting over.")
                break

        if len(percentages) == 3:
            print("Your investment ratio: {} - {} - {}".format(percentages[0], percentages[1], percentages[2]))
            return


def input_initial_amounts():
    while True:
        # input initial amounts for each fund. breaks if not a number.
        global initial_amounts
        initial_amounts = []

        for fund in three_fund:
            print("\nWhat is the dollar amount already invested in " + fund + "?")
            try:
                to_add = float(input("Please enter a number:"))
            except:
                print("Please enter a number.\nStarting over.")
                break
            initial_amounts.append(to_add)

        if len(initial_amounts) == 3:
            print(
                "Your initial amounts: {} - {} - {}".format(initial_amounts[0], initial_amounts[1], initial_amounts[2]))
            return


def input_money_to_add():
    while True:
        global money_to_add
        money_to_add = 0
        print("\nHow much money will you add?")
        try:
            money_to_add = float(input("Please enter a positive number:"))
            money_to_add = round(money_to_add, 2)
        except:
            print("Please enter a positive number.\nStarting over.")
            continue
        if money_to_add < 0:
            print("Please enter a positive number.\nStarting over.")

        if money_to_add > 0:
            print("You will add $" + str(money_to_add))
            return


def main():
    while True:
        input_percentages()
        [us_percentage, int_percentage, bond_percentage] = percentages

        # checking if percentages add up to 100
        total_percentage = 0
        for percentage in percentages:
            total_percentage += percentage
        if total_percentage < 0:
            print(
                "The percentages you provided add up to a negative number...\nThey should add up to 100.\nStarting over.")
        elif total_percentage != 100:
            print("The percentages you provided don't add up to 100.\nStarting over.")
            continue

        # getting initial total amount
        input_initial_amounts()
        [us_initial, int_initial, bonds_initial] = initial_amounts
        total_initial = us_initial + int_initial + bonds_initial

        input_money_to_add()

        # getting the final total amount
        total_final = total_initial + money_to_add

        # calculating amount needed to buy or sell
        us_to_invest = round(us_percentage * 0.01 * total_final - us_initial, 2)
        int_to_invest = round(int_percentage * 0.01 * total_final - int_initial, 2)
        bonds_to_invest = round(bond_percentage * 0.01 * total_final - bonds_initial, 2)

        if us_to_invest >= 0 and int_to_invest >= 0 and bonds_to_invest >= 0:
            print("You need to buy ${} in US stocks, ${} in international stocks, and ${} in bonds.".format(
                us_to_invest, int_to_invest, bonds_to_invest))
            break
        if us_to_invest < 0 or int_to_invest < 0 or bonds_to_invest < 0:
            print(
                "You need to buy ($amount is positive) or sell ($amount is negative) ${} in US stocks, ${} in international stocks, and ${} in bonds.".format(
                    us_to_invest, int_to_invest, bonds_to_invest))
            break


if __name__ == "__main__":
    main()
