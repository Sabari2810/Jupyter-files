#!/usr/bin/env python
# coding: utf-8

# In[11]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass


# In[12]:


class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(2)
        self.driver.find_element_by_link_text("sabarii_v").click() # give your profile name here
        sleep(4)
        
    def _get_names(self,path):
        scroll_bar = self.driver.find_element_by_xpath(path)
        sleep(2)
        last_ht,ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,scroll_bar)
        
        links = scroll_bar.find_elements_by_tag_name("a")
        
        names = [link.text for link in links if link.text !='']
        return names

    def acc_following(self):
        self.driver.find_element_by_xpath("//a[text()=' following']").click()
        following = self._get_names("/html/body/div[4]/div/div/div[2]")
        return following
    def acc_followers(self):
        self.driver.find_element_by_xpath("//a[text()=' followers']").click()
        followers = self._get_names("/html/body/div[4]/div/div/div[2]")
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return followers
    def bad_eggs(self):
        bad_eggs_list = []
        followers = s.acc_followers()
        following = s.acc_following()
        for name in following:
            if name not in followers:
                bad_eggs_list.append(name)
        return bad_eggs_list


# In[10]:


email = getpass.getpass("Enter your Email")
password = getpass.getpass("Enter your password")
s = InstaBot(email,password)
bad_eggs = s.bad_eggs()


# In[ ]:





# In[6]:





# In[ ]:




