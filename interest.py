principal = float(input("Enter the Principal amount: "))
rate_of_interest_per_year = float(input("Enter the Rate of Interest: "))
time_in_years = float(input("Enter the Time in Years: "))


def simple_interest(p, r, t):
    return (p * r * t) / 100


def compound_interest(principle, rate, time):
    CI = principle * (pow((1 + rate / 100), time))
    return CI


print(simple_interest(principal, rate_of_interest_per_year, time_in_years))
print(compound_interest(principal, rate_of_interest_per_year, time_in_years))
