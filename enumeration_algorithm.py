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


findit = 0 # ФЛАГ ТОГО, ЧТО НАШЛИ ПОЛИНОМ
allvecs = []
resfinpol = 0
vec = 12120201210222021000210220
vec = 12120201         # 121202012 
#vec = 3010
vec = 120
vec = 100
vec = 200
vec = 121202012
print("Введите вектор значения : ")
vec = int(input())
#vec = 102021120
#vec = 120211102
klog = 3 # указывается величина многозначной логики
n = 2 # указывается число переменных
itogpol = 0 # ФИНАЛЬНЫЙ ПОЛИНОМ

tekpol = 10 ** (2 * n) # сразу приступаемк к кф = 1 а не 0
tekpoldec = to10ss(tekpol, klog) # в десятеричной
allpols = []
ourlen = 1 # длина
while True:
    tekpoldec = tekpoldec + 1
    tekpol = from10ss(tekpoldec, klog)   # РЕАЛИЗАЦИЯ СУММИРОВАНИЯ НА 1 И ПЕРЕВОДА В K СС

#    print(tekpol)  # для проверки - текущий полином 

    if tekpol == 10 ** (2 * n + 1): # n - число переменных,1 - это коэффициент
        break # тут переход на новую длину - можно просто continue и далее уже стройка (?)

    thisvec = int(veccalc(str(tekpol), klog, n, ourlen))   # ОБЯЗАТЕЛЬНО !!!!!!! ПРОВЕРИТЬ РАБОТОСПОСОБНОСТЬ!!!
    if checkvec(allvecs, thisvec) == 0:
        allvecs.append(thisvec)
        allpols.append(tekpol)
        if thisvec == vec:
            print("Полином длины 1 = ", tekpol)
            if itogpol == 0:
                itogpol = tekpol
            findit = 1
            resfinpol = tekpol


    # НОВЫЕ ПОЛИНОМЫ СТРОЯТСЯ ДЛИНЫ УЖЕ БОЛЬШЕЙ - СОБИРАЕТСЯ ИЗ ПРЕДЫДУЩЕГО

    # ПРАВИЛА ДЛЯ N = 4: - ЕСТЬ В ТЕКСТЕ

ourlen = ourlen + 1
print("AFTER ETAP 1")
print()
print("Все минимальные полиномы = ", allpols)
print()
print("Все вектора = ", allvecs)
print("Длина полиномов на 1 этапе = ", ourlen)
print("next step -------------------")
etap1 = len(allpols)
cntalarm = 0
print("ETAP1 = ", etap1)

# СЛЕДУЮЩИЙ ЭТАП! - СКЛАДЫВАНИЕ ПОЛИНОМОВ
for i in range (0, etap1 - 1):
    for j in range (i + 1, etap1):
        newpol = int(str(allpols[i]) + str(allpols[j]))
        thisvec = int(veccalc(str(newpol), klog, n, ourlen))  
        if checkvec(allvecs, thisvec) == 0:
            allvecs.append(thisvec)
            allpols.append(newpol)
            if thisvec == vec:
                print("Полином длины 2 = ", newpol)
                findit = 1
                resfinpol = newpol # полином данной длинны
                if itogpol == 0:
                    itogpol = newpol # итоговой минимамальной длины
        cntalarm = cntalarm + 1
    if cntalarm > 1000000: # or findit == 1:
        break

print("AFTER ETAP 2")
print()
print("Все минимальные полиномы = ", allpols)
print()
print("Все вектора = ", allvecs)
print("Длина полиномов на 2 этапе = ", ourlen)
print("next step -------------------")
ourlen = ourlen + 1

countfordig = 0 #  БУДЕТ УВЕЛИЧИВАТЬСЯ ПРИ КАЖДОМ УВЕЛИЧЕНИИ ИТЕРАТОРА - ТО ЧИСЛО, КОТОРОЕ СО СТАРТА ПРОПУСКАЕМ
countfordigs = []
countfordigs.append(0) # запоминаем первый countfordig, равный нулю
countfordig = ourlen
etap2 = len(allpols) 
itt = 0
cntalarm = 0
print("Paramters etap 1 = ", etap1, " etap2 = ", etap2)
for i in range (etap1, etap2 - 1):
    itt = itt + 1
    for j in range(countfordig, etap1 - 1):    
        newpol = int(str(allpols[i]) + str(allpols[j]))
        thisvec = int(veccalc(str(newpol), klog, n, ourlen))
        if checkvec(allvecs, thisvec) == 0:
            allvecs.append(thisvec)
            allpols.append(newpol)
            if thisvec == vec:
                print("Полином длины 3 = ", newpol)
                findit = 1
                resfinpol = newpol
                if itogpol == 0:
                    itogpol = newpol
            cntalarm = cntalarm + 1
    countfordig = countfordig + 1
    if i + 1 != etap2 - 1: # следующий - не пустой, существует
        if str(allpols[i+1])[-5:] < str(allpols[i])[-5:]: # вернулись на новый этап
            for jjj in range(0, etap1 - 1):
                if str(allpols[jjj]) == str(allpols[i+1])[-5:]:
                    countfordig = jjj + 1
        
    if cntalarm > 150000000: # or findit == 1:
        break

print("AFTER ETAP 3")
print()
print("Все минимальные полиномы = ", allpols)
print()
print("Все вектора = ", allvecs)
print("Длина полиномов на 3 этапе = ", ourlen)
print("next step -------------------")

ourlen = ourlen + 1

etaps = []
etaps.append(etap1)
etaps.append(etap2)
etaps.append(len(allpols))
print("Количество неэквивалентных минимальных полиномов, не превышиющих даннцую длину = ", etaps)

cntalarm = 0
print("NOW OURLEN = ", ourlen)
while ourlen < klog ** n + 1: 
    countfordig = ourlen
    etapwas = etaps[ourlen - 3] 
    etapnow = etaps[ourlen - 2]
#    print("ETAPWAS = ", etapwas, "ETAPNOW = ", etapnow, "OURLEB BOW = ", ourlen, " NOW ETAPS = ", etaps)
    print(" Переход на новый этап с длиной = ", ourlen)
    for i in range (etapwas, etapnow - 1):
        itt = itt + 1
        for j in range(countfordig, etap1 - 1):     
            newpol = int(str(allpols[i]) + str(allpols[j]))
            thisvec = int(veccalc(str(newpol), klog, n, ourlen))
            if checkvec(allvecs, thisvec) == 0:
                allvecs.append(thisvec)
                allpols.append(newpol)
                if thisvec == vec:
                    print("Полином длины ", ourlen, "= ", newpol)
                    findit = 1
                    resfinpol = newpol
                    if itogpol == 0:
                        itogpol = newpol
                    #break                
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


print("NOW FINPOL = ", itogpol)



#print("NOW FINPOL = ", newpol)
