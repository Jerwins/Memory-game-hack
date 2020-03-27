from selenium import webdriver
path_geckodriver = r"path_of_geckodriver_folder" # download if you haven't


driver = webdriver.Firefox(
    executable_path=r"path_of_geckodriver_executable")
driver.get("http://zzzscore.com/1to50/en/?ts=1585227914297#") #sample

grid = driver.find_element_by_id('grid')
for number in range(1, 51): 
    grid.find_element_by_xpath('//div[text()={}]'.format(number)).click()
