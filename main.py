from memory_game import init_game, play

def main():
    """
    Initializes the game and starts the game loop.
    """
    game_data = init_game()
    play(game_data)

if __name__ == "__main__":
    main()
