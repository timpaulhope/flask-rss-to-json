# RSS Feed Aggregator

This is a Flask API that reads RSS feeds from a YAML configuration file and serves a JSON endpoint. The API returns the title, link, and an image for the first n results of each feed.

## Prerequisites

Make sure you have the following libraries installed:

- Flask
- Flask-RESTful
- xmltodict
- requests-html
- PyYAML
- apscheduler

You can install these libraries using `pip`:

```
pip install flask flask-restful xmltodict requests-html pyyaml apscheduler
```

## Configuration

1. Open the `config.yaml` file located in the same directory as the script.

2. Configure the `target_feeds` section with the RSS feed sources you want to fetch. Each feed should have a unique key and include the `feed_url` and `image` attributes.

3. Set the `n_results` value to specify the number of results you want to retrieve from each feed.

4. Optionally, modify the `port` value to set a custom port number for the API (default is 5000).

5. Save the modifications.

## Usage

1. Open the script file (`app.py`) in a text editor.

2. Ensure that the `config.yaml` file is in the same directory as `app.py`.

3. Run the script by executing the following command in your terminal:

```
python app.py
```

4. The API will start running on `http://localhost:<port>/`.

## API Endpoint

- **GET `/`**: Returns a JSON object containing the first n results of each configured RSS feed. The JSON object is structured with each feed as a key and the corresponding results as a list of objects containing the title, link, and image.

## Example Response

The response will be a JSON object with each configured feed as a key. The corresponding value will be a list of objects, where each object represents an article and includes the title, link, and image attributes.

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

The number of results returned will be based on the configured `n_results` value.

## Customization

- You can modify the `port` value in the `config.yaml` file to set a custom port number for the API.

- Feel free to customize other parts of the script as needed to meet your requirements.

---

That's it! You now have a Flask API that reads RSS feeds from a configuration file and serves the data as JSON.