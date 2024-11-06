class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio

def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value accumulated in the knapsack
    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item that fits
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is now full

    return total_value

# Example usage
if __name__ == "__main__":
    # Define items as (value, weight)
    items = [
        Item(60, 10),  # item with value 60 and weight 10
        Item(100, 20),  # item with value 100 and weight 20
        Item(120, 30)   # item with value 120 and weight 30
    ]
    capacity = 50  # Knapsack capacity

    max_value = fractional_knapsack(items, capacity)
    print("Maximum value in Knapsack =", max_value)
