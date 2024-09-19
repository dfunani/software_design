class GameManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.score = 0
            cls.level = 1
            cls.is_muted = False
        return cls.__instance

    def increase_score(self, points):
        self.score += points

    def next_level(self):
        self.level += 1

    def toggle_mute(self):
        self.is_muted = not self.is_muted


print("=" * 10 + " Game Manager " + "=" * 10)

print("=" * 10 + " First Game " + "=" * 10)
game_manager1 = GameManager()
print("Score Incremented By 10.")
game_manager1.increase_score(10)
print(f"Score 1: {game_manager1.score}")  # Output: 10
print(f"game Manager 1: Muted == {game_manager1.is_muted}")  # Output: 10

print("=" * 10 + " Second Game " + "=" * 10)
game_manager2 = GameManager()
print("Score Incremented By 10.")
game_manager2.increase_score(10)
print("Game Muted.")
game_manager2.toggle_mute()
print(f"Score 2: {game_manager2.score}")  # Output: 10
print(f"game Manager 2: Muted == {game_manager1.is_muted}")  # Output: 10

print("=" * 10 + " Game Over " + "=" * 10)
print(
    f"Game Manager Instance 1 is Game Manager Instance 2 == {game_manager1.score is game_manager2.score}"
)
print(
    f"Game Manager 1 is Muted == {game_manager1.is_muted} and Game Manager 2 is Muted == {game_manager1.is_muted}"
)
print(
    f"Score 1 ({game_manager1.score}) == Score 2 ({game_manager2.score}) ==  {game_manager1.score == game_manager2.score}"
)
