import sys

header = sys.stdin.readline()

for line in sys.stdin:
    line = line.strip()  # 개행 제거
    title, genre, year = line.split(".")
    print(f"제목: {title}, 장르: {genre}, 연도: {year}")
