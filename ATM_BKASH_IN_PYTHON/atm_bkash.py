import os
import time

password = 1234
user_pin = 12345

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

# ATM balance function
def load_balance():
  try:
    with open('ATM_BKASH_IN_PYTHON\\atm_balance.txt', 'r') as file:
      return int(file.read())
  
  except FileNotFoundError:
    return 10000  # Default balance if the file doesn't exist
  
def save_balance(balance):
  try:
    with open('ATM_BKASH_IN_PYTHON\\atm_balance.txt', 'w') as file:
      file.write(str(balance))
  
  except Exception as e:
    print(f"Error saving balance: {e}")

balance = load_balance()

# bKash balance function
def check_balance():
  try:
    with open("ATM_BKASH_IN_PYTHON\\bkash_balance.txt", "r") as f:
      return int(f.read())
  except FileNotFoundError:
    return 100000

def update_balance(balance):
  with open("ATM_BKASH_IN_PYTHON\\bkash_balance.txt", "w") as f:
    f.write(str(balance))

balance = check_balance()

# Bangladeshi phone number validation function
def valid_phone_number(phone_number):
  phone_number = ''.join(filter(str.isdigit, phone_number))
  if len(phone_number) != 11:
    return False
  if not (phone_number.startswith('014') or phone_number.startswith('019') or phone_number.startswith('017') or phone_number.startswith('015') or phone_number.startswith('018') or phone_number.startswith('016')):
    return False
  if not phone_number[3:].isdigit():
    return False
  return True

# Banglalink phone number validation function
def valid_banglalink(b_number):
  b_number = ''.join(filter(str.isdigit, b_number))
  if len(b_number) != 11:
    return False
  if not (b_number.startswith('014') or b_number.startswith('019')):
    return False
  if not b_number[3:].isdigit():
    return False
  return True

# Grameenphone phone number validation function
def valid_grameen(g_number):
  g_number = ''.join(filter(str.isdigit, g_number))
  if len(g_number) != 11:
    return False
  if not (g_number.startswith('017')):
    return False
  if not g_number[3:].isdigit():
    return False
  return True 

# Teletalk phone number validation function
def valid_teletalk(t_number):
  t_number = ''.join(filter(str.isdigit, t_number))
  if len(t_number) != 11:
    return False
  if not (t_number.startswith('015')):
    return False
  if not t_number[3:].isdigit():
    return False
  return True

# Robi phone number validation function
def valid_robi(r_number):
  r_number = ''.join(filter(str.isdigit, r_number))
  if len(r_number) != 11:
    return False
  if not (r_number.startswith('018')):
    return False
  if not r_number[3:].isdigit():
    return False
  return True

# Airtel phone number validation function
def valid_airtel(a_number):
  a_number = ''.join(filter(str.isdigit, a_number))
  if len(a_number) != 11:
    return False
  if not (a_number.startswith('018')):
    return False
  if not a_number[3:].isdigit():
    return False
  return True

print('''
     =============================== 
    |                               |
    |  Menu:                        |
    |  1. ATM                       |
    |  2. BKASH                     |
    |                               |
     ===============================''')
try:
  method = int(input('''
    ----------------------
    Select Your Option: '''))
  
