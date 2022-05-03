### ШАГ 0 - ФУНКЦИИ ЛЯ ДАЛЬНЕЙШЕЙ РАБОТЫ
def from10ss(x, ss):
    t = 1
    d = 0
    while x > 0:
        d = d + (x % ss) * t
        t = t * 10
        x = x // ss
    return d

def to10ss(x, ss):
    r = 0
    d = 0
    while x > 0:
        d = d + x % 10 * ss ** r
        r += 1
        x //= 10
    return d

def checkvec(vecs, thisvec):
    for jj in range(0, len(vecs)):
        if thisvec == vecs[jj]:
            return 1
    return 0

def veccalc(pol, klog, n, itlen):
    strit = ''
    for i in range(0, klog ** n):
        a4 = from10ss(i, klog)
        a = []
        for jj in range (0, n):
            a.append(0)
        for tt in range(0, n - len(str(a4))):
            a[tt] = 0
        tt2 = 0
        for tt in range(n - len(str(a4)), n):
            a[tt] = int(str(a4)[tt2])
            tt2 = tt2 + 1
        bufn = 1
        itpol = 0
        ww = 0 # отвечают за индексацию в мономе
        for rr in range(0, itlen):
            bufn = 1
            kf = int(pol[ww])
            ww = ww + 1
            for kk in range (0, n):
                sch = int(pol[ww]) # свободный член
                dig = int(pol[ww + 1]) # степень
                thisetap = (a[kk] + sch) ** dig % klog # вычисляем значение скобки
                ww = ww + 2
                bufn = bufn * thisetap % klog
            bufn = bufn * kf % klog
            itpol = (itpol + bufn) % klog
        strit = strit + str(itpol)
    return strit

def calcpolpereb(vec, klog, n):
    findit = 0 # ФЛАГ ТОГО, ЧТО НАШЛИ ПОЛИНОМ
    allvecs = []
    resfinpol = 0
    tekpol = 10 ** (2 * n) # сразу приступаемк к кф = 1 а не 0
    tekpoldec = to10ss(tekpol, klog)
    allpols = []
    ourlen = 1 # длина
    while True:
        tekpoldec = tekpoldec + 1
        tekpol = from10ss(tekpoldec, klog)   # РЕАЛИЗАЦИЯ СУММИРОВАНИЯ НА 1 И ПЕРЕВОДА В ДРУГУЮ СС

        if tekpol == 10 ** (2 * n + 1):
            break 

        thisvec = int(veccalc(str(tekpol), klog, n, ourlen))  
        if checkvec(allvecs, thisvec) == 0:
            allvecs.append(thisvec)
            allpols.append(tekpol)
            if thisvec == vec:
                findit = 1
                resfinpol = tekpol
                return tekpol


    ourlen = ourlen + 1
    etap1 = len(allpols)
    cntalarm = 0
    itersforpols = [] 
    for i in range (0, etap1 - 1):   
        for j in range (i + 1, etap1):
            newpol = int(str(allpols[i]) + str(allpols[j]))
            thisvec = int(veccalc(str(newpol), klog, n, ourlen)) 
            if checkvec(allvecs, thisvec) == 0:
                allvecs.append(thisvec)
                allpols.append(newpol)
                if thisvec == vec:
                    return newpol
                    findit = 1
                    resfinpol = newpol
            cntalarm = cntalarm + 1
        itersforpols.append(len(allpols))
        if cntalarm > 100000 or findit == 1:
            break

    ourlen = ourlen + 1

    countfordig = 0 
    etap2 = len(allpols) 
    itt = 0
    cntalarm = ourlen
    for i in range (etap1, etap2 - 1):
        itt = itt + 1
        for j in range(countfordig, etap1 - 1):  
            newpol = int(str(allpols[i]) + str(allpols[j]))
            thisvec = int(veccalc(str(newpol), klog, n, ourlen))
            if checkvec(allvecs, thisvec) == 0:
                allvecs.append(thisvec)
                allpols.append(newpol)
                if thisvec == vec:
                    return newpol
                    findit = 1
                    resfinpol = newpol
                cntalarm = cntalarm + 1
        countfordig = countfordig + 1
        if i + 1 != etap2 - 1: # следующий - не пустой, существует
            if str(allpols[i+1])[-5:] < str(allpols[i])[-5:]: # вернулись на новый этап
                for jjj in range(0, etap1 - 1):
                    if str(allpols[jjj]) == str(allpols[i+1])[-5:]:
                        countfordig = jjj + 1
        if cntalarm > 15000 or findit == 1:
            break

    ourlen = ourlen + 1

    etaps = []
    etaps.append(etap1)
    etaps.append(etap2)
    etaps.append(len(allpols))

    cntalarm = 0
    while ourlen < klog ** n + 1: 
        countfordig = ourlen
        etapwas = etaps[ourlen - 3] 
        etapnow = etaps[ourlen - 2]
        for i in range (etapwas, etapnow - 1):
            itt = itt + 1
            for j in range(countfordig, etap1 - 1):     
                newpol = int(str(allpols[i]) + str(allpols[j]))
                thisvec = int(veccalc(str(newpol), klog, n, ourlen))
                if checkvec(allvecs, thisvec) == 0:
                    allvecs.append(thisvec)
                    allpols.append(newpol)
                    if thisvec == vec:
                        findit = 1
                        resfinpol = newpol
                        break                
                    cntalarm = cntalarm + 1
            countfordig = countfordig + 1
            if i + 1 != etap2 - 1: # следующий - не пустой, существует
                if str(allpols[i+1])[-5:] < str(allpols[i])[-5:]: # вернулись на новый этап
                    for jjj in range(0, etap1 - 1):
                        if str(allpols[jjj]) == str(allpols[i+1])[-5:]:
                            countfordig = jjj + 1
            if cntalarm > 200000 or findit == 1:
                break
        ourlen = ourlen + 1
        etaps.append(len(allpols))
        if findit == 1:
            break
        
    return newpol


