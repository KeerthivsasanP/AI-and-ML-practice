def del_line(fname,line_no):
    with open(fname,'r',encoding="utf-8") as fobj:
        lines = fobj.readlines()
        total_lines = len(lines)
        if(line_no > total_lines):
            print("File only has %g lines"%(total_lines))
            print(lines)
        else:
            with open(fname,'w') as fobj:
                print(lines)
                del lines[line_no - 1]
                print(lines)
                fobj.writelines(lines)
                        

file_name = input("Enter the file name to be deleted")      
line_no = int(input("Enter the line number to be deletedd"))
del_line(file_name,line_no)
