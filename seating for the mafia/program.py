import random as r
from config import PLAYERS_NICK, NUMBER_OF_ROUNDS, NUMBER_OF_TABLES


def create_players(nicks: list) -> list:
    """Создает из списка ников список игроков

    Args:
        nicks (list): Список ников

    Returns:
        list: Список игроков 
    """
    players = []
    for nick in nicks:
        player = {
            'name': nick,
            'position': [0] * 10
        }
        players.append(player)
    return players


def get_players_with_minimal_slot(pos_slot: int, players: list) -> list:
    '''
    Возращает список игроков, кто меньше всего играл на данной позиции
    '''
    players_with_min_slot = []
    min_slot = 100
    for i, player in enumerate(players):
        if min_slot > player['position'][pos_slot]:
            players_with_min_slot = [player]
            min_slot = player['position'][pos_slot]
        elif min_slot == player['position'][pos_slot]:
            players_with_min_slot.append(player)
    return players_with_min_slot


def print_players(games):
    """_summary_

    Args:
        games (_type_): _description_
    """
    for i, round in enumerate(games):
        print(f'************ Игра #{i+1} ************')
        if round['passing_players'] != []:
            print('Отыхающие')
            for player in round['passing_players']:
                print(player['name'])
        for j, table in enumerate(round['tables']):
            print(f'************ Стол #{j+1} ************')
            for k, player in enumerate(table):
                print(player['name'])


def create_games(n_rounds: int, n_tables: int, players: list) -> list:
    """Создает рассадку игроков на игры, где каждый игрок сидит минимальное количесво раз за одним слотом, 
    если игроков больше чем мест за столом, так же записывает отдыхающих

    Args:
        n_rounds (int): количесво раундов
        n_tables (int): количество столов
        players (list): игроки

    Returns:
        list: список всех игр
    """
    games = []
    
    for i in range(n_rounds):
        round = {'tables': [],
                 'passing_players': []
                 }
        number_of_passing_players = len(players) % (n_tables * 10)
        
            
        if number_of_passing_players != 0:
            start_index = (i % number_of_passing_players) * \
            number_of_passing_players
            passing_players = players[start_index: start_index + 6]
            players_for_round = [
                item for item in players if item not in passing_players]
            round['passing_players'] = passing_players
        else:
            players_for_round = players[:]
            
        for _ in range(n_tables):
            table = []
            for k in range(10):
                choosen_player = r.choice(
                    get_players_with_minimal_slot(k, players_for_round))
                choosen_player['position'][k] += 1
                table.append(choosen_player)
                players_for_round.remove(choosen_player)

            round['tables'].append(table)
        games.append(round)
    return games


if __name__ == '__main__':
    players = create_players(PLAYERS_NICK)
    games = create_games(NUMBER_OF_ROUNDS, NUMBER_OF_TABLES, players)

    print_players(games)
    