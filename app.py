"""
Servidor Flask - Simulador EGEL Plus ISOFT y Comprensión Lectora
Desarrollado con arquitectura limpia, bajo acoplamiento y enfoque anti-saturación cognitiva.
"""

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import questions_bank as qb
import official_references as oref

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['JSON_AS_ASCII'] = False

# Áreas oficiales del examen según la Guía CENEVAL EGEL Plus ISOFT
AREAS_INFO = [
    {
        "id": "area_1",
        "name": "Área 1: Análisis de Sistemas de Software",
        "short_name": "Análisis de Sistemas",
        "icon": "clipboard-check",
        "reactivos": 31,
        "description": "1.1 Tipos de requerimientos (12), 1.2 Obtención, análisis, priorización y validación (9), 1.3 Documentación de requerimientos (10). Estándares ISO/IEC/IEEE 29148 y Wiegers & Hokanson."
    },
    {
        "id": "area_2",
        "name": "Área 2: Diseño de Sistemas de Software",
        "short_name": "Diseño de Sistemas",
        "icon": "layout",
        "reactivos": 33,
        "description": "2.1 Diseño arquitectónico (10), 2.2 Diseño de módulos, componentes y datos (16), 2.3 Diseño de interfaces (7). 4+1 Vistas (Kruchten), Heurísticas de Nielsen (2024), Date y Harrington."
    },
    {
        "id": "area_3",
        "name": "Área 3: Desarrollo de Sistemas de Software",
        "short_name": "Desarrollo de Software",
        "icon": "code",
        "reactivos": 49,
        "description": "3.1 Lenguajes de desarrollo (10), 3.2 Paradigmas (10), 3.3 Entornos (10), 3.4 Gestión de datos (9), 3.5 Plataformas (10). SQL (Beaulieu), POO/Funcional (Gabbrielli), Git y Algoritmos."
    },
    {
        "id": "area_4",
        "name": "Área 4: Gestión de Proyectos de Software",
        "short_name": "Gestión de Proyectos",
        "icon": "briefcase",
        "reactivos": 30,
        "description": "4.1 Tiempos, costos, recursos y riesgo (8), 4.2 Calidad de software (10), 4.3 Metodologías de desarrollo (12). Scrum (Schwaber & Sutherland), RUP (Booch), XP (Wells), PMBOK 7ma ed. y COCOMO."
    },
    {
        "id": "lectura",
        "name": "Lenguaje y Comunicación: Comprensión Lectora",
        "short_name": "Comprensión Lectora",
        "icon": "book-open",
        "reactivos": 30,
        "description": "1.1 Ámbito de estudio (12), 1.2 Ámbito literario (12), 1.3 Ámbito de participación social (6). Identificación, interpretación y evaluación crítica."
    },
    {
        "id": "redaccion",
        "name": "Lenguaje y Comunicación: Redacción Indirecta",
        "short_name": "Redacción Indirecta",
        "icon": "edit-3",
        "reactivos": 30,
        "description": "2.1 Ámbito de estudio (15), 2.2 Ámbito de participación social (15). Dimensión comunicativa, dimensión gramatical y semántica, y dimensión ortográfica."
    }
]


@app.route('/')
def index():
    """Página principal de la aplicación PWA."""
    return render_template('index.html')


@app.route('/manifest.json')
def serve_manifest():
    """Servir manifest.json desde la raíz para compatibilidad total PWA."""
    return send_from_directory('static', 'manifest.json', mimetype='application/manifest+json')


@app.route('/sw.js')
def serve_sw():
    """Servir Service Worker con scope global '/'."""
    response = send_from_directory('static', 'sw.js', mimetype='application/javascript')
    # Prevenir caché del archivo de Service Worker en el navegador
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@app.route('/api/areas', methods=['GET'])
def get_areas():
    """Devuelve las áreas temáticas disponibles para el simulador."""
    return jsonify({
        "success": True,
        "areas": AREAS_INFO
    })


@app.route('/api/official-references', methods=['GET'])
def get_official_references():
    """Devuelve el catálogo oficial de normas, estructura CENEVAL y bibliografía sugerida."""
    return jsonify({
        "success": True,
        "standards": oref.STANDARDS_AND_NORMS,
        "exam_structure": oref.EXAM_STRUCTURE,
        "bibliography": oref.OFFICIAL_BIBLIOGRAPHY
    })


import exam_engine as ee


@app.route('/api/exam/start', methods=['POST'])
def start_exam():
    """
    Inicia una sesión de examen de 30 reactivos únicos y diferentes.
    Almacena la sesión en data/exams/exam_<id>.json.
    Parámetros JSON:
      - modality: 'disciplinar' | 'lectura' | 'integral' | 'area'
      - area_id (opcional): 'area_1', 'area_2', 'area_3', 'area_4', 'lectura', 'redaccion'
    """
    data = request.get_json(silent=True) or {}
    modality = data.get('modality', 'disciplinar')
    area_id = data.get('area_id', None)

    exam_session = ee.generate_unique_exam(modality=modality, area_id=area_id, count=30)
    questions = exam_session["client_questions"]
    exam_id = exam_session["exam_id"]

    modality_labels = {
        "disciplinar": "Simulador Disciplinar ISOFT (30 reactivos)",
        "lectura": "Simulador de Lenguaje y Comunicación (30 reactivos)",
        "integral": "Simulador Integral EGEL Plus (30 reactivos)",
        "area": f"Práctica por Área Específica (30 reactivos)"
    }

    return jsonify({
        "success": True,
        "exam_id": exam_id,
        "modality": modality,
        "modality_title": modality_labels.get(modality, "Simulador EGEL"),
        "total_questions": len(questions),
        "questions": questions
    })