####
#### ШАГ 1. ИЩЕМ ВЕКТОР ЗНАЧЕНИЙ ДЛЯ ВВЕЕДЁНОГО ПОЛИНОМА


n = 1
klog = 3
ruchnpol = '(x1+1)^1*(x2^2+2)+(x1+1)^1*(x2+2)^3'
ruchnpol = '(x1+1)^2+(x1+1)^3)'
ruchnpol = '(x1+1)^2+(x1+3)^2'
ruchnpol = '(x1+0)^2+(x1+1)^2'
ruchnpol = '(x1+0)^1+(x1+2)^2'
ruchnstr = ''
gg = 0
while gg < len(ruchnpol):
    if ruchnpol[gg] == '(':
        if gg == 0:
            kf = 1
            ruchnstr = ruchnstr + str(kf)  
        elif ruchnpol[gg-1] == '+':
            kf = 1
            ruchnstr = ruchnstr + str(kf)  
        elif ruchnpol[gg-1] != '*':
            kf = int(ruchnpol[gg-1])
            ruchnstr = ruchnstr + str(kf)
        gg = gg + 1
        continue
    elif ruchnpol[gg] == 'x':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        delkh = kh // (1 + 2 * n) # делитель - промежуточно значение, чтобы знать сколько скобок прошлиэ
        for rr in range(len(ruchnstr), delkh * (1 + 2 * n) + 1 + (int(zn) - 1) * 2): # от последнего текущего значения (допустим 16) до ненулевого (допустим 18) - т.е. тут будет 2 доп нуля
            ruchnstr = ruchnstr + '0'  # вместо недостоющих значений пишем нули
        gg = gg + 2
        
    elif ruchnpol[gg] == '+' and ruchnpol[gg+1] != '(':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        ruchnstr = ruchnstr + zn  # вместо недостоющих значений пишем нули
        gg = gg + 3

    elif ruchnpol[gg] == '^':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        ruchnstr = ruchnstr + zn  # вместо недостоющих значений пишем нули
        gg = gg + 2
    else:
        gg = gg + 1
    


