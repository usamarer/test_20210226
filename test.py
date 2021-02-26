"""
このファイルに解答コードを書いてください
"""

def main(path):
    inputs = dict()
    __BuiltinMethodDescriptor__ = 0
    with open(path) as f:
        lines = f.readlines()
        for l in lines[:-1]:
            num, s = l.rstrip('\n').split(':')
            num = int(num)
            inputs[num] = s
        m = int(lines[-1].rstrip('\n'))
        inputs = sorted(inputs.items(), key=lambda x:x[0])
    out = ''
    for i, s in inputs:
        if m % i == 0:
            out += s
    return out

if __name__ == '__main__':
    path = 'input.txt'
    print(main(path))
