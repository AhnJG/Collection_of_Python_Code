!pip install pytubefix

import os
from pytubefix import YouTube

def download_youtube_as_mp3(youtube_url, output_path):
    try:
        # YouTube 객체 생성
        yt = YouTube(youtube_url)
        print(f"'{yt.title}' 영상 찾는 중...")
        
        # 오디오 스트림만 필터링
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # 다운로드 경로 설정
        os.makedirs(output_path, exist_ok=True)
        
        # 오디오 다운로드
        print("오디오 다운로드 중...")
        audio_file = audio_stream.download(output_path)
        
        # 확장자 MP3로 변환
        base, ext = os.path.splitext(audio_file)
        mp3_file = base + ".mp3"
        os.rename(audio_file, mp3_file)
        
        print(f"다운로드 완료! MP3 파일 경로: {mp3_file}")
        
    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
if __name__ == "__main__":
    youtube_url = 'Youtube Url'
    output_path = 'Save path'

    download_youtube_as_mp3(youtube_url, output_path)
