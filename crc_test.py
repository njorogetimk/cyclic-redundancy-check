from crc import main


def test_use1():
    """ binary 1010011 """

    assert main(1010011) == 11101


def test_use2():
    """ binary 1010011 repeated """

    pad = [int(num) for num in str(main(1010011))]
    binary = 1010011

    assert main(binary, pad) == 00000