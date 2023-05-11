"""
Pretty Print
"""

from pprint import pprint

colors = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
data = {'gun': 1197, 'bit': 'bob97@example.org', 'nice': 'https://warner-ferguson.net/privacy.htm', 'foot': 'GBRSvRPiAMwWfpEVWYOq', 'police': 'james74@example.com', 'ability': {'indeed': 'aaronlarson@example.org', 'hope': 'AebIPyAATmycHEdGtuJW', 'before': 291,}, 'together': 'VwtvNSBfNHHKFTsFNlDb'}

pprint(colors, width=20)
pprint(data, width=30)
