import os
import re
import glob

# HTML template string
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Plano de Aula SA {SA_NUM} — {SHORT_TITLE} · Redes</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{ --uc-main: #0F6E56; --uc-light: #E1F5EE; --uc-tx: #04342C; --dark: #0D1A2B; --yellow: #F9C74F; --gold: #C49A00; --gray: #64748B; --light: #F2F5F8; --white: #FFFFFF; --text: #1A2635; --border: #D4DCE4; --warn-bg: #FFF8E7; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'DM Sans', sans-serif; background: var(--light); color: var(--text); line-height: 1.7; }}
  .page-header {{ background: var(--dark); position: relative; overflow: hidden; }}
  .page-header::before {{ content:''; position:absolute; left:0; top:0; bottom:0; width:6px; background:var(--uc-main); }}
  .page-header::after  {{ content:''; position:absolute; left:6px; top:0; bottom:0; width:3px; background:var(--yellow); }}
  .header-inner {{ max-width:980px; margin:0 auto; padding:44px 48px 44px 60px; display:flex; justify-content:space-between; align-items:flex-start; gap:32px; }}
  .header-label {{ font-family:'DM Sans',sans-serif; font-size:15px; font-weight:500; color:#94A3B8; margin-bottom:14px; display:flex; align-items:center; flex-wrap:wrap; gap:8px; }}
  .header-label .hl-sep  {{ color:#475569; font-weight:300; }}
  .header-label .hl-sa   {{ font-family:'DM Mono',monospace; font-size:14px; font-weight:600; color:var(--uc-main); background:rgba(15,110,86,0.18); padding:2px 10px; border-radius:20px; }}
  .header-label .hl-tri  {{ color:var(--yellow); font-weight:600; }}
  .header-label .hl-data {{ font-family:'DM Mono',monospace; font-size:13px; color:#64748B; }}
  .header-title {{ font-family:'DM Serif Display',serif; font-size:36px; line-height:1.15; color:var(--white); margin-bottom:10px; }}
  .header-title span {{ color:var(--yellow); }}
  .header-sub {{ font-size:13.5px; color:#64748B; line-height:1.6; }}
  .header-badge {{ background:var(--uc-main); color:var(--white); font-size:12px; font-weight:600; padding:6px 14px; border-radius:20px; white-space:nowrap; margin-top:4px; }}
  .container {{ max-width:980px; margin:0 auto; padding:40px 48px; }}
  .section {{ background:var(--white); border-radius:12px; border:1px solid var(--border); box-shadow:0 2px 12px rgba(0,0,0,0.04); margin-bottom:28px; overflow:hidden; }}
  .section-header {{ display:flex; align-items:center; gap:12px; padding:18px 26px; border-bottom:1px solid var(--border); background:var(--light); }}
  .section-icon  {{ font-size:20px; }}
  .section-title {{ font-size:16px; font-weight:700; color:var(--dark); flex:1; }}
  .section-tag   {{ font-family:'DM Mono',monospace; font-size:11px; font-weight:500; background:var(--uc-light); color:var(--uc-main); padding:3px 10px; border-radius:12px; }}
  .section-tag-gray {{ background:var(--light); color:var(--gray); border:1px solid var(--border); font-family:'DM Mono',monospace; font-size:11px; font-weight:500; padding:3px 10px; border-radius:12px; }}
  .section-body  {{ padding:24px 26px; }}
  
  .tema-box {{ background:var(--light); border-radius:8px; padding:14px 18px; font-size:15px; font-weight:600; color:var(--dark); border-left:4px solid var(--uc-main); }}
  .hab-row  {{ margin-top:14px; display:flex; flex-wrap:wrap; gap:8px; }}
  .hab-tag  {{ font-family:'DM Mono',monospace; font-size:11.5px; font-weight:500; background:var(--uc-light); color:var(--uc-tx); padding:4px 12px; border-radius:12px; border:1px solid rgba(15,110,86,0.2); }}
  
  .obj-list  {{ list-style:none; display:flex; flex-direction:column; gap:8px; }}
  .obj-list li {{ display:flex; align-items:flex-start; gap:12px; padding:12px 16px; background:var(--light); border-radius:8px; font-size:13.5px; border-left:3px solid var(--uc-main); }}
  .obj-num {{ background:var(--uc-main); color:var(--white); font-family:'DM Mono',monospace; font-size:11px; font-weight:500; width:22px; height:22px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-shrink:0; margin-top:1px; }}
  
  .content-list {{ list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:16px; }}
  .content-list li {{ display:flex; align-items:flex-start; gap:12px; padding:12px 16px; background:var(--white); border:1px solid var(--border); border-radius:8px; font-size:13.5px; }}
  .content-list li::before {{ content:'▸'; color:var(--uc-main); font-weight:bold; }}
  
  .time-table {{ width:100%; border-collapse:collapse; font-size:13px; border-radius:8px; overflow:hidden; border:1px solid var(--border); margin-bottom:16px; }}
  .time-table thead tr {{ background:var(--dark); }}
  .time-table th {{ color:var(--white); padding:11px 14px; text-align:left; font-size:12.5px; }}
  .time-table td {{ padding:10px 14px; border-bottom:1px solid var(--border); vertical-align:top; }}
  .time-table tr:nth-child(even) td {{ background:#F7FAFC; }}
  .etapa-pill {{ font-size:12px; font-weight:600; padding:2px 10px; border-radius:12px; display:inline-block; white-space:nowrap; background:#DCFCE7; color:#166534; }}
  
  .connection-row {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
  .conn-card  {{ border-radius:8px; padding:14px 18px; font-size:13.5px; }}
  .conn-ant   {{ background:var(--uc-light); border-left:4px solid var(--uc-main); }}
  .conn-prox  {{ background:var(--warn-bg); border-left:4px solid var(--gold); }}
  .conn-label {{ font-size:11px; font-family:'DM Mono',monospace; font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px; }}
  .conn-ant  .conn-label {{ color:var(--uc-main); }}
  .conn-prox .conn-label {{ color:var(--gold); }}
  
  .recursos-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }}
  .recurso-item  {{ background:var(--light); border:1px solid var(--border); border-radius:8px; padding:12px 14px; font-size:13px; display:flex; align-items:center; gap:10px; }}
  
  .btn-group  {{ position:fixed; top:20px; right:24px; z-index:999; display:flex; flex-direction:column; gap:8px; }}
  .btn-action {{ border:none; border-radius:8px; padding:10px 18px; font-family:'DM Sans',sans-serif; font-size:13px; font-weight:600; cursor:pointer; display:flex; align-items:center; gap:8px; white-space:nowrap; background:var(--dark); color:var(--white); }}
  footer {{ background:var(--dark); color:#475569; text-align:center; padding:22px; font-size:12px; font-family:'DM Mono',monospace; margin-top:16px; border-top:3px solid var(--uc-main); }}
  
  .nota-box {{ background:var(--uc-light); border:1px solid rgba(15,110,86,0.25); border-left:4px solid var(--uc-main); border-radius:8px; padding:12px 16px; font-size:13px; color:var(--uc-tx); margin-bottom:16px; }}
  .dinamica-box {{ background:var(--light); border:1px solid var(--border); border-radius:10px; overflow:hidden; margin-bottom:16px; }}
  .dinamica-header {{ background:var(--uc-tx); color:var(--white); padding:12px 18px; font-size:14px; font-weight:700; display:flex; align-items:center; gap:8px; }}
  .dinamica-body {{ padding:18px; font-size:13.5px; }}
</style>
</head>
<body>
<div class="btn-group">
  <button class="btn-action" onclick="window.print()">🖨️ Imprimir</button>
</div>

<header class="page-header">
  <div class="header-inner">
    <div>
      <div class="header-label">
        Plano de Aula
        <span class="hl-sep">·</span>
        <span class="hl-sa">SA {SA_NUM}</span>
        <span class="hl-sep">·</span>
        <span class="hl-tri">{TRIMESTRE}</span>
        <span class="hl-sep">·</span>
        <span class="hl-data">{DATE}</span>
      </div>
      <h1 class="header-title">{THEME_H1}</h1>
      <p class="header-sub">
        <span class="uc-nome">UC: Fundamentos de Redes de Computadores · 2ª Série · Técnico em Desenvolvimento de Sistemas</span>
        SENAI Umuarama · Prof. Julio Cesar
      </p>
    </div>
    <div class="header-badge">{BADGE}</div>
  </div>
</header>

<main class="container">
{SECTIONS}
</main>
<footer>
  Plano de Aula · SA {SA_NUM} · Prof. Julio Cesar · Técnico em Desenvolvimento de Sistemas · SENAI Umuarama · 2026
</footer>
</body>
</html>
"""

def parse_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata from top
    sa_num = ""
    trimestre = ""
    theme = "Plano de Aula"
    hability = "Continuidade"
    
    lines = content.split('\n')
    for l in lines:
        if l.startswith('## Aula'):
            m = re.search(r'Aula (\d+) — (.+)', l)
            if m:
                sa_num = m.group(1)
                trimestre = m.group(2)
        elif l.startswith('**Habilidade da matriz:**'):
            hability = l.replace('**Habilidade da matriz:**', '').strip()
            
    # Find Tema
    try:
        idx = lines.index('## Tema')
        theme = lines[idx+2].strip()
    except:
        pass
        
    return sa_num, trimestre, theme, hability, lines

def md_to_html(lines, section_name):
    # Very crude Markdown to HTML parser tailored to this project
    html = []
    in_list = False
    in_table = False
    
    def close_open():
        nonlocal in_list, in_table
        if in_list: html.append('</ul>'); in_list = False
        if in_table: html.append('</tbody></table>'); in_table = False

    for l in lines:
        l = l.strip()
        if not l or l == '---': continue
        
        # Format text
        l = re.sub(r'\*\*(.*?)\*\*', r'<strong>\g<1></strong>', l)
        l = re.sub(r'\*(.*?)\*', r'<em>\g<1></em>', l)

        if l.startswith('- '):
            if in_table: close_open()
            if not in_list:
                html.append('<ul class="content-list">')
                in_list = True
            html.append(f'<li>{l[2:]}</li>')
            
        elif l.startswith('|') and '---' not in l:
            if in_list: close_open()
            parts = [p.strip() for p in l.split('|')[1:-1]]
            if not in_table:
                html.append('<table class="time-table">')
                html.append('<thead><tr>')
                for p in parts: html.append(f'<th>{p}</th>')
                html.append('</tr></thead><tbody>')
                in_table = True
            else:
                html.append('<tr>')
                for i, p in enumerate(parts): 
                    if i==0 and section_name == 'Organização do Tempo':
                        html.append(f'<td><span class="etapa-pill">{p}</span></td>')
                    else:
                        html.append(f'<td>{p}</td>')
                html.append('</tr>')
                
        elif l.startswith('|') and '---' in l:
            pass
            
        elif l.startswith('> '):
            close_open()
            html.append(f'<div class="nota-box">{l[2:]}</div>')
            
        elif re.match(r'^\d+\.', l): # numbered list
            if in_table: close_open()
            if not in_list:
                html.append('<ul class="obj-list">')
                in_list = True
            item = re.sub(r'^\d+\.\s*', '', l)
            num = re.match(r'^(\d+)\.', l).group(1)
            html.append(f'<li><span class="obj-num">{num}</span>{item}</li>')
            
        elif l.startswith('### '):
            close_open()
            html.append(f'<p style="font-size:14px;font-weight:700;color:var(--dark);margin:18px 0 8px;">{l[4:]}</p>')
            
        else:
            close_open()
            if section_name == 'Objetivos de Aprendizagem' and l.startswith('Ao final'):
                html.append(f'<p class="obj-intro">{l}</p>')
            elif section_name == 'Conexão com Conteúdos' and '←' in l:
                pass # skip raw text for connections, we handle it later
            else:
                html.append(f'<p style="font-size:13.5px; margin-bottom:12px;">{l}</p>')

    close_open()
    return '\n'.join(html)

def build_all():
    files = glob.glob('plano_aula_SA*.md')
    # Filter files >= SA28
    files = [f for f in files if int(re.search(r'SA(\d+)', f).group(1)) >= 28]

    # In redes.html we can get dates, but we can also just guess or leave placeholder
    # Actually, the user's files have "← Aula anterior | Aula 27 — 02/09/2026"
    # We can extract dates from the 'Conexão com Conteúdos' section of the markdown itself!

    for f in files:
        sa_num = re.search(r'SA(\d+)', f).group(1); _, trimestre, theme, hability, lines = parse_md(f)
        
        # Split into sections based on '## '
        sections = {}
        curr_section = None
        curr_lines = []
        
        for l in lines:
            if l.startswith('## '):
                if curr_section:
                    sections[curr_section] = curr_lines
                curr_section = l[3:].strip()
                curr_lines = []
            else:
                curr_lines.append(l)
        if curr_section:
            sections[curr_section] = curr_lines

        # Extract dates from "Conexão com Conteúdos"
        date = "11/11/2026" # fallback
        ant = "Aula anterior"
        prox = "Próxima aula"
        if 'Conexão com Conteúdos' in sections:
            con_lines = sections['Conexão com Conteúdos']
            for cl in con_lines:
                if '←' in cl:
                    parts = cl.split('|')
                    if len(parts) >= 3: ant = parts[2].strip()
                elif '→' in cl:
                    parts = cl.split('|')
                    if len(parts) >= 3: prox = parts[2].strip()
                    
            # Try to extract current date from the anterior or proxima
            # Wait, the date of SA28 is in SA27's "Próxima aula".
            # Or in SA28's markdown, maybe it says "Próxima aula -> 16/09", so SA28 is 09/09.
            # I will just put the date from `ant` or `prox` if possible, otherwise placeholder.
            # Let's read it from redes.html!
            date_match = ""

        # Let's read redes.html to get the correct date
        with open('redes.html', 'r', encoding='utf-8') as redes_f:
            redes_html = redes_f.read()
            # <span class="aula-num">SA 28</span><span class="aula-data">09/09</span>
            dm = re.search(fr'<span class="aula-num">SA {sa_num}</span><span class="aula-data">([^<]+)</span>', redes_html)
            if dm:
                date = f"{dm.group(1)}/2026"

        out_sections = []
        
        for sec_name, sec_lines in sections.items():
            if sec_name in ['Tema', 'Aula ' + sa_num + ' — ' + trimestre]: continue
            
            icon = '📌'
            if 'Objetivos' in sec_name: icon = '🏆'
            elif 'Conteúdo' in sec_name: icon = '📚'
            elif 'Tempo' in sec_name: icon = '⏱️'
            elif 'Dinâmica' in sec_name: icon = '🎮'
            elif 'Avaliação' in sec_name: icon = '📝'
            elif 'Conexão' in sec_name: icon = '🔗'
            elif 'Recursos' in sec_name: icon = '📦'
            
            html_body = ""
            
            if 'Conexão com Conteúdos' in sec_name:
                html_body = f'''<div class="connection-row">
        <div class="conn-card conn-ant"><div class="conn-label">← Aula anterior</div><div>{ant}</div></div>
        <div class="conn-card conn-prox"><div class="conn-label">Próxima aula →</div><div>{prox}</div></div>
      </div>'''
            elif 'Tema' in sec_name:
                pass # handled below
            elif 'Recursos' in sec_name:
                html_body = '<div class="recursos-grid">'
                for r in sec_lines:
                    r = r.replace('- ', '').strip()
                    if not r: continue
                    html_body += f'<div class="recurso-item"><span class="recurso-icon">✔️</span><span>{r}</span></div>'
                html_body += '</div>'
            elif 'Dinâmica' in sec_name:
                # Wrap everything in a dinamica box
                inner_html = md_to_html(sec_lines, sec_name)
                html_body = f'<div class="dinamica-box"><div class="dinamica-header">🎮 {sec_name}</div><div class="dinamica-body">{inner_html}</div></div>'
            else:
                html_body = md_to_html(sec_lines, sec_name)
            
            out_sections.append(f'''
  <section class="section">
    <div class="section-header">
      <span class="section-icon">{icon}</span>
      <span class="section-title">{sec_name}</span>
      <span class="section-tag-gray">SA {sa_num}</span>
    </div>
    <div class="section-body">
      {html_body}
    </div>
  </section>''')

        # Add Tema section manually
        tema_section = f'''
  <section class="section">
    <div class="section-header">
      <span class="section-icon">🎯</span>
      <span class="section-title">Tema e Habilidade</span>
      <span class="section-tag">{trimestre} · SA {sa_num}</span>
    </div>
    <div class="section-body">
      <div class="tema-box">{theme}</div>
      <div class="hab-row"><span class="hab-tag">{hability}</span></div>
    </div>
  </section>'''
  
        out_sections.insert(0, tema_section)
        
        final_html = html_template.format(
            SA_NUM=sa_num,
            SHORT_TITLE=theme,
            TRIMESTRE=trimestre,
            DATE=date,
            THEME_H1=f"{theme}<br><span>Redes de Computadores</span>",
            BADGE="Aula Regular",
            SECTIONS=''.join(out_sections)
        )
        
        out_name = f'plano_aula_SA{sa_num}_redes.html'
        with open(out_name, 'w', encoding='utf-8') as f_out:
            f_out.write(final_html)
        print(f"Generated {out_name}")

if __name__ == '__main__':
    build_all()
