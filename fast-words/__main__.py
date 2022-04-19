import argparse
import sys

from os import path
from . import game

def main():
    parser = argparse.ArgumentParser(prog='fast-words', description='Make some words as fast as you can!')
    m_game = game.Game()
    m_game.play()

if __name__ == "__main__":
    main()