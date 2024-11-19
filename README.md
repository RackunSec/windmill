# Windmill
## Windmill Cookie Reviewer
I created this script to output session cookie information that is report friendly.
## Install
You don't need to install the tool but you may need some dependencies. Use the following commands to get Windmill up and running:
```bash
sudo apt install python3-venv ## or something similar
git clone https://github.com/RackunSec/windmill.git
cd windmill
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
## Usage
To use Windmill, use the following steps:
 1. Open Burp Browser (Chrome) and navigate to your target web application
 2. Log into the web application
 3. Use developer tools to veiw cookies - Application tab->Cookies on left side bar->choose the domain
 4. Copy all the text shown into a file
 5. Run Windmill

```bash
python3 windmill.py -f (COOKIE FILE PATH) -d (TARGET DOMAIN TO REVIEW COOKIES)
``` 
The output should be printable for your penetration test report. DO NOT forget to demonstrate risk of cookie issues. Pentests =/= Vuln Scans!