# This is for ATM
  if method == 1:
    clear_console()
  
    print('''
      --------------------     
      Enter your CARD...
      --------------------''')
  
    time.sleep(3)  # Delay to read card
    clear_console()
    print('''
      ------------------     
      Welcome to ATM
      ------------------''')
    time.sleep(2)
    clear_console()
  
    
    pin = int(
        input('''
      -------------------------
      Enter your ATM PIN: '''))
    clear_console()
  
    if pin == password:
  
      while True:
        print('''
                  
       ______________________________  
      |                              |
      |  Main menu:                  |
      |       1 - View my balance    |
      |       2 - Withdraw cash      |
      |       3 - Deposit funds      |
      |       4 - Exit               |
      |______________________________|''')
  
        try:
          option = int(input('''
      -----------------
      Enter a choice: '''))
          clear_console()
  
          if option == 1:
            print(" ------------------------------------")
            print(f"| Your current balance is {balance}✅    |")
            print(" ------------------------------------")
  
          elif option == 2:
            withdraw_amount = int(
                input('''
      ---------------------------------------
      Please enter withdrawl amount: '''))
            clear_console()
  
            if withdraw_amount <= balance:
              balance -= withdraw_amount
              save_balance(balance)
  
              print("\t----------------------------------------")
              print(f"\t- BD {withdraw_amount} is debited from your account✅")
              print(f"\t- Your current balance is {balance} BD")
              print("\t----------------------------------------")
  
            else:
              print("Insufficient funds...⚠️")
  
          elif option == 3:
            deposit_amount = int(
                input('''
      ---------------------------------------                                         
      Please enter deposit amount: '''))
            clear_console()
  
            if deposit_amount > 0:
              balance += deposit_amount
              save_balance(balance)
  
              print("\t----------------------------------------")
              print(f"\t- BD {deposit_amount} is credited to your account✅")
              print(f"\t- Your current balance is {balance} BD")
              print("\t----------------------------------------")
  
            else:
              print('''
      ----------------------------                        
      Invalid deposit amount...
      ----------------------------''')
  
          elif option == 4:
            print('''
      ----------------------------------------                    
      Thank you for using the 🏧. Goodbye!👋
      ----------------------------------------''')
            break
  
          else:
            print('''
      --------------------------------------                    
      Invalid option. Please try again...🔄
      --------------------------------------''')
            break
  
        except ValueError:
          print('''
      ---------------------------------------                
      Invalid... Please enter a valid number
      ---------------------------------------''')
  
    else:
      print('''
      ---------------        
      Wrong pin!!!❎
      ---------------''')
  
