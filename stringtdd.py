class StringCalculator:

    def add(self, s):
        if len(s) == 0:
            return 0

        x = s.split(',')
        ans = 0
        if len(x) == 1:
            ans = int(x[0])
        elif len(x) == 2:
            ans = int(x[0]) + int(x[1])

        return ans
