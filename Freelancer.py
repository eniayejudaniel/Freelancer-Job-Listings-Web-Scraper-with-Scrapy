import scrapy

class FreelancerSpider(scrapy.Spider):
    name = "Freelancer"
    allowed_domains = ["www.freelancer.com"]
    start_urls = ["https://www.freelancer.com/jobs"]
    page = 1
    headers = {
        "authority": "www.freelancer.com",
        "method": "GET",
        "path": f"/jobs/{page}/",
        "scheme": "https",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Cookie": "BROWSE_PROJECT_LISTING_keyword=; BROWSE_PROJECT_LISTING_duration=false; BROWSE_PROJECT_LISTING_budget_min=false; BROWSE_PROJECT_LISTING_budget_max=false; BROWSE_PROJECT_LISTING_hourlyrate_min=false; BROWSE_PROJECT_LISTING_hourlyrate_max=false; BROWSE_PROJECT_LISTING_budget_min_locale=30; BROWSE_PROJECT_LISTING_budget_max_locale=5000; BROWSE_PROJECT_LISTING_hourlyrate_min_locale=2; BROWSE_PROJECT_LISTING_hourlyrate_max_locale=100; BROWSE_PROJECT_LISTING_currencycode=USD; BROWSE_PROJECT_LISTING_contest_budget_min=false; BROWSE_PROJECT_LISTING_contest_budget_max=false; BROWSE_PROJECT_LISTING_contest_budget_min_locale=10; BROWSE_PROJECT_LISTING_contest_budget_max_locale=5000; _tracking_session=335e2914-7314-a268-bf6e-311821924a99; uniform_id_linked=linked; requires_gdpr=false; GETAFREE_NOTNEW=true; GETAFREE_LANGUAGE=en; qfence=eyJhbGciOiJIUzI1NiIsInR5cCI6IkZyZWVsYW5jZXJcXEdBRlxcQ29yZVxcSldUXFxKV1QifQ.eyI3MTA3Mzg2MCI6MTY5MDU2MzU3Nywic3ViIjoicXVpY2tsb2dpbmZlbmNlIiwiaWF0IjoxNjkwNTYzNTc3fQ.2Xn7-4JcrPu-Yf8WzoJZngW1oolb2d5z2FHW0ljcR2k; _gid=GA1.2.1613839183.1691432465; ln_or=eyIzMDQ1MzQ2IjoiZCJ9; XSRF-TOKEN=7gj2gR8lH4R4OZxoBddNyqgPqtnV7R36rjQHNPE6rHBNy8wnmT3G8FSF5NBepMxr; session2=9e69ac214366ed4709702ab591426023f3d5d63b907840390261f7f561e8cc68e2198b354919504f; USER_LANGUAGE_SEARCH_FILTER=tr; _hjSessionUser_1223449=eyJpZCI6ImUwYmNhNmJmLTI1YWUtNWZlOC04OWYxLTIyNjUwMTJhNWFiZSIsImNyZWF0ZWQiOjE2OTA1NjM1NDUzMjEsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_1223449=0; _hjSession_1223449=eyJpZCI6ImFiNjJlZjJiLWM0M2QtNGU5Ni1iOWQ2LTYwNThjYjU2MTEyYSIsImNyZWF0ZWQiOjE2OTE0MzQxNjM1ODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjHasCachedUserAttributes=true; _ga=GA1.2.d8baceea-fec9-6898-623d-6b4b87818495; _ga_31ZQKFK760=GS1.1.1691432461.2.1.1691434223.59.0.0; GETAFREE_JOB_SEARCH=[{\"keyword\":\"\",\"location\":{\"country\":\"\",\"vicinity\":\"\",\"lat\":\"\",\"lon\":\"\"}}]",
        "Referer": "https://www.freelancer.com/jobs",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }


    def start_requests(self):

        next_page = f"https://www.freelancer.com/jobs/{str(self.page)}"
        yield scrapy.Request(next_page, headers=self.headers, callback=self.parse)

        
    def parse(self, response):
        links = response.css('div.JobSearchCard-primary-heading a::attr(href)').getall()
        for link in links:
            url = f"https://www.freelancer.com/{link}"
            yield scrapy.Request(url, headers=self.headers, callback=self.get_info)

            self.page += 1
            if self.page <= 199:
                next_page = f"https://www.freelancer.com/jobs/{str(self.page)}"
                yield scrapy.Request(next_page, headers=self.headers, callback=self.parse)
    def get_info(self,response):
        job_title = response.css('h1.PageProjectViewLogout-projectInfo-title::text').get() 
        description = response.css('div.PageProjectViewLogout-detail p::text').getall()
        location = response.css('span[itemprop="addressLocality"]::text').get()
        price = response.css('p.PageProjectViewLogout-projectInfo-byLine::text').get()
        yield {
                "link": response.url,
                "job_title": job_title,
                "location": location,
                "description": description,
                "price": price
                
        }
