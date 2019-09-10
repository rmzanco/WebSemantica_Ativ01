import re

# Return a list containing every occurrence of "ai":
cod = 26
str_cod = str(cod)
str = "<span>26</span><a href='cursos/cur26.html'>Artes Cênicas - Integral</a><br/>"
x = re.search(r"\b" + str_cod + r"\b", str)
print(x)