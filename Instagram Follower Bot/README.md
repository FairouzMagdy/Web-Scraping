A bot that signs into your Instagram account and then goes into a page you choose to follow their followers.

What's used:

- Selenium Webdriver to help signing into Instagram and scraping data.

- Time Module to provide a delay between each step.

- OS Module to create environment variables.

- OOP Class InstaFollower which has 3 methods:

    - init method: to initialize the webdriver.
    
    - login method: to login into Instagram.
    
    - find_followers method: to go into the other instagram page and open the followers popup and then scrolls the bar.
    
    - follow method: to follow the page followers. This method has an exception if you tried to follow an acoount that you've
             already followed before, if this happens then the bot clicks the 'cancel' button and continues to follow other accounts.
    
- Last step is to create an object from this class and call the above methods in order.
