
class Deductions:
    # set constants
    STATE_LOCAL_TAX_LIMIT = 10000
    MEDICAL_EXP_AGI_LIMIT = 0.1
    CHARITABLE_AGI_LIMIT = 0.6
    MFJ_SD = 24400
    HOH_SD = 18350
    SINGLE_SD = 12200

    # initializes the course object
    def __init__(self, name = '', status = '', mortgageInt = 0.0, mortgageIns = 0.0, charitable = 0.0,
                 medicalExp = 0.0, slIncomeTax = 0.0):
        self.__name = name
        self.__status = status
        self.__mortgageInt = mortgageInt
        self.__mortgageIns = mortgageIns
        self.__charitable = charitable
        self.__medicalExp = medicalExp
        self.__slIncomeTax = slIncomeTax

    # property decorators for getters
    @property
    def name(self):
        return self.__name
    @property
    def status(self):
        return self.__status
    @property
    def mortgageInt(self):
        return self.__mortgageInt
    @property
    def mortgageIns(self):
        return self.__mortgageIns
    @property
    def charitable(self):
        return self.__charitable
    @property
    def medicalExp(self):
        return self.__medicalExp
    @property
    def slIncomeTax(self):
        return self.__slIncomeTax

    # property decorators for setters
    @name.setter
    def name(self, name):
        self.__name = name
    @status.setter
    def status(self, status):
        self.__status = status
    @mortgageInt.setter
    def mortgageInt(self, mortgageInt):
        self.__mortgageInt = mortgageInt
    @mortgageIns.setter
    def mortgageIns(self, mortgageIns):
        self.__mortgageIns = mortgageIns
    @charitable.setter
    def charitable(self, charitable):
        self.__charitable = charitable
    @medicalExp.setter
    def medicalExp(self, medicalExp):
        self.__medicalExp = medicalExp
    @slIncomeTax.setter
    def slIncomeTax(self, slIncomeTax):
        self.__slIncomeTax = slIncomeTax

    # string representation of object (for testing purposes only)
    def __str__(self):
        displayDeductions = str('Name: {}\nStatus: {}\nMortgage Interest: {:,.2f}\n'
                                'Mortgage Insurance: {:,.2f}\nCharitable Contributions: {:,.2f}\n'
                                'Medical Expense: {:,.2f}\nState & Local Tax: {:,.2f}'.format(self.name,
                                                                                              self.status,
                                                                                              self.mortgageInt,
                                                                                              self.mortgageIns,
                                                                                              self.charitable,
                                                                                              self.medicalExp,
                                                                                              self.slIncomeTax))
        return displayDeductions

    # method that calculates the total itemized deduction (takes AGI as an argument)
    def calcTotalItemizedDeduction(self, AGI):
        # state and local income tax deduction cannot be greater than limit
        if self.slIncomeTax > Deductions.STATE_LOCAL_TAX_LIMIT:
            stateTaxDeduct = Deductions.STATE_LOCAL_TAX_LIMIT
        else:
            stateTaxDeduct = self.slIncomeTax

        # Only Medical expenses over 10% of AGI are deductible
        if self.medicalExp > (AGI * Deductions.MEDICAL_EXP_AGI_LIMIT):
            medicalDeduct = self.medicalExp - (AGI * Deductions.MEDICAL_EXP_AGI_LIMIT)
        else:
            medicalDeduct = 0

        # Charitable contributions can be deducted up to 60% of AGI
        if self.charitable > (AGI * Deductions.CHARITABLE_AGI_LIMIT):
            charitableDeduct = (AGI * Deductions.CHARITABLE_AGI_LIMIT)
        else:
            charitableDeduct = self.charitable

        # total itemized deduction is equal to the sum of deductible costs calculated above
        itemizedDeduct = (self.mortgageInt + self.mortgageIns + charitableDeduct + medicalDeduct
                          + stateTaxDeduct)

        # return a list of deductible amounts and total itemized
        return self.mortgageInt, self.mortgageIns, charitableDeduct, medicalDeduct, stateTaxDeduct, itemizedDeduct

    # method that will return whether to take Standard Deduction or Itemized Deduction based on filing status
    def itemizeOrStandard(self, Itemize):
        # if filing status is Married Filing Jointly, take the greater of itemize or standard deduction
        if self.status == 'MFJ':
            if Itemize > Deductions.MFJ_SD:
                deduct = ('Take Itemize Deduction of ', Itemize)
                return deduct
            else:
                deduct = ('Take Standard Deduction of ', Deductions.MFJ_SD)
                return deduct

        #  for filing status Head of Household, take the greater of itemize or standard deduction
        elif self.status == 'HOH':
            if Itemize > Deductions.HOH_SD:
                deduct = ('Take Itemized Deduction of ', Itemize)
                return deduct
            else:
                deduct = ('Take Standard Deduction of ', Deductions.HOH_SD)
                return deduct

        # for all other filing status (single or married filing separate), take the greater of itemize or standard
        else:
            if Itemize > Deductions.SINGLE_SD:
                deduct = ('Take Itemized Deduction of ', Itemize)
                return deduct
            else:
                deduct = ('Take Standard Deduction of ', Deductions.SINGLE_SD)
                return deduct















