# Get user's email address.
print("Enter your email address.")
email = input("-->").strip()

# Slice out user name.
user = email[:email.index("@")]
print(user)

# Slice out domain name.
domain = email[email.index("@"):].strip("@")
print(domain)

# Format message.
output = "Your username is {} and your domain name is {}.".format(user,domain)

# Display output message.
print(output)
