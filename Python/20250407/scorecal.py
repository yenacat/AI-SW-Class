with open(
    "C:/Users/UserK/projects/github python/20250407/score.csv", "r", encoding="UTF-8"
) as f:
    kor = list()
    eng = list()
    math = list()

    lines = f.readlines()

    for line in lines[1:]:
        line = line.strip()
        num, name, k, e, m = line.split(",")
        kor.append(int(k))
        eng.append(int(e))
        math.append(int(m))

    kor_avg = sum(kor) / len(kor)
    eng_avg = sum(eng) / len(eng)
    math_avg = sum(math) / len(math)
    print(
        f"국어 평균: {kor_avg:.2f}, 영어 평균: {eng_avg:.2f}, 수학 평균: {math_avg:.2f}"
    )
