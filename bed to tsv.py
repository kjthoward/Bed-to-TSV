import sys, os, tkFileDialog, Tkinter, pdb, time

os.system("title BED to TSV Converter")

def main():
    rootwindow = Tkinter.Tk()
    rootwindow.withdraw()
    renamed = 0

    print "BED to TSV Converter"
    print "Please select a folder"
    folderpath = tkFileDialog.askdirectory(parent=rootwindow, title='Please select a folder')
    if folderpath == "":
        sys.exit()

    print "Selected Folder: {0}".format(os.path.basename(folderpath))
    for root, dirnames, filenames in os.walk(folderpath):
        for filename in filenames:
            if filename.endswith(".bed"):

                oldfile = os.path.join(root, filename)
                print "Renaming {0}".format(filename)
                os.rename(oldfile, oldfile[:-4] + '.tsv')
                renamed +=1
    time.sleep(1)
    if renamed > 0 :
        print "{0} Files were successfully renamed".format(renamed)
    if renamed == 0:
        print "No files with the .bed extension were found"
                
    raw_input("Press enter to quit")


if __name__ == "__main__":
    main()
