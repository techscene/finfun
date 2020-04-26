class Interest:

    @staticmethod
    def compound(value, interest, periods):
        if interest > 1:
            compound_factor = 1 + interest / 100
        else:
            compound_factor = 1 + interest
        return value * compound_factor**periods

    @staticmethod
    def savings_plan(periodized_value, interest, periods): # todo annual interest but monthly savings....!
        total_payout = 0
        if isinstance(periodized_value, int):
            for index, n in enumerate(range(periods)):
                total_payout += Interest.compound(periodized_value, interest, index + 1)

        return total_payout


if __name__ == "__main__":
    value = 1000 * 12
    interest_rate = 5
    years = 30
    print(Interest.savings_plan(value, interest_rate, years))
