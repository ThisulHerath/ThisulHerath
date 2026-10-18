"""Build the original, GitHub-safe SVG artwork for Thisul's profile.

Run: python scripts/build_profile.py
Only standard-library modules are required. No external fonts or SVG scripts.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "orbital"
OUT.mkdir(parents=True, exist_ok=True)
BG, PANEL, LINE = "#080f19", "#0e1a27", "#26394a"
WHITE, MUTED, MINT, LIME = "#edf5f2", "#9cb1bf", "#6ce5c0", "#d6f77b"


def text(x, y, value, size=16, color=WHITE, weight=400, mono=False, spacing=0):
    font = "'Courier New',monospace" if mono else "Arial,Helvetica,sans-serif"
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>'


def line(x1, y1, x2, y2, color=LINE, extra=""):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{color}" {extra}/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" {extra}/>'


def rect(x, y, w, h, fill=PANEL, rx=12, stroke=LINE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'


def save(name, height, title, description, body, width=1200):
    defs = '''<defs>
      <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#203347" stroke-opacity=".32"/></pattern>
      <radialGradient id="halo"><stop stop-color="#6ce5c0" stop-opacity=".16"/><stop offset="1" stop-color="#6ce5c0" stop-opacity="0"/></radialGradient>
      <linearGradient id="beam"><stop stop-color="#6ce5c0"/><stop offset="1" stop-color="#d6f77b"/></linearGradient>
    </defs>
    <style>
      .orbit{transform-origin:940px 242px;animation:orbit 48s linear infinite}
      .pulse{animation:pulse 4s ease-in-out infinite}
      .drift{animation:drift 6s ease-in-out infinite}
      @keyframes orbit{to{transform:rotate(360deg)}}
      @keyframes pulse{50%{opacity:.4}}
      @keyframes drift{50%{transform:translateY(-7px)}}
      @media(prefers-reduced-motion:reduce){.orbit,.pulse,.drift{animation:none}}
    </style>'''
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>{defs}{rect(1,1,width-2,height-2,BG,18)}{body}</svg>\n'
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")


def label(number, title, right, y=36):
    return text(32, y, f"{number} / {title}", 13, MINT, mono=True, spacing=2) + text(888, y, right, 11, MUTED, mono=True, spacing=1) + line(32, y+18, 1168, y+18)


def hero():
    b = '<rect x="700" y="2" width="498" height="476" rx="18" fill="url(#grid)"/>'
    b += '<circle cx="940" cy="242" r="245" fill="url(#halo)"/>'
    b += rect(32,30,38,38,LIME,8,LIME) + text(39,55,"th",20,BG,700)
    b += text(86,54,"ORBITAL / RESEARCH STATION",13,MINT,mono=True,spacing=2)
    b += text(34,115,"EXPLORER FILE  /  THISULHERATH",12,MUTED,mono=True,spacing=2)
    b += text(30,190,"THISUL",76,WHITE,700,spacing=-3)
    b += text(30,267,"HERATH",76,WHITE,700,spacing=-3)
    b += text(35,311,"Curiosity is the launch sequence.",24,LIME)
    b += text(35,347,"Data. Intelligence. Interfaces.",18,MUTED)
    b += line(35,381,656,381)
    for x, s in [(35,"AI / ML"),(180,"FULL STACK"),(370,"MOBILE")]:
        b += text(x,414,s,13,WHITE,mono=True,spacing=2)
    b += '<circle class="pulse" cx="40" cy="450" r="4" fill="#6ce5c0"/>'
    b += text(54,454,"SRI LANKA  /  UTC+05:30  /  ALWAYS EXPLORING",11,MUTED,mono=True,spacing=1)
    b += '<g fill="none" stroke="#395a67"><circle cx="940" cy="242" r="177" stroke-dasharray="3 9"/><ellipse cx="940" cy="242" rx="204" ry="79" transform="rotate(-35 940 242)"/><ellipse cx="940" cy="242" rx="204" ry="79" transform="rotate(35 940 242)"/><circle cx="940" cy="242" r="110"/></g>'
    b += '<g class="orbit"><circle cx="940" cy="65" r="7" fill="#d6f77b"/><circle cx="940" cy="419" r="4" fill="#6ce5c0"/><path d="M940 51V38M926 65H913M954 65H967" stroke="#d6f77b"/></g>'
    b += '<g class="drift">'+rect(876,178,128,128,PANEL,26,MINT)+text(897,257,"{ th }",32,LIME,700,mono=True)+'</g>'
    b += text(777,43,"DEEP SPACE / OPEN SOURCE",10,MUTED,mono=True,spacing=2)
    b += text(827,454,"IDEA → EXPERIMENT → BUILD",11,MINT,mono=True)
    save("00-arrival",480,"Thisul Herath — Orbital Research Station","An animated orbital emblem in mint and chartreuse. AI/ML, full-stack and mobile development. Based in Sri Lanka, UTC+05:30.",b)


def console():
    b = label("01","FLIGHT DECK","OPERATOR BRIEFING")
    b += text(36,102,"A curious mind. A builder's instinct.",31,WHITE,700)
    b += text(36,139,"IT undergraduate exploring the space between models and useful software.",17,MUTED)
    b += line(36,170,1164,170)
    rows = [("HOME BASE","Sri Lanka"),("TRAJECTORY","Machine learning · Full-stack · Mobile"),("CURRENT SIGNAL","Advanced NLP · AI/ML projects · React Native"),("COLLAB CHANNEL","AI/ML ideas & useful software")]
    for i,(k,v) in enumerate(rows):
        y = 209 + i*42
        b += text(36,y,k,12,MINT,mono=True,spacing=1)+text(235,y,v,17,WHITE)
    b += rect(848,192,314,148,"#132320",12,"#335147")
    b += text(868,221,"RESEARCH QUESTION",11,LIME,mono=True,spacing=1)
    for i,t in enumerate(["What happens after", "the experiment?", "Make it useful. Ship it."]):
        b += text(868,254+i*29,t,20,WHITE,700 if i==2 else 400)
    b += line(36,379,1164,379) + text(36,411,"FIRST JAVA. THEN PYTHON. NOW FOLLOWING THE NEXT GOOD QUESTION.",12,MUTED,mono=True,spacing=1)
    save("01-flight-deck",438,"Flight deck — About Thisul","IT undergraduate in Sri Lanka. Exploring advanced NLP, AI/ML and React Native. Open to collaboration.",b)


def projects():
    entries = [
        ("02a-churn","01","TELCO CUSTOMER CHURN","From customer data to a prediction service.","Data preparation · Feature engineering · Experiment tracking","Python / MLflow / FastAPI / Docker / GitHub Actions","MODEL → API", "churn"),
        ("02b-univault","02","UNIVAULT","A shared home for student knowledge.","Study notes · Resource reviews · Collections · Study groups","React Native / Expo / TypeScript / Node.js / MongoDB","KNOWLEDGE → COMMUNITY", "vault"),
        ("02c-sharebite","03","SHAREBITE LK","Good food deserves another destination.","Surplus listings · Local discovery · Reservations · Team project","React / Vite / Express / MongoDB / JWT","SURPLUS → OPPORTUNITY", "food")]
    for filename,n,title,tag,details,stack,mission,icon in entries:
        b = text(32,36,f"MISSION {n} / FIELD WORK",12,MINT,mono=True,spacing=2)+text(884,36,"EXPLORE REPOSITORY ↗",12,LIME,mono=True)
        b += line(32,54,1168,54)
        b += text(32,105,title,34,WHITE,700,spacing=-.5)+text(34,143,tag,21,LIME)
        b += text(34,181,details,16,MUTED)+text(34,226,stack,13,WHITE,mono=True)
        b += '<circle cx="1068" cy="149" r="65" fill="url(#halo)" stroke="#29443f"/>'
        if icon == "churn":
            b += '<g fill="none" stroke="#6ce5c0" stroke-width="3"><path d="M1028 180V115M1028 180H1107"/><path d="M1038 164L1055 146L1075 155L1098 124" stroke="#d6f77b"/><circle cx="1098" cy="124" r="5" fill="#d6f77b"/></g>'
        elif icon == "vault":
            b += '<g fill="none" stroke="#6ce5c0" stroke-width="2"><path d="M1029 124Q1052 117 1068 132Q1084 117 1107 124V174Q1084 167 1068 181Q1052 167 1029 174Z"/><path d="M1068 132V181M1038 138L1056 141M1080 141L1097 138M1038 150L1056 153M1080 153L1097 150"/></g>'
        else:
            b += '<g fill="none" stroke="#6ce5c0" stroke-width="2"><path d="M1026 151H1110Q1104 183 1068 183Q1032 183 1026 151ZM1044 190H1092"/><path d="M1068 147Q1064 112 1095 107Q1098 132 1068 147ZM1068 147L1084 121" stroke="#d6f77b"/></g>'
        save(filename,256,title,f"{tag} {details}. {stack}. Open the linked project repository for source and documentation.",b)
    b=label("02","MISSION ARCHIVE","SELECTED PROJECTS")+text(32,100,"Three problems. One instinct: make information useful.",24,WHITE,700)
    save("02-missions",130,"Mission archive — Featured projects","Customer churn prediction, shared student resources, and surplus food redistribution.",b)


def toolkit():
    b = label("03","EQUIPMENT BAY","TOOLS, NOT POWER LEVELS")
    rows=[("A","DATA & INTELLIGENCE","Python · R · SQL","scikit-learn · TensorFlow · PyTorch","Pandas · NumPy · Jupyter"),
          ("B","INTERFACES & APPS","JavaScript · TypeScript · Java","React · React Native · Node.js","Express · Spring Boot"),
          ("C","STORAGE & DELIVERY","MongoDB · PostgreSQL · MySQL","Supabase · Docker · GitHub Actions","Git · Postman · Ubuntu")]
    for i,(letter,title,a,c,d) in enumerate(rows):
        x=32+i*386
        b += rect(x,80,364,244)
        b += rect(x+20,100,34,34,LIME,6,LIME)+text(x+30,123,letter,18,BG,700,mono=True)
        b += text(x+20,174,title,15,MINT,700,mono=True)
        for j,t in enumerate([a,c,d]):b += text(x+20,215+j*31,t,15,WHITE if j==0 else MUTED)
    b += text(32,364,"ALSO IN THE KIT / C++ · HTML · CSS · Keras · OpenCV · Matplotlib",13,MUTED,mono=True)
    save("03-equipment",394,"Equipment bay — Technology toolkit","Data: Python, R, SQL, scikit-learn, TensorFlow, PyTorch. Apps: React, React Native, Node.js, Java and Spring Boot. Databases, Docker and GitHub Actions.",b)


def trajectory():
    b=label("04","FLIGHT PATH","KEEP FOLLOWING CURIOSITY")
    b += '<path d="M100 128H1100" stroke="#395a67" stroke-width="2" stroke-dasharray="5 8"/>'
    items=[(70,"01","THE SPARK","Java foundations.","A first line of code."),(360,"02","THE EXPERIMENT","Python, data & ML.","Questions become models."),(650,"03","THE BUILD","Web & mobile apps.","Ideas become interfaces."),(940,"04","THE NEXT ORBIT","NLP & intelligent apps.","Still exploring.")]
    for x,n,title,a,c in items:
        b += f'<circle cx="{x+30}" cy="128" r="23" fill="{BG}" stroke="{LIME if n=="04" else MINT}" stroke-width="2"/>'
        b += text(x+19,133,n,14,LIME if n=="04" else MINT,mono=True)
        b += text(x,192,title,17,WHITE,700)+text(x,223,a,15,MUTED)+text(x,248,c,14,MUTED)
    b += text(32,302,"NO FINAL LEVEL. JUST BETTER QUESTIONS AND MORE USEFUL BUILDS.",12,MINT,mono=True,spacing=1)
    save("04-flight-path",330,"Flight path — From Java to intelligent applications","Java foundations, Python and ML experiments, web and mobile builds, and an ongoing exploration of NLP.",b)


def footer():
    b=label("06","OPEN A CHANNEL","COLLABORATION WELCOME")
    b += text(32,112,"Have a curious problem?",39,WHITE,700)+text(32,155,"Let's build something useful.",30,LIME)
    b += text(34,201,"AI/ML ideas · Interesting datasets · Thoughtful software",17,MUTED)
    b += line(32,234,1168,234)+text(32,271,"THISUL HERATH / SRI LANKA",12,MINT,mono=True,spacing=2)+text(885,271,"END OF TRANSMISSION _",12,MUTED,mono=True)
    b += '<g fill="none" stroke="#395a67"><circle cx="1040" cy="144" r="52"/><ellipse cx="1040" cy="144" rx="89" ry="25" transform="rotate(-25 1040 144)"/></g><circle class="pulse" cx="1104" cy="115" r="6" fill="#d6f77b"/>'
    save("06-contact",299,"Open a channel — Let's connect","Have an AI/ML idea, an interesting dataset or a software project? Reach out to Thisul Herath.",b)
    for name,title,sub in [("portfolio","PORTFOLIO","VIEW WORK ↗"),("linkedin","LINKEDIN","CONNECT ↗"),("kaggle","KAGGLE","EXPLORE ↗"),("email","EMAIL","SAY HELLO ↗"),("instagram","INSTAGRAM","FOLLOW ↗")]:
        b=text(16,28,title,14,WHITE,700,mono=True,spacing=1)+text(16,51,sub,10,MINT,mono=True,spacing=1)
        save(f"link-{name}",68,title,sub,b,width=216)


if __name__ == "__main__":
    hero(); console(); projects(); toolkit(); trajectory(); footer()
    print(f"Built profile SVGs in {OUT}")
