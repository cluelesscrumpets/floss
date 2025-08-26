from flask import Flask, Response, redirect, render_template, request, url_for
from csscompressor import compress
import os
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug("This is a debug message")

# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
app = Flask(__name__)

"""@app.before_request
def redirect_to_www():
    # Skip redirect for local development
    if request.host.startswith("127.0.0.1") or request.host.startswith("localhost"):
        return
    if not request.host.startswith("www."):
        new_url = request.url.replace(f"//{request.host}", f"//www.{request.host}")
        return redirect(new_url, code=301)
"""
@app.route("/robots.txt")
def robots():
    robots_text = """User-agent: *
    Disallow:
    Sitemap: https://flossdentalclinic.online/sitemap.xml
    """
    return Response(robots_text, mimetype="text/plain")

def minify_css(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"[!] CSS input file not found: {input_path}")
        return
    with open(input_path, 'r') as f:
        css = f.read()
    minified = compress(css)
    with open(output_path, 'w') as f:
        f.write(minified)
    print(f"[✓] Minified CSS saved to {output_path}")

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-redirect.html'), 404


if __name__ == "__main__":
    minify_css('static/style.css', 'static/style.min.css')
    app.run(debug=True)
