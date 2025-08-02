# AI Travel Designer Agent
def travel_plan(destination):
    if destination.lower() == "paris":
        return "Visit Eiffel Tower, Louvre Museum, and enjoy croissants at a local café."
    elif destination.lower() == "tokyo":
        return "Explore Shibuya Crossing, Tokyo Skytree, and try sushi at a local restaurant."
    else:
        return "Choose a destination and explore its culture, food, and landmarks!"

# Test the function
user_input = input("Enter your travel destination (e.g., Paris, Tokyo): ")
print(travel_plan(user_input))