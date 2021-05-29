#-sylaby
#cat 1.syll.ext.pl.txt | grep ^..$
#cat 1.syll.ext.pl.txt | grep ^...$
#cat 1.syll.ext.pl.txt | grep ^.*[aeęioóuy]$
#cat 1.syll.ext.pl.txt | grep ^[^aeęioóuy]*[aeęioóuy]$ > 1.syll.ext.lastvowel.pl.txt
#egrep '^[a-z]+[0-9]+$' hasla.txt #poczatek znaki, koniec cyfry

#-litery polskie
#cat dic.towns.diacritics.pl.txt | iconv -f=utf-8 -t=ascii//TRANSLIT
#cat dic.towns.pl.txt | tr [A-Z] [a-z]

#-tworz changelog
#git log --no-color --grep '^-' > ChangeLog-$(git tag | tail -n1)".txt"