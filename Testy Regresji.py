from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)

###############TEST 1 - Logowanie ####################
def logowanie():
    try:
        driver.get("http://localhost:28555/")
        driver.maximize_window()
        time.sleep(2)
        log = driver.find_element_by_name('login')
        log.send_keys('admin@xopero.com')

        pas = driver.find_element_by_id('mat-input-1')
        pas.send_keys('Admin_123')

        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/app-auth/div/app-auth-login/div/form/app-save-button/button').click()
        time.sleep(1)
        title = driver.current_url
        if title == 'http://localhost:28555/devices':
            print ("Test 1 - Logowanie: Pass")
            return
        else:
            print("Test 1 - Logowanie: Failed")
            return
    except:
        print("Test 1 - Logowanie: Failed")
        exit()


#################Test 2 - Dodawanie urządzenia#############
def dodanieUrzadzenia():
    try:
        if driver.find_element_by_id("mat-badge-content-0").is_displayed():
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[2]/button[1]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="mat-checkbox-2"]/label/span[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-activate-devices-table/div/div[4]/app-save-button/button/span[1]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//app-license[2]/p').click()
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-licenses-list/div/div[4]/app-save-button/button/span[1]/span').click()
            print('Test 2 - Dodawanie urządzenia: Pass')
            return
        else:
            print('Test 2 - Dodawanie urządzenia: Pass(Brak urządzeń do dodania)')
            return
    except:
        print('Test 2 - Dodawanie urządzenia: Failed')
        return

################Test Kontrola Xopero Storage####################
def xoperoStorage():
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(text(),'Magazyny')]").click() #wybór magazynu
    time.sleep(1)
    print('Test Kontrola Xopero Storage: ', driver.find_element_by_xpath("//*[contains(text(),'Xopero Storage #1')]").is_displayed())
    return

#############Test 3 - Dodawanie magazynu lokalnego##########
def dodajLokalny():
    try:
        driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]').click()
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/ng-component/button/span[1]').click()
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field").click()
        elem = driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field/div/div[1]/div[2]/input")#
        ID = (elem.get_attribute("id")) 
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).clear()
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).send_keys("magazyn lokalny")
        matInput=int(ID[-2:])
        if matInput>=0:
            pass
        else:
            matInput=int(ID[-1:])
        matInput+=2
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("D:\storage testowy")
        driver.find_element_by_xpath("//*[contains(text(),'Zapisz')]").click()
        print ("Test 3 - Dodawanie magazynu lokalnego: Pass")
    except:
        print ("Test 3 - Dodawanie magazynu lokalnego: Failed")
        try:
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[1]/app-close-aside-button/button').click()
            driver.find_element_by_xpath('//*[@id="mat-dialog-8"]/app-modal/div/div[3]/button[2]').click()
        except:
            pass
    return

time.sleep(2)
##############Test 4 - Dodawanie magazynu SMB##########
def dodajSMB():
    try:
        driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]').click()
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/ng-component/button/span[1]').click()
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field").click()
        elem = driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field/div/div[1]/div[2]/input")#
        ID = (elem.get_attribute("id"))
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).clear()
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).send_keys("magazyn SMB")
        time.sleep(1)
        matInput=int(ID[-2:])
        if matInput>=0:
            pass
        else:
            matInput=int(ID[-1:])
        matInput+=4
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/ng-select/div').click()
        driver.find_element_by_xpath("//*[contains(text(),'Lokalizacja sieciowa')]").click()
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("admin")
        driver.find_element_by_xpath("//*[contains(text(),'Wybierz lub dodaj')]").click()
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-list-container/app-passwords-list/div/div[3]/button").click()
        matInput+=1
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("admin")
        matInput+=1
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("Admin_123")
        matInput+=1
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("Admin_123")
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-form-container/app-passwords-form/form/div[3]/app-save-button/button/span[1]").click()
        matInput-=4
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("\\\\192.168.0.198\Public\MStasiak") 
        driver.find_element_by_xpath("//*[contains(text(),'Zapisz')]").click()
        print ("Test 3 - Dodawanie magazynu SMB: Pass")
    except:
        print ("Test 3 - Dodawanie magazynu SMB: Failed")
        try:
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[1]/app-close-aside-button/button').click()
            driver.find_element_by_xpath('//*[@id="mat-dialog-8"]/app-modal/div/div[3]/button[2]').click()
        except:
            pass
    time.sleep(2)
    return

#############Test 4 - Dodawanie magazynu NFS#########
def dodajNFS():
    try:
        driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]').click()
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/ng-component/button/span[1]').click()
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field").click()
        elem = driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field/div/div[1]/div[2]/input")#
        ID = (elem.get_attribute("id")) 
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).clear()
        driver.find_element_by_xpath('//*[@id="%s"]' %(ID)).send_keys("magazyn NFS")
        matInput=int(ID[-2:])
        if matInput>=0:
            pass
        else:
            matInput=int(ID[-1:])
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/ng-select/div').click()
        driver.find_element_by_xpath("//*[contains(text(),'Network File Storage')]").click()
        matInput+=3
        driver.find_element_by_xpath('//*[@id="mat-input-%d"]' %(matInput)).send_keys("192.168.0.198:/StorageNFS")
        driver.find_element_by_xpath("//*[contains(text(),'Zapisz')]").click()
        print ("Test 4 - Dodawanie magazynu NFS: Pass")
    except:
        print ("Test 4 - Dodawanie magazynu NFS: Failed")
        try:
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[1]/app-close-aside-button/button').click()
            driver.find_element_by_xpath('//*[@id="mat-dialog-8"]/app-modal/div/div[3]/button[2]').click()
        except:
            pass
    time.sleep(1)
    return

