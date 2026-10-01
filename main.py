import os
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template_string, url_for

app = Flask(__name__)

BUSINESS = "Horse Country Outdoor Services"
PHONE = "859-880-2202"
PHONE_LINK = "tel:+18598802202"

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description"
          content="Lawn care, deck staining and deck repairs in Georgetown,
                   Kentucky and surrounding areas. Call 859-880-2202.">
    <meta name="theme-color" content="#123b88">
    <title>{{ title }} | {{ business }}</title>

    <style>
        :root {
            --blue: #123b88;
            --dark: #122c41;
            --cream: #faf9f5;
            --muted: #526474;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            background: var(--cream);
            color: var(--dark);
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
        }

        a { color: inherit; }

        a:focus-visible, summary:focus-visible {
            outline: 3px solid #e5ac32;
            outline-offset: 5px;
        }

        .wrap {
            width: min(1150px, calc(100% - 40px));
            margin: auto;
        }

        .topbar {
            padding: 10px 20px;
            background: var(--blue);
            color: white;
            text-align: center;
            font-size: 12px;
            letter-spacing: 1px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 24px;
            padding: 22px 0;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            font-size: 22px;
            font-weight: bold;
            line-height: 1.2;
        }

        .brand img {
            width: 65px;
            height: 65px;
            object-fit: contain;
        }

        .brand small {
            display: block;
            margin-top: 6px;
            font-size: 10px;
            letter-spacing: 2px;
        }

        nav {
            display: flex;
            gap: 25px;
            flex-shrink: 0;
        }

        nav a {
            padding: 8px 0;
            text-decoration: none;
            font-size: 14px;
        }

        nav a[aria-current="page"] {
            border-bottom: 2px solid var(--blue);
        }

        .hero {
            padding: 65px 0;
            background: #eaf0f3;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .eyebrow {
            margin: 0 0 18px;
            color: var(--blue);
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 2px;
        }

        h1, h2, h3 {
            margin: 0;
            line-height: 1.1;
            letter-spacing: -1px;
        }

        h1 { font-size: clamp(42px, 5.5vw, 72px); }
        h2 { font-size: clamp(30px, 3.5vw, 44px); }
        h3 { font-size: 28px; }

        .intro {
            max-width: 550px;
            margin: 25px 0;
            color: var(--muted);
            font-size: 18px;
        }

        .actions {
            display: flex;
            align-items: center;
            gap: 22px;
            flex-wrap: wrap;
        }

        .button {
            display: inline-block;
            padding: 15px 24px;
            border-radius: 5px;
            background: var(--blue);
            color: white;
            font-weight: bold;
            text-decoration: none;
        }

        .button:hover { background: #092859; }

        .brand-panel {
            padding: 32px;
            border-radius: 100px 100px 8px 8px;
            background: var(--blue);
            color: white;
            text-align: center;
        }

        .brand-panel img {
            display: block;
            width: min(100%, 320px);
            height: auto;
            margin: 0 auto 22px;
        }

        .brand-panel .eyebrow { color: #c9dfff; }

        .brand-panel h2 { font-size: 34px; }

        .brand-panel p:last-child { color: #d9e6ff; }

        .section { padding: 65px 0; }

        .section-heading { margin-bottom: 32px; }

        .section-heading p {
            max-width: 620px;
            color: var(--muted);
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .card {
            display: flex;
            flex-direction: column;
            padding: 30px;
            border: 1px solid #dce3e6;
            border-radius: 7px;
            background: white;
        }

        .card.featured {
            background: var(--blue);
            color: white;
            border-color: var(--blue);
        }

        .card.featured .eyebrow { color: #c9dfff; }

        .card ul {
            margin: 24px 0;
            padding: 0;
            list-style: none;
        }

        .card li {
            padding: 9px 0;
            border-bottom: 1px solid #dce3e6;
            font-size: 15px;
        }

        .card.featured li {
            border-color: rgba(255,255,255,.2);
        }

        .card a {
            margin-top: auto;
            font-weight: bold;
            font-size: 14px;
        }

        .area { background: #e7eeeb; }

        .area p {
            max-width: 650px;
            color: var(--muted);
        }

        details {
            max-width: 650px;
            margin-top: 30px;
            padding: 20px;
            border-radius: 6px;
            background: white;
        }

        summary { cursor: pointer; font-weight: bold; }

        .poster {
            display: block;
            width: 100%;
            height: auto;
            margin-top: 20px;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-top: 35px;
        }

        .call-box {
            padding: 36px;
            border-radius: 8px;
            background: var(--blue);
            color: white;
        }

        .call-box .eyebrow { color: #c9dfff; }

        .call-box h2 {
            font-size: clamp(28px, 3.7vw, 44px);
        }

        .call-box p { color: #d9e6ff; }

        .call-box .button {
            margin-top: 15px;
            background: white;
            color: var(--blue);
        }

        .call-box .button:hover { background: #e4edff; }

        .contact-details li { padding: 7px 0; }

        .contact-details p { color: var(--muted); }

        footer {
            padding: 35px 0;
            background: var(--dark);
            color: white;
        }

        .footer-grid {
            display: flex;
            justify-content: space-between;
            gap: 25px;
        }

        footer p {
            margin: 8px 0;
            color: #c4d2de;
            font-size: 13px;
        }

        .copyright { margin-top: 25px; }

        .skip {
            position: absolute;
            top: -100px;
            left: 15px;
            padding: 12px;
            background: white;
        }

        .skip:focus { top: 10px; }

        @media (max-width: 760px) {
            header { flex-wrap: wrap; gap: 15px; }
            .brand { font-size: 19px; }
            .brand img { width: 50px; height: 50px; }
            nav { gap: 24px; }
            .hero { padding: 40px 0; }
            .hero-grid, .cards, .contact-grid {
                grid-template-columns: 1fr;
                gap: 24px;
            }
            .brand-panel { border-radius: 60px 60px 8px 8px; }
            .brand-panel img { width: 220px; }
            .section { padding: 45px 0; }
            .footer-grid { flex-direction: column; }
            .call-box { padding: 28px; }
        }
    </style>
</head>

<body>
    <a class="skip" href="#main">Skip to content</a>

    <div class="topbar">
        GEORGETOWN, KY & SURROUNDING AREAS
    </div>

    <header class="wrap">
        <a class="brand" href="{{ url_for('information') }}">
            {% if has_logo %}
                <img src="{{ url_for('static', filename='logo.png') }}"
                     alt="Horse Country Outdoor Services logo">
            {% endif %}
            <span>
                Horse Country
                <small>OUTDOOR SERVICES</small>
            </span>
        </a>

        <nav aria-label="Main navigation">
            <a href="{{ url_for('information') }}"
               {% if page == 'information' %}aria-current="page"{% endif %}>
                Information
            </a>
            <a href="{{ url_for('contact') }}"
               {% if page == 'contact' %}aria-current="page"{% endif %}>
                Contact us
            </a>
        </nav>
    </header>

    <main id="main">
        {% if page == 'information' %}
        <section class="hero">
            <div class="wrap hero-grid">
                <div>
                    <p class="eyebrow">LAWN CARE IN GEORGETOWN, KENTUCKY</p>
                    <h1>A yard you’re proud to come home to.</h1>
                    <p class="intro">
                        From lawn mowing and crisp edges to seasonal cleanup,
                        give your outdoor space the attention it deserves.
                    </p>
                    <div class="actions">
                        <a class="button" href="{{ url_for('contact') }}">
                            Talk about your lawn
                        </a>
                        <a href="{{ phone_link }}">Call {{ phone }}</a>
                    </div>
                </div>

                <div class="brand-panel">
                    {% if has_logo %}
                        <img src="{{ url_for('static', filename='logo.png') }}"
                             alt="Horse Country Outdoor Services">
                    {% endif %}
                    <p class="eyebrow">CARE FOR YOUR OUTDOORS</p>
                    <h2>Your lawn.<br>Your deck.<br>Your place to unwind.</h2>
                    <p>Serving Georgetown and surrounding areas.</p>
                </div>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-heading">
                <p class="eyebrow">OUR SERVICES</p>
                <h2>Lawn care comes first.</h2>
                <p>
                    Keep your yard looking its best, then bring new life
                    to your deck with staining, sealing and repairs.
                </p>
            </div>

            <div class="cards">
                <article class="card featured">
                    <p class="eyebrow">01 / LAWN CARE</p>
                    <h3>A cleaner cut.<br>A tidier yard.</h3>
                    <ul>
                        <li>Lawn mowing</li>
                        <li>Trimming & edging</li>
                        <li>Weed control</li>
                        <li>Yard cleanup</li>
                        <li>Seasonal maintenance</li>
                    </ul>
                    <a href="{{ url_for('contact') }}">Discuss lawn care →</a>
                </article>

                <article class="card">
                    <p class="eyebrow">02 / DECK STAINING</p>
                    <h3>Refresh your<br>outdoor wood.</h3>
                    <ul>
                        <li>Deck cleaning & preparation</li>
                        <li>Deck staining</li>
                        <li>Wood sealing & protection</li>
                        <li>Refresh faded decks</li>
                        <li>Care to help extend deck life</li>
                    </ul>
                    <a href="{{ url_for('contact') }}">Discuss staining →</a>
                </article>

                <article class="card">
                    <p class="eyebrow">03 / DECK REPAIRS</p>
                    <h3>Give your deck<br>some attention.</h3>
                    <ul>
                        <li>Damaged board replacement</li>
                        <li>Railing repairs</li>
                        <li>Stair repairs</li>
                        <li>Rot & weather damage</li>
                        <li>General deck maintenance</li>
                    </ul>
                    <a href="{{ url_for('contact') }}">Discuss repairs →</a>
                </article>
            </div>
        </section>

        <section class="area section">
            <div class="wrap">
                <p class="eyebrow">CLOSE TO HOME</p>
                <h2>Georgetown, KY<br>& surrounding areas.</h2>
                <p>
                    Call with your location and the work you have in mind
                    to discuss service availability and pricing.
                </p>
                <a class="button" href="{{ phone_link }}">Call {{ phone }}</a>

                {% if has_poster %}
                <details>
                    <summary>View our service flyer</summary>
                    <img class="poster"
                         src="{{ url_for('static', filename='services-poster.png') }}"
                         alt="Horse Country lawn care, deck staining and deck
                              repair services flyer. Call 859-880-2202."
                         loading="lazy">
                </details>
                {% endif %}
            </div>
        </section>

        {% else %}
        <section class="wrap section">
            <p class="eyebrow">CONTACT US</p>
            <h1>Let’s talk<br>about your yard.</h1>
            <p class="intro">
                Need lawn care, a deck refresh or a repair?
                Call Horse Country Outdoor Services to discuss your project.
            </p>

            <div class="contact-grid">
                <div class="call-box">
                    <p class="eyebrow">START A CONVERSATION</p>
                    <h2>{{ phone }}</h2>
                    <p>
                        Tell us what needs attention, where you’re located
                        and when you’d like the work done.
                    </p>
                    <a class="button" href="{{ phone_link }}">Call now ↗</a>
                </div>

                <div class="contact-details">
                    <h2>A little detail<br>goes a long way.</h2>
                    <p>Have these details ready when you call:</p>
                    <ol>
                        <li>Your name and callback number</li>
                        <li>Your address or neighborhood</li>
                        <li>The service you need</li>
                        <li>Your preferred timing</li>
                    </ol>
                    <p>
                        <strong>Service area:</strong><br>
                        Georgetown, Kentucky and surrounding areas.
                        Call to confirm availability for your location.
                    </p>
                    <a href="{{ url_for('information') }}">
                        Explore our services →
                    </a>
                </div>
            </div>
        </section>
        {% endif %}
    </main>

    <footer>
        <div class="wrap">
            <div class="footer-grid">
                <div>
                    <strong>{{ business }}</strong>
                    <p>Lawn care. Deck staining. Deck repairs.</p>
                </div>
                <div>
                    <a href="{{ phone_link }}">{{ phone }}</a>
                    <p>Georgetown, KY & surrounding areas</p>
                </div>
            </div>
            <p class="copyright">© {{ year }} {{ business }}</p>
        </div>
    </footer>
</body>
</html>
"""


def show_page(page, title):
    assets = Path(app.static_folder)
    return render_template_string(
        PAGE,
        page=page,
        title=title,
        business=BUSINESS,
        phone=PHONE,
        phone_link=PHONE_LINK,
        year=datetime.now().year,
        has_logo=(assets / "logo.png").is_file(),
        has_poster=(assets / "services-poster.png").is_file(),
    )


@app.get("/")
def information():
    return show_page("information", "Lawn Care & Deck Services")


@app.get("/contact")
def contact():
    return show_page("contact", "Contact Us")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
