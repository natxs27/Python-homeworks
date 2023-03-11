S = "Litwo, ojczyzno moja ty jesteś jak zdrowie, i le cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie, widzę i opisuję, bo tęsknię po tobie. Panno święta, co Jasnej bronisz Częstochowy i w Ostrej świecisz Bramie! Ty, co gród zamkowy nowogródzki ochraniasz z jego wiernym ludem jak mnie dziecko do zdrowia powróciłaś cudem. Gdy od płaczącej matki, pod Twoją opiekę. Ofiarowany martwą podniosłem powiekę i zaraz mogłem pieszo, do Twych świątyń progu iść za wrócone życie podziękować Bogu tak nas powrócisz cudem na Ojczyzny łono, tymczasem, przenoś moją duszę utęsknioną do tych pagórków leśnych, do tych łąk zielonych, szeroko nad błękitnym Niemnem rozciągnionych; do tych pól malowanych zbożem rozmaitem, wyzłacanych pszenicą, posrebrzanych żytem, gdzie bursztynowy świerzop, gryka jak śnieg biała. Gdzie panieńskim rumieńcem dzięcielina pała,a wszystko przepasane jakby wstęgą, miedzą zieloną, na niej zrzadka ciche grusze siedzą."
a=str(S.count(" "))
b=str(len(S)-S.count(" "))
print("Lista S ma " + a + " wyrazy, " + b + " znaki czarne, a najdłuższe słowo to " + max(S.split(), key=len) + ".")
L=S.split()
L.sort(key=str.casefold)
print(L)
L.sort(key=len)
print(L)
