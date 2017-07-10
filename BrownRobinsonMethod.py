import numpy as np

def main():
    pay_matrix = np.array([
        [6, 1, 4],
        [2, 4, 2],
        [4, 3, 5]
    ])
    rezult = brown_robinson(pay_matrix, print_iterations=True)
    print(
        '\nGame price: W =', rezult['game_price'],
        '\nPlayer A optimal mixed strategy: P =', rezult['player_a_optimal_mixed_strategy'],
        '\nPlayer B optimal mixed strategy B: Q =', rezult['player_b_optimal_mixed_strategy']
    )

def brown_robinson(pay_matrix, iterations=20, start_strategy=0, print_iterations=False):
    round_step = 2
    player_a_current_strategy_number = start_strategy
    player_b_current_strategy_number = pay_matrix[player_a_current_strategy_number].argmin()
    player_a_mixed_strategy = np.array(pay_matrix[player_a_current_strategy_number])
    player_b_mixed_strategy = np.array(pay_matrix[:, player_b_current_strategy_number])
    player_a_strategy_choose_frequency = np.zeros(len(pay_matrix))
    player_b_strategy_choose_frequency = np.zeros(len(pay_matrix[0]))  
    
    for i in range(1, iterations + 1):
        player_a_strategy_choose_frequency[player_a_current_strategy_number] += 1
        player_b_strategy_choose_frequency[player_b_current_strategy_number] += 1
        lower_game_price = min(player_a_mixed_strategy) / i
        upper_game_price = max(player_b_mixed_strategy) / i
        if print_iterations:
            print(
                i,
                player_a_current_strategy_number + 1, player_a_mixed_strategy,
                player_b_current_strategy_number + 1, player_b_mixed_strategy,
                round(lower_game_price, round_step), round(upper_game_price, round_step),
                round((lower_game_price + upper_game_price) / 2, round_step),
                sep=' | '
            )
        player_a_current_strategy_number = player_b_mixed_strategy.argmax()
        player_a_mixed_strategy += pay_matrix[player_a_current_strategy_number]
        player_b_current_strategy_number = player_a_mixed_strategy.argmin()
        player_b_mixed_strategy += pay_matrix[:, player_b_current_strategy_number]
        
    return {
        'game_price': (lower_game_price + upper_game_price) / 2,
        'player_a_optimal_mixed_strategy': player_a_strategy_choose_frequency / iterations,
        'player_b_optimal_mixed_strategy': player_b_strategy_choose_frequency / iterations
    }

if __name__ == '__main__':
    main()