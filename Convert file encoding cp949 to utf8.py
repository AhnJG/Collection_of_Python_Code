# Convert file encoding cp949 to utf8
# Linux Command
iconv -f cp949 -t utf-8 "Original File Name" > "Copied File Name"

# Run on Python
import subprocess
subprocess.check_output("iconv -f cp949 -t utf-8 'Original File Name' > 'Copied File Name'", shell=True)
