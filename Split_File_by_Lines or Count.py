# Split .txt file by lines or count 


# Split file by lines
def split_file_by_lines(input_file, lines_per_file=1000):
    """텍스트 파일을 지정된 줄 수에 따라 여러 개의 파일로 분할합니다."""
    file_number = 1
    line_number = 1
    
    # 원본 파일명에서 확장자 분리
    file_base_name, file_ext = input_file.rsplit('.', 1) if '.' in input_file else (input_file, '')
    if file_ext:
        file_ext = '.' + file_ext
    
    # 원본 파일 열기
    with open(input_file, 'r', encoding='utf-8') as in_file:
        # 첫 번째 출력 파일 생성
        output_file_name = f"{file_base_name}_{file_number}{file_ext}"
        out_file = open(output_file_name, 'w', encoding='utf-8')
        
        # 라인별로 파일 읽기
        for line in in_file:
            out_file.write(line)
            line_number += 1
            
            # 지정된 줄 수에 도달하면 새 파일 생성
            if line_number > lines_per_file:
                out_file.close()
                file_number += 1
                line_number = 1
                output_file_name = f"{file_base_name}_{file_number}{file_ext}"
                out_file = open(output_file_name, 'w', encoding='utf-8')
        
        # 마지막 파일 닫기
        out_file.close()
    
    print(f"{input_file}을(를) {file_number}개의 파일로 분할했습니다.")

# 사용 예시
file_name = 'File Name.txt'
split_file_by_lines(file_name, 5000)  # 각 파일당 5000줄씩 분할


# Split file by count
import math

def split_file_by_count(input_file, max_files=5):
    """텍스트 파일을 지정된 개수의 파일로 균등하게 분할합니다."""
    # 전체 라인 수 계산
    total_lines = sum(1 for _ in open(input_file, 'r', encoding='utf-8'))
    lines_per_file = math.ceil(total_lines / max_files)
    
    # 줄 수 기준으로 파일 분할 함수 호출
    split_file_by_lines(input_file, lines_per_file)



# 사용 예시
file_name = 'File Name.txt'
split_file_by_count(file_name, 10)  # 10개의 파일로 분할
