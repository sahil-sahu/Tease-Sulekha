import scrapy
import random
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
dict = {
    'ROBOTSTXT_OBEY': False,
    'DOWNLOAD_DELAY': 5,
    'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    'dont_filter': True,
    'ROTATING_PROXY_LIST': [
            '118.175.93.148:36744',
            '160.19.113.10:8080',
            '186.125.59.8:46316',
            '1.179.144.41:8080',
            '159.89.29.28:3128',
            '82.165.105.48:80',
            '180.211.183.138:8080',
            '175.106.10.164:8089',
            '74.205.128.200:80',
            '165.227.237.96:80',
            '180.183.228.44:8080',
            '80.93.213.214:3137',
            '177.70.243.1:8080',
            '122.144.3.235:63123',
            '5.16.0.180:8080',
            '175.139.179.65:42580',
            '118.172.176.61:8080',
            '41.33.66.246:34560',
            '187.190.226.53:999',
            '51.159.24.172:3167',
            '94.232.11.178:46449',
            '36.95.24.49:8080',
            '95.154.104.147:44393',
            '157.230.40.79:8080',
            '190.6.141.30:999',
            '218.253.39.60:8382',
            '103.11.106.33:8181',
            '46.254.217.54:53281',
            '139.59.119.125:8080',
            '116.68.254.252:8089',
            '85.117.78.195:3128',
            '46.0.203.186:8080',
            '195.138.90.226:3128',
            '12.218.209.130:53281',
            '187.44.163.73:80',
            '188.166.127.242:8080',
            '195.170.38.230:8080',
            '58.152.94.117:8080',
            '117.204.255.243:8080',
            '122.144.5.229:3888',
            '43.229.254.162:3128',
            '193.193.240.34:45944',
            '174.71.185.194:48678',
            '190.121.131.10:8080',
            '177.125.169.6:55443',
            '167.71.212.154:80',
            '157.230.103.189:36407',
            '140.227.64.248:58888',
            '74.208.112.84:8080',
            '95.217.34.209:3128',
    ],
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
        'rotating_proxies.middlewares.BanDetectionMiddleware': 620, },

}
reviews = ['one of the best software company in Bhubaneswar Service quality is good. Recommended.',
           'Best website and android app development in bhubaneswar. Best support and service as per now. Great expertise. Recommend to all.',
           'Best website design company in bhubaneswar. Great team of professionals. On-time delivery and proper commitment make them the best in industry in my opinion.',
           'Great Service with fabulous team of experts. Thanks Contrivers.',
           'Highly professional web designer in our city, services are prompt and ensure regular back to support you to capture information in easy to access format. Thanks a lot, Contrivers and its awesome team.',
           'Great work done on my website like design,development, content, SEO as well as Mobile responsiveness. Now I am getting more response from the customers. I totally admire such kind of work. Honestly, Impressive job done by Contrivers. I wish them to keep up this great work and all the very best for their bright future. I would recommend them to anyone looking for the Best SEO Company in Bhubaneswar.',
           'I satisfy dealing with them and they can provide services in many areas',
           'One of the best company for digital marketing in India. Great service at reasonable prices.',
           'Good Service. Very helpful. Nice Work',
           'Contrivers is a good professional team. They have maintained their commitment. I am satisfied with the development of my project. And of course the next project will give to Contrivers. Anyone will be recommended for any type of software development.']

