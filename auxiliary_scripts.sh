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
#ChangeLog=ChangeLog-$(git tag | tail -n1)".txt" && git log --no-walk --tags --decorate=full > $ChangeLog
#zmiana nazwy komitu
#git rebase -i @~9   # Show the last 9 commits in a text editor
#edit zamiast pick
#git rebase --continue


