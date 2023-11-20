import random

# Animal Class 

class Animal:
    def __init__(self, points_value):
        self.points_value = points_value

    def appear(self):
        print(f"A {self.__class__.__name__} appears!")

    def get_shot(self):
        print(f"The {self.__class__.__name__} is hit!")
        return self.points_value

class Deer(Animal):
    def __init__(self):
        super().__init__(points_value=10)

    def appear(self):
        # Specific appearance behavior for Deer
        super().appear()
        print("The deer looks around cautiously.")

class Bear(Animal):
    def __init__(self):
        super().__init__(points_value=20)

    def appear(self):
        # Specific appearance behavior for Bear
        super().appear()
        print("The bear growls menacingly.")


# Gun class
class Gun:
    def fire(self):
        raise NotImplementedError("Subclass must implement this method")

class Rifle(Gun):
    def fire(self):
        # Assume a higher accuracy for the rifle
        return random.random() < 0.8  # 80% chance to hit

class Shotgun(Gun):
    def fire(self):
        # Assume a lower accuracy for the shotgun but higher damage
        return random.random() < 0.5  # 50% chance to hit



class Game:
    def __init__(self):
        self.player = Player()
        self.scoreboard = ScoreBoard()
        self.animals = [Deer(), Bear()]  # Example list of animals
        self.guns = [Rifle(), Shotgun()]  # Example list of guns
        self.is_game_running = False

    def start_game(self):
        self.is_game_running = True
        print("Welcome to the Shooting Game!")
        gun = self.choose_gun_from_list()
        while gun is None:
          gun = self.choose_gun_from_list()
        self.player.choose_gun(gun)
        self.game_loop()

    def choose_gun_from_list(self):
        # Display gun choices and return the selected gun
        print("Choose your gun:")
        for index, gun in enumerate(self.guns, start=1):
            print(f"{index}. {gun.__class__.__name__}")
        try:
          choice = int(input("Enter your choice: "))
          return self.guns[choice - 1]
        except Exception as e:
          print("Invalid Choice for Gun")
        

    def game_loop(self):
        while self.is_game_running:
            self.display_options()
            choice = input("Enter your action: ")
            if choice == '1':
                self.player.shoot(self.random_animal())
            elif choice == '2':
                self.end_game()
            else:
                print("Invalid choice. Please try again.")

    def display_options(self):
        print("\n1. Shoot an animal")
        print("2. End game")

    def random_animal(self):
        # Randomly select an animal
        import random
        return random.choice(self.animals)

    def end_game(self):
        self.is_game_running = False
        self.display_score()
        print("Game Over. Thank you for playing!")

    def display_score(self):
        print(f"Final Score: {self.player.points}")



# Player class
class Player:
    def __init__(self):
        self.selected_gun = None
        self.points = 0

    def choose_gun(self, gun):
        self.selected_gun = gun
        print(f"You have selected {self.selected_gun.__class__.__name__}")

    def shoot(self, target):
        if self.selected_gun is None:
            print("You need to select a gun first!")
            return

        hit = self.selected_gun.fire()  # Assuming fire() returns True/False for hit/miss
        if hit:
            points_earned = target.get_shot()  # Assuming get_shot() returns points for the animal
            self.add_points(points_earned)
            print(f"Hit! You earned {points_earned} points.")
        else:
            print("Missed! Better luck next time.")

    def add_points(self, points):
        self.points += points
        print(f"Total Points: {self.points}")



class ScoreBoard:
    def __init__(self):
        self.total_score = 0
        self.score_history = []

    def update_score(self, points):
        self.total_score += points
        self.score_history.append(points)
        print(f"Score updated: +{points} points")

    def display_score(self):
        print(f"Current Score: {self.total_score}")
        print("Score History:")
        for score in self.score_history:
            print(f"  +{score} points")

    def display_final_score(self):
        print(f"Final Score: {self.total_score}")


if __name__ == "__main__":
    game = Game()
    game.start_game()