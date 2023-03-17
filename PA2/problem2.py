# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Feb 21, 2022
# Programming Homework: 02
#
# File: problem2.py

def customer_dictionary(balfilename):
    """ Takes one argument, balfilename, a file, and returns a dictionary named,
    cdictionary, with banking information"""

    # opening file for reading.
    balance_file = open(balfilename, "r")

    # create empty dictionary to store values.
    cdictionary = {}

    # iterate through each line in the opened file.
    for line in balance_file:

        # split each line into its respective values, save it in variable.
        bank_info = line.split()
        ssn = bank_info[0]
        account_num = bank_info[1]
        balance = bank_info[2]
        # create dictionary with previously defined variables.
        cdictionary[account_num] = [ssn, float(balance)]

    # close the file.
    balance_file.close()

    # return the new dictionary.
    return cdictionary

def update_customer_dictionary(cdictionary, transfilename):
    """ Takes two arguments, cdictionary, a dictionary, and transfilename,
    the name of a file. It returns cdictionary, a dictionary, with updated banking
    information"""

    # open transfile for reading.
    trans_file = open(transfilename, "r")

    # add 0's to list in dictionary so appropriate values can be added.
    for line in cdictionary:
        cdictionary[line].extend([0, 0, 0, 0])

    # iterate through each line in the opened file.
    for lines in trans_file:

        # split each line into its respective values, save it in variable.
        trans_info = lines.split()
        account_num = trans_info[0]
        transactions = float(trans_info[1])

        # create if statements to determine if the transaction is a withdraw or deposit, and
        # the max withdraw and the max deposit. Add them to correct dictionary position.
        if transactions > 0:
            cdictionary[account_num][2] = cdictionary[account_num][2] + transactions
        if transactions < 0:
            cdictionary[account_num][3] = cdictionary[account_num][3] + abs(transactions)
        if cdictionary[account_num][4] < transactions:
            cdictionary[account_num][4] = transactions
        if cdictionary[account_num][5] < abs(transactions) and transactions < 0:
            cdictionary[account_num][5] = abs(transactions)

    # close the file
    trans_file.close()

    # return the dictionary.
    return cdictionary

def new_balance_files(cdictionary, summfilename, newbalfilename):
    """Take three arguments, cdictionary, a dictionary, summfilename, a filename, and newbalfilename,
     a file name. Writes banking information to two files."""

    # open files for writing.
    trans_summ = open(summfilename, "w")
    new_balance = open(newbalfilename, "w")

    # print header to new file.
    trans_summ.write("ACCT#   SSN            PREVBAL  DEPOSITS  WITHDRAWALS   MAXDEP  MAXWDRAW  INTEREST   PENALTY   NEW BAL\n")
    trans_summ.write("-" * 102 + "\n")

    # iterate through the dictionary.
    for account in cdictionary:

        # create variables to use for later.
        max_dep = cdictionary[account][4]
        max_draw = cdictionary[account][5]
        interest = 0
        penalty = 0
        new_bal = round(cdictionary[account][1] + cdictionary[account][2] - cdictionary[account][3], 2)

        # check if new_bal is greater than 3000. If it is then add on .02 interest.
        if new_bal > 3000:
            interest = (new_bal * .02) // 0.01 / 100

        # check if the final_balance is under 100. If it is apply the penalty.
        if new_bal < 100:
            penalty = 10

        # set new_bal to the final value. Adding in interest and penalty charges.
        new_bal = round(new_bal - penalty + interest, 2)

        # output the values in the correct format and then write it to the file.
        trans_summ.write("{:<8s}{:<12}{:>10.2f}{:>10.2f}{:>13.2f}{:>9.2f}{:>10.2f}{:>10.2f}{:>10.2f}{:>10.2f}\n".format(account, cdictionary[account][0],
        cdictionary[account][1], cdictionary[account][2], cdictionary[account][3], max_dep, max_draw, interest, penalty, new_bal))
        new_balance.write("{:<10}{:>8}{:>14.2f}\n".format(cdictionary[account][0], account, new_bal))

    # close the files.
    trans_summ.close()
    new_balance.close()

if __name__ == "__main__":
    print("Running the problem2 module (Bank Transactions problem)\n")
    cdict = customer_dictionary("balance.dat")
    update_customer_dictionary(cdict, "transactions.dat")
    new_balance_files(cdict, "transsummary.dat", "newbalance.dat")
    print("Updated bank balance data appears in the files transsummary.dat and newbalance.dat")
    print("Goodbye!\n")