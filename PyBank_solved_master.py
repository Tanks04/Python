
#App works only from console.

import datetime
import os

# GLOBALNE VARIJABLE
company_name = 'Mind$hare'
company_street_and_number = 'Street'
company_postal_code = '10'
company_city = 'City'
company_tax_id = '12341234123'
company_manager = 'John Doe'
currency = 'eur'

#delete this values in order to start fresh.

# Prazan Dictionary u kojem ce biti pohranjene transakcije
transaction_id = 0
transactions = { }

# Format broja racuna: BA-GODINA-MJESEC-Redni_broj 
# BA - Business Account
# Redni_broj - 00001 - 5 znamenki
account_number = 'BA-2023-03-00001'
account_balance = 1000.00
orocenje = 0
orocenje_mj = 0



def prikaz_transakcija():
    global transactions
    global transactions_id
    

    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('ISPIS SVIH TRANSAKCIJA NA RAČUNU\n'.center(65))   


    for kljuc, transakcije in transactions.items():
        print(f'{kljuc}', end="\n")
        for data in transakcije:
            print("{} : {}".format(kljuc, data))
        print()
    
    input("Unesite enter za nastavak!")
    
    return

def polog_novca():
    global account_number
    global company_manager
    global transactions
    global account_balance
    global transaction_id
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('Polog na račun\n'.center(65), '\n')
    print('*' * 65)

    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun: \n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        current_date = datetime.date.today()
        time_now = datetime.datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        
        transaction.append(current_date)
        transaction.append(current_time)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Dodan iznos na račun!')
        transaction.append(company_manager)
        transaction_id += 1
        transactions[transaction_id] = transaction
        print(f'Uspješno ste položili novac i sada imate ukupno {account_balance} novca na računu.')
        input('Pritisnite enter za povratak u menu')
    return

def podizanje_novca():
    
    global account_number
    global company_manager
    global transactions
    global account_balance
    global transaction_id
    
    maxminus = -1000.00 
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('Podizanje novca sa računa\n'.center(65), '\n')
    print('*' * 65)

    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    while True:
        
        print(f'Maksimalni negativni minus iznosi {maxminus:.2f}{currency}.\n')    
        print('Molimo Vas upisite iznos koji zelite podignuti sa računa: \n')
    
        amount = float(input('\t'))
        
        if (account_balance - amount) < maxminus:
            print("Prelazite maximalni dozvoljeni minus!")    
            input("Molim unesite manji iznos!")
            pass
        else:
            transaction = []
            account_balance -= amount

            current_date = datetime.date.today()
            time_now = datetime.datetime.now()
            current_time = time_now.strftime("%H:%M:%S")
        
            transaction.append(current_date)
            transaction.append(current_time)
            transaction.append(amount)
            transaction.append(account_balance)
            transaction.append(account_number)
            transaction.append('Podignut iznos sa računa')
            transaction.append(company_manager)
            transaction_id += 1
            transactions[transaction_id] = transaction
            print(f'Uspješno ste podignuli novac i sada imate ukupno {account_balance} novca na računu.')
            input("Pritisnite enter za povratak u menu.")
            break
    False
    return


def update_account(): #riješeno
    
    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    naziv = ''
    adresa = ''
    postalcode = ''
    grad = ''
    oib = ''
    manager = ''
    valuta = ''
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*' * 65)
        print('PyBank by mind$hare\n'.center(65), '\n')
        print('!!!Broj računa je jedinstven i ne može se mijenjati!!!\n')
        print('Molim daberite iz menija:')
        
        print("\t1. Promjena imena firme\n"
        "\t2. Promjena adrese firme\n"
        "\t3. Promjena poštanskog koda\n"
        "\t4. Promjena središta tvrtke\n"
        "\t5. Promjena odgovorne osobe\n"
        "\t6. Promjena OIB-a tvrtke\n"
        "\t7. Promjena valute\n"
        "\t0. Izlaz\n")

        odabir = int(input('Vas izbor:\t'))

        if odabir == 1:
            print("Tretnutno ime firme:",company_name)
            naziv = input('Unesite novi naziv Tvrtke: ')
            if naziv == '':
                print("Promjena nije unesena!")
                input("Pritisnite enter za nastavak!")
                break
            else:
                company_name = naziv
                print("Uspješna promjena!")
                input("Pritisnite enter za nastavak!")
        elif odabir == 2:
            print("Trenutno je sjedište:",company_street_and_number)
            adresa = input('Unesite novu ulicu i broj sjedišta Tvrtke: ')
            if adresa == '':
                print("Promjena nije unesena!")
                input("Pritisnite enter za nastavak!")
                break
            else:
                company_street_and_number = adresa
                print("Uspješna promjena!")
                input("Pritisnite enter za nastavak!")
        elif odabir == 3:
            print("Trenutni poštanski kod: ", company_postal_code) 
            while True:
                company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
                if not company_postal_code.isdigit():
                    print('Poštanski broj sadrži samo brojeve\nMolimo Vas ponovite unos\n')
                else:
                    break
            print("Uspješna promjena!")
            input("Pritisnite enter za nastavak!")
        elif odabir == 4:
            print("Trenutno je firma u gradu:",company_city)
            grad = input('Grad u kojem je sjediste Tvrtke: ')
            if grad == '':
                print("Promjena nije unesena!")
                input("Pritisnite enter za nastavak!")
                break
            else:
                company_city = grad
                print("Uspješna promjena!")
                input("Pritisnite enter za nastavak!")
        elif odabir == 5:
            print("Trenutni je manager:",company_manager)
            manager = input('Unesite ime i prezime nove odgovorne osobe Tvrtke: ')
            if manager == '':
                print("Promjena nije unesena!")
                input("Pritisnite enter za nastavak!")
                break
            else:
                company_manager = manager
                print("Uspješna promjena!")
                input("Pritisnite enter za nastavak!")
        elif odabir == 6:
            print("Trenutno je OIB:",company_tax_id)
            while True:
                company_tax_id = input('OIB Tvrtke: ')
                # string.isdigit() vraca Ture ako su sve znamenke u stringu brojke
                if len(company_tax_id) != 11 or not company_tax_id.isdigit():
                    print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
                else:
                    print("Uspješna promjena!")
                    input("Pritisnite enter za nastavak!")
        elif odabir == 7:
            print("Trenutna je valuta:",currency)
            currency = input('Upisite naziv valute racuna (EUR ili HRK):')
            if currency.upper() == 'HRK':
                currency = ' hr'
            else:
                currency = ' €'
                print("Uspješna promjena!")
                input("Pritisnite enter za nastavak!")
        elif odabir == 0:
            False
        return

