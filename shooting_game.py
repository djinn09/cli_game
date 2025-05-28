import random
from typing import List, Optional

# Animal Class
class Animal:
    """
    Represents an animal in the game.

    Attributes:
        points_value (int): The number of points awarded for shooting this animal.
    """
    def __init__(self, points_value: int):
        """
        Initializes an Animal instance.

        Args:
            points_value: The points value for the animal.
        """
        self.points_value: int = points_value

    def appear(self) -> None:
        """Prints a message indicating the animal has appeared."""
        print(f"A {self.__class__.__name__} appears!")

    def get_shot(self) -> int:
        """
        Handles the animal being shot.

        Returns:
            The points value of the animal.
        """
        print(f"The {self.__class__.__name__} is hit!")
        return self.points_value

class Deer(Animal):
    """Represents a Deer, a type of Animal."""
    def __init__(self):
        """Initializes a Deer instance with a predefined points value."""
        super().__init__(points_value=10)

    def appear(self) -> None:
        """Prints a message specific to a Deer appearing."""
        # Specific appearance behavior for Deer
        super().appear()
        print("The deer looks around cautiously.")

class Bear(Animal):
    """Represents a Bear, a type of Animal."""
    def __init__(self):
        """Initializes a Bear instance with a predefined points value."""
        super().__init__(points_value=20)

    def appear(self) -> None:
        """Prints a message specific to a Bear appearing."""
        # Specific appearance behavior for Bear
        super().appear()
        print("The bear growls menacingly.")


# Gun class
class Gun:
    """Represents a gun in the game."""
    def fire(self) -> bool:
        """
        Fires the gun.

        This method should be implemented by subclasses to define specific firing behavior
        and accuracy.

        Raises:
            NotImplementedError: If the subclass does not implement this method.

        Returns:
            True if the shot hits, False otherwise.
        """
        raise NotImplementedError("Subclass must implement this method")

class Rifle(Gun):
    """Represents a Rifle, a type of Gun with high accuracy."""
    def fire(self) -> bool:
        """
        Fires the rifle with an 80% chance of hitting.

        Returns:
            True if the shot hits, False otherwise.
        """
        # Assume a higher accuracy for the rifle
        return random.random() < 0.8  # 80% chance to hit

class Shotgun(Gun):
    """Represents a Shotgun, a type of Gun with lower accuracy."""
    def fire(self) -> bool:
        """
        Fires the shotgun with a 50% chance of hitting.

        Returns:
            True if the shot hits, False otherwise.
        """
        # Assume a lower accuracy for the shotgun but higher damage
        return random.random() < 0.5  # 50% chance to hit



