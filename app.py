"""
app.py - واجهة المستخدم التفاعلية
"""

from google.colab import files
import os
from file_handlers import FileHandler

def upload_file():
    """تحميل ملف من جهاز المستخدم."""
    print("⬆️  من فضلك، اختر ملفًا (.txt أو .docx أو .pdf)...")
    uploaded = files.upload()
    if not uploaded:
        raise Exception("لم يتم تحميل أي ملف.")
    return list(uploaded.keys())[0]

def get_user_preferences():
    """الحصول على تفضيلات المستخدم."""
    print("\n⚙️  الرجاء تحديد إعدادات إخفاء الهوية:")
    entities_input = input("اختر أنواع الكيانات (مثال: PERSON, ORG, GPE): ").strip()
    entity_types = [etype.strip().upper() for etype in entities_input.split(",") if etype.strip()]
    
    mode_input = input("نمط الاستبدال: (1) بيانات وهمية, (2) [REDACTED]: ").strip()
    replacement_mode = 'fake' if mode_input == '1' else 'redacted'
    
    return entity_types, replacement_mode

def main():
    """الدالة الرئيسية."""
    print("مرحبًا بك في تطبيق إخفاء هوية المستندات! 🛡️\n")
    
    try:
        filename = upload_file()
        entity_types, replacement_mode = get_user_preferences()
        
        output_path, anonymized_text = FileHandler.process_file(
            input_path=filename,
            entity_types=entity_types,
            replacement_mode=replacement_mode,
            output_dir="output"
        )
        
        print(f"\n💾 تم الحفظ في: {output_path}")
        print("\n🔍 معاينة:")
        print(anonymized_text[:300] + "...")
        
        files.download(output_path)
        print("\n🎉 تم الإنجاز!")
        
    except Exception as e:
        print(f"\n❌ خطأ: {e}")

if __name__ == "__main__":
    main()