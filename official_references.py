"""
Catálogo Oficial de Estructura y Bibliografía Sugerida CENEVAL EGEL Plus ISOFT
Fuente: Guía Oficial EGEL Plus en Ingeniería de Software (EGEL Plus ISOFT)
Sección Disciplinar y Sección Transversal de Lenguaje y Comunicación.
"""

# Normas, estándares y marcos legales oficiales
STANDARDS_AND_NORMS = [
    {
        "code": "ISO/IEC 25002:2024",
        "title": "Systems and software engineering. Systems and software Quality Requirements and Evaluation (SQuaRE). Quality model overview and usage.",
        "author": "ISO/IEC",
        "year": "2024",
        "scope": "Evaluación y modelos de calidad de software (sistemas y productos)."
    },
    {
        "code": "ISO/IEC/IEEE 29148:2018(E)",
        "title": "Systems and software engineering: Life cycle processes. Requirements engineering.",
        "author": "ISO/IEC/IEEE International Standard",
        "year": "2018",
        "scope": "Procesos del ciclo de vida e ingeniería de requerimientos."
    },
    {
        "code": "PMBOK 7a ed.",
        "title": "Guía de los fundamentos para la Dirección de Proyectos (Guía del PMBOK®) (7a. ed.)",
        "author": "Project Management Institute (PMI)",
        "year": "2021",
        "scope": "Dirección y gestión de proyectos, tiempos, costos, riesgos y valor."
    }
]

# Estructura del examen oficial CENEVAL EGEL Plus ISOFT (143 disciplinares + 60 lenguaje = 203 totales)
EXAM_STRUCTURE = {
    "total_reactivos": 203,
    "nota": "El examen incluye 15% de reactivos piloto que no se consideran para la calificación.",
    "secciones": [
        {
            "id": "disciplinar",
            "name": "Sección Disciplinar específica de la profesión",
            "total_reactivos": 143,
            "areas": [
                {
                    "id": "area_1",
                    "code": "1",
                    "name": "1. Análisis de Sistemas de Software",
                    "total_reactivos": 31,
                    "definition": "Se abordan los conceptos, técnicas y herramientas para identificar, validar, priorizar y documentar los objetivos y límites del sistema, así como los diferentes tipos de requerimientos que caracterizan su funcionamiento.",
                    "subareas": [
                        {"code": "1.1", "name": "1.1. Tipos de requerimientos", "reactivos": 12},
                        {"code": "1.2", "name": "1.2. Técnicas y herramientas para la obtención, análisis, priorización y validación de requerimientos", "reactivos": 9},
                        {"code": "1.3", "name": "1.3. Técnicas y herramientas de documentación de requerimientos", "reactivos": 10}
                    ]
                },
                {
                    "id": "area_2",
                    "code": "2",
                    "name": "2. Diseño de Sistemas de Software",
                    "total_reactivos": 33,
                    "definition": "Comprende el diseño arquitectónico, el diseño modular, de componentes y estructuras de datos, así como el diseño ergonómico de interfaces de usuario.",
                    "subareas": [
                        {"code": "2.1", "name": "2.1. Diseño arquitectónico de software", "reactivos": 10},
                        {"code": "2.2", "name": "2.2. Diseño de módulos, componentes y de datos de software", "reactivos": 16},
                        {"code": "2.3", "name": "2.3. Diseño de interfaces", "reactivos": 7}
                    ]
                },
                {
                    "id": "area_3",
                    "code": "3",
                    "name": "3. Desarrollo de Sistemas de Software",
                    "total_reactivos": 49,
                    "definition": "Abarca lenguajes de desarrollo, paradigmas de programación, entornos y plataformas de construcción, así como la gestión avanzada de datos relacionales y no relacionales.",
                    "subareas": [
                        {"code": "3.1", "name": "3.1. Lenguajes de desarrollo de software", "reactivos": 10},
                        {"code": "3.2", "name": "3.2. Paradigmas de programación", "reactivos": 10},
                        {"code": "3.3", "name": "3.3. Entornos de desarrollo", "reactivos": 10},
                        {"code": "3.4", "name": "3.4. Gestión de datos", "reactivos": 9},
                        {"code": "3.5", "name": "3.5. Plataformas de desarrollo", "reactivos": 10}
                    ]
                },
                {
                    "id": "area_4",
                    "code": "4",
                    "name": "4. Gestión de Proyectos de Software",
                    "total_reactivos": 30,
                    "definition": "Contempla la estimación de tiempos, costos, riesgos y recursos, estándares de calidad del software y aplicación de metodologías ágiles y tradicionales.",
                    "subareas": [
                        {"code": "4.1", "name": "4.1. Gestión de tiempos, costos, recursos humanos y de riesgo", "reactivos": 8},
                        {"code": "4.2", "name": "4.2. Calidad de software", "reactivos": 10},
                        {"code": "4.3", "name": "4.3. Metodologías de desarrollo", "reactivos": 12}
                    ]
                }
            ]
        },
        {
            "id": "lenguaje_comunicacion",
            "name": "Sección Transversal de Lenguaje y Comunicación (común a todas las profesiones)",
            "total_reactivos": 60,
            "areas": [
                {
                    "id": "comprension_lectora",
                    "name": "Comprensión Lectora",
                    "total_reactivos": 30,
                    "subareas": [
                        {
                            "code": "1.1",
                            "name": "1.1. Ámbito de estudio",
                            "reactivos": 12,
                            "temas": ["Identificación de información", "Interpretación", "Evaluación de la forma y el contenido"]
                        },
                        {
                            "code": "1.2",
                            "name": "1.2. Ámbito literario",
                            "reactivos": 12,
                            "temas": ["Identificación de información", "Interpretación", "Evaluación de la forma y el contenido"]
                        },
                        {
                            "code": "1.3",
                            "name": "1.3. Ámbito de participación social",
                            "reactivos": 6,
                            "temas": ["Identificación de información", "Interpretación", "Evaluación de la forma y el contenido"]
                        }
                    ]
                },
                {
                    "id": "redaccion_indirecta",
                    "name": "Redacción Indirecta",
                    "total_reactivos": 30,
                    "subareas": [
                        {
                            "code": "2.1",
                            "name": "2.1. Ámbito de estudio",
                            "reactivos": 15,
                            "temas": ["Dimensión comunicativa", "Dimensión gramatical y semántica", "Dimensión ortográfica"]
                        },
                        {
                            "code": "2.2",
                            "name": "2.2. Ámbito de participación social",
                            "reactivos": 15,
                            "temas": ["Dimensión comunicativa", "Dimensión gramatical y semántica", "Dimensión ortográfica"]
                        }
                    ]
                }
            ]
        }
    ]
}

