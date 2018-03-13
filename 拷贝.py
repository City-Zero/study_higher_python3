#coidng=utf-8
import copy
def fuzhi():
    a = [1,['s','z']]
    b = a
    print('a=%s,id(a)=%d,id(a[i])={%s}'%(a,id(a),[id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}'%(b,id(b),[id(i) for i in b]))
    a[0] = 2
    a[1].append('x')
    print('do some change on a...')
    print('a=%s,id(a)=%d,id(a[i])={%s}' % (a, id(a), [id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}' % (b, id(b), [id(i) for i in b]))

def ShallowCopy():
    a = [1,['s','z']]
    b = copy.copy(a)
    print('a=%s,id(a)=%d,id(a[i])={%s}' % (a, id(a), [id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}' % (b, id(b), [id(i) for i in b]))
    a[0] = 2
    a[1].append('x')
    print('do some change on a...')
    print('a=%s,id(a)=%d,id(a[i])={%s}' % (a, id(a), [id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}' % (b, id(b), [id(i) for i in b]))

def DeepCopy():
    a = [1, ['s', 'z']]
    b = copy.deepcopy(a)
    print('a=%s,id(a)=%d,id(a[i])={%s}' % (a, id(a), [id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}' % (b, id(b), [id(i) for i in b]))
    a[0] = 2
    a[1].append('x')
    print('do some change on a...')
    print('a=%s,id(a)=%d,id(a[i])={%s}' % (a, id(a), [id(i) for i in a]))
    print('b=%s,id(b)=%d,id(b[i])={%s}' % (b, id(b), [id(i) for i in b]))

if __name__ == '__main__':
    DeepCopy()