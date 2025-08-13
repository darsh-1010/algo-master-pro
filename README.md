# 🚀 AlgoMaster Pro

> **AI-Powered Data Structures & Algorithms Problem Solver**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange.svg)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive web application that helps you master Data Structures & Algorithms through AI-powered solutions, interactive problem solving, and modern web interface.

## ✨ Features

- **🧠 50+ DSA Problems** - Categorized by difficulty (Easy, Medium, Hard)
- **🤖 AI-Powered Solutions** - Powered by Groq LLM API for intelligent problem solving
- **💻 Multi-Language Support** - Solutions in Python, Java, and C++
- **🎨 Modern UI/UX** - Beautiful, responsive design with smooth animations
- **🔍 Smart Search & Filtering** - Find problems by name, category, or difficulty
- **📊 Problem Statistics** - Visual breakdown of problem distribution
- **📝 Detailed Explanations** - Step-by-step solutions with dry-run examples
- **⚡ Performance Analysis** - Time & space complexity for each solution

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python Flask 3.0+ |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **AI Integration** | Groq API (llama3-8b-8192) |
| **Styling** | Custom CSS with animations & glassmorphism |
| **Code Highlighting** | Prism.js |
| **Deployment** | Cross-platform startup scripts |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/algo-master-pro.git
   cd algo-master-pro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env_example.txt .env
   # Edit .env and add your GROQ_API_KEY
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

### Alternative Startup Methods

- **Windows**: Double-click `run.bat`
- **Linux/Mac**: Run `./run.sh`

## 🌟 Key Features

### Problem Categories
- **Arrays & Strings** - Manipulation, searching, sorting
- **Linked Lists** - Single, double, circular lists
- **Trees & Graphs** - Binary trees, BST, graph algorithms
- **Dynamic Programming** - Memoization, tabulation
- **Sorting & Searching** - Various algorithms and optimizations
- **Stack & Queue** - Data structure implementations
- **Hash Tables** - Collision resolution, applications

### AI-Powered Solutions
- **Optimal Algorithms** - Most efficient solutions for each problem
- **Step-by-step Explanations** - Easy to understand breakdowns
- **Dry-run Examples** - Visualize how the solution works
- **Complexity Analysis** - Time & space complexity breakdown
- **Alternative Approaches** - Multiple solution methods when applicable

## 🎨 UI Features

- **Responsive Design** - Works seamlessly on all devices
- **Smooth Animations** - Engaging user experience with CSS animations
- **Modern Glassmorphism** - Beautiful visual effects and depth
- **Interactive Elements** - Hover effects, transitions, and micro-interactions
- **Code Highlighting** - Syntax highlighting for Python, Java, and C++
- **Dark/Light Theme Ready** - Easy to customize color schemes

## 📁 Project Structure

```
algo-master-pro/
├── 📄 app.py                 # Flask backend & API endpoints
├── 📋 requirements.txt       # Python dependencies
├── 🎨 templates/
│   └── 📱 index.html        # Main HTML template
├── 🎭 static/
│   ├── 🎨 css/
│   │   └── 🖌️ style.css     # Styling, animations & themes
│   └── ⚡ js/
│       └── 🧠 script.js     # Frontend functionality & API calls
├── 🚀 run.py                # Python startup script
├── 🪟 run.bat               # Windows startup script
├── 🐧 run.sh                # Unix/Linux/Mac startup script
├── 🔑 env_example.txt       # Environment variables template
├── 📚 README.md             # This file
├── 📜 LICENSE               # MIT License
└── 🚫 .gitignore            # Git ignore rules
```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

### API Configuration
- **Groq Model**: `llama3-8b-8192`
- **Response Format**: Structured (EXPLANATION, CODE, COMPLEXITY, DRY_RUN, ALTERNATIVES)
- **Language Support**: Python, Java, C++

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/get_problem_categories` | GET | Get all DSA problems |
| `/solve_problem` | POST | Get AI solution for a problem |
| `/search_problems` | GET | Search problems by query |
| `/get_problems_by_difficulty` | GET | Filter by difficulty level |
| `/get_problems_by_category` | GET | Filter by problem category |

## 🎯 Use Cases

- **Students** - Learn DSA concepts with AI explanations
- **Developers** - Practice coding problems with optimal solutions
- **Interview Prep** - Prepare for technical interviews
- **Educators** - Use as a teaching tool for algorithms
- **Competitive Programming** - Quick reference for problem solving

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 for Python code
- Add comments for complex logic
- Test your changes before submitting
- Update documentation if needed

## 🐛 Bug Reports & Feature Requests

- **Bug Reports**: Use the [Issues](https://github.com/YOUR_USERNAME/algo-master-pro/issues) tab
- **Feature Requests**: Open an issue with the `enhancement` label
- **Questions**: Use the [Discussions](https://github.com/YOUR_USERNAME/algo-master-pro/discussions) tab

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 AlgoMaster Pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Groq API** for providing powerful LLM capabilities
- **Flask** for the robust web framework
- **Prism.js** for beautiful code syntax highlighting
- **Open Source Community** for inspiration and tools

## 📞 Support & Community

- **GitHub Issues**: [Report bugs](https://github.com/YOUR_USERNAME/algo-master-pro/issues)
- **Discussions**: [Join the conversation](https://github.com/YOUR_USERNAME/algo-master-pro/discussions)
- **Wiki**: [Documentation](https://github.com/YOUR_USERNAME/algo-master-pro/wiki)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/algo-master-pro&type=Date)](https://star-history.com/#YOUR_USERNAME/algo-master-pro&Date)

---

<div align="center">

**Made with ❤️ by the AlgoMaster Pro Team**

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/algo-master-pro?style=social)](https://github.com/YOUR_USERNAME/algo-master-pro)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/algo-master-pro?style=social)](https://github.com/YOUR_USERNAME/algo-master-pro)
[![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/algo-master-pro)](https://github.com/YOUR_USERNAME/algo-master-pro/issues)

**If this project helps you, please give it a ⭐ star!**

</div>
