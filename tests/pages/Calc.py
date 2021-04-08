from  selenium . webdriver . support  import  expected_conditions  as  EC
from  selenium . webdriver . support . wait  import  WebDriverWait
from  appium . webdriver . common . mobileby  import  MobileBy


class  Calculator :
    def  __init__ ( self , driver ):
        self.driver  =  driver
        self.eq  =  WebDriverWait ( self.driver , 10 ).until ( EC.presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/eq'
        )))
        self.equals  =  WebDriverWait ( self.driver , 10 ).until ( EC.presence_of_element_located ((
            MobileBy.ACCESSIBILITY_ID , 'equals'
        )))
        self.dec_point  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/dec_point'
        )))
        self.delete  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/del'
        )))
        self.divide  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/op_div'
        )))
        self.multiply  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/op_mul'
        )))
        self.minus  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/op_sub'
        )))
        self.plus  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/op_add'
        )))
        self.formula  =  WebDriverWait ( self.driver , 10 ). until ( EC . presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/formula'
        )))

    def final_result (self):
        return WebDriverWait ( self.driver , 10 ). until ( EC.presence_of_element_located ((
            MobileBy . ID , 'com.google.android.calculator:id/result_final'
        ))).text
        #return self.driver.find_element(MobileBy.ID ,'com.google.android.calculator:id/result_final' ).text

    def checkNumArgs (self, numbers):
        if(len(numbers) < 2):
            raise Exception("Minimum of 2 numbers!")

    def  clicknumber ( self , number ):
        _num  =  str ( number )
        for char in _num:
            if(char == '.'):
                self.dec_point.click()
            else:
                num_id  =  'com.google.android.calculator:id/digit_'  + char
                self.driver . find_element ( MobileBy . ID , num_id ). click ()

    def  sum ( self, *args):
        self.checkNumArgs(args)
        result = 0
        
        for i,num in enumerate(args):
            self.clicknumber( num )
            result += num
            if i < len(args)-1:
                self.plus.click()
            
        self.eq.click()
        calcResult = float(self.final_result())
        assert  result  ==  calcResult , 'Different results for sum'

    def  multiplying ( self, *args):
        self.checkNumArgs(args)
        result = 1
        
        for i,num in enumerate(args):
            self.clicknumber( num )
            result = result * num
            if i < len(args)-1:
                self.multiply.click()

        self.eq.click()
        calcResult = float(self.final_result())
        assert  result  ==  calcResult , 'Different results for multiplication'

    def  dividing ( self, *args):
        self.checkNumArgs(args)
        result = args[0]
        
        for i,num in enumerate(args):
            self.clicknumber( num )
            
            if i > 0:
                result = result / num

            if i < len(args)-1:
                self.divide.click()

        self.eq.click()
        calcResult = float(self.final_result())
        assert  result  ==  calcResult , 'Different results for division'