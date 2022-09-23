from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)

############logowanie GIT
ran = random.randint(1,7)

driver.implicitly_wait(10)
driver.get("https://github.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,("//*[contains(text(),'Sign in')]")).click()
time.sleep(2)
GH = driver.find_element(By.NAME,'login')
GH.send_keys("stasiak.marek93@gmail.com")
PASY = driver.find_element(By.NAME,"password")
PASY.send_keys("1Q2w3e4raz.")
driver.find_element(By.NAME,"commit").click()
time.sleep(1)


driver.get("https://gitprotect.io/sign-up.html")



TimeVar = str((time.time()))
MailVar = TimeVar.replace(".","")
PartEmail = ("m.stasiak+","@xopero.com")
Email = MailVar.join(PartEmail)

start = time.time()

##############Tworzenie konta gitprotect
firstEmail = driver.find_element(By.ID,"email_first")
firstEmail.send_keys(Email)
time.sleep(5)
driver.find_element(By.TAG_NAME,'button').click()

time.sleep(ran)
fullName = driver.find_element(By.ID,"full_name")
fullName.send_keys('Marek')
time.sleep(ran)
org = driver.find_element(By.ID,"organization")
org.send_keys("Xopero Test")
time.sleep(ran)
# phone = driver.find_element(By.ID,'intlTelInput')
# phone.send_keys('201-555-0123')
select = Select(driver.find_element(By.ID,'region'))
select.select_by_value('EMEA')
password = driver.find_element(By.ID,'password')
password.send_keys('1Q2w3e4r.')




driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/form/button").click()
time.sleep(2)


tworzenieKonta = 0
while driver.current_url == "https://gitprotect.io/sign-up.html":
    time.sleep(1)
    tworzenieKonta+=1
    if tworzenieKonta < 90:
        pass
    else:
        print ("Captcha :( lub nie wstają pody")
        driver.quit()
        exit()

print("Konto tworzy się ", tworzenieKonta," sekund")
title = driver.current_url


######Dodawanie organizacji GIT
#try:
driver.implicitly_wait(15)
driver.refresh()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click() #wybór git do utworzenia
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/app-git-no-organizations/div/button[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[5]/app-save-button/button").click() #zatwierdzenie tworzenia git
#try:
print("Dodano organizację GitHub")
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-modal/div/div[3]/button[2]').click()
time.sleep(10)
#driver.find_element(By.XPATH,"//*[contains(text(),'Git Protection')]").click()
# time.sleep(2)
print("Dodano plan do organizacji GIT")
    # try:
    #     time.sleep(1)
    #     driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click()
    #     print("Uruchomiono plan backapu GIT")
    # except:
    #     print ("Błąd uruchamiania planu GIT")
    #     time.sleep(2)
    # #except:
    #     print("Nie Udało się dodać planu do organizacji GIT")
# except:
#     print("Nie udało się dodać organizacji GIT")
time.sleep(3)
try:
    driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[2]/aside/app-aside/ng-component/app-dashboard-plan/div/div[1]/app-close-aside-button/button/span[1]').click()
except:
    pass
time.sleep(1)

####################Kontrola Licencji
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[contains(text(),'Settings')]").click() #wybór ustawień
driver.find_element(By.XPATH,"//p[contains(.,'Manage your licenses')]").click() #wybór licencji
driver.find_element(By.XPATH,"//*[contains(text(),'See details')]").click() #wybór detali licencji
licencje = ['Microsoft 365','GitProtect','Feature worker','Server Agent','Endpoint Agent','Cloud Worker','Virtual Agent per Host','Virtual Agent per Socket']
for lic in licencje:
    try:
        istrue = driver.find_element(By.XPATH,"//*[contains(text(),'%s')]" %(lic)).is_displayed()
        print("Dostępność licencji %s = %s" % (lic,istrue))
        
    except:
        pass

#########Kontrola workera i magazynu
driver.find_element(By.XPATH,"//*[contains(text(),'Storages')]").click() #wybór magazynu
time.sleep(1)
print('Dostępność magazynu xopero: ', driver.find_element(By.XPATH,"//*[contains(text(),'Xopero Storage #1')]").is_displayed())

driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-storages-page/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr/td[5]/button').click()
print('Dostępność cloud workera: ', driver.find_element(By.XPATH,"//*[contains(text(),'Cloud Worker')]").is_displayed())
driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań

#kontrola zakończenia zadania backup
time.sleep(3)
x = True
print("Buckup w trakcie wykonywania")
try:
    while x:
        if driver.find_element(By.ID,'mat-badge-content-4').is_displayed():
            time.sleep(5)
        else:
            x = False
except:
    pass
try:
    #driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
    driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
    okelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[1]/div/span')
    OK = (okelem.get_attribute("innerHTML"))
    time.sleep(3)
    warelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[2]/div/span')
    Warnings = (warelem.get_attribute("innerHTML"))
    time.sleep(1)
    nokelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[3]/div/span')
    NOK = (nokelem.get_attribute("innerHTML"))
    time.sleep(1)
    print("Podsumowanie backupu GitHub")
    print("Pomyślnie zakończono %s repozytoriów" %(OK))
    print("Ostrzeżeniami zakończono %s repozytoriów " %(Warnings))
    print("Błędami zakończono %s repozytoriów" %(NOK))
except:
    print("Błąd wyświetlania podsumowania")
#Kontrola przywróconych backupów
driver.find_element(By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[1]').click()
#time.sleep(30)
plany = 0
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/app-organization-container[1]/app-organization/section/footer/button[2]/span[1]").click()
time.sleep(2)
for i in range(1,11):
    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-repositories/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[%d]/td[8]/button[2]/span[1]" %(i)).click()
    time.sleep(4)
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'View available plans, then select the backup copy to restore')]").is_displayed()
    except:
        plany+=1
x= ("Utworzono ", plany, "na 10 planów")
print(str(x))

#####uruchomienie backupu
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button').click()
time.sleep(6)
driver.find_element(By.XPATH,"//*[contains(text(),'Restore all')]").click()
time.sleep(6)
driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click()

driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
time.sleep(2)
x = True
print("Przywracanie w trakcie wykonywania")
while x:
    if driver.find_element(By.ID,'mat-badge-content-4').is_displayed():
        time.sleep(5)
    else:
        x = False
driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
print("Wykonano przywracanie repozytorium")

try:
    okelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[1]/div/span')
    OK = (okelem.get_attribute("innerHTML"))
    time.sleep(3)
    warelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[2]/div/span')
    Warnings = (warelem.get_attribute("innerHTML"))
    time.sleep(2)
    nokelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[3]/div/span')
    NOK = (nokelem.get_attribute("innerHTML"))
    time.sleep(2)
    print("Podsumowanie przywracania GitHub")
    print("Pomyślnie zakończono %s repozytoriów" %(OK))
    print("Ostrzeżeniami zakończono %s repozytoriów " %(Warnings))
    print("Błędami zakończono %s repozytoriów" %(NOK))
except:
    print("Błąd wyświetlania podsumowania")

###########BIT BUCKET
driver.find_element(By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[1]').click()
time.sleep(3)
##################################
driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/app-toolbar/button/span[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[3]/app-add/section/ng-select/div").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[3]/app-add/section/ng-select/ng-dropdown-panel/div[2]/div[2]/div[1]/div").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'Proceed')]").click()