# This is for bKash
  elif method == 2:
    clear_console()
    print('''
        \tCarrier info
    
  ==========================================
  ||                                      ||
  ||\tbKash                             ||
  ||\t1.send money                      ||
  ||\t2.send money to non-bkash user    ||
  ||\t3.mobile recharge                 ||
  ||\t4.payment                         ||
  ||\t5.cash out                        ||
  ||\t6.Check Balance                   ||
  ||                                      ||
  ==========================================''')
    
    
    user_input = int(input('''
  ----------------------                   
  Enter your choice : '''))
  
    if user_input == 1:
      clear_console()
      number = input('''
  
  Enter Receiver bKash Account No: ''')
      clear_console()
      
      if valid_phone_number(number):
        Amount = int(input("  \nEnter Amount: "))
        clear_console()
        Reference = int(input("  \nEnter Reference: "))
        clear_console()
        Pin = int(input("  \nEnter Menu Pin: "))
        if Pin == user_pin:
          clear_console()
          if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print("  \nCongratulations you have successfully send money.😀\n  Number:",
                number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
          else:
            print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
        else:
          clear_console()
          print('\t==========================')
          print('\t\t\tWrong pin😔')
          print('\t==========================')
      else:
        print('''
  --------------------------------
  The bkash Account No is invalid.
  --------------------------------''')
  
    elif user_input == 2:
      clear_console()
      number = input('''
                     
  Enter Receiver bKash Account No: ''')
      clear_console()

      if valid_phone_number(number):
        Amount = int(input("  \nAmount: "))
        clear_console()
        Reference = int(input("  \nReference: "))
        clear_console()
        pin = int(input("  \nEnter Menu Pin: "))
        if pin == user_pin:
          clear_console()
          if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print("  \nCongratulations😀\n  Send Money to non-bkash user is Successful. \n  Number:",
                number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
          else:
            print('''
  -----------------------------                
  You do not have enough money.
  -----------------------------''')
        else:
          clear_console()
          print('\t=============================================')
          print('\t\t\tWrong pin😔')
          print('\t=============================================')
      else:
        print('''
  --------------------------------            
  The bkash Account No is invalid.
  --------------------------------''')
  
    elif user_input == 3:
  
      clear_console()
      print("\n  1. Banglalink")
      print("  2. GrameenPhone")
      print("  3. Teletalk")
      print("  4. Robi")
      print("  5. Airtel")

      user_sim = int(input('''
  -------------------                         
  Select Your Sim: '''))
  
      if user_sim == 1:
        clear_console()
        b_number = input("\n  Enter Banglalink Number: ")
        clear_console()

        if valid_banglalink(b_number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
    
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                    b_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------                  
  You do not have enough money.
  -----------------------------''')
    
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  ----------------------------------              
  Invalid Banglalink Number Entered.
  ----------------------------------''')
  
      elif user_sim == 2:
  
        clear_console()
        g_number = input("\n  Enter GrameenPhone Number: ")
        clear_console()

        if valid_grameen(g_number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
    
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                    g_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  ------------------------------------              
  Invalid Grameenphone number entered.
  ------------------------------------''')
  
      elif user_sim == 3:
        clear_console()
        t_number = input("\n  Enter Teletalk Number: ")
        clear_console()

        if valid_teletalk(t_number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
    
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                    t_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  --------------------------------              
  Invalid Teletalk number entered.
  --------------------------------''')
  
      elif user_sim == 4:
        clear_console()
        r_number = input("\n  Enter Robi Number: ")
        clear_console()

        if valid_robi(r_number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
    
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                    r_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  ----------------------------              
  Invalid Robi number entered.
  ----------------------------''')
          
      elif user_sim == 5:
        clear_console()
        a_number = input("\n  Enter Airtel Number: ")
        clear_console()

        if valid_airtel(a_number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
    
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                    a_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  ----------------------------              
  Invalid Airtel number entered.
  ----------------------------''')
  
    elif user_input == 4:
      clear_console()
      number = input("\n  Enter Your Merchant Account: ")
      clear_console()

      if valid_phone_number(number):
        Amount = int(input("\n  Enter Your Amount: "))
        clear_console()
        Reference = int(input("\n  Enter Reference: "))
        clear_console()
        pin = int(input("\n  Enter Menu PIN to confirm: "))
        if pin == user_pin:
          clear_console()
          if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print("  \nCongratulations\n  Your Payment is successfull. \n  To:", number,
                  "\n  Amount:", Amount, "\n  Current Amount:", balance)
          else:
            print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
        else:
          clear_console()
          print('\t=============================================')
          print('\t\t\tWrong pin😔')
          print('\t=============================================')
      else:
        print('''
  --------------------------------              
  The bkash Account No is invalid.
  --------------------------------''')
  
    elif user_input == 5:
      clear_console()
      print('''
  ---------------------------------------------
  Only Agent Number can transfer money.
  If you are agreed please enter either 1 or 2''')
      user_decision = int(input("  "))
      if user_decision == 1:
        clear_console()
        number = input("\n  Enter Receiver Number: ")
        clear_console()

        if valid_phone_number(number):
          Amount = int(input("\n  Enter Amount: "))
          clear_console()
          pin = int(input("\n  Enter Menu PIN to confirm: "))
          if pin == user_pin:
            clear_console()
            if Amount <= balance:
              balance -= Amount
              update_balance(balance)
              print("  \nCongratulations\n  Your Cash Out is successful. \n  To:", number,
                    "\n  Amount:", Amount, "\n  Current Amount:", balance)
            else:
              print('''
  -----------------------------
  You do not have enough money.
  -----------------------------''')
          else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tWrong pin😔')
            print('\t=============================================')
        else:
          print('''
  --------------------------------              
  The bkash Account No is invalid.
  --------------------------------''')

      elif user_decision == 2:
        clear_console()

    elif user_input == 6:
      clear_console()
      pin = int(input("\n  Enter Menu PIN: "))
      if pin == user_pin:
        clear_console()
        print(f"\n  Your current bKash Account balance is\n  TK {balance}. Your available bKash Account\n  balance is Tk {balance}. bKash App diye\n  balance check ekdom simple!")
      else:
        print("Wrong PIN.")

    else:
      clear_console()
      print('''
  ----------------------------         
  You Entered Wrong Number😥
  ----------------------------''')
  else:
    clear_console()
    print('''
  ---------------------------        
  You Entered Wrong Number😥
  ---------------------------''')
except:
  print('''
  -------------------     
  Invalid entered!!!
  -------------------''')