datas = [{'name': 'Amaresh Nanda', 'email': 'amareshnanda@ghmail.com', 'psswd': 'adnanZhserama'}, {'name': 'Apsar Alli  Khan', 'email': 'apsarallikhan@ghmail.com', 'psswd': 'nahkZZillaZraspa'}, {'name': 'Nihar Ranjan Nayak', 'email': 'niharranjannayak@ghmail.com', 'psswd': 'kayanZnajnarZrahin'}, {'name': 'Raj Narayan Pattanaik', 'email': 'rajnarayanpattanaik@ghmail.com', 'psswd': 'kianattapZnayaranZjar'}, {'name': 'Kishore Kumar Sahoo', 'email': 'kishorekumarsahoo@ghmail.com', 'psswd': 'oohasZramukZerohsik'}, {'name': 'Sashikanta Rath', 'email': 'sashikantarath@ghmail.com', 'psswd': 'htarZatnakihsas'}, {'name': 'Pradeep Kumar Patta', 'email': 'pradeepkumarpatta@ghmail.com', 'psswd': 'attapZramukZpeedarp'}, {'name': 'Jagamohan Pattnaik', 'email': 'jagamohanpattnaik@ghmail.com', 'psswd': 'kianttapZnahomagaj'}, {'name': 'Babula Patra', 'email': 'babulapatra@ghmail.com', 'psswd': 'artapZalubab'}, {'name': 'Niranjan Mohapatra', 'email': 'niranjanmohapatra@ghmail.com', 'psswd': 'artapahomZnajnarin'}, {'name': 'Priya Ranjan Samantara', 'email': 'priyaranjansamantara@ghmail.com', 'psswd': 'aratnamasZnajnarZayirp'}, {'name': 'Gopinath Mohanty', 'email': 'gopinathmohanty@ghmail.com', 'psswd': 'ytnahomZhtanipog'}, {'name': 'S.A.Qureshi', 'email': 's.a.qureshi@ghmail.com', 'psswd': 'ihseruq.a.s'}, {'name': 'Srinibas Dalai', 'email': 'srinibasdalai@ghmail.com', 'psswd': 'ialadZsabinirs'}, {'name': 'Sujit Kumar Das', 'email': 'sujitkumardas@ghmail.com', 'psswd': 'sadZramukZtijus'}, {'name': 'Ajaya Kumar Mohapatra', 'email': 'ajayakumarmohapatra@ghmail.com', 'psswd': 'artapahomZramukZayaja'}, {'name': 'Bishnu Charan Sethi', 'email': 'bishnucharansethi@ghmail.com', 'psswd': 'ihtesZnarahcZunhsib'}, {'name': 'Prakash Kumar Nanda', 'email': 'prakashkumarnanda@ghmail.com', 'psswd': 'adnanZramukZhsakarp'}, {'name': 'Trilochana Mohapatra', 'email': 'trilochanamohapatra@ghmail.com', 'psswd': 'artapahomZanahcolirt'}, {'name': 'Chittaranjan Baliarsingh', 'email': 'chittaranjanbaliarsingh@ghmail.com', 'psswd': 'hgnisrailabZnajnarattihc'}, {'name': 'Akshya Kumar Routray', 'email': 'akshyakumarroutray@ghmail.com', 'psswd': 'yartuorZramukZayhska'}, {'name': 'Sakti Prasad Dash', 'email': 'saktiprasaddash@ghmail.com', 'psswd': 'hsadZdasarpZitkas'}, {'name': 'Sujit Jena', 'email': 'sujitjena@ghmail.com', 'psswd': 'anejZtijus'}, {'name': 'Susanta Kumar Patra', 'email': 'susantakumarpatra@ghmail.com', 'psswd': 'artapZramukZatnasus'}, {'name': 'Rabindra Kumar Behera', 'email': 'rabindrakumarbehera@ghmail.com', 'psswd': 'arehebZramukZardnibar'}, {'name': 'Mala Sethi', 'email': 'malasethi@ghmail.com', 'psswd': 'ihtesZalam'}, {'name': 'Pratap Chandra Sahani', 'email': 'pratapchandrasahani@ghmail.com', 'psswd': 'inahasZardnahcZpatarp'}, {'name': 'Jnanaranjan Samal', 'email': 'jnanaranjansamal@ghmail.com', 'psswd': 'lamasZnajnarananj'}, {'name': 'Sudhansu Sekhar Sahoo', 'email': 'sudhansusekharsahoo@ghmail.com', 'psswd': 'oohasZrahkesZusnahdus'}, {'name': 'Nakul Charan Biswal', 'email': 'nakulcharanbiswal@ghmail.com', 'psswd': 'lawsibZnarahcZlukan'}, {'name': 'Sarbeswar Mohapatra', 'email': 'sarbeswarmohapatra@ghmail.com', 'psswd': 'artapahomZrawsebras'}, {'name': 'Kishor Chandra Padhan', 'email': 'kishorchandrapadhan@ghmail.com',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'psswd': 'nahdapZardnahcZrohsik'}, {'name': 'Ranjeet Bhardwaj', 'email': 'ranjeetbhardwaj@ghmail.com', 'psswd': 'jawdrahbZteejnar'}, {'name': 'Ajit Kumar Barik', 'email': 'ajitkumarbarik@ghmail.com', 'psswd': 'kirabZramukZtija'}, {'name': 'Hemant Kumar Rout', 'email': 'hemantkumarrout@ghmail.com', 'psswd': 'tuorZramukZtnameh'}, {'name': 'Arun Kumar Dash', 'email': 'arunkumardash@ghmail.com', 'psswd': 'hsadZramukZnura'}, {'name': 'Hemanta Swain', 'email': 'hemantaswain@ghmail.com', 'psswd': 'niawsZatnameh'}, {'name': 'Jagabandhu Patra', 'email': 'jagabandhupatra@ghmail.com', 'psswd': 'artapZuhdnabagaj'}, {'name': 'Pradipta Kumar Behera', 'email': 'pradiptakumarbehera@ghmail.com', 'psswd': 'arehebZramukZatpidarp'}, {'name': 'Tanmay Kumar Jena', 'email': 'tanmaykumarjena@ghmail.com', 'psswd': 'anejZramukZyamnat'}, {'name': 'Atul Agarwal', 'email': 'atulagarwal@ghmail.com', 'psswd': 'lawragaZluta'}, {'name': 'Prasana Kumar Rath', 'email': 'prasanakumarrath@ghmail.com', 'psswd': 'htarZramukZanasarp'}, {'name': 'Kulamani Parida', 'email': 'kulamaniparida@ghmail.com', 'psswd': 'adirapZinamaluk'}, {'name': 'Santosh Kumar Tripathy', 'email': 'santoshkumartripathy@ghmail.com', 'psswd': 'yhtapirtZramukZhsotnas'}, {'name': 'Rashmit Kumar Harichandan', 'email': 'rashmitkumarharichandan@ghmail.com', 'psswd': 'nadnahcirahZramukZtimhsar'}, {'name': 'N.K. Khagesh Srichandan', 'email': 'n.k.khageshsrichandan@ghmail.com', 'psswd': 'nadnahcirsZhsegahkZ.k.n'}, {'name': 'Upendra Nath Chhatoi', 'email': 'upendranathchhatoi@ghmail.com', 'psswd': 'iotahhcZhtanZardnepu'}, {'name': 'Dillip Ranjan Patra', 'email': 'dillipranjanpatra@ghmail.com', 'psswd': 'artapZnajnarZpillid'}, {'name': 'Ranjan Mallick', 'email': 'ranjanmallick@ghmail.com', 'psswd': 'kcillamZnajnar'}, {'name': 'Tarini Prasad Mishra', 'email': 'tariniprasadmishra@ghmail.com', 'psswd': 'arhsimZdasarpZinirat'}, {'name': 'Mitu Nayak', 'email': 'mitunayak@ghmail.com', 'psswd': 'kayanZutim'}, {'name': 'Ajit Kumar Mishra', 'email': 'ajitkumarmishra@ghmail.com', 'psswd': 'arhsimZramukZtija'}, {'name': 'Siriki Simhachalam', 'email': 'sirikisimhachalam@ghmail.com', 'psswd': 'malahcahmisZikiris'}, {'name': 'Gopabandhu Dash', 'email': 'gopabandhudash@ghmail.com', 'psswd': 'hsadZuhdnabapog'}, {'name': 'Benudhar Prusty', 'email': 'benudharprusty@ghmail.com', 'psswd': 'ytsurpZrahduneb'}, {'name': 'Rabindra Nath Sethi', 'email': 'rabindranathsethi@ghmail.com', 'psswd': 'ihtesZhtanZardnibar'}, {'name': 'Pinak Bhusan Rath', 'email': 'pinakbhusanrath@ghmail.com', 'psswd': 'htarZnasuhbZkanip'}, {'name': 'Munna Kumar Churasia', 'email': 'munnakumarchurasia@ghmail.com', 'psswd': 'aisaruhcZramukZannum'}, {'name': 'Pradeep Ku Dahiya', 'email': 'pradeepkudahiya@ghmail.com', 'psswd': 'ayihadZukZpeedarp'}, {'name': 'Ashis Kumar Dubay', 'email': 'ashiskumardubay@ghmail.com', 'psswd': 'yabudZramukZsihsa'}, {'name': 'Arjuna Samal', 'email': 'arjunasamal@ghmail.com', 'psswd': 'lamasZanujra'}, {'name': 'Kishore Ku Sethi', 'email': 'kishorekusethi@ghmail.com', 'psswd': 'ihtesZukZerohsik'}, {'name': 'Ajaya Ku Mallick', 'email': 'ajayakumallick@ghmail.com', 'psswd': 'kcillamZukZayaja'}, {'name': 'Prasanta Ku Dash', 'email': 'prasantakudash@ghmail.com', 'psswd': 'hsadZukZatnasarp'}]


