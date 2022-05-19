#region Imports
import sideTasks
import fileBackupPath
import fileRestore
import pathBackup
import systemVariable
import xoperoVariable
import time
from selenium import webdriver
#endregion

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)

sideTasks.logowanie(driver)

fileBackupPath.fileBackupCLD(driver,"fileBackup")
pathBackup.pathBackup(driver,"By Path","E:\\abecadlo")

xoperoVariables = ["HOMES","USERS_DOCUMENTS","USERS_DESKTOP","USERS_DOWNLOADS"]
for variable in xoperoVariables:
    planName = 'Zmienna %s' %(variable)
    xoperoVariable.xoperoVar(driver,planName,variable)
    time.sleep(1)

systemVariable.systemVar(driver,"System Var","smieci")

fileRestore.FileRestore_Cloud(driver,"Xopero Storage #1 (XoperoOneEmea)","fileBackup")
