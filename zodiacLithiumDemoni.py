def zodiac(year):
    if year % 12 == 0:
        return "Monkey"
    elif year % 12 == 1:
        return "Rooster"
    elif year % 12 == 2:
        return "Dog"
    elif year % 12 == 3:
        return "Pig"
    elif year % 12 == 4:
        return "Rat (鼠 / Shǔ)"
    elif year % 12 == 5:
        return "Ox (牛 / Niú)"
    elif year % 12 == 6:
        return "Tiger (虎 / Hǔ)"
    elif year % 12 == 7:
        return "Rabbit (兔 / Tù)"
    elif year % 12 == 8:
        return "Dragon (龙 / Lóng)"
    elif year % 12 == 9:
        return "Snake (蛇 / Shé)"
    elif year % 12 == 10:
        return "Horse (马 / Mǎ)"
    else:
        return "Goat (羊 / Yáng)"

year = int(input("Enter your birth year: "))
print("\nYour Chinese zodiac sign is :", zodiac(year))
