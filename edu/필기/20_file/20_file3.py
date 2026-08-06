import os
import csv

csv_path = os.path.join("edu", "data", "result.csv")

# newline=""을 입력해 빈 줄 생기는거 방지
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])  # 리스트로 넣어줘야한다.
    writer.writerow(["09:00", "PUMP-01"])
