# Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
# You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
shared_destinations = our_routes.intersection(competitor_routes)

print("Both airlines fly to ", shared_destinations)

print("Our unique destinations are ", our_routes.difference(competitor_routes))
print("their unique destinations are ", competitor_routes.difference(our_routes))

neither_flights = (our_routes.union(competitor_routes)).difference(shared_destinations)
print(neither_flights)

# routes = {"LAX", "JFK", "CDG", "DXB"}
# for destination in routes:
#     print(f"We fly to ", (routes))



# Duplicate Entries Cleanup

# You are given a list of customer IDs, some of which are duplicated. 
# Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customer_ids = sorted(set(customer_ids))

print(unique_customer_ids)