itlen = (int(len(ruchnstr))) // (1 + 2 * n)
print(ruchnstr, " itlen = ", itlen)
pol = ruchnstr
strit = ''
#pol = input()
#vec = input()
#klog = 4
#n = 2
for i in range(0, klog ** n):
    a4 = from10ss(i, klog)
    a = []
    for jj in range (0, n):
        a.append(0)
    for tt in range(0, n - len(str(a4))):
        a[tt] = 0
    tt2 = 0
    for tt in range(n - len(str(a4)), n):
        a[tt] = int(str(a4)[tt2])
        tt2 = tt2 + 1
    kf = int(pol[0])
    bufn = 1
    ww = 0 # отвечают за индексацию в мономе
    bufn = 1
    itpol = 0
    ww = 0 # отвечают за индексацию в мономе
    for rr in range(0, itlen):
        bufn = 1
        kf = int(pol[ww])
        ww = ww + 1
        for kk in range (0, n):
            sch = int(pol[ww]) # свободный член
            dig = int(pol[ww + 1]) # степень
            thisetap = (a[kk] + sch) ** dig % klog # вычисляем значение скобки
            ww = ww + 2
            bufn = bufn * thisetap % klog
            if (i == 5):
                print("dig = ", dig, " sch = ", " thisetap = ", thisetap, " bufn = ", bufn)
        bufn = bufn * kf % klog
        itpol = (itpol + bufn) % klog
    strit = strit + str(itpol)
    
print(strit)


### ШАГ 2 - ПОДАЁМ ВЕКТОР НА ВХОД СЛЕДУЮЩЕЙ ПРОГРАММЕ

s = klog ** (n - 1)
nowpol = calcpolpereb(int(strit), klog, n)
# print("NOW POL = ", nowpol)   # ЦЕЛЬ НАЙТИ ТАКИЕ ПОЛИНОМЫ ДЛЯ ВСЕХ СУММ ДЛИНЫ 2


tekpol = 10 ** (2 * n) # сразу приступаемк к кф = 1 а не 0
tekpoldec = to10ss(tekpol, klog) # в десятеричной
odinipolvecs = [] 
odinipols = []
ourlen = 1
while True:
    tekpoldec = tekpoldec + 1
    tekpol = from10ss(tekpoldec, klog)   
    if tekpol == 10 ** (2 * n + 1):
        break
    else:
        lennowpol = len(str(tekpol)) # для вычисления текущей "длины одночлена"
        itforlen = 1
        gotonext = 0
        while itforlen < lennowpol:
            if str(tekpol)[itforlen] != '1' and str(tekpol)[itforlen + 1] == '0':
                gotonext = 1
                break
            else:
                itforlen = itforlen + 2
        if gotonext == 0:           # исключаем из рассмотрения повторяющиеся нулевые степени
            odinipols.append(tekpol)   
        else:
            continue

    thisvec = int(veccalc(str(tekpol), klog, n, ourlen))
    odinipolvecs.append(thisvec)

print("Полиномы длины 1: ", odinipols)
print("Вектора, реализ. полиомами длины 1 ", odinipolvecs)

