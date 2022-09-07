class StringCalculator:

    def add(self, s):
        if len(s) == 0:
            return 0

        list_of_num = s.split(',')
        sum_of_num = 0
        for i in list_of_num:
            if i.isalpha():
                sum_of_num += ord(i) - 96
            elif int(i) < 0:
                raise Exception("Negatives not allowed.", i)
            else:
                sum_of_num += int(i)

        return sum_of_num