time.sleep(5)
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)

x = driver.find_element(By.NAME,'username')
x.send_keys("stasiak.marek93@gmail.com")
driver.find_element(By.XPATH,"//*[contains(text(),'Kontynuuj')]").click()
time.sleep(1)
y = driver.find_element(By.NAME,'password')
y.send_keys("Plokijuh1.")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login-submit"]/span/span').click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(text(),'Grant access')]").click()
time.sleep(15)
driver.switch_to.window(main_window_handle)
time.sleep(5)
driver.find_element(By.XPATH,"//*[contains(text(),'Assign plan')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(text(),'Git Protection')]").click()
time.sleep(2)
driver.refresh()
time.sleep(5)
print("Dodano plan do organizacji GIT")
##############################################
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/app-organization-container[2]/app-organization/section/article/app-simplified-backup-plans/div/div/div/div[2]/button/span[1]").click()
driver.find_element(By.XPATH,"//div[@class='cdk-overlay-pane']/div/div/button[3]").click()
print("Uruchomiono plan backapu GIT")

time.sleep(3)
x = True
print("Buckup w trakcie wykonywania")
while x:
    if driver.find_element(By.ID,'mat-badge-content-4').is_displayed():
        time.sleep(5)
    else:
        x = False
try:
    #driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[2]/aside/app-aside/ng-component/app-dashboard-plan/div/div[1]/app-close-aside-button/button").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
    driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
    okelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[1]/div/span')
    OK = (okelem.get_attribute("innerHTML"))
    time.sleep(3)
    warelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[2]/div/span')
    Warnings = (warelem.get_attribute("innerHTML"))
    time.sleep(1)
    nokelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[3]/div/span')
    NOK = (nokelem.get_attribute("innerHTML"))
    time.sleep(1)
    print("Podsumowanie backupu BitBucket")
    print("Pomyślnie zakończono %s repozytoriów" %(OK))
    print("Ostrzeżeniami zakończono %s repozytoriów " %(Warnings))
    print("Błędami zakończono %s repozytoriów" %(NOK))
