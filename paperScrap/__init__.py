from PaperScrap import PaperScrap

PaperScrap_instance = PaperScrap()
website = "http://jacm.acm.org/search-acm.cfm"
keywords ='Cyber+Physical+System'
cookie = '_ga=GA1.2.2019075266.1456282750; CFID=388281440; CFTOKEN=76463149; AK=expires%3D1464511197%7Eaccess%3D%2F10%2E1145%2F1800000%2F1795205%2F%2A%7Emd5%3D98a51807ad987f2da8f614d763882718; _gat=1'
PaperScrap_instance.getPaper(website=website,
                             keywords='Cyber+Physical+Systems',
                             cookie=cookie
                             )