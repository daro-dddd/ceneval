"""
Motor de Exámenes Dinámicos, Almacenamiento en data/exams/ y Tutor Pedagógico CENEVAL
Garantiza que cada examen sea diferente, almacena sesiones en JSON y genera
diagnósticos precisos de áreas y subáreas a reforzar.
"""

import os
import json
import random
import time
import uuid
from datetime import datetime
import questions_bank as qb
from official_references import OFFICIAL_BIBLIOGRAPHY

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
EXAMS_DIR = os.path.join(DATA_DIR, 'exams')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')

os.makedirs(EXAMS_DIR, exist_ok=True)


def _load_history():
    """Carga el historial de reactivos preguntados recientemente para no repetirlos."""
    if not os.path.exists(HISTORY_FILE):
        return {"recent_question_ids": []}
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"recent_question_ids": []}


def _save_history(history):
    """Guarda el historial reciente."""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error guardando historial: {e}")


def _select_fresh_sample(question_pool, count, recent_ids):
    """
    Selecciona reactivos priorizando los que NO han aparecido en exámenes recientes.
    Si el conjunto de reactivos frescos es insuficiente, resetea y completa con los restantes.
    """
    fresh = [q for q in question_pool if q["id"] not in recent_ids]
    
    if len(fresh) >= count:
        selected = random.sample(fresh, count)
    else:
        # Usar todos los frescos disponibles y completar con el resto
        needed = count - len(fresh)
        remaining = [q for q in question_pool if q["id"] in recent_ids]
        random.shuffle(remaining)
        selected = fresh + remaining[:needed]
        random.shuffle(selected)
        
    return selected


