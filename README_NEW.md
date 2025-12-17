# 🏥 מערכת אבחון רפואי מתקדמת / Advanced Medical Diagnostic System

מערכת מקצועית לניתוח תסמינים רפואיים באמצעות בינה מלאכותית, בנויה על CrewAI עם ארכיטקטורת Backend-Frontend מפוצלת.

Professional AI-powered medical symptom analysis system built with CrewAI, featuring separated Backend-Frontend architecture.

---

## 📋 תוכן עניינים / Table of Contents

- [תכונות](#-תכונות--features)
- [ארכיטקטורה](#-ארכיטקטורה--architecture)
- [התקנה](#-התקנה--installation)
- [שימוש](#-שימוש--usage)
- [מבנה הפרויקט](#-מבנה-הפרויקט--project-structure)
- [תצורה](#-תצורה--configuration)

---

## ✨ תכונות / Features

### 🤖 3 סוכני AI מומחים / 3 Expert AI Agents

1. **רכז קבלת חולים** / **Medical Intake Coordinator**
   - ראיון מקיף של המטופל
   - שימוש במסגרת OPQRST
   - זיהוי סימני אזהרה

2. **רופא מאבחן בכיר** / **Senior Diagnostic Physician**
   - ניתוח רב-תחומי
   - אבחנה דיפרנציאלית מבוססת ראיות
   - הערכת סיכון והמלצות

3. **מומחה תקשורת עם מטופלים** / **Patient Communication Specialist**
   - תרגום מונחים רפואיים לשפה פשוטה
   - הנחיות ברורות ומעשיות
   - רמת קריאה כיתה ח'

### 🎨 ממשק משתמש דו-לשוני / Bilingual User Interface
- תמיכה בעברית ואנגלית
- עיצוב רספונסיבי
- חווית משתמש אינטואיטיבית

### 🔧 ארכיטקטורה מודולרית / Modular Architecture
- Backend מבוסס FastAPI
- Frontend עם HTML/CSS/JS
- כל ה-prompts בקבצים חיצוניים
- קל לתחזוקה ועדכון

---

## 🏗 ארכיטקטורה / Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (UI Layer)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐        │
│  │  index.html │  │  styles.css │  │    app.js    │        │
│  └─────────────┘  └─────────────┘  └──────────────┘        │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/REST API
┌────────────────────────▼────────────────────────────────────┐
│                    Backend (API Layer)                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              FastAPI (api.py)                        │   │
│  │  • REST Endpoints                                    │   │
│  │  • Request/Response validation                       │   │
│  │  • CORS handling                                     │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                    │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │         Medical Service (medical_service.py)         │   │
│  │  • Business logic                                    │   │
│  │  • Error handling                                    │   │
│  │  • Logging                                           │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                    │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │         Crew Factory (crew_factory.py)               │   │
│  │  • Agent creation                                    │   │
│  │  • Task configuration                                │   │
│  │  • Crew orchestration                                │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                    │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │       Prompt Loader (prompt_loader.py)               │   │
│  │  • Load agent roles from JSON                        │   │
│  │  • Load task descriptions from JSON                  │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                    │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │           Configuration Files (JSON)                 │   │
│  │  • agent_roles.json                                  │   │
│  │  • task_descriptions.json                            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 💾 התקנה / Installation

### דרישות מקדימות / Prerequisites
- Python 3.10+
- pip
- מפתח API של OpenAI / OpenAI API key

### שלבי ההתקנה / Installation Steps

```bash
# 1. צור סביבה וירטואלית / Create virtual environment
python -m venv venv

# 2. הפעל את הסביבה / Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. התקן תלויות / Install dependencies
pip install -r requirements.txt

# 4. העתק והגדר .env / Copy and configure .env
copy .env.example .env
# ערוך את .env והוסף את ה-API key שלך
# Edit .env and add your OpenAI API key
```

### הגדרת קובץ .env / .env Configuration

ערוך את הקובץ `.env` והוסף:
Edit `.env` file and add:

```env
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL_NAME=gpt-4o
```

---

## 🚀 שימוש / Usage

### הפעלת Backend

```bash
# מהתיקייה הראשית / From root directory
python backend/api.py
```

השרת יעלה על: `http://localhost:8000`

תיעוד API: `http://localhost:8000/docs`

### הפעלת Frontend

פתח את הקובץ הבא בדפדפן:
Open this file in browser:

```
frontend/templates/index.html
```

או השתמש בשרת HTTP פשוט:
Or use a simple HTTP server:

```bash
# Python 3
cd frontend/templates
python -m http.server 8080

# לאחר מכן פתח / Then open:
# http://localhost:8080
```

### שימוש ב-API ישירות / Direct API Usage

```python
import requests

response = requests.post(
    'http://localhost:8000/api/analyze',
    json={
        'patient_input': '''
        I'm a 35-year-old male. For the past week I've had
        severe headaches, fatigue, and occasional dizziness...
        '''
    }
)

result = response.json()
print(result['result'])
```

---

## 📁 מבנה הפרויקט / Project Structure

```
new_crew_doctor_project/
│
├── backend/                        # Backend (שרת)
│   ├── __init__.py
│   ├── api.py                     # FastAPI REST API
│   │
│   ├── app/                       # אפליקציה
│   │   ├── __init__.py
│   │   ├── crew_factory.py       # יצירת Crew וסוכנים
│   │   ├── medical_service.py    # לוגיקה עסקית
│   │   └── prompt_loader.py      # טעינת prompts
│   │
│   ├── config/                    # תצורה
│   │   ├── __init__.py
│   │   └── settings.py           # הגדרות מערכת
│   │
│   ├── prompts/                   # Prompts חיצוניים
│   │   ├── __init__.py
│   │   ├── agent_roles.json      # תפקידי סוכנים
│   │   └── task_descriptions.json # תיאורי משימות
│   │
│   └── logs/                      # קבצי לוג
│
├── frontend/                       # Frontend (ממשק משתמש)
│   ├── templates/
│   │   └── index.html            # עמוד ראשי
│   │
│   └── static/
│       ├── styles.css            # עיצוב
│       └── app.js                # JavaScript
│
├── crew.py                        # גרסה מקורית (legacy)
├── example_usage.py               # דוגמה ישנה (legacy)
│
├── requirements.txt               # תלויות Python
├── .env.example                  # דוגמת תצורה
├── .env                          # תצורה אישית (אל תשתף!)
│
└── README_NEW.md                 # התיעוד הזה
```

---

## ⚙️ תצורה / Configuration

### קבצי Prompts / Prompt Files

כל ה-prompts נמצאים בקבצים חיצוניים ב-`backend/prompts/`:

#### `agent_roles.json`
מגדיר את תפקיד, מטרה ורקע של כל סוכן:
Defines role, goal, and backstory for each agent:

```json
{
  "intake_coordinator": {
    "role": "Chief Triage Officer...",
    "goal": "Conduct comprehensive...",
    "backstory": "You are a seasoned..."
  }
}
```

#### `task_descriptions.json`
מגדיר תיאור ופלט צפוי לכל משימה:
Defines description and expected output for each task:

```json
{
  "interview_task": {
    "description": "Conduct a comprehensive...",
    "expected_output": "A structured medical..."
  }
}
```

### עריכת Prompts / Editing Prompts

1. ערוך את הקבצים ב-`backend/prompts/`
2. השינויים ייטענו אוטומטית בהפעלה הבאה
3. אין צורך לשנות קוד Python

Edit files in `backend/prompts/` - changes load automatically on next run.

### הגדרות מערכת / System Settings

ב-`backend/config/settings.py`:

```python
CREW_MAX_RPM = 10              # בקשות מקסימליות לדקה
CREW_VERBOSE = True            # הדפסת לוגים מפורטת
CREW_MEMORY_ENABLED = True     # הפעלת זיכרון
```

---

## 🔌 API Endpoints

### `GET /`
מידע על ה-API / API information

### `GET /health`
בדיקת תקינות / Health check

### `POST /api/analyze`
ניתוח תסמינים / Symptom analysis

**Request Body:**
```json
{
  "patient_input": "I'm a 45-year-old male..."
}
```

**Response:**
```json
{
  "success": true,
  "result": "MEDICAL SYMPTOM ANALYSIS...",
  "metadata": {
    "start_time": "2025-01-15T10:30:00",
    "duration_seconds": 45.2
  }
}
```

---

## 📊 Logging

לוגים נשמרים ב-`backend/logs/medical_service.log`

Logs are saved to `backend/logs/medical_service.log`

```python
# דוגמה לצפייה בלוגים / Example viewing logs
tail -f backend/logs/medical_service.log
```

---

## 🛠 פתרון בעיות / Troubleshooting

### שגיאת חיבור ל-API / API Connection Error

```
Cannot connect to API server
```

**פתרון / Solution:**
1. ודא ש-Backend רץ: `python backend/api.py`
2. בדוק URL נכון: `http://localhost:8000`

### שגיאת API Key

```
OPENAI_API_KEY not found
```

**פתרון / Solution:**
1. בדוק שקיים קובץ `.env`
2. ודא שה-API key תקין
3. הפעל מחדש את Backend

### שגיאת Import

```
Import "crewai" could not be resolved
```

**פתרון / Solution:**
```bash
pip install -r requirements.txt
```

---

## 🔐 אבטחה / Security

- **אל תשתף את קובץ `.env`** / Never share `.env` file
- **אל תעלה API keys ל-Git** / Don't commit API keys
- בסביבת ייצור, הגדר CORS מדויק / In production, configure specific CORS origins

---

## 📝 הצהרה חשובה / Important Disclaimer

⚠️ **למטרות חינוכיות בלבד** / **For Educational Purposes Only**

מערכת זו אינה מהווה תחליף לבדיקה רפואית מקצועית. תמיד היוועץ ברופא מוסמך.

This system does not replace professional medical care. Always consult a licensed physician.

---

## 🤝 תרומה / Contributing

רעיונות לשיפור:
Suggestions for improvement:

- תמיכה בשפות נוספות / Additional language support
- שילוב עם מסדי נתונים רפואיים / Medical database integration
- שמירת היסטוריית מטופלים / Patient history tracking
- ייצוא ל-PDF / PDF export

---

## 📄 רישיון / License

פרויקט חינוכי לדוגמה. התייעץ עם אנשי מקצוע רפואיים ומשפטיים לפני שימוש קליני.

Educational demonstration project. Consult medical and legal professionals before clinical use.

---

## 📞 תמיכה / Support

- תיעוד CrewAI: https://docs.crewai.com
- תיעוד FastAPI: https://fastapi.tiangolo.com
- בעיות OpenAI API: https://platform.openai.com

---

**גרסה / Version:** 1.0.0
**עדכון אחרון / Last Updated:** 2025-12-16

---

🏥 **בריאות טובה! / Good Health!** 🏥
