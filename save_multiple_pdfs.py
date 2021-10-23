import pyautogui as pg
from time import sleep

def main():
    num_tabs = int(input('how many tabs? '))
    for i in range(5, 0, -1):
        print(f'starts in {i}...')
        sleep(1)

    for i in range(num_tabs):
        pg.hotkey('ctrl', 's')
        sleep(3)
        pg.keyDown('enter')
        sleep(2)
        pg.hotkey('ctrl', 'w')
        sleep(0.5)

    print('completed')

if __name__ == "__main__":
    main()