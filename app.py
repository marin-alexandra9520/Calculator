import streamlit as st

# ==========================================
# 1. Configurare Pagină & Stiluri CSS
# ==========================================
st.set_page_config(
    page_title="Află Singur Prețul - Lucrări Academice",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    """
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
    
    /* Formular */
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
    
    /* Caseta Informare / Avertisment */
    .info-box {
        background-color: #fef3c7;
        border-left: 5px solid #f59e0b;
        color: #92400e;
        padding: 12px 15px;
        border-radius: 6px;
        margin-top: 10px;
        font-weight: bold;
        font-size: 0.9rem;
    }
    
    /* Butoane Formular */
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
    
    /* Caseta Rezultat Deviz */
    .result-box {
        background-color: #0b2545;
        color: white;
        padding: 30px;
        border-radius: 12px;
        border-left: 8px solid #cf9e42;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(11, 37, 69, 0.2);
    }
    
    /* Sectiune Servicii Incluse */
    .included-services {
        background-color: #134074;
        border: 1px solid #cf9e42;
        border-radius: 8px;
        padding: 20px;
        margin-top: 20px;
        color: #e2e8f0;
    }
    .included-services h4 {
        color: #cf9e42;
        margin-top: 0;
        margin-bottom: 12px;
        font-family: 'Georgia', serif;
    }
    .included-services ul {
        margin: 0;
        padding-left: 20px;
    }
    .included-services li {
        margin-bottom: 8px;
        font-size: 0.92rem;
        line-height: 1.4;
    }

    /* Buton Messenger */
    .fb-button {
        display: block;
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
""",
    unsafe_allow_html=True,
)

# Header HTML
st.markdown(
    """
    <div class="brand-header">
        <div class="brand-title">AFLĂ SINGUR PREȚUL</div>
        <div class="brand-subtitle">Calculator Estimativ de Prețuri • Lucrări Academice</div>
    </div>
""",
    unsafe_allow_html=True,
)

st.write(
    "Selectați detaliile proiectului dumneavoastră. Pentru comenzi de mai multe lucrări, "
    "sistemul va aplica automat **10% discount pentru 2 lucrări** și **15% discount pentru 3 sau mai multe lucrări**."
)

# Admin Stare Coș (Număr de Lucrări)
if "numar_lucrari" not in st.session_state:
    st.session_state.numar_lucrari = 1

col_add, col_rem = st.columns(2)
with col_add:
    if st.button("➕ Adaugă încă o lucrare"):
        st.session_state.numar_lucrari += 1
with col_rem:
    if (
        st.button("➖ Elimină ultima lucrare")
        and st.session_state.numar_lucrari > 1
    ):
        st.session_state.numar_lucrari -= 1

# ==========================================
# 2. Mapare Niveluri Domenii & Grile
# ==========================================

NIVELURI_SPECIALIZARI = {
    # Nivel 1
    "Administrarea afacerilor": 1,
    "Management": 1,
    "Marketing": 1,
    "Turism": 1,
    "Comerț": 1,
    "Economie": 1,
    "Sport / Educație fizică și sport": 1,
    "Comunicare și relații publice": 1,
    "Științele comunicării": 1,
    "Jurnalism": 1,
    # Nivel 2
    "Geografie": 2,
    "Pedagogie": 2,
    "PIPP – Pedagogia învățământului primar și preșcolar": 2,
    "Psihopedagogie": 2,
    "Științele educației": 2,
    "Sociologie": 2,
    "Asistență socială": 2,
    "Istorie": 2,
    "Filosofie": 2,
    "Științe politice": 2,
    # Nivel 3
    "Contabilitate": 3,
    "Finanțe": 3,
    "Finanțe-Bănci": 3,
    "Economie și afaceri internaționale": 3,
    "Biologie": 3,
    "Ecologie": 3,
    "Horticultură": 3,
    "Agronomie": 3,
    "Zootehnie": 3,
    "Inginerie agricolă": 3,
    "Silvicultură": 3,
    "Știința mediului": 3,
    "Protecția mediului": 3,
    # Nivel 4
    "Drept": 4,
    "Administrație publică": 4,
    "Științe administrative": 4,
    "Inginerie": 4,
    "Automatică și calculatoare": 4,
    "Informatică": 4,
    "Cibernetică": 4,
    "Statistică": 4,
    "Electronică": 4,
    "Electrotehnică": 4,
    "Construcții": 4,
    "Arhitectură": 4,
    # Nivel 5
    "Medicină": 5,
    "Medicină dentară": 5,
    "Farmacie": 5,
    "Asistență medicală generală – AMG": 5,
    "Moașe": 5,
    "Kinetoterapie / Balneofiziokinetoterapie": 5,
    "Nutriție și dietetică": 5,
    "Științe biomedicale": 5,
}

