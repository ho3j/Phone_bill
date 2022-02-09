"""
Hossein Jalili
feb-9-2022
version 1.0.0
Issuance of telephone bill in Isfahan province of Iran

"""

from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import jdatetime
import subprocess
import platform
import getpass
import socket

#----------------------------------------------
clear=lambda : os.system("cls")
# jdatetime.set_locale('fa_IR')
now = jdatetime.datetime.now()
#----------------------------------------------

# print("*** start ***")
def ghabz():
    i=1
    lines=[]
    while True:
        print("---------------- try",str(i)," -----------------")
        tell_number=input('\nTell number: for example: 3134252697\n')
        print('\nyour number is: '+tell_number,"\n")
        if tell_number.isdigit()==False:
            clear()
            print('\nplease enter a valid number(0-9)\n')
            i += 1
            
        else:
            if len(tell_number)==10:
                # q=input("Enter 'y' to download png : \n")
                break
            else:
                i += 1
                clear()
                print('\nplease enter a valid 11_number (3134252697)\n')
                
    #----------------------------------------------

    path = os.path.dirname(os.path.abspath(__file__))
    address=os.path.join(path, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=address)
    driver.get('https://my.tci.ir/bill/'+tell_number)
    # driver.get('https://my.tci.ir/bill/3133383652')

    #----------------------------------------------
    time.sleep(10)
    try:
        pic_download=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/button')
    except:
        pic_download="can't connect to server"
    try:
        start_period=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[3]/div[1]/p[2]').text)
    except:
        start_period="can't connect to server"
    try:
        end_period=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[4]/div[1]/p[2]').text)
    except:
        end_period="can't connect to server"
    try:
        payment_dead_line=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/p[2]').text)
    except:
        payment_dead_line="can't connect to server"
    try:
        membership_right=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/p').text)
    except:
        membership_right="can't connect to server"
    try:
        Duties_and_taxes=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div[2]/p').text)
    except:
        Duties_and_taxes="can't connect to server"
    try:
        Bill=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[4]/div[2]/p').text)
    except:
        Bill="can't connect to server"
    try:
        Previous_debt=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[5]/div[2]/p').text)
    except:
        Previous_debt="can't connect to server"
    try:
        Correction_amount=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div[2]/div[2]/p[2]').text)
    except:
        Correction_amount="can't connect to server"
    try:
        Rial_cost_deduction=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div[3]/div[2]/p[2]').text)
    except:
        Rial_cost_deduction="can't connect to server"
    try:
        The_amount_payable_to_the_bank=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div[4]/div[2]/p[2]').text)
    except:
        The_amount_payable_to_the_bank="can't connect to server"
    try:
        Billing_ID=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/p[2]').text)
    except:
        Billing_ID="can't connect to server"
    try:
        Payment_code=(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[3]/p[2]').text)
    except:
        Payment_code="can't connect to server"
    time.sleep(2)
    clear()

    print("---------------- try",str(i)," -----------------")
    print("Today is: ",now)
    print('your number is: '+tell_number,"\n")

    print("Billing ID :\t\t",Billing_ID)
    print("Payment code :\t\t",Payment_code)
    print("payment dead-line :\t",payment_dead_line,"\n")

    print("start period :\t\t",start_period)
    print("end period :\t\t",end_period)
    print("membership right :\t",membership_right)
    print("Duties and taxes :\t",Duties_and_taxes)
    print("Bill :\t\t\t",Bill)
    print("Previous debt :\t\t",Previous_debt,"\n")

    print("Correction amount :\t",Correction_amount)
    print("Rial cost deduction :\t",Rial_cost_deduction)
    rrr=''.join([n for n in The_amount_payable_to_the_bank if n.isdigit()])
    print("\nThe amount payable to the bank : ",rrr,"Rial")

    if t.startswith('Y') or t.startswith('y'):
        try:
            lines=lines+[
            " Issuance of telephone bill in Isfahan province of Iran",
            "\nToday is:             ",str(now),
            '\nyour number is:       ',str(tell_number),
            "\nBilling ID :          ",str(Billing_ID),
            "\nPayment code :        ",str(Payment_code),
            "\npayment dead-line :   ",str(payment_dead_line),
            "\nstart period :        ",str(start_period),
            "\nend period :          ",str(end_period),
            "\nmembership right :    ",str(membership_right),
            "\nDuties and taxes :    ",str(Duties_and_taxes),
            "\nBill :                ",str(Bill),
            "\nPrevious debt :       ",str(Previous_debt),
            "\nCorrection amount :   ",str(Correction_amount),
            "\nRial cost deduction : ",str(Rial_cost_deduction),
            "\nThe amount payable to the bank------> : ",str(rrr)]
            # print(lines)
            t_time="-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.second)              
            
            with open(str(tell_number)+t_time+'.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
        except:
            print("\ncan't save file")

    if q.startswith('Y') or q.startswith('y'):
        try:
            pic_download.send_keys(Keys.ENTER)
            # print("\nfind button of Download")
            print("\ndownload png is done.\n")
        except:
            print("\ncan't find button of Download")
    else:
        pass

    print("\n10 sec utill quit ")
    time.sleep(10)
    driver.quit()
    # print("\nquit is done\n")
    print("----------------------------------------------")

clear()
while True:
    clear()
    print("\nDeveloped by #ho3j ")
    print("____________________________________")
    try:
        
        host_name = socket.gethostname()
        ip_addr = socket.gethostbyname(host_name)
        print("os : \t\t\t",platform.system())
        print("Windows version : \t",platform.release())
        # print("Windows 32/64bit : \t",platform.machine())
        # print("Windows User : \t\t",getpass.getuser())
        print ("Host Name: \t\t {0}".format(host_name))
        print ("IP Address: \t\t {0}".format(ip_addr))
    except:
        print("can not print Information of windows ")

    try:
        print("____________________________________\n")
        print("                Hi, Good Luck ",getpass.getuser())
        # print("----------")
        print("""
                    Issuance of 
          telephone bill in Isfahan province
        |*************************************|
        |   1 :  Show only in the app         |
        |   2 :  View and with download png   |
        |   3 :  View and with save txt file  |
        |   4 :  viwe and save and download   |
        |   5 :  quit app                     |
        ***************************************
        """)
        i=int(input("Enter number of function :\t"))
        if i ==1:
            
            q="n"
            t="n"
            ghabz()
        elif i==2:
            q="y"
            t="n"
            ghabz()
        elif i==3:
            q="n"
            t="y"
            ghabz()
        elif i==4:
            q="y"
            t="y"
            ghabz()
        elif i==5:
            break
        else :
            clear()
            print("wrong  number !!! " ,end="\n \n")
            print( end=" ")
            qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
            if qq =="q" :
                break
            else :
                clear()
                continue
    except:
        clear()
        print("Enter number !")

#----------------------------------------------

