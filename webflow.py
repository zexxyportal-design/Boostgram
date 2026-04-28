<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoostGram | Premium Followers</title>
    <style>
        :root {
            --primary: #8a3ab9;
            --secondary: #e95950;
            --bg: #0f0f0f;
            --card-bg: #1a1a1a;
            --text: #ffffff;
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        header {
            text-align: center;
            margin-bottom: 40px;
        h1 {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1000px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            border: 1px solid #333;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
        }

        .price {
            font-size: 2rem;
            font-weight: bold;
            margin: 15px 0;
        }

        .btn {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin-top: 10px;
        }

        .btn:hover {
            opacity: 0.9;
        }

        .footer-note {
            margin-top: 50px;
            font-size: 0.8rem;
            color: #666;
        }
    </style>
</head>
<body>

<header>
    <h1>BoostGram Panel</h1>
    <p>High-Quality Followers • Instant Delivery</p>
</header>

<div class="container">
    <div class="card">
        <h3>Starter Pack</h3>
        <p>100 Followers</p>
        <div class="price">₹20</div>
        <a href="upi://pay?pa=8788599201@axl&pn=BoostGram&am=20&cu=INR" class="btn">Add Funds</a>
    </div>

    <div class="card">
        <h3>Growth Pack</h3>
        <p>5,000 Followers</p>
        <div class="price">₹150</div>
        <a href="upi://pay?pa=8788599201@axl&pn=BoostGram&am=150&cu=INR" class="btn">Add Funds</a>
    </div>

    <div class="card">
        <h3>Influencer Pack</h3>
        <p>10,000 Followers</p>
        <div class="price">₹250</div>
        <a href="upi://pay?pa=8788599201@axl&pn=BoostGram&am=250&cu=INR" class="btn">Add Funds</a>
    </div>
</div>

<p class="footer-note">Note: UPI links work best on mobile devices with UPI apps installed.</p>

</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoostGram | Official Store</title>
    <style>
        :root {
            --primary: #8a3ab9;
            --secondary: #e95950;
            --bg: #0f0f0f;
            --card-bg: #1a1a1a;
            --accent: #4caf50;
            --text: #ffffff;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .user-input-section {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            width: 100%;
            max-width: 400px;
            border: 1px solid #333;
            text-align: center;
        }

        input {
            width: 80%;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #444;
            background: #222;
            color: white;
            font-size: 1rem;
            margin-top: 10px;
        }

        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1000px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            border: 1px solid #333;
            transition: 0.3s;
        }

        .card:hover {
            border-color: var(--secondary);
            background: #222;
        }

        .price-tag {
            font-size: 1.8rem;
            color: var(--accent);
            margin: 10px 0;
        }

        .buy-btn {
            display: block;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            padding: 12px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 15px;
        }

        .buy-btn.disabled {
            background: #444;
            pointer-events: none;
            opacity: 0.5;
        }
    </style>
</head>
<body>

    <h2>Step 1: Enter Target Account</h2>
    <div class="user-input-section">
        <input type="text" id="ig-handle" placeholder="@8z3xy" oninput="toggleButtons()">
        <p style="font-size: 0.8rem; color: #aaa; margin-top: 8px;">Enter the 8z3xy before selecting a pack.</p>
    </div>

    <h2>Step 2: Choose Your Pack</h2>
    <div class="container">
        <div class="card">
            <h3>Basic</h3>
            <p>100 Bot Followers</p>
            <div class="price-tag">₹20</div>
            <a href="#" onclick="pay(20)" class="buy-btn disabled" id="btn-20">Add Funds</a>
        </div>

        <div class="card" style="border: 2px solid var(--primary);">
            <div style="background: var(--primary); font-size: 0.7rem; padding: 2px; border-radius: 5px; margin-bottom: 5px;">BEST VALUE</div>
            <h3>Silver</h3>
            <p>5,000 Bot Followers</p>
            <div class="price-tag">₹150</div>
            <a href="#" onclick="pay(150)" class="buy-btn disabled" id="btn-150">Add Funds</a>
        </div>

        <div class="card">
            <h3>Gold</h3>
            <p>10,000 Bot Followers</p>
            <div class="price-tag">₹250</div>
            <a href="#" onclick="pay(250)" class="buy-btn disabled" id="btn-250">Add Funds</a>
        </div>
    </div>

    <script>
        const upiId = "8788599201@axl";

        function toggleButtons() {
            const handle = document.getElementById('ig-handle').value;
            const buttons = document.querySelectorAll('.buy-btn');
            buttons.forEach(btn => {
                if(handle.length > 2) {
                    btn.classList.remove('disabled');
                } else {
                    btn.classList.add('disabled');
                }
            });
        }

        function pay(amount) {
            const handle = document.getElementById('ig-handle').value;
            const upiUrl = `upi://pay?pa=${upiId}&pn=BoostGram&am=${amount}&tn=Followers_for_${handle}&cu=INR`;
            window.location.href = upiUrl;
        }
    </script>

</body>
</html>
