import random
from pandas import DataFrame

from lote.templates.template_1 import Template1


class CardGenerator():

  def __init__(self, cards):
    self.cards = cards

  def generate_set(self, lucky_pos = None):
    card_set = []

    # get 14 cards randomly from the cards list
    i = 0
    while i <= 14:
      card = random.choice(self.cards)
      if(card not in card_set):
        card_set.append(card)
        i += 1

    # shuffle the cards
    random.shuffle(card_set)

    lucky_card = random.choice(card_set)
    card_set.remove(lucky_card)
    print(f'[+] Carta de suerte: {lucky_card}')

    '''
      [0, 0], [1, 0], [2, 0], [3, 0],
      [0, 1], [1, 1], [2, 1], [3, 1],
      [0, 2], [1, 2], [2, 2], [3, 2],
      [0, 3], [1, 3], [2, 3], [3, 3]
    '''
    lucky_card_pos = [
      [[0, 0], [3, 0]], #horizontal_top
      [[0, 3], [3, 3]], #horizontal_bottom,
      [[0, 0], [0, 3]], #vertical_left,
      [[3, 0], [3, 3]], #vertical_right,
      [[3, 0], [0, 3]], #diagonal_top_left,
      [[0, 0], [3, 3]], #diagonal_top_right,
      [[1, 1], [2, 1]], #inner_top,
      [[1, 2], [2, 2]], #inner_bottom,
      [[1, 1], [1, 2]], #inner_left,
      [[2, 1], [2, 2]], #inner_right,
      [[1, 1], [2, 2]], #inner_diagonal_right
      [[2, 1], [1, 2]], #inner_diagonal_left
    ]

    if lucky_pos == None or lucky_pos >= len(lucky_card_pos):
      lucky_pos = random.choice(lucky_card_pos) # [[2, 1], [1, 2]], #diagonal_top_right,
    else:
      lucky_pos = lucky_card_pos[lucky_pos]

    x = 0
    y = 0
    i = 0

    while i <= 13:
      card = card_set[i]

      if(card == lucky_card):
        continue

      if((x == lucky_pos[0][0] and y == lucky_pos[0][1]) or (x == lucky_pos[1][0] and y == lucky_pos[1][1])):
        #i += 1
        x += 1

        if(x == 4):
          x = 0
          y += 1
        continue 

      card_set[i] = {
        'x': Template1.coord2slot(x, y)[0],
        'y': Template1.coord2slot(x, y)[1],
        'card': card
      }

      i += 1
      x += 1
      if(x == 4):
        x = 0
        y += 1
    
    card_set.append({
      'x': Template1.coord2slot(lucky_pos[0][0], lucky_pos[0][1])[0],
      'y': Template1.coord2slot(lucky_pos[0][0], lucky_pos[0][1])[1],
      'card': lucky_card
    })

    card_set.append({
      'x': Template1.coord2slot(lucky_pos[1][0], lucky_pos[1][1])[0],
      'y': Template1.coord2slot(lucky_pos[1][0], lucky_pos[1][1])[1],
      'card': lucky_card
    })

    return card_set


