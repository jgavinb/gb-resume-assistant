import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Gavin Brumfield, M.S. Candidate in Analytics
##### *Resume* 
''')

st.sidebar.success("Select a page above.")

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Inquisitive mind, fueled by a passion for uncovering patterns and making
data-driven decisions. Leverages a diagnostic mindset and analytical rigor to navigate complex challenges,
delivering actionable insights that enhance outcomes and drive strategic initiatives.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://linkedin.com/in/gavinbrumfield" target="_blank">Gavin Brumfield</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#practicum">Practicum</a>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science Candidate** (Analytics), *Institute for Advanced Analytics*, North Carolina State University',
'June 2024-Present')
#st.markdown('''
#- Eventually Add Summary or Projects Here
#'')

txt('**Bachelors of Science** (Business Administration), *North Carolina State University*, Raleigh, NC',
'2019-2023')
#st.markdown('''
#- Eventually Add Summary Here
#''')

#####################
st.markdown('''
## Practicum
''')

txt('**Data Scientist, Communication Lead**, Artemis Health',
'Sep 2024-Present')
st.markdown('''
- Performing data engineering on a billion-row dataset in PostgreSQL, employing SQL optimizations, indexing, and partitioning for faster queries and efficient data handling.
- Developing an ensemble of anomaly detection and unsupervised learning algorithms to identify, categorize, and score data quality issues within third-party vendor datasets.
- Creating comprehensive data quality dashboards in Python, providing real-time, actionable interventions based on root-cause analysis to assist the client's data operations team in improving data quality.
- Collaborating with stakeholders to define the scope of work including key quality indicators, aligning the project with broader data governance objectives and existing company infrastructure.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Application Security Intern**, Syneos Health, Morrisville, NC',
'Dec 2022-Jan 2024')
st.markdown('''
- Enhanced CI/CD pipeline efficiency by integrating code-scanning tools and providing guidance to development leads on tool implementation to proactively identify and mitigate security vulnerabilities early in the development process.
- Improved decision-making and security practices by communicating code scan results to stakeholders and development teams, facilitating timely, data-driven actions to address critical findings and reduce potential risks.
- Strengthened legal and privacy standards by implementing a 'Shift left' approach within the Software Development Lifecycle, ensuring compliance with national and international regulations and minimizing compliance-related risks across projects.
''')

txt('**Solution Architect Intern**, Syneos Health, Morrisville, NC',
'May 2022-Dec 2022')
st.markdown('''
- Increased data accuracy and visibility of project progress by developing and managing PowerBI dashboards with automated data pipelines, providing the Enterprise Architecture team and upper management with real-time metrics on data transfer from the existing Change Management Database to LeanIX.
- Enhanced productivity and efficiency of the Architecture Review Board by creating key performance indicator dashboards with automated data pipelines, enabling Syneos Health to track performance and effectively identify areas for process improvement.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SQL`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`, `R Shiny`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/gavinbrumfield')
txt2('GitHub', 'https://github.com/jgavinb/')