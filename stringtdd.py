class StringCalculator:

    def add(self, s):
        if len(s) == 0:
            return 0

        list_of_num = s.split(',')
        sum_of_num = 0
        neagtive = []
        for i in list_of_num:
            if i.isalpha():
                sum_of_num += ord(i) - 96
            elif int(i) > 1000:
                continue
            elif int(i) < 0:
                neagtive.append(i)
            else:
                sum_of_num += int(i)

        if len(neagtive) > 0:
            raise Exception("Negatives not allowed.", neagtive)

        return sum_of_num
