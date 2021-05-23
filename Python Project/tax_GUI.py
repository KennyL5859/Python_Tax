
# imports all the files and functions needed
import AGI as ag
import Deductions as dd
import tkinter as tk
import tkinter.font
import tkinter.filedialog
import tkinter.messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class tax_GUI:
    # set class constants
    MARRIED_FILING_JOINT = 'MFJ'
    MARRIED_FILING_SEPARATE = 'MFS'
    SINGLE = 'S'
    HEAD_OF_HOUSEHOLD = 'HOH'

    def __init__(self):
        # set the initial size of screen
        self.main_window = tk.Tk()
        self.main_window.title('Tax Calculator')
        self.main_window.geometry('1400x900+20+20')

        # Sets the min/max size of window
        self.main_window.minsize(1200, 900)
        self.main_window.maxsize(1400, 900)

        # create frame for calculate AGI widgets, calculate itemize decutions, filing status radio buttons
        self.agiFrame = tk.Frame(self.main_window, highlightbackground = 'black', highlightthickness = 2)
        self.itemizedFrame = tk.Frame(self.main_window, highlightbackground='black', highlightthickness=2)
        self.clientInfoFrame = tk.Frame(self.main_window)
        self.agiButtonFrame = tk.Frame(self.main_window)
        self.itemizedButtonFrame = tk.Frame(self.main_window)
        self.filingFrame = tk.Frame(self.main_window)
        self.listboxFrame = tk.Frame(self.main_window)
        self.menubar = tk.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)

        # add menu options to menu bar
        self.file_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'Save File As...', command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit', command = self.exit_app)

        # create the filing status radio buttons
        self.filing_fam = tk.StringVar()

        # create radio buttons
        self.filing_fam.set(tax_GUI.MARRIED_FILING_JOINT) # initialize it to Married Filing Jointly

        self.mfj_button = tk.Radiobutton(self.filingFrame, variable = self.filing_fam,
                                         value = tax_GUI.MARRIED_FILING_JOINT, text = 'Married Filing Jointly    ',
                                         font = 'Ariel 12 bold')

        self.mfs_button = tk.Radiobutton(self.filingFrame, variable = self.filing_fam, text = 'Married Filing Separate',
                                         value = tax_GUI.MARRIED_FILING_SEPARATE, font = 'Ariel 12 bold')


        self.single_button = tk.Radiobutton(self.filingFrame, variable = self.filing_fam, text = '{:30s}'.format('Single'),
                                            value = tax_GUI.SINGLE, font = 'Ariel 12 bold')

        self.hoh_button = tk.Radiobutton(self.filingFrame, variable = self.filing_fam, text = 'Head of Household',
                                         value = tax_GUI.HEAD_OF_HOUSEHOLD, font = 'Ariel 12 bold')

        # arrange the radio buttons into grid format
        self.mfj_button.grid(row = 0, column = 0)
        self.single_button.grid(row = 0, column = 1)
        self.mfs_button.grid(row = 1, column = 0)
        self.hoh_button.grid(row=1, column=1)

        # create listbox and scrollbar for to show gross income / agi
        self.scrollbar = tk.Scrollbar(self.listboxFrame, orient = tk.VERTICAL)
        self.listbox = tk.Listbox(self.listboxFrame, yscrollcommand = self.scrollbar.set, height = 37,
                                  width = 60, bd = 4, font = 'Consolas 12 bold')
        self.scrollbar.config(command = self.listbox.yview)
        self.scrollbar.pack(side = 'right', fill = tk.Y)
        self.listbox.pack(side = 'left', fill = tk.BOTH, expand = 1)

        # create and set the title label
        self.title_label = tk.Label(self.main_window, text = 'Tax Preparation Calculator', font = ('Ariel 24 bold'),
                                    bg = 'white', fg = 'blue')
        self.title_label.place(relx = 0.5, rely = 0.01, anchor = 'n')

        # create and set the title label for AGI section
        self.agiTitle_label = tk.Label(self.main_window, text = 'Adjusted Gross Income', font = ('Ariel 18 bold'),
                                       bg = 'yellow', fg = 'blue')
        self.agiTitle_label.place(relx = 0.05, rely = 0.30, anchor = 'nw')

        # create and set the title label for Itemize Dedcution section
        self.itemizedTitle_label = tk.Label(self.main_window, text = 'Total Itemized Amount', font = ('Ariel 18 bold'),
                                           bg = 'yellow', fg = 'blue')
        self.itemizedTitle_label.place(relx = 0.4, rely = 0.3, anchor = 'n')

        # create labels and entry for client info. frame
        self.name_label = tk.Label(self.clientInfoFrame, text = 'Name:', padx = 15, pady = 4, font = ('Ariel 12 bold'))
        self.name_entry = tk.Entry(self.clientInfoFrame, width = 30, bd = 5, font = ('Ariel 12 bold'))
        self.email_label = tk.Label(self.clientInfoFrame, text = 'Email:', padx = 15, pady = 4, font = ('Ariel 12 bold'))
        self.email_entry = tk.Entry(self.clientInfoFrame, width = 30, bd = 5, font = ('Ariel 12 bold'))

        # create labels and entry for all AGI fields
        self.w2_label = tk.Label(self.agiFrame, text = '{:30s}'.format('W2 Income:'), padx = 15,
                                 font = ('Ariel 12 bold'))
        self.w2_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.capital_label = tk.Label(self.agiFrame, text = '{:30s}'.format('Capital gains:'), padx = 15, pady = 4,
                                      font = ('Ariel 12 bold'))
        self.capital_entry = tk.Entry(self.agiFrame, width=20,  bd = 4)

        self.rental_label = tk.Label(self.agiFrame, text = '{:30s}'.format('Schedule E:'), padx = 15, pady = 4,
                                     font = ('Ariel 12 bold'))
        self.rental_entry = tk.Entry(self.agiFrame, width=20,  bd = 4)

        self.scheduleC_label = tk.Label(self.agiFrame, text = '{:30s}'.format('Schedule C:'), padx = 15, pady = 4,
                                        font = ('Ariel 12 bold'))
        self.scheduleC_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.retirement_label = tk.Label(self.agiFrame, text = '{:30s}'.format('Retirement:'), padx = 15, pady = 4,
                                         font = ('Ariel 12 bold'))
        self.retirment_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.hsa_label = tk.Label(self.agiFrame, text='HSA Contribution:      ', padx = 15, pady = 4,
                                  font = ('Ariel 12 bold'))
        self.hsa_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.stuLoanInt_label = tk.Label(self.agiFrame, text='Student Loan Interest:', padx = 15, pady = 4,
                                         font=('Ariel 12 bold'))
        self.stuLoanInt_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.ira_label = tk.Label(self.agiFrame, text='IRA Contribution:       ', padx = 15, pady = 4,
                                  font = ('Ariel 12 bold'))
        self.ira_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        self.seTax_label = tk.Label(self.agiFrame, text='Self-Employment Tax:', padx = 15, pady = 4,
                                    font = ('Ariel 12 bold'))
        self.seTax_entry = tk.Entry(self.agiFrame, width=20, bd = 4)

        # set grid layout for client info. fields
        self.name_label.grid(row = 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)
        self.email_label.grid(row = 1, column = 0)
        self.email_entry.grid(row = 1, column = 1)

        # set grid layout for AGI fields
        self.w2_label.grid(row = 2, column = 0)
        self.w2_entry.grid(row = 2, column = 1)
        self.capital_label.grid(row = 3, column = 0)
        self.capital_entry.grid(row = 3, column = 1)
        self.rental_label.grid(row = 4, column = 0)
        self.rental_entry.grid(row = 4, column = 1)
        self.scheduleC_label.grid(row = 5, column = 0)
        self.scheduleC_entry.grid(row = 5, column = 1)
        self.retirement_label.grid(row = 6, column = 0)
        self.retirment_entry.grid(row = 6, column = 1)
        self.hsa_label.grid(row = 7, column = 0)
        self.hsa_entry.grid(row = 7, column = 1)
        self.stuLoanInt_label.grid(row = 8, column = 0)
        self.stuLoanInt_entry.grid(row = 8, column = 1)
        self.ira_label.grid(row = 9, column = 0)
        self.ira_entry.grid(row = 9, column = 1)
        self.seTax_label.grid(row = 10, column = 0)
        self.seTax_entry.grid(row = 10, column = 1)

        # create labels and entry fields for itemized field
        self.mortgageInt_label = tk.Label(self.itemizedFrame, text = '{:29s}'.format('Mortgage Interest:'),
                                          padx=15, pady=4, font=('Ariel 12 bold'))

        self.mortgageInt_entry = tk.Entry(self.itemizedFrame, width=20, bd = 4, state = 'disabled')

        self.mortgageIns_label = tk.Label(self.itemizedFrame, text = '{:25s}'.format('Mortgage Insurance:'),
                                          padx=15, pady=4, font=('Ariel 12 bold'))
        self.mortgageIns_entry = tk.Entry(self.itemizedFrame, width=20, bd = 4, state = 'disabled')

        self.charitable_label = tk.Label(self.itemizedFrame, text='Charitable Contribution:', padx=15, pady=4,
                                          font=('Ariel 12 bold'))
        self.charitable_entry = tk.Entry(self.itemizedFrame, width=20, bd = 4, state = 'disabled')

        self.medicalExp_label = tk.Label(self.itemizedFrame, text = '{:28s}'.format('Medical Expense:'), padx=15,
                                         pady=4, font=('Ariel 12 bold'))
        self.medicalExp_entry = tk.Entry(self.itemizedFrame, width=20, bd = 4, state = 'disabled')

        self.slIncomeTax_label = tk.Label(self.itemizedFrame, text = '{:29s}'.format('State & Local Tax:'), padx=15,
                                          pady=4, font=('Ariel 12 bold'))
        self.slIncomeTax_entry = tk.Entry(self.itemizedFrame, width=20, bd = 4, state = 'disabled')

        # set the grid layout itemized deduction field
        self.mortgageInt_label.grid(row=0, column=0)
        self.mortgageInt_entry.grid(row=0, column=1)
        self.mortgageIns_label.grid(row=1, column=0)
        self.mortgageIns_entry.grid(row=1, column=1)
        self.charitable_label.grid(row=2, column=0)
        self.charitable_entry.grid(row=2, column=1)
        self.medicalExp_label.grid(row=3, column=0)
        self.medicalExp_entry.grid(row=3, column=1)
        self.slIncomeTax_label.grid(row=4, column=0)
        self.slIncomeTax_entry.grid(row=4, column=1)

        # set the properties for all the buttons in file
        self.calcAGI_button = tk.Button(self.agiButtonFrame, text = 'Calculate AGI', font = ('Ariel 14 bold'),
                                        bg = 'skyblue', command = self.calculateAGI)

        self.clearAGI_button = tk.Button(self.agiButtonFrame, text = 'Clear', font = ('Ariel 14 bold'),
                                         bg = 'skyblue', command = self.clearAGI_entry)

        self.calcItemized_button = tk.Button(self.itemizedButtonFrame, text='Calculate Itemized',
                                             font=('Ariel 14 bold'), bg='lightgreen', command = self.calcItemized)

        self.clearItemized_button = tk.Button(self.itemizedButtonFrame, text='Clear', font=('Ariel 14 bold'),
                                         bg='lightgreen', command = self.clearItemized_entry)

        self.clearListboxButton = tk.Button(self.main_window, text = 'Clear Listbox', font =('Ariel 14 bold'),
                                            bg = 'orange red', command = self.clearListbox)

        self.emailClientButton = tk.Button(self.main_window, text = 'Email Client', font = ('Ariel 14 bold'),
                                           bg = 'deepskyblue', command = self.email_client)

        # pack the buttons
        self.calcAGI_button.pack(side = 'left', padx = 30)
        self.clearAGI_button.pack(side = 'left')
        self.calcItemized_button.pack(side = 'left', padx = 25)
        self.clearItemized_button.pack(side = 'left')

        # place all the frames setup accordingly
        self.agiFrame.place(relx = 0.15, rely = 0.5, anchor = 'center')
        self.agiButtonFrame.place(relx = 0.12, rely = 0.7, anchor = 'center')
        self.itemizedFrame.place(relx = 0.4, rely = 0.433, anchor= 'center')
        self.itemizedButtonFrame.place(relx = 0.39, rely = 0.56, anchor = 'center')
        self.clientInfoFrame.place(relx = 0.172, rely = 0.10, anchor = 'n')
        self.filingFrame.place(relx = 0.05, rely = 0.20, anchor = 'nw')
        self.listboxFrame.place(relx = 0.75, rely = 0.5, anchor = 'center')
        self.clearListboxButton.place(relx = 0.75, rely = 0.95, anchor = 'center')
        self.emailClientButton.place(relx = 0.38, rely = 0.15, anchor = 'center')

        # infinite loop to run GUI file
        self.main_window.mainloop()

    # method that activates all itemized fields once the user presses calculate AGI
    def config_Itemized(self):
        self.mortgageInt_entry.configure(state = 'normal')
        self.mortgageIns_entry.configure(state = 'normal')
        self.charitable_entry.configure(state = 'normal')
        self.medicalExp_entry.configure(state = 'normal')
        self.slIncomeTax_entry.configure(state = 'normal')

    # closes the program once users clicks exit
    def exit_app(self):
        response = tk.messagebox.askyesno('Confirmation', 'Are you sure you want to exit? All data will be lost')
        if response == True:
            self.main_window.destroy()

    # clears all the AGI entry fields and places cursor on name
    def clearAGI_entry(self):
        self.name_entry.delete(0, tk.END)
        self.w2_entry.delete(0, tk.END)
        self.capital_entry.delete(0, tk.END)
        self.rental_entry.delete(0, tk.END)
        self.scheduleC_entry.delete(0, tk.END)
        self.retirment_entry.delete(0, tk.END)
        self.hsa_entry.delete(0, tk.END)
        self.stuLoanInt_entry.delete(0, tk.END)
        self.ira_entry.delete(0, tk.END)
        self.seTax_entry.delete(0, tk.END)
        self.name_entry.focus()

    # clears all the Itemized entry fields and places cursor on Mortgage Interest
    def clearItemized_entry(self):
        self.mortgageInt_entry.delete(0, tk.END)
        self.mortgageIns_entry.delete(0, tk.END)
        self.charitable_entry.delete(0, tk.END)
        self.medicalExp_entry.delete(0, tk.END)
        self.slIncomeTax_entry.delete(0, tk.END)
        self.mortgageInt_entry.focus()

    # clear the listbox and warn user before hand
    def clearListbox(self):
        response = tk.messagebox.askyesno('Confirmation', 'Are you sure you want to clear listbox?')
        if response == True:
            self.listbox.delete(0, tk.END)

    # method to calculate the AGI
    def calculateAGI(self):

        # get the needed fields
        name = self.name_entry.get()
        status = self.filing_fam.get()
        w2 = self.w2_entry.get()
        capital = self.capital_entry.get()
        rental = self.rental_entry.get()
        scheduleC = self.scheduleC_entry.get()
        retirement = self.retirment_entry.get()
        hsa = self.hsa_entry.get()
        stuLoanInt = self.stuLoanInt_entry.get()
        ira = self.ira_entry.get()
        seTax = self.seTax_entry.get()

        # if name is blank, prompt user
        try:
            name = str(name).upper()
            if name == '':
                raise AttributeError()

        except AttributeError:
            tk.messagebox.showerror('ERROR', 'Client name must be filed out')
            self.name_entry.focus()
        else:
            try:
                w2 = float(w2)
                capital = float(capital)
                rental = float(rental)
                scheduleC = float(scheduleC)
                retirement = float(retirement)
                hsa = float(hsa)
                stuLoanInt = float(stuLoanInt)
                ira = float(ira)
                seTax = float(seTax)

                # if any of the values are negative, then prompt user
                if (w2 < 0 or capital < 0 or rental < 0 or scheduleC < 0 or retirement < 0 or hsa < 0 or
                    stuLoanInt < 0 or ira < 0 or seTax < 0):
                    raise ValueError()

            except ValueError:
                tk.messagebox.showerror('ERROR', 'All AGI fields must be either postive numbers or 0')

            else:
                # place all fields into the AGI class from AGI file
                agiList = ag.AGI(name, status, w2, capital, rental, scheduleC, retirement, hsa, stuLoanInt, ira, seTax)

                # use the calcAGI method from AGI class
                agiSeries = ag.AGI.calcAGI(agiList)

                # calcuate the Gross Income
                grossIncome = (w2 + capital + rental + scheduleC + retirement)

                # set variables to actual deductible amount, these numbers come from  AGI class of AGI file
                hsaDeduct = agiSeries[0]
                stuDeduct = agiSeries[1]
                iraDeduct = agiSeries[2]
                seTaxDeduct = agiSeries[3]
                agi = agiSeries[4]

                # prep variables to insert into listbox
                name_1 = ('{:40}'.format('Name:') + name)
                status_1 = ('{:40s}'.format('Filing Status:   ') + status)
                w2_1 = ('{:40s}'.format('W2:') + str(w2))
                capital_1 = ('{:40s}'.format('Capital Gains:') + str(capital))
                rental_1 = ('{:40s}'.format('Schedule E Income:') + str(rental))
                scheduleC_1 = ('{:40s}'.format('Schedule C Income:') + str(scheduleC))
                retirement_1 = ('{:40s}'.format('Retirement Income:') + str(retirement))
                hsa_1 = ('{:50s}'.format('HSA Contributions:') + str(hsa))
                stuLoanInt_1 = ('{:50s}'.format('Student Loan Interest:') + str(stuLoanInt))
                ira_1 = ('{:50s}'.format('IRA Contribution:') + str(ira))
                seTax_1 = ('{:50s}'.format('Self Employment Tax:') + str(seTax))
                grossIncome_1 = ('{:40s}'.format('Gross Income:') + str(grossIncome))
                hsaDeduct_1 = ('{:50s}'.format('HSA Deduction:') + '(' +str(hsaDeduct) + ')')
                stuDeduct_1 = ('{:50s}'.format('Student Interest Deduction:') + '(' +str(stuDeduct) + ')')
                iraDeduct_1 = ('{:50s}'.format('IRA Contribution Deduction:') + '(' +str(iraDeduct) + ')')
                seTaxDeduct_1 = ('{:50s}'.format('Self-Employment Tax Deduction:') + '(' +str(seTaxDeduct) + ')')
                agi_1 = ('{:40s}'.format('Adjusted Gross Income:') + str(agi))

                # insert the variables above into listbox
                self.listbox.delete(0, tk.END)
                self.listbox.insert(1, name_1)
                self.listbox.insert(2, status_1)
                self.listbox.insert(3, w2_1)
                self.listbox.insert(4, capital_1)
                self.listbox.insert(5, rental_1)
                self.listbox.insert(6, scheduleC_1)
                self.listbox.insert(7, retirement_1)
                self.listbox.insert(8, hsa_1)
                self.listbox.insert(9, stuLoanInt_1)
                self.listbox.insert(10, ira_1)
                self.listbox.insert(11, seTax_1)
                self.listbox.insert(12, '')
                self.listbox.insert(13, grossIncome_1)
                self.listbox.insert(14, '')
                self.listbox.insert(15, hsaDeduct_1)
                self.listbox.insert(16, stuDeduct_1)
                self.listbox.insert(17, iraDeduct_1)
                self.listbox.insert(18, seTaxDeduct_1)
                self.listbox.insert(19, '')
                self.listbox.insert(20, agi_1)

                # enables the itemiezed fields once the user clicks calculate AGI button
                tax_GUI.config_Itemized(self)

                # return the following variables in a list form as it will be used later
                return w2, capital, rental, scheduleC, retirement, hsaDeduct, stuDeduct, iraDeduct, \
                       name, status, seTaxDeduct, agi

    def calcItemized(self):
        # get all the necessary fields needed to calculate total itemized deduction
        name = self.name_entry.get()
        status = self.filing_fam.get()
        mortgageInt = self.mortgageInt_entry.get()
        mortgageIns = self.mortgageIns_entry.get()
        charitable = self.charitable_entry.get()
        medicalExp = self.medicalExp_entry.get()
        slTax = self.slIncomeTax_entry.get()

        # get the AGI components from the calcAGI method
        agi_List = tax_GUI.calculateAGI(self)

        # agi is equal to the 11th item on that list
        agi = agi_List[11]

        try:
            # make sure all itemized variables entered will be greater than 0
            name = str(name).upper()
            status = str(status)
            mortgageInt = float(mortgageInt)
            mortgageIns = float(mortgageIns)
            charitable = float(charitable)
            medicalExp = float(medicalExp)
            slTax = float(slTax)

            if mortgageInt < 0 or mortgageIns < 0 or charitable < 0 or medicalExp < 0 or slTax < 0:
                raise ValueError()

        except ValueError:
            tk.messagebox.showerror('ERROR', 'All itemize fields must be positive numbers or 0')
            self.mortgageInt_entry.focus()

        else:
            # call the Deductions class from Deductions file
            itemizedList = dd.Deductions(name, status, mortgageInt, mortgageIns, charitable, medicalExp, slTax)

            # calcuate the total itemized deductions from method in the deductions class from deductions file
            # this will return a list of deductible amounts and the final total itemized deduction
            itemizedDeduct = dd.Deductions.calcTotalItemizedDeduction(itemizedList, agi)

            # set varaibles of deductible amount
            mortgageIntDeduct = itemizedDeduct[0]
            mortgageInsDeduct = itemizedDeduct[1]
            charitableDeduct = itemizedDeduct[2]
            medicalExpDeduct = itemizedDeduct[3]
            slTaxDeduct = itemizedDeduct[4]
            sumItemized = itemizedDeduct[5]



            # this returns whether Itemize Deduction or Standard Deduction should be take
            takeItemorStandard = dd.Deductions.itemizeOrStandard(itemizedList, sumItemized)
            # break it into two parts
            itemizeString = takeItemorStandard[0]
            itemizeInt = takeItemorStandard[1]

            # calcuate taxable income
            taxableIncome = agi - itemizeInt


            # prep variables to insert into listbox
            mortgageInt_1 = ('{:50s}'.format('Mortgage Interest:') + str(mortgageInt))
            mortgageIns_1 = ('{:50s}'.format('Mortgage Insurance:') + str(mortgageIns))
            charitable_1 = ('{:50s}'.format('Charitable Contributions:') + str(charitable))
            medicalExp_1 = ('{:50s}'.format('Medical Expense:') + str(medicalExp))
            slTax_1 = ('{:50s}'.format('State & Local Tax') + str(slTax))
            mortgageIntDeduct_1 = ('{:50s}'.format('Deductible Mortgage Interest') + '(' +str(mortgageIntDeduct) + ')')
            mortgageInsDeduct_1 = ('{:50s}'.format('Deductible Mortgage Insurance') + '(' +str(mortgageInsDeduct) + ')')
            charitableDeduct_1 = ('{:50s}'.format('Deductible Charitable Contributions') + '(' +str(charitableDeduct) + ')')
            medicalExpDeduct_1 = ('{:50s}'.format('Deductible Medical Expenses') + '(' +str(medicalExpDeduct) + ')')
            slTaxDeduct_1 = ('{:50s}'.format('Deductible State/Local Tax') + '(' +str(slTaxDeduct) + ')')
            sumItemized_1 = ('{:50s}'.format('Total Itemize Deduction') + str(sumItemized))
            takeItemize_1 = ('{:40s}'.format(itemizeString) + str(itemizeInt))
            taxableIncome_1 = ('{:40s}'.format('Taxable Income') + str(taxableIncome))

            # insert into the listbox
            self.listbox.delete(20, tk.END)
            self.listbox.insert(21, '-------------------------------------------------------------')
            self.listbox.insert(22, mortgageInt_1)
            self.listbox.insert(23, mortgageIns_1)
            self.listbox.insert(24, charitable_1)
            self.listbox.insert(25, medicalExp_1)
            self.listbox.insert(26, slTax_1)
            self.listbox.insert(27, '')
            self.listbox.insert(28, mortgageIntDeduct_1)
            self.listbox.insert(29, mortgageInsDeduct_1)
            self.listbox.insert(30, charitableDeduct_1)
            self.listbox.insert(31, medicalExpDeduct_1)
            self.listbox.insert(32, slTaxDeduct_1)
            self.listbox.insert(33, '')
            self.listbox.insert(34, sumItemized_1)
            self.listbox.insert(35, '')
            self.listbox.insert(36, takeItemize_1)
            self.listbox.insert(37, taxableIncome_1)

            # return the following fields, they are needed for the email and save file methods
            return mortgageIntDeduct, mortgageInsDeduct, charitableDeduct, medicalExpDeduct, slTaxDeduct,\
                   sumItemized, itemizeString, itemizeInt, taxableIncome

    # method that saves the file into a CSV format
    def save_file(self):
        try:
            # call the calculateAGI method and get the list of returned items and set varibles
            agi_List = tax_GUI.calculateAGI(self)
            name = agi_List[8]
            status = agi_List[9]
            w2 = agi_List[0]
            capital = agi_List[1]
            rental = agi_List[2]
            scheduleC = agi_List[3]
            retirement = agi_List[4]
            hsaDeduct = agi_List[5]
            stuDeduct = agi_List[6]
            iraDeduct = agi_List[7]
            seTax = agi_List[10]
            agi = agi_List[11]

            # call the calcItemized method and get the list of returned items and set variables
            itemizedList = tax_GUI.calcItemized(self)
            mortgageIntDeduct = itemizedList[0]
            mortgageInsDeduct = itemizedList[1]
            charitableDeduct = itemizedList[2]
            medicalExpDeduct = itemizedList[3]
            slTaxDeduct = itemizedList[4]
            sumItemized = itemizedList[5]
            itemizeString = itemizedList[6]
            itemizeInt = itemizedList[7]
            taxableIncome = itemizedList[8]

        except TypeError:
            tk.messagebox.showerror('ERROR', 'Both AGI and Itemized Field must be filled before saving')

        else:
            # open the save file dialog box once user clicks Save As...
            file_name = tk.filedialog.asksaveasfilename(initialdir = '/',
                                                        filetypes = [('CSV', '*csv')],
                                                        title = 'Select file for saving',
                                                        defaultextension = '*.csv')

            # if filename is not nothing, then save data into CSV file in the format below
            if len(file_name) != 0:
                self.file_var = open(file_name, 'w')

                stringAGI = 'Client Name,{}\nFiling Status,{}\n\nW2 Income,{}\nCapital Gains,{}\n' \
                         'Schedule E Income,{}\nSchedule C Income,{}\nRetirement Income,{}\n\n' \
                         'HSA Deduction,,-{}\nStudent Loan Deduction,,-{}\nIRA Contribution Deduction,,-{}\n' \
                         'Self-Employment Tax,,-{}\n\nAdjusted Gross Income,{}\n\n\n'.format(name, status, w2, capital,
                                                                                       rental, scheduleC, retirement,
                                                                                       hsaDeduct, stuDeduct, iraDeduct,
                                                                                       seTax, agi)

                stringSD = 'Mortgage Interest Deduction,,{}\nMortgage Insurance Deduction,,{}\n' \
                           'Charitable Contributions Deduction,,{}\nMedical Expense Dedcution,,{}\n' \
                           'State & Local Tax Deduction,,{}\n\nTotal Itemized Deduction,,{}\n\n' \
                           '{},-{}\n\nTaxable Income,{}'.format(mortgageIntDeduct, mortgageInsDeduct, charitableDeduct,
                                                               medicalExpDeduct, slTaxDeduct, sumItemized,
                                                               itemizeString, itemizeInt, taxableIncome)

                self.file_var.write(stringAGI + stringSD)
                self.file_var.close()

        # return the filename as it is needed in the email
        return file_name


    # method to email the client with results and attachment of csv file
    def email_client(self):

        # get client name, email, agi and itemize amount
        clientName = str(self.name_entry.get())
        clientEmail = str(self.email_entry.get())

        # call the calcAGI and calcItemize methods to get data needed in email
        agiList = tax_GUI.calculateAGI(self)
        itemizeList = tax_GUI.calcItemized(self)
        agi = agiList[11]
        itemizeString = itemizeList[6]
        itemizeInt = itemizeList[7]
        taxableIncome = itemizeList[8]


        msg = MIMEMultipart()

        # formulate the header, body, and ending of email
        header = ('Dear ' + clientName)
        main = ('Based on the tax documents you have provided, you AGI for 2019 comes out to be $' + str(agi) + '.' + \
                ' As for deduction, ' + str(itemizeString)  + str(itemizeInt) + ' will maximize your tax savings.' + \
                'Your taxable income comes out to be ' + str(taxableIncome) +
                ' The attachment below will give you a breakdown of how those numbers are arrived.')

        ending = ('Please feel free to contact me if you have any questions\n\nKenneth Lin, CPA'
                  '\nQaulity Back Office Llc.\n600 S Washington St #105\nNaperville IL, 60540\n630-802-5485')
        message = f'{header}\n\n{main}\n\n{ending}'

        msg['From'] = 'kennethlin88@gmail.com'
        msg['To'] = clientEmail
        msg['Subject'] = '2019 AGI and Deduction Amount'
        body = message

        msg.attach(MIMEText(body, 'plain'))

        # get filename of attachement by calling the save file method
        filename = tax_GUI.save_file(self)
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session
        s.starttls()
        s.login('kennethlin88@gmail.com', 'pfwv uzar dupt jkop')

        # Converts the Multipart msg into a string
        text = msg.as_string()
        s.sendmail('kennethlin88@gmail.com', clientEmail, text)  # send the email
        s.quit()




















