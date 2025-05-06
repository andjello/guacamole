import numpy as np
import matplotlib.pyplot as plt

# Triangular Membership Function
def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)

# Generate values and compute membership
a, b, c = 10, 20, 30  # Triangle points
x_vals = np.linspace(0, 40, 100)
membership_vals = [triangular_membership(x, a, b, c) for x in x_vals]

# Display specific values
print("Membership Values at selected points:")
for x in [10, 15, 20, 25, 30]:
    print(f"μ({x}) = {triangular_membership(x, a, b, c)}")

# Plot the membership function
plt.plot(x_vals, membership_vals, label="Triangular MF")
plt.title("Triangular Membership Function")
plt.xlabel("x")
plt.ylabel("Membership Value")
plt.grid(True)
plt.legend()
plt.show()
