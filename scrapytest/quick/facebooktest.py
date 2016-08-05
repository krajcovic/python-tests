#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import os


def get_object(graph, what):
    post = graph.get_object(what)
    return post


def get_friends(graph):
    # Get all of the authenticated user's friends
    return graph.get_connections(id='me', connection_name='friends')


def get_feeds(graph):
    return graph.get_connections(id='me', connection_name='feed')


def get_comments(graph):
    return graph.get_connections(id='me', connection_name='comments')


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    graph = facebook.GraphAPI(access_token=os.getenv('FACEBOOK_USER_TOKEN'),
                              version='2.6')
    facebookUser = get_object(graph, 'me')
    print(facebookUser)
    # print(graph.get_object(id=facebookUser.get('id')))

    facebookFriends = get_friends(graph)
    print(facebookFriends)

    graph.put_object(parent_object='me', connection_name='feed',
                     message='This is testing message from python')

    attachment = {
        'name': 'Link name',
        'link': 'https://www.example.com/',
        'caption': 'Check out this example',
        'description': 'This is a longer description of the attachment',
        'picture': 'https://www.example.com/thumbnail.jpg'
    }

    graph.put_wall_post(message='Check this out...', attachment=attachment)

    print(get_feeds(graph))

    print(get_comments(graph))
