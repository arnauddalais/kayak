import scrapy

class BookingSpider(scrapy.Spider):
    name = "booking"

    #starting URL
    start_urls = ['https://www.booking.com/searchresults.fr.html']
    
    #init function for cities
    def __init__(self):
        self.list_cities = ["Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris", "Amiens", "Lille", "Strasbourg", 
"Chateau du Haut Koenigsbourg", "Colmar", "Eguisheim", "Besancon", "Dijon", "Annecy", "Grenoble", "Lyon", "Gorges du Verdon",
"Bormes les Mimosas", "Cassis", "Marseille", "Aix en Provence", "Avignon", "Uzes", "Nimes", "Aigues Mortes", "Saintes Maries de la mer",
"Collioure", "Carcassonne","Ariege", "Toulouse", "Montauban", "Biarritz", "Bayonne", "La Rochelle"]

    
    #parse function
    def parse(self, response):
        for i, city in enumerate(self.list_cities):
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"ss": city},
                callback= self.result,
                #id_city is the key for merging the both files after.
                cb_kwargs = {'id_city' : i}
            )
    
    def result(self, response, id_city):
       
        hotel_names = response.xpath('//*[@class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f"]/div[1]/div/div[1]/div/h3/a/div[1]/text()')
        urls = response.xpath('//*[@class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f"]/div[1]/div/div[1]/div/h3/a')
        scores = response.xpath('//*[@class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f"]/div[2]/div[1]/a/span/div/div[1]/text()')
        texts = response.xpath('//*[@class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f"]/div[1]/div/div[3]/text()')
  
        for hotel_name, url, score, text in zip(hotel_names, urls, scores, texts):
            yield scrapy.Request(
                url = response.urljoin(url.attrib["href"]),
                callback=self.hotel_latlon,
                cb_kwargs = {
                    'id_city' : id_city,
                    'city' : response.xpath('//*[@id="right"]/div[1]/div/div/div/h1/text()').get().split(':')[0],
                    'hotel_name': hotel_name.get(),
                    'url': url.attrib["href"],
                    'score' : score.get(),
                    'text' : text.get()
                }
            )

    def hotel_latlon(self, response, id_city, city, hotel_name, url, score, text) :

        yield {
            'id_city' : id_city,
            'city' : city,
            'hotel_name': hotel_name,
            'url': url,
            'score' : score,
            'text' : text,
            'latlon': response.xpath('//*[@id="hotel_header"]').attrib['data-atlas-latlng'],
        }