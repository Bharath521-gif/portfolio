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
@media (max-width:560px){nav ul li:nth-child(n+4){display:none}}
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
