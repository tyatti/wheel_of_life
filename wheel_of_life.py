
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


    plt.pie(ratings, labels=categories, autopct='%1.1f%%', startangle=90)

   
    plt.axis('equal')

   
    plt.title('Wheel of Life')

    
    plt.show()


create_wheel_of_life()
