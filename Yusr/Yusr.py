"""
تصميم واجهات المستخدم (UI) لمنصة "يسر" الحكومية السودانية
----------------------------------------------------------
هذا الملف يصف بشكل مفصل هيكل صفحات المنصة، العناصر المرئية، التفاعلات، وربط الصفحات.
يمكن استخدام هذا التصميم كمرجع لفريق التطوير (Frontend/Backend) وأيضاً لفريق التصميم (UI/UX).

1. صفحة الهبوط / تسجيل الدخول / التسجيل (Landing/Login/Signup)
-----------------------------------------------------------------
العناصر المرئية:
- شعار السودان واسم المنصة "يسر" (أعلى الصفحة - منتصف أو يسار)
- رسالة ترحيبية مختصرة: "بوابتك الموحدة للخدمات الحكومية في السودان"
- صندوق تسجيل الدخول:
    - حقل اسم المستخدم/رقم الهوية
    - حقل كلمة المرور
    - زر "تسجيل الدخول"
    - رابط "نسيت كلمة المرور؟"
    - رابط "استعادة الحساب"
- زر/رابط "إنشاء حساب جديد" (واضح أسفل صندوق الدخول)
- صور/أيقونات تمثل الخدمات الحكومية (اختياري)
- اختيار اللغة (عربي/إنجليزي) في الزاوية

التفاعلات:
- تسجيل الدخول يدعم SSO + كلمة سر + OTP (مستقبلاً: بصمة)
- الضغط على "إنشاء حساب جديد" ينقل لصفحة التسجيل
- روابط المساعدة تفتح صفحات/نوافذ فرعية

2. الصفحة الرئيسية (Home/Dashboard)
------------------------------------
العناصر المرئية:
- رأس الصفحة (Header):
    - شعار السودان واسم المنصة (يسار)
    - شريط بحث عالمي للخدمات (منتصف/يمين)
    - أيقونة ملف المستخدم (يمين)
    - أيقونات اللغة (عربي/إنجليزي)
- لوحة تحكم شخصية:
    - بيانات المستخدم (اسم، رقم هوية، الحالة)
    - ملخص الطلبات (قيد المعالجة، منتهية، مرفوضة) وروابط التفاصيل
    - تنبيهات وإشعارات فورية
    - روابط سريعة للخدمات المستخدمة مؤخراً
- قسم الخدمات السريعة/الأكثر استخداماً:
    - أيقونات/بطاقات كبيرة (الهوية، الجوازات، الضرائب، المرور...)
- قسم الأخبار والإعلانات الحكومية
- قسم الخدمات المصنفة:
    - بطاقات/قائمة حسب القطاعات (الداخلية، الصحة، التعليم...)

التفاعلات:
- جميع الأقسام تفاعلية وقابلة للنقر
- البحث يقترح خدمات فورية

3. صفحة تفاصيل الخدمة (Service Detail)
---------------------------------------
العناصر المرئية:
- عنوان الخدمة (مثال: "تجديد جواز السفر")
- وصف الخدمة (موجز وواضح)
- قائمة المستندات المطلوبة (PDF, JPG, PNG)
- خطوات التنفيذ (مرقمة أو نقطية)
- زر "تقديم الطلب"
- قسم الأسئلة الشائعة (اختياري)
- تقدير زمني لإنجاز الخدمة (اختياري)

التفاعلات:
- زر "تقديم الطلب" ينقل لنموذج التقديم
- روابط للأسئلة الشائعة ذات الصلة

4. صفحة تقديم الطلب (Service Application Form)
-----------------------------------------------
العناصر المرئية:
- نموذج إلكتروني تفاعلي (حقول واضحة مع تسميات)
- قسم رفع المستندات (سحب وإفلات/اختيار ملفات)
- مؤشر تقدم (Progress Indicator) إذا كان النموذج متعدد الخطوات
- صفحة مراجعة قبل الإرسال النهائي
- زر "إرسال الطلب" أو "الدفع والتقديم"

التفاعلات:
- التحقق الثنائي (OTP/بصمة) قبل الإرسال النهائي
- بوابة دفع إلكتروني متكاملة إذا كانت الخدمة برسوم

5. صفحة متابعة الطلبات (Track Applications)
--------------------------------------------
العناصر المرئية:
- قائمة الطلبات المقدمة (جدول/بطاقات):
    - اسم الخدمة، رقم الطلب، تاريخ التقديم، الحالة، آخر تحديث
- تفاصيل الطلب عند النقر:
    - ملخص البيانات والمستندات
    - سجل التحديثات
    - رسالة توضيحية لسبب الرفض (إن وجدت)
    - زر "تواصل بخصوص هذا الطلب"

التفاعلات:
- النقر على أي طلب يعرض التفاصيل الكاملة
- زر التواصل يفتح نموذج اتصال مع الجهة المعنية

6. قسم المساعدة / الدعم الفني (Help/Support)
---------------------------------------------
العناصر المرئية:
- الأسئلة الشائعة (FAQ) مصنفة حسب الموضوع
- طرق التواصل:
    - أرقام هواتف مركز خدمة العملاء
    - بريد إلكتروني للدعم
    - نموذج اتصال مباشر
- قسم الشكاوى والاقتراحات (نموذج مخصص)

التفاعلات:
- جميع وسائل الدعم متاحة من أي صفحة (عادة في التذييل أو شريط التنقل)

7. ملف المستخدم / الإعدادات (User Profile/Settings)
-----------------------------------------------------
العناصر المرئية:
- عرض وتعديل البيانات الشخصية (اسم، رقم هوية، عنوان، بريد إلكتروني، هاتف)
- إعدادات الأمان (تغيير كلمة المرور، إدارة الأجهزة، تفعيل/تعطيل التحقق الثنائي)
- إعدادات الإشعارات (بريد إلكتروني، رسائل نصية، إشعارات داخل التطبيق)
- سجل النشاطات (اختياري)

التفاعلات:
- حفظ التعديلات، إدارة الأجهزة، تفعيل/تعطيل الإشعارات

ربط الصفحات والتنقل (Seamless Navigation)
------------------------------------------
- شريط تنقل رئيسي (Header) ثابت في أعلى الصفحة (Sticky)
    - روابط: الصفحة الرئيسية، لوحة التحكم/طلباتي، الخدمات، المساعدة/الدعم، ملف المستخدم/تسجيل الخروج
    - في الموبايل: قائمة هامبرغر (Hamburger Menu) تضم جميع العناصر
- روابط داخلية (Contextual Links) في نصوص الصفحات
- مسار التنقل (Breadcrumbs) في الصفحات الداخلية
- أزرار واضحة (Calls to Action) مثل "تقديم الطلب"، "عرض التفاصيل"
- أزرار العودة تعمل بشكل طبيعي
- إدارة الجلسات: جلسة المستخدم تبقى نشطة مع أمان مناسب

ملاحظات عامة:
-------------
- جميع الصفحات متوافقة مع الموبايل (Responsive)
- الأمان أولوية: تشفير، جدران نارية، مراقبة، إدارة جلسات، تحقق ثنائي
- تجربة المستخدم سلسة وسهلة، مع وضوح في جميع العناصر والوظائف
- يمكن لفريق التصميم تحويل هذا الوصف إلى Wireframes أو Mockups
- يمكن لفريق التطوير استخدام هذا الهيكل لبناء React/Angular Frontend وDjango/Node.js Backend

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {
            "id": "123456789",
            "name": "غسان خالد محمد أحمد",
            "email": "ghassan@yusr.gov.sd",
            "phone": "0912345678",
            "password": "yusr2024",
            "twoFA": False,
            "apps": [],
            "activity": ["تسجيل الدخول الأخير: 2024-06-10 09:12"]
        }
    ]

def save_users():
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(usersDB, f, ensure_ascii=False, indent=2)

usersDB = load_users()

# بيانات الخدمات (محاكاة)
services = [
    {
        "id": "passport-renew",
        "title": "تجديد جواز السفر",
        "desc": "خدمة إلكترونية لتجديد جواز السفر السوداني للمواطنين داخل وخارج السودان.",
        "docs": ["صورة الجواز القديم (PDF, JPG, PNG)", "صورة شخصية حديثة", "إيصال سداد الرسوم"],
        "steps": ["تعبئة النموذج الإلكتروني", "رفع المستندات المطلوبة", "دفع الرسوم", "انتظار الموافقة والاستلام"],
        "fields": [
            {"label": "رقم الجواز", "type": "text", "id": "passportNum", "required": True},
            {"label": "مكان الإصدار", "type": "text", "id": "issuePlace", "required": True}
        ],
        "eta": "2 يوم عمل"
    },
    {
        "id": "id-renew",
        "title": "تجديد بطاقة الهوية",
        "desc": "خدمة تجديد بطاقة الهوية الوطنية إلكترونياً.",
        "docs": ["صورة البطاقة القديمة", "صورة شخصية", "إيصال سداد الرسوم"],
        "steps": ["تعبئة البيانات", "رفع المستندات", "دفع الرسوم", "انتظار الموافقة"],
        "fields": [
            {"label": "رقم البطاقة", "type": "text", "id": "idNum", "required": True}
        ],
        "eta": "1 يوم عمل"
    }
]

# بيانات القطاعات
sectors = [
    {"name": "الداخلية", "services": ["passport-renew", "id-renew"]},
    {"name": "الصحة", "services": []},
    {"name": "التعليم", "services": []},
    {"name": "المالية", "services": []},
    {"name": "القضاء", "services": []},
    {"name": "العدل", "services": []},
    {"name": "الشرطة", "services": []},
    {"name": "السجل المدني", "services": []}
]

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = next((u for u in usersDB if (u['id'] == username or u['email'] == username) and u['password'] == password), None)
    if user:
        user_copy = user.copy()
        user_copy.pop('password')
        # تحديث سجل النشاط
        user['activity'].insert(0, f"تسجيل الدخول الأخير: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
        save_users()
        return jsonify({"success": True, "user": user_copy})
    return jsonify({"success": False, "msg": "بيانات الدخول غير صحيحة."}), 401

@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.json
    if any(u['id'] == data['id'] or u['email'] == data['email'] for u in usersDB):
        return jsonify({"success": False, "msg": "المستخدم موجود مسبقاً."}), 409
    new_user = {
        "id": data['id'],
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone'],
        "password": data['password'],
        "twoFA": False,
        "apps": [],
        "activity": []
    }
    usersDB.append(new_user)
    save_users()
    return jsonify({"success": True})

@app.route('/api/services')
def api_services():
    return jsonify(services)

@app.route('/api/sectors')
def api_sectors():
    return jsonify(sectors)

@app.route('/api/user/<user_id>')
def api_user(user_id):
    user = next((u for u in usersDB if u['id'] == user_id), None)
    if user:
        user_copy = user.copy()
        user_copy.pop('password')
        return jsonify(user_copy)
    return jsonify({"msg": "المستخدم غير موجود"}), 404

@app.route('/api/user/<user_id>/apps', methods=['GET', 'POST'])
def api_user_apps(user_id):
    user = next((u for u in usersDB if u['id'] == user_id), None)
    if not user:
        return jsonify({"msg": "المستخدم غير موجود"}), 404
    if request.method == 'GET':
        return jsonify(user.get('apps', []))
    # إضافة طلب جديد
    data = request.json
    app_data = {
        "id": data.get('id'),
        "service": data.get('service'),
        "date": data.get('date'),
        "status": data.get('status'),
        "lastUpdate": data.get('lastUpdate')
    }
    user['apps'].append(app_data)
    save_users()
    return jsonify({"success": True})

@app.route('/api/user/<user_id>/profile', methods=['POST'])
def api_update_profile(user_id):
    user = next((u for u in usersDB if u['id'] == user_id), None)
    if not user:
        return jsonify({"msg": "المستخدم غير موجود"}), 404
    data = request.json
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    user['phone'] = data.get('phone', user['phone'])
    save_users()
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)