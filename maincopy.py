import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

def check():
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    url = "https://www.nasdaqomxnordic.com/shares"
    driver.get(url)
    driver.delete_all_cookies()
    driver.maximize_window()
    time.sleep(2)

    find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden showOnNordicShares']//ul[@class='floatLeft overflowHidden checkboxSet']//label[@title='Companies with a market value between 150 million and 1 billion euro.']")
    find.click()

    find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden showOnNordicShares']//ul[@class='floatLeft overflowHidden checkboxSet']//label[@title='Companies with a market value below 150 million euro.']")
    find.click()

    find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden showOnNordicShares']//ul[@class='floatLeft overflowHidden checkboxSet']//label[@title='SPAC traded on Nasdaq OMX Nordic.']")
    find.click()

    time.sleep(4)

    with open("general.txt", "w") as general:
        general.write("\n")
        general.write("\n")

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//tr")
        with open("resultats_next_day.txt", "w") as file:
            for item in find_lines:
                title = item.get_attribute("title")
                file.write(title + "\n")

        previous = []
        nextd = []

        with open("resultats_previous_day.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                previous.append(first[0])

        with open("resultats_next_day.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                nextd.append(first1[0])


        # if previous == nextd:
        #     print ("good")
        # else:
        #     print ("")
        #     result = list(set(nextd)^set(previous))
        #     print ("set: ", result)
        #     print ("")


        new_shares = []
        for template in nextd:
            if template not in previous:
                new_shares.append(template)
        print("New Shares in Main Market: ", new_shares)
        general.write(f"New Shares in Main Market: {new_shares}\n")

        removed_shares = []
        for template in previous:
            if template not in nextd:
                removed_shares.append(template)
        print("Removed Shares in Main Market: ", removed_shares)
        general.write(f"Removed Shares: in Main Market: {removed_shares}\n")
        general.write("\n")
        print ()

        ############################################################

        find = driver.find_element(By.XPATH, "//label[@class='ui-button ui-widget ui-state-default ui-button-text-only']")
        find.click()
        time.sleep(2)

        find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden hide showOnFNShares']//label[@title='First North GM']")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//tr")
        with open("First_North_GM1.txt", "w") as file:
            for item in find_lines:
                title = item.get_attribute("title")
                file.write(title + "\n")

        firstnorth1 = []
        firstnorth2 = []

        with open("First_North_GM1.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                firstnorth1.append(first[0])

        with open("First_North_GM2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                firstnorth2.append(first1[0])

        new_shares1 = []
        for template in firstnorth1:
            if template not in firstnorth2:
                new_shares1.append(template)
        print("New Shares in First North GM: ", new_shares1)
        general.write(f"New Shares in First North GM:  {new_shares1}\n")

        removed_shares1 = []
        for template in firstnorth2:
            if template not in firstnorth1:
                removed_shares1.append(template)
        print("Removed Shares in First North GM: ", removed_shares1)
        print ()
        general.write(f"Removed Shares in First North GM:  {removed_shares1}\n")
        general.write("\n")

        #############################################################

        find1 = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden hide showOnFNShares']//label[@title='Norwegian shares traded on First North Trading List']")
        find1.click()
        time.sleep(3)
        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//tr")
        with open("Taiding_List_Norway1.txt", "w") as file:
            for item in find_lines:
                title = item.get_attribute("title")
                file.write(title + "\n")

        norway1 = []
        norway2 = []

        with open("Taiding_List_Norway1.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                norway1.append(first[0])

        with open("Taiding_List_Norway2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                norway2.append(first1[0])

        new_shares11 = []
        for template in norway1:
            if template not in norway2:
                new_shares11.append(template)
        print("New Shares in Traiding List Norway: ", new_shares11)
        general.write(f"New Shares in Traiding List Norway: {new_shares11}\n")

        removed_shares12 = []
        for template in norway2:
            if template not in norway1:
                removed_shares12.append(template)
        print("Removed Shares in Traiding List Norway: ", removed_shares12)
        print ()
        general.write(f"Removed Shares in Traiding List Norway: {removed_shares12}\n")
        general.write("\n")      

        #############################################################

        find = driver.find_element(By.XPATH, "//label[@class='ui-button ui-widget ui-state-default ui-button-text-only ui-corner-right']")
        find.click()
        time.sleep(2)

        find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden hide showOnBalticShares']//label[@title='Secondary list.']")
        find.click()
        
        find = driver.find_element(By.XPATH, "//div[@class='filterAreaRow overflowHidden hide showOnBalticShares']//label[@title='First North GM']")
        find.click()
        time.sleep(2)
        
        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//tr")
        with open("Baltic_next_day.txt", "w") as file:
            for item in find_lines:
                title = item.get_attribute("title")
                file.write(title + "\n")

        baltic1 = []
        baltic2 = []

        with open("Baltic_next_day.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                baltic1.append(first[0])

        with open("Baltic_previous_day.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                baltic2.append(first1[0])

        new_shares111 = []
        for template in baltic1:
            if template not in baltic2:
                new_shares111.append(template)
        print("New Shares in Baltic: ", new_shares111)
        general.write(f"New Shares in Baltic: {new_shares111}\n")

        removed_shares111 = []
        for template in baltic2:
            if template not in baltic1:
                removed_shares111.append(template)
        print("Removed Shares Baltic: ", removed_shares111)
        print ()
        general.write(f"Removed Shares in Baltic: {removed_shares111}\n")
        general.write("\n")

        ############################################################

        find = driver.find_element(By.XPATH, "//nav[@class='floatLeft']//a[@title='Go to Bonds']")
        find.click()
        time.sleep(2)

        find = driver.find_element(By.XPATH, "//a[@title='Go to Denmark']//span[@class='ui-corner-all subMenuItemLinkText']")
        find.click()
        time.sleep(3)

        find = driver.find_element(By.XPATH, "//a[@id='cookieConsentOK']")
        find.click()
        time.sleep(3)

        find = driver.find_element(By.XPATH, "//label[@title='Corporate and other bonds']")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody//a")
        with open("bonds_denmark.txt", "w") as file:
            for item in find_lines:
                file.write(item.text + "\n")

        denmark1 = []
        denmark2 = []

        with open("bonds_denmark.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                denmark1.append(first)

        with open("bonds_denmark2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                denmark2.append(first1)

        new_bonds_denmark = []
        for template in denmark1:
            if template not in denmark2:
                new_bonds_denmark.append(template)
        print("New Bonds in Denmark: ", new_bonds_denmark)
        general.write(f"New Bonds in Denmark: {new_bonds_denmark}\n")

        removed_bonds_denmark = []
        for template in denmark2:
            if template not in denmark1:
                removed_bonds_denmark.append(template)
        print("Removed Bonds in Denmark: ", removed_bonds_denmark)
        print ()
        general.write(f"Removed Bonds in Denmark: {removed_bonds_denmark}\n")
        general.write("\n")    

        ################################################################

        find = driver.find_element(By.XPATH, "//a[@title='Go to Sweden']//span[@class='ui-corner-all subMenuItemLinkText']")
        find.click()
        time.sleep(2)
        
        find = driver.find_element(By.XPATH, "//select[@class='floatLeft marginRight20']")
        find.click()
        time.sleep(2)
        
        with open ("bonds_sweden.txt", "w") as kick:
            find = driver.find_elements(By.XPATH, "//select[@class='floatLeft marginRight20']//option")
            for each in find:
                each.click()
                time.sleep(3)
                find = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//a")
                for item in find:
                    kick.write(item.text + "\n")

        sweden1 = []
        sweden2 = []

        with open("bonds_sweden.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                sweden1.append(first)

        with open("bonds_sweden2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                sweden2.append(first1)

        new_list1 = []
        for each in sweden1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in sweden2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_sweden = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_sweden.append(template)
        print("New Bonds in Sweden: ", new_bonds_sweden)
        general.write(f"New Bonds in Sweden: {new_bonds_sweden}\n")

        removed_bonds_sweden = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_sweden.append(template)
        print("Removed Bonds in Sweden: ", removed_bonds_sweden)
        print ()
        general.write(f"Removed Bonds in Sweden: {removed_bonds_sweden}\n")
        general.write("\n") 

        ############################################################### 

        find = driver.find_element(By.XPATH, "//a[@title='Go to Iceland']//span")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//a")
        with open("bonds_iceland.txt", "w") as file:
            for item in find_lines:
                file.write(item.text + "\n")

        iceland1 = []
        iceland2 = []

        with open("bonds_iceland.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                iceland1.append(first)

        with open("bonds_iceland2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                iceland2.append(first1)

        new_list1 = []
        for each in iceland1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in iceland2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_iceland = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_iceland.append(template)
        print("New Bonds in Iceland: ", new_bonds_iceland)
        general.write(f"New Bonds in Iceland: {new_bonds_iceland}\n")

        removed_bonds_iceland = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_iceland.append(template)
        print("Removed Bonds in Iceland: ", removed_bonds_iceland)
        print()
        general.write(f"Removed Bonds in Iceland: {removed_bonds_iceland}\n")
        general.write("\n")

        #########################################################################

        find = driver.find_element(By.XPATH, "//a[@title='Go to Finland']//span")
        find.click()
        time.sleep(2)

        with open ("bonds_finland.txt", "w") as kick:
            find = driver.find_elements(By.XPATH, "//select[@id='bondsSearchFISelect']//option")
            for each in find:
                each.click()
                time.sleep(3)
                find = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//a")
                for item in find:
                    kick.write(item.text + "\n")

        finland1 = []
        finland2 = []

        with open("bonds_finland.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                finland1.append(first)

        with open("bonds_finland2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                finland2.append(first1)

        new_list1 = []
        for each in finland1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in finland2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_finland = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_finland.append(template)
        print("New Bonds in Finland: ", new_bonds_finland)
        general.write(f"New Bonds in Finland: {new_bonds_finland}\n")

        removed_bonds_finland = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_finland.append(template)
        print("Removed Bonds in Finland: ", removed_bonds_finland)
        general.write(f"Removed Bonds in Finland: {removed_bonds_finland}\n")
        general.write("\n")

        #######################################################################

        find = driver.find_element(By.XPATH, "//a[@title='Go to First North']//span")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//a")
        with open("bonds_first_north.txt", "w") as file:
            for item in find_lines:
                file.write(item.text + "\n")

        first_north1 = []
        first_north2 = []

        with open("bonds_first_north.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                first_north1.append(first)

        with open("bonds_first_north2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                first_north2.append(first1)

        new_list1 = []
        for each in first_north1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in first_north2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_first_north = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_first_north.append(template)
        print("New Bonds in First North: ", new_bonds_first_north)
        general.write(f"New Bonds in First North: {new_bonds_first_north}\n")

        removed_bonds_first_north = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_first_north.append(template)
        print("Removed Bonds in First North: ", removed_bonds_first_north)
        print()
        general.write(f"Removed Bonds in First North: {removed_bonds_first_north}\n")
        general.write("\n")

        ########################################################################

        find = driver.find_element(By.XPATH, "//a[@title='Go to Sustainable Debt']//span")
        find.click()
        time.sleep(2)

        find = driver.find_element(By.XPATH, "//label[@class='nordic-checkbox fn']")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//a")
        with open("bonds_Sustainable Debt.txt", "w") as file:
            for item in find_lines:
                file.write(item.text + "\n")

        sustainable_debt1 = []
        sustainable_debt2 = []

        with open("bonds_Sustainable Debt.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                if len(first) > 0:
                    first = " ".join(first)
                sustainable_debt1.append(first)

        with open("bonds_Sustainable Debt2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                if len(first1) > 0:
                    first1 = " ".join(first1)
                sustainable_debt2.append(first1)

        new_list1 = []
        for each in sustainable_debt1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in sustainable_debt2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_sustainable_debt = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_sustainable_debt.append(template)
        print("New Bonds in Sustainable Debt: ", new_bonds_sustainable_debt)
        general.write(f"New Bonds in Sustainable Debt: {new_bonds_sustainable_debt}\n")

        removed_bonds_sustainable_debt = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_sustainable_debt.append(template)
        print("Removed Bonds in Sustainable Debt: ", removed_bonds_sustainable_debt)
        print()
        general.write(f"Removed Bonds in Sustainable Debt: {removed_bonds_sustainable_debt}\n")
        general.write("\n")

        ############################################################################

        find = driver.find_element(By.XPATH, "//a[@title='Go to Baltic']//span")
        find.click()
        time.sleep(2)

        find_lines = driver.find_elements(By.XPATH, "//tbody[@aria-live='polite']//tr")
        with open("bonds_baltic.txt", "w") as file:
            for item in find_lines:
                title = item.get_attribute("title")
                file.write(title + "\n")

        baltic1 = []
        baltic2 = []

        with open("bonds_baltic.txt", "r") as f:
            read = f.readlines()
            for x in read:
                row = x.rstrip("\n")
                first = row.split() 
                # if len(first) > 0:
                #     first = " ".join(first)
                baltic1.append(first[0])

        with open("bonds_baltic2.txt", "r") as f1:
            read1 = f1.readlines()
            for y in read1:
                row1 = y.rstrip("\n")
                first1 = row1.split() 
                # if len(first1) > 0:
                #     first1 = " ".join(first1)
                baltic2.append(first1[0])

        new_list1 = []
        for each in baltic1: 
            if each in new_list1:
                continue
            else:
                new_list1.append(each)
        # print(len(new_list1))

        new_list2 = []
        for each in baltic2: 
            if each in new_list2:
                continue
            else:
                new_list2.append(each)
        # print(len(new_list2))

        new_bonds_baltic = []
        for template in new_list1:
            if template not in new_list2:
                new_bonds_baltic.append(template)
        print("New Bonds in Baltic: ", new_bonds_baltic)
        general.write(f"New Bonds in Baltic: {new_bonds_baltic}\n")

        removed_bonds_baltic = []
        for template in new_list2:
            if template not in new_list1:
                removed_bonds_baltic.append(template)
        print("Removed Bonds in Baltic: ", removed_bonds_baltic)
        print()
        general.write(f"Removed Bonds in Baltic: {removed_bonds_baltic}\n")
        general.write("\n")

    
def main():
    check()
    # schedule.every(1).minutes.do(check)
    # # schedule.every().day.at('11:23').do(check)

    # while True:
    #     schedule.run_pending()

if __name__ == '__main__':
    main()
