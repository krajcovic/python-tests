#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import json
import os
import pprint
import sys
import time

from slacker import Slacker

from mikrotik.rosapi_slacker_publish import mikrotik_api as mapi
# import rosapi


def test_convert():
    """

    :return:
    """
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


def publist_to_slacker(slack_token, channel, text):
    """

    :param slack_token:
    :param channel:
    :param text:
    :return:
    """
    slack = Slacker(slack_token)
    slack.chat.post_message(channel, text)


def publish_registered_device(host, username, password, slack_token):
    """

    :param host:
    :param username:
    :param password:
    :param slack_token:
    :return:
    """
    response = get_registered_devices(host, username, password)
    # pprint.pprint(response)
    with open('wifi_log.txt', 'a') as f:
        # json.dump(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), f)
        response.append(["timestamp", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')])
        json.dump(response, f)

    for [key, value] in response:
        if key == 'mac-address':
            # print("{} = {}".format(key, value))
            # publist_to_slacker('#general', value)
            mac_address = value
        if key == 'comment':
            # print("{} = {}".format(key, value))
            publist_to_slacker('#general', "{} -> {}".format(slack_token, mac_address, value))

            # publist_to_slacker('#general', "{} {} {}".format(response['comment'], response['mac-address'], response['uptime']))


def print_registered_devices(host, username, password):
    """

    :param host:
    :param username:
    :param password:
    :return:
    """
    pprint.pprint(get_registered_devices(host, username, password))


def get_registered_devices(host, username, password):
    """

    :param host:
    :param username:
    :param password:
    :return:
    """
    apiros = mapi.get_apiros(host, 8728, username, password)

    inputsentence = ['/interface/wireless/registration-table/print']
    apiros.writeSentence(inputsentence)
    response = apiros.readSentence()
    # print("******************")
    # pprint(response)
    # print("******************")
    return [item.split("=") for item in [item[1:] for item in response] if "=" in item]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    publish_registered_device(sys.argv[1], sys.argv[2], sys.argv[3], os.environ.get('SLACK_TOKEN'))
