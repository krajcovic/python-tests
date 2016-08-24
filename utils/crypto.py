#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import string
import pprint

import collections


def hex2base64(hexString):
    """
    Return base64 string from hexString
    :param hexString:
    :return:

    >>> hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    """

    return base64.encodebytes(bytearray.fromhex(hexString))[:-1]


def fixedXOR(in1, in2):
    """
    Takes 2 equal length buffers and produces their xor combination
    :param in1:
    :param in2:
    :return:

    >>> fixedXOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    '746865206b696420646f6e277420706c6179'
    """

    if len(in1) != len(in2):
        raise ValueError('Different length of input parameters')

    ba1 = bytearray.fromhex(in1)
    ba2 = bytearray.fromhex(in2)

    result = ''
    for i in range(len(ba1)):
        # print(ba1[i], ba2[i], format(ba1[i] ^ ba2[i], '02x'))
        result += format(ba1[i] ^ ba2[i], '02x')

    return result

def singleByteXORDecrytp(encodedHexString, xorChar):
    """
    Hex encoded string has xorded with single character. get result
    :param encodedHexString:
    :return:
    """

    encodedByteArray = bytearray.fromhex(encodedHexString)

    result = ''
    for i in range(len(encodedByteArray)):
        result += format(encodedByteArray[i] ^ ord(xorChar), '02x')
    return result


def getFrequencyMap():
    return {
        'a': 8.167,
        'b': 1.492,
        'c': 2.278,
        'd': 4.253,
        'e': 12.702,
        'f': 2.228,
        'g': 2.015,
        'h': 6.094,
        'i': 6.966,
        'j': 0.153,
        'k': 0.772,
        'l': 4.025,
        'm': 2.406,
        'n': 6.749,
        'o': 7.507,
        'p': 1.929,
        'q': 0.095,
        'r': 5.987,
        's': 6.327,
        't': 9.056,
        'u': 2.758,
        'v': 0.978,
        'w': 2.361,
        'x': 0.150,
        'y': 1.974,
        'z': 0.074,
    }


def countFrequency(string):
    fm = getFrequencyMap()
    score = 0

    for key, value in collections.Counter(string.lower()).items():
        if key in fm:
            frequency = fm.get(key)
            # print(frequency, value)
            score += frequency * value

    return score


# Scenario 1
# print(hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

# Scenario 2
# print(fixedXOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))

def executeSingleXor(encodedHexString, xorChar):
    try:
        hex = singleByteXORDecrytp(encodedHexString, xorChar=xorChar)
        string = bytearray.fromhex(hex).decode('utf-8')
        if string.isprintable() and len(string) > 0:
            print(xorChar, round(countFrequency(string), 2), string)
    except UnicodeDecodeError as e:
        pass
        # print(e)


# Scenario 3
# testedHexString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# # testedHexString = '4554414f494e20534852444c55'
#
# for i in range(ord('a'), ord('z') + 1):
#     executeSingleXor(testedHexString, chr(i))
#
# for i in range(ord('A'), ord('Z') + 1):
#     executeSingleXor(testedHexString, chr(i))

# Sceanrio 4
with open('4.txt', 'r') as testedFile:
    testedHexString = testedFile.read().replace('\n', '')

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(collections.Counter(bytearray.fromhex(testedHexString)))
    # print(type(testedHexString))

    # wordList = testedHexString.split('0x71')

    ba = bytearray.fromhex(testedHexString)
    print(ba)
    start = 0
    end = len(ba)
    while start < end:
        index = ba.find(0x72, start, end)

        if index == -1:
             print('Index not found')
             break

        testedHexString = ''.join('{:02x}'.format(x) for x in ba[start:index])
        print('Searched text:', testedHexString)

        for i in range(ord('a'), ord('z') + 1):
            executeSingleXor(testedHexString, chr(i))

        for i in range(ord('A'), ord('Z') + 1):
            executeSingleXor(testedHexString, chr(i))

        start = index+1