step2polssum = []
step2polsfind = []
step2tozhds = []
for kkk in range(len(odinipols) - 1):
    for ttt in range(kkk + 1, len(odinipols)):
        pol = str(odinipols[kkk]) + str(odinipols[ttt])
        step2polssum.append(pol)
        strit = ''
        for i in range(0, klog ** n):  
            a4 = from10ss(i, klog)
            a = []
            for jj in range (0, n):
                a.append(0)
            for tt in range(0, n - len(str(a4))):
                a[tt] = 0
            tt2 = 0
            for tt in range(n - len(str(a4)), n):
                a[tt] = int(str(a4)[tt2])
                tt2 = tt2 + 1
            kf = int(pol[0])
            bufn = 1
            ww = 0 # отвечают за индексацию в мономе
            bufn = 1
            itpol = 0
            ww = 0 # отвечают за индексацию в мономе
            for rr in range(0, itlen):
                bufn = 1
                kf = int(pol[ww])
                ww = ww + 1
                for kk in range (0, n):
                    sch = int(pol[ww]) # свободный член
                    dig = int(pol[ww + 1]) # степень
                    thisetap = (a[kk] + sch) ** dig % klog # вычисляем значение скобки
                    ww = ww + 2
                    bufn = bufn * thisetap % klog
                bufn = bufn * kf % klog
                itpol = (itpol + bufn) % klog
            strit = strit + str(itpol)

        s = klog ** (n - 1)
        nowpol = calcpolpereb(int(strit), klog, n)
        step2polsfind.append(nowpol)
        findsmaller = int(pol)
        for itz in range(len(odinipolvecs)):
            if int(strit) == odinipolvecs[itz]:
                findsmaller = odinipols[itz] # ставим в соответствие тому двойному полиному полином длины меньшей
        step2tozhds.append(findsmaller)

print("Начальные полиномы = ", step2polssum)
print("Минимальные полиномы = ", step2tozhds)


        # АЛГОРИТМ
        # КАК ПОЛЬЗОВАТЬСЯ - ИЩЕМ В step2polssum, ТО ЧТО НУЖНО - ИЩЕМ АНАЛОГ В step2polsfind - ЕСЛИ НАХОДИМ, ВСЁ ОК - СОКРАЩАЕМ, ИНАЧЕ ПРОПУСКАЕМ И ДАЛЬШЕ ИЩЕМ
        # ШАГ 2 - ИСКАТЬ ВСЕ ПОЛИНОМЫ ДЛЯ ДАННОГО ВЕКТОРА И ОСТАВЛЯТЬ "НОРМИРОВАННЫЙ" - НАПРИМЕР, ГДЕ 0 СТЕПЕНЬ, ИЛИ 0 - СВОБОДНЫЙ ЧЛЕН
        # ШАГ 3 - ПОСЛЕ ВСЕХ СОКРАЩЕНИЙ ПОВТОРИТЬ ПОИСК


### ТЕСТ НАПИСАННОГО СОКРАЩЕНИЯ


n = 2
klog = 3
ruchnpol = '(x1+1)^1*(x2^2+2)+(x1+1)^1*(x2+2)^3'
ruchnpol = '(x1+1)^2+(x1+1)^3)'
ruchnpol = '(x1+1)^2+(x1+3)^2'
ruchnpol = '(x1+0)^2+(x1+1)^2'
ruchnpol = '(x1+0)^1+(x1+2)^2'
ruchnpol = '(x1+1)^1*(x2^2+2)+2*(x1+1)^1*(x2+2)^1'
ruchnpol = '(x1+1)^1*(x2+2)^2+1*(x1+1)^1*(x2+0)^1'
#ruchnpol = '(x1+1)^1*(x2+2)^2+1*(x1+1)^1*(x2+2)^2'
ruchnpol = '(x1+1)^1*(x2+0)^1+1*(x1+1)^1*(x2+1)^2'
ruchnpol = '(x1+2)^2*(x2+2)^2+1*(x1+0)^1*(x2+2)^2'
ruchnpol = '(x1+2)^2*(x2+1)^2+2*(x1+2)^2*(x2+2)^2'
ruchnpol = '(x1+2)^2*(x2+1)^2+2*(x1+2)^2*(x2+2)^2+(x1+0)^1*(x2+0)^1'
# В РУЧНПОЛ МОЖНО ЗАДАТЬ ВРУЧНУЮ НУЖНЫЙ ПОЛИНОМ
#ruchnpol = input()
print(" Входной полином: (x1+2)^2*(x2+1)^2+2*(x1+2)^2*(x2+2)^2+(x1+0)^1*(x2+0)^1 ")
ruchnstr = ''
gg = 0
while gg < len(ruchnpol):
    if ruchnpol[gg] == '(':
        if gg == 0:
            kf = 1
            ruchnstr = ruchnstr + str(kf)  
        elif ruchnpol[gg-1] == '+':
            kf = 1
            ruchnstr = ruchnstr + str(kf)  
        elif ruchnpol[gg-1] != '*':
            kf = int(ruchnpol[gg-1])
            ruchnstr = ruchnstr + str(kf)
        gg = gg + 1
        continue
    elif ruchnpol[gg] == 'x':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        delkh = kh // (1 + 2 * n) # делитель - промежуточно значение, чтобы знать сколько скобок прошлиэ
        for rr in range(len(ruchnstr), delkh * (1 + 2 * n) + 1 + (int(zn) - 1) * 2): # от последнего текущего значения (допустим 16) до ненулевого (допустим 18) - т.е. тут будет 2 доп нуля
            ruchnstr = ruchnstr + '0'  # вместо недостоющих значений пишем нули
        gg = gg + 2
        
    elif ruchnpol[gg] == '+' and ruchnpol[gg+1] != '(':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        ruchnstr = ruchnstr + zn  # вместо недостоющих значений пишем нули
        gg = gg + 3

    elif ruchnpol[gg] == '^':
        zn = ruchnpol[gg+1]     
        kh = len(ruchnstr)
        ruchnstr = ruchnstr + zn  # вместо недостоющих значений пишем нули
        gg = gg + 2
    else:
        gg = gg + 1

