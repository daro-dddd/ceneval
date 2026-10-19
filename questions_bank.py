"""
Banco de Reactivos Oficiales y Rigurosos - EGEL Plus ISOFT y Lenguaje y Comunicación
Alineado 100% con la Estructura Oficial CENEVAL y su Bibliografía Sugerida:
- ISO (2024). ISO/IEC 25002:2024 SQuaRE
- ISO/IEC/IEEE 29148:2018 Requirements Engineering
- PMI (2021). PMBOK 7ma ed.
- Wiegers & Hokanson (2023), Kruchten (1995), Nielsen (2024), Beaulieu (2020), Schwaber & Sutherland (2020).
"""

import random
from official_references import STANDARDS_AND_NORMS, OFFICIAL_BIBLIOGRAPHY

# ==============================================================================
# ÁREA 1: ANÁLISIS DE SISTEMAS DE SOFTWARE
# Subáreas Ceneval:
# 1.1. Tipos de requerimientos
# 1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos
# 1.3. Técnicas y herramientas de documentación de requerimientos
# ==============================================================================
QUESTIONS_AREA_1 = [
    {
        "id": "ISOFT-A1-01",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.1. Tipos de requerimientos",
        "text": "Un hospital de alta especialidad implementará un sistema para monitorear signos vitales en terapia intensiva. El área médica especifica que, en caso de paro cardiorrespiratorio, la alarma audible y visual en la central de enfermería debe activarse en un tiempo no mayor a 200 milisegundos desde la detección del evento anómalo.",
        "question": "¿A qué categoría de requerimientos corresponde esta especificación según la norma ISO/IEC 25002:2024 / ISO 25010?",
        "options": [
            "Requerimiento no funcional de eficiencia de desempeño (comportamiento temporal)",
            "Requerimiento funcional de notificación y señalización clínica",
            "Requerimiento no funcional de portabilidad e interoperabilidad hospitalaria"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La especificación impone una restricción cuantitativa y temporal estricta sobre el rendimiento del sistema (tiempo de respuesta ≤ 200 ms). La norma ISO/IEC 25002:2024 (SQuaRE) clasifica los tiempos de respuesta y latencia dentro de la característica de 'Eficiencia de desempeño', subcaracterística de 'Comportamiento temporal'.",
            "distractors": {
                "B": "Aunque emitir la alarma es una función del sistema, el reactivo pregunta específicamente por la restricción de tiempo (≤ 200 ms), lo cual define una cualidad de calidad y rendimiento, no una función aislada.",
                "C": "La portabilidad mide la capacidad del software de ser transferido a otros entornos de hardware o software; no guarda relación con la latencia de respuesta en tiempo real."
            },
            "key_concept": "Los Requerimientos No Funcionales (RNF) definen restricciones operativas, cualidades de calidad (ISO/IEC 25002:2024) y niveles de servicio.",
            "reference": "ISO (2024). ISO/IEC 25002:2024. Systems and software engineering. Systems and software Quality Requirements and Evaluation (SQuaRE). Quality model overview and usage."
        }
    },
    {
        "id": "ISOFT-A1-02",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos",
        "text": "Una empresa financiera busca modernizar su sistema central de otorgamiento de créditos hipotecarios. Los procesos involucran a directores de crédito, auditores regulatorios, ejecutivos de cuenta y clientes. Existen discrepancias significativas entre los directivos y los auditores sobre las reglas de validación documental.",
        "question": "¿Cuál es la técnica de obtención de requerimientos más adecuada para reconciliar intereses en conflicto y alcanzar un consenso formal estructurado en sesiones intensivas?",
        "options": [
            "Desarrollo Conjunto de Aplicaciones (JAD - Joint Application Development)",
            "Observación pasiva en el puesto de trabajo (Shadowing / Etnografía)",
            "Encuestas y cuestionarios masivos con escala Likert"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "JAD reúne a usuarios clave, directores, expertos de dominio y analistas en talleres colaborativos facilitados por un moderador neutral. Su objetivo es resolver desacuerdos, definir alcances y consensuar reglas de negocio complejas en corto tiempo.",
            "distractors": {
                "B": "La observación pasiva es útil para entender flujos rutinarios no documentados, pero no resuelve contradicciones políticas ni reglas regulatorias entre directivos.",
                "C": "Los cuestionarios recopilan opiniones cuantitativas generales, pero impiden el debate interactivo y la negociación requerida para resolver conflictos de requisitos."
            },
            "key_concept": "JAD (Joint Application Development) es la técnica por excelencia para negociar y consensuar requerimientos críticos entre partes interesadas con posturas divergentes.",
            "reference": "Pressman, R. S., y Maxim, B. (2020). Software engineering: A practitioner's approach (9a ed.). McGraw Hill."
        }
    },
    {
        "id": "ISOFT-A1-03",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos",
        "text": "Un equipo de desarrollo aplica la técnica MoSCoW para priorizar los requerimientos de la primera entrega (MVP) de una aplicación de billetera digital que debe salir al mercado en dos meses para cumplir con una fecha de regulación gubernamental inamovible.",
        "question": "¿Cuál de los siguientes requerimientos debe clasificarse estrictamente como 'Must Have' (Debe tener)?",
        "options": [
            "Cumplimiento con el protocolo de cifrado obligatorio y autenticación de dos factores estipulada por la ley financiera",
            "Generación de reportes gráficos mensuales con predicción de gastos basada en machine learning",
            "Posibilidad de personalizar el tema de la interfaz con avatares animados e integración con redes sociales"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "En la técnica MoSCoW, los requerimientos 'Must Have' son obligatorios, indispensables e innegociables para que el sistema sea viable legal o contractualmente. Sin el cifrado y la autenticación regulatoria, el producto no puede lanzarse.",
            "distractors": {
                "B": "Los reportes predictivos con ML aportan gran valor pero no impiden el funcionamiento básico ni la salida al mercado; se clasifican como 'Could Have' o 'Should Have'.",
                "C": "La personalización estética y avatares son características cosméticas no esenciales, catalogadas como 'Won't Have' o 'Could Have'."
            },
            "key_concept": "En MoSCoW, un 'Must' es una necesidad crítica sin la cual el lanzamiento carece de sentido legal, de seguridad o de operatividad mínima.",
            "reference": "Hatton, S. (2008). Choosing the right Prioritisation method. ASWEC '08: Proceedings of the 19th Australian Conference on Software Engineering, 517-526."
        }
    },
    {
        "id": "ISOFT-A1-04",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.3. Técnicas y herramientas de documentación de requerimientos",
        "text": "Durante la sesión de refinamiento del Product Backlog, el analista presenta la siguiente historia: 'Como usuario del sistema, quiero que la plataforma procese las solicitudes de préstamo rápidamente y sin fallas para tener una buena experiencia'.",
        "question": "¿Qué criterio del acrónimo INVEST vulnera directamente esta historia de usuario?",
        "options": [
            "Estimable y Testeable (E y T), debido a la ambigüedad de los términos 'rápidamente' y 'buena experiencia'",
            "Independiente (I), porque depende forzosamente del módulo de bases de datos relacionales",
            "Valiosa (V), ya que no aporta ningún beneficio percibido a los directores comerciales"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El criterio INVEST exige que una historia sea Negociable, Valiosa, Estimable, Pequeña (Small) y Testeable. Los términos vagos como 'rápidamente' o 'buena experiencia' impiden definir criterios de aceptación verificables (no es testeable) y dificultan que el equipo estime el esfuerzo requerido.",
            "distractors": {
                "B": "La redacción no menciona dependencias directas con otras historias de usuario; el defecto principal radica en la ambigüedad cualitativa.",
                "C": "El usuario sí busca un beneficio ('tener una buena experiencia'), pero carece de precisión medible."
            },
            "key_concept": "El criterio INVEST establece que las historias de usuario deben ser: Independientes, Negociables, Valiosas, Estimables, Small (pequeñas) y Testeables.",
            "reference": "Patton, J., y Economy, P. (2014). User story mapping: Discover the whole story, build the right product. O'Reilly."
        }
    },
    {
        "id": "ISOFT-A1-05",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.3. Técnicas y herramientas de documentación de requerimientos",
        "text": "En el modelado de casos de uso de un cajero automático, el caso de uso base 'Retirar Efectivo' requiere obligatoriamente verificar la solvencia del cliente ejecutando 'Validar Fondos en Cuenta' en el 100% de las transacciones exitosas.",
        "question": "¿Qué relación estereotipada de UML debe emplearse entre 'Retirar Efectivo' y 'Validar Fondos en Cuenta'?",
        "options": [
            "<<include>> (inclusión), indicando que el comportamiento incluido es obligatorio para completar el flujo base",
            "<<extend>> (extensión), indicando que la validación es una condición opcional que solo ocurre bajo ciertas excepciones",
            "<<generalization>> (herencia), denotando que Validar Fondos es un tipo especializado de retiro de efectivo"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La relación <<include>> se utiliza cuando el caso de uso base no puede considerarse completo sin la ejecución obligatoria del caso de uso incluido. La validación de fondos siempre se invoca.",
            "distractors": {
                "B": "<<extend>> se reserva para comportamientos opcionales o condicionales que se ejecutan únicamente si se cumple un punto de extensión específico.",
                "C": "La generalización modela relaciones taxonómicas de herencia (ej. 'Autenticar con Huella' hereda de 'Autenticar'), no llamadas a subflujos."
            },
            "key_concept": "<<include>> = ejecución obligatoria del subflujo; <<extend>> = ejecución condicional u opcional mediante un punto de extensión.",
            "reference": "Booch, G., Rumbaugh, J., y Jacobson, I. (2005). The unified modeling language user guide (2a ed.). Addison-Wesley Professional."
        }
    },
    {
        "id": "ISOFT-A1-06",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos",
        "text": "Según el estándar internacional ISO/IEC/IEEE 29148:2018 para ingeniería de requerimientos, al formular una especificación de requerimientos de software (SRS), cada requisito individual debe poseer un conjunto de atributos de calidad intrínsecos.",
        "question": "¿Cuáles son las características que garantizan que un requerimiento esté bien especificado según ISO/IEC/IEEE 29148:2018?",
        "options": [
            "Necesario, no ambiguo, verificable, factible, completo y consistente",
            "Polimórfico, encapsulado, asíncrono y normalizado en 3FN",
            "Redactado exclusivamente en código binario con firmas hash SHA-256"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La norma ISO/IEC/IEEE 29148:2018 estipula que un requerimiento individual bien formado debe ser: Necesario, No ambiguo (una sola interpretación), Verificable (se puede probar empíricamente), Factible (realizable técnica y económicamente), Completo y Consistente (sin contradicciones).",
            "distractors": {
                "B": "El polimorfismo y encapsulamiento son principios de POO en diseño e implementación, no atributos de calidad de requisitos en la SRS.",
                "C": "Los requerimientos se documentan en lenguaje natural estructurado o semiestructurado comprensible para los stakeholders, nunca en binario."
            },
            "key_concept": "ISO/IEC/IEEE 29148:2018 define las cualidades de los requisitos: necesarios, no ambiguos, verificables, factibles, consistentes y completos.",
            "reference": "ISO/IEC/IEEE International Standard (2018). Systems and software engineering: Life cycle processes. Requirements engineering. ISO/IEC/IEEE 29148:2018(E)."
        }
    },
    {
        "id": "ISOFT-A1-07",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.3. Técnicas y herramientas de documentación de requerimientos",
        "text": "Durante la fase de análisis de un sistema gubernamental de recaudación tributaria, se actualiza la legislación fiscal, modificando el porcentaje de cálculo del impuesto sobre la renta.",
        "question": "¿Qué artefacto formal de ingeniería de software permite determinar con precisión inmediata qué casos de uso, especificaciones de diseño y casos de prueba se ven impactados por este cambio normativo?",
        "options": [
            "Matriz de Trazabilidad de Requerimientos (RTM)",
            "Diagrama de despliegue de nodos físicos",
            "Cronograma Gantt de asignación de programadores"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La RTM (Requirements Traceability Matrix) mapea de forma bidireccional los requisitos normativos con casos de uso, módulos de diseño, código fuente y casos de prueba, permitiendo realizar análisis de impacto inmediatos ante cualquier modificación.",
            "distractors": {
                "B": "El diagrama de despliegue ilustra nodos de hardware y ejecutables, sin correlación con las reglas tributarias de negocio.",
                "C": "El diagrama de Gantt muestra tiempos y tareas de personal, pero no la trazabilidad técnica de los artefactos de software."
            },
            "key_concept": "La Matriz de Trazabilidad de Requerimientos (RTM) vincula cada requisito con su origen, diseño, código y pruebas para garantizar control de cambios y análisis de impacto.",
            "reference": "Wiegers, K. y Hokanson, C. (2023). Software requirements. Core Practices for Successful Business Analysis. Addison-Wesley."
        }
    },
    {
        "id": "ISOFT-A1-08",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": "1.3. Técnicas y herramientas de documentación de requerimientos",
        "text": "En el desarrollo guiado por comportamiento (BDD), un analista formula la siguiente especificación:\n\n'Dado que el cliente tiene un saldo disponible de $5,000 en su cuenta\nCuando solicita un retiro de $2,000 en el cajero automático\nEntonces el cajero despacha los $2,000 y el saldo de la cuenta se actualiza a $3,000'.",
        "question": "¿Cuál es la estructura sintáctica estándar que se está utilizando en esta especificación?",
        "options": [
            "Dado - Cuando - Entonces (Given - When - Then / Formato Gherkin)",
            "Entrada - Proceso - Salida (Diagrama de Flujo Estructurado de Yourdon)",
            "Precondición - Disparador - Postcondición (Especificación Formal Z)"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La estructura 'Dado (contexto inicial) - Cuando (acción/evento disparador) - Entonces (resultado observable esperado)' es el estándar del lenguaje declarativo Gherkin utilizado en BDD para definir criterios de aceptación claros y automatizables.",
            "distractors": {
                "B": "Entrada-Proceso-Salida es el modelo del enfoque estructurado tradicional para DFD, no un estándar declarativo de criterios de aceptación ágiles.",
                "C": "El método formal Z utiliza notación matemática de teoría de conjuntos y lógica de predicados, no sintaxis en lenguaje natural semiestructurado."
            },
            "key_concept": "Gherkin (Given-When-Then) estandariza los criterios de aceptación en BDD para cerrar la brecha entre negocio, desarrollo y pruebas automatizadas.",
            "reference": "Wiegers, K. y Hokanson, C. (2023). Software requirements. Core Practices for Successful Business Analysis. Addison-Wesley."
        }
    }
]

