# cricket_management_system.py
class Player:
    def __init__(self, name, matches, runs, wickets):
        self.name = name
        self.matches = matches
        self.runs = runs
        self.wickets = wickets

    def batting_average(self):
        return self.runs / self.matches if self.matches > 0 else 0

    def bowling_average(self):
        return self.wickets / self.matches if self.matches > 0 else 0

    def __str__(self):
        return (f"Player: {self.name}, Matches: {self.matches}, Runs: {self.runs}, "
                f"Wickets: {self.wickets}, Batting Avg: {self.batting_average():.2f}, "
                f"Bowling Avg: {self.bowling_average():.2f}")

class CricketManagementSystem:
    def __init__(self):
        self.players = []

    def add_player(self, name, matches, runs, wickets):
        player = Player(name, matches, runs, wickets)
        self.players.append(player)

    def generate_performance_report(self):
        print("Cricket Performance Report")
        print("=" * 30)
        for player in self.players:
            print(player)
        print("=" * 30)

# Example usage
if __name__ == "__main__":
    cms = CricketManagementSystem()
    cms.add_player("Virat Kohli", 250, 12000, 4)
    cms.add_player("Jasprit Bumrah", 100, 260, 150)
    cms.add_player("MS Dhoni", 350, 10500, 10)
    cms.add_player("Rohit Sharma", 200,10000,0)
    cms.add_player("Ravindra Jadeja", 150, 2560, 200)
    cms.add_player("Shikhar Dhawan", 150, 5675, 0)
    cms.add_player("Hardik Pandya", 100, 2439, 100)
    cms.add_player("KL Rahul", 100, 3000, 0)
    cms.add_player("Rishabh Pant", 50, 1000, 0)
    cms.add_player("Yuzvendra Chahal", 50, 198, 50)
    cms.add_player("Shreyas Iyer", 50, 2486, 0)
    cms.add_player("Kuldeep Yadav", 50, 100, 5)
    cms.add_player("Mohammed Shami", 100, 100, 150)
    cms.add_player("Ravichandran Ashwin", 150, 1789, 200)
    cms.add_player("Axar Patel", 50, 100, 50)
    cms.add_player("Bhuvneshwar Kumar", 150, 1309, 200)
    cms.add_player("Shubman Gill", 50, 4380, 0)
    cms.add_player("Mayank Agarwal", 50, 2850, 0)
    cms.add_player("Ishan Kishan", 50, 3470, 0)
    cms.add_player("Suryakumar Yadav", 50, 3130, 0)
    cms.add_player("Shardul Thakur", 50, 100, 50)
    cms.add_player("Deepak Chahar", 50, 100, 50)
    cms.add_player("T Natarajan", 50, 100, 50)
    cms.add_player("Washington Sundar", 50, 100, 50)
    cms.add_player("Prithvi Shaw", 50, 100, 50)
    cms.add_player("Sanju Samson", 50, 100, 50)
    cms.add_player("Shivam Dube", 50, 100, 50)
     

    cms.generate_performance_report()