def generate_unique_exam(modality="disciplinar", area_id=None, count=30):
    """
    Crea un examen garantizando que sea diferente:
    1. Prioriza preguntas no vistas recientemente.
    2. Mezcla aleatoriamente las opciones (A, B, C) de cada reactivo.
    3. Asigna un ID único de examen y lo guarda en data/exams/exam_<id>.json.
    """
    history = _load_history()
    recent_ids = set(history.get("recent_question_ids", []))

    raw_selected = []

    if modality == "disciplinar":
        s1 = _select_fresh_sample(qb.QUESTIONS_AREA_1, min(8, len(qb.QUESTIONS_AREA_1)), recent_ids)
        s2 = _select_fresh_sample(qb.QUESTIONS_AREA_2, min(8, len(qb.QUESTIONS_AREA_2)), recent_ids)
        s3 = _select_fresh_sample(qb.QUESTIONS_AREA_3, min(7, len(qb.QUESTIONS_AREA_3)), recent_ids)
        s4 = _select_fresh_sample(qb.QUESTIONS_AREA_4, min(7, len(qb.QUESTIONS_AREA_4)), recent_ids)
        combined = s1 + s2 + s3 + s4
        random.shuffle(combined)
        raw_selected = combined[:count]

    elif modality == "lectura":
        # 18 reactivos de Comprensión Lectora + 12 de Redacción Indirecta = 30 reactivos
        s_lec = _select_fresh_sample(qb.QUESTIONS_LECTURA, min(18, len(qb.QUESTIONS_LECTURA)), recent_ids)
        s_red = _select_fresh_sample(qb.QUESTIONS_REDACCION, min(12, len(qb.QUESTIONS_REDACCION)), recent_ids)
        combined = s_lec + s_red
        random.shuffle(combined)
        raw_selected = combined[:count]

    elif modality == "integral":
        s1 = _select_fresh_sample(qb.QUESTIONS_AREA_1, min(5, len(qb.QUESTIONS_AREA_1)), recent_ids)
        s2 = _select_fresh_sample(qb.QUESTIONS_AREA_2, min(5, len(qb.QUESTIONS_AREA_2)), recent_ids)
        s3 = _select_fresh_sample(qb.QUESTIONS_AREA_3, min(4, len(qb.QUESTIONS_AREA_3)), recent_ids)
        s4 = _select_fresh_sample(qb.QUESTIONS_AREA_4, min(4, len(qb.QUESTIONS_AREA_4)), recent_ids)
        pool_leng = qb.QUESTIONS_LECTURA + qb.QUESTIONS_REDACCION
        s_leng = _select_fresh_sample(pool_leng, min(12, len(pool_leng)), recent_ids)
        combined = s1 + s2 + s3 + s4 + s_leng
        random.shuffle(combined)
        raw_selected = combined[:count]

    elif modality == "area":
        target_group = qb.ALL_QUESTIONS.get(area_id, qb.QUESTIONS_AREA_1)
        raw_selected = _select_fresh_sample(target_group, min(count, len(target_group)), recent_ids)

    else:
        combined = qb.QUESTIONS_AREA_1 + qb.QUESTIONS_AREA_2 + qb.QUESTIONS_AREA_3 + qb.QUESTIONS_AREA_4
        raw_selected = _select_fresh_sample(combined, min(count, len(combined)), recent_ids)

    # Actualizar historial de reactivos recientes (máximo 120 en ventana deslizante)
    new_recent = [q["id"] for q in raw_selected] + list(recent_ids)
    history["recent_question_ids"] = new_recent[:120]
    _save_history(history)

    # Generar ID de sesión único
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    exam_id = f"EXAM_{timestamp_str}_{uuid.uuid4().hex[:6]}"

    # Mezclar aleatoriamente las opciones (A, B, C) de cada reactivo para que varíe en cada examen
    exam_questions_internal = []
    client_questions = []

    for idx, q in enumerate(raw_selected):
        orig_options = q["options"]
        orig_correct_idx = q["correct_index"]
        correct_text = orig_options[orig_correct_idx]

        # Crear lista con textos e índices originales
        indexed_opts = list(enumerate(orig_options))
        random.shuffle(indexed_opts)

        shuffled_options = [opt[1] for opt in indexed_opts]
        new_correct_idx = shuffled_options.index(correct_text)

        # Mapa para recuperar justificadores de distractores
        internal_item = {
            "number": idx + 1,
            "id": q["id"],
            "area_id": q["area_id"],
            "area_name": q["area_name"],
            "subarea": q["subarea"],
            "text": q.get("text", ""),
            "question": q["question"],
            "shuffled_options": shuffled_options,
            "correct_index": new_correct_idx,
            "original_item": q
        }
        exam_questions_internal.append(internal_item)

        # Lo que se entrega al frontend (sin revelar la respuesta correcta)
        client_questions.append({
            "number": idx + 1,
            "id": q["id"],
            "area_id": q["area_id"],
            "area_name": q["area_name"],
            "subarea": q["subarea"],
            "text": q.get("text", ""),
            "question": q["question"],
            "options": shuffled_options
        })

    # Guardar en archivo data/exams/exam_<id>.json
    exam_file_path = os.path.join(EXAMS_DIR, f"{exam_id}.json")
    exam_record = {
        "exam_id": exam_id,
        "created_at": datetime.now().isoformat(),
        "modality": modality,
        "area_id": area_id,
        "status": "in_progress",
        "total_questions": len(exam_questions_internal),
        "questions": [
            {
                "id": it["id"],
                "subarea": it["subarea"],
                "options": it["shuffled_options"],
                "correct_index": it["correct_index"]
            }
            for it in exam_questions_internal
        ]
    }

    try:
        with open(exam_file_path, 'w', encoding='utf-8') as f:
            json.dump(exam_record, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error guardando examen en disco: {e}")

    return {
        "exam_id": exam_id,
        "client_questions": client_questions,
        "exam_file_path": exam_file_path
    }


def verify_exam_answer(exam_id, question_id, selected_index):
    """
    Verifica la respuesta tomando en cuenta el orden específico de opciones del examen.
    """
    exam_file_path = os.path.join(EXAMS_DIR, f"{exam_id}.json")
    
    # Si existe el archivo del examen, verificar con su mapeo mezclado
    if os.path.exists(exam_file_path):
        try:
            with open(exam_file_path, 'r', encoding='utf-8') as f:
                exam_data = json.load(f)
            
            matching = next((item for item in exam_data.get("questions", []) if item["id"] == question_id), None)
            if matching:
                correct_idx = matching["correct_index"]
                shuffled_opts = matching["options"]
                is_correct = (selected_index == correct_idx)
                letters = ["A", "B", "C"]

                q_orig = qb.ALL_QUESTIONS_BY_ID.get(question_id)
                options_breakdown = []
                
                for i, opt_text in enumerate(shuffled_opts):
                    letter = letters[i]
                    if i == correct_idx:
                        explanation = q_orig["justification"]["correct"]
                        status = "correct"
                    else:
                        explanation = "Opción incorrecta según la fundamentación técnica y normativa de la guía CENEVAL."
                        # Buscar si coincide con alguna justificación original
                        if "distractors" in q_orig.get("justification", {}):
                            for orig_letter, dist_text in q_orig["justification"]["distractors"].items():
                                orig_opt_idx = {"A": 0, "B": 1, "C": 2}.get(orig_letter)
                                if orig_opt_idx is not None and orig_opt_idx < len(q_orig["options"]) and q_orig["options"][orig_opt_idx] == opt_text:
                                    explanation = dist_text
                                    break
                        status = "distractor"

                    options_breakdown.append({
                        "letter": letter,
                        "text": opt_text,
                        "status": status,
                        "explanation": explanation
                    })

                feedback_summary = (
                    f"¡Excelente! Has seleccionado la opción ({letters[selected_index]}), que es la respuesta correcta."
                    if is_correct else
                    f"Has seleccionado la opción ({letters[selected_index]}). Sin embargo, la respuesta correcta es la ({letters[correct_idx]}). Analicemos los motivos técnicos:"
                )

                return {
                    "question_id": question_id,
                    "is_correct": is_correct,
                    "selected_index": selected_index,
                    "correct_index": correct_idx,
                    "correct_letter": letters[correct_idx],
                    "feedback_summary": feedback_summary,
                    "options_breakdown": options_breakdown,
                    "key_concept": q_orig["justification"].get("key_concept", ""),
                    "reference": q_orig["justification"].get("reference", "Guía Oficial CENEVAL EGEL Plus.")
                }
        except Exception as e:
            print(f"Error verificando con archivo de examen: {e}")

    # Fallback si no hay exam_id
    return qb.verify_answer(question_id, selected_index)


def generate_tutor_diagnostic(exam_id, user_answers):
    """
    El Tutor Pedagógico CENEVAL analiza a detalle el desempeño del estudiante
    y le indica exactamente en qué áreas y subáreas TIENE QUE REFORZAR,
    con diagnóstico técnico de los fallos y recomendaciones bibliográficas oficiales.
    """
    total = len(user_answers)
    if total == 0:
        return {"error": "No hay respuestas para analizar"}

    correct_count = sum(1 for a in user_answers if a.get("isCorrect"))
    percentage = round((correct_count / total) * 100, 1)

    # Agrupar estadísticas por Área y por Subárea
    area_stats = {}
    failed_by_area = {}

    for item in user_answers:
        q = item["question"]
        is_ok = item.get("isCorrect", False)
        area_id = q.get("area_id", "disciplinar")
        area_name = q.get("area_name", "Ingeniería de Software")
        subarea = q.get("subarea", "Tema General")

        if area_name not in area_stats:
            area_stats[area_name] = {
                "area_id": area_id,
                "area_name": area_name,
                "total": 0,
                "correct": 0,
                "failed": 0,
                "subareas": {}
            }

        area_stats[area_name]["total"] += 1
        if is_ok:
            area_stats[area_name]["correct"] += 1
        else:
            area_stats[area_name]["failed"] += 1
            if area_name not in failed_by_area:
                failed_by_area[area_name] = []
            
            failed_by_area[area_name].append({
                "subarea": subarea,
                "question": q.get("question", ""),
                "key_concept": item.get("verificationData", {}).get("key_concept", ""),
                "reference": item.get("verificationData", {}).get("reference", "")
            })

        # Detalle de subárea
        if subarea not in area_stats[area_name]["subareas"]:
            area_stats[area_name]["subareas"][subarea] = {"total": 0, "correct": 0, "failed": 0}
        
        area_stats[area_name]["subareas"][subarea]["total"] += 1
        if is_ok:
            area_stats[area_name]["subareas"][subarea]["correct"] += 1
        else:
            area_stats[area_name]["subareas"][subarea]["failed"] += 1

    # Clasificar áreas que requieren refuerzo vs áreas dominadas
    areas_to_reinforce = []
    areas_mastered = []

    for a_name, stats in area_stats.items():
        pct = round((stats["correct"] / stats["total"]) * 100)
        stats["percentage"] = pct

        if stats["failed"] > 0 or pct < 80:
            # Esta área TIENE QUE REFORZARSE
            failed_subareas = []
            for sub_name, s_data in stats["subareas"].items():
                if s_data["failed"] > 0:
                    failed_subareas.append({
                        "name": sub_name,
                        "failed_count": s_data["failed"],
                        "total_count": s_data["total"],
                        "accuracy": round((s_data["correct"] / s_data["total"]) * 100)
                    })

            # Extraer recomendaciones específicas de bibliografía oficial
            area_id = stats["area_id"]
            suggested_books = OFFICIAL_BIBLIOGRAPHY.get(area_id, [
                "Guía Oficial CENEVAL EGEL Plus ISOFT (2024 / 2025)."
            ])[:3]

            # Sintetizar fallos de esta área
            mistakes = failed_by_area.get(a_name, [])
            concepts_to_review = list(set([m["key_concept"] for m in mistakes if m["key_concept"]]))[:3]

            areas_to_reinforce.append({
                "area_name": a_name,
                "area_id": area_id,
                "percentage": pct,
                "failed_count": stats["failed"],
                "total_count": stats["total"],
                "failed_subareas": failed_subareas,
                "concepts_to_review": concepts_to_review,
                "recommended_reading": suggested_books
            })
        else:
            areas_mastered.append({
                "area_name": a_name,
                "percentage": pct,
                "total_count": stats["total"]
            })

    # Mensaje pedagógico del tutor
    if correct_count == total:
        tutor_message = (
            "🌟 ¡Desempeño Impecable! Has respondido correctamente el 100% de los reactivos de esta sesión. "
            "Tu comprensión de los estándares de ingeniería de software y comprensión crítica es sobresaliente. "
            "No se detectaron áreas críticas de refuerzo en esta tanda; te recomiendo realizar otro examen aleatorio para abarcar más reactivos del banco."
        )
    elif len(areas_to_reinforce) > 0:
        area_names_str = ", ".join([f"'{a['area_name']}'" for a in areas_to_reinforce])
        tutor_message = (
            f"He evaluado con rigor tus 30 respuestas. Tu efectividad global fue del {percentage}%. "
            f"Para asegurar la acreditación con Testimonio Sobresaliente (D-SS), **tienes que reforzar en las siguientes áreas prioritarias:** {area_names_str}. "
            "A continuación te detallo las subáreas específicas donde se presentaron fallos y la bibliografía exacta que debes repasar:"
        )
    else:
        tutor_message = (
            f"¡Muy bien! Alcanzaste un {percentage}% de aciertos, superando el estándar satisfactorio del CENEVAL. "
            "Revisa los reactivos fallados para consolidar los conceptos clave."
        )

    diagnostic_result = {
        "exam_id": exam_id,
        "score": correct_count,
        "total": total,
        "percentage": percentage,
        "tutor_message": tutor_message,
        "areas_to_reinforce": areas_to_reinforce,
        "areas_mastered": areas_mastered,
        "area_stats": area_stats
    }

    # Guardar diagnóstico en el archivo de examen data/exams/exam_<id>.json
    if exam_id:
        exam_file_path = os.path.join(EXAMS_DIR, f"{exam_id}.json")
        if os.path.exists(exam_file_path):
            try:
                with open(exam_file_path, 'r', encoding='utf-8') as f:
                    exam_data = json.load(f)
                
                exam_data["status"] = "completed"
                exam_data["completed_at"] = datetime.now().isoformat()
                exam_data["score"] = correct_count
                exam_data["percentage"] = percentage
                exam_data["diagnostic"] = diagnostic_result

                with open(exam_file_path, 'w', encoding='utf-8') as f:
                    json.dump(exam_data, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error actualizando examen completado: {e}")

    return diagnostic_result
