print("Wprowadź pierwsze słowo.")
pierwsze = input()
print("Wprowadź to słowo jeszcze raz (może mieć zamienioną kolejność liter, pamiętaj, żeby zgadzała się ich cyfra.")
drugie = input()
łańcuch1 = ""
łańcuch2 = ""

łańcuch1 = "".join(pierwsze)
łańcuch2 = "".join(drugie)

print(łańcuch1 + " " + łańcuch2)

for i in range(len(łańcuch1)):
     if łańcuch1[i] != łańcuch2[i]:
         print("Znaleziono różnicę na pozycji:", i+1)

###
# print("Podaj numer telefonu.")
# numer = input()
# numer_telefonu = ""
# numer_telefonu = "".join(numer)
#
# for znak in numer_telefonu:
#     if znak == " ":
#         numer_telefonu = numer_telefonu.replace(" ", "")
#     elif znak == "-":
#         numer_telefonu = numer_telefonu.replace("-", "")
#
# print(numer_telefonu)
# same_litery = numer_telefonu.isalpha()
# print(same_litery)

# print("Podaj dowolne zdanie.")
# zdanie = input()
#
# łańcuch = ""
# łańcuch = "".join(zdanie)
# print(łańcuch)
#
# # łańcuch_lista = list(łańcuch)
# # print(łańcuch_lista)
#
#
# print(łańcuch.find(" "))
#
# # człon1 = ""
# # for i in range(len(łańcuch)):
# #     if "i" < " ":
# #         człon = "".join(i)

#Napisz program, który pobiera z klawiatury dowolny łańcuch znaków numerycznych
#(1,2,3,4,5,6,7,8,9,0) i wyświetla informację o unikalnych znakach w ciągu. Np.

    # 111111111: unikalne znaki to 1
    # 123123123333: unikalne znaki to 123
    # 4: unikalne znaki to 4

print("Podaj dowolną ilość cyfr.")
cyfry = input()
łańcuch_cyfr = ""
łańcuch_cyfr = "".join(cyfry)
łańcuch_lista = list(łańcuch_cyfr)
for i in range(len(łańcuch_lista)):
    if łańcuch_lista[i] != [i+1]
        print(łańcuch_cyfr[i])
# for liczba in łańcuch_lista[:]:
#     if liczba == liczba:
#         łańcuch_lista.remove(liczba)
# print(łańcuch_lista)
# lista = []
#
# # for znak in łańcuch_cyfr:
#
#
# for i in range(len(łańcuch_cyfr)):
#     if [i+1] != [i]:
#         lista.append(i)
# print(lista)
#
#

# print("Podaj dowolną ilość cyfr.")
# cyfry = input()
# łańcuch_cyfr = ""
# łańcuch_cyfr = "".join(cyfry)
# print(łańcuch_cyfr)
#
# ilość_wystąpień = łańcuch_cyfr.count()
# for i in range(len(łańcuch_cyfr)):
#     if łańcuch_cyfr[]

# Napisz program, który pobiera z klawiatury dowolny łańcuch znaków.
# Wymień pierwszą i ostatnią literę. Wyświetl otrzymany rezultat.
#
#
# print("Podaj dowolny łańcuch znaków.")
# wyraz = input()
# łańcuch = ""
# łańcuch = "".join(wyraz)
#
# pierwsza = łańcuch[0]
# ostatnia = łańcuch[-1]
#
łańcuch_lista = list(łańcuch)
łańcuch_lista[0] = ostatnia
łańcuch_lista[-1] = pierwsza
łańcuch = "".join(łańcuch_lista)
#
# print(łańcuch)

# Program powinien pobierać z klawiatury 3 stringi.
# Bez pomocy funkcji len() zbadaj, który jest najdłuższy i wyświetl tę informację w podsumowaniu.

# print("Podaj pierwszy łańcuch znaków.")
# pierwszy = input()
# print("Podaj drugi łańcuch znaków.")
# drugi = input()
# print("Podaj trezci łańcuch znaków.")
# trzeci = input()
#
# pierwszy_łańcuch = ""
# drugi_łańcuch = ""
# trzeci_łańcuch = ""
#
# pierwszy_łańcuch = "".join(pierwszy)
# drugi_łańcuch = "".join(drugi)
# trzeci_łańcuch = "".join(trzeci)
#
# suma_znaków1 = 0
# for znak in pierwszy_łańcuch:
#     suma_znaków1 += 1
# print("Pierwszy łańcuch ma:", suma_znaków1, "znaków.")
#
# suma_znaków2 = 0
# for znak in drugi_łańcuch:
#     suma_znaków2 +=1
# print("Drugi łańcuch ma:", suma_znaków2, "znaków.")
#
# suma_znaków3 = 0
# for znak in trzeci_łańcuch:
#     suma_znaków3 += 1
# print("Drugi łańcuch ma:", suma_znaków3, "znaków.")
#
# if suma_znaków1 > suma_znaków2 and suma_znaków1 > suma_znaków3:
#     print("Najwięcej znaków ma łańcuch 1.")
# elif suma_znaków2 > suma_znaków1 and suma_znaków2 > suma_znaków3:
#     print("Najwięcej znaków ma łańcuch 2.")
# elif suma_znaków3 > suma_znaków2 and suma_znaków3> suma_znaków1:
#     print("Najwięcej znaków ma łańcuch 3.")

# Poproś użytkownika o podanie imienia i nazwiska.
# Sprawdź, czy podany ciąg znaków składa się tylko z liter.
# Użytkownicy bywają leniwi.
# Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich, usuń zbędne znaki.
# Sprawdź działanie programu na kilku stringach: np jan kowalski, jan.kowalski, JaN KOWALskI, Jan1Kowalski1

# print("Podaj imię.")
# imię = input()
# print("Podaj nazwisko.")
# nazwisko = input()
# imię_łańcuch= ""
# imię_łańcuch= "".join(imię)
# nazwisko_łańcuch = ""
# nazwisko_łańcuch = "".join(nazwisko)
#
#
# imię_łańcuch = imię_łańcuch.capitalize()
# nazwisko_łańcuch = nazwisko_łańcuch.capitalize()
# łańcuch_główny = imię_łańcuch + " " + nazwisko_łańcuch
# print(łańcuch_główny)
#
# same_litery = łańcuch_główny.isalpha()
# print(same_litery)
