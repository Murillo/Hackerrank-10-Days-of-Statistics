# Set data
x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

# Get possibilities
first_possibility = x["Red"] * y["Red"] * z["Black"]
second_possibility = x["Red"] * y["Black"] * z["Red"]
third_possibility = x["Black"] * y["Red"] * z["Red"]

# Get probability
print(first_possibility + second_possibility + third_possibility)
