Simulating a business case that i will do a scrapping on mercado livre platform for understand the market of laptops

Step 1: create the scrapy project using the cli command scrapy startproject mercado_licre

Step 2: create a spider: scrapy spidergen notebook '<website link that i want to scrapy>'
    *a spider is the tool that will scrapy the website

Step 3: do a command scrapy shell and then do a fetch to bring the website html to my local env.

but... when i run, i receive a 403 error: forbidden access

Step 4: solving the step 3. I get My User Agent in Chrome: I want to say for mercado livre server that i'm not a hacker (or am i?)
    - on setting.py i put the user agent (do this too). So, mercado livre will understand that i am accessing using the chrome
    - i run the fetch again and didnt work. So i exit the terminal and did the scrapy shell again, run the fetch and it worked.