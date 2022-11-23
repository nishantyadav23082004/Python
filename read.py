# This code is used to read a file named demofile.txt
f = open("C:\\Python\demofile.txt","r")
print(f.read()) # This prints whole text written in demofile.txt

print(f.read(5))# This prints first 5 characters of demofile.txt including whitespaces
