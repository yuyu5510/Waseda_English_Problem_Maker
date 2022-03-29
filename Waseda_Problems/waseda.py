# coding: utf-8
from nltk.corpus import wordnet as wn
#同じ階層にあるword_use.pyをimport
from word_use import word_use
import numpy as np


class Waseda:
    def __init__(self):
        #word_useは先頭のアルファベットによって振り分けている二重のリスト
        #24以下の数字をランダムに選択
        #xから始まる英単語で高校以前で学ぶものがなさそうなので省きました
        #xから始まる英単語を入れる場合は25を26にして、
        #word_useにxからはじまる英単語のリストを入れてください
        rand = np.random.randint(25)
        rand2 = np.random.randint(len(word_use[rand]))
        #答え
        self.ans = word_use[rand][rand2]
        rand3 = np.random.randint(len(word_use[rand]))
        rand4 = np.random.randint(len(word_use[rand]))
        #選択肢を存在する単語から2つ生成
        self.dummy = word_use[rand][rand3]
        self.dummy2 = word_use[rand][rand4]
        #選択肢
        self.choices = []
        #例文を入れる
        self.examples= []

        synsets = wn.synsets(self.ans)
        #選んだ単語の定義と例文を呼び出して追加
        for i in range(len(synsets)):
            if self.ans in str(synsets[i]):
        #teachの例文でtaughtが入ってたりすると問題としてふさわしくないし面倒なのでそういうのは切り捨てる
                ok = False
                for j in range(len(synsets[i].examples())):
                    if ok: break
                    if self.ans in synsets[i].examples()[j]:
                        exam = synsets[i].definition()
                        exam += ';  '
                        exam += synsets[i].examples()[j]
                        self.examples.append(exam)
                        ok = True

        #例文が複数ある場合、毎回固定だとつまらないのでシャッフルしておく
        np.random.shuffle(self.examples)
        #例文がひとつもなかった時用に定義だけ追加
        for i in range(len(synsets)):
            if self.ans in str(synsets[i]):
                if len(self.examples) == 0:
                    self.examples.append(synsets[i].definition())

        #本家は2個なので2個以上ある場合は2個になるまで削除
        while len(self.examples) > 2:
            self.examples.pop()

    #早稲田方式に単語を変換
    def convert_waseda(self, s):
        one = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        two = ['h', 'i', 'j', 'k', 'l', 'm']
        three = ['n', 'o', 'p','q', 'r', 's']
        four = ['t', 'u', 'v', 'w', 'x', 'y', 'z']

        conv = ""
        conv += s[0]
        for i in range(1,len(s)):
            if s[i] in one:
                conv += '1'
            elif s[i] in two:
                conv += '2'
            elif s[i] in three:
                conv += '3'
            elif s[i] in four:
                conv += '4'
        
        if not conv in self.choices:
            self.choices.append(conv)
        #もし選択肢に同一のがあればランダムに生成
        else:
            self.random_choice()
        return conv
    
    def random_choice(self):
        rand_choice = self.ans[0]
        #長さが短すぎると嘘がわかるので最低4文字以上にする
        rand_num1 = np.random.randint(3,8)
        for i in range(rand_num1):
            rand_choice += str(np.random.randint(4)+1)
        #重複がなければ追加あればもう一回呼ぶ(確率的には何回も完全一致はしないはずなので)
        if not rand_choice in self.choices:
            self.choices.append(rand_choice)
        else :
            self.random_choice()
    
    def solve(self):
        print("The correct answer is {}.".format(self.ans))
            

    def problem(self):
        #例文の中にある正解の単語を(   )で置き換える
        for i in range(len(self.examples)):
            tmp = '{}. {}.'.format(i+1, self.examples[i].replace(self.ans, '(     )'))
            print(tmp)
        #答えが早稲田方式に変換されたのを持っておく
        ans_converted = self.convert_waseda(self.ans)
        self.convert_waseda(self.dummy)
        self.convert_waseda(self.dummy2)
        self.random_choice()
        np.random.shuffle(self.choices)

        #print()で改行する蛮行をする
        print()
        print()


        for i in range(len(self.choices)):
            print('{}. {}'.format(i+1, self.choices[i]))

        ok = True
        
        while ok:
            print('\nChoose answer: ')
            #例外処理
            try:
                kaitou = int(input())
            except KeyboardInterrupt:
                return
            except:
                print('Invalid input. Try again.')
                continue

            #1,2,3,4以外の数字が選ばれた際もう一回入力させる
            if kaitou <= 0 or kaitou > 4:
                print('Invalid input. Try again.')
                continue

            kaitou -= 1
            if ans_converted == self.choices[kaitou]:
                print('Your answer is collect!!')
                self.solve()
                ok = False
            else:
                print('Your answer is wrong')
                print('Do you continue ? please answer yes or no.')
                cont = str(input())
                if cont == "YES" or cont == "Yes" or cont == "yes" or cont == "y" or cont == "Y":
                    continue
                #yes以外では終了
                else:
                    ok = False
                #答えを見せる
                self.solve()

a = Waseda()
a.problem()

        


        

            
        
        


        