# Grile fixe pe [min_p, max_p, pret_n1, pret_n2, pret_n3, pret_n4, pret_n5]
GRILE_COMPLEXE = {
    "Licență": [
        (30, 35, 1200, 1250, 1300, 1400, 1500),
        (36, 60, 1500, 1600, 1700, 1800, 1950),
        (61, 80, 1800, 1900, 2000, 2150, 2300),
        (81, 100, 2000, 2150, 2300, 2450, 2600),
        (101, 120, 2250, 2400, 2550, 2700, 2900),
        (121, 150, 2550, 2750, 2950, 3150, 3400),
    ],
    "Disertație": [
        (30, 35, 1300, 1350, 1400, 1500, 1600),
        (36, 60, 1600, 1700, 1800, 1900, 2050),
        (61, 80, 1900, 2000, 2100, 2250, 2400),
        (81, 100, 2150, 2300, 2400, 2550, 2700),
        (101, 120, 2400, 2550, 2700, 2850, 3000),
        (121, 150, 2700, 2900, 3050, 3200, 3400),
    ],
    "Lucrare de grad": [
        (30, 35, 1250, 1350, 1350, 1450, 1550),
        (36, 60, 1550, 1650, 1750, 1850, 2000),
        (61, 80, 1850, 1950, 2050, 2200, 2350),
        (81, 100, 2050, 2200, 2350, 2500, 2650),
    ],
}

GRILE_SIMPLE = {
    "Eseu": [
        (5, 10, 150),
        (11, 15, 200),
        (16, 20, 275),
        (21, 25, 350),
        (26, 30, 450),
    ],
    "Proiect facultate": [
        (10, 15, 250),
        (16, 20, 300),
        (21, 30, 400),
        (31, 40, 500),
        (41, 50, 600),
        (51, 60, 700),
    ],
    "Articol științific": [
        (5, 8, 300),
        (9, 12, 400),
        (13, 16, 500),
        (17, 20, 600),
        (21, 25, 700),
        (26, 30, 850),
    ],
}

CONTINUT_COEF = {
    "Corectură + verificare": 0.30,
    "Doar partea teoretică": 0.40,
    "Doar partea practică": 0.60,
    "Lucrare completă": 1.00,
}

URGENTA_COEF = {
    "Standard – peste 30 zile": 1.00,
    "Normal – 15–30 zile": 1.08,
    "Urgent – 7–14 zile": 1.20,
    "Critic – sub 7 zile": 1.35,
}

# ==========================================
# 3. Formular Dinamic
# ==========================================

lucrari_salvate = []

