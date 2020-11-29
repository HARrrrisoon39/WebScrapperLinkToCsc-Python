from selenium import webdriver
import time
import xlsxwriter
import requests
import csv

users = ['cbdistillery_','joyorganics']
    #, 'charlotteswebcbd' ,'ashley_greenroads','thelordjones','nuleafnaturals','lazarusnaturalscbd','cbdfx_','bluebirdbotanicals','sagelynaturals']

browser = webdriver.Chrome(
    executable_path='C:/Users/Buddha/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
f = csv.writer(open('insta_profile_details.csv', 'w',encoding="utf-8"))
f.writerow(['User_Name', 'Number_of_Posts','Profile_URL','N_Followers','N_Following','Bio'])
for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    pro_url="https://www.instagram.com/"+user

    time.sleep(2)

    number_of_posts, followers, following = browser.find_elements_by_css_selector(
        '.g47SY')

    bio = browser.find_element_by_css_selector('.-vDIg')

    '''with open(f"{user}.txt", "w" ,encoding="utf-8") as file:
        file.write(
            f"User_Name: {user}\nNumber of Posts: {number_of_posts.text}\nProfile URL: {pro_url}\nFollowers: {followers.text}\nFollowing: {following.text}\n\nBio:\n{bio.text}")
'''

    User_Name=user
    Number_of_Posts=number_of_posts.text
    Profile_URL=pro_url
    N_Followers=followers.text
    N_Following=following.text
    Bio=bio.text
    f.writerow([User_Name, Number_of_Posts,Profile_URL,N_Followers,N_Following,Bio])

    time.sleep(4)
print("next")
browser.quit()
