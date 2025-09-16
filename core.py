"""
core.py - النواة الأساسية للتطبيق
تحتوي على منطق إخفاء الهوية، نموذج NER، وFaker.
"""

import os
from typing import List, Dict, Any
from pathlib import Path
from gliner import GLiNER
from faker import Faker

class TextAnonymizerCore:
    """
    فئة النواة الأساسية التي تدير منطق إخفاء الهوية.
    """

    def __init__(self):
        """
        تهيئة النموذج وFaker.
        """
        print("🔄 جاري تحميل نموذج NuNER Zero...")
        self.model = GLiNER.from_pretrained("numind/NuNER_Zero")
        self.faker = Faker()
        print("✅ تم تحميل النموذج بنجاح!")

    def anonymize_text(self, text: str, entity_types: List[str], replacement_mode: str = 'fake') -> str:
        """
        إخفاء هوية الكيانات في نص معين باستخدام نموذج Zero-shot.

        Args:
            text: النص الأصلي.
            entity_types: قائمة الفئات (مثل ['PERSON', 'ORG', 'GPE']).
            replacement_mode: 'fake' للبيانات المزيفة أو 'redacted' لـ [REDACTED].

        Returns:
            النص بعد إخفاء الهوية.
        """
        # تحويل الفئات إلى labels
        labels_map = {'PERSON': 'person', 'ORG': 'organization', 'GPE': 'location'}
        labels = []
        for et in entity_types:
            if et in labels_map:
                labels.append(labels_map[et])
            else:
                labels.append(et.lower())
        
        if not labels:
            return text
        
        try:
            # التنبؤ بالكيانات
            entities = self.model.predict_entities(text, labels)
            # دمج وفرز الكيانات
            from utils import merge_entities
            entities = merge_entities(entities, text)
            
            # تقسيم النص واستبدال الكيانات
            parts = []
            last_end = 0
            
            for ent in entities:
                parts.append(text[last_end:ent['start']])
                
                if replacement_mode == 'fake':
                    label_lower = ent['label'].lower()
                    if 'person' in label_lower:
                        replacement = self.faker.name()
                    elif 'organization' in label_lower or 'org' in label_lower:
                        replacement = self.faker.company()
                    elif 'location' in label_lower or 'loc' in label_lower:
                        replacement = self.faker.city()
                    else:
                        replacement = '[REDACTED]'
                else:
                    replacement = '[REDACTED]'
                
                parts.append(replacement)
                last_end = ent['end']
            
            parts.append(text[last_end:])
            return ''.join(parts)
            
        except Exception as e:
            raise RuntimeError(f"خطأ في معالجة NER: {e}")