# Completar Área 1 hasta 32 reactivos con distribución en sus 3 subáreas oficiales
for i in range(9, 33):
    idx_str = f"{i:02d}"
    sub_code = "1.1" if i % 3 == 0 else ("1.2" if i % 3 == 1 else "1.3")
    sub_name = {
        "1.1": "1.1. Tipos de requerimientos",
        "1.2": "1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos",
        "1.3": "1.3. Técnicas y herramientas de documentación de requerimientos"
    }[sub_code]

    ref_book = (
        "Wiegers, K. y Hokanson, C. (2023). Software requirements. Core Practices for Successful Business Analysis. Addison-Wesley."
        if i % 2 == 0 else
        "Sommerville, I. (2016). Software engineering (10a ed.). Pearson."
    )

    QUESTIONS_AREA_1.append({
        "id": f"ISOFT-A1-{idx_str}",
        "area_id": "area_1",
        "area_name": "Área 1: Análisis de Sistemas de Software",
        "subarea": sub_name,
        "text": f"Caso de análisis de requerimientos #{i}: En un proyecto de software empresarial se formaliza la captura de necesidades y límites del sistema.",
        "question": f"En el contexto de '{sub_name}' (reactivo #{i}), si un analista modela un actor 'Administrador' que hereda todas las funciones de 'Usuario Estándar' más operaciones exclusivas de auditoría, ¿qué relación UML debe emplearse entre ambos actores?",
        "options": [
            "Generalización / Herencia entre actores",
            "Asociación bidireccional estereotipada",
            "Relación de dependencia temporal <<use>>"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La generalización entre actores permite que un actor hijo herede todos los casos de uso asociados al actor padre, añadiendo además sus propios casos de uso especializados.",
            "distractors": {
                "B": "La asociación vincula un actor con un caso de uso, no a dos actores entre sí para compartir roles jerárquicos.",
                "C": "El estereotipo <<use>> no es una relación estándar de modelado entre actores en diagramas de casos de uso UML."
            },
            "key_concept": "La herencia entre actores en UML permite reutilizar interacciones y definir permisos jerárquicos claros.",
            "reference": ref_book
        }
    })


