
# Parcel Collection and Delivery System
# Activity 4 - BTEC Computing Unit 4

print("======================================")
print("   PARCEL COLLECTION SYSTEM")
print("======================================")

# Function to collect a positive whole number
def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")

# Function to collect a positive weight
def get_positive_weight(message):
    while True:
        try:
            weight = float(input(message))
            if weight > 0:
                return weight
            else:
                print("Please enter a weight greater than zero.")
        except ValueError:
            print("Please enter a valid weight.")

# Function for yes/no questions
def get_yes_no(message):
    while True:
        answer = input(message).lower()

        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Please enter yes or no.")

# Customer details
print("\nCUSTOMER DETAILS")

customer_name = input("Enter customer name: ")
customer_address = input("Enter customer address: ")
customer_phone = input("Enter customer phone number: ")

# Number of parcels
print("\nPARCEL DETAILS")

while True:
    number_of_parcels = get_positive_integer(
        "Enter number of parcels (1-6): "
    )

    if number_of_parcels >= 1 and number_of_parcels <= 6:
        break
    else:
        print("You can only collect between 1 and 6 parcels.")

# Store parcel information
parcels = []
total_cost = 0

# Process each parcel
for parcel_number in range(1, number_of_parcels + 1):

    print("\n------------------------------")
    print("PARCEL", parcel_number)
    print("------------------------------")

    height = get_positive_integer("Enter height in cm: ")
    length = get_positive_integer("Enter length in cm: ")
    width = get_positive_integer("Enter width in cm: ")
    weight = get_positive_weight("Enter weight in kg: ")

    # Calculate parcel size
    parcel_size = height + length + width

    # Check whether parcel can be collected
    if parcel_size > 450 or weight > 30:

        print("Parcel cannot be collected.")
        print("Parcel exceeds the maximum size or weight.")

        parcels.append({
            "number": parcel_number,
            "size": parcel_size,
            "weight": weight,
            "cost": 0,
            "signature": 0,
            "tracking": 0,
            "accepted": False
        })

        continue

    # Calculate price based on parcel size
    if parcel_size < 95:
        size_price = 5
    elif parcel_size <= 150:
        size_price = 20
    else:
        size_price = 30

    # Calculate price based on parcel weight
    if weight <= 2:
        weight_price = 5
    elif weight <= 15:
        weight_price = 20
    else:
        weight_price = 30

    # Apply the highest price
    parcel_cost = max(size_price, weight_price)

    # Optional signature service
    if get_yes_no("Add signature on delivery? (yes/no): "):
        signature_cost = 2
    else:
        signature_cost = 0

    # Optional tracking service
    if get_yes_no("Add parcel tracking? (yes/no): "):
        tracking_cost = 5
    else:
        tracking_cost = 0

    # Calculate total cost for this parcel
    parcel_total = parcel_cost + signature_cost + tracking_cost

    # Add parcel cost to collection total
    total_cost = total_cost + parcel_total

    # Store parcel information
    parcels.append({
        "number": parcel_number,
        "size": parcel_size,
        "weight": weight,
        "cost": parcel_cost,
        "signature": signature_cost,
        "tracking": tracking_cost,
        "accepted": True
    })

# Display collection receipt
print("\n======================================")
print("       COLLECTION RECEIPT")
print("======================================")

print("Customer name:", customer_name)
print("Customer address:", customer_address)
print("Customer phone:", customer_phone)

print("\nNumber of parcels:", number_of_parcels)

print("\nITEMISED BILL")
print("--------------------------------------")

# Display each parcel
for parcel in parcels:

    print("\nParcel number:", parcel["number"])

    if parcel["accepted"]:

        print("Parcel size:", parcel["size"], "cm")
        print("Parcel weight:", parcel["weight"], "kg")

        print("Parcel cost: £{:.2f}".format(parcel["cost"]))
        print("Signature: £{:.2f}".format(parcel["signature"]))
        print("Tracking: £{:.2f}".format(parcel["tracking"]))

        parcel_total = (
            parcel["cost"]
            + parcel["signature"]
            + parcel["tracking"]
        )

        print("Parcel total: £{:.2f}".format(parcel_total))

    else:
        print("REJECTED - Parcel cannot be collected.")

# Final receipt total
print("\n--------------------------------------")
print("TOTAL COLLECTION COST: £{:.2f}".format(total_cost))
print("--------------------------------------")

print("\nThank you for using our service!")
print("======================================")

