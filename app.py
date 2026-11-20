"""Bharath Ragavendhar G - Portfolio, converted from Flask to Streamlit."""
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
html{scroll-behavior:smooth;overflow-x:hidden}
body{width:100%;overflow-x:hidden;font-family:var(--body);background:var(--cream);color:var(--green);line-height:1.65;font-size:1.05rem}
a{color:inherit}
:focus-visible{outline:3px solid var(--bordo);outline-offset:3px}
.on-dark :focus-visible{outline-color:var(--cream)}
h1,h2,h3{font-family:var(--display);font-weight:700;line-height:.95;letter-spacing:.005em}
.wrap{width:100%;max-width:1120px;margin:0 auto;padding:0 1.5rem;min-width:0}
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

/* bands */
.green{background:var(--green);color:var(--cream)}
.bordo{background:var(--bordo);color:var(--cream)}
.green h2,.bordo h2{color:var(--cream)}
.cream h2{color:var(--bordo)}

/* about */
.about{display:grid;grid-template-columns:1fr 1fr;gap:3rem}
.about p{max-width:34rem}
.edu{display:grid;gap:1rem}
.edu article{border:2px solid var(--cream-a);border-radius:18px;padding:1.4rem 1.6rem}
.edu h3{font-size:1.7rem;margin-bottom:.3rem}
.edu small{display:block;opacity:.85;font-size:.95rem}
.edu strong{display:block;margin-top:.5rem}

/* experience timeline */
.timeline{list-style:none;border-left:3px solid var(--bordo);margin-left:.5rem}
.timeline > li{position:relative;padding:0 0 2.6rem 2rem;min-width:0}
.timeline > li:last-child{padding-bottom:0}
.timeline > li::before{content:"";position:absolute;left:-11px;top:.55rem;width:19px;height:19px;border-radius:50%;background:var(--cream);border:4px solid var(--bordo)}
.when{font-weight:700;color:var(--bordo)}
.timeline h3{font-size:2rem;margin:.2rem 0}
.org{font-weight:500;margin-bottom:.6rem}
.timeline > li > ul{padding-left:1.1rem;max-width:42rem;list-style:circle}
.timeline > li > ul > li{position:static;padding:0;margin:.25rem 0;overflow-wrap:anywhere}
.timeline > li > ul > li::before{content:none}

/* projects */
.projects{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
.project{background:var(--cream);color:var(--green);border-radius:24px;padding:2.2rem}
.project h3{font-size:2.3rem;color:var(--bordo);margin-bottom:1rem}
.project p{margin-bottom:1.3rem}
.tags{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none}
.tags li{border:2px solid var(--green);border-radius:999px;padding:.15rem .85rem;font-size:.9rem;font-weight:500}

/* skills */
.skills{display:grid;grid-template-columns:repeat(2,1fr);gap:2rem 3rem}
.skills h3{font-size:1.8rem;color:var(--bordo);margin-bottom:.7rem}
.skills .tags li{border-color:var(--bordo);color:var(--bordo)}
.certs{margin-top:3.5rem;border-top:2px solid var(--bordo-a);padding-top:2rem}
.certs h3{font-size:2.2rem;color:var(--bordo);margin-bottom:1rem}
.certs p{margin-bottom:.4rem}
.certs span{opacity:.85}

/* contact */
.contact{text-align:left}
.contact .big{display:inline-block;font-family:var(--display);font-weight:700;font-size:clamp(1.8rem,6.2vw,4.6rem);line-height:1.05;word-break:break-all;text-decoration:none;border-bottom:4px solid var(--cream)}
.contact .big:hover{color:var(--cream);border-bottom-color:transparent}
.contact p{margin:1.8rem 0 0}
footer{background:var(--green);color:var(--cream);padding:1.5rem 0;border-top:1px solid var(--cream-a);font-size:.95rem}

@media (max-width:820px){
  .hero .wrap,.about,.projects,.skills{grid-template-columns:1fr}
  nav ul{gap:1rem;font-size:.95rem}
  section{padding:4rem 0}
}
@media (max-width:560px){
  nav .wrap{align-items:flex-start;gap:.6rem;flex-direction:column}
  nav ul{flex-wrap:wrap;gap:.45rem .9rem}
  .wrap{padding-left:1rem;padding-right:1rem}
  section{padding:3rem 0}
  h2{font-size:clamp(2rem,9vw,3rem);line-height:1.08;overflow-wrap:anywhere;margin-bottom:1.6rem}
  .timeline{margin-left:.45rem}
  .timeline > li{padding-left:1.35rem;padding-bottom:2rem}
  .timeline h3{font-size:clamp(1.35rem,6vw,1.8rem);line-height:1.15;overflow-wrap:anywhere}
  .org,.when,.timeline p{overflow-wrap:anywhere}
  .contact .big{font-size:clamp(1.35rem,6vw,2.2rem);overflow-wrap:anywhere}
}
@media (prefers-reduced-motion:reduce){.slab{animation:none}.btn{transition:none}html{scroll-behavior:auto}}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ p.first }} {{ p.last }} | Portfolio</title>
<meta name="description" content="Portfolio of {{ p.first }} {{ p.last }}: Python, front-end web development and IoT.">
<meta name="theme-color" content="#6C151E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>{{ css|safe }}</style>
</head>
<body>

