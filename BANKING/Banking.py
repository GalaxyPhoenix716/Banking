from datetime import *
import random

sacc = {}                  #Current Account feature coming soon
loanlist = {}  
acc_stmt = {}
memberinfo = {}
def withdrawl(name) :
    if wth_name in sacc :                   #Here Account is being checked if it exists or not
        wth_ask = int(input("Enter amount you want to withdraw \n"))
        if wth_ask > sacc[wth_name] :               #Here account balance is being checked
            print("Insufficient balance")
        else:
            sacc[wth_name] = sacc[wth_name] - wth_ask 
            print(wth_ask,"got withdrawn \nYour new account balance is",sacc[wth_name])
            print("Reciept will be sent on your phone")
            memberinfo[wth_name]['Balance'] = sacc[wth_name]
            #Account Statement function
            if wth_name in acc_stmt :
                nt = {}
                nt['Withdrawl Amount'] = wth_ask
                nt_ = {}
                today = str(datetime.now())
                nt_[today] = nt
                nt_ = str(nt_)
                acc_stmt[wth_name] = acc_stmt[wth_name] + ',' + nt_
            else :
                t = {}
                t_ = {}
                t['Withdrawl Amount'] = wth_ask
                today = str(datetime.now())
                t_[today] = t
                t_ = str(t_)
                acc_stmt[wth_name] = t_
    else :
        print("Account do not exist")

def deposit(name) :                        #Cheque Deposit feature coming soon
    if dep_name in sacc :                       #Here Account is being checked if it exists or not
        dep_ask = int(input("Enter amount you want to deposit \n"))
        sacc[dep_name] = sacc[dep_name] + dep_ask 
        print(dep_ask,"got deposited \nYour new account balance is",sacc[dep_name])
        memberinfo[dep_name]['Balance'] = sacc[dep_name]
        #Account Statement function
        if wth_name in acc_stmt :
            nt = {}
            nt['Deposited Amount'] = dep_ask
            nt_ = {}
            today = str(datetime.now())
            nt_[today] = nt
            nt_ = str(nt_)
            acc_stmt[dep_name] = acc_stmt[dep_name] + ',' + nt_
        else :
            t = {}
            t_ = {}
            t['Deposited Amount'] = dep_ask
            today = str(datetime.now())
            t_[today] = t
            t_ = str(t_)
            acc_stmt[dep_name] = t_
    else :
        print("Account do not exist")

def transfer(sender,reciever) : 
    #Transfer Part
    if trf_sender in sacc and trf_rec in sacc :                     #Here Accounts are being checked if they exist or not
        trf_ask = int(input("Enter amount you want to transfer \n"))
        if trf_ask < sacc[trf_sender] :
            sacc[trf_sender] = sacc[trf_sender] - trf_ask
            sacc[trf_rec] = sacc[trf_rec] + trf_ask
            print(trf_ask,"got transferred to",trf_rec,"\nYour new account balance is",sacc[trf_sender])
            memberinfo[trf_sender]['Balance'] = sacc[trf_sender]
            memberinfo[trf_rec]['Balance'] = sacc[trf_rec]
            
            #Account Statement Function

            if trf_sender in acc_stmt :
                nt = {}
                nt['Transferred Amount'] = trf_ask
                nt['Transferred To'] = trf_rec
                nt_ = {}
                today = str(datetime.now())
                nt_[today] = nt
                nt_ = str(nt_)
                acc_stmt[trf_sender] = acc_stmt[trf_sender] + ',' + nt_
            else :
                t = {}
                t_ = {}
                t['Transferred Amount'] = trf_ask
                t['Transferred To'] = trf_rec
                today = str(datetime.now())
                t_[today] = t
                t_ = str(t_)
                acc_stmt[trf_sender] = t_
            if trf_rec in acc_stmt :
                nt = {}
                nt['Recieved Amount'] = trf_ask
                nt['Recieved From'] = trf_sender
                nt_ = {}
                today = str(datetime.now())
                nt_[today] = nt
                nt_ = str(nt_)
                acc_stmt[trf_rec] = acc_stmt[trf_rec] + ',' + nt_
            else :
                t = {}
                t_ = {}
                t['Recieved Amount'] = trf_ask
                t['Recieved From'] = trf_sender
                today = str(datetime.now())
                t_[today] = t
                t_ = str(t_)
                acc_stmt[trf_rec] = t_
        else :
            print("Insufficient Balance")
    elif trf_sender not in sacc and trf_rec in sacc:
        print(trf_sender,"Account do not exist")
    elif trf_rec not in sacc and trf_sender in sacc:
        print(trf_rec,"Account do not exist")
    else:
        print("Both accounts do not exist")

