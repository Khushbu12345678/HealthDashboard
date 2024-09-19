import streamlit as st

def main():
    # Set page title and background color
    st.set_page_config(page_title="Global Mental Health Analysis Dashboard", page_icon=":brain:", layout="wide", initial_sidebar_state="collapsed")
    
    # Custom CSS for styling the page
    st.markdown(
        """
        <style>
            .main {
                background-image: url('https://img.freepik.com/free-photo/pastel-brush-paint-textured-background_53876-96676.jpg');
                background-size: cover;
                background-position: center;
                padding: 20px;
            }
            .title {
                color: #ffffff;
                font-family: 'Arial', sans-serif;
                text-align: left;
                font-size: 45px;
                margin-bottom: 30px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            .intro-text {
                font-size: 22px;
                color: white;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            .disorder-title {
                font-size: 30px;
                font-weight: bold;
                color: white;
                margin-bottom: 20px;
            }
            .disorder-description {
                font-size: 20px;
                color: #f2f2f2;
                margin-bottom: 30px;
                line-height: 1.5;
            }
            .element-container img {
                display: block;
                margin: 20px auto;
                max-width: 600px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # Display background image container
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Display title and introductory text
    c1, c2 = st.columns([1, 9])
    with c1:
        st.image("https://img.icons8.com/color/100/mental-health.png", width=100)

    with c2:
        st.markdown("<h1 class='title'>Global Mental Health Analysis Dashboard</h1>", unsafe_allow_html=True)
    
    st.markdown("<p class='intro-text'>Welcome to the Global Mental Health Analysis Dashboard. This dashboard provides insights and analysis of mental health data from around the world.</p>", unsafe_allow_html=True)

    # Display section for various mental health disorders
    st.markdown("<div class='disorder-section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='disorder-title'>Common Mental Health Disorders</h2>", unsafe_allow_html=True)

    # List of disorders
    disorders = [
        {
            "name": "Anxiety Disorders",
            "description": "Anxiety disorders are a group of mental disorders characterized by significant feelings of anxiety and fear. Common types include generalized anxiety disorder (GAD), panic disorder, and social anxiety disorder.",
            "image_path": "https://your-image-path.com/anxiety-disorder.png"
        },
        {
            "name": "Depression",
            "description": "Depression is a mood disorder that causes persistent feelings of sadness, hopelessness, and loss of interest. It can affect how you feel, think, and handle daily activities.",
            "image_path": "https://your-image-path.com/depression.jpg"
        },
        {
            "name": "Bipolar Disorder",
            "description": "Bipolar disorder, formerly known as manic-depressive illness, is a brain disorder that causes unusual shifts in mood, energy, activity levels, and the ability to carry out day-to-day tasks.",
            "image_path": "https://your-image-path.com/bipolar-disorder.jpg"
        },
        {
            "name": "Schizophrenia",
            "description": "Schizophrenia is a severe mental disorder characterized by profound disruptions in thinking, affecting language, perception, and sense of self. People with schizophrenia often experience hallucinations and delusions.",
            "image_path": "https://your-image-path.com/schizophrenia.jpg"
        },
        {
            "name": "Eating Disorder",
            "description": "Eating disorders are serious mental health conditions characterized by unhealthy behaviors surrounding food and weight. Common types include anorexia nervosa, bulimia nervosa, and binge eating disorder.",
            "image_path": "https://your-image-path.com/eating-disorder.jpg"
        }
    ]

    for disorder in disorders:
        st.markdown(f"<h3 class='disorder-title'>{disorder['name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='disorder-description'>{disorder['description']}</p>", unsafe_allow_html=True)
        st.image(disorder["image_path"], caption=disorder["name"], use_column_width=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if _name_ == "_main_":
    main()