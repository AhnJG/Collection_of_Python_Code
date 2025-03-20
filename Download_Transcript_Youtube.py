# Linux Shell Command
yt-dlp --write-subs --skip-download --sub-langs ko --sub-format vtt --output 'Output Name' 'Youtube URL'

# Python 
import subprocess
subprocess.check_output("yt-dlp --write-subs 
                        --skip-download 
                        --sub-langs ko 
                        --sub-format vtt 
                        --output 'transcript' 
                        'https://www.youtube.com/watch?v=9kPhqnqUYz4'"
                        , shell=True)
