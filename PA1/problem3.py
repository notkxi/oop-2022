def int_to_text(N):

    ones = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '')

    twos = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')

    tens = ('', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',)

    length = len(str(N))
    N_string = str(N)

    while N != 0:

        if length == 1:
            return ones[N - 1]

        elif length == 2 and N < 20:
            return twos[N%10]

        elif length == 2 and N >= 20:
            return tens[N//10 - 1] + " " + (ones[N%10 - 1])

        elif length == 3 and 10 > int(N_string[1:]):
            return ones[int(N_string[0]) - 1] + " hundred " + ones[int(N_string[1:]) - 1]

        elif length == 3 and 20 > int(N_string[1:]) >= 10:
            return ones[int(N_string[0]) - 1] + " hundred " + twos[N%10]

        elif length == 3 and 20 <= int(N_string[1:]):
            return ones[int(N_string[0]) - 1] + " hundred " + tens[int(N_string[1:])//10 - 1] + " " + (ones[int(N_string[1:])%10 - 1])

        else:
            return "one thousand"

    return "zero"