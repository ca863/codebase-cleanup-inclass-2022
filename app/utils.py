def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":

    # nesting code in the main condition will
    # allow other scripts to cleanly import functions from this file
    # without running this code

    # this code still gets run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))



def determine_winner(user_choice, computer_choice):

    """
    This function takes two strings the computer choice and the user choice. It runs a logical test to determine the winner of the rock paper
    scissor exercise.... This function will return the winning choice of the game
    
    Param: rock_paper_scissor (string,string) like 'rock'
    
    Example: determine_winner('rock','scissors')
    
    Returns: 'rock'
    """

    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"