def kontrolaZadania():
    time.sleep(2)
    x = True
    while x:
        if driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[7]/span[1]/app-icon/span').is_displayed():
            time.sleep(5)
        else:
            x = False
    driver.fin('/html/body/app-root/app-main/div/app-content/div[2]/aside/app-aside/ng-component/app-dashboard-plan/div/div[1]/app-close-aside-button/button').click()
    print("Zakończono zadanie")
    return

#############Test 5 -  Logowanie organizacji GitHub#######
def zalogujGH():
    try:
        driver.get("https://github.com/")
        time.sleep(2)
        driver.find_element_by_xpath("//*[contains(text(),'Sign in')]").click()
        time.sleep(2)
        GH = driver.find_element_by_name("login")
        GH.send_keys("stasiak.marek93@gmail.com")
        PASY = driver.find_element_by_name("password")
        PASY.send_keys("Plokijuh1.")
        driver.find_element_by_name("commit").click()
        print ("Test 5 - Logowanie organizacji GitHub: Pass")
    except:
        print ("Test 5 - Logowanie organizacji GitHub: Failed")
    time.sleep(1)
    driver.get("http://localhost:28555/git")
    return

#############Test 6 - Dodawanie organizacji GitHub#######
def dodajGH():
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/ng-containter/app-git-no-organizations/div/button[2]').click() #wybór git do utworzenia
        driver.find_element_by_xpath("//*[contains(text(),'Kontynuuj')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[5]/app-save-button/button").click() #zatwierdzenie tworzenia git
        print("Test 6 - Dodawanie organizacji GitHub: Pass")
    except:
        print('Test 6 - Dodawanie organizacji GitHub: Failed')
    time.sleep(1)    
    return
#############Test 7 -  Dodawanie i uruchomienie planu predefiniowanego do organizacji GitHub#######
def predefiniowany():
    try:   
        driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-modal/div/div[3]/button[2]/span[1]').click()
        print ("Test 7 - Dodawanie i uruchomienie planu predefiniowanego do organizacji GitHub: Pass")
    except:
        try:
            driver.get("http://localhost:28555/git")
            driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/ng-containter/app-organization-container/app-organization/section/article/app-simplified-backup-plans/div/div/div/button/span[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath("//*[contains(text(),'Git Protection')]").click()
            print("Test 7 -  Dodawanie planu predefiniowanego do organizacji GitHub: Pass")
        except:
            print("Test 7 -  Dodawanie planu predefiniowanego do organizacji GitHub: Failed")
        time.sleep(1)  
        #############Test 8 -  Uruchamianie planu predefiniowanego do organizacji GitHub#######
        try:
            time.sleep(1)
            driver.find_element_by_xpath("//*[contains(text(),'Wykonaj teraz')]").click()
            print("Test 8 -  Uruchamianie planu predefiniowanego do organizacji GitHub: Pass")
        except:
            print ("Test 8 -  Uruchamianie planu predefiniowanego do organizacji GitHub: Failed")
            time.sleep(2)
    kontrolaZadania()


##################Test 10 - Podsumowanie backupu GIT (test 8)#################
def podsumowanie():
    driver.find_element_by_xpath("//*[contains(text(),'Zadania')]").click() #wybór zadań
    driver.find_element_by_xpath("//*[contains(text(),'Ostatnie 24 godziny')]").click() #wybór wykonanych zadań
    okelem = driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[1]/div/span[1]')
    OK = (okelem.get_attribute("innerHTML"))
    time.sleep(1)
    warelem = driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[2]/div/span[1]')
    Warnings = (warelem.get_attribute("innerHTML"))
    time.sleep(1)
    nokelem = driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[3]/div/span')
    NOK = (nokelem.get_attribute("innerHTML"))
    time.sleep(1)
    print("Pomyślnie zakończono %s repozytoriów" %(OK))
    print("Ostrzeżeniami zakończono %s repozytoriów " %(warelem))
    print("Błędami zakończono %s repozytoriów" %(NOK))
    return

#################Test 11 - Kontrola przywróconych backupów (test8)########################
def kontrolaBackupu():
    driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[4]').click()
    #time.sleep(30)
    plany = 0
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/ng-containter/app-organization-container/app-organization/section/footer/button[2]").click()
    time.sleep(2)
    for i in range(1,11):
        driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-repositories/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[%d]/td[7]/button[2]/span[1]" %(i)).click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath("//*[contains(text(),'Wyświetl dostępne plany, a następnie wybierz backup do przywrócenia')]").is_displayed()
            print("Brak planu backup")
        except:
            print("Plan backup dostępny")
            plany+=1
    print("Utworzono ", plany, "na 10 planów")
    return

#################Test 12 - przywracanie backupu (test8)#################
def przywracanieGH():
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button').click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(),'Restore all')]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(),'Start now')]").click()
    driver.find_element_by_xpath("//*[contains(text(),'Zadania')]").click() #wybór zadań
    time.sleep(2)
    kontrolaZadania()
    driver.find_element_by_xpath("//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
    print("Wykonano przywracanie repozytorium GH")
    return

for i in range(1,100):
    if i==1:
        logowanie()
    elif i==2:
        dodanieUrzadzenia()
    elif i==3:
        xoperoStorage()
    elif i==4:
        dodajLokalny()
    elif i==5:
        dodajSMB()
    elif i==6:
        dodajNFS()
    elif i==7:
        zalogujGH()
    elif i==8:
        dodajGH()
    elif i==9:
        predefiniowany()
    elif i==10:
        podsumowanie()
    elif i==11:
        kontrolaBackupu()
    elif i==12:
        przywracanieGH()
    else:
        exit()

#driver.close()