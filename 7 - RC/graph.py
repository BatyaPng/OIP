import matplotlib.pyplot as plt
import random as rnd


def crd():
    with open('data.txt', 'w') as f:
        for i in range(100):
            f.write(str(rnd.randrange(0, 100)) + '\n')


def graph():
    with open('data.txt') as f:
        data = []
        try:
            while True:
                data.append(int(f.readline()))
        except (IndexError, ValueError):
            pass
        finally:
            plt.plot(data)
            plt.show()


graph()
