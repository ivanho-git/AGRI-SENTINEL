import os

files = ['login.html', 'onboarding.html', 'dashboard.html', 'history.html', 'market-help.html', 'index.html']
templates_dir = 'templates'

premium_readable_css = """
        /* ==================================================
           ULTIMATE READABILITY & ENTERPRISE PREMIUM DESIGN
           ================================================== */
        :root {
            /* Clean & Crisp Colors */
            --green-900: #022c22;
            --green-800: #064e3b;
            --green-700: #047857;
            --green-600: #059669;
            --green-500: #10b981;
            --green-400: #34d399;
            --green-300: #6ee7b7;
            --green-100: #d1fae5;
            --green-50:  #ecfdf5;
            
            --g9: #022c22; --g8: #064e3b; --g7: #047857; --g6: #059669; --g5: #10b981;
            --g4: #34d399; --g3: #6ee7b7; --g2: #a7f3d0; --g1: #d1fae5; --g0: #ecfdf5;

            var(--bg): #f8fafc; 
            --card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #475569;
            --text-faint: #94a3b8;

            /* Override existing variables for perfect legibility */
            --text: #0f172a;
            --text2: #334155;
            --text3: #475569;
            --txt: #0f172a;
            --txt2: #334155;
            --txt3: #475569;
            --txtF: #64748b;

            --border: #e2e8f0;
            --border-light: #f1f5f9;
            --bdr: #e2e8f0;
            --bdrL: #f1f5f9;
        }

        body {
            color: var(--text-main) !important;
            font-family: 'Outfit', 'Inter', -apple-system, sans-serif !important;
            background: #f8fafc !important; 
        }

        /* ATMOSPHERIC BUT 100% READABLE BACKGROUND */
        body::before {
            content: ''; 
            position: fixed; 
            inset: 0;
            /* 93% opaque white overlay over the farm image - creates a beautiful texture without compromising readability */
            background-image: 
                linear-gradient(to bottom, rgba(255,255,255,0.92), rgba(248, 250, 252, 0.95)),
                url('https://images.unsplash.com/photo-1590682680695-43b964a3ae17?q=80&w=2600&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            z-index: -2; 
        }

        /* Crisp, Solid White Cards with Soft Premium Shadows */
        .card, .phase-section, .upload-box, .stat, .weather, .summary-card, .recipe-card, .soil-data-section, .chat-container .welcome, .scan-card, .table-wrap, .form-wrap .card, .community {
            background: #ffffff !important;
            border: 1px solid rgba(226, 232, 240, 0.8) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 10px 25px -5px rgba(0, 0, 0, 0.03) !important;
            border-radius: 20px !important;
            color: var(--text-main) !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
            backdrop-filter: none !important; /* Removed blur to ensure pure white clarity */
        }

        .card:hover, .stat:hover, .scan-card:hover, .type-opt:hover {
            border-color: rgba(16, 185, 129, 0.3) !important;
            box-shadow: 0 10px 20px -3px rgba(16, 185, 129, 0.08), 0 20px 40px -10px rgba(0,0,0,0.05) !important;
            transform: translateY(-3px) !important;
            background: #ffffff !important;
        }

        /* Vivid, Accessible Buttons */
        .btn, .action-btn, .gps-btn, .forum-btn, .pill-btn, .cta-button, .speak-btn {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%) !important;
            color: #ffffff !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25) !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            letter-spacing: 0.3px !important;
            border-radius: 12px !important;
            transition: all 0.2s ease !important;
        }

        .btn:hover, .action-btn:hover, .gps-btn:hover, .forum-btn:hover, .pill-btn:hover, .cta-button:hover, .speak-btn:hover {
            box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4) !important;
            transform: translateY(-1px) !important;
            background: linear-gradient(135deg, #047857 0%, #059669 100%) !important;
        }

        .btn-send {
            background: #10b981 !important;
            border-radius: 50% !important;
            box-shadow: 0 4px 10px rgba(16, 185, 129, 0.2) !important;
            color: #ffffff !important;
            border: none !important;
        }

        .btn-mic {
            background: #ecfdf5 !important;
            color: #059669 !important;
            border: 1px solid #d1fae5 !important;
            border-radius: 50% !important;
        }

        /* High Visibility Inputs */
        .input, .select, .form-input, .form-select, #inp, select {
            background: #f8fafc !important;
            border: 1px solid #cbd5e1 !important;
            color: #0f172a !important;
            border-radius: 12px !important;
            padding: 14px 16px !important;
            font-size: 15px !important;
            font-weight: 500 !important;
            transition: all 0.2s ease !important;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.02) !important;
            backdrop-filter: none !important;
        }
        
        .input::placeholder, #inp::placeholder {
            color: #94a3b8 !important;
            font-weight: 400 !important;
        }

        .input:focus, .select:focus, .form-input:focus, .form-select:focus, #inp:focus {
            background: #ffffff !important;
            border-color: #10b981 !important;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15) !important;
            outline: none !important;
        }

        /* Flawless Typography */
        h1, h2, h3, h4, h5, .title, .panel-title, .brand-name, .disease-name {
            color: #022c22 !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em !important;
            text-shadow: none !important;
        }
        
        /* Label Readability */
        .label {
            color: #334155 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
            letter-spacing: 0.01em !important;
        }

        /* Layout specific visibility overrides */
        .panel {
            background: transparent !important;
            position: relative;
        }
        
        .panel::before {
            content: '';
            position: absolute; inset: 0;
            /* Provide a solid contrasting green for the left login panel */
            background: linear-gradient(145deg, #022c22 0%, #064e3b 100%) !important;
            z-index: -1;
        }

        .panel-content, .panel-title, .panel-sub {
            color: #ffffff !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }
        
        .panel-feat {
            background: rgba(255,255,255,0.1) !important;
            border-color: rgba(255,255,255,0.15) !important;
            color: #ffffff !important;
            backdrop-filter: blur(8px) !important;
        }
        
        .panel-feat .ft { color: #ffffff !important; font-weight: 600 !important; }

        .topbar, .nav {
            background: #ffffff !important;
            border-bottom: 1px solid #e2e8f0 !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02) !important;
            backdrop-filter: none !important;
        }
        
        .topbar-logo, .logo, .nav-links a {
            color: #064e3b !important;
            font-weight: 800 !important;
        }

        .topbar-nav a {
            color: #475569 !important;
            border: 1px solid transparent !important;
            font-weight: 600 !important;
            background: transparent !important;
        }
        
        .topbar-nav a:hover, .topbar-nav a.active {
            background: #f1f5f9 !important;
            color: #064e3b !important;
        }
        
        .topbar-nav .logout {
            color: #ef4444 !important;
            background: #fef2f2 !important;
        }

        .diagnosis-header {
            background: #ecfdf5 !important;
            border: 1px solid #d1fae5 !important;
            border-radius: 12px !important;
        }

        /* Clear chat bubbles */
        .msg.bot .bubble {
            background: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            color: #0f172a !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02) !important;
        }

        .msg.user .bubble {
            background: #10b981 !important;
            color: #ffffff !important;
            border: none !important;
            box-shadow: 0 2px 5px rgba(16, 185, 129, 0.2) !important;
        }
        
        .act {
            background: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
        }
        .act .t { color: #064e3b !important; font-weight: 700 !important; }
        .act .d { color: #64748b !important; }

        .timeline-content, .timeline-controls {
            background: #f8fafc !important;
            border: 1px solid #e2e8f0 !important;
        }
        
        .hero {
            background: transparent !important;
            position: relative;
        }
        .hero::before {
            content: '';
            position: absolute; inset: 0;
            background: linear-gradient(to bottom, rgba(236, 253, 245, 0.9), #f8fafc) !important;
            z-index: 0;
        }
        
        .hero-title {
            color: #022c22 !important;
            text-shadow: none !important;
        }
        .hero p { color: #475569 !important; }
        
        .env-card {
            background: #f8fafc !important;
            border: 1px solid #e2e8f0 !important;
        }
        
        .empty {
            background: #ffffff !important;
            border: 2px dashed #cbd5e1 !important;
        }
        
        .table-wrap {
            border: 1px solid #e2e8f0 !important;
            overflow: hidden !important;
        }
        .table-wrap th {
            background: #f8fafc !important;
            color: #064e3b !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
            border-bottom: 2px solid #e2e8f0 !important;
            padding: 16px !important;
        }
        
        .table-wrap td {
            color: #334155 !important;
            border-bottom: 1px solid #f1f5f9 !important;
            padding: 16px !important;
        }

        .table-wrap tr:hover td {
            background: #f8fafc !important;
        }
        
        .chip, .scan-tag {
            background: #f1f5f9 !important;
            border: 1px solid #e2e8f0 !important;
            color: #475569 !important;
            font-weight: 600 !important;
        }
        .chip:hover {
            background: #e2e8f0 !important;
            color: #0f172a !important;
        }
        
        /* Land selection toggle readability */
        .type-opt {
            background: #ffffff !important;
            border: 2px solid #e2e8f0 !important;
            color: #334155 !important;
        }
        .type-opt:hover {
            border-color: #cbd5e1 !important;
            background: #f8fafc !important;
        }
        .type-opt.on {
            background: #ecfdf5 !important;
            border-color: #10b981 !important;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1) !important;
        }
        .type-opt.on .t { color: #059669 !important; }
        .type-opt .t { color: #334155 !important; font-weight: 700 !important; }
        .type-opt .d { color: #64748b !important; }
        
        .stat-val { color: #022c22 !important; font-weight: 800 !important; }
        .weather-temp { color: #022c22 !important; font-weight: 800 !important; }
        .info-label { color: #64748b !important; font-weight: 600 !important; }
        .info-val { color: #0f172a !important; font-weight: 600 !important; }
"""

for file in files:
    path = os.path.join(templates_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clear previous overrides
    if '/* ==================================================' in content:
        content = content.split('/* ==================================================')[0] + '</style>' + content.split('</style>')[1]

    # Inject premium styles
    content = content.replace('</style>', premium_readable_css + '\n    </style>')

    # Ensure font link is pure
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
    if 'fonts.googleapis.com/css2?family=Inter' in content:
        content = content.replace(
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">',
            font_link
        )
        content = content.replace(
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
            font_link
        )

    # For login, change specific image
    if file == 'login.html':
        content = content.replace(
            "url('https://images.unsplash.com/photo-1590682680695-43b964a3ae17?q=80&w=2600&auto=format&fit=crop')",
            "url('https://images.unsplash.com/photo-1595822533038-f9448e9c6de2?q=80&w=2600&auto=format&fit=crop')" # Indian farmer field
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied Ultimate Readability + Enterprise Aesthetics.")
