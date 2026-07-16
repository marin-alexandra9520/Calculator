import streamlit as st

# 1. Proprietățile de bază ale paginii web
st.set_page_config(
    page_title="Calculator Preț - Alexandra Marin",
    page_icon="🎓",
    layout="centered"
)

# 2. Design Premium Modern (Culorile Brandului: Albastru Regal și Auriu)
st.markdown("""
    <style>
    .stApp {
        background-color: #fcfdfe;
    }
    
    /* Header Principal */
    .brand-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #0b2545 0%, #134074 100%);
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        border-bottom: 5px solid #cf9e42;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .brand-title {
        font-family: 'Georgia', serif;
        font-size: 2.3rem;
        font-weight: bold;
        color: #ffffff;
        margin: 0;
        letter-spacing: 1px;
    }
    .brand-subtitle {
        font-size: 1rem;
        color: #cf9e42;
        margin-top: 5px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Casetele de completare date */
    div[data-testid="stForm"] {
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        background-color: #ffffff !important;
        padding: 30px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }
    
    .section-title {
        color: #0b2545;
        border-left: 5px solid #cf9e42;
        padding-left: 10px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-weight: bold;
    }
    
    /* Butoane Streamlit standard */
    .stButton > button {
        background: linear-gradient(135deg, #cf9e42 0%, #b38430 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        box-shadow: 0 4px 10px rgba(207, 158, 66, 0.3) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 15px rgba(207, 158, 66, 0.5) !important;
    }
    
    /* Caseta finală cu rezultatul */
    .result-box {
        background-color: #0b2545;
        color: white;
        padding: 30px;
        border-radius: 12px;
        border-left: 8px solid #cf9e42;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(11, 37, 69, 0.2);
    }
    
    /* Butonul de trimitere pe Facebook Messenger */
    .fb-button {
        display: inline-block;
        background-color: #1877f2;
        color: white !important;
        text-decoration: none;
        padding: 14px 20px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        margin-top: 20px;
        box-shadow: 0 4px 10px rgba(24, 119, 242, 0.3);
        transition: background-color 0.3s;
    }
    .fb-button:hover {
        background-color: #145dbf;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Antetul Vizual
st.markdown("""
    <div class="brand-header">
        <div class="brand-title">AM ALEXANDRA MARIN</div>
        <div class="brand-subtitle">Excelență în Educație • Calculator Oficial de Prețuri</div>
    </div>
""", unsafe_allow_html=True)

st.write("Introduceți detaliile lucrărilor dorite. Pentru comenzi multiple, sistemul aplică automat discountul în coș (20% pentru 2 lucrări, 30% pentru 3 lucrări și 40% pentru minim 4 lucrări). De asemenea, modulele suplimentare devin gratuite pentru lucrările de cel puțin 60 de pagini.")

# 4. Gestionarea stării pentru lucrări multiple
if 'numar_lucrari' not in st.session_state:
    st.session_state.numar_lucrari = 1

col_add, col_rem = st.columns(2)
with col_add:
    if st.button("➕ Adaugă încă o lucrare în comandă"):
        st.session_state.numar_lucrari += 1
with col_rem:
    if st.button("➖ Elimină ultima lucrare") and st.session_state.numar_lucrari > 1:
        st.session_state.numar_lucrari -= 1

# 5. Configurația tarifelor, domeniilor și coeficienților
dict_tip_lucrare = {
    "Eseu": 12,
    "Proiect facultate": 12,
    "Articol științific": 30,
    "Lucrare de licență / grad": 20,
    "Lucrare de disertație": 22,
    "Teză de doctorat": 40
}

dict_domenii = {
    "Admin. afacerilor, Marketing, Turism, Sport": 1.0,
    "Geografie, PIPP (Pedagogie)": 1.2,
    "Contabilitate, Finanțe-Bănci, Biologie, Horticultură, Silvicultură": 1.4,
    "Drept": 1.6,
    "Medicină, AMG (Nursing)": 1.8
}

dict_continut = {
    "Doar corecturi și verificare": 0.30,
    "Doar partea teoretică": 0.40,
    "Doar partea practică": 0.60,
    "Lucrare completă (Teorie + Practică)": 1.00
}

dict_urgenta = {
    "Standard (peste 30 de zile)": 1.0,
    "Normal (15 - 30 de zile)": 1.1,
    "Urgent (7 - 14 zile)": 1.3,
    "Critic (sub 7 zile)": 1.6
}

lucrari_salvate = []

# 6. Structura interfeței (Formular)
with st.form("calculator_nou_simplu"):
    
    for i in range(st.session_state.numar_lucrari):
        st.markdown(f"<h3 class='section-title'>Lucrarea #{i+1}</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            tip_sel = st.selectbox(f"Tipul Lucrării #{i+1}:", list(dict_tip_lucrare.keys()), key=f"tip_{i}")
            domeniu_sel = st.selectbox(f"Specializarea / Domeniul #{i+1}:", list(dict_domenii.keys()), key=f"dom_{i}")
        with col2:
            tema_introdusa = st.text_input(f"Tema lucrării #{i+1} (Opțional):", placeholder="Ex: Managementul resurselor umane...", key=f"tema_{i}")
            
        continut_sel = st.radio(
            f"Ce structură doriți pentru Lucrarea #{i+1}?",
            list(dict_continut.keys()),
            key=f"cont_{i}"
        )
        
        col3, col4 = st.columns(2)
        with col3:
            pagini_sel = st.number_input(f"Număr pagini necesare #{i+1}:", min_value=1, max_value=300, value=30, step=5, key=f"pag_{i}")
        with col4:
            urgenta_sel = st.selectbox(f"Timpul de predare #{i+1}:", list(dict_urgenta.keys()), key=f"urg_{i}")
            
        st.markdown(f"**Module practice și pachete suplimentare pentru Lucrarea #{i+1} (opțional):**")
        c1, c2, c3 = st.columns(3)
        with c1:
            opt_spss = st.checkbox("Analiză statistică avansată (SPSS/Excel) (+200 lei)", key=f"spss_{i}")
            opt_qgis = st.checkbox("Hărți tematice în QGIS (+200 lei)", key=f"qgis_{i}")
        with c2:
            opt_python = st.checkbox("Aplicații și programare în Python (+300 lei)", key=f"py_{i}")
            opt_wp = st.checkbox("Site-uri web în WordPress (+500 lei)", key=f"wp_{i}")
        with c3:
            opt_ppt = st.checkbox("Pachet susținere (PPT + discurs) (+50 lei)", key=f"ppt_{i}")

        # Salvarea datelor
        lucrari_salvate.append({
            "tip": tip_sel,
            "domeniu": domeniu_sel,
            "tema": tema_introdusa if tema_introdusa else "Nespecificată",
            "continut": continut_sel,
            "pagini": pagini_sel,
            "urgenta": urgenta_sel,
            "module": {
                "spss": opt_spss,
                "qgis": opt_qgis,
                "python": opt_python,
                "wordpress": opt_wp,
                "ppt": opt_ppt
            }
        })
        if i < st.session_state.numar_lucrari - 1:
            st.markdown("<hr style='border:1px dashed #e2e8f0'/>", unsafe_allow_html=True)
            
    submit_calcul = st.form_submit_button("GENEREAZĂ CALCULUL DE PREȚ")

# 7. Logica Matematică Executată la Click
if submit_calcul:
    suma_lucrari_individuale = 0
    detalii_afisare_lucrari = ""
    
    for idx, lucrare in enumerate(lucrari_salvate):
        pret_per_pagina = dict_tip_lucrare[lucrare["tip"]]
        B = dict_continut[lucrare["continut"]]
        C_urg = dict_urgenta[lucrare["urgenta"]]
        A_dom = dict_domenii[lucrare["domeniu"]]
        
        # Calcul module suplimentare (Devin GRATUITE dacă pagini >= 60)
        are_module_gratuite = lucrare["pagini"] >= 60
        
        Df = 0
        if not are_module_gratuite:
            if lucrare["module"]["spss"]: Df += 200
            if lucrare["module"]["qgis"]: Df += 200
            if lucrare["module"]["python"]: Df += 300
            if lucrare["module"]["wordpress"]: Df += 500
            if lucrare["module"]["ppt"]: Df += 50
        
        # Formula: Preț = [(Nr. pagini * Ppag) * B * C_urg * A_dom] + Df
        pret_calculat = ((lucrare["pagini"] * pret_per_pagina) * B * C_urg * A_dom) + Df
        
        if pret_calculat < 200:
            pret_calculat = 200.0
            prag_aplicat = " (Ajustat la pragul minim)"
        else:
            prag_aplicat = ""
            
        suma_lucrari_individuale += pret_calculat
        
        # Generare detalii module pentru afișare
        text_module = ""
        if are_module_gratuite:
            selectate = []
            if lucrare["module"]["spss"]: selectate.append("SPSS/Excel")
            if lucrare["module"]["qgis"]: selectate.append("Hărți QGIS")
            if lucrare["module"]["python"]: selectate.append("Python")
            if lucrare["module"]["wordpress"]: selectate.append("WordPress")
            if lucrare["module"]["ppt"]: selectate.append("Pachet PPT")
            
            if selectate:
                text_module = f"• Module incluse: <i>{', '.join(selectate)}</i> <b style='color:#22c55e;'>(GRATUIT - Ofertă lucrare peste 60 pagini)</b><br/>"
            else:
                text_module = "• Module suplimentare: Fără module adiționale selectate<br/>"
        else:
            text_module = f"• Module suplimentare: +{Df} lei<br/>"

        detalii_afisare_lucrari += (
            f"🔹 <b>Lucrarea #{idx+1}</b> ({lucrare['tip']})<br/>"
            f"• Domeniu: <i>{lucrare['domeniu']}</i> | Temă: <i>{lucrare['tema']}</i><br/>"
            f"• Structură selectată: <i>{lucrare['continut']}</i><br/>"
            f"• Dimensiune: {lucrare['pagini']} pagini<br/>"
            f"• Timp de predare: {lucrare['urgenta']}<br/>"
            f"{text_module}"
            f"• <b>Preț estimat: {round(pret_calculat)} lei</b>{prag_aplicat}<br/><br/>"
        )
        
    numar_total_lucrari = len(lucrari_salvate)
    reducere_procent = 0
    
    # Noua grilă de discount-uri solicitată:
    if numar_total_lucrari == 1:
        pret_final_facturat = suma_lucrari_individuale
    elif numar_total_lucrari == 2:
        pret_final_facturat = suma_lucrari_individuale * 0.80  # 20% reducere
        reducere_procent = 20
    elif numar_total_lucrari == 3:
        pret_final_facturat = suma_lucrari_individuale * 0.70  # 30% reducere
        reducere_procent = 30
    else:  # de la 4 lucrări în sus
        pret_final_facturat = suma_lucrari_individuale * 0.60  # 40% reducere
        reducere_procent = 40
        
    pret_final_facturat = round(pret_final_facturat)
    subtotal_rotund = round(suma_lucrari_individuale)

    # Construirea secțiunii de preț cu preț tăiat
    if reducere_procent > 0:
        randuri_pret = (
            f"<tr><td>Preț inițial cumulat:</td>"
            f"<td style='text-align:right; text-decoration: line-through; color: #ef4444; font-size: 1.1rem;'>{subtotal_rotund} lei</td></tr>"
            f"<tr><td>Reducere aplicată ({reducere_procent}%):</td>"
            f"<td style='text-align:right; color:#22c55e;'>-{subtotal_rotund - pret_final_facturat} lei</td></tr>"
            f"<tr style='font-size: 1.6rem; font-weight: bold; color: #ffffff;'><td style='padding-top:10px;'>PREȚ FINAL REDUS:</td>"
            f"<td style='text-align:right; padding-top:10px; color: #cf9e42;'>{pret_final_facturat} RON</td></tr>"
        )
    else:
        randuri_pret = (
            f"<tr style='font-size: 1.6rem; font-weight: bold; color: #ffffff;'><td style='padding-top:10px;'>PREȚ TOTAL ESTIMAT:</td>"
            f"<td style='text-align:right; padding-top:10px; color: #cf9e42;'>{pret_final_facturat} RON</td></tr>"
        )

    # 8. Devizul Final (fără tab-uri sau indentări la început de rând ca să nu se strice afișarea)
    st.markdown(f"""
<div class="result-box">
<h3 style="color: #cf9e42; margin-top: 0; font-family: 'Georgia', serif; border-bottom: 1px solid #cf9e42; padding-bottom: 5px;">Deviz Estimativ Rezultat</h3>
<p style="font-size: 0.95rem; line-height: 1.4; color: #f1f5f9;">{detalii_afisare_lucrari}</p>
<hr style="border: 0; border-top: 2px solid #cf9e42; margin: 15px 0;" />
<table style="width:100%; font-size: 1.05rem; color: white;">
{randuri_pret}
</table>
<p style="font-size: 0.9rem; color: #e2e8f0; margin-top: 15px; background: rgba(255,255,255,0.05); padding: 10px; border-radius: 6px;">
✔ Lucrări academice originale cu raport anti-plagiat inclus<br/>
✔ Modificări nelimitate până la predarea finală a proiectului<br/>
✔ Confidențialitate deplină garantată
</p>
<a href="https://m.me/61577630195202" target="_blank" class="fb-button">📩 Trimite comanda direct pe Facebook Messenger</a>
</div>
""", unsafe_allow_html=True)