class tease_sulekha(scrapy.Spider):
    name = 'laggaye'
    link_type = []
    x = ''
    naam = []
    loglinks = []
    count = 0
    for i in range(15, 21):
        dat = datas[i]
        data = f"https://myaccount.sulekha.com/network/userauthsulv2.aspx?mode=login&loginvia=sulekha&socialid=&socialurl=&refurl=www.sulekha.com&name={dat['name']}&email={dat['email']}&photourl=&sLoginSite=sulekha&gender=&firstname=&lastname=&dob=&location=&city=&mobilenumber=&password={dat['psswd']}&AutoLogin=&rnd=0.234302582532947&callback=jQuery1102020072287705774539_1621484941081"
        loglinks.append(data)

    start_urls = loglinks

    def parse(self, response):
        mrand = random.choice(["12208", "57200", "57300"])
        review = random.choice(reviews)
        rev = f"https://www.sulekha.com/mvc5/lazy/v1/profile/save-review?PartialPageData=eyIkaWQiOiIxIiwiQ2l0eUlkIjo0MiwiQXJlYUlkIjo2MzMwLCJDYXRlZ29yeUlkIjo2MzYsIk5lZWRJZCI6MCwiUm91dGVOYW1lIjoiV2ViIERlc2lnbiBhbmQgRGV2ZWxvcG1lbnQiLCJQYWdlVmlld1R5cGUiOjcsIkhhc0xjZiI6ZmFsc2UsIklzT25seVByaW1hcnlUYWciOmZhbHNlLCJBcmVhTmFtZSI6IlBhdHJhcGFkYSIsIkNsZWFyQ2FjaGUiOmZhbHNlLCJWZXJzaW9uIjoyLCJJc0FkTGlzdGluZ1BhZ2UiOmZhbHNlLCJJc0FkRGV0YWlsUGFnZSI6ZmFsc2UsIlJlZk5lZWRJZCI6MCwiSXNQd2EiOmZhbHNlLCJEaXNhYmxlR29vZ2xlQWRzIjpmYWxzZSwiU3RhdGVDb2RlIjoiT1IiLCJSb3V0ZUlkIjoid2ViLWRlc2lnbi1hbmQtZGV2ZWxvcG1lbnQiLCJDaXR5TmFtZSI6IkJodWJhbmVzd2FyIn0%3D&UserPid=0&Review={review.replace(' ','+')}&Rating=4&NeedMetBusinessId=11075146&NeedMetBusinessName=Contrivers&Needid={mrand}"
        yield response.follow(rev, callback=self.temptest)

    # def parse(self, response):
    #     print("\n\n", response.css("p::text").extract_first(), "\n\n")
    #     # open_in_browser(response)
    #     checker = "https://www.sulekha.com/mvc5/lazy/v1/common/user-details?PartialPageData=eyIkaWQiOiIxIiwiQ2l0eUlkIjo0MiwiQXJlYUlkIjo2MzMwLCJDYXRlZ29yeUlkIjo2MzYsIk5lZWRJZCI6MCwiUm91dGVOYW1lIjoiV2ViIERlc2lnbiBhbmQgRGV2ZWxvcG1lbnQiLCJQYWdlVmlld1R5cGUiOjcsIkhhc0xjZiI6ZmFsc2UsIklzT25seVByaW1hcnlUYWciOmZhbHNlLCJBcmVhTmFtZSI6IlBhdHJhcGFkYSIsIkNsZWFyQ2FjaGUiOmZhbHNlLCJWZXJzaW9uIjoyLCJJc0FkTGlzdGluZ1BhZ2UiOmZhbHNlLCJJc0FkRGV0YWlsUGFnZSI6ZmFsc2UsIlJlZk5lZWRJZCI6MCwiSXNQd2EiOmZhbHNlLCJEaXNhYmxlR29vZ2xlQWRzIjpmYWxzZSwiU3RhdGVDb2RlIjoiT1IiLCJSb3V0ZUlkIjoid2ViLWRlc2lnbi1hbmQtZGV2ZWxvcG1lbnQiLCJDaXR5TmFtZSI6IkJodWJhbmVzd2FyIn0%3D"

    #     yield response.follow(checker, callback=self.temper)

    def temptest(self, response):
        print("\n\n", response.css("p::text").extract_first(), "\n\n")
        # ,callback=self.phirsere)
        yield response.follow('http://myaccount.sulekha.com/network/signout.aspx')

    # def phirsere(self, response):
    #     if self.count < 15:
    #         self.count += 1
    #         yield response.follow(self.loglinks[self.count], callback=self.parse)


process = CrawlerProcess(settings=dict)
process.crawl(tease_sulekha)
process.start()
