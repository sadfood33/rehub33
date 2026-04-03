#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_main_content(html_path):
    """Извлекаем основной текстовый контент из HTML"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекаем текст между тегами
    text = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def get_city_from_path(path):
    """Извлекаем название города из пути"""
    parts = path.split('/')
    for part in parts:
        if part.endswith('.html'):
            return part.replace('.html', '')
    return ''

# Собираем все страницы городов
mo_pages = []
yo_pages = []

for root, dirs, files in os.walk('goroda/moskva'):
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            mo_pages.append(os.path.join(root, f))

for root, dirs, files in os.walk('goroda/yaroslavl'):
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            yo_pages.append(os.path.join(root, f))

print(f"Страниц МО: {len(mo_pages)}")
print(f"Страниц ЯО: {len(yo_pages)}")

# Проверяем несколько страниц на идентичность
if len(mo_pages) >= 2:
    content1 = extract_main_content(mo_pages[0])
    content2 = extract_main_content(mo_pages[1])
    
    # Простая проверка на совпадение (без учета названия города)
    words1 = set(content1.lower().split())
    words2 = set(content2.lower().split())
    
    overlap = len(words1 & words2) / min(len(words1), len(words2)) * 100
    print(f"\nПример сравнения:")
    print(f"{mo_pages[0]} vs {mo_pages[1]}")
    print(f"Перекрытие слов: {overlap:.1f}%")
