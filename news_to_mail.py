from selenium import webdriver
# Using Chrome to access web
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver",chrome_options = chrome_options)
driver.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
headlines = []

for i in range(1,30):
    link = '//*[@id="yDmH0d"]/c-wiz/div/c-wiz/div/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/div[1]/div/h3/a/span'
    head = driver.find_element_by_xpath(link)
    k = head.text
    headlines.append(k)

# =============================================================================
# Save into pdf
# =============================================================================

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
 
canvas = canvas.Canvas("C:\\Users\\visha\\Desktop\\news.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 10)
k = 750
for i in headlines:
    canvas.drawString(30,k,i)
    k = k-20
canvas.save()

# =============================================================================
# Using mail client to send mails.
# =============================================================================
test = input('Enter YES to send a pdf of news to you mail address and NO to quit: ')
YES = 'YES'
if test == YES:
    b = input('Enter email address to send to: ')
    import smtplib 
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders 
       
    fromaddr = "Your email ID "
    toaddr = str(b)
       
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = "news_today"
      
    # string to store the body of the mail 
    body = "news_today_body"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = "news.pdf"
    attachment = open("C:\\Users\\visha\\Desktop\\news.pdf", "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, "password") 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit()
