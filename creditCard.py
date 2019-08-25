# Takes user input and turns it into a list - I used this section to check if my program was working as intended
def split (creditcardnumber):
    return list(creditcardnumber)
creditcardnumber = input('Please input your credit card number: ')

# print(split(creditcardnumber))

my_sum = 0
my_sum2 = 0
totalone = 0
totaltwo = 0
totalthree = 0

for counter, number in enumerate(creditcardnumber,1):
    number = int(number)
    if counter % 2 == 0:
        my_sum = (number * 2)
        if my_sum > 9:
            my_sum2 = my_sum - 9
            totalone += my_sum2
        else: 
            totaltwo += my_sum
    else:
        totalthree += number
    calculate_credit_card_number_check_digit = (totalone + totaltwo + totalthree)


def validate_credit_card_number_check_digit():
    if calculate_credit_card_number_check_digit % 10 == 0:
        print("valid card number entered")
    else: 
        print("invalid card number entered")

validate_credit_card_number_check_digit()