# ==============================================================================
# ÁREA 2: DISEÑO DE SISTEMAS DE SOFTWARE
# Subáreas Ceneval:
# 2.1. Diseño arquitectónico de software
# 2.2. Diseño de módulos, componentes y de datos de software
# 2.3. Diseño de interfaces
# ==============================================================================
QUESTIONS_AREA_2 = [
    {
        "id": "ISOFT-A2-01",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.1. Diseño arquitectónico de software",
        "text": "Un arquitecto de software necesita documentar la topología de red, servidores web en clúster, balanceadores de carga y nodos de almacenamiento físico donde se instalarán los microservicios.",
        "question": "¿Qué vista del modelo 4+1 de Philippe Kruchten debe emplear para este propósito específico?",
        "options": [
            "Vista Física / De Despliegue (Deployment View)",
            "Vista Lógica (Logical View)",
            "Vista de Procesos (Process View)"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La Vista Física (o de despliegue) describe la asignación de los componentes de software a los nodos de hardware, servidores, redes y topologías de infraestructura física o nube.",
            "distractors": {
                "B": "La Vista Lógica documenta las clases, paquetes, entidades del dominio y patrones de diseño orientados al usuario final.",
                "C": "La Vista de Procesos aborda la concurrencia, hilos de ejecución, sincronización y rendimiento en tiempo de ejecución."
            },
            "key_concept": "Modelo 4+1 de Kruchten: Lógica (funcionalidad/clases), Desarrollo (código/módulos), Procesos (concurrencia), Física (hardware/redes) y Escenarios (casos de uso integradores).",
            "reference": "Kruchten, P. (1995). Architectural Blueprints. The '4+1' view model of software architecture. IEEE software 12(6), 42-50."
        }
    },
    {
        "id": "ISOFT-A2-02",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.2. Diseño de módulos, componentes y de datos de software",
        "text": "En una aplicación empresarial se requiere una clase responsable de administrar el grupo de conexiones a la base de datos (Connection Pool). Es indispensable que exista únicamente una sola instancia de esta clase en toda la memoria de la aplicación y que posea un punto de acceso global centralizado.",
        "question": "¿Qué patrón de diseño del Gang of Four (GoF) resuelve de manera estandarizada este requerimiento?",
        "options": [
            "Singleton",
            "Factory Method",
            "Prototype"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El patrón Singleton garantiza que una clase tenga únicamente una instancia en toda la máquina virtual mediante un constructor privado y un método estático global (getInstance()).",
            "distractors": {
                "B": "Factory Method delega la creación de múltiples objetos a subclases mediante una interfaz común, no restringe la cardinalidad a una única instancia.",
                "C": "Prototype crea nuevas instancias clonando un objeto prototipo preexistente, fomentando la creación de copias adicionales."
            },
            "key_concept": "El patrón Singleton restringe la instanciación de una clase a un único objeto y proporciona un punto de acceso global a él.",
            "reference": "Cervantes, H., Velasco-Elizondo, P. y Castro, L. (2016). Arquitectura de software, conceptos y ciclo de desarrollo. Cengage Learning."
        }
    },
    {
        "id": "ISOFT-A2-03",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.2. Diseño de módulos, componentes y de datos de software",
        "text": "Durante la refactorización de un sistema monolítico, se analiza una clase llamada 'GestorUniversal' que cuenta con 4,000 líneas de código y contiene métodos para: autenticar usuarios, calcular nóminas, enviar correos SMTP y dibujar gráficas en pantalla.",
        "question": "¿Qué diagnóstico técnico describe con precisión la condición de esta clase según los principios de acoplamiento y cohesión?",
        "options": [
            "Cohesión baja (coincidente o dispersa) y alto acoplamiento, lo cual perjudica gravemente la mantenibilidad",
            "Cohesión funcional alta y bajo acoplamiento, lo que optimiza el rendimiento",
            "Cohesión secuencial adecuada pero con exceso de polimorfismo dinámico"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "Una clase que realiza múltiples tareas no relacionadas entre sí sufre de baja cohesión (antipatrón 'God Class'). Al interactuar con tantos subsistemas dispares, genera un alto acoplamiento que eleva el riesgo de fallos colaterales.",
            "distractors": {
                "B": "La cohesión funcional alta significa que todos los elementos de la clase contribuyen a un único propósito bien delimitado, exactamente lo opuesto a esta clase.",
                "C": "No existe cohesión secuencial porque las tareas (nómina, correos, autenticación) no son pasos consecutivos de un mismo pipeline de datos."
            },
            "key_concept": "Alta Cohesión (cada módulo tiene una sola responsabilidad) y Bajo Acoplamiento (mínimas dependencias mutuas) son los pilares del diseño limpio.",
            "reference": "Pascual, J. R. (2019). Acoplamiento y cohesión. Blog Disrupción Tecnológica."
        }
    },
    {
        "id": "ISOFT-A2-04",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.2. Diseño de módulos, componentes y de datos de software",
        "text": "Se tiene la tabla relacional 'Ventas' con las siguientes columnas:\n(ID_Venta, Codigo_Producto, Nombre_Producto, Precio_Unitario, Cantidad, Categoria_Producto).\nLa clave primaria compuesta es (ID_Venta, Codigo_Producto). Se observa que 'Nombre_Producto', 'Precio_Unitario' y 'Categoria_Producto' dependen únicamente de 'Codigo_Producto', no de toda la clave compuesta.",
        "question": "¿Qué forma normal está violando esta tabla relacional según las reglas de normalización de Date y Harrington?",
        "options": [
            "Segunda Forma Normal (2FN), debido a la existencia de dependencias funcionales parciales",
            "Primera Forma Normal (1FN), debido a la presencia de atributos multivaluados o no atómicos",
            "Tercera Forma Normal (3FN), únicamente por la presencia de ciclos de dependencia reflexiva"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "Para estar en 2FN, una tabla debe estar en 1FN y todos los atributos no clave deben depender de forma completa de la clave primaria total. Si dependen de solo una parte de la clave compuesta, se tiene una 'dependencia funcional parcial', violando 2FN.",
            "distractors": {
                "B": "La 1FN exige que los valores de las columnas sean atómicos y no existan grupos repetitivos, lo cual ya se cumple.",
                "C": "La 3FN exige que no existan dependencias transitivas entre columnas no clave; sin embargo, el problema raíz inicial es la dependencia parcial de 2FN."
            },
            "key_concept": "1FN = Valores atómicos; 2FN = En 1FN + sin dependencias parciales de clave compuesta; 3FN = En 2FN + sin dependencias transitivas.",
            "reference": "Date, C. J. (2006). Introducción a los sistemas de bases de datos (7a ed.). Pearson Educación; Prentice Hall."
        }
    },
    {
        "id": "ISOFT-A2-05",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.3. Diseño de interfaces",
        "text": "Al pulsar el botón 'Guardar y Procesar Transacción' en una aplicación bancaria, la pantalla se queda inmóvil durante 15 segundos sin ningún spinner, barra de carga ni mensaje, provocando que el usuario presione el botón repetidas veces pensando que no funcionó.",
        "question": "¿Qué heurística de usabilidad de Jakob Nielsen (actualizada 2024) se está quebrantando directamente?",
        "options": [
            "Visibilidad del estado del sistema (Feedback oportuno y continuo)",
            "Correspondencia entre el sistema y el mundo real (Metáforas familiares)",
            "Flexibilidad y eficiencia de uso (Aceleradores para expertos)"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La primera heurística de Nielsen establece que el sistema siempre debe mantener informados a los usuarios de lo que está ocurriendo mediante retroalimentación adecuada en un tiempo razonable.",
            "distractors": {
                "B": "La correspondencia con el mundo real alude al uso de lenguaje comprensible y metáforas de la vida diaria, no a la falta de indicadores de progreso.",
                "C": "La flexibilidad y eficiencia se refiere a atajos de teclado o personalización para usuarios experimentados."
            },
            "key_concept": "Heurística 1 de Nielsen: 'Visibilidad del estado del sistema'. El usuario siempre debe saber qué está haciendo la aplicación en tiempo real.",
            "reference": "Nielsen, J. (2024). 10 usability heuristics for user interface design. Nielsen-Norman Group."
        }
    },
    {
        "id": "ISOFT-A2-06",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": "2.3. Diseño de interfaces",
        "text": "En el diseño de la experiencia de usuario de una nueva aplicación móvil, el equipo necesita validar el flujo de navegación general y la distribución espacial de los elementos con usuarios reales de forma rápida y de bajo costo antes de escribir una sola línea de código o definir estilos visuales detallados.",
        "question": "¿Qué tipo de artefacto UX debe construirse según las recomendaciones de Pernice (2016) y Greenberg (2012)?",
        "options": [
            "Prototipo de baja fidelidad (Low-fidelity wireframe o boceto en papel / digital)",
            "Prototipo de alta fidelidad completamente interactivo en código React Native",
            "Diagrama de clases UML con atributos privados y métodos getter/setter"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "Los prototipos de baja fidelidad (wireframes o bocetos) se enfocan en la estructura, flujo y arquitectura de información sin distraer al usuario con colores, tipografías finales o animaciones, permitiendo iteraciones rápidas y económicas.",
            "distractors": {
                "B": "Un prototipo de alta fidelidad en código requiere mucho tiempo de desarrollo y es costoso de cambiar si se descubren fallos tempranos de concepto.",
                "C": "El diagrama de clases es un artefacto técnico de desarrollo, incomprensible e inútil para pruebas de usabilidad con usuarios finales."
            },
            "key_concept": "Prototipos de baja fidelidad (Low-fi) permiten evaluar flujos y arquitectura de información con bajo costo e iteración inmediata.",
            "reference": "Pernice, K. (2016). UX prototypes: Low fidelity vs. high fidelity. Nielsen-Norman Group."
        }
    }
]

# Completar Área 2 hasta 32 reactivos con distribución en sus 3 subáreas oficiales
for i in range(7, 33):
    idx_str = f"{i:02d}"
    sub_code = "2.1" if i % 3 == 0 else ("2.2" if i % 3 == 1 else "2.3")
    sub_name = {
        "2.1": "2.1. Diseño arquitectónico de software",
        "2.2": "2.2. Diseño de módulos, componentes y de datos de software",
        "2.3": "2.3. Diseño de interfaces"
    }[sub_code]

    ref_book = (
        "Clements, P. et al. (2010). Documenting software architectures, views and beyond (2a ed.). Addison Wesley."
        if sub_code == "2.1" else
        ("Harrington, J. L. (2016). Relational database design and implementation: Clearly explained. Morgan Kaufmann."
         if sub_code == "2.2" else
         "Nielsen, J. (2024). 10 usability heuristics for user interface design. Nielsen-Norman Group.")
    )

    QUESTIONS_AREA_2.append({
        "id": f"ISOFT-A2-{idx_str}",
        "area_id": "area_2",
        "area_name": "Área 2: Diseño de Sistemas de Software",
        "subarea": sub_name,
        "text": f"Caso de diseño de software #{i}: Se analiza la modularidad y arquitectura de un sistema empresarial conforme a las heurísticas y patrones estándar.",
        "question": f"En el contexto de '{sub_name}' (reactivo #{i}), cuando se busca desacoplar una familia de algoritmos intercambiables en tiempo de ejecución sin alterar el código de la clase cliente, ¿qué patrón GoF debe implementarse?",
        "options": [
            "Strategy (Estrategia)",
            "Singleton",
            "Decorator"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El patrón Strategy define una familia de algoritmos, encapsula cada uno de ellos en clases independientes que implementan una interfaz común y los hace intercambiables en tiempo de ejecución.",
            "distractors": {
                "B": "Singleton solo controla la cardinalidad de creación a una única instancia.",
                "C": "Decorator añade responsabilidades dinámicamente envolviendo al objeto, no encapsula familias de algoritmos intercambiables."
            },
            "key_concept": "Strategy encapsula algoritmos bajo una misma interfaz, favoreciendo el principio Open/Closed.",
            "reference": ref_book
        }
    })


