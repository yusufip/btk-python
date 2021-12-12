#listeye eleman ekleme:append

liste=[1,2,3,8,6,4,9]
print(liste)
liste.append("btk")
print(liste)

#eleman silme:pop
liste.pop()#son elemanı siler
print(liste)
liste.pop(0) #indekdeki elemanı siler
print(liste)
#a-z veya tam tersi yani küçükden buyuge yada tam tersi sıralama : sort
liste.sort(reverse=True)
print(liste)