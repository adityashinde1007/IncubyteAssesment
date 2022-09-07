class StringCalculator:

    def add(self, s):
        if len(s) == 0:
            return 0

        x = s.split(',')
        ans = 0
        for i in x:
            if i.isalpha():
                ans += ord(i) - 96
            else:
                ans += int(i)

        return ans
