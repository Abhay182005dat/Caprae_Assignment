# 🔍 Smart B2B Lead Finder

A lightweight and interactive **Streamlit app** that helps filter and explore web development companies based on their **location** and **hourly rate**. Ideal for startups, agencies, and investors looking for vetted tech partners scraped from Clutch.

---

## 📌 Features

- ✅ Upload your own CSV file of scraped company data  
- 🌍 Search and filter companies by **location** with autocomplete  
- 💸 Filter leads by **hourly rate range**  
- 🔗 Clickable links to company websites  
- 🎯 Clean, minimal UI with styled results  

---

## 📁 Sample CSV Format

Ensure your CSV file has the following columns:


Example:

| Company Name | Website              | Hourly Rate    | Location               |
|--------------|----------------------|----------------|------------------------|
| OAKS LAB     | https://oakslab.com  | $50 - $99 / hr | Prague, Czech Republic |
| INOXOFT      | https://inoxoft.com  | $25 - $49 / hr | Newark, DE             |

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.8+
- `streamlit`
- `pandas`

### 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smart-lead-finder.git
cd smart-lead-finder
```

### Run 
```
streamlit run app.py
