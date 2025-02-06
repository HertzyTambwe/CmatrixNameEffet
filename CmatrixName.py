import curses
import random
import time

def matrix_effect(stdscr, name="Hertzy"):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(30)
    height, width = stdscr.getmaxyx()
    columns = [0] * width
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%^&*()"

    while True:
        stdscr.clear()
        for i in range(width):
            if columns[i] >= height or random.random() < 0.95:
                columns[i] = 0
            char = random.choice(chars)
            if random.random() > 0.98:  # Insère ton nom parfois
                char = name[random.randint(0, len(name) - 1)]
            stdscr.addch(columns[i], i, char, curses.color_pair(1))
            columns[i] += 1
        
        stdscr.refresh()
        time.sleep(0.05)
        if stdscr.getch() == 27:  # Quitter avec Échap
            break

def main():
    curses.wrapper(lambda stdscr: setup_curses(stdscr, "Hertzy"))

def setup_curses(stdscr, name):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    matrix_effect(stdscr, name)

if __name__ == "__main__":
    main()