from .models import *
import random
import binascii
import numpy as np

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

def random_word_from_db(sentence, word_len):
    for i in sentence:
        if len(str(i)) == word_len:
            return(str(i))
    return ""


def listToString(s):
    str1 = ""
    for ele in s:
        if ele != s[-1]:
            str1 += str(ele) + ', '
        else:
            str1 += str(ele)
    return str1

def text_to_bits(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

def isint(s):
    return float(s).is_integer()


def clean_ex5(_task5):
    if _task5.answer <= 0:
        return False
    elif isint(_task5.answer) == False:
        return False
    elif _task5.answer > 200:
        return False
    else:
        return True

class ex1():
    def __init__(self, level):
        self.koef = 0
        if level == 1:
            koef = 8
        elif level == 2:
            koef = 16
        else:
            koef = 32
        list_of_sentense = self.generate_sentence()
        list_len = len(list_of_sentense)
        temp = random.randint(0, list_len-1)
        self.word = list_of_sentense[random.randint(0, temp)]
        self.sentence = listToString(list_of_sentense)
        self.size_of_word = ((len(self.word)+2)*koef)/8
    def generate_sentence(self):
        sentence = Model_Word.objects.all().order_by('?')
        list_of_sentence = list()
        for i in range(2, 11):
            temp = random_word_from_db(sentence, i)
            if temp != "":
                list_of_sentence.append(temp)
        return list_of_sentence

class ex2():
    def __init__(self, level):
        start = 0
        end = 0
        if level == 1:
            start = 0
            end = 4
        elif level == 2:
            start = 4
            end = 6
        else:
            start = 6
            end = 12
        sentence = Model_Word.objects.all().order_by('?')
        list_len = len(sentence)
        temp = random.randint(0, list_len-1)
        flag = False
        self.word = sentence[random.randint(0, temp)]
        while (flag == False):
            self.word = sentence[random.randint(0, temp)]
            if len(str(self.word)) >= start and len(str(self.word)) <= end:
                flag = True
        for_mixed_word = list(str(self.word))
        self.mixed_word = random.sample(for_mixed_word, len(for_mixed_word))
        self.char_dict = dict()
        counter = 1
        self.code = ''
        for i in self.mixed_word:
            self.char_dict[i] = text_to_bits(counter)
            counter += 1
        for i in for_mixed_word:
            self.code += str(self.char_dict[i])


class ex3():
    def __init__(self, level):
        start = 0
        end = 0
        if level == 1:
            start = 20
            end = 40
        elif level == 2:
            start = 30
            end = 50
        else:
            start = 40
            end = 60
        border1 = random.randint(1, start)
        border2 = random.randint(border1 + 1, end)
        self.MIN_OR_MAX = random.randint(1, 2)
        EX_NUMBER = random.randint(1, 4)
        self.EX_TEXT = self.get_ex_string(EX_NUMBER, border1, border2)
        self.ANSWER = self.ANSWER_NUMBER(EX_NUMBER, self.MIN_OR_MAX, border1, border2)

    def ANSWER_NUMBER(self, ex_number, min_or_max, b1, b2):
        border1 = b1
        border2 = b2
        if ex_number == 1:
            number_list = []
            for i in range(1, 100):
                if self.NE_I(i, border1, border2):
                    number_list.append(i)
            if min_or_max == 1:
                return min(number_list)
            else:
                return max(number_list)
        elif ex_number == 2:
            number_list = []
            for i in range(1, 100):
                if self.NE_I_CHET(i, border1):
                    number_list.append(i)
            if min_or_max == 1:
                return min(number_list)
            else:
                return max(number_list)
        elif ex_number == 3:
            number_list = []
            for i in range(1, 100):
                if self.NE_I_NECHET(i, border1):
                    number_list.append(i)
            if min_or_max == 1:
                return min(number_list)
            else:
                return max(number_list)
        elif ex_number == 4:
            number_list = []
            for i in range(1, 100):
                if self.NE_I_NE(i, border1, border2):
                    number_list.append(i)
            if min_or_max == 1:
                return min(number_list)
            else:
                return max(number_list)

    def get_ex_string(self, EX_NUMBER, border1, border2):
        if EX_NUMBER == 1:
            return "НЕ (x < {0}) И (Х < {1})".format(border1, border2)
        elif EX_NUMBER == 2:
            return "НЕ (x < {0}) И (Х - четное)".format(border1)
        elif EX_NUMBER == 3:
            return "НЕ (x < {0}) И (Х - нечетное)".format(border1)
        elif EX_NUMBER == 4:
            return "НЕ (x <= {0}) И НЕ (Х > {1})".format(border1, border2)

    def NE_I(self, x, border1, border2):
        if x >= border1 and x < border2:
            return True
        return False

    def NE_I_CHET(self, x, border1):
        if x >= border1 and x % 2 == 0:
            return True
        return False

    def NE_I_NECHET(self, x, border1):
        if x >= border1 and x % 2 != 0:
            return True
        return False

    def NE_I_NE(self, x, border1, border2):
        if x > border1 and x <= border2:
            return True
        return False

class ex4():
    def __init__(self, level):
        if level == 1:
            vector = [
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            ]
            self.graph = [
                [0, vector[0], vector[1], vector[2]],
                [vector[0], 0, vector[3], vector[4]],
                [vector[1], vector[3], 0, vector[5]],
                [vector[2], vector[4], vector[5], 0]
            ]

            way1 = self.graph[0][2]
            way2 = self.graph[0][2]+self.graph[2][3]
            way3 = self.graph[0][1]+self.graph[1][2]+self.graph[2][3]
            way4 = self.graph[0][1]+self.graph[1][3]
            self.answer = min(min(way1, way2), min(way3, way4))
        elif level == 2:
            vector = [
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            ]
            self.graph = [
                [0, vector[0], vector[1], vector[2], vector[3]],
                [vector[0], 0, vector[4], vector[5], vector[6]],
                [vector[1], vector[4], 0, vector[7], vector[8]],
                [vector[2], vector[5], vector[7], 0, vector[9]],
                [vector[3], vector[6], vector[8], vector[9], 0]
            ]

            way1 = self.graph[0][2] + self.graph[2][4]
            way2 = self.graph[0][2] + self.graph[3][2] + self.graph[4][3]
            way3 = self.graph[0][1] + self.graph[1][2] + self.graph[2][4]
            way4 = self.graph[0][1] + self.graph[1][2] + self.graph[2][3] + self.graph[3][4]

            self.answer = min(min(way1, way2), min(way3, way4))
        else:
            vector = [
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            ]
            self.graph = [
                [0, vector[0], vector[1], vector[2], vector[3]],
                [vector[0], 0, vector[4], vector[5], vector[6]],
                [vector[1], vector[4], 0, vector[7], vector[8]],
                [vector[2], vector[5], vector[7], 0, vector[9]],
                [vector[3], vector[6], vector[8], vector[9], 0]
            ]

            way1 = self.graph[0][4]
            way2 = self.graph[0][3]+self.graph[3][4]
            way3 = self.graph[0][2]+self.graph[2][4]
            way4 = self.graph[0][2]+self.graph[2][3]+self.graph[3][4]
            way5 = self.graph[0][1]+self.graph[1][4]
            way6 = self.graph[0][1]+self.graph[1][3]+self.graph[3][4]
            way7 = self.graph[0][1]+self.graph[1][2]+self.graph[2][4]
            way8 = self.graph[0][1]+self.graph[1][2]+self.graph[2][3]+self.graph[3][4]

            self.answer = min(way1,way2,way3,way4,way5,way6,way7,way8)

class ex5():
    def __init__(self, level):
        open_type = random.randint(1,5)
        close_type = random.randint(1,5)
        self.question1 = ""
        self.question2 = ""
        number1 = 0
        number2 = 0
        level_number = 0
        if level == 1:
            level_number = 7
        elif level == 2:
            level_number = 9
        else:
            level_number = 12
        if open_type == 3:
            number1 = random.randint(1,3)
        else:
            number1 = random.randint(1, level_number)

        if close_type == 3:
            close_type = 1
            number2 = random.randint(2,3)
        else:
            number2 = random.randint(2, level_number)

        if close_type == 5:
            number2 = random.randint(2,5)
            number1 = random.randint(5, level_number)
        if open_type == 5:
            number1 = random.randint(2,5)
            number2 = random.randint(5, level_number)

        if open_type == 5 and close_type == 5:
            close_type = 4
        self.type1 = open_type
        self.type2 = close_type
        self.number_open_type = number1
        self.number_close_type = number2
        self.number = random.randint(1,10)
        self.algoritm = []
        for i in range(1, random.randint(3,6)):
            self.algoritm.append(random.randint(1,2))
        self.answer = self.number
        for i in self.algoritm:
            if i == 1:
                if open_type == 1:
                    self.answer += number1
                elif open_type == 2:
                    self.answer -= number1
                elif open_type == 3:
                    self.answer = self.answer ** 2
                elif open_type == 4:
                    self.answer *= number1
                elif open_type == 5:
                    self.answer /= number1
            else:
                if close_type == 1:
                    self.answer += number2
                elif close_type == 2:
                    self.answer -= number2
                elif close_type == 3:
                    self.answer = self.answer ** 2
                elif close_type == 4:
                    self.answer *= number2
                elif close_type == 5:
                    self.answer /= number2

        if open_type == 1:
            self.question1 = self.addition(1, number1)
        elif open_type == 2:
            self.question1 = self.substract(1, number1)
        elif open_type == 3:
            self.question1 = self.square(1, number1)
        elif open_type == 4:
            self.question1 = self.mult(1, number1)
        elif open_type == 5:
            self.question1 = self.devide(1, number1)


        if close_type == 1:
            self.question2 = self.addition(2, number2)
        elif close_type == 2:
            self.question2 = self.substract(2, number2)
        elif close_type == 3:
            self.question2 = self.square(2, number2)
        elif close_type == 4:
            self.question2 = self.mult(2, number2)
        elif close_type == 5:
            self.question2 = self.devide(2, number2)


    def addition(self, mode, number):
        if mode == 1:
            return "Прибавь на {0}".format(number)
        else:
            return "Прибавь на b"
    def substract(self, mode, number):
        if mode == 1:
            return "Вычти {0}".format(number)
        else:
            return "Вычти b"
    def square(self, mode, number):
        if mode == 1:
            return "Возведи в квадрат".format(number)
        else:
            return "Возведи в квадрат"
    def mult(self, mode, number):
        if mode == 1:
            return "Умнож на {0}".format(number)
        else:
            return "Умнож на  b"
    def devide(self, mode, number):
        if mode == 1:
            return "Раздели на {0}".format(number)
        else:
            return "Раздели на  b"

class ex6():
    def __init__(self,level):
        self.mode = random.randint(1,8)
        self.rand_number_for_s = random.randint(1,10*level)
        self.rand_number_for_t = random.randint(1,10*level)
        self.alg = self.alg_lang(self.mode, self.rand_number_for_s, self.rand_number_for_t)
        self.pascel = self.pascal_lang(self.mode, self.rand_number_for_s, self.rand_number_for_t)
        self.basic = self.basic_lang(self.mode, self.rand_number_for_s, self.rand_number_for_t)
        self.python = self.python_lang(self.mode, self.rand_number_for_s, self.rand_number_for_t)
        self.cpp = self.cpp_lang(self.mode, self.rand_number_for_s, self.rand_number_for_t)

        self.number_quantity = random.randint(4, 10)
        self.sum = 0
        self.pairs = []
        for i in range(1, self.number_quantity + 1):
            s = random.randint(-10*level, 10*level)
            t = random.randint(-10*level, 10*level)
            self.pairs.append([s,t])
            if self.fuction(self.mode, s,t, self.rand_number_for_s, self.rand_number_for_t):
                self.sum += 1
            else:
                pass


    def fuction(self, mode, s, t, rnd_s, rnd_t):
        if mode == 1:
            if s > rnd_s or t > rnd_t:
                return True
            else:
                return False
        elif mode == 2:
            if s > rnd_s or t < rnd_t:
                return True
            else:
                return False
        elif mode == 3:
            if s < rnd_s or t > rnd_t:
                return True
            else:
                return False
        elif mode == 4:
            if s < rnd_s or t < rnd_t:
                return True
            else:
                return False
        elif mode == 5:
            if s > rnd_s and t > rnd_t:
                return True
            else:
                return False
        elif mode == 6:
            if s > rnd_s and t < rnd_t:
                return True
            else:
                return False
        elif mode == 7:
            if s < rnd_s and t > rnd_t:
                return True
            else:
                return False
        elif mode == 8:
            if s < rnd_s and t < rnd_t:
                return True
            else:
                return False


    def alg_lang(self,mode, rnd_s, rnd_t):
        result = """алг <br>
                    нач <br>
                    цел s, t <br>
                    ввод s <br>
                    ввод t <br>
                    ввод A <br>"""
        if mode == 1:
            result += "если s > {0} или t > {1} <br>".format(rnd_s, rnd_t)
        elif mode == 2:
            result += "если s > {0} или t < {1} <br>".format(rnd_s, rnd_t)
        elif mode == 3:
            result += "если s < {0} или t > {1} <br>".format(rnd_s, rnd_t)
        elif mode == 4:
            result += "если s < {0} или t < {1} <br>".format(rnd_s, rnd_t)
        elif mode == 5:
            result += "если s > {0} и t > {1} <br>".format(rnd_s, rnd_t)
        elif mode == 6:
            result += "если s > {0} и t < {1} <br>".format(rnd_s, rnd_t)
        elif mode == 7:
            result += "если s < {0} и t > {1} <br>".format(rnd_s, rnd_t)
        elif mode == 8:
            result += "если s < {0} и t < {1} <br>".format(rnd_s, rnd_t)

        result +="""то вывод 'YES'<br>
                    иначе вывод 'NO' <br>
                    все<br>
                    кон<br>
                """
        return result

    def pascal_lang(self,mode, rnd_s, rnd_t):
        result = """var s, t: integer;  <br>
                    begin  <br>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">readln(s);</p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">readln(t);</p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">readln(A);</p>"""
        if mode == 1:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) or (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 2:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) or (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 3:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) or (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 4:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) or (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 5:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) and (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 6:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) and (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 7:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) and (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 8:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) and (t < {1})</p>'.format(rnd_s, rnd_t)

        result +="""<p style="margin: 1px 1px 1px 50px; padding: 1px;">then</p>
                    <p style="margin: 1px 1px 1px 50px; padding: 1px;">writeln("YES")</p>
                    <p style="margin: 1px 1px 1px 50px; padding: 1px;">else</p>
                    <p style="margin: 1px 1px 1px 50px; padding: 1px;">writeln("NO")</p>
                    end.
                """
        return result

    def basic_lang(self, mode, rnd_s, rnd_t):
        result = """DIM s, t AS INTEGER   <br>
                    INPUT s  <br>
                    INPUT t 
                    INPUT A """
        if mode == 1:
            result += 'IF s > {0} OR t > {1} THEN <br>'.format(rnd_s,rnd_t)
        elif mode == 2:
            result += 'IF s > {0} OR t < {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 3:
            result += 'IF s < {0} OR t > {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 4:
            result += 'IF s < {0} OR t < {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 5:
            result += 'IF s > {0} AND t > {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 6:
            result += 'IF s > {0} AND t < {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 7:
            result += 'IF s < {0} AND t > {1} THEN <br>'.format(rnd_s, rnd_t)
        elif mode == 8:
            result += 'IF s < {0} AND t < {1} THEN <br>'.format(rnd_s, rnd_t)
        result += """<p style="margin: 1px 1px 1px 25px; padding: 1px;">PRINT "YES" </p>
                    ELSE<br>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">PRINT "NO" </p>
                    ENDIF <br>
                """
        return result

    def python_lang(self, mode, rnd_s, rnd_t):
        result = """s = int(input())  <br>
                    t = int(input())  <br>
                    A = int(input())  <br> """
        if mode == 1:
            result += 'if (s > {0}) or (t > {1}):  <br>'.format(rnd_s,rnd_t)
        elif mode == 2:
            result += 'if (s > {0}) or (t < {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 3:
            result += 'if (s < {0}) or (t > {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 4:
            result += 'if (s < {0}) or (t < {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 5:
            result += 'if (s > {0}) and (t > {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 6:
            result += 'if (s > {0}) and (t < {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 7:
            result += 'if (s < {0}) and (t > {1}):  <br>'.format(rnd_s, rnd_t)
        elif mode == 8:
            result += 'if (s < {0}) and (t < {1}):  <br>'.format(rnd_s, rnd_t)
        result += """<p style="margin: 1px 1px 1px 25px; padding: 1px;">PRINT "YES" </p>
                    ELSE<br>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">PRINT "NO" </p>
                    ENDIF <br>
                """
        return result


    def cpp_lang(self,mode, rnd_s, rnd_t):
        result = """#include <iostream> <br>
                    using namespace std;   <br>
                    int main(){  <br>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">int s, t;;</p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">cin >> s;</p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">cin >> t;</p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">cin >> A;</p>"""
        if mode == 1:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) or (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 2:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) or (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 3:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) or (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 4:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) or (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 5:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) and (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 6:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s > {0}) and (t < {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 7:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) and (t > {1})</p>'.format(rnd_s, rnd_t)
        elif mode == 8:
            result += '<p style="margin: 1px 1px 1px 25px; padding: 1px;"> if (s < {0}) and (t < {1})</p>'.format(rnd_s, rnd_t)

        result +="""<p style="margin: 1px 1px 1px 50px; padding: 1px;">cout << "YES" << endl; </p>
                    <p style="margin: 1px 1px 1px 25px; padding: 1px;">else</p>
                    <p style="margin: 1px 1px 1px 50px; padding: 1px;">cout << "NO" << endl; </p>
                    return 0; <br>
                    } <br>
                """
        return result

class ex7():
    def __init__(self):
        numbers = range(1, 8)
        option = random.sample(numbers, 7)
        sentence = dict()
        sentence[option[0]] = 'https'
        sentence[option[1]] = '://'
        sentence[option[2]] = 'obr.'
        sentence[option[3]] = 'org'
        sentence[option[4]] = '/'
        sentence[option[5]] = 'rus.'
        sentence[option[6]] = 'doc'
        self.combination = ""
        for i in option:
            self.combination += str(i)
        self.sentence_list = list()
        for i in range(1, 8):
            self.sentence_list.append(sentence[i])

class ex8():
    def __init__(self,level):
        A = random.randint(1,30) * 10 * level
        B = random.randint(1, 30) * 10 * level
        A_and_B = random.randint(1,30) * 10 * level
        if A_and_B > min(A,B):
            A_and_B = int(min(A,B)/2)
        A_or_B = int(A+B-A_and_B)
        numbers = range(1, 5)
        option = random.sample(numbers, 4)
        options = list()
        options.append(A)
        options.append(B)
        options.append(A_and_B)
        options.append(A_or_B)
        self.list_of_numbers = list()
        self.list_of_types = list()
        self.answer = 0
        self.type = 0
        counter = 1
        for i in option:
            if counter >= 4:
                self.answer = int(options[i-1])
                self.type = int(i)
            else:
                self.list_of_numbers.append(int(options[i-1]))
                self.list_of_types.append(int(i))
            counter += 1
class ex10():
    def __init__(self, level):
        self.first_number = random.randint(1,100*level)
        self.second_number = random.randint(1,100*level)
        self.third_number = random.randint(1,100*level)
        self.max_number = max(self.first_number, self.second_number, self.third_number)
        self.hex = convert_base(self.first_number, 16,10)
        self.oct = convert_base(self.second_number, 8, 10)
        self.bin = convert_base(self.third_number, 2, 10)

class all_ex():
    def __init__(self,question_numbers, lvl):
        self.ex1_ = None
        self.ex2_ = None
        self.ex3_ = None
        self.ex4_ = None
        self.ex5_ = None
        self.ex6_ = None
        self.ex7_ = None
        self.ex8_ = None
        self.ex10_ = None
        for i in question_numbers:
            if int(i) == 1:
                self.ex1_ = ex1(lvl)
            elif int(i) == 2:
                self.ex2_ = ex2(lvl)
            elif int(i) == 3:
                self.ex3_ = ex3(lvl)
            elif int(i) == 4:
                self.ex4_ = ex4(lvl)
            elif int(i) == 5:
                self.ex5_ = ex5(lvl)
                flag = False
                while (flag != True):
                    self.ex5_ = ex5(lvl)
                    if clean_ex5(self.ex5_):
                        flag = True
            elif int(i) == 6:
                self.ex6_ = ex6(lvl)
            elif int(i) == 7:
                self.ex7_ = ex7()
            elif int(i) == 8:
                self.ex8_ = ex8(lvl)
            elif int(i) == 9:
                self.ex10_ = ex10(lvl)
            else:
                pass

