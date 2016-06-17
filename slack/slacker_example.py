#!/usr/bin/env python3

import os
from slacker import Slacker

slack = Slacker(os.environ.get('SLACK_TOKEN'))
slack.chat.post_message('#general', 'Toto je testovaci zprava z slacker_example.py')