except:
    print("Błąd wyświetlania podsumowania")
#Kontrola przywróconych backupów
driver.find_element(By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[1]').click()
#time.sleep(30)
plany = 0
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/app-organization-container[2]/app-organization/section/footer/button[2]/span[1]").click()
time.sleep(2)
for i in range(1,11):
    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-repositories/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[%d]/td[8]/button[2]/span[1]" %(i)).click()
    time.sleep(5)
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'View available plans, then select the backup copy to restore')]").is_displayed()
    except:
        plany+=1

print("Utworzono ", plany, "na 10 planów")

#####uruchomienie backupu
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[contains(text(),'Restore all')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click()

driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
time.sleep(2)
x = True
print("Buckup w trakcie wykonywania")
while x:
    if driver.find_element(By.ID,'mat-badge-content-4').is_displayed():
        time.sleep(5)
    else:
        x = False
driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
print("Wykonano przywracanie repozytorium")

try:
    okelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[1]/div/span')
    OK = (okelem.get_attribute("innerHTML"))
    time.sleep(3)
    warelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[2]/div/span')
    Warnings = (warelem.get_attribute("innerHTML"))
    time.sleep(1)
    nokelem = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/main/div/ng-component/article/mat-tab-group/div/mat-tab-body[2]/div/app-packages/mat-accordion/app-package[1]/mat-expansion-panel/mat-expansion-panel-header/span/div[2]/app-package-tasks-statuses/div[3]/div/span')
    NOK = (nokelem.get_attribute("innerHTML"))
    time.sleep(1)
    print("Podsumowanie przywracania BitBucket")
    print("Pomyślnie zakończono %s repozytoriów" %(OK))
    print("Ostrzeżeniami zakończono %s repozytoriów " %(Warnings))
    print("Błędami zakończono %s repozytoriów" %(NOK))
except:
    print("Błąd wyświetlania podsumowania")


##############GIT LAB#########################################
# driver.find_element(By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[1]').click()
# time.sleep(1)
# ##################################
# driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/app-toolbar/button/span[1]').click()
# time.sleep(1)
# driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[3]/app-add/section/ng-select/div").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"//*[contains(text(),'GitLab')]").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"//*[contains(text(),'Proceed')]").click()
# time.sleep(10)
# driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[3]/app-git-select-bb-project/div/section/ul/li[1]/mat-checkbox/label/span[1]")
# time.sleep(1)
# driver.find_element(By.XPATH,"//*[contains(text(),'Proceed')]").click()
# # stop = time.time()
# Worktime = stop-start
# print(Worktime)

driver.quit()
exit()