itlen = (int(len(ruchnstr))) // (1 + 2 * n)
#print(ruchnstr, " itlen = ", itlen)

monns = []
bufruchn = ruchnstr
ith = 0
while ith < len(bufruchn):
    itmon = bufruchn[ith : (ith + (1+ 2 * n))]
    monns.append(itmon)
    ith = ith + (1+ 2 * n)
#print(monns)
# ДАЛЕЕ - ФОРМИРУЕМ ДВУМЕРНЫЙ МАССИВ ИЗ КАЖДОЙ СКОБКИ. ИДЁМ ПО ПОЛИНОМУ И СВЕРЯЕМ В КАЖДОМ МОНОМЕ ЧИСЛО ОДИНАКОВЫХ. ЕСЛИ ЧИСЛО ОТЛИЧАЕТСЯ НА ЕДИНИЦУ - СОКРАЩАЕМ, ИНАЧЕ ИДЁМ ДАЛЬШЕ
brackets = [[0] * (n + 1) for i in range(itlen)]
for ii in range (0, itlen):
    for jj in range(0, n + 1):
        if jj == 0:
            brackets[ii][jj] = monns[ii][jj]
        else:
            brackets[ii][jj] = monns[ii][2 * jj - 1 : 2 * jj + 1]
print("Изначальные скобки = ", brackets)
delmons = []  # мономы, которые будут убраны - сокращены
itbr = 0
itb2 = 0
bufflen = itlen
while itbr < bufflen - 1:
    tobegin = 0
    if brackets[itbr][0] == '0': # значит, что занулённый
        itbr = itbr + 1
        continue
    itb2 = itbr + 1
    while itb2 < bufflen:
        tobeginpt2 = 0
        if brackets[itb2][0] == '0': # значит, что занулённый
            itb2 = itb2 + 1
            continue
