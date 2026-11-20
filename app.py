"""
Bharath Ragavendhar G - Portfolio
Pure Python (Flask). Run locally:   python app.py
Export static site (optional):      python app.py build   -> creates docs/index.html
"""
from datetime import date
from pathlib import Path
import streamlit as st
from jinja2 import Template

# ----------------------------------------------------------------------------
# CONTENT  (edit only this section to update your portfolio)
# ----------------------------------------------------------------------------
PROFILE = {
    "first": "Bharath",
    "last": "Ragavendhar G",
    "role": "Computer Science graduate (IoT)",
    "summary": (
        "Computer Science graduate with a foundation in Python programming and "
        "front-end development, complemented by strong communication, teamwork "
        "and organizational skills. I keep learning and I want to contribute "
        "effectively to the teams I join."
    ),
    "email": "gbharathragavendhar@gmail.com",
    "phone": "+91 9042927771",
    "location": "Chennai, India",
}

FOCUS = [
    ("Python", "Programming, SQL and full stack web basics"),
    ("Front end", "Responsive web pages built under supervision"),
    ("IoT systems", "Automation, smart systems and Industry 4.0"),
]

EDUCATION = [
    {
        "title": "B.E. Computer Science and Engineering (IoT)",
        "place": "Sri Sairam Engineering College, Chennai",
        "years": "2022 – 2026",
        "note": "CGPA 6.91",
    },
    {
        "title": "SSLC and HSC",
        "place": "Little Jacky Mat. Hr. Sec. School, Chengalpattu",
        "years": "2020 – 2022",
        "note": "SSLC 62.4%  ·  HSC 67.5%",
    },
]

EXPERIENCE = [
    {
        "when": "Jun – Jul 2025",
        "role": "Web Development Intern",
        "org": "EPIC GROUPS, Chennai",
        "points": [
            "Gained practical experience in web development.",
            "Focused on creating responsive web solutions under professional supervision.",
        ],
    },
    {
        "when": "Jan 2025",
        "role": "Python Full Stack Web Development Intern",
        "org": "VEI Technologies Pvt Ltd, Chennai",
        "points": [
            "Completed an industrial internship on Python Full Stack development.",
            "Collaborated with experts to build and deploy web-based applications.",
        ],
    },
    {
        "when": "Feb 2024",
        "role": "IoT and Automation Workshop",
        "org": "MIT Campus, Anna University, Chennai",
        "points": [
            "Hands-on experience with automation machinery and smart system integration.",
            "Learned how IoT is integrated into industrial processes for better efficiency.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Quantum Cryptography Based Encryption System",
        "text": (
            "An encryption system built on Quantum Key Distribution (QKD), "
            "aimed at theoretically unhackable secure communication."
        ),
        "tags": ["QKD", "Encryption", "Python"],
    },
    {
        "name": "Greenhouse Management System using IoT",
        "text": (
            "An automated monitoring and control system for environmental "
            "conditions that helps optimize plant growth, using specialized "
            "IoT hardware and software."
        ),
        "tags": ["IoT", "Automation", "Sensors"],
    },
]

SKILLS = [
    ("Languages and tools", ["Python", "SQL", "MS Excel", "MS Word"]),
    ("AI tools", ["Microsoft Copilot", "Claude", "GitHub Copilot"]),
    ("Specializations", ["IoT Systems", "Front end web development", "Industry 4.0"]),
    ("Soft skills", ["Communication", "Team collaboration", "Problem solving", "Adaptability"]),
]

CERTS = [
    ("Microsoft Azure Fundamentals (AZ-900)", "Microsoft Azure"),
    ("Introduction to Industry 4.0 and Industrial IoT", "Swayam NPTEL"),
]

# ----------------------------------------------------------------------------
# DESIGN  (palette from your reference image - nothing else is used)
# ----------------------------------------------------------------------------
CSS = """
:root{
  --bordo:#6C151E; --green:#0F3D3A; --cream:#F5DABF;
  --bordo-a:rgba(108,21,30,.28); --cream-a:rgba(245,218,191,.30);
  --display:'Roboto Slab',Georgia,serif;
  --body:'DM Sans','Segoe UI',system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--body);background:var(--cream);color:var(--green);line-height:1.65;font-size:1.05rem}
a{color:inherit}
:focus-visible{outline:3px solid var(--bordo);outline-offset:3px}
.on-dark :focus-visible{outline-color:var(--cream)}
h1,h2,h3{font-family:var(--display);font-weight:700;line-height:.95;letter-spacing:.005em}
.wrap{max-width:1120px;margin:0 auto;padding:0 1.5rem}
section{padding:6rem 0}
h2{font-size:clamp(2.6rem,6vw,4.4rem);margin-bottom:2.5rem}

/* nav */
nav{position:sticky;top:0;z-index:5;background:var(--cream);border-bottom:1px solid var(--bordo-a)}
nav .wrap{display:flex;justify-content:space-between;align-items:center;padding-top:.9rem;padding-bottom:.9rem}
.logo{font-family:var(--display);font-weight:700;font-size:1.6rem;color:var(--bordo);text-decoration:none}
nav ul{display:flex;gap:1.6rem;list-style:none}
nav ul a{text-decoration:none;font-weight:500}
nav ul a:hover{color:var(--bordo);text-decoration:underline;text-underline-offset:5px}

/* hero */
.hero{padding:5rem 0 6rem}
.hero .wrap{display:grid;grid-template-columns:1.25fr 1fr;gap:3rem;align-items:center}
.hero h1{font-size:clamp(2.6rem,7vw,5.2rem);color:var(--bordo);margin-bottom:1.5rem;line-height:1.05}
.hero h1 span{display:block}
.role{font-size:1.25rem;font-weight:500;margin-bottom:.8rem}
.lead{max-width:34rem;margin-bottom:2rem}
.btns{display:flex;gap:1rem;flex-wrap:wrap}
.btn{display:inline-block;padding:.85rem 1.6rem;border-radius:14px;font-weight:700;text-decoration:none;border:2px solid var(--bordo);transition:transform .15s}
.btn:hover{transform:translateY(-2px)}
.btn.solid{background:var(--bordo);color:var(--cream)}
.btn.line{color:var(--bordo)}
.slabs{display:grid;gap:1rem}
.slab{border-radius:22px;padding:1.6rem 1.8rem;animation:slide .8s cubic-bezier(.2,.7,.2,1) both}
.slab h3{font-size:2.8rem;margin-bottom:.3rem}
.slab p{font-size:.98rem;opacity:.92}
.slab:nth-child(1){background:var(--bordo);color:var(--cream)}
.slab:nth-child(2){background:var(--green);color:var(--cream);animation-delay:.15s}
.slab:nth-child(3){background:var(--cream);color:var(--bordo);border:2px solid var(--bordo);animation-delay:.3s}
@keyframes slide{from{opacity:0;transform:translateX(60px)}to{opacity:1;transform:none}}
