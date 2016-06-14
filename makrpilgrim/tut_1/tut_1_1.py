#!/bin/pytho3

try:
    import chardet
except ImportError:
    print("ImportError by chardet")
    chardet = None

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def appromate_size(size, a_kilobyte_is_1024_bytes=True):
    """
    Convert a file size to human-readable form.

    Keyword arguments:
    :param size: file size in bytes
    :param a_kilobyte_is_1024_bytes: if True(default), use multipes of 1024 if False, use multiples of 1000
    :return: string
    """
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

def test():
    print('test')

if __name__ == '__main__':
    test()
    print(appromate_size(1000000000000, False))
    print(appromate_size(1000000000000))