def acc_balance(name) :
    if acc_name in sacc :
        print("---------------------------------")
        print("| Account Name |     Balance    |")
        print("---------------------------------")
        print("|    ",acc_name,"   |    ",sacc[acc_name],"    |")
        print("---------------------------------")
    else :
        print("Account do not exist")

def loan(name) :
    d={}
    if (loan_name in sacc and loan_name not in loanlist) or (loan_name in sacc and 'Date of Payment' not in loanlist[loan_name]):
        ln_mdg = int(input("Enter you mortgage value \n"))
        ln_ask = int(input("How much amount you need as loan \n"))
        if ln_ask > ln_mdg :                        #Here your mortgage value will be compared with your ask
            print("Your loan credit value is less than your ask")
        else:
            print("You have to return your loan in maximum 10 years")
            ln_interest = (ln_ask*10*10)/100
            ln_amt = ln_ask + ln_interest
            print(f"You have to pay {ln_amt} in 10 years and your yearly interest will be {ln_interest/10}")
            print(f"Your monthly payment will be {ln_amt/120} with monthly interest {ln_interest/120}")
            ln_confirm = input("Do you want to proceed? \n")
            if ln_confirm == "yes" or loan_ans == "Yes" :
                
                #Loan Records Part

                ln_age = int(input("Enter your age \n"))
                d['Name'] = loan_name
                d['Age'] = ln_age
                d["Mortgage Value"] = ln_mdg
                d['Loan Value'] = ln_ask
                d['Loan Interest'] = ln_interest
                d['Loan Amount'] = ln_amt
                d['Monthly Loan Interest'] = ln_interest/120
                d['Monthly Loan Amount'] = ln_amt/120
                d['Payment Left'] = ln_amt
                d['Date of Issuing Loan'] = str(date.today())
                loanlist[loan_name] = d
                loanlist[loan_name] = d
                print("Name :",loan_name,"\nAge :",ln_age,"\nLoan Value :",ln_ask,"\nLoan Amount :",ln_amt)
                print("Loan Sactioned!")
                sacc[loan_name] = sacc[loan_name] + ln_ask
                print(ln_ask,"got deposited \nYour new account balance is",sacc[loan_name])
                memberinfo[loan_name]['Balance'] = sacc[loan_name]
            elif ln_confirm == "no" or loan_ans == "No" :
                print("Okay!")
    elif loan_name in loanlist :
        print("Please pay off your previous loan first")
    else :
        print("Account do not exist")        

