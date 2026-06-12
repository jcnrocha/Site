import re

with open('redes.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_fn(match):
    sa_num = match.group(1)
    # The span we want to replace is match.group(2)
    # But wait, we can just replace the whole match
    # match is the entire block from '<span class="aula-num">SA XX</span>' down to '<span class="tag tag-aula">Plano de Aula</span>'
    
    full_text = match.group(0)
    replaced_text = full_text.replace(
        '<span class="tag tag-aula">Plano de Aula</span>',
        f'<a href="plano_aula_SA{sa_num}_redes.html" class="tag tag-aula" target="_blank">Plano de Aula</a>'
    )
    return replaced_text

# Regex matches <span class="aula-num">SA (\d+)</span> followed by anything up to <span class="tag tag-aula">Plano de Aula</span>
new_content = re.sub(
    r'(<span class="aula-num">SA (\d+)</span>.*?<div class="aula-tags">)<span class="tag tag-aula">Plano de Aula</span>',
    lambda m: m.group(1) + f'<a href="plano_aula_SA{m.group(2)}_redes.html" class="tag tag-aula" target="_blank">Plano de Aula</a>',
    content,
    flags=re.DOTALL
)

with open('redes.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated redes.html links")
