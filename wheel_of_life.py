
import matplotlib.pyplot as plt

def get_user_input(category):
    while True:
        try:
            rating = float(input(f"Rate your {category} (0 to 10): "))
            if 0 <= rating <= 10:
                return rating
            else:
                print("Please enter a value between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def create_wheel_of_life():
    categories = ['Body', 'Mind', 'Soul', 'Mission', 'Money', 'Growth', 'Friends', 'Family', 'Romance']
    ratings = []

    for category in categories:
        rating = get_user_input(category)
        ratings.append(rating)

    # Create a pie chart
    plt.pie(ratings, labels=categories, autopct='%1.1f%%', startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    # Add a title
    plt.title('Wheel of Life')

    # Display the pie chart
    plt.show()

# Run the script
create_wheel_of_life()
