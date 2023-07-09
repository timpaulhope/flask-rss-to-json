from flask import Flask
from flask_restful import Resource, Api
import xmltodict
from requests_html import HTMLSession
import yaml
import requests.exceptions
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
api = Api(app)

def load_configuration(file_path):
    """Load configuration from YAML file."""
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def get_source(url):
    """Fetch the RSS feed source."""
    try:
        session = HTMLSession()
        response = session.get(url)
        response.raise_for_status()  # Raise an exception if request fails
        return response

    except requests.exceptions.RequestException as e:
        raise Exception("Failed to fetch the RSS feed source.") from e

class JsonOut(Resource):
    def get(self):
        return df_out

def update_feeds():
    """Update the RSS feeds periodically."""
    global df_out
    for source, attributes in target_feeds.items():
        response = get_source(attributes["feed_url"])
        data_dict = xmltodict.parse(response.text)
        articles = data_dict["rss"]["channel"]["item"]

        df_row = []
        for i in range(n_results):
            article = articles[i]
            title = article["title"]
            link = article["link"]
            img = attributes["image"]
            df_row.append({'title': title, 'link': link, 'image': img})

        df_out[source] = df_row

if __name__ == "__main__":
    config = load_configuration('config.yaml')
    target_feeds = config['target_feeds']
    n_results = config['n_results']
    custom_port = config['port']

    df_out = {}  # Global variable to store the feed data

    # Initialize the feed data
    update_feeds()

    # Create a scheduler to refresh the feeds every 5 minutes
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_feeds, 'interval', minutes=5)
    scheduler.start()

    # Assign the JsonOut resource to the root endpoint
    api.add_resource(JsonOut, '/')
    # Run the Flask app on the specified host and port
    app.run(host='0.0.0.0', port=custom_port, debug=True)
