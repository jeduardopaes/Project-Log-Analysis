#!/usr/bin/env python3
import connect

mostaar = connect.most_accessed_articles()
mostaau = connect.most_accessed_authors()
mostepd = connect.percent_erros_per_day()


def fill_with_space(text):
    if(len(text) < 22):
        return "{:<22}".format(text)

    return text


print("\n=========== MOST VIEWED ARTICLES ===========")
print("|          Title                   |  Views |")
print("|----------------------------------|--------|")
for ar in mostaar:
    print("| "+str(ar[0])+" | "+str(ar[1])+" |")

print("\n\n\n======= MOST VIEWED AUTHORS =======")
print("|          Title         |  Views |")
print("|------------------------|--------|")
for au in mostaau:
    print("| "+fill_with_space(str(au[0]))+" | "+str(au[1])+" |")

print("\n\n\n==== SIGNIFICANT ERROS PER DAY ====")
print("|     Day    |      % of Erros    |")
print("|------------|--------------------|")
for er in mostepd:
    print("| "+str(er[0])+" | "+str(er[1])+" |")

print("\n\n\n")

connect.closeConnection()
