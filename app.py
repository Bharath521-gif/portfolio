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
    if resume_bytes:
        st.download_button(
            label="Download resume PDF",
            data=resume_bytes,
            file_name="Bharath_Ragavendhar_Resume.pdf",
            mime="application/pdf",
            key="resume_download",
        )
    else:
        st.caption(
            "To enable the resume download, add resume.pdf to the same GitHub "
            "folder as app.py (or include your existing resume_data.py)."
        )

    portfolio_html = render_portfolio()
    st.components.v1.html(
        portfolio_html,
        height=3600,
        scrolling=True,
    )
