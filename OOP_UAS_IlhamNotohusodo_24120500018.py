
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Player(Person):
    def __init__(self, name, age, position, jersey_number):
        super().__init__(name, age)
        self.position = position
        self.jersey_number = jersey_number

class Coach(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role  # "Head Coach" or "Assistant Coach"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.head_coach = None
        self.assistant_coach = None

    def set_head_coach(self, coach):
        if coach.role == "Head Coach":
            self.head_coach = coach

    def set_assistant_coach(self, coach):
        if coach.role == "Assistant Coach":
            self.assistant_coach = coach

    def add_player(self, player):
        if len(self.players) < 15:
            self.players.append(player)

    def display_team(self):
        print(f"Team: {self.name}")
        print(f"Head Coach: {self.head_coach.name}")
        print(f"Assistant Coach: {self.assistant_coach.name}")
        print("Players:")
        for player in self.players:
            print(f" - #{player.jersey_number} {player.name} ({player.position})")

######i nstansiasi
team = Team("FC Cakrawala Muda")
team.set_head_coach(Coach("Pak Budi", 45, "Head Coach"))
team.set_assistant_coach(Coach("Pak Andi", 40, "Assistant Coach"))

###### add 15 players
for i in range(1, 16):
    team.add_player(Player(f"Pemain {i}", 20+i%3, "Midfielder", i))

team.display_team()
