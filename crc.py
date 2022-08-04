
def xor(a: int, b: int):
    if a == b:
        return 0
    else:
        return 1

def main(binary: int, pad = [0,0,0,0,0]) -> int:
    code = [int(num) for num in str(binary)]
    code.extend(pad)

    fb = v1 = v2 = v3 = v4 = v5 = 0

    for elem in code:
        fb = v1
        v1 = xor(v2, fb)
        v2 = v3
        v3 = xor(v4, fb)
        v4 = v5
        v5 = xor(elem, fb)
    
    return int(''.join([str(v1),str(v2),str(v3),str(v4),str(v5)]))