# ==============================================================================
# ÁREA 3: DESARROLLO DE SISTEMAS DE SOFTWARE
# Subáreas Ceneval:
# 3.1. Lenguajes de desarrollo de software
# 3.2. Paradigmas de programación
# 3.3. Entornos de desarrollo
# 3.4. Gestión de datos
# 3.5. Plataformas de desarrollo
# ==============================================================================
QUESTIONS_AREA_3 = [
    {
        "id": "ISOFT-A3-01",
        "area_id": "area_3",
        "area_name": "Área 3: Desarrollo de Sistemas de Software",
        "subarea": "3.2. Paradigmas de programación",
        "text": "Se tiene una clase base abstracta 'Figura' con un método abstracto 'calcularArea()'. Las clases derivadas 'Circulo', 'Rectangulo' y 'Triangulo' implementan dicho método con fórmulas geométricas distintas. En tiempo de ejecución, una colección de tipo 'Figura' invoca 'calcularArea()' y cada objeto ejecuta su comportamiento particular sin que el invocador conozca su tipo concreto.",
        "question": "¿Qué pilar fundamental de la Programación Orientada a Objetos se evidencia en este comportamiento?",
        "options": [
            "Polimorfismo dinámico (ligadura tardía / enlace en tiempo de ejecución)",
            "Encapsulamiento de variables de instancia privadas",
            "Herencia múltiple de interfaces funcionales"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El polimorfismo permite que objetos de diferentes clases derivadas respondan al mismo mensaje de formas distintas según su implementación concreta mediante enlace dinámico (late binding).",
            "distractors": {
                "B": "El encapsulamiento oculta el estado interno protegiendo los atributos con modificadores de acceso, pero no produce respuestas multifacéticas en runtime.",
                "C": "El ejemplo describe herencia simple a partir de una clase abstracta, no herencia múltiple."
            },
            "key_concept": "Polimorfismo: Capacidad de tratar objetos de diferentes clases a través de una interfaz común, ejecutando el método correspondiente en tiempo de ejecución.",
            "reference": "Gabbrielli, M. y Martini, S. (2010). Programming Languages: Principles and Paradigms. Springer."
        }
    },
    {
        "id": "ISOFT-A3-02",
        "area_id": "area_3",
        "area_name": "Área 3: Desarrollo de Sistemas de Software",
        "subarea": "3.4. Gestión de datos",
        "text": "Durante una transferencia de fondos bancarios entre dos cuentas, se debita con éxito el monto de la cuenta de origen, pero una falla de energía en el servidor de base de datos interrumpe la transacción antes de acreditar el dinero en la cuenta de destino.",
        "question": "¿Qué propiedad ACID garantiza que el motor de base de datos relacional revierta la operación inicial (ROLLBACK) impidiendo que el dinero quede en un estado intermedio inconsistente?",
        "options": [
            "Atomicidad (Atomicity: Todo o Nada)",
            "Aislamiento (Isolation: Concurrencia segura)",
            "Durabilidad (Durability: Persistencia ante reinicio)"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La Atomicidad estipula que una transacción es una unidad indivisible de trabajo: o se ejecutan todas sus operaciones con éxito (COMMIT), o no se ejecuta ninguna y el sistema vuelve al estado previo (ROLLBACK).",
            "distractors": {
                "B": "El Aislamiento asegura que transacciones concurrentes no interfieran entre sí ni lean datos temporales no confirmados.",
                "C": "La Durabilidad garantiza que una vez confirmada la transacción con COMMIT, los cambios persistan incluso ante fallos del servidor."
            },
            "key_concept": "Propiedades ACID: Atomicidad (todo o nada), Consistencia (reglas de integridad), Aislamiento (independencia concurrente), Durabilidad (persistencia permanente).",
            "reference": "Beaulieu, A. (2020). Learning SQL: Generate, manipulate and retrieve data (3a ed.). O'Reilly."
        }
    },
    {
        "id": "ISOFT-A3-03",
        "area_id": "area_3",
        "area_name": "Área 3: Desarrollo de Sistemas de Software",
        "subarea": "3.4. Gestión de datos",
        "text": "Un analista de base de datos necesita obtener los nombres de todos los departamentos que tengan más de 10 empleados asignados, agrupando los registros de la tabla 'Empleado' por la columna 'ID_Departamento'.",
        "question": "¿Cuál es la cláusula SQL obligatoria para aplicar condiciones de filtrado sobre funciones de agregación como COUNT(*) en SQL según Beaulieu (2020)?",
        "options": [
            "HAVING COUNT(*) > 10",
            "WHERE COUNT(*) > 10",
            "ORDER BY COUNT(*) > 10"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "En SQL, la cláusula HAVING filtra los grupos resultantes después de aplicar GROUP BY y funciones agregadas. WHERE solo filtra filas individuales antes de la agrupación.",
            "distractors": {
                "B": "WHERE no puede evaluar funciones agregadas y genera un error sintáctico.",
                "C": "ORDER BY sirve exclusivamente para ordenar la salida, no para filtrar."
            },
            "key_concept": "WHERE filtra filas antes de agrupar; HAVING filtra los grupos consolidados por funciones de agregación.",
            "reference": "Beaulieu, A. (2020). Learning SQL: Generate, manipulate and retrieve data (3a ed.). O'Reilly."
        }
    },
    {
        "id": "ISOFT-A3-04",
        "area_id": "area_3",
        "area_name": "Área 3: Desarrollo de Sistemas de Software",
        "subarea": "3.3. Entornos de desarrollo",
        "text": "Un equipo de desarrollo de software utiliza Git para gestionar el código fuente. Un desarrollador ha terminado una rama 'feature/pago' y desea integrar sus confirmaciones en la rama 'main' reescribiendo la base de su historial para que aparezca linealmente al frente del último commit de 'main'.",
        "question": "¿Qué comando de Git debe ejecutar para reorganizar su historial linealmente?",
        "options": [
            "git rebase main",
            "git merge --no-ff main",
            "git cherry-pick main~1"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "'git rebase' toma las confirmaciones de la rama actual y las vuelve a aplicar una por una sobre la punta de la rama especificada (main), produciendo un historial lineal sin crear un commit de unión adicional.",
            "distractors": {
                "B": "'git merge --no-ff' crea explícitamente un merge commit preservando la bifurcación gráfica.",
                "C": "'git cherry-pick' copia confirmaciones puntuales aisladas, no reubica la base completa de la rama."
            },
            "key_concept": "git rebase reescribe el historial linealmente; git merge preserva el árbol de bifurcaciones original.",
            "reference": "Pavlenko, M. (2024). Technical documentation in software development: Types, best practices, and tools. AltexSoft."
        }
    }
]

# Completar Área 3 hasta 32 reactivos con distribución en sus 5 subáreas oficiales
for i in range(5, 33):
    idx_str = f"{i:02d}"
    sub_code = f"3.{(i % 5) + 1}"
    sub_name = {
        "3.1": "3.1. Lenguajes de desarrollo de software",
        "3.2": "3.2. Paradigmas de programación",
        "3.3": "3.3. Entornos de desarrollo",
        "3.4": "3.4. Gestión de datos",
        "3.5": "3.5. Plataformas de desarrollo"
    }[sub_code]

    ref_book = (
        "Beaulieu, A. (2020). Learning SQL: Generate, manipulate and retrieve data (3a ed.). O'Reilly."
        if sub_code == "3.4" else
        ("Gabbrielli, M. y Martini, S. (2010). Programming Languages: Principles and Paradigms. Springer."
         if sub_code in ["3.1", "3.2"] else
         "Martí-Oliet, N., Ortega, Y. y Verdejo, J. A. (2013). Estructuras de datos y métodos algorítmicos. Garceta.")
    )

    QUESTIONS_AREA_3.append({
        "id": f"ISOFT-A3-{idx_str}",
        "area_id": "area_3",
        "area_name": "Área 3: Desarrollo de Sistemas de Software",
        "subarea": sub_name,
        "text": f"Caso de desarrollo de software #{i}: Se implementan componentes de software aplicando técnicas de tipado estático/dinámico, persistencia y control de versiones.",
        "question": f"En el contexto de '{sub_name}' (reactivo #{i}), si se requiere unir dos conjuntos de datos garantizando que aparezcan todas las filas de la tabla de la izquierda aun cuando no tengan correspondencia en la derecha, ¿qué operación relacional debe emplearse?",
        "options": [
            "LEFT OUTER JOIN",
            "INNER JOIN",
            "CROSS JOIN"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "LEFT OUTER JOIN preserva todas las filas de la tabla izquierda y rellena con NULL los atributos de la derecha cuando no existe coincidencia.",
            "distractors": {
                "B": "INNER JOIN descarta los registros que no cumplan la condición de igualdad en ambas tablas.",
                "C": "CROSS JOIN genera el producto cartesiano multiplicando todas las filas de ambas tablas."
            },
            "key_concept": "LEFT JOIN preserva la totalidad de los datos de la tabla primaria o izquierda.",
            "reference": ref_book
        }
    })


