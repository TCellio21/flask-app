from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cloud Survival Dashboard</title>
        <style>
            * { box-sizing: border-box; }

            body {
                margin: 0;
                padding: 60px 24px;
                background: #0f172a;
                color: #f1f5f9;
                font-family: Arial, sans-serif;
            }

            main { max-width: 1000px; margin: auto; }

            .badge {
                color: #38bdf8;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 2px;
            }

            h1 { font-size: 40px; margin-bottom: 12px; }
            .subtitle { color: #94a3b8; line-height: 1.6; }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 20px;
                margin-top: 32px;
            }

            .card {
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 18px;
                padding: 26px;
            }

            h2 { font-size: 20px; margin-top: 0; }

            #clock {
                font-size: 32px;
                font-weight: bold;
                color: #38bdf8;
                margin: 24px 0 12px;
            }

            #date, .muted { color: #94a3b8; line-height: 1.6; }

            .status {
                color: #4ade80;
                font-weight: bold;
                font-size: 22px;
                margin: 24px 0;
            }

            label {
                display: flex;
                align-items: flex-start;
                gap: 10px;
                padding: 12px 0;
                line-height: 1.4;
                cursor: pointer;
            }

            input {
                accent-color: #38bdf8;
                margin-top: 3px;
                width: 18px;
                height: 18px;
                flex-shrink: 0;
            }

            input:checked + span {
                color: #94a3b8;
                text-decoration: line-through;
            }

            footer {
                margin-top: 32px;
                color: #94a3b8;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <main>
            <div class="badge">HELLO MSOE · VERSION 2</div>
            <h1>Cloud Survival Dashboard</h1>
            <p class="subtitle">
                Tanner's command center for finishing the lab
                and making it to bedtime.
            </p>

            <div class="grid">
                <section class="card">
                    <h2>Current Time</h2>
                    <div id="clock"></div>
                    <div id="date"></div>
                    <p class="muted">
                        Your local time. The deadline approaches.
                    </p>
                </section>

                <section class="card">
                    <h2>Lab Survival Checklist</h2>
                    <label>
                        <input type="checkbox">
                        <span>Convince the cloud to run my app.</span>
                    </label>
                    <label>
                        <input type="checkbox">
                        <span>Make the app look impressive.</span>
                    </label>
                    <label>
                        <input type="checkbox">
                        <span>Take screenshots as proof.</span>
                    </label>
                    <label>
                        <input type="checkbox">
                        <span>Submit the lab and feedback.</span>
                    </label>
                    <label>
                        <input type="checkbox">
                        <span>Delete cloud app. Eat. Sleep.</span>
                    </label>
                </section>

                <section class="card">
                    <h2>Deployment Status</h2>
                    <p class="status">✓ Deployment successful!</p>
                    <p class="muted">
                        If you are reading this at my DigitalOcean URL,
                        the enhanced Flask app is live.
                    </p>
                    <p class="muted">
                        It worked on my machine. Now it works
                        on someone else's.
                    </p>
                </section>
            </div>

            <footer>
                Microservices & Cloud Compute · Flask + DigitalOcean
            </footer>
        </main>

        <script>
            function updateClock() {
                const now = new Date();
                document.getElementById("clock").textContent =
                    now.toLocaleTimeString();
                document.getElementById("date").textContent =
                    now.toLocaleDateString(undefined, {
                        weekday: "long",
                        month: "long",
                        day: "numeric",
                        year: "numeric"
                    });
            }

            updateClock();
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """