#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, posix, time, hashlib, binascii, socket, select
import pprint


class ApiRos:
    "Routeros api"

    def __init__(self, sk):
        self.sk = sk
        self.currenttag = 0

    def login(self, username, pwd):
        for repl, attrs in self.talk(["/login"]):
            chal = binascii.unhexlify(attrs['=ret'])
        md = hashlib.md5()
        md.update(b'\x00')
        md.update(bytes(pwd, 'utf-8'))
        md.update(chal)
        self.talk(["/login", "=name=" + username,
                   "=response=00" + binascii.hexlify(md.digest()).decode('utf-8')])

    def talk(self, words):
        if self.writeSentence(words) == 0: return
        r = []
        while 1:
            i = self.readSentence();
            if len(i) == 0: continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if (j == -1):
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j + 1:]
            r.append((reply, attrs))
            if reply == '!done': return r

    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret

    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '': return r
            r.append(w)

    def writeWord(self, w):
        print("<<< " + w)
        b = bytes(w, "utf-8")
        self.writeLen(len(b))
        self.writeBytes(b)

    def readWord(self):
        ret = self.readBytes(self.readLen()).decode('utf-8')
        print(">>> " + ret)
        return ret

    def writeLen(self, l):
        if l < 0x80:
            self.writeBytes(bytes([l]))
        elif l < 0x4000:
            l |= 0x8000
            self.writeBytes(bytes([(l >> 8) & 0xff, l & 0xff]))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeBytes(bytes([(l >> 16) & 0xff, (l >> 8) & 0xff, l & 0xff]))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.writeBytes(bytes([(l >> 24) & 0xff, (l >> 16) & 0xff, (l >> 8) & 0xff, l & 0xff]))
        else:
            self.writeBytes(bytes([0xf0, (l >> 24) & 0xff, (l >> 16) & 0xff, (l >> 8) & 0xff, l & 0xff]))

    def readLen(self):
        c = self.readBytes(1)[0]
        if (c & 0x80) == 0x00:
            pass
        elif (c & 0xC0) == 0x80:
            c &= ~0xC0
            c <<= 8
            c += self.readBytes(1)[0]
        elif (c & 0xE0) == 0xC0:
            c &= ~0xE0
            c <<= 8
            c += self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
        elif (c & 0xF0) == 0xE0:
            c &= ~0xF0
            c <<= 8
            c += self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
        elif (c & 0xF8) == 0xF0:
            c = self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
            c <<= 8
            c += self.readBytes(1)[0]
        return c

    def writeBytes(self, str):
        n = 0;
        while n < len(str):
            r = self.sk.send(str[n:])
            if r == 0: raise RuntimeError("connection closed by remote end")
            n += r

    def readBytes(self, length):
        ret = b''
        while len(ret) < length:
            s = self.sk.recv(length - len(ret))
            if len(s) == 0: raise RuntimeError("connection closed by remote end")
            ret += s
        return ret


def main(host, username, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 8728))
    apiros = ApiRos(s);
    apiros.login(username, password);

    inputsentence = []

    while 1:
        r = select.select([s, sys.stdin], [], [], None)
        if s in r[0]:
            # something to read in socket, read sentence
            x = apiros.readSentence()

        if sys.stdin in r[0]:
            # read line from input and strip off newline
            l = sys.stdin.readline()
            l = l[:-1]

            # if empty line, send sentence and start with new
            # otherwise append to input sentence
            if l == '':
                apiros.writeSentence(inputsentence)
                inputsentence = []
            else:
                inputsentence.append(l)


def testConvert():
    data = ['re', '.id=*1', 'interface=wlan1', 'mac-address=B8:27:EB:0C:F8:3D', 'ap=false', 'wds=false', 'bridge=false',
            'rx-rate=72.2Mbps-20MHz/1S/SGI', 'tx-rate=36Mbps', 'packets=1123,433', 'bytes=44025,59534',
            'frames=1123,505',
            'frame-bytes=52159,64639', 'hw-frames=14108,37457', 'hw-frame-bytes=1006095,971655',
            'tx-frames-timed-out=0',
            'uptime=5h47m42s', 'last-activity=430ms', 'signal-strength=-30@24Mbps', 'signal-to-noise=69',
            'signal-strength-ch0=-36', 'signal-strength-ch1=-32',
            'strength-at-rates=-38@1Mbps 23s470ms,-30@6Mbps 26m30s200ms,-30@24Mbps 430ms,-30@HT20-4 3h27m31s160ms,-31@HT20-7 1m21s690ms',
            'tx-ccq=79', 'p-throughput=23893', 'distance=4', 'last-ip=192.168.88.231', '802.1x-port-enabled=true',
            'authentication-type=wpa2-psk', 'encryption=aes-ccm', 'group-encryption=aes-ccm',
            'management-protection=false',
            'wmm-enabled=true', 'tx-rate-set=CCK:1-11 OFDM:6-54 BW:1x SGI:1x HT:0-7', 'comment=Raspberry pi 3']
    dictionary = dict(item.split("=") for item in data if "=" in item)
    print(dictionary)

def printRegisteredDevices(host, username, password):
    pprint.pprint(getRegisteredDevices(host, username, password))


def getRegisteredDevices(host, username, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 8728))
    apiros = ApiRos(s);
    apiros.login(username, password);

    inputsentence = ['/interface/wireless/registration-table/getall']
    apiros.writeSentence(inputsentence)
    # response = apiros.readSentence()
    # print(type(response), response)
    return dict(item.split("=") for item in [item[1:] for item in apiros.readSentence()] if "=" in item)
    # return [response['comment'], response['mac-address'], response['uptime']]


if __name__ == '__main__':
    import doctest

    doctest.__test__;
    # testConvert()
    # main(sys.argv[1], sys.argv[2], sys.argv[3])
    # getRegisteredDevices(sys.argv[1], sys.argv[2], sys.argv[3])