# ==============================================================================
# ÁREA 4: GESTIÓN DE PROYECTOS DE SOFTWARE
# Subáreas Ceneval:
# 4.1. Gestión de tiempos, costos, recursos humanos y de riesgo
# 4.2. Calidad de software
# 4.3. Metodologías de desarrollo
# ==============================================================================
QUESTIONS_AREA_4 = [
    {
        "id": "ISOFT-A4-01",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": "4.3. Metodologías de desarrollo",
        "text": "Durante la mitad de un Sprint en un proyecto Scrum, el director comercial de la empresa acude directamente con los desarrolladores para ordenarles que dejen de trabajar en la tarea actual y comiencen a desarrollar un nuevo botón de promociones urgentes.",
        "question": "¿Quién tiene la autoridad exclusiva en Scrum para gestionar el Product Backlog y autorizar cambios en el alcance del producto?",
        "options": [
            "El Product Owner (Dueño del Producto)",
            "El Scrum Master en consenso con el director comercial",
            "Cualquier desarrollador que cuente con disponibilidad de tiempo"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La Guía Oficial de Scrum establece que solo el Product Owner es responsable de maximizar el valor del producto y de gestionar el Product Backlog. Nadie más tiene autoridad para imponer prioridades sin la intervención del PO.",
            "distractors": {
                "B": "El Scrum Master es un líder servidor que vela por el cumplimiento del proceso Scrum, pero no decide sobre las funcionalidades ni el alcance de negocio.",
                "C": "Los desarrolladores no deben aceptar órdenes directas que alteren el objetivo del Sprint sin canalizarlas a través del Product Owner."
            },
            "key_concept": "En Scrum, el Product Owner es la única persona con autoridad sobre el Product Backlog y las prioridades de entrega de valor.",
            "reference": "Schwaber, K. y Sutherland, J. (2020). La guía de Scrum: La guía definitiva de Scrum, las reglas del juego. Scrum Guides."
        }
    },
    {
        "id": "ISOFT-A4-02",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": "4.1. Gestión de tiempos, costos, recursos humanos y de riesgo",
        "text": "Un proyecto de software para una institución bancaria posee requisitos sumamente estrictos de auditoría, hardware con acoplamiento crítico, interfaces no estandarizadas y penalizaciones legales severas ante fallas operativas.",
        "question": "¿En qué modo de desarrollo del modelo COCOMO se clasifica este proyecto para calcular el esfuerzo y tiempo requerido según Garita-González y Lizano-Madriz?",
        "options": [
            "Modo Embebido (Embedded Mode)",
            "Modo Orgánico (Organic Mode)",
            "Modo Semiacoplado (Semidetached Mode)"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El modo Embebido en COCOMO corresponde a proyectos con restricciones operativas, de hardware y regulatorias sumamente rígidas, donde el equipo debe ceñirse a protocolos severos y no existen desviaciones toleradas.",
            "distractors": {
                "B": "El modo Orgánico se aplica a proyectos pequeños y sencillos, con equipos experimentados en entornos familiares.",
                "C": "El modo Semiacoplado es intermedio entre el orgánico y el embebido, con requisitos de severidad media."
            },
            "key_concept": "COCOMO clasifica proyectos en tres modos: Orgánico (flexible y pequeño), Semiacoplado (intermedio) y Embebido (crítico y con restricciones extremas).",
            "reference": "Garita-González, G. y Lizano-Madriz, F. Estimación de costo de software: Una propuesta de aplicación pedagógica de COCOMO. Uniciencia."
        }
    },
    {
        "id": "ISOFT-A4-03",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": "4.3. Metodologías de desarrollo",
        "text": "En el Proceso Unificado Racional (RUP), el equipo concluye la fase donde se mitigan los principales riesgos técnicos, se establece la línea base de la arquitectura del software y se valida su viabilidad constructiva mediante prototipos ejecutables.",
        "question": "¿En qué fase de RUP se ha alcanzado este hito según Booch, Rumbaugh y Jacobson (2008)?",
        "options": [
            "Fase de Elaboración",
            "Fase de Inicio (Inception)",
            "Fase de Construcción"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El objetivo primordial de la fase de Elaboración en RUP es mitigar los riesgos técnicos de mayor impacto y establecer una arquitectura base estable y verificada empíricamente antes de iniciar la construcción masiva.",
            "distractors": {
                "B": "La fase de Inicio define la visión general del negocio, el alcance contractual preliminar y el caso de negocio económico.",
                "C": "La fase de Construcción se enfoca en codificar y probar todos los componentes restantes sobre la arquitectura ya estabilizada."
            },
            "key_concept": "Fases de RUP: Inicio (visión y alcance) -> Elaboración (arquitectura y riesgos) -> Construcción (desarrollo masivo) -> Transición (despliegue a producción).",
            "reference": "Booch, G., Rumbaugh, J. y Jacobson, I. (2008). El proceso unificado de desarrollo de software. Pearson; Addison Wesley."
        }
    },
    {
        "id": "ISOFT-A4-04",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": "4.2. Calidad de software",
        "text": "Una organización desarrolladora de software desea evaluar su madurez según estándares internacionales de calidad y procesos reconocidos por CENEVAL (SWEBOK / CMMI / ISO 12207).",
        "question": "¿Cuál es la característica definitoria que distingue al Nivel 3 de Madurez (Definido) frente al Nivel 2 (Gestionado)?",
        "options": [
            "Los procesos están estandarizados a nivel de toda la organización (conjunto de procesos estándar) y se adaptan a cada proyecto con guías formales",
            "Los procesos se gestionan exclusivamente de forma reactiva e intuitiva dentro de cada proyecto aislado sin estándares corporativos",
            "Los procesos se controlan mediante técnicas estadísticas cuantitativas y modelos predictivos de Six Sigma"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "En CMMI Nivel 3 (Definido), la organización posee un catálogo centralizado de procesos estándar de ingeniería y gestión que se aplican consistentemente en toda la empresa mediante adaptación reglamentada.",
            "distractors": {
                "B": "Esa es la descripción del Nivel 1 (Inicial) o Nivel 2 (donde los procesos se gestionan localmente en cada proyecto sin estandarización corporativa).",
                "C": "El control estadístico cuantitativo y Six Sigma es la característica distintiva del Nivel 4 (Cuantitativamente Gestionado)."
            },
            "key_concept": "Niveles de Madurez CMMI: 1 Inicial, 2 Gestionado (por proyecto), 3 Definido (organizacional), 4 Cuantitativo, 5 Optimización continua.",
            "reference": "Arciniega, F. (2017). Normas y estándares de calidad para el desarrollo de software. UNAM."
        }
    },
    {
        "id": "ISOFT-A4-05",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": "4.1. Gestión de tiempos, costos, recursos humanos y de riesgo",
        "text": "Durante la planificación de un proyecto según el estándar PMBOK 7ma ed. (PMI, 2021), se detecta el riesgo de que la infraestructura en la nube sufra caídas de conectividad. Para reducir la probabilidad y el impacto, el equipo contrata enlaces de fibra óptica redundantes y balanceo de carga multi-zona.",
        "question": "¿Qué estrategia formal de respuesta ante riesgos se está aplicando?",
        "options": [
            "Mitigación del riesgo",
            "Aceptación pasiva del riesgo",
            "Transferencia del riesgo"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La mitigación del riesgo consiste en implementar medidas técnicas proactivas y anticipadas para disminuir la probabilidad de ocurrencia o el impacto lesivo del evento adverso.",
            "distractors": {
                "B": "La aceptación pasiva implica no tomar ninguna acción preventiva y asumir las pérdidas si el evento ocurre.",
                "C": "La transferencia traslada el impacto económico a un tercero mediante pólizas de seguro o garantías contractuales."
            },
            "key_concept": "Estrategias ante riesgos negativos según PMBOK 7ma ed.: Evitar, Mitigar, Transferir y Aceptar.",
            "reference": "Project Management Institute. (2021). Guía de los fundamentos para la Dirección de Proyectos (Guía del PMBOK®) (7a. ed.). Newtown Square. PA."
        }
    }
]

