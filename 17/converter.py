def group_converter(group, face_value):
    # digit --> The values for digits in units and hundreds place
    digit = {
        '0': '', '1': ' One', '2': ' Two', '3': ' Three', '4': ' Four',
        '5': ' Five', '6': ' Six', '7': ' Seven', '8': ' Eight', '9': ' Nine'
    }
    # digit --> The values for digits in tens place with an exception for 10-19 in English language
    tens = {
        '0': '',
        '1': {'0': ' Ten', '1': ' Eleven', '2': ' Tewlve', '3': ' Thirteen', '4': ' Fourteen', '5': ' Fifteen',
              '6': ' Sixteen', '7': ' Seventeen', '8': ' Eighteen', '9': ' Nineteen'},
        '2': ' Twenty', '3': ' Thirty', '4': ' Forty',
        '5': ' Fifty', '6': ' Sixty', '7': ' Seventy', '8': ' Eighty', '9': ' Ninety', }

    # words corresponding to thousand separator

    unit = {
        0: '', 1: ' Thousand', 2: ' Million', 3: ' Billion', 4: ' Trillion',
        5: ' Quadrillion', 6: ' Quintillion', 7: ' Sextillion', 8: ' Septillion', 9: ' Octillion',
        10: ' Nonillion', 11: ' Decillion', 12: ' Undecillion', 13: ' Duodecillion', 14: ' Tredecillion',
        15: ' Quatttuor-decillion', 16: ' Quindecillion', 17: ' Duodecillion', 18: ' Tredecillion',
        19: ' Octodecillion', 20: ' Novemdecillion', 21: ' Vigintillion',
    }

    # names the hundreds digit of each triplet

    def hundreds_namer(num_letter):
        if num_letter != '0':
            # use <digit> hundred if digit isnt 0
            return '{} Hundred'.format(digit[num_letter])
        else:
            return ''

    # names the tenth digit of each triplet

    def tens_namer(num_letter):
        if num_letter != '0':
            return '{}'.format(tens[num_letter])
        else:
            return ''

    # names the unit digit of each triplet

    def units_namer(num_letter):
        return '{}'.format(digit[num_letter])

    if (len(group) == 3):
        if int(group) != 0:
            # prevent returning face value (thousands name) if it is 000 eg:-1000000=1 million not 1 millon thousand

            if (group[1] != '1'):  # special case not for ?10 to ?19

                if group[1] != '0' or group[2] != '0':  # for triplets with tens and units place defined

                    if face_value == 0:  # for first triplet

                        word = hundreds_namer(group[0]) + ' and' + tens_namer(group[1]) + units_namer(group[2]) + unit[
                            face_value]

                    else:  # for rest excpet the first triplet
                        word = hundreds_namer(group[0]) + tens_namer(group[1]) + units_namer(group[2]) + unit[
                            face_value]

                else:
                    word = hundreds_namer(group[0]) + unit[face_value]

            else:  # special case for ?10 to ?19

                if face_value == 0:  # for first triplet
                    word = hundreds_namer(group[0]) + ' and' + tens[group[1]][group[2]] + unit[face_value]

                else:  # for rest excpet the first triplet
                    word = hundreds_namer(group[0]) + tens[group[1]][group[2]] + unit[face_value]

        else:
            word = ''

    elif (len(group) == 2):

        if (group[0] != '1'):
            word = tens_namer(group[0]) + units_namer(group[1]) + unit[face_value]

        else:
            word = tens[group[0]][group[1]] + unit[face_value]

    else:
        word = digit[group] + unit[face_value]

    return word


def converter(number):
    if number == 0:
        return " Zero "
    elif number >= 999:
        # String formatted with a thousand separator
        str_number = '{:,}'.format(number)

        # grouping the numbers and reversing so that it goes increasing i.e thousands,millions,bilion..
        groups = str_number.split(',')
        groups.reverse()

        word_list = [group_converter(groups[x], x) for x in range((len(groups) - 1), -1, -1)]
        return ''.join(word_list)
    else:
        # for the numbers between 1 and 999
        word = group_converter(str(number), 0)
        return word


if __name__ == "__main__":
    import sys

    try:
        num = int(sys.argv[1])
        print(converter(num))

    except ValueError as e:
        print("Please enter a valid integer number.")

    except IndexError as e:
        print("Enter a valid integer you want to convert to words.\n Eg :- python {} 101".format(sys.argv[0]))