#        print("itbr = ", itbr, "itb2 = ", itb2)
        countravn = 0
        disravninds = []
        newpol = ''
        for hh in range(1, n + 1):  # С 1 - т.к. целенаправленно игнорируем кф (см модификацию алгоритма)
            if brackets[itbr][hh] == brackets[itb2][hh]:
                countravn = countravn + 1
            else:
                disravninds.append(hh)
        # кейс - когда все равны
        if countravn == n:
            a = int(brackets[itbr][0])
            b = int(brackets[itb2][0])
            sumab = (a + b) % klog
            newpol = str(sumab) + str(brackets[itbr])[1:]  
            delmons.append(itbr)
            delmons.append(itb2)
            # зануляем старые, добавляем новые
            brackets[itbr][0] = '0'
            brackets[itb2][0] = '0' # зануляем оба
            if sumab != 0: # ЕСЛИ РАВНО 0 - ничего не делаем - не вносим
                newbr = []
                newbr.append(str(sumab))
                for itbbrit in range(1, len(brackets[itb2])):
                    newbr.append(brackets[itbr][itbbrit])
                brackets.append(newbr)
                # далее подчёркиваем, что начинаем сначала
                itbr = 0
                itb2 = 0
                tobegin = 1
                bufflen = bufflen + 1
        # далее кейс - когда равны оказались все, кроме одного, 
        elif countravn == n - 1:
            if 1 == 1: # сразу идём по ветке, когда у нас не совпала именно одна из скобок
                notravn = disravninds[0]
                a = brackets[itbr][notravn]
                b = brackets[itb2][notravn]
                sumab = str(brackets[itbr][0]) + str(brackets[itbr][notravn]) + str(brackets[itb2][0]) + str(brackets[itb2][notravn])
                sumab2 = str(brackets[itb2][0]) + str(brackets[itb2][notravn]) + str(brackets[itbr][0]) + str(brackets[itbr][notravn])
                changeflag = 0 # Флаг того, что мы меняем полином на меньший
                for ittmon in range(0, len(step2polssum)):
                    if step2polssum[ittmon] == sumab or step2polssum[ittmon] == sumab2: # ищем полином в той таблице - и его вносим как небольший
                        chang =  step2tozhds[ittmon]  # замена тем двум мономам
                        if chang != sumab and chang != sumab2:
                            changeflag = 1
                        break
                ### ДАЛЕЕ ТА САМАЯ СУММА ДВУХ
                findless = 0
                if len(str(chang)) < len(str(sumab)): # ПОЛУЧИЛИ МЕНЬШЕ
                    if notravn == n: 
                        newpol = ''
                        newkf = str(chang)[0]
                        for itst in range(0, notravn):
                            newpol = newpol + brackets[itbr][itst]
                        newpol = newpol + str(chang)[1:]
                    else:
                        newpol = ''
                        newkf = str(chang)[0]
                        for tttt in range(0, notravn):
                            newpol = newpol + str(brackets[itbr][tttt])
                        newpol = newpol + str(chang)[1:]
                        for tttt in range(notravn + 1, n + 1):
                            newpol = newpol + str(brackets[itbr][tttt])
