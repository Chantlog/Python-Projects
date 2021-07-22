import subprocess, time, webbrowser
# webbrowser.get('windows-default').open('https://youtube.com')

fileObj = open('hello.txt','w')
fileObj.write("Hello World!")
fileObj.close()

text = subprocess.Popen(['start','hello.txt'],shell=True)
text.wait()
print("Closed")
