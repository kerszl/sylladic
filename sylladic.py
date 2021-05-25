#!/usr/bin/python3
from pathlib import Path, PureWindowsPath
from tqdm import tqdm
import argparse
import os
import itertools
import pyphen

VERSION = 'v. 0.3\n'
DATE = "date: (25.05.2021)\n"
AUTHOR = 'author: Szikers (kerszi@protonmail.com)\n'
GITHUB = 'repo: https://github.com/kerszl/sylladic\n'
PLATFORMS = "Linux, Windows"

class draw_sample_graph:
    def __init__(self):
        pass

    def draw_chars(self):
        #size = {"s":26,"s+b":52,"s+pl":35,"s+b+pl":70,"prin...":100,"syll":17653}
        size = {"d": 10, "l": 26, "l+u": 52,
                "l+pl": 35, "l+u+pl": 70, "prin...": 100}

        print("{:<8}{:<4}{:<7,}{:<10,}{:<12,}{:<15,}{:<18,}{:<21,}{:<22,}".format(
            "char", 1, 2, 3, 4, 5, 6, 7, 8))

        for j, i in size.items():
            print("{:<8}{:<4}{:<7,}{:<10,}{:<12,}{:<15,}{:<18,}{:<21,}{:<22,}".format(
                j, i, i**2, i**3, i**4, i**5, i**6, i**7, i**8))

    def draw_legend(self):
        print()
        print("1..8 - iterations, d - digits, l - lower chars, u - upper chars,")
        print("pl - polish chars, prin.. - all printable chars")

def file_suffix_message (file_name):
    print("Filename "+file_name+" must have a suffix")

class Dictionary:
    pyph = 0
    path_and_file_in = 0
    path_and_file_out = 0
    word_dict = 0
    syll_dict = set()
    sorted_syll_dict = []
    progress_bar = 0

    def __init__(self, file_, contry_code_):
        contry_code_check = pyphen.language_fallback(contry_code_)
        if contry_code_check:
            self.pyph = pyphen.Pyphen(lang=contry_code_check)
            print("The Contry Code :", contry_code_check)
        else:
            print("The Country code", contry_code_, "is unavailable")
            exit()
        path_and_file_in_ = file_
        path_and_file_in_ = Path(PureWindowsPath(path_and_file_in_))
        path_and_file_out_ = file_
        path_and_file_out_ = Path(PureWindowsPath(path_and_file_out_))


        suffix = Path(path_and_file_out_).suffix
        file_name = Path(path_and_file_out_).name
        
        if not suffix:
            file_suffix_message(file_name)            
            exit()        

        path_and_file_out_= str(path_and_file_out_).rsplit(suffix)[0]
        path_and_file_out_ +="."+contry_code_+suffix
                
        if not path_and_file_in_.exists():
            print("File        :", file_,
                  "doesn't exists.")
            exit()

        else:
            self.path_and_file_in = path_and_file_in_
            self.path_and_file_out = path_and_file_out_
            print("FileIn      :", self.path_and_file_in)
            print("FileOut     :", self.path_and_file_out)

    def load_word_dictionary(self):
        with open(self.path_and_file_in) as f:
            self.word_dict = f.read().splitlines()
        print(self.path_and_file_in, ": loaded")

    def word2syll(self):
        word_dic_len = len(self.word_dict)
        print("Scrapping syllables")
        self.progress_bar = tqdm(total=word_dic_len)
        for i in self.word_dict:
            syllables = self.pyph.inserted(i, ' ').split()
            self.progress_bar.update(1)

            for j in syllables:
                self.syll_dict.add(j)
        self.progress_bar.close()
        print("Syllables     :", len(self.syll_dict))

    def sort_syll(self):
        self.sorted_syll_dict = sorted(self.syll_dict)

    def save_syll_directory(self):
        state=0
        if os.path.exists(self.path_and_file_out):                
            state="overwrited"
        else:
            state="saved"
        with open(self.path_and_file_out, 'w') as f:
            for data in self.sorted_syll_dict:
                f.write(data+"\n")        
            print(str(self.path_and_file_out)+" :"+state)

