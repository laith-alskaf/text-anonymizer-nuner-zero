"""
utils.py - دوال مساعدة عامة
"""

from typing import List, Dict, Any

def merge_entities(entities: List[Dict[str, Any]], text: str) -> List[Dict[str, Any]]:
    """
    دمج الكيانات المجاورة لتجنب التكرار في الاستخراج.
    
    Args:
        entities: قائمة الكيانات المستخرجة.
        text: النص الأصلي.
        
    Returns:
        قائمة الكيانات المدمجة والمرتبة.
    """
    if not entities:
        return []
    
    # فرز الكيانات حسب موقع البداية
    sorted_entities = sorted(entities, key=lambda x: x['start'])
    
    # دمج الكيانات المتجاورة
    merged = []
    current = sorted_entities[0]
    
    for next_entity in sorted_entities[1:]:
        if (next_entity['label'] == current['label'] and 
            next_entity['start'] <= current['end'] + 1):
            # توسيع الكيان الحالي
            current['text'] = text[current['start']:next_entity['end']].strip()
            current['end'] = next_entity['end']
        else:
            merged.append(current)
            current = next_entity
    
    merged.append(current)
    return merged