from tkinter import *
from tkinter import ttk
from utility import paint
from utility import File_location
import time
from utility import SMPC
from utility import NN
from utility import NN_helper
from utility import two_layer
from utility import CNN_layer
from utility import CNN_helper
from utility import CNN_Split
from utility import four_layer
from utility import five_layer
from utility import Six_layer


# window = Tk()


def call():
    window = Tk()
    window.title("SMPC")

    WIDTH = 600
    HEIGHT = 575

    window.geometry("1320x1020")

    canvas_2 = Canvas(window, width=WIDTH, height=70)
    canvas_2.grid(row=0, column=0)
    canvas_2.option_add("*TCombobox*Listbox.font", "sans 20 bold")
    canvas_2.option_add("*TCombobox*Listbox.justify", "center")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('W.TCombobox', arrowsize=25)

    options = [
        "Secure Multiparty Computation",
        "Neural Network Inferencing",
        "Neural Network Inferencing with helper node",
        "Setup: Two Layer Neural Network",
        "Setup: Five Layer Neural Network",
        #   "Convolution Neural Network",
        "Convolution Neural Network Inferencing with helper node",
        "Convolution Neural Network Split",
        "Setup: Four Layer Convolution Network",
        "Setup: Six Layer Convolution Network"
    ]

    def display_selected(event):
        choice = my_combo.get()
        if choice == "Secure Multiparty Computation":
            window.destroy()
            SMPC.call()
        elif choice == "Neural Network Inferencing":
            window.destroy()
            NN.call()
        elif choice == "Neural Network Inferencing with helper node":
            window.destroy()
            NN_helper.call()
        elif choice == "Setup: Two Layer Neural Network":
            window.destroy()
            two_layer.call()
      #  elif choice == "Convolution Neural Network":
       #     window.destroy()
        #    CNN_layer.call()
        elif choice == "Convolution Neural Network Inferencing with helper node":
            window.destroy()
            CNN_helper.call()
        elif choice == "Convolution Neural Network Split":
            window.destroy()
            CNN_Split.call()
        elif choice == "Setup: Four Layer Convolution Network":
            window.destroy()
            four_layer.call()
        elif choice == "Setup: Five Layer Neural Network":
            window.destroy()
            five_layer.call()
        elif choice == "Setup: Six Layer Convolution Network":
            window.destroy()
            Six_layer.call()

    clicked = StringVar()
    my_combo = ttk.Combobox(canvas_2, values=options, font=(
        'sans 20 bold'), justify=CENTER, textvariable=clicked, style='W.TCombobox', state="readonly")
    my_combo.grid(row=0, column=0, ipadx=280, ipady=10, padx=10, pady=10)
    # my_combo.config(dropdown_font = ('Times 20 bold'))
    my_combo.set("CNN 6 Layer")
    my_combo.bind("<<ComboboxSelected>>", display_selected)

    # canvas_1 = Canvas(window, width= WIDTH, height=HEIGHT)
    canvas_1 = Canvas(window, width=1000, height=320)
    canvas_1.grid(row=1, column=0, padx=20)

    # back_image2 = PhotoImage(file="./Images_Video/NN.png")
    # my_image2 = canvas_1.create_image(WIDTH/2,HEIGHT/2,anchor=CENTER,image = back_image2)

    text_1 = "Configuration"
    canvas_1.create_text(20, 25, anchor=W, text=text_1,
                         fill="black", font=('sans 20 bold'))
    text_30 = "Layer"
    text_31 = "No. of kernels"
    text_32 = "No. of Mult"
    text_33 = "No. of Parameters"
    canvas_1.create_text(20, 60, anchor=W, text=text_30,
                         fill="black", font=('sans 18 bold'))
    canvas_1.create_text(300, 60, anchor=W, text=text_31,
                         fill="black", font=('sans 18 bold'))
    canvas_1.create_text(560, 60, anchor=W, text=text_32,
                         fill="black", font=('sans 18 bold'))
    canvas_1.create_text(755, 60, anchor=W, text=text_33,
                         fill="black", font=('sans 18 bold'))

    text_40 = "CNN1"
    text_41 = "32"
    text_42 = "878 x 10³"
    text_43 = "32 x 3 X 3 X 3"
    canvas_1.create_text(20,  100, anchor=W, text=text_40,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 100, anchor=W, text=text_41,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 100, anchor=W, text=text_42,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 100, anchor=W, text=text_43,
                         fill="black", font=('sans 16 '))
    text_50 = "CNN2"
    text_51 = "32"
    text_52 = "5760 x 10³"
    text_53 = "32 x 32 X 5 X 5"

    canvas_1.create_text(20, 140, anchor=W, text=text_50,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 140, anchor=W, text=text_51,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 140, anchor=W, text=text_52,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 140, anchor=W, text=text_53,
                         fill="black", font=('sans 16 '))
    text_60 = "CNN3"
    text_61 = "64"
    text_62 = "3276 x 10³"
    text_63 = "64 X 32 x 5 x 5"
    canvas_1.create_text(20, 180, anchor=W, text=text_60,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 180, anchor=W, text=text_61,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 180, anchor=W, text=text_62,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 180, anchor=W, text=text_63,
                         fill="black", font=('sans 16 '))
    text_70 = "CNN4"
    text_71 = "64"
    text_72 = "1327 x 10³"
    text_73 = "64 X 64 x 3 X 3"
    canvas_1.create_text(20, 220, anchor=W, text=text_70,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 220, anchor=W, text=text_71,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 220, anchor=W, text=text_72,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 220, anchor=W, text=text_73,
                         fill="black", font=('sans 16 '))
    text_80 = "NN5"
    text_81 = " -"
    text_82 = "1179 x 10³"
    text_83 = "512 x 2304"
    canvas_1.create_text(20, 260, anchor=W, text=text_80,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 260, anchor=W, text=text_81,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 260, anchor=W, text=text_82,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 260, anchor=W, text=text_83,
                         fill="black", font=('sans 16 '))
    text_90 = "NN6"
    text_91 = " -"
    text_92 = "5 x 10³"
    text_93 = "10 x 512"
    canvas_1.create_text(20, 300, anchor=W, text=text_90,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(340, 300, anchor=W, text=text_91,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(560, 300, anchor=W, text=text_92,
                         fill="black", font=('sans 16 '))
    canvas_1.create_text(820, 300, anchor=W, text=text_93,
                         fill="black", font=('sans 16 '))

    canvas_2 = Canvas(window, width=1000, height=230)
    canvas_2.grid(row=2, column=0, padx=20)
    TEXT_1 = "System Configuration (WAN)"
    canvas_2.create_text(20, 25, anchor=W, text=TEXT_1,
                         fill="black", font=('sans 20 bold'))
    TEXT_30 = "Server 0"
    TEXT_31 = "2 GB RAM"
    TEXT_32 = "2.6 GHZ"
    canvas_2.create_text(20, 60, anchor=W, text=TEXT_30,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(340, 60, anchor=W, text=TEXT_31,
                         fill="black", font=('sans 16'))
    canvas_2.create_text(600, 60, anchor=W, text=TEXT_32,
                         fill="black", font=('sans 16'))
    TEXT_40 = "Server 1"
    TEXT_41 = "2 GB RAM"
    TEXT_42 = "2.4 GHZ"
    canvas_2.create_text(20, 100, anchor=W, text=TEXT_40,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(340, 100, anchor=W, text=TEXT_41,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(600, 100, anchor=W, text=TEXT_42,
                         fill="black", font=('sans 16 '))
    TEXT_50 = "Server 2"
    TEXT_51 = "0.7 GB RAM"
    TEXT_52 = "2.4 GHZ"
    canvas_2.create_text(20, 140, anchor=W, text=TEXT_50,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(340, 140, anchor=W, text=TEXT_51,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(600, 140, anchor=W, text=TEXT_52,
                         fill="black", font=('sans 16 '))
    TEXT_60 = "Local system Configuration"
    canvas_2.create_text(20, 180, anchor=W, text=TEXT_60,
                         fill="black", font=('sans 18 bold '))
    TEXT_60 = "No. of cores: 4"
    TEXT_61 = "16 GB RAM"
    TEXT_62 = "2.5 GHZ"
    canvas_2.create_text(20, 220, anchor=W, text=TEXT_60,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(340, 220, anchor=W, text=TEXT_61,
                         fill="black", font=('sans 16 '))
    canvas_2.create_text(600, 220, anchor=W, text=TEXT_62,
                         fill="black", font=('sans 16 '))

    canvas_3 = Canvas(window, width=1100, height=550)
    canvas_3.grid(row=3, column=0, padx=20, pady=20)
    text_90 = "SPLIT Configuration"
    Label_90 = Label(canvas_3, text=text_90, font=(
        'sans 18 bold'), height=2, width=20)
    Label_90.grid(row=0, column=0, columnspan=3, sticky='w')
    text_00 = "Configuration"
    text_10 = "RAM (GB)"
    text_20 = "Execution Time\n(Sec)"
    Label_00 = Label(canvas_3, text=text_00, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    Label_00.grid(row=1, column=0)
    Label_10 = Label(canvas_3, text=text_10, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    Label_10.grid(row=1, column=1)
    Label_30 = Label(canvas_3, text=text_20, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=15)
    Label_30.grid(row=1, column=2)

    # text_01 = "CNN_split:(1,1,1,1)\nNN_split:(1,1)"
    # text_11 = "-"
    # text_21 = "-"
    # text1_41 = "-"
    # text1_51 = "-"
    # text1_31 = "878 | 5760 | 3276 | 1327 | 1179 | 5"
    # Label_01 = Label(canvas_3, text=text_01, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    # Label_01.grid(row=2, column=0)
    # Label_11 = Label(canvas_3, text=text_11, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    # Label_11.grid(row=2, column=1)
    # Label_21 = Label(canvas_3, text=text_21, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    # Label_21.grid(row=2, column=2)
    # Label_31 = Label(canvas_3, text=text1_41, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    # Label_31.grid(row=2, column=3)
    # Label_41 = Label(canvas_3, text=text1_51, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    # Label_41.grid(row=2, column=4)
    # Label_51 = Label(canvas_3, text=text1_31, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=29)
    # Label_51.grid(row=2, column=5)

    # text_01 = "CNN_split:(32,32,64,64)\nNN_split:(256,5)"
    # text_11 = "0.549"
    # text1_41 = "1835"
    # Label_01 = Label(canvas_3, text=text_01, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    # Label_01.grid(row=2, column=0)
    # Label_11 = Label(canvas_3, text=text_11, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    # Label_11.grid(row=2, column=1)
    # Label_31 = Label(canvas_3, text=text1_41, highlightthickness=1,
    #                  highlightbackground="black", font=('sans 16 normal'), height=2, width=15)
    # Label_31.grid(row=2, column=2)

    text_03 = "CNN_split:(32,16,64,64)\nNN_split:(256,5)"
    text_13 = "1.078"
    text1_43 = "1416"
    Label_03 = Label(canvas_3, text=text_03, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    Label_03.grid(row=2, column=0)
    Label_13 = Label(canvas_3, text=text_13, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    Label_13.grid(row=2, column=1)
    Label_33 = Label(canvas_3, text=text1_43, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=15)
    Label_33.grid(row=2, column=2)

    text_04 = "Helper Node\n(Conv and Mult)"
    text_14 = "0.725"
    text1_44 = "82"
    Label_04 = Label(canvas_3, text=text_04, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    Label_04.grid(row=3, column=0)
    Label_14 = Label(canvas_3, text=text_14, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    Label_14.grid(row=3, column=1)
    Label_34 = Label(canvas_3, text=text1_44, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=15)
    Label_34.grid(row=3, column=2)

    text_05 = "Helper Node\n(Conv, Mult and ReLU)"
    text_15 = "0.19"
    text1_45 = "51"
    Label_05 = Label(canvas_3, text=text_05, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=18)
    Label_05.grid(row=4, column=0)
    Label_15 = Label(canvas_3, text=text_15, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=10)
    Label_15.grid(row=4, column=1)
    Label_35 = Label(canvas_3, text=text1_45, highlightthickness=1,
                     highlightbackground="black", font=('sans 16 normal'), height=2, width=15)
    Label_35.grid(row=4, column=2)

    # text_06 = "H3:(1,2,-,-)"
    # text_16 = "0.035"
    # text_26 = "60"
    # text1_36= "4265, 1440, 540, 500"
    # Label_06 = Label(canvas_2, text = text_06,highlightthickness=1, highlightbackground="black",font=('sans 16 normal'), height=2, width=20)
    # Label_06.grid(row = 7, column=0)
    # Label_16 = Label(canvas_2, text = text_16,highlightthickness=1, highlightbackground="black",font=('sans 16 normal'), height=2, width=20)
    # Label_16.grid(row = 7, column=1)
    # Label_26 = Label(canvas_2, text = text_26,highlightthickness=1, highlightbackground="black",font=('sans 16 normal'), height=2, width=20)
    # Label_26.grid(row = 7, column=2)
    # Label_36 = Label(canvas_2, text = text1_36,highlightthickness=1, highlightbackground="black",font=('sans 16 normal'), height=2, width=20)
    # Label_36.grid(row = 7, column=3)

    window.resizable(False, False)
    window.mainloop()
