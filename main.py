import logging

logging.basicConfig(filename='example.log')

def log():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


if __name__ == '__main__':
    log()
