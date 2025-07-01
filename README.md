# 📄 ResumePro+

> **AI-Powered Resume Analysis Tool** - Get instant feedback and suggestions to improve your resume with support for multiple file formats.

![ResumePro+](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 **[🚀 Try Live Demo](https://resumepro.streamlit.app/)**

## ✨ Features

- 📁 **Multi-Format Support**: TXT, DOCX, and PDF files
- 🎯 **Smart Scoring**: AI-powered resume scoring (0-100 scale)
- 🔍 **Keyword Matching**: Compare resume against job descriptions
- 🌀 **Word Cloud**: Visual representation of key terms
- 🏷️ **Skills Detection**: Automatically identify relevant skills
- 📊 **Section Analysis**: Check for essential resume components
- 🎨 **Modern UI**: Professional and responsive design

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit python-docx PyPDF2 wordcloud matplotlib
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   ```
   http://localhost:8501
   ```

## 🎯 How It Works

### 1. Upload Your Resume
Support for multiple formats:
- **📄 TXT** - Plain text files
- **📄 DOCX** - Microsoft Word documents  
- **📄 PDF** - Portable Document Format

### 2. Get Instant Analysis
- **Resume Score**: 0-100 based on keyword presence
- **Missing Elements**: Suggestions for improvement
- **Skills Detected**: Relevant technical and soft skills
- **Section Check**: Verify essential resume components

### 3. Job Matching (Optional)
- Paste job description for targeted feedback
- Get specific keyword suggestions
- Improve resume-job alignment

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Text Processing**: python-docx, PyPDF2
- **Visualization**: WordCloud, Matplotlib
- **Language**: Python 3.11+

## 📊 Analysis Features

### Keyword Scoring
Analyzes resume for essential keywords:
- `python`, `project`, `experience`, `education`, `skills`
- Each keyword found adds 20 points to the score

### Skills Detection
Identifies relevant skills including:
- Programming languages (Python, JavaScript, Java, SQL)
- Technologies (Machine Learning, Data Science)
- Soft skills (Leadership, Communication, Teamwork)

### Section Analysis
Checks for essential resume sections:
- ✅ Contact Information
- ✅ Education
- ✅ Experience  
- ✅ Skills
- ✅ Projects

## 🎨 User Interface

### Modern Design
- **Gradient Backgrounds**: Professional color schemes
- **Responsive Layout**: Adapts to different screen sizes
- **Interactive Elements**: Expandable sections and options
- **Visual Feedback**: Color-coded status indicators

### Layout Structure
- **Sidebar**: Job description input and analysis options
- **Main Area**: File upload and results display
- **Metrics**: Real-time statistics (word count, file type)
- **Score Card**: Prominent score display with gradient styling

### Analysis Options
Toggle features in the sidebar:
- 🌀 **Word Cloud Generation**
- 🔑 **AI Keywords Extraction**  
- 📋 **Detailed Section Analysis**

### Customization
Easily modify keywords and scoring logic in the code:
```python
keywords = ['python', 'project', 'experience', 'education', 'skills']
score = sum(1 for k in keywords if k in text.lower()) * 20
```

## 🌟 Acknowledgments

- **Streamlit** - For the amazing web framework
- **python-docx** - For Word document processing
- **PyPDF2** - For PDF text extraction
- **WordCloud** - For beautiful word visualizations

## 🔮 Roadmap

- [ ] **AI Integration**: Advanced NLP analysis
- [ ] **Resume Templates**: Built-in resume builder
- [ ] **Industry Analysis**: Field-specific feedback
- [ ] **Export Options**: PDF analysis reports
- [ ] **Batch Processing**: Multiple file analysis

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Yejarla Srinivas](https://github.com/yourusername)

</div>
