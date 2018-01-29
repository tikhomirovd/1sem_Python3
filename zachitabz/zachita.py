import pickle

name = '2016.db'
value = 'а'
p2='poisk2.bin'

fn='qwert1.bin'
fn2='copy.bin'
s='sort.bin'

with open(fn, 'rb') as f:
    k = pickle.load(f)
    for i in range(k):
        a = pickle.load(f)
        print('{:2d}'.format(a['n']), '%-15s' % a['f'],
              '{:4d}{:4d}{:4d}'.format(a['w'], a['ni'], a['l']))
    print('--------------------------------------------------------')
    print()


def poisk1(fn):
    count = 0
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        with open(p2, 'wb') as p:
            pickle.dump(count, p)
            for i in range(k):
                a = pickle.load(f)
                if value in a['f'] or value.upper() in a['f']:
                    print('{:2d}'.format(a['n']), '%-15s' % a['f'],
                          '{:4d}{:4d}{:4d}'.format(a['w'], a['ni'], a['l']))


poisk1(fn)
