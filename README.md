# qa-portfolio-makeupstore
My QA portfolio project: test documentation (test cases, bug reports, test plan) and UI automation tests (Selenium + Pytest) for makeupstore.com

# QA Portfolio – Makeupstore (UI Automation)

UI automation tests and test documentation for **https://makeupstore.com**  
Author: **Alla Karpenko (QA Engineer)**

---

## 📌 What’s inside
- https://docs.google.com/document/d/1XBMubhTKOQErkaQTxlqaLAjt4qzVh5em-dwG7BVDO68/edit?usp=sharing


- **Automation Tests (Selenium + Pytest):**
  - Login (positive & negative)
  - Search (positive & no results)
  - Add to Cart
  - Checkout (validation + smoke)

---

## 📂 Project structure
qa-portfolio-makeupstore/
├── README.md
├── requirements.txt
├── conftest.py
├── utils/
│ └── waits.py
├── pages/
│ ├── base_page.py
│ ├── home_page.py
│ ├── login_page.py
│ ├── search_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ └── checkout_page.py
└── tests/
├── test_login.py
├── test_search.py
└── test_cart_checkout.py

---


---

## ⚙️ Setup (how to run locally)
```bash
# 1. Clone repo
git clone https://github.com/karpenkoalla1504-blip/qa-portfolio-makeupstore.git
cd qa-portfolio-makeupstore

# 2. Create venv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

## ▶️ Run tests
pytest -q

## 🔧 Config
Base URL (default: https://makeupstore.com)
Set via env var:

export BASE_URL="https://makeupstore.com"


Credentials (for positive login test)

export TEST_LOGIN_EMAIL="karpenkoalla15.04+test@gmail.com"
export TEST_LOGIN_PASSWORD="TestTest123"

