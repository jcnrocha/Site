import re

with open('fti.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(
    r'(<span class="aula-num">SA (\d+)</span>.*?<div class="aula-tags">)<span class="tag tag-aula">Plano de Aula</span>',
    lambda m: m.group(1) + f'<a href="plano_aula_SA{m.group(2)}_fti.html" class="tag tag-aula" target="_blank">Plano de Aula</a>',
    content,
    flags=re.DOTALL
)

with open('fti.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated fti.html links")
