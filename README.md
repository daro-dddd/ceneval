# EGEL Plus ISOFT - Simulador & Asistente Pedagógico (PWA)

Aplicación web progresiva (PWA) con backend en **Python (Flask)** diseñada con enfoque riguroso de **accesibilidad cognitiva y aprendizaje sin sobrecarga mental** para estudiar y simular el examen **EGEL Plus en Ingeniería de Software (ISOFT)** y el módulo transversal de **Comprensión Lectora**, conforme a las guías oficiales del CENEVAL.

---

## ✨ Características Principales

1. **Experiencia Anti-Saturación Cognitiva (UX/UI Crítico):**
   - **Estrictamente una pregunta a la vez** en pantalla (modo tarjeta paso a paso).
   - Cero ruido visual ni listas abrumadoras interminables.
   - Panel de lectura cómodo y colapsable para textos de casos y comprensión lectora.
   - Navegación por teclado accesible (`1`/`2`/`3` o `A`/`B`/`C` y `Enter`).
2. **Rigor Ceneval (3 opciones por reactivo: A, B, C):**
   - Justificación técnica detallada tanto para la respuesta correcta como para los distractores.
   - Concepto clave y referencia bibliográfica oficial (Pressman, Sommerville, Kruchten, Nielsen, Ceneval).
   - Asistente Pedagógico con consultas adicionales (analogías cotidianas, tips mnemotécnicos, ejemplos en la industria).
3. **4 Modalidades de Examen (30 reactivos cada una):**
   - 💻 **Simulador Disciplinar ISOFT (30 reactivos):** Áreas 1 (Análisis), 2 (Diseño), 3 (Desarrollo) y 4 (Gestión).
   - 📖 **Simulador de Comprensión Lectora (30 reactivos):** Ámbitos de estudio, literario y participación social.
   - 🏆 **Simulador Integral EGEL Plus (30 reactivos mixtos):** 18 reactivos disciplinares + 12 de comprensión lectora.
   - 🎯 **Práctica por Área Específica (30 reactivos):** 100% enfocado en el área que elijas para reforzar temas débiles.
4. **Pantalla de Resultados y Diagnóstico:**
   - Puntuación (ej. 24 / 30) y clasificación según la escala oficial CENEVAL (*Sobresaliente*, *Satisfactorio*, *Aún no satisfactorio*).
   - Desglose porcentual por áreas temáticas.
   - **Modo "Revisar reactivos fallados":** Permite repasar únicamente las preguntas erradas una a una sin estrés.
5. **Progressive Web App (PWA) 100% Instalable:**
   - `manifest.json` y Service Worker (`sw.js`) con soporte de caché y uso sin conexión.
   - Logotipo geométrico vectorial SVG y variantes PNG (192x192 y 512x512).
   - Soporte nativo para Modo Claro y Modo Oscuro con persistencia automática.

---

## 🚀 Instrucciones de Ejecución Local

### 1. Requisitos Previos
Tener instalado Python 3.9 o superior y las dependencias (Flask y Pillow ya están en tu entorno):

```bash
pip install -r requirements.txt
```

### 2. Iniciar el Servidor
En la terminal o PowerShell, en la raíz del proyecto, ejecuta:

```bash
python app.py
```

### 3. Abrir en el Navegador
Abre tu navegador (Google Chrome, Microsoft Edge, Firefox, Brave, Safari) en:

```
http://127.0.0.1:5000
```

### 4. Instalación como PWA (App de Escritorio / Móvil)
- En **Google Chrome / Microsoft Edge** en tu PC: Haz clic en el botón **"Instalar App"** en la barra superior o en el icono de instalación (pantalla con flecha) en la barra de direcciones del navegador.
- En **Móviles Android / iOS**: Pulsa en el menú del navegador "Añadir a la pantalla de inicio" o "Instalar aplicación".
- La app se abrirá en su propia ventana sin barra de direcciones, con comportamiento nativo instantáneo.

---

## 📂 Estructura Limpia del Proyecto

```
Ceneval/
├── app.py                   # Servidor backend Flask y endpoints de la API
├── questions_bank.py        # Banco de 160 reactivos Ceneval y motor de verificación
├── requirements.txt         # Dependencias Python
├── README.md                # Documentación de uso y arquitectura
├── templates/
│   └── index.html           # Plantilla HTML5 semántica y accesible
└── static/
    ├── css/
    │   └── style.css        # CSS responsivo con variables de tema claro/oscuro
    ├── js/
    │   └── app.js           # Lógica frontend Vanilla JS paso a paso
    ├── icons/
    │   ├── logo.svg         # Isotipo minimalista vectorial
    │   ├── icon-192.png     # Icono PWA estándar 192x192
    │   └── icon-512.png     # Icono PWA alta resolución 512x512
    ├── manifest.json        # Configuración estándar PWA
    └── sw.js                # Service Worker para caché y soporte offline
```
