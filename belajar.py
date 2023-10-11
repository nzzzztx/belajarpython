datas = [
    {'name':'Viserys Targaryen', 'age':50, 'dragon': {'isRaider':True, 'name':'Balerion', 'size':'Extra Large', 'age':'old'}},
    {'name':'Laenor Velaryon', 'age':26, 'dragon': {'isRaider':True, 'name':'Seasmoke', 'size':'Medium', 'age':'adult'}},
    {'name':'Alicent', 'age':27, 'dragon': {'isRaider':False}},
    {'name':'Daemon Targaryen', 'age':28, 'dragon': {'isRaider':True, 'name':'Caraxes', 'size':'Large', 'age':'adult'}},
    {'name':'Rhaenyra Targaryen', 'age':25, 'dragon': {'isRaider':True, 'name':'Syrax', 'size':'Medium', 'age':'young'}},
    {'name':'Corlys Velaryon', 'age':48, 'dragon': {'isRaider':False}},
]

oldest_age = 0 

characters_without_dragons = []

for character in datas:
    if 'dragon' not in character or not character['dragon'].get('isRaider', False):
        characters_without_dragons.append(character['name'])
    
        oldest_age = character['age']

print("Karakter yang tidak memiliki naga:")
for character_name in characters_without_dragons:
    print(character_name)

print(f"Umur tertua dari karakter yang ditampilkan adalah {oldest_age} tahun.")


def not_a_rider():
    numbering = 1
    max = 0
    for data in datas:
        if (not data['dragon']['isRaider']):
            if (data['age'] > max):
                max = data['age']
                print(numbering,".",data["name"])
                numbering += 1
        
    print("Umur maksimal: ",max)   

not_a_rider()