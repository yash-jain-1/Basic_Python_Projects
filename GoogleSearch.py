from googlesearch import search
query = input("What do you want to search about:")
for i in search(query, tld = "co.in", num = 10, stop = 20, pause = 2):
  print(i)
