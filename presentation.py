import os, sys, random, time
random.random()

def get_sleep_time():
    min_t, max_t = float(sys.argv[1]), float(sys.argv[2])
    return random.uniform(min_t, max_t)

def show(filepath):
    AAMOUNT = 30
    print '>' * AAMOUNT + ' file: %s ' % filepath + '<' * AAMOUNT
    time.sleep(0.2)
    f = open(filepath, 'r')
    for nr, line in enumerate(f):
        t = get_sleep_time()
        time.sleep(t)
        if line.endswith('\n'):
            line = line[:-1]
        print line

def should_show(path):
    return os.path.isfile(path) and path.endswith('.py')

def do_walk(arg, dirname, names):
    for name in names:
        path = os.path.join(dirname, name)
        if should_show(path):
            show(path)
def main():
    os.path.walk(os.path.dirname(os.path.abspath(__file__)), do_walk, None)

if __name__ == '__main__':
    main()