class Game:
    """
    Manages the overall game logic and flow.

    Attributes:
        player (Player): The player participating in the game.
        scoreboard (ScoreBoard): The scoreboard tracking the player's score.
        animals (List[Animal]): A list of available animals in the game.
        guns (List[Gun]): A list of available guns in the game.
        is_game_running (bool): A flag indicating if the game is currently active.
    """
    def __init__(self):
        """Initializes a Game instance, setting up the player, scoreboard, animals, and guns."""
        self.player: Player = Player()
        self.scoreboard: ScoreBoard = ScoreBoard() # Scoreboard is initialized but not used actively in the current game logic
        self.animals: List[Animal] = [Deer(), Bear()]  # Example list of animals
        self.guns: List[Gun] = [Rifle(), Shotgun()]  # Example list of guns
        self.is_game_running: bool = False

    def start_game(self) -> None:
        """Starts the game, including gun selection and the main game loop."""
        self.is_game_running = True
        print("Welcome to the Shooting Game!")
        gun: Optional[Gun] = self.choose_gun_from_list()
        # Loop until a valid gun is chosen
        while gun is None:
          gun = self.choose_gun_from_list()
        self.player.choose_gun(gun)
        self.game_loop()

    def choose_gun_from_list(self) -> Optional[Gun]:
        """
        Allows the player to choose a gun from the available list.

        Returns:
            The selected Gun object, or None if the choice was invalid.
        """
        # Display gun choices and return the selected gun
        print("Choose your gun:")
        for index, gun_option in enumerate(self.guns, start=1):
            print(f"{index}. {gun_option.__class__.__name__}")
        try:
          choice: int = int(input("Enter your choice: "))
          # Adjust choice to be zero-indexed for list access
          if 1 <= choice <= len(self.guns):
              return self.guns[choice - 1]
          else:
              print("Invalid Choice for Gun. Please select a valid number.")
              return None
        except ValueError: # Handle cases where input is not an integer
          print("Invalid input. Please enter a number.")
          return None
        except Exception as e: # Catch any other unexpected errors
          print(f"An unexpected error occurred: {e}")
          return None

    def game_loop(self) -> None:
        """Runs the main game loop, allowing the player to shoot or end the game."""
        while self.is_game_running:
            self.display_options()
            choice: str = input("Enter your action: ")
            if choice == '1':
                # Player chooses to shoot
                selected_animal: Animal = self.random_animal()
                selected_animal.appear() # Make the animal appear before shooting
                self.player.shoot(selected_animal)
            elif choice == '2':
                # Player chooses to end the game
                self.end_game()
            else:
                print("Invalid choice. Please try again.")

    def display_options(self) -> None:
        """Displays the available actions to the player."""
        print("\n1. Shoot an animal")
        print("2. End game")

    def random_animal(self) -> Animal:
        """
        Randomly selects an animal from the available list.

        Returns:
            A randomly selected Animal object.
        """
        # Randomly select an animal
        return random.choice(self.animals)

    def end_game(self) -> None:
        """Ends the game and displays the final score."""
        self.is_game_running = False
        self.display_score() # Display player's points from Player class
        print("Game Over. Thank you for playing!")

    def display_score(self) -> None:
        """Displays the player's final score."""
        # This method currently displays the score from the Player object.
        # The ScoreBoard class has more detailed score tracking capabilities
        # that could be integrated here if desired.
        print(f"Final Score: {self.player.points}")



# Player class
class Player:
    """
    Represents the player in the game.

    Attributes:
        selected_gun (Optional[Gun]): The gun currently selected by the player.
        points (int): The player's current score.
    """
    def __init__(self):
        """Initializes a Player instance with no gun selected and zero points."""
        self.selected_gun: Optional[Gun] = None
        self.points: int = 0

    def choose_gun(self, gun: Gun) -> None:
        """
        Allows the player to select a gun.

        Args:
            gun: The Gun object to be selected.
        """
        self.selected_gun = gun
        print(f"You have selected {self.selected_gun.__class__.__name__}")

    def shoot(self, target: Animal) -> None:
        """
        Allows the player to shoot at a target animal.

        Args:
            target: The Animal object to be shot at.
        """
        if self.selected_gun is None:
            print("You need to select a gun first!")
            return

        # The fire() method of the selected gun determines if the shot is a hit
        hit: bool = self.selected_gun.fire()
        if hit:
            # The get_shot() method of the animal returns the points for hitting it
            points_earned: int = target.get_shot()
            self.add_points(points_earned)
            print(f"Hit! You earned {points_earned} points.")
        else:
            print("Missed! Better luck next time.")

    def add_points(self, points: int) -> None:
        """
        Adds points to the player's score.

        Args:
            points: The number of points to add.
        """
        self.points += points
        print(f"Total Points: {self.points}")



class ScoreBoard:
    """
    Tracks the game's score.

    Attributes:
        total_score (int): The cumulative score.
        score_history (List[int]): A list of individual scores achieved.
    """
    def __init__(self):
        """Initializes a ScoreBoard instance with a total score of zero and an empty score history."""
        self.total_score: int = 0
        self.score_history: List[int] = []

    def update_score(self, points: int) -> None:
        """
        Updates the scoreboard with new points.

        Args:
            points: The points to add to the score.
        """
        self.total_score += points
        self.score_history.append(points)
        print(f"Score updated: +{points} points")

    def display_score(self) -> None:
        """Displays the current total score and the history of scores."""
        print(f"Current Score: {self.total_score}")
        print("Score History:")
        for score in self.score_history:
            print(f"  +{score} points")

    def display_final_score(self) -> None:
        """Displays the final total score."""
        print(f"Final Score: {self.total_score}")


def main():
    """Runs the main game sequence."""
    game: Game = Game()
    game.start_game()

if __name__ == "__main__":
    main()