def loanpayoff() :
    lr_name = input("Enter your account name \n")
    if lr_name in loanlist :
        lr_paytype = input("\nEMI , Early payment or On time payment? \n")
        if lr_paytype == 'early' :
            print("Your loan details are ~\n")
            for lrtitles,lrvalues in loanlist[lr_name].items() :
                print(lrtitles,":",lrvalues)
            months = int(input("Enter months you are paying in \n"))
            t_amt = print(f"You have to pay {loanlist[lr_name]['Monthly Loan Amount']*months}")
            lr_paymode = int(input("Payment mode ~\n1) Cash \n2) Balance\n==> "))
            if lr_paymode == 1 :
                print("\nPayment Completed!")
            elif lr_paymode == 2 :
                print("\nPayment Proceeding...")
                sacc[lr_name] = sacc[lr_name] - t_amt
                print("Payment Completed")
            else :
                print("Invalid Payment Mode")
            paydate = str(date.today())
            loanlist[lr_name]['Date of Payemnt'] = paydate
            loanlist[lr_name]['Payment Left'] = 0
        elif lr_paytype == 'on time' :
            print("Your loan details are ~\n")
            for lrtitles,lrvalues in loanlist[lr_name].items() :
                print(lrtitles,":",lrvalues)
            print(f"You have to pay {loanlist[lr_name]['Loan Amount']}")
            lr_paymode = int(input("Payment mode ~\n1) Cash \n2) Balance\n==> "))
            if lr_paymode == 1 :
                print("\nPayment Completed!")
            elif lr_paymode == 2 :
                print("\nPayment Proceeding...")
                sacc[lr_name] = sacc[lr_name] - loanlist[lr_name]['Loan Amount']
                print("Payment Completed")
            else :
                print("Invalid Payment Mode")
            paydate = str(date.today())
            loanlist[lr_name]['Date of Payemnt'] = paydate
            loanlist[lr_name]['Payment Left'] = 0
        elif lr_paytype == 'emi' :
            print("Your loan details are ~\n")
            for lrtitles,lrvalues in loanlist[lr_name].items() :
                print(lrtitles,":",lrvalues)
            print(f"You have to pay {loanlist[lr_name]['Monthly Loan Amount']}")
            lr_paymode = int(input("Payment mode ~\n1) Cash \n2) Balance\n==> "))
            if lr_paymode == 1 :
                print("\nPayment Completed!")
            elif lr_paymode == 2 :
                print("\nPayment Proceeding...")
                sacc[lr_name] = sacc[lr_name] - loanlist[lr_name]['Monthly Loan Amount']
                print("Your EMI Payment is Completed")
            else :
                print("Invalid Payment Mode")
            loanlist[lr_name]['Payment Left'] = loanlist[lr_name]['Payment Left'] - loanlist[lr_name]['Monthly Loan Amount']
            if loanlist[lr_name]['Payment Left'] == 0 :
                paydate = str(date.today())
                loanlist[lr_name]['Date of Payemnt'] = paydate
        else:
            print("Invalid!")
        memberinfo[lr_name]['Balance'] = sacc[lr_name]
    else :
        print("This account haven't taken any loan")

