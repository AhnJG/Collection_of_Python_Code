import re

def reduce_consecutive_newlines(filename):
    # 파일 읽기
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # 연속된 두 개 이상의 개행문자를 하나로 줄이기
    reduced_content = re.sub(r'\n{2,}', '\n', content)

    # 결과를 새 파일에 저장
    with open('Result.txt', 'w', encoding='utf-8') as file:
        file.write(reduced_content)

    return reduced_content

# 함수 호출 예시
file_name = 'Original.txt'

result = reduce_consecutive_newlines(file_name)
print(result)