#                    print("HERE NEWPOL = ", newpol)
                    delmons.append(itbr)
                    delmons.append(itb2)
                    waskf = str(brackets[itbr][0]) # БУФЕР ДЛЯ КОЭФФИЦИЕНТА
                    brackets[itbr][0] = '0'
                    brackets[itb2][0] = '0' # зануляем оба
                    if sumab != 0: # ЕСЛИ РАВНО 0 - ничего не делаем - не вносим
                        newbr = []
                        newbr.append(newkf)
                        for itbbrit in range(0, len(str(newpol)) // 2):
                            newbr.append(str(newpol)[1 + 2 * itbbrit : 1 + 2 * itbbrit + 2])
                        brackets.append(newbr)
                        # далее подчёркиваем, что начинаем сначала
                        itbr = 0
                        itb2 = 0
                        tobegin = 1
                        bufflen = bufflen + 1
                else: # ВТОРОЙ СЛУЧАЙ - БУДЕТ НЕСКОЛЬКО ОДНОЧЛЕНОВ
                    if changeflag == 0: # мы ничего не поменяли, - просто уходим
                        itb2 = itb2 + 1
                        continue
                    # ЕСТЬ ЗАМЕНА - МЕНЯЕМ
                    lenchang = len(chang)
                    chang1 = chang[0: lenchang // 2]
                    chang2 = chang[(lenchang // 2) : lenchang]
                    if notravn == n:
                        newkf1 = str(chang1)[0]
                        newkf2 = str(chang2)[0]
                        newpol1 = newkf1
                        newpol2 = newkf2
                        for itst in range(1, notravn):
                            newpol1 = newpol1 + brackets[itbr][itst]
                            newpol2 = newpol2 + brackets[itbr][itst]
                        newpol1 = newpol1 + str(chang1)[1:]   ###ТУТ ТОЖЕ ВЫДЕЛЯЕТ НУЖНОЕ И ЗАМЕНЁННОЕ
                        newpol2 = newpol2 + str(chang2)[1:]   ###ТУТ ТОЖЕ ВЫДЕЛЯЕТ НУЖНОЕ И ЗАМЕНЁННОЕ
                    else:
                        newkf1 = str(chang1)[0]
                        newkf2 = str(chang2)[0]
                        newpol1 = newkf1
                        newpol2 = newkf2
                        for tttt in range(1, notravn):
                            newpol1 = newpol1 + str(brackets[itbr][tttt])
                            newpol2 = newpol2 + str(brackets[itbr][tttt]) # Одинаковая часть
                        newpol1 = newpol1 + str(chang1)[1:]
                        newpol2 = newpol2 + str(chang1)[1:]
                        for tttt in range(notravn + 1, n + 1):
                            newpol1 = newpol1 + str(brackets[itbr][tttt])
                            newpol2 = newpol2 + str(brackets[itbr][tttt])
#                    print("HERE NEWPOL1 = ", newpol1, " NEWPOL2 = ", newpol2)
                    delmons.append(itbr)
                    delmons.append(itb2)
                    waskf = str(brackets[itbr][0]) # БУФЕР ДЛЯ КОЭФФИЦИЕНТА
                    brackets[itbr][0] = '0'
                    brackets[itb2][0] = '0' # зануляем оба
                    if sumab != 0: # ЕСЛИ РАВНО 0 - ничего не делаем - не вносим
                        newbr1 = []
                        newbr2 = [] # учитываем, что длина у newpol1 и Newpol2 - SAME
                        newbr1.append(newkf1)
                        newbr2.append(newkf2)
                        for itbbrit in range(0, len(str(newpol1)) // 2):
                            newbr1.append(str(newpol1)[1 + 2 * itbbrit : 1 + 2 * itbbrit + 2])
                            newbr2.append(str(newpol2)[1 + 2 * itbbrit : 1 + 2 * itbbrit + 2])
                        brackets.append(newbr1)
                        brackets.append(newbr2)
                        # далее подчёркиваем, что начинаем сначала
                        itbr = 0
                        itb2 = 0
                        tobegin = 1
                        bufflen = bufflen + 2
#                print("После шага скобки в виде = ", brackets)

                #else:   # !!! ВОЗМОЖНО, ИМЕННО ТУТ СТОИТ РАССМОТРЕТЬ ПРИВЕДЕНИЕ К КАНОН ВИДУ. ТО ЕСТЬ - ЕСЛИ СУММА ПРОШЛАЯ ОТЛИЧАЕТСЯ ОТ НОВОЙ, МЕНЯЕМ
                     
        itb2 = itb2 + 1
        if tobegin == 1:
            itbr = 0
            break   # возвращаемся в начало

    itb2 = 0
    itbr = itbr + 1
                
            # ЕСЛИ ВНЕСЛИ ПЕРЕЕЗАПУСКАЕМ АЛГОРИТМ - ОПЯТЬ С 1 ПО УЖЕ НОВЫЙ ЭЛЕМЕНТ ИЩЕМ. СТАРЫЙ - УДАЛЯЕМ
            
                # занесённое сверяем далее с другим элементом (сначала)

finpol = ''
for finm in range(0, len(brackets)):
#    print("HERE: brackets[finm])[0] = ", str(brackets[finm][0]))
    if str(brackets[finm][0]) != '0':
        for kmas in range (0, len(brackets[finm])):            
            finpol = finpol + brackets[finm][kmas]

print("Финльный полином = ", finpol)



# ДАЛЬШЕ ЦЕЛЬ - ПРОВЕРИТЬ И ДОБАВИТЬ ВОЗМОЖНОСТЬ ИДТИ НЕ ТОЛЬКО ПО ЕДИНИЦЕ, НО И ПО РАЗНЫМ КФ + ПРОВЕРКА
