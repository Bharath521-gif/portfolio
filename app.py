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
