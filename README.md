💻 Mercado Livre Scraping - Laptop Market Research
This personal project simulates a business case where I’m scraping the Mercado Livre platform to better understand the laptop market in Brazil.

⚙️ Project Steps
✅ Step 1 - Create the Scrapy Project
Start your Scrapy project using the CLI command:

bash
Copy
Edit
scrapy startproject mercado_licre
Yep, I accidentally typed "licre" instead of "livre"... and rolled with it 😅

🕷️ Step 2 - Generate the Spider
Create your spider with the command:

bash
Copy
Edit
scrapy genspider notebook '<website link you want to scrape>'
A spider is the tool that actually scrapes the data from the website.

🧪 Step 3 - Test Access with Scrapy Shell
Run:

bash
Copy
Edit
scrapy shell
Then try fetching the HTML with:

python
Copy
Edit
fetch('<website link>')
⚠️ Problem: I got a 403 Forbidden error. The server blocked my access.

🛠️ Step 4 - Solving the 403 Error
Mercado Livre was blocking me because it didn’t detect a real browser. So I added my Chrome User-Agent to settings.py.

Got my Chrome user agent string.

Added it to settings.py:

python
Copy
Edit
USER_AGENT = 'my_user_agent_here'
Tried fetch() again — still didn’t work 🤕

Restarted the Scrapy shell and tried again — this time, it worked! 🎉

Created a .env file inside the spiders folder to store the USER_AGENT securely.

Example .env:

ini
Copy
Edit
USER_AGENT=my_user_agent_here
🔍 Step 5 - Exploring the HTML Structure
I inspected the website's HTML to locate the data I wanted.

First field I targeted: Brand

Used this command inside the Scrapy shell:

python
Copy
Edit
response.css('span.poly-component__brand::text').get()
::text extracts only the text

.get() grabs the first match

Testing in the shell helps avoid rerunning the full spider every time.

🧩 Step 6 - Writing the parse Function
I began implementing the spider logic in the parse method:

Selected elements using .css()

Used yield in a loop to collect each result

Saved everything to a JSON file with:

bash
Copy
Edit
scrapy crawl notebook -o data.json
📌 Final Notes
The project is still a work in progress.

I plan to expand the data extraction to more fields beyond just brand.

Future improvements may include pagination, category filtering, and more robust error handling.