with st.form("calculator_form"):
    for i in range(st.session_state.numar_lucrari):
        st.markdown(
            f"<h3 class='section-title'>Lucrarea #{i+1}</h3>",
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            tip_sel = st.selectbox(
                f"Tip Lucrare #{i+1}:",
                [
                    "Licență",
                    "Disertație",
                    "Lucrare de grad",
                    "Eseu",
                    "Proiect facultate",
                    "Articol științific",
                    "Teză de Doctorat",
                ],
                key=f"tip_{i}",
            )
            spec_sel = st.selectbox(
                f"Specializare #{i+1}:",
                sorted(list(NIVELURI_SPECIALIZARI.keys())),
                key=f"spec_{i}",
            )

        with col2:
            pagini_sel = st.number_input(
                f"Număr Pagini #{i+1}:",
                min_value=1,
                max_value=300,
                value=35,
                step=1,
                key=f"pag_{i}",
            )
            tema_introdusa = st.text_input(
                f"Tema lucrării #{i+1} (Opțional):",
                placeholder="Ex: Strategii de marketing...",
                key=f"tema_{i}",
            )

        if tip_sel == "Teză de Doctorat":
            st.markdown(
                "<div class='info-box'>⚠️ Tezele de doctorat se evaluează individual în funcție de domeniu, volum, metodologie și complexitate. (De la 4.000 lei → ofertă personalizată)</div>",
                unsafe_allow_html=True,
            )

        col3, col4 = st.columns(2)
        with col3:
            continut_sel = st.selectbox(
                f"Tip Conținut #{i+1}:",
                list(CONTINUT_COEF.keys()),
                index=3,
                key=f"cont_{i}",
            )
        with col4:
            urgenta_sel = st.selectbox(
                f"Termen Predare #{i+1}:",
                list(URGENTA_COEF.keys()),
                index=0,
                key=f"urg_{i}",
            )

        st.markdown(
            f"**Module suplimentare pentru Lucrarea #{i+1} (opțional):**"
        )
        c1, c2, c3 = st.columns(3)
        with c1:
            opt_qgis = st.checkbox("Hărți tematice + QGIS", key=f"qgis_{i}")
            opt_spss = st.checkbox(
                "Analiză statistică SPSS", key=f"spss_{i}"
            )
        with c2:
            opt_python = st.checkbox(
                "Aplicație / programare Python", key=f"py_{i}"
            )
            opt_wp = st.checkbox("Site WordPress", key=f"wp_{i}")
        with c3:
            opt_pachet = st.checkbox(
                "Pachet susținere (PPT + Discurs) - INCLUS (0 lei)",
                value=True,
                key=f"pachet_{i}",
            )

        lucrari_salvate.append(
            {
                "tip": tip_sel,
                "spec": spec_sel,
                "tema": tema_introdusa if tema_introdusa else "Nespecificată",
                "pagini": pagini_sel,
                "continut": continut_sel,
                "urgenta": urgenta_sel,
                "module": {
                    "qgis": opt_qgis,
                    "spss": opt_spss,
                    "python": opt_python,
                    "wordpress": opt_wp,
                    "pachet": opt_pachet,
                },
            }
        )

        if i < st.session_state.numar_lucrari - 1:
            st.markdown(
                "<hr style='border:1px dashed #e2e8f0'/>", unsafe_allow_html=True
            )

    submit_calcul = st.form_submit_button("GENEREAZĂ CALCULUL DE PREȚ")

# ==========================================
# 4. Logica de Calcul & Afișare Deviz
# ==========================================

if submit_calcul:
    suma_lucrari_individuale = 0
    detalii_afisare_lucrari = ""

    for idx, lucrare in enumerate(lucrari_salvate):
        tip = lucrare["tip"]

        if tip == "Teză de Doctorat":
            detalii_afisare_lucrari += (
                f"🔹 <b>Lucrarea #{idx+1}</b> (Teză de Doctorat)<br/>"
                f"• Specializare: <i>{lucrare['spec']}</i><br/>"
                f"• Statut: <b>Ofertă personalizată (Evaluare de la 4.000 lei)</b><br/><br/>"
            )
            continue

        pagini = lucrare["pagini"]
        nivel = NIVELURI_SPECIALIZARI[lucrare["spec"]]
        pret_baza_lucrare = None

        if tip in GRILE_COMPLEXE:
            tabela = GRILE_COMPLEXE[tip]
            for tuple_row in tabela:
                min_p, max_p = tuple_row[0], tuple_row[1]
                if min_p <= pagini <= max_p:
                    pret_baza_lucrare = tuple_row[nivel + 1]
                    break
        elif tip in GRILE_SIMPLE:
            tabela = GRILE_SIMPLE[tip]
            for min_p, max_p, pret in tabela:
                if min_p <= pagini <= max_p:
                    pret_baza_lucrare = pret
                    break

        if pret_baza_lucrare is None:
            detalii_afisare_lucrari += (
                f"🔹 <b>Lucrarea #{idx+1}</b> ({tip})<br/>"
                f"• Pagini: {pagini} pag. | Specializare: <i>{lucrare['spec']}</i><br/>"
                f"• Statut: <b>Ofertă personalizată (Volum peste grila standard)</b><br/><br/>"
            )
            continue

        # Aplicare Tip Conținut și Urgență
        coef_continut = CONTINUT_COEF[lucrare["continut"]]
        coef_urgenta = URGENTA_COEF[lucrare["urgenta"]]

        pret_inainte_module = pret_baza_lucrare * coef_continut * coef_urgenta

        # Ajustare Corectură (prag minim 200 lei)
        if lucrare["continut"] == "Corectură + verificare":
            if pret_inainte_module < 200:
                pret_inainte_module = 200

        # Calcul Module Opționale
        cost_module = 0
        is_peste_60 = pagini > 60
        mod_list = []

        if lucrare["module"]["qgis"]:
            cost_q = 200 if is_peste_60 else 150
            cost_module += cost_q
            mod_list.append(f"Hărți QGIS (+{cost_q} lei)")

        if lucrare["module"]["spss"]:
            cost_s = 400 if is_peste_60 else 300
            cost_module += cost_s
            mod_list.append(f"Analiză SPSS (+{cost_s} lei)")

        if lucrare["module"]["python"]:
            cost_py = 400 if is_peste_60 else 300
            cost_module += cost_py
            mod_list.append(f"Aplicație Python (+{cost_py} lei)")

        if lucrare["module"]["wordpress"]:
            cost_wp = 400 if is_peste_60 else 300
            cost_module += cost_wp
            mod_list.append(f"Site WordPress (+{cost_wp} lei)")

        if lucrare["module"]["pachet"]:
            mod_list.append("PACHET SUSȚINERE (PPT + Discurs) - INCLUS (0 lei)")

        pret_lucrare_total = pret_inainte_module + cost_module
        suma_lucrari_individuale += pret_lucrare_total

        text_module = (
            f"• Module suplimentare: {', '.join(mod_list)}<br/>"
            if mod_list
            else "• Module suplimentare: Fără module opționale<br/>"
        )

        detalii_afisare_lucrari += (
            f"🔹 <b>Lucrarea #{idx+1}</b> ({tip})<br/>"
            f"• Specializare: <i>{lucrare['spec']}</i> | Temă: <i>{lucrare['tema']}</i><br/>"
            f"• Volum: {pagini} pagini | Conținut: {lucrare['continut']}<br/>"
            f"• Predare: {lucrare['urgenta']}<br/>"
            f"{text_module}"
            f"• <b>Subtotal: {round(pret_lucrare_total)} lei</b><br/><br/>"
        )

    # Calcul Discount de Volum
    nr_lucrari = len(lucrari_salvate)
    reducere_procent = 0

    if nr_lucrari == 2:
        reducere_procent = 10
    elif nr_lucrari >= 3:
        reducere_procent = 15

    pret_final = suma_lucrari_individuale * (1 - reducere_procent / 100)
    subtotal_rotund = round(suma_lucrari_individuale)
    pret_final_rotund = round(pret_final)

    if reducere_procent > 0:
        randuri_pret = (
            f"<tr><td>Suma inițială:</td>"
            f"<td style='text-align:right; text-decoration: line-through; color: #ef4444; font-size: 1.1rem;'>{subtotal_rotund} lei</td></tr>"
            f"<tr><td>Discount de volum ({reducere_procent}%):</td>"
            f"<td style='text-align:right; color:#22c55e;'>-{subtotal_rotund - pret_final_rotund} lei</td></tr>"
            f"<tr style='font-size: 1.6rem; font-weight: bold; color: #ffffff;'><td style='padding-top:10px;'>PREȚ FINAL:</td>"
            f"<td style='text-align:right; padding-top:10px; color: #cf9e42;'>{pret_final_rotund} RON</td></tr>"
        )
    else:
        randuri_pret = (
            f"<tr style='font-size: 1.6rem; font-weight: bold; color: #ffffff;'><td style='padding-top:10px;'>PREȚ TOTAL ESTIMAT:</td>"
            f"<td style='text-align:right; padding-top:10px; color: #cf9e42;'>{pret_final_rotund} RON</td></tr>"
        )

    servicii_incluse_html = (
        '<div class="included-services">'
        '<h4>SERVICII INCLUSE ÎN PACHET:</h4>'
        '<ul>'
        '<li><b>✓ Structură academică:</b> Elaborarea cuprinsului și structurii conform ghidului facultății și cerințelor coordonatorului.</li>'
        '<li><b>✓ Metodologie:</b> Stabilirea scopului, obiectivelor, ipotezelor și designului de cercetare adaptat temei.</li>'
        '<li><b>✓ Instrument de cercetare:</b> Conceperea și structurarea chestionarului (dacă metodologia o impune).</li>'
        '<li><b>✓ Documentare academică:</b> Identificarea și integrarea surselor academice relevante și actuale.</li>'
        '<li><b>✓ Redactare & Tehnoredactare:</b> Formatare completă (fonturi, paragrafe, margini, numerotare, tabele, bibliografie).</li>'
        '<li><b>✓ Predare etapizată:</b> Transmiterea materialelor pe capitole pentru obținerea de feedback parțial.</li>'
        '<li><b>✓ PACHET SUSȚINERE (INCLUS - 0 lei):</b> Prezentare PowerPoint profesională + Discurs Word structurat pe slide-uri.</li>'
        '<li><b>✓ Modificări și corecturi:</b> Corecturile solicitate de coordonator pe parcurs sunt incluse în limita temei și structurii inițial agreate.</li>'
        '</ul>'
        '</div>'
    )

    final_card_html = (
        f'<div class="result-box">'
        f'<h3 style="color: #cf9e42; margin-top: 0; font-family: \'Georgia\', serif; border-bottom: 1px solid #cf9e42; padding-bottom: 5px;">Deviz Estimativ Rezultat</h3>'
        f'<p style="font-size: 0.95rem; line-height: 1.4; color: #f1f5f9;">{detalii_afisare_lucrari}</p>'
        f'{servicii_incluse_html}'
        f'<hr style="border: 0; border-top: 2px solid #cf9e42; margin: 20px 0;" />'
        f'<table style="width:100%; font-size: 1.05rem; color: white;">{randuri_pret}</table>'
        f'<a href="https://m.me/" target="_blank" class="fb-button">💬 Trimite comanda pe Facebook Messenger</a>'
        f'</div>'
    )

    st.markdown(final_card_html, unsafe_allow_html=True)
