from flask import Flask, request, render_template_string
import urllib.parse

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Angebotefinder</title>
<h1>Amazon Affiliate Link Generator</h1>
<form method="GET">
  Suchbegriff: <input name="q" value="{{ query or '' }}">
  <input type="submit" value="Link generieren">
</form>

{% if link %}
  <h2>🔗 Affiliate-Link:</h2>
  <p><a href="{{ link }}" target="_blank">{{ link }}</a></p>

  <h2>📲 WhatsApp-Text:</h2>
  <textarea rows="3" cols="60">Hey, schau dir das an: {{ link }}</textarea>
{% endif %}
'''

AFFILIATE_TAG = "miraunterwegs-21"

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q")
    link = None
    if query:
        encoded = urllib.parse.quote_plus(query)
        link = f"https://www.amazon.de/s?k={encoded}&tag={AFFILIATE_TAG}"
    return render_template_string(HTML, link=link, query=query)
