import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from PIL import Image
from streamlit_option_menu import option_menu
import sqlite3
from pathlib import Path

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,post TEXT ,postdate DATE)')

def add_data(author,title,post,postdate):
    c.execute('INSERT INTO blogtable(author,title,post,postdate) VALUES (?,?,?,?)', (author, title, post, postdate))
    conn.commit()

def view_all_notes():
    c.execute("SELECT * FROM blogtable")
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data

title_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
<h6> Author:{} </h6>
<br/>
<br/> 
<p style="text-align:justify">{}</p>
</div>
"""

#Change the background color

head_message_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6> 
</div>
"""

full_message_temp ="""
<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
<p style="text-align:justify;color:black;padding:10px">{}</p>
</div>
"""

st.set_page_config(page_title = "Professional Portfolio",page_icon = ":tada:",layout = "wide")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("/Volumes/ExDrive/Images/Hello.png")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_rbtawnwz.json")
lottie_welcome = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_c1hkermx.json")
lottie_computer = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_TKxfYaMROq.json")

selected = option_menu(
        menu_title = None,
        options = ["Introduction","Home","About", "Resume","Contact", "Blog"],
        icons = ["info-circle","house","book","clipboard","envelope", "people-fill"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal",
    )

if selected == "Introduction":
    st.subheader("Welcome to my Professional Portfolio! :wave:")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html = True)
    st.markdown('<p class = "big-font">Select a tab on the navigation menu to get started!</p>', unsafe_allow_html = True)
    st_lottie(lottie_computer,height = 300, key = "computer")

if selected == "Home":
    st.subheader("Hi, I am Anush! :wave:") 
    st.write("I am currently a sophomore at the University of Illinois at Urbana-Champaign and I am majoring in Aerospace Engineering." )
    st_lottie(lottie_welcome,height = 300, key = "welcome")


if selected == "About":
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("Anush Rajan is currently an undergraduate student at the University of Illinois at Urbana-Champaign majoring in Aerospace Engineering. "
            "He is involved in undergraduate research and is part of the Spaceshot team of the Illinois Space Society"
            ",which is a Registered Student Organization (RSO) that aims to launch a rocket past the Karman Line"
            ",which is the boundary between the Earth's atmosphere and space."
            "As part of this project, he has developed a combination of project management skills, communication skills, and technical skills.")

            st.write("Outside of being a student, Anush enjoys reading, coding in Python, taking walks, and watching movies."
            "He hopes to get a valuable internship at a company that will allow him to gain important work experience that he can utilize in a full-time career."
            "In addition to technical organizations, he is also involved in community service organizations such as Asha for Education.")
        with right_column:
            st_lottie(lottie_hello,height = 300, key = "hello")

