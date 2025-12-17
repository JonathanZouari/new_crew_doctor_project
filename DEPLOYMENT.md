# 🚀 Railway Deployment Guide

מדריך פריסת פרויקט Medical Diagnostic Assistant ב-Railway

## 📋 דרישות מוקדמות

1. חשבון Railway (הירשם בחינם ב-https://railway.app)
2. Git מותקן במחשב
3. מפתח API של OpenAI

## 🔧 הכנת הפרויקט

הפרויקט כבר מכיל את כל הקבצים הדרושים ל-deployment:

### קבצים שנוצרו אוטומטית:

- ✅ `main.py` - נקודת הכניסה הראשית לאפליקציה (נדרש ל-Railway)
- ✅ `Procfile` - מגדיר איך להריץ את האפליקציה
- ✅ `railway.toml` - קונפיגורציה של Railway
- ✅ `runtime.txt` - גרסת Python
- ✅ `requirements.txt` - תלויות Python (עודכן עם gunicorn)
- ✅ `.railwayignore` - קבצים להתעלם מהם בפריסה
- ✅ `.gitignore` - מונע העלאה של `.env` ל-Git

## 📦 שלבי הפריסה ב-Railway

### שלב 1: יצירת Repository ב-GitHub

אם עדיין לא יצרת repository:

```bash
# Initialize git (אם עדיין לא נעשה)
git init

# הוסף את כל הקבצים
git add .

# צור commit
git commit -m "Ready for Railway deployment"

# צור repository חדש ב-GitHub ואז:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### שלב 2: יצירת פרויקט חדש ב-Railway

1. היכנס ל-https://railway.app
2. לחץ על "New Project"
3. בחר "Deploy from GitHub repo"
4. אשר את הגישה ל-GitHub
5. בחר את ה-repository שלך

### שלב 3: הגדרת משתני סביבה (Environment Variables)

ב-Railway Dashboard:

1. לחץ על הפרויקט שנוצר
2. עבור לטאב "Variables"
3. הוסף את המשתנים הבאים:

```
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

**חשוב מאוד:** ללא מפתח API של OpenAI, האפליקציה לא תעבוד!

### שלב 4: Deploy

Railway יתחיל להריץ את ה-deployment אוטומטית:

1. הוא יזהה את `railway.toml` או `Procfile`
2. יתקין את כל התלויות מ-`requirements.txt`
3. יריץ את הפקודה: `uvicorn backend.api:app --host 0.0.0.0 --port $PORT`

### שלב 5: קבלת ה-URL

1. לאחר שה-deployment מסתיים בהצלחה
2. Railway יספק לך URL ציבורי
3. ה-URL יהיה בפורמט: `https://your-project-name.up.railway.app`

## 🔍 בדיקת הפריסה

לאחר ה-deployment, בדוק:

### 1. Health Check
```
https://your-project-name.up.railway.app/health
```

אמור להחזיר:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-17T...",
  "version": "1.0.0"
}
```

### 2. API Documentation
```
https://your-project-name.up.railway.app/docs
```

תראה ממשק Swagger UI אינטראקטיבי

### 3. Root Endpoint
```
https://your-project-name.up.railway.app/
```

יציג מידע על ה-API

## 🧪 בדיקת ניתוח תסמינים

דרך ה-Swagger UI ב-`/docs`:

1. פתח את endpoint `/api/analyze`
2. לחץ "Try it out"
3. הזן תסמינים לדוגמה:

```json
{
  "patient_input": "I'm a 34-year-old female experiencing severe fatigue for the past week. I feel exhausted even after sleeping well."
}
```

4. לחץ "Execute"

## 📊 ניטור ו-Logs

ב-Railway Dashboard:

1. **Logs**: לחץ על "View Logs" כדי לראות את כל ה-output של האפליקציה
2. **Metrics**: ראה שימוש ב-CPU, זיכרון ורשת
3. **Deployments**: היסטוריה של כל ה-deployments

## 🔧 פתרון בעיות נפוצות

### בעיה: "Application failed to respond"

**פתרון:**
1. בדוק ש-OPENAI_API_KEY מוגדר נכון
2. בדוק את ה-Logs לשגיאות
3. ודא ש-port binding נכון (Railway מספק $PORT אוטומטית)

### בעיה: "Module not found"

**פתרון:**
1. ודא שכל התלויות ב-`requirements.txt`
2. בדוק שאין שגיאות טייפוס בשמות המודולים
3. נסה rebuild מחדש

### בעיה: "OpenAI API Error"

**פתרון:**
1. ודא שמפתח ה-API תקף
2. בדוק שיש מספיק קרדיט בחשבון OpenAI
3. ודא שהמפתח לא הוגבל לכתובות IP ספציפיות

### בעיה: Health check נכשל

**פתרון:**
1. בדוק את `railway.toml` - ה-path אמור להיות `/health`
2. ודא שה-endpoint /health עובד מקומית
3. העלה את `healthcheckTimeout` ל-300 שניות (כבר מוגדר)

## 🔄 עדכון הפרויקט

כשאתה עושה שינויים:

```bash
git add .
git commit -m "Your update message"
git push
```

Railway יזהה אוטומטית את ה-push וירוץ deployment חדש.

## 🌐 חיבור Frontend

אם יש לך frontend נפרד:

1. עדכן את כתובות ה-CORS ב-`backend/api.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # עדכן כאן
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

2. ב-frontend שלך, עדכן את ה-API URL:
```javascript
const API_URL = "https://your-project-name.up.railway.app";
```

## 💰 תמחור

Railway מציע:
- **$5 חינם לחודש** (עם כרטיס אשראי)
- לאחר מכן, תשלום לפי שימוש
- האפליקציה הזו צריכה להיות מכוסה ב-tier החינמי למרבית המקרים

## 📱 Custom Domain (אופציונלי)

להוספת domain משלך:

1. ב-Railway Dashboard -> Settings -> Domains
2. לחץ "Add Domain"
3. הזן את ה-domain שלך
4. עדכן את ה-DNS records כמו שמוצג

## 🔒 אבטחה

**חשוב!**

1. **לעולם אל תעלה** את קובץ `.env` ל-GitHub
2. השתמש ב-Environment Variables של Railway
3. הגבל CORS לדומיינים ספציפיים בפרודקשן
4. שקול הוספת rate limiting
5. שקול הוספת authentication אם צריך

## 📞 תמיכה

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- OpenAI Support: https://help.openai.com

## ✅ Checklist לפני Go-Live

- [ ] משתני הסביבה מוגדרים
- [ ] Health check עובד
- [ ] API endpoint `/api/analyze` עובד
- [ ] CORS מוגדר נכון
- [ ] Logs נראים תקינים
- [ ] בדיקת ביצועים עם תסמינים שונים
- [ ] תיעוד עדכני למשתמשים
- [ ] Monitoring פעיל

---

**הצלחה ב-deployment!** 🎉

אם יש בעיות, בדוק את ה-Logs ב-Railway או פתח issue ב-GitHub.
