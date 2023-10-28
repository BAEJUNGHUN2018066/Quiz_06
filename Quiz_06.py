num =input("주민등록번호를 입력하세요.")

sum =int(num[0])*2 + int(num[1])*3 + int(num[2])*4 + int(num[3])*5 + int(num[4])*6 + int(num[5])*7 + int(num[7])*8 + int(num[8])*9 + int(num[9])*2 +int(num[10])*3 + int(num[11])*4 + int(num[12])*5
final_result = 11-(sum % 11)
final_result = str(final_result)

if final_result[-1] == num[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")




