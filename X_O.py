# 1. Приветсвие
# 2. Что и где храним?
# 3. Что делаем с данными?
# 4. Ввод вользовотеля

# def hello():
#     print("-------------------------")
#     print("| Приветсвую вас в игре |")
#     print("|    Крестики-нолики    |")
#     print("|||||||||||||||||||||||||")
#     print("| Играем по координатам:|")
#     print("|   x - номер строки    |")
#     print("|   y - номер столбца   |")
#     print("-------------------------")
#
# def play_field():
#     print()
#     print("   | 0 | 1 | 2 | ")
#     print("  -------------- ")
#     for i, row in enumerate(game):
#         row_str = f" {i} | {' | '.join(row)} | "
#         print(row_str)
#         print("  -------------- ")
#     print()
#
# def where_xy():
#
#     while True:
#         supply = input("Введите координаты: ").split()
#         if len(supply) != 2:
#             print("Нужно ввести две координаты")
#             continue
#         x, y = supply
#         if not(x.isdigit() or not(y.isdigit())):
#             print("Введите числа! ")
#             continue
#         x, y = int(x), int(y)
#         if x < 0 or x > 2 or y < 0 or y > 2:
#             print('Неправильные координаты! Вводите от 0 до 2х!')
#             continue
#         if game[x][y] != " ":
#             print("Клетка занята, попробуйте другую")
#             continue
#         return x, y
#
#
# def who_win():
#     win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
#                  ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
#                  ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
#     for cord in win_cords:
#         win_row = []
#         for w in cord:
#             win_row.append(game[w[0]][w[1]])
#         if win_row == ["X", "X", "X"]:
#             print("Крестики победили!!!!")
#             print("------------------------")
#             print(" ／ﾌﾌ 　　　　　　 　ム｀ヽ")
#             print("/ ノ) 　 ）　ヽ                ")
#             print("/ ｜　　( ͡° ͜ʖ ͡°）（ゝ._,ノ   ")
#             print("/　ﾉ⌒7⌒ヽーく　  ＼　   ／      ")
#             print("丶＿ ノ ｡　　 ノ､　 ｡|/          ")
#             print("　　 `ヽ `ー-'_人`ーﾉ           ")
#             print("　　　 丶 ￣ _人'彡             ")
#             return True
#         if win_row == ["0", "0", "0"]:
#             print("Нолики победили!!!!")
#             print("------------------------")
#             print(" ／ﾌﾌ 　　　　　　 　ム｀ヽ")
#             print("/ ノ) 　 ）　ヽ                ")
#             print("/ ｜　　( ͡° ͜ʖ ͡°）（ゝ._,ノ   ")
#             print("/　ﾉ⌒7⌒ヽーく　  ＼　   ／      ")
#             print("丶＿ ノ ｡　　 ノ､　 ｡|/          ")
#             print("　　 `ヽ `ー-'_人`ーﾉ           ")
#             print("　　　 丶 ￣ _人'彡             ")
#             return True
#     return False
#
# hello()
# game = [[" "] * 3 for i in range(3) ]
# count = 0
# while True:
#     count += 1
#     play_field()
#     if count % 2 == 1:
#         print("Ход крестиков! ")
#     else:
#         print("Ход ноликов! ")
#
#     x, y = where_xy()
#
#     if count % 2 == 1:
#         game[x][y] = "X"
#     else:
#         game[x][y] = "0"
#     if who_win():
#         break
#     if count == 9:
#         print("Ничья!!!")
#         break