def generate_account_number():
    global account_number

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if month < 10:
        month = str('0' + str(month))
    else:
        month = str(month)

    if account_number == '':
        account_number = 'BA-' + str(year) + '-' + month + '-00001'
    else:
        number_str = account_number.split('-')[-1]
        number = int(number_str)

        if number < 9:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0000' + str(number)
        elif number < 99:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-000' + str(number)
        elif number < 999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-00' + str(number)
        elif number < 9999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0' + str(number)
        else:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-' + str(number)
    
    return account_number

def open_account():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Podaci o vlasniku racuna\n'.center(65))

    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance
    global transaction_id

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    while True:
        company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
        if not company_postal_code.isdigit():
            print('Poštanski broj sadrži samo brojeve\nMolimo Vas ponovite unos\n')
        else:
            break
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')
    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        # string.isdigit() vraca Ture ako su sve znamenke u stringu brojke
        if len(company_tax_id) != 11 or not company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    print()
    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'
    
    input('\nSPREMI? (Pritisnite bilo koju tipku) ')    # Nece spremiti nista, jer su sve izmjene vec spremljene, 
                                                        # ali dobro izgleda :-)


    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')

    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Stanje racuna\n'.center(65), '\n')

    print(f'Broj racuna {generate_account_number()}')

    # {account_balance:.2f} Broj account_balance zaokruzi na dvije decimale SAMO kod prikaza, broj ostaje ne promijenjen
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        # transakcija - datum, vrijeme, iznos, stanje, broj racuna, opis
        current_date = datetime.date.today()
        time_now = datetime.datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        
        transaction.append(current_date)
        transaction.append(current_time)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Polog kod otvaranja racuna')
        transaction.append(company_manager)
        transaction_id += 1
        transactions[transaction_id] = transaction

    else:
        amount = 0.00
    
    return #dodao

def display_account_balance():
    # Detalji o racunu
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('PRIKAZ STANJA RACUNA\n'.center(65), '\n')

    print(f'Broj racuna:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.today()} {datetime.datetime.now()}\n')
    
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n\n')
    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')

    return #dodao

def main_menu():
    global transaction_id
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('*' * 65)
    print('PyBank by mind$hare\n'.center(65), '\n')
    print('GLAVNI IZBORNIK\n'.center(65))

    if company_name == '':
        print('1. Kreiranje racuna')        # Kreiranje podataka
    else:
        print('1. Azuriranje racuna')       # Azuriranje podataka

    print('2. Prikaz stanja racuna')        # Trenutno stanje
    print('3. Prikaz prometa po racunu')    # Dictionary

    print('4. Polog novca na racun')        # Dodaj na racun i kreiraj transakciju
    print('5. Podizanje novca s racuna')    # Oduzmi s racuna i kreiraj transakciju
    print('0. Izlaz')                       # Izadi iz while petlje

    print('_' * 65)
    
    return 


os.system('cls')

main_menu()

while True:
    main_menu()
    print('Molimo Vas upisite samo broj ispred opcije koju zelite odabrati')
    print('-' * 65)
    choice = int(input('Vas izbor:\t'))
    print()

    if company_name == '':
            print('Hvala što ste odabrali našu banku, krećemo sa izradnjom računa!')
            print('-' * 65)
            print()

            input("Pritisni enter za nastavak!")

    if choice == 1 and company_name == '':
        open_account()
    elif choice == 1 and company_name != '':
        update_account()
    elif choice == 2:
        display_account_balance()
    elif choice == 3:
        prikaz_transakcija()
    elif choice == 4: 
        polog_novca()
    elif choice == 5: 
        podizanje_novca()
    elif choice == 0:  
        False
        break
    else:
        print("Neipravan unos!")

        