class MakeMultiSyllab:
    progress_bar = 0
    MAX_BUFFOR = 100200350
    syllabdic = 0
    iterations = 0
    path_and_file_out = 0
    path_and_file_in = 0
    amount = 2
    MIN_AMOUNT = 2    
    MAX_AMOUNT = 6

    def __init__(self, file_, amount_):
        try:
            amount_ = int(amount_)
        except:
            print("Amount must be a digit")
            exit()
        self.amount = int(amount_)

        if self.amount > self.MAX_AMOUNT or self.amount < self.MIN_AMOUNT:
            print("Enter a number in the range: "+str(self.MIN_AMOUNT)+".."+str(self.MAX_AMOUNT))
            exit()


        path_and_file_in_ = file_
        path_and_file_in_ = Path(PureWindowsPath(path_and_file_in_))

        self.path_and_file_in = path_and_file_in_
        path_and_file_out_ = Path(PureWindowsPath(path_and_file_in_))
        suffix = Path(path_and_file_out_).suffix
        file_name = Path(path_and_file_out_).name

        if not suffix:
            file_suffix_message(file_name)            
            exit()

        self.path_and_file_out = str(path_and_file_out_).rsplit(suffix)[0]
        self.path_and_file_out += ".x"+str(self.amount)+"it"+suffix

        if not self.path_and_file_in.exists():
            print("File        :", file_,
                  "doesn't exists.")
            exit()

        else:
            status = 0
            if os.path.exists(self.path_and_file_out):
                os.remove(self.path_and_file_out)
                status="(overwrited)"
            else:
                status="(saved)"            
            print("FileIn      :", self.path_and_file_in)
            print("FileOut     :", self.path_and_file_out,status)

            



    def iteration_dic(self, *iteration):
        to_limit = 0
        line = []
        print("Writing combinations to file")
        self.progress_bar = tqdm(total=self.iterations)

        for i in itertools.product(*iteration):
            self.progress_bar.update(1)

            line.append("".join(i)+'\n')
            to_limit += 1
            if to_limit > self.MAX_BUFFOR:
                with open(self.path_and_file_out, 'a') as f:
                    f.write("".join(line))
                to_limit = 0
                line = []
        if to_limit != 0:
            with open(self.path_and_file_out, 'a') as f:
                f.write("".join(line))

        self.progress_bar.close()

    def multi_syllab(self):

        with open(self.path_and_file_in, 'r') as f:
            syllabdic_ = f.readlines()

        self.syllabdic = [i.strip() for i in syllabdic_]
        syllabdic_lenght = len(self.syllabdic)

        self.iterations = syllabdic_lenght**self.amount

        if self.amount == 2:
            self.iteration_dic(self.syllabdic, self.syllabdic)
        if self.amount == 3:
            self.iteration_dic(self.syllabdic, self.syllabdic, self.syllabdic)
        if self.amount == 4:
            self.iteration_dic(self.syllabdic, self.syllabdic,
                               self.syllabdic, self.syllabdic)
        if self.amount == 5:
            self.iteration_dic(self.syllabdic, self.syllabdic,
                               self.syllabdic, self.syllabdic,
                               self.syllabdic)
        if self.amount == 6:
            self.iteration_dic(self.syllabdic, self.syllabdic,
                               self.syllabdic, self.syllabdic,
                               self.syllabdic, self.syllabdic)


parser = argparse.ArgumentParser(description=
"""Sylladic is a program which helps you to create dictionaries. 
A dictionary is made up of words and converted into syllables 
(thanx 4 great pyphen library) 
E.g. (word from Polish dictionary): 
word = abolicjonistyczną 
syllab = abo-li-cjo-ni-stycz-ną 

./sylladic.py -d dic.sample.pl.txt pl

When you create the dictionary, you can
multiply syllables and other chars from file.

./sylladic.py -m digits.txt 4



""", formatter_class=argparse.RawTextHelpFormatter
                                 )

parser.add_argument('-m', '--multiply', help='multiply words and write all to the file. Value of multiply must be beetwen 2..4',
                    nargs=2, metavar=('file', 'multiply'))
parser.add_argument('-d', '--dictionary', help='scrab syllables from words',
                    nargs=2, metavar=('file', 'contry_code [like pl,en]'))
parser.add_argument('-v', '--version', action='version',
                    version='program: %(prog)s '+VERSION+DATE+AUTHOR+GITHUB
                                        
                      )
parser.add_argument(
    '-g', '--graph', help='draw a simple iteration graph', action="store_true")
args = parser.parse_args()

if args.multiply:
    multiply = MakeMultiSyllab(args.multiply[0], args.multiply[1])
    multiply.multi_syllab()
    exit()

if args.dictionary:
    make_syll = Dictionary(args.dictionary[0], args.dictionary[1])
    make_syll.load_word_dictionary()
    make_syll.word2syll()
    make_syll.sort_syll()
    make_syll.save_syll_directory()
    exit()

if args.graph:
    graph = draw_sample_graph()
    graph.draw_chars()
    graph.draw_legend()
    exit()


parser.print_help()
