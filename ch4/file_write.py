def writeFile():
    # Open a file for writing and create it if its not present
    f = open("textfile.txt","w+")

    #Open the file for appending text to the end
    #f = open("textfile.txt","a+")

    # write some lines of data to the file
    for i in range (10):
        f.write("This is line {0}\n".format(i+1))

    #close the file when done
    f.close()
    
    f= open("textfile.txt","r")
    if f.mode == 'r':  #check to make sure the file was opened
        # use the read() function to read the entire file
        contents = f.read()
        print (contents)

        #use the readlines() function to read the file one line at a time
        fl = f.readlines() #readlines reads the lines into a list
        for x in fl:
            print (x)

writeFile()
