from finfun.Interest import Interest


class SavingsPlan:

    def __init__(self, payment_per_month, interest_rate_pa, years_to_maturity):
        self.payment_per_month = payment_per_month
        self.interest_rate_pa = interest_rate_pa if interest_rate_pa < 1 else interest_rate_pa / 100
        self.years_to_maturity = years_to_maturity

    def describe(self):
        interest = self.interest_rate_pa
        months = self.years_to_maturity * 12
        payout = self.get_payout()
        sum_payments = self.payment_per_month * months
        sum_payments_label = 'Sum payments:'
        interest_label = 'Interest p.a.:'
        months_label = 'Months:'
        payout_label = 'Payout:'
        gain = payout - sum_payments

        print('{:25} {:10.2f}'.format(sum_payments_label, sum_payments))
        print('{:25} {:10.2f}'.format(interest_label, interest))
        print('{:25} {:10.2f}'.format(months_label, months))
        print('{:25} {:10.2f}'.format(payout_label, payout))
        print('{:25} {:10.2f}'.format('Pre-tax gain', gain))
        print('{:25} {:10.2f}'.format('Capital gains tax (25%)', gain * 0.25))
        print('{:25} {:10.2f}'.format('After-tax gain', gain * 0.75))

    def get_payout(self):
        total_payout = 0
        monthly_interest = self.interest_rate_pa / 12
        months = self.years_to_maturity * 12
        for index, n in enumerate(range(months)):
            total_payout += Interest.compound(self.payment_per_month, monthly_interest, index + 1)
        return total_payout


if __name__ == "__main__":
    value = 500
    interest_rate = 4
    years = 30
    savings_plan = SavingsPlan(value, interest_rate, years)
    print(savings_plan.describe())
