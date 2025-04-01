class CricketMatch:
    def __init__(self, team_name):
        self.team_name = team_name
        self.total_runs = 87
        self.total_wickets = 2
        self.total_overs = 48.5
        self.players_scores = {}

    def add_player(self, player_name):
        """Add a player to the team."""
        self.players_scores[player_name] = {
            "runs": 0,
            "balls_faced": 0,
            "wickets_taken": 0
        }
        
    def update_player_score(self, player_name, runs, balls_faced, wickets_taken):
        """Update score for a player."""
        if player_name in self.players_scores:
            self.players_scores[player_name]["runs"] += runs
            self.players_scores[player_name]["balls_faced"] += balls_faced
            self.players_scores[player_name]["wickets_taken"] += wickets_taken
            self.total_runs += runs
            self.total_wickets += wickets_taken
        else:
            print(f"Player {player_name} not found!")

    def update_overs(self, overs):
        """Update overs for the team."""
        self.total_overs += overs

    def calculate_batting_average(self, player_name):
        """Calculate the batting average for a player."""
        if player_name in self.players_scores:
            runs = self.players_scores[player_name]["runs"]
            balls = self.players_scores[player_name]["balls_faced"]
            if balls > 0:
                strike_rate = (runs / balls) * 100
            else:
                strike_rate = 0
            return runs, strike_rate
        else:
            return 0

    def calculate_bowling_average(self, player_name):
        """Calculate the bowling average for a player."""
        if player_name in self.players_scores:
            runs_conceded = self.players_scores[player_name]["runs"]
            wickets_taken = self.players_scores[player_name]["wickets_taken"]
            if wickets_taken > 0:
                return runs_conceded / wickets_taken
            else:
                return 0

    def display_team_report(self):
        """Display the overall score and performance report for the team."""
        print(f"Team: {self.team_name}")
        print(f"Total Runs: {self.total_runs}")
        print(f"Total Wickets: {self.total_wickets}")
        print(f"Total Overs: {self.total_overs:.2f}")
        for player_name, stats in self.players_scores.items():
            runs, strike_rate = self.calculate_batting_average(player_name)
            bowling_avg = self.calculate_bowling_average(player_name)
            print(f"\nPlayer: {player_name}")
            print(f"Runs: {runs}, Strike Rate: {strike_rate:.2f}")
            print(f"Wickets Taken: {stats['wickets_taken']}, Bowling Average: {bowling_avg:.2f}")

        #EXAMPLE OF CRICKET MATCH SIMULATOR

# Create two teams
team1 = CricketMatch("Team A")
team2 = CricketMatch("Team B")

# Add players to the teams
team1.add_player("Player 1")
team1.add_player("Player 2")
team2.add_player("Player 3")
team2.add_player("Player 4")
team1.add_player("Player 5")
team1.add_player("Player 6")
team2.add_player("Player 7")
team2.add_player("Player 8")
team1.add_player("Player 9")
team1.add_player("Player 10")
team2.add_player("Player 11")
team2.add_player("Player 12")
team1.add_player("Player 13")
team1.add_player("Player 14")
team2.add_player("Player 15")
team2.add_player("Player 16")
team1.add_player("Player 17")
team1.add_player("Player 18")
team2.add_player("Player 19")
team2.add_player("Player 20")
team1.add_player("Player 21")
team1.add_player("Player 22")


# Update scores for players in the teams
team1.update_player_score("Player 1", runs=45, balls_faced=30, wickets_taken=1)
team1.update_player_score("Player 2", runs=35, balls_faced=25, wickets_taken=0)
team2.update_player_score("Player 3", runs=60, balls_faced=40, wickets_taken=2)
team2.update_player_score("Player 4", runs=25, balls_faced=20, wickets_taken=1)
team1.update_player_score("Player 5", runs=20, balls_faced=15, wickets_taken=0)
team1.update_player_score("Player 6", runs=30, balls_faced=20, wickets_taken=1)
team2.update_player_score("Player 7", runs=40, balls_faced=30, wickets_taken=0)
team2.update_player_score("Player 8", runs=50, balls_faced=35, wickets_taken=1)
team1.update_player_score("Player 9", runs=15, balls_faced=10, wickets_taken=0)
team1.update_player_score("Player 10", runs=10, balls_faced=5, wickets_taken=0)
team2.update_player_score("Player 11", runs=30, balls_faced=20, wickets_taken=1)
team2.update_player_score("Player 12", runs=20, balls_faced=15, wickets_taken=0)
team1.update_player_score("Player 13", runs=25, balls_faced=15, wickets_taken=1)
team1.update_player_score("Player 14", runs=30, balls_faced=20, wickets_taken=0)
team2.update_player_score("Player 15", runs=40, balls_faced=25, wickets_taken=1)
# Update overs for the teams
team1.update_overs(48.5)
team2.update_overs(49.2)
# Display the team report
team1.display_team_report()
team2.display_team_report()
 