# Bibliografía sugerida oficial CENEVAL clasificada por área
OFFICIAL_BIBLIOGRAPHY = {
    "area_1": [
        "Booch, G., Rumbaugh, J., y Jacobson, I. (2005). The unified modeling language user guide (2a ed.). Addison-Wesley Professional.",
        "Davis, A. M. (2013). Just enough requirements management: Where software development meets marketing. Dorset House Publishing.",
        "Gómez, J. (2014). Guía práctica de estimación y medición de proyectos Software. Autor.",
        "Hatton, S. (2008). Choosing the right Prioritisation method. ASWEC '08: Proceedings of the 19th Australian Conference on Software Engineering, 517-526.",
        "ISO/IEC/IEEE International Standard (2018). Systems and software engineering: Life cycle processes. Requirements engineering. ISO/IEC/IEEE 29148:2018(E).",
        "Kerzner, H. (2022). Project management: A systems approach to planning, scheduling, and controlling (13a ed.). Wiley.",
        "McConnell, S. (s.f.). Code complete checklist (2a ed.). Autor.",
        "Patton, J., y Economy, P. (2014). User story mapping: Discover the whole story, build the right product. O'Reilly.",
        "Pressman, R. S., y Maxim, B. (2020). Software engineering: A practitioner's approach (9a ed.). McGraw Hill.",
        "Rohrer, C. (2022). When to use which user-experience research methods. Nielsen Norman Group.",
        "Sommerville, I. (2016). Software engineering (10a ed.). Pearson.",
        "SysML (s.f.). SysML Open Source Project: What is SysML? SysML.",
        "TenStep Latinoamérica (2010). Técnicas de estimación. Blog de Proyectum.",
        "Usman, M., Mendes, E. y Börstler, J. (2015). Effort estimation in agile software development: a survey on the state of the practice. EASE '15.",
        "Visual-Paradigm (s.f.). What is user story? Visual-Paradigm.",
        "Wiegers, K. y Hokanson, C. (2023). Software requirements. Core Practices for Successful Business Analysis. Addison-Wesley.",
        "Wong, S. (2017). Análisis y requerimientos de software. Universidad Continental."
    ],
    "area_2": [
        "Blokdyk, G. (2018). Architecture tradeoff analysis method: A clear and concise reference. Createspace Independent Publishing Platform.",
        "Brown, S. (2020). Software architecture for developers: A developer-friendly guide to software architecture (2a ed.). Autor.",
        "Cervantes, H., Velasco-Elizondo, P. y Castro, L. (2016). Arquitectura de software, conceptos y ciclo de desarrollo. Cengage Learning.",
        "Clements, P., Bachmann, F., Bass, L., Garlan, D., Ivers, J., Little, R., Merson, P., Nord, R. y Stafford, J. (2010). Documenting software architectures, views and beyond (2a ed.). Addison Wesley.",
        "Date, C. J. (2006). Introducción a los sistemas de bases de datos (7a ed.). Pearson Educación; Prentice Hall.",
        "Folmer, E., Gurp, J.V. y Bosch, J. (2003). Scenario-based Assessment of Software Architecture Usability. ICSE Workshop on SE-HCI.",
        "Greenberg, S., Carpendale, S., Marquardt, N. y Buxton, B. (2012). Sketching user experiences: The Workbook. Morgan Kaufmann.",
        "Harrington, J. L. (2016). Relational database design and implementation: Clearly explained. Morgan Kaufmann.",
        "Ingeno, J. (2018). Software architect's handbook. Packt Publishing.",
        "ISO (2024). ISO/IEC 25002:2024. Systems and software engineering. Systems and software Quality Requirements and Evaluation (SQuaRE). ISO; IEC.",
        "Jacko, J. (Ed.) (2012). Human computer interaction handbook: Fundamentals, evolving technologies, and emerging applications (3a ed.). CRC Press.",
        "Jacobson, I., Spence, I. y Bittner, K. (2011). USE-CASE 2.0. The guide to succeeding with use cases. Ivar Jacobson International.",
        "Joyanes, L. y Zahonero, I. (2014). Programación en C, C++, Java y UML (2a ed.). McGraw Hill.",
        "Kruchten, P. (1995). Architectural Blueprints. The '4+1' view model of software architecture. IEEE software 12(6), 42-50.",
        "McCloskey, M. (2014). Turn user goals into task scenarios for usability testing. Nielsen-Norman Group.",
        "Nielsen, J. (2024). 10 usability heuristics for user interface design. Nielsen-Norman Group.",
        "Pascual, J. R. (2019). Acoplamiento y cohesión. Blog Disrupción Tecnológica.",
        "Pernice, K. (2016). UX prototypes: Low fidelity vs. high fidelity. Nielsen-Norman Group.",
        "Suárez, J. y Gutiérrez, L. E. (2016). Tipificación de dominios de requerimientos para la aplicación de patrones arquitectónicos. Información Tecnológica, 27(4), 193-202.",
        "Sweeting, C. (2017). How utterances & slot samples affect intent-matching in Alexa skills. Medium.",
        "Ullman, J. y Widom, J. (2016). Introducción a los sistemas de bases de datos. Prentice Hall."
    ],
    "area_3": [
        "Banahan, M., Brady, D. y Doran, M. (2010). The C Book.",
        "Beaulieu, A. (2020). Learning SQL: Generate, manipulate and retrieve data (3a ed.). O'Reilly.",
        "Burets, A. (2025). PHP vs. Javascript: A short comparison. Scand.",
        "Cano, A. (2019). Programación para principiantes: Guía completa aprende programación paso a paso de la A a la Z. Autor.",
        "Date, C. J. (2001). Introducción a los sistemas de bases de datos (7a ed.). Pearson Educación.",
        "Dean, J. S. y Dean, R. H. (2009). Introducción a la programación con Java. McGraw Hill.",
        "EcuRed (s.f.). Lenguaje de programación Haskell.",
        "Francis, Paul. (2022). Python vs Other Programming Languages in 2024: Detailed Comparison.",
        "Gabbrielli, M. y Martini, S. (2010). Programming Languages: Principles and Paradigms. Springer.",
        "Herrera, J., Gutiérrez, J. y Pulgarín Robinson (2017). Introducción a la Lógica de la programación. EIZZCOM S.A.S.",
        "Juganaru, M. (2014). Introducción a la programación. Patria.",
        "Laudon, J. y Laudon, K. (2016). Sistemas de información gerencial: Administración de la empresa digital (14a ed.). Pearson.",
        "Loy, M., Niemeyer, P. y Leuck, D. (2023). Learning Java (5a ed.). O'Reilly Media.",
        "Martí-Oliet, N., Ortega, Y. y Verdejo, J. A. (2013). Estructuras de datos y métodos algorítmicos: 213 ejercicios resueltos (2a ed.). Garceta.",
        "Meier, A. y Kaufmann, M. (2019). SQL & NoSQL databases: Models, languages, consistency options and architectures for big data management. Springer Vieweg.",
        "O'Hanlon, P. (2019). Advanced TypeScript Programming Projects: Build 9 different apps. Packt Publishing.",
        "Sánchez, J. y Martínez, C. R. (2013). Estructura de datos. ESCOM IPN."
    ],
    "area_4": [
        "Arciniega, F. (2017). Normas y estándares de calidad para el desarrollo de software. UNAM.",
        "Bass, L., Clements, P., y Kazman, R. (2021). Software architecture in practice (4a ed.). Pearson; Addison Wesley.",
        "Boar, B. (2001). The art of strategic planning for information technology. John Wiley & Sons Inc.",
        "Booch, G., Rumbaugh, J. y Jacobson, I. (2008). El proceso unificado de desarrollo de software. Pearson; Addison Wesley.",
        "Campo, R., Campo, M. y Raya, V. R. (2013). Gestión de proyectos. RA-MA.",
        "David, F. R. (2017). Conceptos de Administración Estratégica (15a ed.). Pearson.",
        "Díaz, J. y Robiolo, G. (2014). Método de estimación de costos de un producto de software web. 43 JAIIO - ASSE.",
        "Eeles, P. (2001). Capturing architectural requirements. IBM Rational Developer Works.",
        "Gamboa-Carrascal, J. y Rosado, A. (2019). Diseño de un método ágil de desarrollo de software basado en XP, SCRUM, OPENUP. Revista Ingenio.",
        "García, J. (2018). Estudio comparativo de metodologías, herramientas y wiki de soporte para la gestión de proyectos de desarrollo software. UOC.",
        "Garita-González, G. y Lizano-Madriz, F. Estimación de costo de software: Una propuesta de aplicación pedagógica de COCOMO. Uniciencia.",
        "Maida, E., y Pazienza, J. (2015). Metodologías de desarrollo de software. Universidad Católica Argentina.",
        "Paredes, D., Martínez, L., Bermúdez, R., y Mendoza, S. (2019). Análisis de la metodología RUP en el desarrollo de software académico. Recimundo.",
        "Pavlenko, M. (2024). Technical documentation in software development: Types, best practices, and tools. AltexSoft.",
        "Project Management Institute. (2021). Guía de los fundamentos para la Dirección de Proyectos (Guía del PMBOK®) (7a. ed.).",
        "Sánchez, A., Urban, S. y Rodríguez, D. (2012). Ingeniería del Software: Un enfoque desde la Guía Swebok. Alfaomega.",
        "Schwaber, K. y Sutherland, J. (2020). La guía de Scrum: La guía definitiva de Scrum, las reglas del juego. Scrum Guides.",
        "Wells, D. (2013). Extreme Programming: A gentle introduction. Extreme Programming."
    ],
    "comprension_lectora": [
        "Cassany, D. (2006). Tras las líneas: Sobre la lectura contemporánea. Anagrama.",
        "Carlino, P. (2005). Escribir, leer y aprender en la universidad: Una introducción a la alfabetización académica. Fondo de Cultura Económica.",
        "Solé, I. (2012). Estrategias de lectura (21a ed.). Graó / Colofón.",
        "Parodi, G. (2010). Saber leer. Aguilar / Instituto Cervantes."
    ],
    "redaccion_indirecta": [
        "Real Academia Española y Asociación de Academias de la Lengua Española (2010). Ortografía de la lengua española. Espasa.",
        "Real Academia Española y Asociación de Academias de la Lengua Española (2010). Nueva gramática de la lengua española: manual. Espasa.",
        "Cassany, D. (2014). La cocina de la escritura (22a ed.). Anagrama.",
        "Seco, M. (2011). Diccionario de dudas y dificultades de la lengua española. Espasa."
    ]
}
