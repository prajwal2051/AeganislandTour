def create_itinerary(H, C, customers):
    # Initialize the itinerary with all by-sea hops
    itinerary = ['by-sea'] * H
    airborne_count = 0  # Count of airborne hops
    # Iterate through each customer's preferences
    for customer in customers:
        for hop, transport in customer:
            if itinerary[hop] == transport:
                continue  # The preference is already satisfied
            elif itinerary[hop] == 'by-sea' and transport == 'airborne':
                # Assign airborne transport if it reduces airborne hops
                itinerary[hop] = 'airborne'
                airborne_count += 1
            elif itinerary[hop] == 'airborne' and transport == 'by-sea':
                # If the customer wants by-sea but the hop is already airborne, we cannot satisfy them
                # return "NO ITINERARY"
                itinerary[hop] = 'by-sea'

    # Check if all customers are satisfied (at least one hop matching their preference)
    for customer in customers:
        satisfied = False
        for hop, transport in customer:
            if itinerary[hop] == transport:
                satisfied = True
                break
        if not satisfied:
            return "NO ITINERARY"
        else:
            return itinerary


if __name__ == "__main__":
    H = int(input())
    C = int(input())

    customers = []
    for _ in range(C):
        customer_prefs = input().split(", ")
        customer_hops = [(int(hop), transport) for hop, transport in [pref.split() for pref in customer_prefs]]
        customers.append(customer_hops)

    itinerary = create_itinerary(H, C, customers)

    if itinerary == "NO ITINERARY":
        print("NO ITINERARY")
    else:
        # Print the final itinerary
        output = ', '.join([f"{hop} {transport}" for hop, transport in enumerate(itinerary)])
        print(output) 