# project-
project management system
rom datetime import datetime

# Class to represent a Player

class Player:
    def __init__(self, player_id, name, role, age, batting_style, bowling_style):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.age = age
        self.batting_style = batting_style
        self.bowling_style = bowling_style
        self.runs_scored = 0
        self.wickets_taken = 0

    def update_stats(self, runs, wickets):
        self.runs_scored += runs
        self.wickets_taken += wickets

    def __str__(self):
        return f"ID: {self.player_id}, Name: {self.name}, Role: {self.role}, Runs: {self.runs_scored}, Wickets: {self.wickets_taken}"

# Class to represent a Team

class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        return [str(player) for player in self.players]

    def __str__(self):
        return f"Team: {self.team_name}, Players: {', '.join([player.name for player in self.players])}"

# Class to represent a Match

class Match:
    def __init__(self, match_id, team1, team2, match_date, venue):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.match_date = match_date
        self.venue = venue
        self.score_team1 = 0
        self.score_team2 = 0

    def set_score(self, team1_score, team2_score):
        self.score_team1 = team1_score
        self.score_team2 = team2_score

    def __str__(self):
        return f"Match ID: {self.match_id}, {self.team1.team_name} vs {self.team2.team_name} on {self.match_date} at {self.venue}. Final Score: {self.team1.team_name} {self.score_team1} - {self.team2.team_name} {self.score_team2}"

# Class to manage all matches

class MatchScheduling:
    def __init__(self):
        self.matches = []

    def schedule_match(self, match):
        if match.match_date < datetime.now():
            print("Error: Cannot schedule match in the past.")
            return
        self.matches.append(match)
        print(f"Match scheduled: {match}")

    def show_schedule(self):
        if not self.matches:
            print("No matches scheduled.")
        for match in self.matches:
            print(match)

# Class to represent a Tournament

class Tournament:
    def __init__(self, tournament_name, teams):
        self.tournament_name = tournament_name
        self.teams = teams
        self.matches = []

    def schedule_tournament_matches(self):
        print(f"\nScheduling matches for the {self.tournament_name} Tournament...")
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                match = Match(f"{self.teams[i].team_name} vs {self.teams[j].team_name}", self.teams[i], self.teams[j], datetime.now(), "Stadium A")
                self.matches.append(match)
                print(f"Match scheduled: {match}")

    def show_tournament_schedule(self):
        if not self.matches:
            print("No matches scheduled for this tournament.")
        for match in self.matches:
            print(match)

# Class to manage Players

class PlayerManagement:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        if player.player_id in self.players:
            print(f"Error: Player with ID {player.player_id} already exists.")
        else:
            self.players[player.player_id] = player
            print(f"Player {player.name} added successfully.")

    def update_player(self, player_id, runs=0, wickets=0):
        if player_id in self.players:
            self.players[player_id].update_stats(runs, wickets)
            print(f"Updated stats for {self.players[player_id].name}: Runs: {runs}, Wickets: {wickets}")
        else:
            print(f"Error: Player with ID {player_id} not found.")

    def delete_player(self, player_id):
        if player_id in self.players:
            deleted_player = self.players.pop(player_id)
            print(f"Player {deleted_player.name} deleted successfully.")
        else:
            print(f"Error: Player with ID {player_id} not found.")

    def list_players(self):
        if not self.players:
            print("No players found.")
        else:
            for player in self.players.values():
                print(player)

# Main driver code to demonstrate the CMS functionality

