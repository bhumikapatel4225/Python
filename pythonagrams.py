letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

letter_to_points = {key:val for key,val in zip(letters, points)}
print(letter_to_points)

def score_word(word):
  point_total = 0
  for wd in word:
    if letter_to_points[wd]:
      point_total += 0
    point_total += letter_to_points[wd]
  return point_total

brownie_points = score_word('BROWNIE')
print("Brownie Points:", brownie_points)

player_to_words = {"BLUE": ["EARTH", "ERASER", "ZAP"], "TENNIS": ["EYES", "BELLY", "COMA"], "EXIT": ["MACHINE", "HUSKY", "PERIOD"]}
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print("Player to Points:", player_to_points)
