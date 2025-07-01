import streamlit as st
import docx
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="ResumePro+",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

def extract_text_from_file(file):
    """Extract text from uploaded file (TXT, DOCX, or PDF)"""
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    else:
        st.error("Unsupported file type!")
        return ""

def generate_wordcloud(text):
    """Generate word cloud from text"""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def analyze_resume(text, job_ref=None):
    keywords = ['python', 'project', 'experience', 'education', 'skills']
    score = sum(1 for k in keywords if k in text.lower()) * 20  # max 100
    suggestions = []
    for k in keywords:
        if k not in text.lower():
            suggestions.append(f"Consider adding '{k}' to your resume.")
    if job_ref:
        job_keywords = job_ref.lower().split()
        missing = [k for k in job_keywords if k not in text.lower()]
        if missing:
            suggestions.append(f"Missing job keywords: {', '.join(missing[:5])}")
    return score, suggestions

st.markdown("""
<div style='text-align:center;'>
    <h1 style='color:#4F8BF9; margin-bottom:0;'>📄 ResumePro+</h1>
    <p style='color:#555; font-size:1.1em;'>Get instant feedback and suggestions to improve your resume!</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🎯 Job Description Matching")
    job_ref = st.text_area("Paste Job Description (Optional)", height=120, placeholder="Paste the job description here for better keyword matching...")
    
    st.markdown("---")
    st.markdown("### 📊 Analysis Options")
    
    # Make checkboxes functional
    generate_wordcloud_option = st.checkbox("🌀 Generate Word Cloud", value=True)
    extract_keywords = st.checkbox("🔑 Extract AI Keywords", value=True)
    detailed_analysis = st.checkbox("📋 Detailed Section Analysis", value=True)
    
    st.markdown("---")
    st.markdown("### 📁 Supported Formats")
    st.info("✅ TXT, DOCX, PDF files supported")

st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2em; border-radius: 15px; margin-bottom: 2em; color: white; text-align: center;'>
    <h2 style='margin: 0; color: white;'>🚀 How to Use</h2>
    <div style='display: flex; justify-content: space-around; margin-top: 1em;'>
        <div style='flex: 1; margin: 0 1em;'>
            <div style='font-size: 2em; margin-bottom: 0.5em;'>1️⃣</div>
            <strong>Upload Resume</strong><br>
            <small>TXT, DOCX, or PDF format</small>
        </div>
        <div style='flex: 1; margin: 0 1em;'>
            <div style='font-size: 2em; margin-bottom: 0.5em;'>2️⃣</div>
            <strong>Add Job Description</strong><br>
            <small>Optional but recommended</small>
        </div>
        <div style='flex: 1; margin: 0 1em;'>
            <div style='font-size: 2em; margin-bottom: 0.5em;'>3️⃣</div>
            <strong>Get Analysis</strong><br>
            <small>Instant feedback & suggestions</small>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

resume_file = st.file_uploader("📄 Upload Your Resume", type=["txt", "docx", "pdf"], help="Supported formats: TXT, DOCX, PDF")

if resume_file:
    text = extract_text_from_file(resume_file)
    
    if text:
        # Create columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("## 📋 Resume Overview")
            
            # Stats in a nice format
            stats_col1, stats_col2, stats_col3 = st.columns(3)
            
            with stats_col1:
                st.metric("Word Count", len(text.split()))
            with stats_col2:
                st.metric("Character Count", len(text))
            with stats_col3:
                st.metric("File Type", resume_file.type.split('/')[-1].upper())
            
            # Show text preview
            with st.expander("📖 Text Preview", expanded=False):
                st.text_area("Resume Content", text[:1000] + "..." if len(text) > 1000 else text, height=200, disabled=True)
        
        with col2:
            # Score card
            score, suggestions = analyze_resume(text, job_ref)
            st.markdown("""
            <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                        border-radius: 20px; padding: 2em; text-align: center; 
                        box-shadow: 0 8px 32px rgba(0,0,0,0.1);'>
                <div style='font-size: 3em; font-weight: bold; color: white; margin-bottom: 0.2em;'>
                    {score}/100
                </div>
                <div style='color: white; font-size: 1.1em; opacity: 0.9;'>
                    Overall Score
                </div>
                <div style='color: white; font-size: 0.9em; opacity: 0.8; margin-top: 0.5em;'>
                    AI-Powered Evaluation
                </div>
            </div>
            """.format(score=score), unsafe_allow_html=True)
        
        # Analysis sections
        st.markdown("---")
        
        # Suggestions
        st.markdown("## 💡 Personalized Suggestions")
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                st.markdown(f"""
                <div style='background: #f8f9ff; border-left: 4px solid #4facfe; 
                            padding: 1em; margin: 0.5em 0; border-radius: 0 8px 8px 0;'>
                    <strong>{i}.</strong> {suggestion}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("🎉 Excellent! All essential sections present and relevant skills found!")
        
        # Optional analysis features
        if generate_wordcloud_option:
            st.markdown("## 🌀 Word Cloud")
            if len(text.split()) > 10:
                fig = generate_wordcloud(text)
                st.pyplot(fig)
                plt.close(fig)
            else:
                st.warning("Text too short to generate meaningful word cloud")
        
        if extract_keywords:
            st.markdown("## 🔑 Key Skills Detected")
            keywords = ['python', 'javascript', 'java', 'sql', 'machine learning', 'data science', 
                        'project management', 'leadership', 'communication', 'teamwork']
            found_keywords = [k for k in keywords if k in text.lower()]
            
            if found_keywords:
                cols = st.columns(min(len(found_keywords), 4))
                for i, keyword in enumerate(found_keywords):
                    with cols[i % 4]:
                        st.markdown(f"""
                        <div style='background: #e8f5e8; border: 1px solid #4caf50; 
                                    border-radius: 20px; padding: 0.5em; text-align: center; margin: 0.2em;'>
                            <span style='color: #2e7d32; font-weight: bold;'>{keyword.title()}</span>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("No common keywords detected. Consider adding relevant skills.")
        
        if detailed_analysis:
            st.markdown("## 📊 Detailed Section Analysis")
            
            sections = {
                'Contact Information': ['email', 'phone', 'address', 'linkedin'],
                'Education': ['education', 'degree', 'university', 'college', 'school'],
                'Experience': ['experience', 'work', 'job', 'employed', 'position'],
                'Skills': ['skills', 'proficient', 'knowledge', 'familiar'],
                'Projects': ['project', 'developed', 'built', 'created', 'implemented']
            }
            
            analysis_cols = st.columns(len(sections))
            
            for i, (section, keywords) in enumerate(sections.items()):
                found = any(keyword in text.lower() for keyword in keywords)
                with analysis_cols[i]:
                    if found:
                        st.markdown(f"""
                        <div style='background: #e8f5e8; border: 2px solid #4caf50; 
                                    border-radius: 10px; padding: 1em; text-align: center;'>
                            <div style='color: #2e7d32; font-weight: bold;'>✅ {section}</div>
                            <div style='color: #4caf50; font-size: 0.8em;'>Present</div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style='background: #ffebee; border: 2px solid #f44336; 
                                    border-radius: 10px; padding: 1em; text-align: center;'>
                            <div style='color: #c62828; font-weight: bold;'>❌ {section}</div>
                            <div style='color: #f44336; font-size: 0.8em;'>Missing</div>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        # Welcome message when no file is uploaded
        st.markdown("""
        <div style='text-align: center; padding: 3em; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                    border-radius: 15px; margin: 2em 0;'>
            <h2 style='color: #333;'>👋 Welcome to Resume Analyzer</h2>
            <p style='color: #666; font-size: 1.1em;'>Upload your resume to get started with AI-powered analysis!</p>
            <div style='margin-top: 2em;'>
                <span style='background: #4facfe; color: white; padding: 0.5em 1em; border-radius: 25px; margin: 0 0.5em;'>📄 TXT</span>
                <span style='background: #4facfe; color: white; padding: 0.5em 1em; border-radius: 25px; margin: 0 0.5em;'>📄 DOCX</span>
                <span style='background: #4facfe; color: white; padding: 0.5em 1em; border-radius: 25px; margin: 0 0.5em;'>📄 PDF</span>
            </div>
        </div>
        """, unsafe_allow_html=True)