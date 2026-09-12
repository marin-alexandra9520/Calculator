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
    
    /* Avertisment Doctorat */
    .doctorat-box {
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
    
    /* Buton Messenger */
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
# 2. Date și Coeficienți de Calcul
# ==========================================

SPECIALIZARI = {
    # Nivel 1
    "Administrarea afacerilor": 1.00,
    "Management": 1.00,
    "Marketing": 1.00,
    "Turism": 1.00,
    "Comerț": 1.00,
    "Economie": 1.00,
    "Sport / Educație fizică și sport": 1.00,
    "Comunicare și relații publice": 1.00,
    "Științele comunicării": 1.00,
    "Jurnalism": 1.00,
    # Nivel 2
    "Geografie": 1.10,
    "Pedagogie": 1.10,
    "PIPP – Pedagogia învățământului primar și preșcolar": 1.10,
    "Psihopedagogie": 1.10,
    "Științele educației": 1.10,
    "Sociologie": 1.10,
    "Asistență socială": 1.10,
    "Istorie": 1.10,
    "Filosofie": 1.10,
    "Științe politice": 1.10,
    # Nivel 3
    "Contabilitate": 1.20,
    "Finanțe": 1.20,
    "Finanțe-Bănci": 1.20,
    "Economie și afaceri internaționale": 1.20,
    "Biologie": 1.20,
    "Ecologie": 1.20,
    "Horticultură": 1.20,
    "Agronomie": 1.20,
    "Zootehnie": 1.20,
    "Inginerie agricolă": 1.20,
    "Silvicultură": 1.20,
    "Știința mediului": 1.20,
    "Protecția mediului": 1.20,
    # Nivel 4
    "Drept": 1.30,
    "Administrație publică": 1.30,
    "Științe administrative": 1.30,
    "Inginerie": 1.30,
    "Automatică și calculatoare": 1.30,
    "Informatică": 1.30,
    "Cibernetică": 1.30,
    "Statistică": 1.30,
    "Electronică": 1.30,
    "Electrotehnică": 1.30,
    "Construcții": 1.30,
    "Arhitectură": 1.30,
    # Nivel 5
    "Medicină": 1.40,
    "Medicină dentară": 1.40,
    "Farmacie": 1.40,
    "Asistență medicală generală – AMG": 1.40,
    "Moașe": 1.40,
    "Kinetoterapie / Balneofiziokinetoterapie": 1.40,
    "Nutriție și dietetică": 1.40,
    "Științe biomedicale": 1.40,
}

TABELE_PRET = {
    "Licență / lucrare de grad": [
        (30, 35, 1200),
        (36, 60, 1500),
        (61, 80, 1800),
        (81, 100, 2000),
        (101, 120, 2300),
        (121, 150, 2700),
    ],
    "Disertație": [
        (30, 35, 1400),
        (36, 60, 1750),
        (61, 80, 2050),
        (81, 100, 2300),
        (101, 120, 2650),
        (121, 150, 3100),
    ],
    "Eseu": [
        (5, 10, 200),
        (11, 15, 300),
        (16, 20, 400),
        (21, 25, 500),
        (26, 30, 600),
    ],
    "Proiect facultate": [
        (10, 15, 300),
        (16, 20, 400),
        (21, 30, 550),
        (31, 40, 700),
        (41, 50, 850),
    ],
    "Articol științific": [
        (5, 8, 350),
        (9, 12, 500),
        (13, 16, 650),
        (17, 20, 800),
        (21, 25, 950),
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
# 3. Construire Formular Dinamic
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
                    "Licență / lucrare de grad",
                    "Disertație",
                    "Eseu",
                    "Proiect facultate",
                    "Articol științific",
                    "Teză de Doctorat",
                ],
                key=f"tip_{i}",
            )
            spec_sel = st.selectbox(
                f"Specializare #{i+1}:",
                sorted(list(SPECIALIZARI.keys())),
                key=f"spec_{i}",
            )

        with col2:
            pagini_sel = st.number_input(
                f"Număr Pagini #{i+1}:",
                min_value=1,
                max_value=300,
                value=45,
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
                "<div class='doctorat-box'>⚠️ Tezele de doctorat se evaluează individual în funcție de domeniu, volum, metodologie și complexitate. (De la 4.000 lei → ofertă personalizată)</div>",
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
            opt_ppt = st.checkbox(
                "PPT + discurs susținere (+50 lei)", key=f"ppt_{i}"
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
                    "ppt": opt_ppt,
                },
            }
        )

        if i < st.session_state.numar_lucrari - 1:
            st.markdown(
                "<hr style='border:1px dashed #e2e8f0'/>", unsafe_allow_html=True
            )

    submit_calcul = st.form_submit_button("GENEREAZĂ CALCULUL DE PREȚ")

# ==========================================
# 4. Logica de Calcul și Afișare Deviz
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
        tabela = TABELE_PRET.get(tip, [])
        pret_baza_nivel1 = None

        for min_p, max_p, pret in tabela:
            if min_p <= pagini <= max_p:
                pret_baza_nivel1 = pret
                break

        if pret_baza_nivel1 is None:
            detalii_afisare_lucrari += (
                f"🔹 <b>Lucrarea #{idx+1}</b> ({tip})<br/>"
                f"• Pagini: {pagini} pag. | Specializare: <i>{lucrare['spec']}</i><br/>"
                f"• Statut: <b>Ofertă personalizată (Volum peste grila standard)</b><br/><br/>"
            )
            continue

        # Formulă Calcul
        coef_spec = SPECIALIZARI[lucrare["spec"]]
        coef_continut = CONTINUT_COEF[lucrare["continut"]]
        coef_urgenta = URGENTA_COEF[lucrare["urgenta"]]

        pret_baza = pret_baza_nivel1 * coef_spec
        pret_continut = pret_baza * coef_continut
        pret_urgenta = pret_continut * coef_urgenta

        # Praguri module (≤60 sau >60 pagini)
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

        if lucrare["module"]["ppt"]:
            cost_module += 50
            mod_list.append("PPT + Discurs (+50 lei)")

        pret_lucrare_inainte_discount = pret_urgenta + cost_module
        suma_lucrari_individuale += pret_lucrare_inainte_discount

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
            f"• <b>Subtotal: {round(pret_lucrare_inainte_discount)} lei</b><br/><br/>"
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

    st.markdown(
        f"""
        <div class="result-box">
            <h3 style="color: #cf9e42; margin-top: 0; font-family: 'Georgia', serif; border-bottom: 1px solid #cf9e42; padding-bottom: 5px;">Deviz Estimativ Rezultat</h3>
            <p style="font-size: 0.95rem; line-height: 1.4; color: #f1f5f9;">{detalii_afisare_lucrari}</p>
            <hr style="border: 0; border-top: 2px solid #cf9e42; margin: 15px 0;" />
            <table style="width:100%; font-size: 1.05rem; color: white;">
                {randuri_pret}
            </table>
            <a href="https://m.me/" target="_blank" class="fb-button">💬 Trimite comanda pe Facebook Messenger</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