print("\t\t\t\tWELCOME TO PHOENIX BANKS \nHow may we help you?")
print("1) Withdrawl \n2) Deposit \n3) Transfer \n4) Account Balance \n5) Loan \n6) New Account \n7) Remove Existing Account \n8) Account Statement \n9) Account Updation\n10) Loan Payment\n")
while True :
    ans = input("\n==> ")
    print()
    if ans == '1':
        wth_name = input("Enter your account name \n")
        withdrawl(wth_name)
    elif ans == '2':
        dep_name = input("Enter your account name \n")
        deposit(dep_name)
    elif ans == '3':
        trf_sender = input("Enter sender's account name \n")
        trf_rec = input("Enter receiver's account name \n")
        transfer(trf_sender,trf_rec)
    elif ans == '4':
        acc_name = input("Enter your account name \n")
        acc_balance(acc_name)
    elif ans == '5':
        print("Our loan interest rate is 10% and you have to pay it in 10 years")
        loan_ans = input("Do you wish to take the loan with it? \n")
        if loan_ans == "yes" or loan_ans == "Yes" :
            loan_name = input("Enter your account name \n")
            loan(loan_name)
        elif loan_ans == "no" or loan_ans == "No" :
            print("Okay!")
    elif ans == '6':
        nacc_name = input("Enter your Name \n")
        nacc_contact = input("Enter your phone number \n")
        nacc_address = input("Enter your address \n")
        nacc_adhaar = int(input("Enter your adhaar number \n"))
        nacc_bal = int(input("Enter starting amount \n"))
        sacc[nacc_name] = nacc_bal
        nacc_record = {}
        nacc_accno = random.randrange(100000000000,999999999999)
        nacc_record['Account Number'] = nacc_accno
        nacc_record['Name'] = nacc_name
        nacc_record['Contact'] = nacc_contact
        nacc_record['Adhaar Number'] = nacc_adhaar
        nacc_record['Address'] = nacc_address
        nacc_record['Balance'] = sacc[nacc_name]
        nacc_date = str(date.today())
        nacc_record['Date of Account Creation'] = nacc_date
        nacc_record['Date of Account Deletion'] = None
        memberinfo[nacc_name] = nacc_record
        print(f"Account succesfully created!\n\nYour details are ~\nAccount Number : {nacc_accno} \nName : {nacc_name} \nContact : {nacc_contact} \nAdhaar Number : {nacc_adhaar} \nAddress : {nacc_address} \nInitial Amount : {nacc_bal} \nDate of Account Creation : {nacc_date} ")
    elif ans == '7':
        racc_name = input("Enter your Name \n")
        if racc_name in sacc :
            r_ask_cnf = input("Do you really want to remove you account? \n")
            if r_ask_cnf == "yes" or r_ask_cnf == "Yes" :
                del sacc[racc_name]
                racc_date = str(date.today())
                memberinfo[racc_name]['Date of Account Deletion'] = racc_date
                print("Account deleted")
            elif r_ask_cnf == "no" or r_ask_cnf == "No" :
                print("Okay!")
        else :
            print("Account do not exist")
    elif ans == '8':
        acc_stmt_name = input("Enter your account name \n")
        print()
        if acc_stmt_name in sacc :
            if acc_stmt_name in acc_stmt :
                split = acc_stmt[acc_stmt_name].split('},{')
                for hehe in split[::-1] :
                    hehe = hehe.replace('{','')
                    hehe = hehe.replace('}','')
                    hehe = hehe.replace("'",'')
                    print(hehe)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else :
                print("account has no transactions")
        else :
            print("Account do not exist")
    elif ans == '9' :
        acc_upd_name = input("Enter your account name \n")
        if acc_upd_name in sacc :
            acc_upd_ask = input("what would you like to update? \n")
            if acc_upd_ask in ('Contact','Address'):
                acc_upd_detail = input("Enter new details \n")
                conf = input(f"Confirm new detail~ {acc_upd_ask} : {acc_upd_detail} \n")
                if conf == 'yes' or conf == 'Yes' :
                    memberinfo[acc_upd_name][acc_upd_ask] = acc_upd_detail
                    print("Updating Details....")
                    print("Details Updated!")
                elif conf == 'no' or conf == 'No' :
                    print("Enter correct details")
            elif acc_upd_ask == 'Name' :
                acc_upd_newname = input("Enter new Name \n")
                conf = input(f"Confirm new detail {acc_upd_newname} \n")
                if conf == 'yes' or conf == 'Yes' :
                    memberinfo[acc_upd_name][acc_upd_ask] = acc_upd_newname
                    acc_upd_newdetail = memberinfo[acc_upd_name].copy()
                    memberinfo[acc_upd_newname] = acc_upd_newdetail
                    del memberinfo[acc_upd_name]
                    newnameacc = sacc[acc_upd_name]
                    sacc[acc_upd_newname] = newnameacc
                    del sacc[acc_upd_name]
                    print("Updating Details....")
                    print("Details Updated!")
                elif conf == 'no' or conf == 'No' :
                    print("Enter correct name")
            else:
                print('There are no such details')
        else :
            print("Account do not exist")
    elif ans == '10' :
        loanpayoff()
    elif ans == '0':
        print("Shutting Down...")
        break
    elif ans == 'show accounts' :
        print("\t\t\t\tACCOUNTS\t\t\t\t")
        for accname,accnamekabal in sacc.items() :
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(accname,'     ~     ',accnamekabal)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    elif ans == 'show loans' :
        print("\t\t\t\tLOANS\t\t\t\t")
        for lname,ldetails in loanlist.items() :
            print(lname.upper(),"~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for lnamekeandarkedetails,jobhiholme in ldetails.items() :
                print(lnamekeandarkedetails,":",jobhiholme)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif ans == 'show members' :
        print("\t\t\t\tMEMBERS\t\t\t\t")
        for miname,midetails in memberinfo.items() :
            #print(miname.upper(),"~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for minamekeandarkedetails,jobhiho in midetails.items() :
                print(minamekeandarkedetails,":",jobhiho)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else :
        print("\nInvalid Function Entered!")
    print("\nAnything else we could help you with?")