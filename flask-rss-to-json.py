from flask import Flask
from flask_restful import Resource, Api
import xmltodict
from requests_html import HTMLSession
app = Flask(__name__)
api = Api(app)

# RSS config
targetfeeds = {
    "herald" : {
        "feedurl" : "https://www.nzherald.co.nz/arc/outboundfeeds/rss/curated/78/?outputType=xml&_website=nzh", 
        "image" : "https://img.shields.io/badge/H-8A2BE2"
    },
    "stuff" : {
        "feedurl" :"https://www.stuff.co.nz/rss",
        "image" : "https://img.shields.io/badge/S-FF2BE2"
    }
}
nResults = 5

# -- Get rss Feed ----
def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

class JsonOut(Resource):
    def get(self):
        dfOut = {}
        dfSource = {}

        # -- loop through config dictionary ----
        for source, attributes in targetfeeds.items():
   
            response = get_source(attributes["feedurl"])    # <- get rss feed
            data_dict = xmltodict.parse(response.text)      # <- Parse response into a dictionary
            articles = data_dict["rss"]["channel"]["item"] # <- Get the items
            dfRow = []
    
            # print(articles)
    
            for i in range(nResults):
                article = articles[i]
                title = article["title"]
                link = article["link"]
                img = attributes["image"]
                dfRow.append({'title': title,'link': link, 'image': img})        #'link'= link)  
    
            # add source 
            dfSource[source] = dfRow

        return(dfSource)

api.add_resource(JsonOut, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)