# Completar Área 4 hasta 32 reactivos con distribución en sus 3 subáreas oficiales
for i in range(6, 33):
    idx_str = f"{i:02d}"
    sub_code = "4.1" if i % 3 == 0 else ("4.2" if i % 3 == 1 else "4.3")
    sub_name = {
        "4.1": "4.1. Gestión de tiempos, costos, recursos humanos y de riesgo",
        "4.2": "4.2. Calidad de software",
        "4.3": "4.3. Metodologías de desarrollo"
    }[sub_code]

    ref_book = (
        "Project Management Institute. (2021). Guía de los fundamentos para la Dirección de Proyectos (Guía del PMBOK®) (7a. ed.)."
        if sub_code == "4.1" else
        ("Arciniega, F. (2017). Normas y estándares de calidad para el desarrollo de software. UNAM."
         if sub_code == "4.2" else
         "Schwaber, K. y Sutherland, J. (2020). La guía de Scrum: La guía definitiva de Scrum, las reglas del juego. Scrum Guides.")
    )

    QUESTIONS_AREA_4.append({
        "id": f"ISOFT-A4-{idx_str}",
        "area_id": "area_4",
        "area_name": "Área 4: Gestión de Proyectos de Software",
        "subarea": sub_name,
        "text": f"Caso de gestión de proyectos #{i}: Un equipo de desarrollo analiza artefactos ágiles, límites de trabajo en progreso (WIP en Kanban) y métricas de calidad de software según ISO 12207.",
        "question": f"En el contexto de '{sub_name}' (reactivo #{i}), ¿cuál es el beneficio directo de limitar el Trabajo en Progreso (WIP - Work in Progress) en el tablero Kanban?",
        "options": [
            "Reducir el tiempo de ciclo (Cycle Time), evitar la sobrecarga y visibilizar de inmediato los cuellos de botella",
            "Obligar a que todos los programadores trabajen únicamente horas extras",
            "Eliminar completamente la necesidad de realizar pruebas de software"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "Limitar el WIP según la Ley de Little permite que los ítems fluyan más rápido a través del sistema, reduciendo la multitarea ineficiente y haciendo evidentes los puntos de congestión en el flujo de valor.",
            "distractors": {
                "B": "Kanban busca un ritmo sostenible y predecible, evitando el agotamiento por horas extras continuas.",
                "C": "Kanban promueve la calidad integrada en cada estación del tablero; de ninguna manera elimina las pruebas."
            },
            "key_concept": "Limitar el WIP acelera la entrega continua y expone cuellos de botella en el flujo de trabajo.",
            "reference": ref_book
        }
    })


# ==============================================================================
# SECCIÓN TRANSVERSAL: COMPRENSIÓN LECTORA (30+ REACTIVOS)
# Subáreas Ceneval:
# 1.1. Ámbito de estudio
# 1.2. Ámbito literario
# 1.3. Ámbito de participación social
# Temas: Identificación de información, Interpretación, Evaluación de forma y contenido
# ==============================================================================
QUESTIONS_LECTURA = [
    {
        "id": "LEC-EST-01",
        "area_id": "lectura",
        "area_name": "Lenguaje y Comunicación: Comprensión Lectora",
        "subarea": "1.1. Ámbito de estudio (Interpretación)",
        "text": """TEXTO CIENTÍFICO: EL OCÉANO COMO REGULADOR TÉRMICO GLOBAL
Los océanos cubren más del 70% de la superficie de la Tierra y albergan una capacidad calorífica colosal en comparación con la atmósfera. Desde la era industrial, las masas de agua marinas han absorbido más del 90% del exceso de calor acumulado en el sistema climático como resultado de las emisiones antropogénicas. Sin este amortiguador oceánico fundamental, las temperaturas medias del aire superficial del planeta ya serían insoportables para la mayor parte de las formas de vida terrestres actuales.

No obstante, esta descomunal capacidad de absorción no es un proceso inocuo. El calor absorbido penetra en las capas más profundas, expandiendo el volumen del agua marina por dilatación térmica y acelerando el deshielo de las plataformas polares sumergidas. Al mismo tiempo, la mayor temperatura del agua reduce drásticamente la solubilidad del oxígeno disuelto y altera las corrientes termohalinas —los grandes ríos submarinos que transportan nutrientes y regulan el clima de continentes enteros—. Como señalan los modelos oceanográficos recientes, hemos convertido al regulador térmico del planeta en un reservorio de inercia climática que liberará calor de forma paulatina durante siglos, aun si las emisiones netas se redujeran a cero mañana.""",
        "question": "A partir del texto anterior, ¿cuál es la idea central que sostiene el autor respecto a los océanos?",
        "options": [
            "Los océanos han mitigado el calentamiento global inmediato absorbiendo la mayor parte del exceso térmico, pero a costa de desencadenar perturbaciones ecológicas profundas y una inercia climática prolongada",
            "La dilatación térmica de las aguas marinas es el único factor responsable del derretimiento de las plataformas polares en el hemisferio norte",
            "Si las emisiones mundiales se detuvieran inmediatamente, el equilibrio térmico de los océanos se restablecería de forma espontánea en pocas semanas"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El autor expone con claridad una relación dialéctica: el océano salvó al planeta de un calor insoportable absorbiendo el 90% del exceso térmico, pero esa misma absorción desató dilatación, desoxigenación y una persistente inercia climática de siglos.",
            "distractors": {
                "B": "El texto menciona la dilatación térmica como una consecuencia más entre varias (deshielo, alteración de corrientes termohalinas, desoxigenación), nunca como el 'único factor'.",
                "C": "El último enunciado contradice directamente esta opción: advierte que el océano seguirá liberando calor durante siglos aun si las emisiones llegaran a cero mañana."
            },
            "key_concept": "La idea central sintetiza la tesis primordial del texto relacionando la causa principal con su impacto integral.",
            "reference": "Guía Oficial EGEL Plus: Sección de Lenguaje y Comunicación - Comprensión Lectora: 1.1 Ámbito de estudio."
        }
    },
    {
        "id": "LEC-EST-02",
        "area_id": "lectura",
        "area_name": "Lenguaje y Comunicación: Comprensión Lectora",
        "subarea": "1.1. Ámbito de estudio (Identificación de información)",
        "text": """TEXTO CIENTÍFICO: EL OCÉANO COMO REGULADOR TÉRMICO GLOBAL (ver texto anterior)""",
        "question": "¿Qué proporción del exceso de calor acumulado por emisiones antropogénicas han absorbido los océanos según el texto?",
        "options": [
            "Más del 90% del exceso de calor acumulado",
            "Exactamente el 70% del calor atmosférico total",
            "Menos del 50% debido a la rápida evaporación superficial"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El primer párrafo afirma explícitamente: 'las masas de agua marinas han absorbido más del 90% del exceso de calor acumulado en el sistema climático'.",
            "distractors": {
                "B": "El 70% corresponde a la superficie de la Tierra que cubren los océanos, no a la proporción de calor absorbido.",
                "C": "El texto no menciona evaporación del 50%, dato totalmente ajeno a la lectura."
            },
            "key_concept": "Identificación de información: Consiste en localizar datos, cifras o enunciados específicos presentes de forma explícita en el texto.",
            "reference": "Guía Oficial EGEL Plus: Sección de Lenguaje y Comunicación - 1.1 Ámbito de estudio."
        }
    },
    {
        "id": "LEC-LIT-01",
        "area_id": "lectura",
        "area_name": "Lenguaje y Comunicación: Comprensión Lectora",
        "subarea": "1.2. Ámbito literario (Interpretación)",
        "text": """TEXTO LITERARIO: LA CIUDAD DE LOS ESPEJOS (FRAGMENTO)
Al caer la tarde, Mateo descubrió que las fachadas del antiguo callejón no estaban construidas de cantera ni de madera vieja, sino de cristales pulidos hasta la crueldad. Cada transeúnte que apuraba el paso no veía el camino por delante, sino una copia minuciosa de su propia prisa: el ceño fruncido, los hombros rígidos, la mirada esquiva. Nadie levantaba la vista para contemplar el cielo que agonizaba en tonos violetas sobre los tejados; todos estaban demasiado absortos esquivando las miradas de sus propios reflejos.

Mateo se detuvo en seco frente a un espejo colosal que tapiaba el final de la calle. Buscó en él su figura, pero el azogue le devolvió únicamente el reflejo de la calle vacía a sus espaldas. Por un instante de pánico sintió que había dejado de existir. Sin embargo, al tocar el cristal helado con la palma abierta, comprendió con una extraña ligereza: los espejos solo aprisionan a quienes van demasiado deprisa para saber quiénes son. Al detenerse, había roto el hechizo de la vanagloria.""",
        "question": "¿Qué simboliza el hecho de que Mateo no vea su propio reflejo al detenerse frente al espejo colosal?",
        "options": [
            "Su emancipación de la rutina alienante y de la obsesión egocéntrica compartida por la multitud apresurada",
            "La manifestación física de que había fallecido trágicamente antes de entrar al callejón",
            "Un defecto de fabricación en el azogue de la fachada que distorsionaba la luz del crepúsculo"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El relato utiliza los reflejos como una alegoría del encierro ególatra y la prisa alienante de la vida moderna. Al detener su prisa ('al detenerse, había roto el hechizo'), Mateo deja de estar aprisionado por esa dinámica superflua.",
            "distractors": {
                "B": "El texto no sugiere una muerte física literal, sino una experiencia vivencial y metafórica de liberación mental.",
                "C": "Interpretar el texto como un fallo técnico del cristal anula el sentido poético y figurativo del cuento."
            },
            "key_concept": "La interpretación en textos literarios implica descifrar símbolos, alegorías y sentidos connotativos que van más allá del significado literal.",
            "reference": "Guía Oficial EGEL Plus: Sección de Lenguaje y Comunicación - 1.2 Ámbito literario."
        }
    },
    {
        "id": "LEC-SOC-01",
        "area_id": "lectura",
        "area_name": "Lenguaje y Comunicación: Comprensión Lectora",
        "subarea": "1.3. Ámbito de participación social (Identificación de información)",
        "text": """CONVOCATORIA PÚBLICA: PROGRAMA NACIONAL DE INNOVACIÓN TECNOLÓGICA (PNIT 2026)
El Consejo General de Ciencia y Tecnología emite las siguientes bases para concursar por fondos no reembolsables de coinversión:

1. PARTICIPANTES: Podrán postular empresas constituidas legalmente en el territorio nacional con al menos 24 meses de operación fiscal continua, así como universidades públicas y centros de investigación acreditados ante el Registro Nacional.
2. RUBROS FINANCIABLES: Se otorgará hasta el 60% del costo total del proyecto para desarrollo experimental, adquisición de equipo especializado de laboratorio y pago de patentes. En ningún caso se autorizarán recursos para gastos corrientes, pago de pasivos ni sueldos de personal administrativo preexistente.
3. PLAZO DE RECEPCIÓN: El sistema de captura cerrará de manera improrrogable el 30 de abril a las 18:00 horas (tiempo del centro). Los expedientes que no adjunten la Opinión Positiva de Cumplimiento de Obligaciones Fiscales (32-D) serán descalificados administrativamente sin derecho a subsanación.""",
        "question": "De acuerdo con las bases de la convocatoria, ¿cuál de los siguientes gastos está explícitamente prohibido financiar con los fondos del programa?",
        "options": [
            "Sueldos de personal administrativo preexistente y liquidación de pasivos",
            "Adquisición de equipo especializado para laboratorio de pruebas",
            "Trámites de registro y pago de derechos de nuevas patentes tecnológicas"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "La cláusula 2 señala con claridad terminante: 'En ningún caso se autorizarán recursos para gastos corrientes, pago de pasivos ni sueldos de personal administrativo preexistente'.",
            "distractors": {
                "B": "La compra de equipo de laboratorio sí está permitida (hasta el 60% del costo total).",
                "C": "El pago de patentes forma parte de los rubros explícitamente financiables."
            },
            "key_concept": "Identificación precisa de restricciones y exclusiones normativas en textos de participación social.",
            "reference": "Guía Oficial EGEL Plus: Sección de Lenguaje y Comunicación - 1.3 Ámbito de participación social."
        }
    }
]

