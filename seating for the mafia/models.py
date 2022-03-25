class Player:
    def __init__(self, nick: str) -> None:
        self.nick = nick
        # [{'player': Player, count : int }, {} ... ]
        self.player_communication = []

    def get_nick(self) -> str:
        return self.nick

    def set_nick(self, nick: str) -> None:
        self.nick = nick

    def add_player_communication(self, player: Player) -> None:
        p = next(
            (item for item in self.player_communication if item['player'] is player), False)
        if not p:
            p['count'] += 1
        else:
            p = {'player': player,
                 'count': 0}
            self.player_communication.append(p)


class Table:
    def __init__(self) -> None:
        self.participants = []
        self.resting_players = []

    def get_participants(self):
        return self.seating_areas

    def add_participants(self, player: Player) -> None:
        self.seating_areas.append(player)

    def get_resting_players(self):
        return self.resting_players

    def add_resting_players(self, player: Player) -> None:
        self.resting_players.append(player)
