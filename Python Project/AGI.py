


# define gross income class
class GrossIncome:

    # make these class constants
    IRA_LIMIT = 6000
    STUDENT_LOAN_LIMIT = 2500
    HSA_SINGLE_LIMIT = 3500

    # initilizes the gross income object with initial chracteristics
    def __init__(self, name = '', status = '', w2 = 0.0, capital = 0.0, rental = 0.0, scheduleC = 0.0,
                 retirement = 0.0):
        self.__name = name
        self.__status = status
        self.__w2 = w2
        self.__capital = capital
        self.__rental = rental
        self.__scheduleC = scheduleC
        self.__retirement = retirement

    # use property decorators for getters
    @property
    def name(self):
        return self.__name
    @property
    def status(self):
        return self.__status
    @property
    def w2(self):
        return self.__w2
    @property
    def capital(self):
        return self.__capital
    @property
    def rental(self):
        return self.__rental
    @property
    def scheduleC(self):
        return self.__scheduleC
    @property
    def retirement(self):
        return self.__retirement

    # user property decorators for setters
    @name.setter
    def name(self, name):
        self.__name = name
    @status.setter
    def status(self, status):
        self.__status = status
    @w2.setter
    def w2(self, w2):
        self.__w2 = w2
    @capital.setter
    def capital(self, capital):
        self.__capital = capital
    @rental.setter
    def rental(self, rental):
        self.__rental = rental
    @scheduleC.setter
    def scheduleC(self, scheduleC):
        self.__scheduleC = scheduleC
    @retirement.setter
    def retirement(self, retirement):
        return self.__retirement

    # create a string representation of object state (used for testing purposes only)
    def __str__(self):
        displayIncome = str('Name: {}\nStatus: {}\nW2: {:,.2f}\nCapital gain/loss: {:,.2f}\nRental Income: {:,.2f}\n'
                            'Schedule C Income: {:,.2f}\nRetirement Income: {:,.2f}'.format(self.name,
                                                                                            self.status,
                                                                                            self.w2,
                                                                                            self.capital,
                                                                                            self.rental,
                                                                                            self.scheduleC,
                                                                                            self.retirement))

        return displayIncome

    # method to calculate Gross Income
    def calcAGI(self):
        agi = self.w2 + self.capital + self.rental + self.scheduleC + self.retirement
        return agi

# create AGI class, which is a sub-class of Gross Income
class AGI(GrossIncome):
    def __init__(self, name = '', status = '', w2 = 0.0, capital = 0.0, rental = 0.0, scheduleC = 0.0,
                 retirement = 0.0, HSA = 0.0, stuloanInt = 0.0, IRA = 0.0, SE_tax = 0.0):

        # it is going to inherit all properties of gross income and adds more properties
        GrossIncome.__init__(self, name, status, w2, capital, rental, scheduleC, retirement)
        self.__HSA = HSA
        self.__stuloanInt = stuloanInt
        self.__IRA = IRA
        self.__SE_tax = SE_tax

    # use property deocrators for getters
    @property
    def HSA(self):
        return self.__HSA
    @property
    def stuloanInt(self):
        return self.__stuloanInt
    @property
    def IRA(self):
        return self.__IRA
    @property
    def SE_tax(self):
        return self.__SE_tax

    # user property decorators for setters
    @HSA.setter
    def HSA(self, HSA):
        self.__HSA = HSA
    @stuloanInt.setter
    def stuloanInt(self, stuloanInt):
        self.__stuloanInt = stuloanInt
    @IRA.setter
    def IRA(self, IRA):
        self.__IRA = IRA
    @SE_tax.setter
    def SE_tax(self, SE_tax):
        self.__SE_tax = SE_tax

    # create string representation of AGI (for testing purposes only
    def __str__(self):
        displayAGI = GrossIncome.__str__(self) + str('\nHSA: ({:,.2f})\nStudent Loan Interest: ({:,.2f})\n'
                    'IRA Contribution: ({:,.2f})\nSelf Employment Tax: ({:,.2f})'.format(self.__HSA, self.__stuloanInt,
                                                                                         self.__IRA, self.__SE_tax))

        return displayAGI

    # method to calculate the AGI
    def calcAGI(self):
        # deductible self employment tax 50% of actual self-employment taxes actually paid
        seTaxDeduct = self.SE_tax / 2

        # if contributed IRA is greater than deductible limit, then deductible limit is the limit
        if self.IRA > GrossIncome.IRA_LIMIT:
            iraDeduct = GrossIncome.IRA_LIMIT
        else:
            # if its less than limit, then take the actual amount
            iraDeduct = self.IRA

        # deductible student loan amount cannot be greater than deductible limit
        if self.stuloanInt > GrossIncome.STUDENT_LOAN_LIMIT:
            stuDeduct = GrossIncome.STUDENT_LOAN_LIMIT
        else:
            stuDeduct = self.stuloanInt

        # Health Saving Deduction is based on the filing status and limits are set accordingly
        if self.status == 'mfj'.upper() or self.status == 'hoh'.upper():
            if self.HSA > GrossIncome.HSA_SINGLE_LIMIT * 2:
                hsaDeduct = GrossIncome.HSA_SINGLE_LIMIT * 2
            else:
                hsaDeduct = self.HSA
        else:
            if self.HSA > GrossIncome.HSA_SINGLE_LIMIT:
                hsaDeduct = GrossIncome.HSA_SINGLE_LIMIT
            else:
                hsaDeduct = self.HSA

        # agi is calculated as Gross Income subtract the deduction allowed for above categories
        agi = (self.w2 + self.capital + self.rental + self.scheduleC + self.retirement
               - hsaDeduct - stuDeduct - iraDeduct - seTaxDeduct)

        # return the deductible allowed for each category and the actual agi
        return hsaDeduct, stuDeduct, iraDeduct, seTaxDeduct, agi






















