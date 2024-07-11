# =========================

# Q2 create funcation to write any thing to the file 

def mywrite(filepath, content, option):
    try:
        file = open(filepath, 'w')
        if (file.writable()):
          if option == 'all':
              file.write(content)
          elif option == 'lines':
              file.writelines(content)
          else:
              raise ValueError("Invalid option for writing")
          file.close()
        else:
            raise FileNotFoundError("File not found")
    except Exception :
        print("Error writing file: ")

mywrite('khaled.txt', 'hello khaled gamal in python world ', 'all')


# Q2    create funcation to add a new contant to the file 

def myappend(filepath, newcontent, option):
    try:
        file = open(filepath, 'a')
        if option == 'write':
            file.write(newcontent)
        elif option == 'lines':
            file.writelines(newcontent)
        else:
            raise ValueError("Invalid option to add")
        file.close()
    except Exception :
        print("Error writing file: ")


myappend('omar.txt', '\n new more of text adding ', 'write')