def main():
    # Initialize classes
    player_manager = PlayerManagement()
    team1 = Team(1, "India")
    team2 = Team(2, "Australia")
    team3 = Team(3, "England")

    # Create players

    player1 = Player(101, "Virat Kohli", "Batsman", 35, "Right-Handed", "N/A")
    player2 = Player(102, "Jasprit Bumrah", "Bowler", 29, "Right-Handed", "Right-arm fast")
    player3 = Player(103, "Steve Smith", "Batsman", 30, "Right-Handed", "N/A")
    player4 = Player(104, "Pat Cummins", "Bowler", 30, "Right-Handed", "Right-arm fast")
    player5 = Player(105, "Joe Root", "Batsman", 30, "Right-Handed", "N/A")
    player6 = Player(106, "Jofra Archer", "Bowler", 26, "Right-Handed", "Right-arm fast")
    player7 = Player(107, "Rohit Sharma", "Batsman", 34, "Right-Handed", "N/A")
    player8 = Player(108, "Ravindra Jadeja", "All-Rounder", 32, "Left-Handed", "Left-arm spin")
    player9 = Player(109, "David Warner", "Batsman", 34, "Left-Handed", "N/A")
    player10 = Player(110, "Mitchell Starc", "Bowler", 31, "Left-Handed", "Left-arm fast")
    player11 = Player(111, "Ben Stokes", "All-Rounder", 29, "Left-Handed", "Right-arm fast")
    player12 = Player(112, "Kane Williamson", "Batsman", 30, "Right-Handed", "N/A")
    player13 = Player(113, "Trent Boult", "Bowler", 31, "Right-Handed", "Left-arm fast")
    player14 = Player(114, "Quinton de Kock", "Batsman", 28, "Left-Handed", "N/A")
    player15 = Player(115, "Kagiso Rabada", "Bowler", 26, "Right-Handed", "Right-arm fast")
    player16 = Player(116, "Aaron Finch", "Batsman", 34, "Right-Handed", "N/A")
    player17 = Player(117, "Glenn Maxwell", "All-Rounder", 32, "Right-Handed", "Right-arm off-spin")
    player18 = Player(118, "Jason Holder", "All-Rounder", 29, "Right-Handed", "Right-arm fast")
    player19 = Player(119, "Shakib Al Hasan", "All-Rounder", 34, "Left-Handed", "Left-arm spin")
    player20 = Player(120, "Rashid Khan", "Bowler", 22, "Right-Handed", "Leg-spin")
    player21 = Player(121, "Mohammad Nabi", "All-Rounder", 36, "Right-Handed", "Off-spin")
    player22 = Player(122, "Mujeeb Ur Rahman", "Bowler", 20, "Right-Handed", "Off-spin")
    player23 = Player(123, "Kusal Perera", "Batsman", 31, "Left-Handed", "N/A")
    player24 = Player(124, "Lasith Malinga", "Bowler", 37, "Right-Handed", "Right-arm fast")
    player25 = Player(125, "Kusal Mendis", "Batsman", 28, "Right-Handed", "N/A")
    player26 = Player(126, "Angelo Mathews", "All-Rounder", 34, "Right-Handed", "Right-arm fast")
    player27 = Player(127, "Dimuth Karunaratne", "Batsman", 33, "Left-Handed", "N/A")
    player28 = Player(128, "Dhananjaya de Silva", "All-Rounder", 29, "Right-Handed", "Right-arm off-spin")
    player29 = Player(129, "Suranga Lakmal", "Bowler", 34, "Right-Handed", "Right-arm fast")
    player30 = Player(130, "Lahiru Kumara", "Bowler", 24, "Right-Handed", "Right-arm fast")
    player31 = Player(131, "Kusal Perera", "Batsman", 31, "Left-Handed", "N/A")
    player32 = Player(132, "Lasith Malinga", "Bowler", 37, "Right-Handed", "Right-arm fast")
    player33 = Player(133, "Kusal Mendis", "Batsman", 28, "Right-Handed", "N/A")
    



    # Add players to teams

    team1.add_player(player1)
    team1.add_player(player2)
    team1.add_player(player5)
    team1.add_player(player6)
    team1.add_player(player7)
    team1.add_player(player8)
    team1.add_player(player9)
    team1.add_player(player10)
    team1.add_player(player11)
    team1.add_player(player12)
    team1.add_player(player13)
    team2.add_player(player3)
    team2.add_player(player4)
    team2.add_player(player14)
    team2.add_player(player15)
    team2.add_player(player16)
    team2.add_player(player17)
    team2.add_player(player18)
    team2.add_player(player19)
    team2.add_player(player20)
    team2.add_player(player21)
    team2.add_player(player22)
    team3.add_player(player23)
    team3.add_player(player24)
    team3.add_player(player25)
    team3.add_player(player26)
    team3.add_player(player27)
    team3.add_player(player28)
    team3.add_player(player29)
    team3.add_player(player30)
    team3.add_player(player31)
    team3.add_player(player32)
    team3.add_player(player33)


    # Manage players

    player_manager.add_player(player1)
    player_manager.add_player(player2)
    player_manager.add_player(player3)
    player_manager.add_player(player4)
    player_manager.add_player(player5)
    player_manager.add_player(player6)
    player_manager.add_player(player7)
    player_manager.add_player(player8)
    player_manager.add_player(player9)
    player_manager.add_player(player10)
    player_manager.add_player(player11)
    player_manager.add_player(player12)
    player_manager.add_player(player13)
    player_manager.add_player(player14)
    player_manager.add_player(player15)
    player_manager.add_player(player16)
    player_manager.add_player(player17)
    player_manager.add_player(player18)
    player_manager.add_player(player19)
    player_manager.add_player(player20)
    player_manager.add_player(player21)
    player_manager.add_player(player22)
    player_manager.add_player(player23)
    player_manager.add_player(player24)
    player_manager.add_player(player25)
    player_manager.add_player(player26)
    player_manager.add_player(player27)
    player_manager.add_player(player28)
    player_manager.add_player(player29)
    player_manager.add_player(player30)
    player_manager.add_player(player31)
    player_manager.add_player(player32)
    player_manager.add_player(player33)


    # Display all players

    print("\nList of Players:")
    player_manager.list_players()

    # Update player stats

    player_manager.update_player(101, runs=5000, wickets=0)

    # Schedule matches

    match_scheduler = MatchScheduling()
    match1 = Match("1", team1, team2, datetime(2025, 4, 15), "Wankhede Stadium")
    match_scheduler.schedule_match(match1)
    match2 = Match("2", team2, team3, datetime(2025, 4, 20), "MCG")
    match_scheduler.schedule_match(match2)
    match3 = Match("3", team1, team3, datetime(2025, 4, 25), "Lords")
    match_scheduler.schedule_match(match3)
    match4= Match("4", team1, team2, datetime(2025, 4, 30), "SCG")
    match_scheduler.schedule_match(match4)
    match5 = Match("5", team2, team3, datetime(2025, 5, 5), "The Oval")
    match_scheduler.schedule_match(match5)
    match6 = Match("6", team1, team3, datetime(2025, 5, 10), "Old Trafford")
    match_scheduler.schedule_match(match6)
    match7 = Match("7", team1, team2, datetime(2025, 5, 15), "Edgbaston")
    match_scheduler.schedule_match(match7)
    match8 = Match("8", team2, team3, datetime(2025, 5, 20), "Headingley")
    match_scheduler.schedule_match(match8)
    match9 = Match("9", team1, team3, datetime(2025, 5, 25), "Trent Bridge")
    match_scheduler.schedule_match(match9)
    match10 = Match("10", team1, team2, datetime(2025, 5, 30), "Rose Bowl")
    match_scheduler.schedule_match(match)
    match11 = Match("11", team2, team3, datetime(2025, 6, 5), "Cardiff")
    match_scheduler.schedule_match(match)
    match12 = Match("12", team1, team3, datetime(2025, 6, 10), "County Ground")
    match_scheduler.schedule_match(match)
    match13 = Match("13", team1, team2, datetime(2025, 6, 15), "Bristol")
    match_scheduler.schedule_match(match)
    match14 = Match("14", team2, team3, datetime(2025, 6, 20), "Riverside Ground")
    match_scheduler.schedule_match(match)
    match15 = Match("15", team1, team3, datetime(2025, 6, 25), "County Ground")
    match_scheduler.schedule_match(match)
    # Display scheduled matches

    print("\nMatch Schedule:")
    match_scheduler.show_schedule()

    # Tournament Management

    tournament = Tournament("ICC World Cup 2025", [team1, team2, team3])
    tournament.schedule_tournament_matches()

    # Display tournament schedule

    print("\nTournament Schedule:")
    tournament.show_tournament_schedule()

if __name__ == "__main__":
    main()
    

