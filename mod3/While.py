# import time
# loop = 0

# while loop < 20:
#     print(round(loop + 0.1, 1))
#     time.sleep(0.003)
#     loop += 0.1

#______________________________________
# import time

# aika = int(input('ajastin: \n'))

# while aika > 0:
#     print(aika)
#     time.sleep(1)
#     aika -= 1
# print('0')
# time.sleep(0.1)
# print('💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
# print('KABOOM!')
# print('💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
#______________________________________

password = 'salasana'
attempt = input('Anna salasana:  \t')
kerta = 1
limit = 6
while attempt != password and kerta < limit:
    attempt = input(f'Väärä salasana. Yrityksiä jäljellä: {limit - kerta}\nYritä uudelleen:\t')
    kerta += 1
    if kerta == limit: break
else:
    print('oikein')

if kerta >= limit: print('Liian monta yritystä, yritä myöhemmin uudelleen.')

