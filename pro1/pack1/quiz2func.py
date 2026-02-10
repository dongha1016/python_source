def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def processfunc(datas):
    pt = {
        "새우깡": 450,
        "감자깡": 300,
        "양파깡": 350
    }

    qq = {
        "새우깡": 0,
        "감자깡": 0,
        "양파깡": 0
    }
    aa = {
        "새우깡": 0,
        "감자깡": 0,
        "양파깡": 0
    }

    tq = 0
    ta = 0

    print("상품명   수량   단가   금액")
    print("-" * 35)

    for data in datas:
        name, qty = data.split(",")
        qty = int(qty)

        price = pt[name]

        amount = qty * price

        print(f"{name:<6} {qty:<6} {price:<6} {amount}")

        qq[name] += qty
        aa[name] += amount

        tq += qty
        ta += amount

    print("\n소계")
    for name in pt:
        print(f"{name} : {qq[name]}건   소계액 : {aa[name]}원")

    print("\n총계")
    print(f"총 건수 : {tq}")
    print(f"총 액  : {ta}원")


datas = inputfunc()
processfunc(datas)