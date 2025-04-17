import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="📄", layout="wide")


st.title("👋 Hi, I'm Maheen Imran")
st.subheader("A Passionate Web Developer and AI Enthusiast")

st.write("""
I am a web developer with a love for learning new technologies. I specialize in creating modern web apps using Python, Next.js, and Javascript.
""")

st.header("🧠 Skills")
cols = st.columns(3)
skills = ["Python", "JavaScript", "Next.js", "Streamlit", "HTML/CSS", "Tailwind"]

for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"✅ {skill}")


st.header("💻 Projects")
project_1, project_2 = st.columns(2)

with project_1:
    st.subheader("🌐 Portfolio Website")
    st.write("A personal website built with Streamlit.")
    st.markdown("[View Project](https://github.com/)")



st.header("📬 Contact")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you! Your message has been sent.")

