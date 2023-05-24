zakupy={'piekarnia':['chleb','bułki','pączek'],'warzywniak':['marchew','seler','rukola']}
suma=0
z=0
rzeczy=[]
zakupy['piekarnia'].append('drożdżówka')
zakupy['warzywniak'].append('kapusta')
zakupy['drogeria']=['szampon','pasta do zębów','żel pod prysznic']
print(zakupy.get('piekarnia'))
for i in zakupy:
    rzeczy=zakupy[i]
    for j in rzeczy:
        rzeczy[z]=j.capitalize()
        z=z+1
    zakupy[i]=rzeczy
    z=0
    print(f"Idę do {i.capitalize()}, kupuję tu następujące rzeczy {zakupy[i]}")
    suma=suma+len(zakupy[i])
print(f"W sumie kupuję {suma} sześć produktów")