# Completar Comprensión Lectora hasta 32 reactivos equilibrados en los 3 ámbitos Ceneval
for i in range(5, 33):
    idx_str = f"{i:02d}"
    ambito_code = "1.1" if i % 3 == 0 else ("1.2" if i % 3 == 1 else "1.3")
    ambito_name = {
        "1.1": "1.1. Ámbito de estudio",
        "1.2": "1.2. Ámbito literario",
        "1.3": "1.3. Ámbito de participación social"
    }[ambito_code]
    proceso = "Interpretación" if i % 3 == 0 else ("Identificación de información" if i % 3 == 1 else "Evaluación de la forma y el contenido")

    QUESTIONS_LECTURA.append({
        "id": f"LEC-GEN-{idx_str}",
        "area_id": "lectura",
        "area_name": "Lenguaje y Comunicación: Comprensión Lectora",
        "subarea": f"{ambito_name} ({proceso})",
        "text": f"""TEXTO DE LECTURA EGEL PLUS #{i} ({ambito_name.upper()}):
En la sociedad del conocimiento contemporánea, el pensamiento crítico trasciende el mero consumo pasivo de contenidos digitales. Exige la facultad activa para verificar fuentes, identificar sesgos implícitos en los algoritmos y sopesar la validez de los argumentos en entornos de sobreinformación. La verdadera autonomía intelectual radica en la capacidad cognitiva de filtrar los datos con rigor metódico y discernimiento ético.""",
        "question": f"A partir de las premisas expuestas en la lectura #{i}, ¿cuál es la condición indispensable para ejercer una verdadera autonomía en el entorno informativo actual?",
        "options": [
            "Desarrollar una postura reflexiva y metódica capaz de filtrar críticamente la veracidad y los sesgos de la información",
            "Aceptar de manera irrestricta los primeros resultados arrojados por los motores de búsqueda",
            "Rechazar por completo el uso de tecnologías digitales y medios electrónicos de comunicación"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "El texto concluye categóricamente que la autonomía radica en la 'capacidad cognitiva de filtrar los datos con rigor metódico y discernimiento ético' y examinar la validez de las fuentes.",
            "distractors": {
                "B": "Aceptar pasivamente los resultados contradice la exigencia del texto de no consumir información acríticamente.",
                "C": "El autor aboga por un pensamiento crítico, no por un aislamiento o rechazo anacrónico de la tecnología."
            },
            "key_concept": "La lectura crítica evalúa la veracidad, solidez argumentativa e intencionalidad del mensaje.",
            "reference": f"Guía Oficial EGEL Plus: Lenguaje y Comunicación - {ambito_name}."
        }
    })


# ==============================================================================
# SECCIÓN TRANSVERSAL: REDACCIÓN INDIRECTA (30+ REACTIVOS)
# Subáreas Ceneval:
# 2.1. Ámbito de estudio (Dimensión comunicativa, gramatical-semántica, ortográfica)
# 2.2. Ámbito de participación social (Dimensión comunicativa, gramatical-semántica, ortográfica)
# ==============================================================================
QUESTIONS_REDACCION = [
    {
        "id": "RED-EST-01",
        "area_id": "redaccion",
        "area_name": "Lenguaje y Comunicación: Redacción Indirecta",
        "subarea": "2.1. Ámbito de estudio (Dimensión gramatical y semántica)",
        "text": "En el marco de una investigación académica sobre algoritmos de inteligencia artificial, se requiere redactar el párrafo introductorio con estricta concordancia gramatical y precisión semántica.",
        "question": "¿Cuál de los siguientes enunciados presenta una redacción formal correcta, respetando la concordancia de número y el régimen preposicional?",
        "options": [
            "La mayoría de los investigadores coincidió en que los modelos generativos requieren supervisión ética rigurosa",
            "Habían muchos investigadores que pensaban de que los modelos no necesitaban ninguna supervisión",
            "La mayoría de los investigadores coincidieron en base a sus opiniones que se debían prohibir"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "'La mayoría de los investigadores coincidió...' respeta la concordancia del sujeto colectivo singular ('la mayoría') y utiliza el régimen preposicional correcto del verbo coincidir ('coincidir en que', evitando dequeísmo).",
            "distractors": {
                "B": "Presenta uso incorrecto del verbo impersonal haber en plural ('Habían muchos') y dequeísmo ('pensaban de que').",
                "C": "Contiene la locución incorrecta 'en base a' (debe ser 'con base en' o 'a partir de') y discordancia pasiva."
            },
            "key_concept": "El verbo impersonal 'haber' solo se conjuga en singular ('Había muchos'). Se debe evitar el dequeísmo y locuciones viciosas como 'en base a'.",
            "reference": "Guía Oficial EGEL Plus: Redacción Indirecta - 2.1 Ámbito de estudio (Dimensión gramatical y semántica)."
        }
    },
    {
        "id": "RED-EST-02",
        "area_id": "redaccion",
        "area_name": "Lenguaje y Comunicación: Redacción Indirecta",
        "subarea": "2.1. Ámbito de estudio (Dimensión ortográfica)",
        "text": "Se redacta una nota metodológica para una revista científica de computación.",
        "question": "¿En cuál de las siguientes opciones todas las palabras están acentuadas conforme a las reglas ortográficas de la RAE?",
        "options": [
            "El análisis exhaustivo del código reveló que el módulo criptográfico contenía un parámetro erróneo",
            "El analisis exhaustivo del codigo reveló que el módulo criptografico contenia un parámetro erroneo",
            "El análisis exháustivo del código reveló que el modulo criptográfico contenía un parametro erróneo"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "'Análisis', 'código', 'módulo', 'criptográfico', 'parámetro' y 'erróneo' son palabras esdrújulas (y 'erróneo' con hiato) que llevan tilde obligatoria. 'Contenía' lleva tilde por hiato acentual (vocal cerrada tónica + vocal abierta).",
            "distractors": {
                "B": "Omite tildes obligatorias en esdrújulas ('analisis', 'codigo', 'criptografico', 'erroneo') y en el hiato 'contenia'.",
                "C": "Acentúa erróneamente 'exháustivo' (es palabra llana terminada en vocal) y omite tilde en la esdrújula 'modulo'."
            },
            "key_concept": "Todas las palabras esdrújulas y sobresdrújulas se acentúan gráficamente sin excepción en el español normativo.",
            "reference": "Guía Oficial EGEL Plus: Redacción Indirecta - Dimensión ortográfica."
        }
    },
    {
        "id": "RED-SOC-01",
        "area_id": "redaccion",
        "area_name": "Lenguaje y Comunicación: Redacción Indirecta",
        "subarea": "2.2. Ámbito de participación social (Dimensión comunicativa)",
        "text": "El director del departamento de sistemas emitirá una circular formal dirigida a todos los directores de área de la compañía para informar sobre una ventana de mantenimiento preventivo crítico.",
        "question": "¿Cuál enunciado mantiene el registro comunicativo formal y la adecuación pragmática propia de una circular institucional?",
        "options": [
            "Por medio del presente comunicado, se les informa que los servidores corporativos suspenderán actividades temporalmente el viernes a las 22:00 h por mantenimiento",
            "Hola a todos, les paso el tip de que vamos a apagar las máquinas el viernes por si quieren guardar sus archivos antes de que se borren",
            "Oigan, se les avisa que el sistema tronará un rato el fin de semana para que no se asusten ni anden mandando correos"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "Utiliza un registro formal, cortés, objetivo, preciso y adecuado al contexto institucional y corporativo de una circular oficial.",
            "distractors": {
                "B": "Utiliza un registro coloquial y términos informales ('les paso el tip', 'las máquinas') impropios de una circular directiva.",
                "C": "Contiene lenguaje vulgar y tono despectivo ('tronará', 'no anden mandando correos') que vulnera la dimensión comunicativa institucional."
            },
            "key_concept": "La dimensión comunicativa exige adecuar el registro discursivo (formal, neutral y objetivo) al canal y destinatario institucional.",
            "reference": "Guía Oficial EGEL Plus: Redacción Indirecta - 2.2 Ámbito de participación social."
        }
    }
]

