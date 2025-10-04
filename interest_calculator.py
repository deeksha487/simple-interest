# interest_calculator.py

def calculate_simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

def calculate_compound_interest(P, R, T):
    CI = P * ((1 + R / 100) ** T) - P
    return CI

# Example usage
P = 10000
R = 5
T = 3

simple_interest = calculate_simple_interest(P, R, T)
compound_interest = calculate_compound_interest(P, R, T)

print(f"Simple Interest: ₹{simple_interest}")
print(f"Compound Interest: ₹{compound_interest}")
