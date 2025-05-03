from flask import Flask, redirect, render_template, request, url_for

# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
app = Flask(__name__)

@app.before_request
def redirect_to_www():
    # Skip redirect for local development
    if request.host.startswith("127.0.0.1") or request.host.startswith("localhost"):
        return
    if not request.host.startswith("www."):
        new_url = request.url.replace(f"//{request.host}", f"//www.{request.host}")
        return redirect(new_url, code=301)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/about-pawan')
def pawan():
    return render_template('about-pawan.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-redirect.html'), 404


if __name__ == "__main__":
    app.run(debug=True)