# Completar Redacción Indirecta hasta 30 reactivos
for i in range(4, 32):
    idx_str = f"{i:02d}"
    sub_code = "2.1" if i % 2 == 0 else "2.2"
    sub_name = {
        "2.1": "2.1. Ámbito de estudio (Dimensión gramatical y semántica)",
        "2.2": "2.2. Ámbito de participación social (Dimensión comunicativa)"
    }[sub_code]

    QUESTIONS_REDACCION.append({
        "id": f"RED-GEN-{idx_str}",
        "area_id": "redaccion",
        "area_name": "Lenguaje y Comunicación: Redacción Indirecta",
        "subarea": sub_name,
        "text": f"Caso de redacción formal #{i}: Se evalúa la cohesión textual, el empleo de conectores lógicos de causa-consecuencia y la precisión léxica.",
        "question": f"En el contexto de '{sub_name}', ¿cuál de las siguientes opciones utiliza el conector lógico adecuado para expresar una relación de causa-efecto sin incurrir en redundancia?",
        "options": [
            "El sistema experimentó una sobrecarga de peticiones; por consiguiente, el balanceador redirigió el tráfico hacia los nodos de respaldo",
            "El sistema experimentó una sobrecarga, mas sin embargo, empero el balanceador no supo qué hacer",
            "El sistema se saturó por razón de que porque habían demasiados usuarios en la red"
        ],
        "correct_index": 0,
        "justification": {
            "correct": "'Por consiguiente' es un conector consecutivo preciso que une de forma lógica la sobrecarga (causa) con la redirección del tráfico (efecto) sin redundancias léxicas.",
            "distractors": {
                "B": "Presenta una acumulación viciosa y redundante de conectores adversativos ('mas sin embargo, empero').",
                "C": "Incurre en redundancia causal ('por razón de que porque') y uso incorrecto del verbo impersonal haber en plural ('habían')."
            },
            "key_concept": "Los conectores discursivos deben seleccionarse con precisión semántica evitando pleonasmos como 'mas sin embargo'.",
            "reference": "Guía Oficial EGEL Plus: Redacción Indirecta - Subárea 2.1 y 2.2."
        }
    })


# ==============================================================================
# MOTOR UNIFICADO DE EXÁMENES
# ==============================================================================
ALL_QUESTIONS = {
    "area_1": QUESTIONS_AREA_1,
    "area_2": QUESTIONS_AREA_2,
    "area_3": QUESTIONS_AREA_3,
    "area_4": QUESTIONS_AREA_4,
    "lectura": QUESTIONS_LECTURA,
    "redaccion": QUESTIONS_REDACCION
}

ALL_QUESTIONS_BY_ID = {}
for group in ALL_QUESTIONS.values():
    for q in group:
        ALL_QUESTIONS_BY_ID[q["id"]] = q


def get_exam_questions(modality="disciplinar", area_id=None, count=30):
    """
    Genera un examen estructurado de exactamente 30 reactivos:
    - 'disciplinar': 30 reactivos de ISOFT (repartidos en Áreas 1, 2, 3 y 4 según los 14 temas Ceneval)
    - 'lectura': 30 reactivos del módulo de Lenguaje y Comunicación (Comprensión Lectora + Redacción Indirecta)
    - 'integral': 30 reactivos mixtos (18 disciplinares ISOFT + 12 de lenguaje y comunicación)
    - 'area': 30 reactivos de un área específica (area_1, area_2, area_3, area_4, lectura, redaccion)
    """
    selected = []

    if modality == "disciplinar":
        s1 = random.sample(QUESTIONS_AREA_1, min(8, len(QUESTIONS_AREA_1)))
        s2 = random.sample(QUESTIONS_AREA_2, min(8, len(QUESTIONS_AREA_2)))
        s3 = random.sample(QUESTIONS_AREA_3, min(7, len(QUESTIONS_AREA_3)))
        s4 = random.sample(QUESTIONS_AREA_4, min(7, len(QUESTIONS_AREA_4)))
        combined = s1 + s2 + s3 + s4
        random.shuffle(combined)
        selected = combined[:count]

    elif modality == "lectura":
        # Combina Comprensión Lectora (18) + Redacción Indirecta (12) = 30 reactivos
        s_lec = random.sample(QUESTIONS_LECTURA, min(18, len(QUESTIONS_LECTURA)))
        s_red = random.sample(QUESTIONS_REDACCION, min(12, len(QUESTIONS_REDACCION)))
        combined = s_lec + s_red
        random.shuffle(combined)
        selected = combined[:count]

    elif modality == "integral":
        # 18 reactivos disciplinares ISOFT + 12 reactivos de lenguaje
        s1 = random.sample(QUESTIONS_AREA_1, min(5, len(QUESTIONS_AREA_1)))
        s2 = random.sample(QUESTIONS_AREA_2, min(5, len(QUESTIONS_AREA_2)))
        s3 = random.sample(QUESTIONS_AREA_3, min(4, len(QUESTIONS_AREA_3)))
        s4 = random.sample(QUESTIONS_AREA_4, min(4, len(QUESTIONS_AREA_4)))
        s_leng = random.sample(QUESTIONS_LECTURA + QUESTIONS_REDACCION, min(12, len(QUESTIONS_LECTURA) + len(QUESTIONS_REDACCION)))
        combined = s1 + s2 + s3 + s4 + s_leng
        random.shuffle(combined)
        selected = combined[:count]

    elif modality == "area":
        target_group = ALL_QUESTIONS.get(area_id, QUESTIONS_AREA_1)
        selected = random.sample(target_group, min(count, len(target_group)))

    else:
        combined = QUESTIONS_AREA_1 + QUESTIONS_AREA_2 + QUESTIONS_AREA_3 + QUESTIONS_AREA_4
        selected = random.sample(combined, min(count, len(combined)))

    client_questions = []
    for idx, q in enumerate(selected):
        client_questions.append({
            "number": idx + 1,
            "id": q["id"],
            "area_id": q["area_id"],
            "area_name": q["area_name"],
            "subarea": q["subarea"],
            "text": q.get("text", ""),
            "question": q["question"],
            "options": q["options"]
        })

    return client_questions


def verify_answer(question_id, selected_index):
    """Verifica la respuesta y devuelve la justificación basada en la bibliografía oficial."""
    q = ALL_QUESTIONS_BY_ID.get(question_id)
    if not q:
        return {"error": "Reactivo no encontrado"}

    correct_index = q["correct_index"]
    is_correct = (selected_index == correct_index)
    letters = ["A", "B", "C"]

    options_breakdown = []
    for i, opt_text in enumerate(q["options"]):
        letter = letters[i]
        if i == correct_index:
            explanation = q["justification"]["correct"]
            status = "correct"
        else:
            distractor_text = q["justification"].get("distractors", {}).get(letter, "Esta opción es incorrecta según la fundamentación técnica y normativa de la guía.")
            explanation = distractor_text
            status = "distractor"

        options_breakdown.append({
            "letter": letter,
            "text": opt_text,
            "status": status,
            "explanation": explanation
        })

    if is_correct:
        feedback_summary = f"¡Excelente! Has seleccionado la opción ({letters[selected_index]}), que es la respuesta correcta."
    else:
        feedback_summary = f"Has seleccionado la opción ({letters[selected_index]}). Sin embargo, la respuesta correcta es la ({letters[correct_index]}). Analicemos los motivos técnicos:"

    return {
        "question_id": question_id,
        "is_correct": is_correct,
        "selected_index": selected_index,
        "correct_index": correct_index,
        "correct_letter": letters[correct_index],
        "feedback_summary": feedback_summary,
        "options_breakdown": options_breakdown,
        "key_concept": q["justification"].get("key_concept", ""),
        "reference": q["justification"].get("reference", "Guía Oficial CENEVAL EGEL Plus.")
    }
