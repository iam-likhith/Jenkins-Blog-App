from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Start a Successful Jenikins Pipeline</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto:wght@400;900&display=swap');
            
            body { font-family: 'Roboto', sans-serif; }
            .hero-text { font-family: 'Oswald', sans-serif; }
            
            /* The diagonal red background clip */
            .diagonal-bg {
                background-color: #b3262d;
                clip-path: polygon(0 12%, 100% 0, 100% 100%, 0 100%);
                margin-top: -50px;
            }

            /* The custom arrow-shaped button */
            .cta-button {
                background: white;
                color: black;
                padding: 12px 30px;
                font-weight: bold;
                display: inline-flex;
                align-items: center;
                border: 2px solid #000;
                clip-path: polygon(0% 0%, 90% 0%, 100% 50%, 90% 100%, 0% 100%);
                transition: transform 0.2s;
            }
            .cta-button:hover { transform: scale(1.05); }

            .logo-box {
                border: 3px solid #b3262d;
                padding: 2px 8px;
                display: inline-block;
                color: white;
                background: #b3262d;
                font-weight: 900;
                font-style: italic;
            }
        </style>
    </head>
    <body class="bg-white">
        <header class="flex justify-between items-center px-16 py-8 relative z-10">
            <div class="logo-box">
                <span class="text-white text-2xl">★ BLOG START ★</span>
            </div>
            <nav class="space-x-10 text-lg font-bold">
                <a href="#" class="text-black hover:text-red-700">New?</a>
                <a href="#" class="text-black hover:text-red-700">Tools</a>
                <a href="#" class="text-black hover:text-red-700">Join</a>
                <a href="#" class="text-black hover:text-red-700">Blog</a>
            </nav>
        </header>

        <section class="diagonal-bg pt-40 pb-24 px-16 text-white flex justify-between items-center">
            <div class="max-w-2xl">
                <div class="border-l-4 border-black pl-4 mb-2">
                    <p class="hero-text text-4xl uppercase italic leading-none">Want to start a</p>
                </div>
                <h1 class="hero-text text-9xl uppercase font-black tracking-tighter mb-6">
                    Successful Blog?
                </h1>
                <p class="text-2xl italic mb-10">Here's how to do it the right way.</p>
                
                <a href="#" class="cta-button text-xl">
                    Beginner's Guide to Start a Blog —>>
                </a>
            </div>
            
            <div class="hidden lg:block w-1/3 opacity-90">
                <img src="https://cdni.iconscout.com/illustration/premium/thumb/superhero-businessman-4488347-3738450.png" alt="Hero">
            </div>
        </section>

        <footer class="bg-[#111] text-white py-10 px-6 text-center">
            <div class="flex flex-wrap justify-center gap-6 text-sm mb-6 border-b border-gray-700 pb-6">
                <span class="font-bold">Contact Us:</span>
                <span>📧 support@blogstart.com</span>
                <span>🌐 www.blogstart.com</span>
                <span>📍 Hyderabad, India</span>
            </div>
            
            <div class="flex justify-center flex-wrap gap-8 text-sm opacity-70 mb-6">
                <span class="font-bold italic opacity-100">Forbes</span>
                <span>Medium</span>
                <span>Dev.to</span>
                <span>Hashnode</span>
                <span>TechCrunch</span>
            </div>
            
            <p class="text-xs text-gray-500">
                Built with <span class="font-bold text-gray-300">Flask & Docker 🚀</span>
            </p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/health")
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)