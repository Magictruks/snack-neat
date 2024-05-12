# importing libraries
import os
import pickle

import neat

from main_game.game import Game


def eval_genomes(genomes, config, is_training=True):
    print("New generation")
    nets = []
    ge = []
    games = []

    snake_speed = 10000

    if not is_training:
        snake_speed = 10

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)
        games.append(Game(display_screen=True, snake_speed=snake_speed))

    for idx, game in enumerate(games):
        score = game.start(nets[idx])
        # print("Score -> {}".format(score))
        ge[idx].fitness = score

def replay_genome(config_path, genome_path="winner.pkl"):
    # Load requried NEAT config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Unpickle saved winner
    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    # Convert loaded genome into required data structure
    genomes = [(1, genome)]

    # Call game with only the loaded genome
    eval_genomes(genomes, config, is_training=False)

def traning(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 50)

    print("Best fitness -> {}".format(winner))

    # Save the winner
    with open("../winner.pkl", "wb") as f:
        print("Save winner")
        pickle.dump(winner, f)


if __name__ == "__main__":
    print("Start")
    local_dir = os.path.dirname(__file__)
    print(local_dir)
    config_path = os.path.join(local_dir, "config-feedforward.txt")

    # Training
    # traning(config_path)

    # Replay
    replay_genome(config_path)
