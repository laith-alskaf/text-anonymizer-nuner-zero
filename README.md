# 🛡️ Text Anonymizer using NuNER Zero-shot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-REST%20API-orange)
![Colab](https://img.shields.io/badge/Run%20on-Colab-brightgreen)

تطبيق لإخفاء الهوية في المستندات النصية تلقائيًا باستخدام تقنيات الذكاء الاصطناعي. يكتشف التطبيق الأسماء (PERSON)، والمنظمات (ORG)، والمواقع (GPE) ويستبدلها إما ببيانات وهمية أو برموز مثل `[REDACTED]`.

تم بناء هذا المشروع كجزء من مهمة أكاديمية لمعالجة المستندات وإخفاء الهوية باستخدام نموذج **Zero-shot NER** (NuNER).

---

## 🎯 الميزات

-   ✅ دعم تحميل ملفات `.txt` و `.docx`.
-   ✅ دعم اختياري لملفات `.pdf` (استخراج نص فقط).
-   ✅ استخدام نموذج **NuNER Zero-shot** للتعرف على الكيانات دون الحاجة لتدريب مسبق.
-   ✅ استبدال الكيانات الحساسة ببيانات وهمية (باستخدام `Faker`) أو برموز مخصصة.
-   ✅ إعادة بناء المستندات المخفية بنفس التنسيق الأصلي (لملفات `.txt` و `.docx`).
-   ✅ واجهة مستخدم تفاعلية في Google Colab.
-   ✅ واجهة برمجة تطبيقات (REST API) للاستخدام الآلي.
-   ✅ دعم نمط استبدال مخصص (مثل `*****` أو `[REDACTED]`).

---

## 🚀 كيفية الاستخدام (في Google Colab)

نظرًا لأن المشروع يستخدم نموذجًا كبيرًا للذكاء الاصطناعي، فإن أسهل طريقة لتشغيله هي عبر **Google Colab**.

1.  **افتح المشروع في Colab:**
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/text-anonymizer-nuner-zero/blob/main/app.ipynb)
    *(سيتم إضافة الرابط بعد رفع الكود على GitHub)*

2.  **شغّل الخلايا بالترتيب:** ابدأ بخلية تثبيت المكتبات وانتهي بتشغيل التطبيق أو الـ API.

3.  **لواجهة المستخدم:**
    *   شغّل خلية `app.py`.
    *   ارفع ملفك.
    *   اختر أنواع الكيانات (`PERSON, ORG, GPE`).
    *   اختر نمط الاستبدال.
    *   احصل على الملف المخفي!

4.  **لـ REST API:**
    *   شغّل خلية `api.py`.
    *   احصل على رابط عام من `ngrok`.
    *   أرسل طلبات POST إلى `/anonymize` مع الملف والإعدادات.

---

## 🧩 هيكل المشروع
text-anonymizer-nuner-zero/
│
├── app.py # واجهة المستخدم التفاعلية (Colab)
├── api.py # خادم REST API (مع ngrok)
├── core.py # النواة الأساسية (نموذج NuNER, Faker)
├── file_handlers.py # معالجة الملفات (.txt, .docx, .pdf)
├── utils.py # دوال مساعدة (مثل دمج الكيانات)
└── requirements.txt # قائمة المكتبات المطلوبة


---

## 📦 المتطلبات

-   Python 3.8+
-   المكتبات المذكورة في `requirements.txt`:
    -   `gliner` (لنموذج NuNER Zero-shot)
    -   `python-docx`, `pdfplumber`
    -   `Faker`
    -   `Flask`, `pyngrok`

---

## 📄 التقرير (Report)

تم إرفاق تقرير منفصل يشرح بالتفصيل:
-   اختيار النموذج (NuNER Zero-shot) وأسبابه.
-   هندسة النظام (من تحميل الملف إلى إخراج الناتج).
-   التحديات التي واجهتنا (مثل دقة النموذج، الحفاظ على تنسيق .docx) وكيف تم حلها.
-   أمثلة قبل وبعد إخفاء الهوية.

*(سيتم رفع ملف `REPORT.pdf` في المستودع)*

---

## 🤝 المساهمة

هذا مشروع أكاديمي، ولكن أي اقتراحات أو تحسينات مرحب بها!

1.  عمل فورك (Fork) للمستودع.
2.  إنشاء فرع (Branch) جديد للخاصية التي تريد إضافتها (`git checkout -b feature/YourFeature`).
3.  عمل commit للتغييرات (`git commit -m 'Add some feature'`).
4.  دفع الفرع (`git push origin feature/YourFeature`).
5.  فتح طلب سحب (Pull Request).

---

## 📜 الترخيص

هذا المشروع مفتوح المصدر بموجب ترخيص MIT. للتفاصيل، انظر ملف [LICENSE](LICENSE).

---

## 📞 للاتصال

لأي استفسار:
-   [laithalksaf@gmail.com](mailto:laithalksaf@gmail.com)

---

**تم التطوير باستخدام ❤️ في Google Colab**