if selected == "Resume":
    #GENERAL SETTINGS
    NAME = "Anush Rajan"
    DESCRIPTION = """
    Sophomore, Majoring in Aerospace Engineering, Minoring in Atmospheric Sciences
    """
    EMAIL = "Email: anush2@illinois.edu"
    SOCIAL_MEDIA = "LinkedIn: https://www.linkedin.com/in/anush-rajan-859546221/"

    col1, col2 = st.columns(2, gap = "small")   

    with col1:
        img = Image.open("/Volumes/ExDrive/Images/pic.jpeg")
        st.image(img, width = 230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write(EMAIL)
        st.write(SOCIAL_MEDIA)

    #WORK EXPERIENCE
    st.write("#")
    st.subheader("Work Experience")
    st.write("---")

    #JOB 1
    st.markdown("**Center for Hypersonics and Entry Systems Studies**")
    st.write("August 2022 - Present")
    st.write("•	Designed a calorimeter sensor for integration in the largest inductively coupled plasma wind tunnel in the US, the Plasmatron X.", "text-align: center")
    st.write("•	Manufactured a calorimeter sensor to provide accurate and consistent heat flux measurements in the Plasmatron X")
    st.write("•	Produced an academic paper explaining the methods, results, impacts, and conclusions of the project")

    #JOB 2
    st.write("#")
    st.markdown("**The Seeded and Natural Orographic Wintertime Clouds: The Idaho Experiment (SNOWIE)**")
    st.write("August 2022 - Present")
    st.write("•	Performed an analysis of flight leg data from flights done by the University of Wyoming King Air Research Aircraft")
    st.write("•	Determine and plotted the concentration of each flight leg using Python")
    st.write("•	Evaluated the impact of orographic cloud seeding in the Idaho Mountains")

    st.write("#")
    st.subheader("Project Highlights")
    st.write("---")

    #PROJECT 1
    st.markdown("**Illinois Space Society**")
    st.write("August 2022 - Present")
    st.write("•	Designed and constructed a recovery and ejection system with a team for the rocket, Intrepid III")
    st.write("•	Worked with a team to manufacture the payload system for Intrepid III")

    #PROJECT 2
    st.markdown("**Illinois Space Society**")
    st.write("August 2021 - December 2021")
    st.write("•	Developed detailed procedures with a team to manufacture, cast, and dispose of solid propellant")
    st.write("•	Designed and constructed a recovery and ejection system with a team for the rocket Intrepid")

    #PROJECT 3
    st.markdown("**Intro to Aerospace Engineering**")
    st.write("August 2021 - December 2021")
    st.write("•	Designed a model rocket from scratch with the goal of reaching an apogee of 1000 ft.")
    st.write("•	Designed the rocket body using Siemens NX and simulated the aerodynamic properties using OpenRocket Software")

    st.write("#")
    st.subheader("Extracurricular Activities and Leadership")
    st.write("---")
    st.markdown("**Illinois Space Society, Level 1 High Power Rocketry Certification Program Manager**")
    st.write("August 2022 - Present")
    st.write("•	Collected funds, performed a cost analysis, and organized 60 rocket launches for students wanting an L1 certification")
    st.markdown("**Illinois Space Society, Mentorship Program Manager**")
    st.write("August 2022 - Present")
    st.write("•	Created pairings and organized events / meetings for mentor – mentee pairs within the Illinois Space Society")


if selected == "Contact":
    with st.container():
        st.write("----")
        st.header("Contact Me! :speech_balloon:")
        st.write("##")
        st.write("Please use the form below to reach out to me regarding any or my professional work history or to learn more about any project samples.")
        #st.write('Streamlit is really **cool**.')

        contact_form = """
        <form action="https://formsubmit.co/anush2@illinois.edu" method="POST">
            <input type = "hidden" name = "_captcha" value="false">
            <input type="text" name="name" placeholder = "Your Name" required>
            <input type="email" name="email" placeholder = "Your Email" required>
            <input type = "message" name = "message" placeholder = "Your Message" required>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html = True)
        with right_column:
            st.empty()

if selected == "Blog":
    with st.container():
        st.title("Welcome to the blog space!")
        choice = option_menu(
            menu_title = None,
            options = ["View Posts","Add Posts"],
            icons = ["info-circle","house"],
            menu_icon = "cast",
            default_index = 0,
            orientation = "horizontal",
    )

    result = view_all_notes()

    for i in result:
        b_author = i[0]
        b_title = i[1]
        b_post = i[2]
        b_post_date = i[3]

    if choice == "View Posts":
        st.subheader("View Posts")
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.sidebar.selectbox("View Posts", all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            b_author = i[0]
            b_title = i[1]
            b_post = i[2]
            b_post_date = i[3]
            st.markdown(head_message_temp.format(b_title, b_author, b_post, b_post_date), unsafe_allow_html = True)

    if choice == "Add Posts":
        st.subheader("Add Posts")
        create_table()
        blog_author = st.text_input("Author Name")
        blog_title = st.text_input("Post Title")
        blog_post = st.text_area("Post Content")
        blog_post_date = st.date_input("Date")
        if st.button("Add"):
            add_data(blog_author, blog_title, blog_post, blog_post_date)
            st.success("Post: {} saved". format(blog_title))

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html = True)

