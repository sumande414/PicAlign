from tkinter import *
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk, Image
import PicAlign_b as back


def home(prev):
    if prev != None:
        prev.destroy()
    screen = Tk()
    screen.title("PicAlign v1.0.0")
    screen.iconbitmap(get_path("logo_small.ico"))

    buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

    get_started = Button(screen,text="Get Started",height='1', width='10', font=buttonFont, command= lambda: file_wizard(screen))
    get_started.grid(row=0, column=0)

    help_app = Button(screen,text="Help",height='1', width='10', font=buttonFont, command=lambda: help(screen))
    help_app.grid(row=1, column=0)

    about = Button(screen,text="About",height='1', width='10', font=buttonFont, command=lambda: about_m(screen))
    about.grid(row=2, column=0)

    exit = Button(screen,text="Exit",height='1', width='10', font=buttonFont, command= lambda: screen.destroy())
    exit.grid(row=3, column=0)

    frame = Frame(screen, width=600, height=400)
    frame.grid(row=0,column=1,rowspan=4)

    img = ImageTk.PhotoImage(Image.open(get_path("logo.jpg")))
    label = Label(frame, image = img)
    label.grid(row=0,column=1)

    screen.mainloop()


def open(gt):
    gt.filename = filedialog.askopenfilenames(title="Open files", filetypes = (("JPG Files","*.jpg"), ("All Files","*.*")))

    buttonfont = font.Font(family='Helvetica', size=16, weight='bold')

    test = Label(gt, text="Files Selected : "+ str(len(gt.filename)))
    test.grid(row=4, column=0)

    preset = DoubleVar()
    preset.set(2.5)

    modes = [
        ("Small", 1.5),
        ("Medium", 2.5),
        ("Large", 3),
    ]

    c=1

    for p, v in modes:
        Radiobutton(gt, text=p, variable= preset, value =v).grid(row=c, column=0)
        c+=1


    process_button = Button(gt, text="Done", font = buttonfont, command = lambda: back.generate_docx(gt.filename, preset.get()))
    process_button.grid(row=5, column=0)



    
def file_wizard(prev):
    prev.destroy()
    gt = Tk()
    gt.title("PicAlign v1.0.0")
    gt.iconbitmap(get_path("logo_small.ico"))
    #gt.geometry("500x400")
    buttonfont = font.Font(family='Helvetica', size=16, weight='bold')
    open_file_button = Button(gt, text="Open Images", font=buttonfont, command = lambda: open(gt))
    open_file_button.grid(row='0', column='0')

    menu_button = Button(gt, text = "Main Menu", font = buttonfont, command = lambda: home(gt))
    menu_button.grid(row = 6, column = 0)

    frame = Frame(gt, width=600, height=400)
    frame.grid(row=0,column=1, rowspan= 7)

    img2 = ImageTk.PhotoImage(Image.open(get_path("logo.jpg")))
    label = Label(frame, image = img2)
    label.grid(row=0,column=1)

    gt.mainloop()

def help(prev):
    if prev != None:
        prev.destroy()
    hlp = Tk()
    hlp.title('Help')
    hlp.iconbitmap(get_path("logo_small.ico"))
    
    frame = Frame(hlp, width=600, height=400)
    frame.grid(row=0,column=0)

    labelfont = font.Font(family='Times New Roman', size=12)
    buttonfont = font.Font(family='Helvetica', size=16, weight='bold')

    frm_label = Label(
        frame, 
        text = "1. Click Get Started\n2. Select Multiple Image Files\n3. Select size and click Done.\n4. Open your file stored in the same directory as the app.",
        font = labelfont)
    frm_label.grid(row=0,column=0)

    menu_button = Button(frame, text = "Main Menu", font = buttonfont, command = lambda: home(hlp))
    menu_button.grid(row = 1, column = 0)

def about_m(prev):
    if prev != None:
        prev.destroy()
    abt=Tk()
    abt.title("About")   
    abt.iconbitmap(get_path("logo_small.ico"))
    frame = Frame(abt, width=600, height=400)
    frame.pack()
    buttonfont = font.Font(family='Helvetica', size=16, weight='bold')
    global img1
    img1 = ImageTk.PhotoImage(Image.open(get_path("dev.jpg")))
    label = Label(frame, image = img1)
    label.pack()

    abt_label = Label(abt, text = "PicAlign v1.0.0\nDeveloper: Suman De")
    abt_label.pack()

    menu_button = Button(abt, text = "Main Menu", font = buttonfont, command = lambda: home(abt))
    menu_button.pack()

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

prev = None

home(prev)