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
#    print("VEC = ", vec)
    findit = 0 # ФЛАГ ТОГО, ЧТО НАШЛИ ПОЛИНОМ
    allvecs = []
    resfinpol = 0
    tekpol = 10 ** (2 * n) # сразу приступаемк к кф = 1 а не 0
    tekpoldec = to10ss(tekpol, klog)
    allpols = []
    ourlen = 1 # длина
    while True:
        tekpoldec = tekpoldec + 1
        tekpol = from10ss(tekpoldec, klog)

        if tekpol == 10 ** (2 * n + 1): # n - число переменных,1 - это коэффициент
            break # тут переход на новую длину 

        thisvec = int(veccalc(str(tekpol), klog, n, ourlen))  
        if checkvec(allvecs, thisvec) == 0:
            allvecs.append(thisvec)
            allpols.append(tekpol)
            if thisvec == vec:
#                print("Нашли полином = ", tekpol)
                findit = 1
                resfinpol = tekpol
                return tekpol


    ourlen = ourlen + 1
#    print(allpols)
    etap1 = len(allpols) 
    cntalarm = 0
#    print("ETAP1 = ", etap1)
    itersforpols = []  # ЭТО МАССИВ, КУДА СКЛАДИРУЕМ ТЕКУЩУЮ ДЛИНУ В БОЛЬШОМ МАССИВЕ - ИМЕННО С ЭТОЙ ДЛИНЫ БУДЕТ ПЕРЕХОД В СЛОЖЕНИИ НА НОВЫЙ МОНОМ

    # СЛЕДУЮЩИЙ ЭТАП - СУММИРОВАНИЕ ПОЛИНОМОВ
    for i in range (0, etap1 - 1):  
        for j in range (i + 1, etap1):
            newpol = int(str(allpols[i]) + str(allpols[j]))
            thisvec = int(veccalc(str(newpol), klog, n, ourlen)) 
            if checkvec(allvecs, thisvec) == 0:
                allvecs.append(thisvec)
                allpols.append(newpol)
                if thisvec == vec:
#                    print("Нашли полином = ", newpol)
                    return newpol
                    findit = 1
                    resfinpol = newpol
            cntalarm = cntalarm + 1
        itersforpols.append(len(allpols))
        if cntalarm > 100000 or findit == 1:
            break

    ourlen = ourlen + 1

    countfordig = ourlen # БУДЕТ УВЕЛИЧИВАТЬСЯ ПРИ КАЖДОМ УВЕЛИЧЕНИИ ИТЕРАТОРА - ТО ЧИСЛО, КОТОРОЕ СО СТАРТА ПРОПУСКАЕМ
    etap2 = len(allpols) 
    itt = 0
    cntalarm = 0
    for i in range (etap1, etap2 - 1):
        itt = itt + 1
        for j in range(countfordig, etap1 - 1):
            newpol = int(str(allpols[i]) + str(allpols[j]))
            thisvec = int(veccalc(str(newpol), klog, n, ourlen))
            if checkvec(allvecs, thisvec) == 0:
                allvecs.append(thisvec)
                allpols.append(newpol)
                if thisvec == vec:
#                    print("Нашли полином = ", newpol)
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
        if cntalarm > 150000: # or findit == 1:
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
#                        print("Нашли полином = ", newpol)
                        findit = 1
                        resfinpol = newpol
                        if itogpol == 0:
                            itogpol = newpol
                        return newpol             
                    cntalarm = cntalarm + 1
            countfordig = countfordig + 1
            if i + 1 != etap2 - 1: # следующий - не пустой, существует
                if str(allpols[i+1])[-5:] < str(allpols[i])[-5:]:
                    for jjj in range(0, etap1 - 1):
                        if str(allpols[jjj]) == str(allpols[i+1])[-5:]:
                            countfordig = jjj + 1
            if cntalarm > 200000: # or findit == 1:
                break
        ourlen = ourlen + 1
        etaps.append(len(allpols))
        if findit == 1:
            break
        
    return newpol





functest = '012102210' # тестовый вектор
klog = 3
n = 2
podvec = []
s = klog ** (n - 1)
#print(functest[0 * s : 1 * s])
for p in range(0, klog):
    podvec.append(functest[s * p : s * (p+1)])
print(podvec)
    
podpols = []
for r in range(0, klog):
    nowpodpol = calcpolpereb(int(podvec[r]), klog, n-1)
    podpols.append(nowpodpol)
print("podpols = ", podpols)

pereklad = 1
mnozh = []
for tt in range(0, klog):
    pereklad = 10 ** (klog - tt - 1)
    nowpodmnozh = calcpolpereb(pereklad, klog, 1)
    mnozh.append(nowpodmnozh)
print("mnozh = ", mnozh)
# ДАЛЬШЕ ИДЁТ ПЕРЕМНОЖЕНИЕ

# ПЕРЕМНОЖЕНИЕ
afterodns = []
for ss in range(0, klog):
    razbor1 = []  # тут именно одночлнены полинома - подвектора
    razbor2 = []  # тут именно одночлнены полинома - множителя
    lenpol = len(str(podpols[ss]))
    reallenpol = lenpol // (1 + 2 ** (n - 1))
    uu = 0
    while uu < lenpol:
        hereodn = str(podpols[ss])[uu : (1 + 2 ** (n - 1)) + uu]
        uu = uu + (1 + 2 ** (n - 1))
        razbor1.append(hereodn)

    lenmnozh = len(str(mnozh[ss]))
    reallenmnozh = lenmnozh // (1 + 2 ** (n - 1))
    uu = 0
    while uu < lenmnozh:
        heremnozh = str(mnozh[ss])[uu : (1 + 2 ** (n - 1)) + uu]
        uu = uu + (1 + 2 ** (n - 1))
        razbor2.append(heremnozh)
    print("razbor1 = ", razbor1)
    print("razbor2 = ", razbor2)
    for rrr in range(0, len(razbor1)):
        for www in range(0, len(razbor2)):
            kf1 = razbor1[rrr][0] # коэф в одночлене
            kf2 = razbor2[www][0] # коэф в множителе
            kfn = int(kf1) * int(kf2) % klog # общий кф
            bufthisodn = str(kfn) + razbor2[www][1:] + razbor1[rrr][1:]
            afterodns.append(bufthisodn)

print("Одночлены в полученном полиноме = ", afterodns)

