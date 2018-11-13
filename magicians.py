def show_magicians(names):
    for name in names:
        print(name.title())

majutsushi = ["arkana", "dmg", "endymion"]

def make_great(names):
    for name in names:
        print("The Great " + name.title())

mages = majutsushi[:]
spellcasters = []
spellcasters.append(make_great(mages))
show_magicians(majutsushi)
show_magicians(spellcasters)
