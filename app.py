import requests
import streamlit  as st
from streamlit_lottie import st_lottie

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
def load_html(file_name):
    with open(file_name,encoding="utf-8") as f:
        return f.read()
def load_image(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    


codding_me_animation = load_image("https://lottie.host/cc929793-9240-4910-9e5d-42460053b6db/X6ExtgIEsO.json")
start_coding = load_image('https://lottie.host/6b0aabaa-b100-4346-ae8e-a07dae9f1f06/0JMwlFkKeR.json')
st.set_page_config(page_title="Coffe Code Courses",layout="wide")
local_css("style/style.css")


with st.container():
    left_columnm, rigth_column = st.columns(2)

    with left_columnm:
        st_lottie(start_coding,height=500, key='start_coding')
        
    with rigth_column:
        st.write(load_html('templates/index_start_coding.html'), unsafe_allow_html=True)

st.write('---')

with st.container():
    left_columnm, rigth_column = st.columns(2)

    with left_columnm:
        st.write(load_html('templates/index_about_me.html'), unsafe_allow_html=True)

    with rigth_column:
        st_lottie(codding_me_animation,height=500, key='coding')

st.write('---')

with st.container():
    st.markdown(load_html('templates/index_course_row.html'), unsafe_allow_html=True)

st.write('---')

with st.container():
    left_columnm, rigth_column = st.columns(2)
    with left_columnm:
        st.write(load_html('templates/index_footer.html'), unsafe_allow_html=True)
    
    with rigth_column:
        st.write(load_html('templates/index_news_letter.html'), unsafe_allow_html=True)
