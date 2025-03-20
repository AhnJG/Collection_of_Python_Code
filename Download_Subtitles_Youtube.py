# Linux Shell Command 
# Download Subtitles 
yt-dlp --write-subs --skip-download --sub-langs ko --sub-format vtt --output <Output Name> <Youtube URL>

--write-subs: 업로더가 제공한 자막을 다운로드.
--write-auto-subs: 자동 생성된 자막을 다운로드.
--skip-download: 영상 파일은 다운로드하지 않음.
--sub-langs ko: 한국어 자막만 다운로드.
--sub-format vtt: VTT 형식으로 저장.
  
# Check Subtitles 
yt-dlp --list-subs <Youtube URL>

# Python 
import subprocess
subprocess.check_output("yt-dlp --write-subs 
                        --skip-download 
                        --sub-langs ko 
                        --sub-format vtt 
                        --output 'transcript' 
                        'https://www.youtube.com/watch?v=9kPhqnqUYz4'"
                        , shell=True)