<nav aria-label="Main">
  <div class="wrap">
    <a class="logo" href="#top">Bharath Ragavendhar G</a>
    <ul>
      <li><a href="#about">About</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</nav>

<header class="hero" id="top">
  <div class="wrap">
    <div>
      <h1><span>{{ p.first }}</span><span>{{ p.last }}</span></h1>
      <p class="role">{{ p.role }}</p>
      <p class="lead">{{ p.summary }}</p>
      <div class="btns">
        <a class="btn solid" href="mailto:{{ p.email }}">Email me</a>
        <a class="btn line" href="#resume-download">Download resume</a>
      </div>
    </div>
    <div class="slabs">
      {% for title, text in focus %}
      <div class="slab"><h3>{{ title }}</h3><p>{{ text }}</p></div>
      {% endfor %}
    </div>
  </div>
</header>

<section class="green on-dark" id="about">
  <div class="wrap about">
    <div>
      <h2>About me</h2>
      <p>{{ p.summary }}</p>
      <p style="margin-top:1rem">Based in {{ p.location }}.</p>
    </div>
    <div class="edu">
      {% for e in education %}
      <article>
        <h3>{{ e.title }}</h3>
        <small>{{ e.place }}</small>
        <small>{{ e.years }}</small>
        <strong>{{ e.note }}</strong>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="cream" id="experience">
  <div class="wrap">
    <h2>Experience and training</h2>
    <ul class="timeline">
      {% for x in experience %}
      <li>
        <span class="when">{{ x.when }}</span>
        <h3>{{ x.role }}</h3>
        <p class="org">{{ x.org }}</p>
        <ul>{% for pt in x.points %}<li style="padding:0;border:0">{{ pt }}</li>{% endfor %}</ul>
      </li>
      {% endfor %}
    </ul>
  </div>
</section>

<section class="bordo on-dark" id="projects">
  <div class="wrap">
    <h2>Projects</h2>
    <div class="projects">
      {% for pr in projects %}
      <article class="project">
        <h3>{{ pr.name }}</h3>
        <p>{{ pr.text }}</p>
        <ul class="tags">{% for t in pr.tags %}<li>{{ t }}</li>{% endfor %}</ul>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="cream" id="skills">
  <div class="wrap">
    <h2>Skills</h2>
    <div class="skills">
      {% for group, items in skills %}
      <div>
        <h3>{{ group }}</h3>
        <ul class="tags">{% for i in items %}<li>{{ i }}</li>{% endfor %}</ul>
      </div>
      {% endfor %}
    </div>
    <div class="certs">
      <h3>Certifications</h3>
      {% for name, org in certs %}
      <p><strong>{{ name }}</strong> <span>by {{ org }}</span></p>
      {% endfor %}
    </div>
  </div>
</section>

<section class="green on-dark contact" id="contact">
  <div class="wrap">
    <h2>Let's work together</h2>
    <a class="big" href="mailto:{{ p.email }}">{{ p.email }}</a>
    <p>Call or message: <a href="tel:{{ p.phone|replace(' ','') }}">{{ p.phone }}</a></p>
  </div>
</section>

<footer class="on-dark">
  <div class="wrap">&copy; {{ year }} {{ p.first }} {{ p.last }}</div>
</footer>

</body>
</html>
"""



def render_portfolio():
    """Render the original HTML/CSS portfolio inside Streamlit."""
    template = Template(PAGE)
    rendered_page = template.render(
        css=CSS,
        p=PROFILE,
        focus=FOCUS,
        education=EDUCATION,
        experience=EXPERIENCE,
        projects=PROJECTS,
        skills=SKILLS,
        certs=CERTS,
        year=date.today().year,
    )
    return rendered_page


def get_resume_bytes():
    """Load the existing resume PDF, if the project contains one."""
    # Preferred: an existing resume.pdf beside this app.py.
    pdf_path = Path(__file__).with_name("resume.pdf")
    if pdf_path.exists():
        return pdf_path.read_bytes()

    # Backward compatibility with the original Flask project's resume_data.py.
    try:
        from resume_data import RESUME_BYTES
        return RESUME_BYTES
    except Exception:
        return None


if __name__ == "__main__":
    st.set_page_config(
        page_title="Bharath Ragavendhar G | Portfolio",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Hide Streamlit's default chrome so the original portfolio design leads.
    st.markdown(
        """
        <style>
          #MainMenu, footer, header {visibility: hidden;}
          .stApp {background: #F5DABF;}
          .block-container {
            max-width: 100%;
            padding: 0 !important;
            margin: 0 !important;
          }
          div[data-testid="stDownloadButton"] {
            padding: 0.75rem 1.5rem 0.25rem 1.5rem;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )

    resume_bytes = get_resume_bytes()
    st.markdown("<div id='resume-download'></div>", unsafe_allow_html=True)
    if resume_bytes:
        st.download_button(
            label="Download resume PDF",
            data=resume_bytes,
            file_name="Bharath_Ragavendhar_Resume.pdf",
            mime="application/pdf",
            key="resume_download",
        )
    else:
        st.warning(
            "Resume PDF is not included yet. Upload your resume as **resume.pdf** "
            "to the same GitHub folder as app.py, then redeploy. The download "
            "button will appear automatically."
        )

    portfolio_html = render_portfolio()
    st.components.v1.html(
        portfolio_html,
        height=3600,
        scrolling=True,
    )