@app.route('/api/exam/verify', methods=['POST'])
def verify_item():
    """
    Verifica la respuesta seleccionada por el estudiante y entrega
    la argumentación técnica pedagógica completa.
    Parámetros JSON:
      - exam_id: str (opcional)
      - question_id: str (ej. 'ISOFT-A1-01')
      - selected_index: int (0, 1 o 2)
    """
    data = request.get_json(silent=True) or {}
    exam_id = data.get('exam_id')
    question_id = data.get('question_id')
    selected_index = data.get('selected_index')

    if question_id is None or selected_index is None:
        return jsonify({"success": False, "error": "Parámetros incompletos"}), 400

    result = ee.verify_exam_answer(exam_id, question_id, int(selected_index))

    if "error" in result:
        return jsonify({"success": False, "error": result["error"]}), 404

    return jsonify({
        "success": True,
        "result": result
    })


@app.route('/api/exam/tutor-diagnostic', methods=['POST'])
def tutor_diagnostic():
    """
    Genera el diagnóstico personalizado del Tutor Pedagógico CENEVAL indicando
    exactamente en qué áreas y subáreas tiene que reforzar el alumno,
    junto con el plan de estudio y referencias bibliográficas específicas.
    """
    data = request.get_json(silent=True) or {}
    exam_id = data.get('exam_id')
    user_answers = data.get('user_answers', [])

    if not user_answers:
        return jsonify({"success": False, "error": "No se recibieron respuestas"}), 400

    diagnostic = ee.generate_tutor_diagnostic(exam_id, user_answers)

    return jsonify({
        "success": True,
        "diagnostic": diagnostic
    })


@app.route('/api/exams/history', methods=['GET'])
def get_exams_history():
    """Devuelve la lista de exámenes realizados guardados en data/exams/."""
    exams = []
    if os.path.exists(ee.EXAMS_DIR):
        for fname in sorted(os.listdir(ee.EXAMS_DIR), reverse=True)[:20]:
            if fname.endswith('.json'):
                try:
                    fpath = os.path.join(ee.EXAMS_DIR, fname)
                    with open(fpath, 'r', encoding='utf-8') as f:
                        edata = json.load(f)
                    exams.append({
                        "exam_id": edata.get("exam_id"),
                        "created_at": edata.get("created_at"),
                        "modality": edata.get("modality"),
                        "status": edata.get("status"),
                        "score": edata.get("score"),
                        "percentage": edata.get("percentage")
                    })
                except Exception:
                    pass

    return jsonify({
        "success": True,
        "exams": exams
    })


@app.route('/api/assistant/explain', methods=['POST'])
def assistant_explain():
    """
    Asistente pedagógico interactivo para resolver dudas adicionales del reactivo
    (explicación con analogía cotidiana, aclaración técnica profunda o tips mnemotécnicos).
    """
    data = request.get_json(silent=True) or {}
    question_id = data.get('question_id')
    query_type = data.get('query_type', 'analogy')  # 'analogy' | 'mnemonic' | 'practical'

    q = qb.ALL_QUESTIONS_BY_ID.get(question_id)
    if not q:
        return jsonify({"success": False, "error": "Pregunta no encontrada"}), 404

    correct_opt = q["options"][q["correct_index"]]
    key_concept = q["justification"].get("key_concept", "")

    # Respuestas pedagógicas estructuradas según el tipo de consulta
    if query_type == 'analogy':
        explanation = (
            f"💡 **Analogía para recordar este concepto:**\n\n"
            f"Imagina el concepto de *'{q['subarea']}'* como la construcción de un edificio seguro: "
            f"la opción correcta (*{correct_opt}*) es la viga maestra de carga que garantiza la estabilidad bajo la norma técnica, "
            f"mientras que las otras opciones son acabados estéticos o elementos que no soportan la estructura requerida.\n\n"
            f"**Recuerda la regla de oro:** {key_concept}"
        )
    elif query_type == 'mnemonic':
        explanation = (
            f"🧠 **Estrategia Mnemotécnica CENEVAL:**\n\n"
            f"Para este tipo de preguntas en *{q['area_name']}*, fíjate en las palabras clave del enunciado: "
            f"busca siempre la relación directa con el estándar formal ({q['justification'].get('reference', 'Norma Oficial')}).\n\n"
            f"**Clave mental:** {key_concept}"
        )
    else:
        explanation = (
            f"🛠️ **Aplicación Práctica en la Industria:**\n\n"
            f"En proyectos de software reales, dominar *{q['subarea']}* evita sobrecostos y vulnerabilidades graves. "
            f"Al diseñar o implementar este componente, el estándar de la industria exige aplicar: *{correct_opt}*.\n\n"
            f"**Fundamento técnico:** {q['justification']['correct']}"
        )

    return jsonify({
        "success": True,
        "explanation": explanation
    })


import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

if __name__ == '__main__':
    # Ejecución local en el puerto 5000
    print("=================================================================")
    print("   [EGEL Plus ISOFT] Simulador & Comprension Lectora (PWA)       ")
    print("   Servidor iniciado en: http://127.0.0.1:5000                   ")
    print("=================================================================")
    app.run(host='127.0.0.1', port=5000, debug=False)

