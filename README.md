# RSS Feed API

This is a simple Flask API that fetches and retrieves RSS feed data from different sources. It utilizes the `flask` and `flask_restful` libraries to create an API endpoint that returns JSON data containing the latest articles from configured RSS feeds.

## Prerequisites

Make sure you have the following libraries installed:

- Flask
- Flask-RESTful
- xmltodict
- requests-html

You can install these libraries using `pip`:

```
pip install flask flask-restful xmltodict requests-html
```

## Usage

1. Open the script file (`flask-rss-to-json.py`) in a text editor.

2. Modify the `targetfeeds` dictionary to configure the RSS feed sources and their corresponding URLs and images. You can add or remove sources as needed.

3. Customize the `nResults` variable to specify the number of articles you want to retrieve from each feed.

4. Save the modifications.

5. Run the script by executing the following command in your terminal:

```
python3 flask-rss-to-json.py
```

6. The API will start running on `http://localhost:5000/`.

## API Endpoint

- **GET `/`**: Returns JSON data containing the latest articles from the configured RSS feeds.

## Example Response

```json
{
  "herald": [
    {
      "title": "Article 1 Title",
      "link": "https://www.nzherald.co.nz/article1",
      "image": "https://img.shields.io/badge/H-8A2BE2"
    },
    {
      "title": "Article 2 Title",
      "link": "https://www.nzherald.co.nz/article2",
      "image": "https://img.shields.io/badge/H-8A2BE2"
    },
    ...
  ],
  "stuff": [
    {
      "title": "Article 1 Title",
      "link": "https://www.stuff.co.nz/article1",
      "image": "https://img.shields.io/badge/S-FF2BE2"
    },
    {
      "title": "Article 2 Title",
      "link": "https://www.stuff.co.nz/article2",
      "image": "https://img.shields.io/badge/S-FF2BE2"
    },
    ...
  ]
}
```

The response will contain a dictionary with each configured source as a key. The corresponding value will be a list of articles, where each article contains a title, link, and image.

**Note:** The number of articles returned will be based on the configured `nResults` variable.

## Customization

- You can modify the port number and host address in the `app.run()` statement to match your desired configuration.

- Feel free to customize other parts of the script as needed to meet your requirements.

---

That's it! You now have a Flask API for fetching and retrieving RSS feed data from different sources.