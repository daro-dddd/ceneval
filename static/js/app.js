/**
 * EGEL Plus ISOFT - Controlador de la Aplicación (JavaScript Vanilla)
 * Diseñado con bajo acoplamiento, alta accesibilidad cognitiva y cero sobrecarga mental.
 */

const App = (() => {
  // Estado interno de la sesión de estudio
  const state = {
    currentModality: 'disciplinar',
    selectedAreaId: null,
    modalityTitle: 'Simulador Disciplinar ISOFT',
    questions: [],
    currentIndex: 0,
    selectedOptionIndex: null,
    isAnswerChecked: false,
    examId: null, // Identificador de la sesión única de examen
    userAnswers: [], // Historial de reactivos respondidos
    failedQuestions: [], // Reactivos errados para revisión
    reviewIndex: 0,
    deferredPrompt: null // Para instalación PWA
  };

  // Referencias al DOM
  const elements = {};

  /**
   * Inicialización al cargar el documento
   */
  function init() {
    cacheDOMElements();
    initTheme();
    setupPWAInstall();
    setupKeyboardNavigation();
  }

  function cacheDOMElements() {
    // Vistas principales
    elements.viewHome = document.getElementById('view-home');
    elements.viewExam = document.getElementById('view-exam');
    elements.viewResults = document.getElementById('view-results');
    elements.viewReview = document.getElementById('view-review');

    // Modales
    elements.areaModal = document.getElementById('area-selector-modal');
    elements.exitModal = document.getElementById('exit-confirm-modal');
    elements.bibModal = document.getElementById('bibliography-modal');
    elements.bibTabContent = document.getElementById('bib-tab-content');
    elements.tabBtnStandards = document.getElementById('tab-btn-standards');
    elements.tabBtnStructure = document.getElementById('tab-btn-structure');
    elements.tabBtnBooks = document.getElementById('tab-btn-books');

    // Header & PWA
    elements.themeToggleBtn = document.getElementById('btn-toggle-theme');
    elements.themeIconMoon = document.getElementById('theme-icon-moon');
    elements.themeIconSun = document.getElementById('theme-icon-sun');
    elements.pwaInstallBtn = document.getElementById('btn-pwa-install');
    elements.brandHomeBtn = document.getElementById('btn-brand-home');

    // Elementos del examen activo
    elements.examModalityTitle = document.getElementById('exam-modality-title');
    elements.examCounter = document.getElementById('exam-counter');
    elements.examProgressBar = document.getElementById('exam-progress-bar');
    elements.currentQuestionCard = document.getElementById('current-question-card');
    elements.qAreaTag = document.getElementById('q-area-tag');
    elements.qSubareaTag = document.getElementById('q-subarea-tag');
    elements.qReadingPanel = document.getElementById('q-reading-panel');
    elements.qReadingContent = document.getElementById('q-reading-content');
    elements.btnToggleReading = document.getElementById('btn-toggle-reading');
    elements.qPrompt = document.getElementById('q-prompt');
    elements.optionsContainer = document.getElementById('options-container');
    elements.btnCheckAnswer = document.getElementById('btn-check-answer');
    elements.btnNextQuestion = document.getElementById('btn-next-question');
    elements.btnNextQuestionBottom = document.getElementById('btn-next-question-bottom');

    // Panel del Asistente Pedagógico
    elements.assistantFeedbackPanel = document.getElementById('assistant-feedback-panel');
    elements.feedbackBanner = document.getElementById('feedback-banner');
    elements.feedbackBannerIcon = document.getElementById('feedback-banner-icon');
    elements.feedbackBannerTitle = document.getElementById('feedback-banner-title');
    elements.feedbackBannerSummary = document.getElementById('feedback-banner-summary');
    elements.optionsBreakdownContainer = document.getElementById('options-breakdown-container');
    elements.feedbackKeyConcept = document.getElementById('feedback-key-concept');
    elements.feedbackReference = document.getElementById('feedback-reference');
    elements.assistantExtraResponse = document.getElementById('assistant-extra-response');

    // Elementos de Resultados
    elements.resultScoreNum = document.getElementById('result-score-num');
    elements.resultTierBadge = document.getElementById('result-tier-badge');
    elements.resultSubtitle = document.getElementById('result-subtitle');
    elements.resultsBreakdownList = document.getElementById('results-breakdown-list');
    elements.btnReviewFailed = document.getElementById('btn-review-failed');
    elements.countFailedItems = document.getElementById('count-failed-items');
    elements.tutorDiagnosticContainer = document.getElementById('tutor-diagnostic-container');

    // Elementos de Revisión de Fallos
    elements.reviewCounter = document.getElementById('review-counter');
    elements.revAreaTag = document.getElementById('rev-area-tag');
    elements.revSubareaTag = document.getElementById('rev-subarea-tag');
    elements.revReadingPanel = document.getElementById('rev-reading-panel');
    elements.revReadingContent = document.getElementById('rev-reading-content');
    elements.revPrompt = document.getElementById('rev-prompt');
    elements.revOptionsContainer = document.getElementById('rev-options-container');
    elements.revOptionsBreakdown = document.getElementById('rev-options-breakdown');
    elements.revKeyConcept = document.getElementById('rev-key-concept');
    elements.revReference = document.getElementById('rev-reference');
    elements.btnNextReview = document.getElementById('btn-next-review');

    // Event Listeners Base
    elements.themeToggleBtn.addEventListener('click', toggleTheme);
    elements.brandHomeBtn.addEventListener('click', () => {
      if (elements.viewExam.classList.contains('active')) {
        confirmExitExam();
      } else {
        goToHome();
      }
    });
  }

  // =========================================================================
  // GESTIÓN DE TEMA (CLARO / OSCURO)
  // =========================================================================
  function initTheme() {
    const savedTheme = localStorage.getItem('egel_theme') || 
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    setTheme(savedTheme);
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('egel_theme', theme);
    if (theme === 'dark') {
      elements.themeIconMoon.style.display = 'block';
      elements.themeIconSun.style.display = 'none';
    } else {
      elements.themeIconMoon.style.display = 'none';
      elements.themeIconSun.style.display = 'block';
    }
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
  }

  // =========================================================================
  // SOPORTE DE INSTALACIÓN PWA
  // =========================================================================
  function setupPWAInstall() {
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      state.deferredPrompt = e;
      if (elements.pwaInstallBtn) {
        elements.pwaInstallBtn.style.display = 'inline-flex';
        elements.pwaInstallBtn.addEventListener('click', async () => {
          if (state.deferredPrompt) {
            state.deferredPrompt.prompt();
            const { outcome } = await state.deferredPrompt.userChoice;
            console.log('Resultado de instalación PWA:', outcome);
            state.deferredPrompt = null;
            elements.pwaInstallBtn.style.display = 'none';
          }
        });
      }
    });

    window.addEventListener('appinstalled', () => {
      console.log('🎉 PWA instalada exitosamente en el sistema');
      if (elements.pwaInstallBtn) elements.pwaInstallBtn.style.display = 'none';
    });
  }

  // =========================================================================
  // CONTROL DE VISTAS (Navegación limpia sin parpadeos)
  // =========================================================================
  function switchView(viewName) {
    elements.viewHome.classList.remove('active');
    elements.viewExam.classList.remove('active');
    elements.viewResults.classList.remove('active');
    elements.viewReview.classList.remove('active');

    if (viewName === 'home') elements.viewHome.classList.add('active');
    else if (viewName === 'exam') elements.viewExam.classList.add('active');
    else if (viewName === 'results') elements.viewResults.classList.add('active');
    else if (viewName === 'review') elements.viewReview.classList.add('active');

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function goToHome() {
    switchView('home');
  }

  // =========================================================================
  // MODAL DE ÁREA ESPECÍFICA (Modalidad 4)
  // =========================================================================
  function openAreaSelectorModal() {
    elements.areaModal.classList.add('active');
  }

  function closeAreaSelectorModal() {
    elements.areaModal.classList.remove('active');
  }

  function closeAreaModalOnBackdrop(event) {
    if (event.target === elements.areaModal) {
      closeAreaSelectorModal();
    }
  }

  function startAreaSpecificExam() {
    const selectedRadio = document.querySelector('input[name="target-area"]:checked');
    const areaId = selectedRadio ? selectedRadio.value : 'area_1';
    closeAreaSelectorModal();
    startExam('area', areaId);
  }

  // =========================================================================
  // INICIO DE EXAMEN (30 REACTIVOS EXACTOS)
  // =========================================================================
  async function startExam(modality = 'disciplinar', areaId = null) {
    state.currentModality = modality;
    state.selectedAreaId = areaId;
    state.currentIndex = 0;
    state.userAnswers = [];
    state.failedQuestions = [];
    state.selectedOptionIndex = null;
    state.isAnswerChecked = false;

    // Mostrar estado de carga si fuera necesario
    try {
      const response = await fetch('/api/exam/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ modality, area_id: areaId })
      });

      const data = await response.json();
      if (!data.success || !data.questions || data.questions.length === 0) {
        alert('No se pudieron obtener los reactivos del simulador. Por favor intenta de nuevo.');
        return;
      }

      state.examId = data.exam_id || null;
      state.questions = data.questions;
      state.modalityTitle = data.modality_title;
      elements.examModalityTitle.textContent = state.modalityTitle;

      switchView('exam');
      renderCurrentQuestion();
    } catch (error) {
      console.error('Error al iniciar examen:', error);
      alert('Error de conexión con el servidor Python. Asegúrate de ejecutar: python app.py');
    }
  }

  // =========================================================================
  // RENDERIZADO DEL REACTIVO ACTUAL (ESTRICTAMENTE 1 TARJETA A LA VEZ)
  // =========================================================================
  function renderCurrentQuestion() {
    const q = state.questions[state.currentIndex];
    if (!q) return;

    state.selectedOptionIndex = null;
    state.isAnswerChecked = false;

    // Actualizar Contador y Barra de Progreso
    const currentNum = state.currentIndex + 1;
    const total = state.questions.length;
    elements.examCounter.textContent = `Reactivo ${currentNum} de ${total}`;
    
    const progressPercent = (currentNum / total) * 100;
    elements.examProgressBar.style.width = `${progressPercent}%`;

    // Tags de Área y Subárea
    elements.qAreaTag.textContent = q.area_name;
    elements.qSubareaTag.textContent = q.subarea;

    // Panel de Lectura (Comprensión Lectora o Casos de Estudio)
    if (q.text && q.text.trim().length > 0) {
      elements.qReadingContent.textContent = q.text;
      elements.qReadingPanel.style.display = 'block';
      elements.btnToggleReading.textContent = 'Ocultar texto';
      elements.qReadingContent.style.display = 'block';
    } else {
      elements.qReadingPanel.style.display = 'none';
    }

    // Enunciado
    elements.qPrompt.textContent = q.question;

    // Renderizar las 3 Opciones (A, B, C)
    elements.optionsContainer.innerHTML = '';
    const letters = ['A', 'B', 'C'];

    q.options.forEach((optText, idx) => {
      const btn = document.createElement('button');
      btn.className = 'option-button';
      btn.type = 'button';
      btn.id = `opt-btn-${idx}`;
      btn.setAttribute('data-index', idx);

      btn.innerHTML = `
        <span class="option-letter">${letters[idx]}</span>
        <span class="option-text">${optText}</span>
      `;

      btn.addEventListener('click', () => selectOption(idx));
      elements.optionsContainer.appendChild(btn);
    });

    // Resetear Botones de Acción
    elements.btnCheckAnswer.disabled = true;
    elements.btnCheckAnswer.style.display = 'inline-flex';
    elements.btnNextQuestion.style.display = 'none';

    // Ocultar panel de Asistente Pedagógico
    elements.assistantFeedbackPanel.classList.remove('active');
    elements.assistantFeedbackPanel.style.display = 'none';
    elements.assistantExtraResponse.style.display = 'none';
    elements.assistantExtraResponse.textContent = '';

    // Scroll suave al inicio de la tarjeta para máxima concentración
    elements.currentQuestionCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function toggleReadingVisibility() {
    if (elements.qReadingContent.style.display === 'none') {
      elements.qReadingContent.style.display = 'block';
      elements.btnToggleReading.textContent = 'Ocultar texto';
    } else {
      elements.qReadingContent.style.display = 'none';
      elements.btnToggleReading.textContent = 'Mostrar texto';
    }
  }

  // =========================================================================
  // SELECCIÓN Y COMPROBACIÓN DE RESPUESTA
  // =========================================================================
  function selectOption(index) {
    if (state.isAnswerChecked) return; // Ya comprobado, bloqueado

    state.selectedOptionIndex = index;

    // Actualizar clases activas en los botones
    const buttons = elements.optionsContainer.querySelectorAll('.option-button');
    buttons.forEach((btn, idx) => {
      if (idx === index) {
        btn.classList.add('selected');
      } else {
        btn.classList.remove('selected');
      }
    });

    // Habilitar botón de comprobar
    elements.btnCheckAnswer.disabled = false;
  }

  async function checkCurrentAnswer() {
    if (state.selectedOptionIndex === null || state.isAnswerChecked) return;

    state.isAnswerChecked = true;
    elements.btnCheckAnswer.disabled = true;

    const q = state.questions[state.currentIndex];

    try {
      const response = await fetch('/api/exam/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          exam_id: state.examId,
          question_id: q.id,
          selected_index: state.selectedOptionIndex
        })
      });

      const data = await response.json();
      if (!data.success) {
        alert('Error al verificar la respuesta: ' + (data.error || ''));
        return;
      }

      const result = data.result;

      // Registrar respuesta en el historial de la sesión
      const answerRecord = {
        question: q,
        selectedIndex: state.selectedOptionIndex,
        isCorrect: result.is_correct,
        verificationData: result
      };
      state.userAnswers.push(answerRecord);

      if (!result.is_correct) {
        state.failedQuestions.push(answerRecord);
      }

      // 1. Resaltar Opciones en la Interfaz (Verde para correcta, Rojo para la incorrecta elegida)
      const buttons = elements.optionsContainer.querySelectorAll('.option-button');
      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === result.correct_index) {
          btn.classList.add('is-correct');
          btn.querySelector('.option-letter').innerHTML = '✓';
        } else if (idx === state.selectedOptionIndex && !result.is_correct) {
          btn.classList.add('is-wrong');
          btn.querySelector('.option-letter').innerHTML = '✕';
        } else {
          btn.classList.add('is-dimmed');
        }
      });

      // 2. Rellenar Panel del Asistente Pedagógico Inmediato
      displayPedagogicalFeedback(result);

      // 3. Transformar Botón de Acción a "Siguiente Reactivo"
      elements.btnCheckAnswer.style.display = 'none';
      elements.btnNextQuestion.style.display = 'inline-flex';

      const isLastQuestion = (state.currentIndex === state.questions.length - 1);
      const nextBtnContent = isLastQuestion ? `
        <span>Ver Resultados Finales 🏆</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
      ` : `
        <span>Siguiente reactivo</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      `;

      elements.btnNextQuestion.innerHTML = nextBtnContent;
      if (elements.btnNextQuestionBottom) {
        elements.btnNextQuestionBottom.innerHTML = nextBtnContent;
      }

    } catch (err) {
      console.error('Error al comprobar respuesta:', err);
      alert('Error de comunicación con el backend');
      elements.btnCheckAnswer.disabled = false;
    }
  }

  function displayPedagogicalFeedback(result) {
    // Banner de Estado
    if (result.is_correct) {
      elements.feedbackBanner.className = 'feedback-banner correct';
      elements.feedbackBannerIcon.textContent = '✔️';
      elements.feedbackBannerTitle.textContent = '¡Correcto!';
    } else {
      elements.feedbackBanner.className = 'feedback-banner incorrect';
      elements.feedbackBannerIcon.textContent = '❌';
      elements.feedbackBannerTitle.textContent = 'Respuesta Incorrecta';
    }
    elements.feedbackBannerSummary.textContent = result.feedback_summary;

    // Desglose técnico de cada una de las 3 opciones (Rigor Ceneval)
    elements.optionsBreakdownContainer.innerHTML = '';
    result.options_breakdown.forEach((item) => {
      const argDiv = document.createElement('div');
      argDiv.className = `arg-item ${item.status}`;
      argDiv.innerHTML = `
        <strong>Opción ${item.letter}: ${item.text}</strong><br>
        <span>${item.explanation}</span>
      `;
      elements.optionsBreakdownContainer.appendChild(argDiv);
    });

    // Concepto Clave y Referencia Oficial
    elements.feedbackKeyConcept.textContent = result.key_concept;
    elements.feedbackReference.textContent = result.reference;

    // Mostrar el panel con animación suave
    elements.assistantFeedbackPanel.style.display = 'block';
    setTimeout(() => {
      elements.assistantFeedbackPanel.classList.add('active');
      elements.assistantFeedbackPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 50);
  }

  // =========================================================================
  // CONSULTAS ADICIONALES AL ASISTENTE (Analogía, Mnemotecnia, Práctica)
  // =========================================================================
  async function askAssistantExtra(queryType) {
    const q = state.questions[state.currentIndex];
    if (!q) return;

    elements.assistantExtraResponse.style.display = 'block';
    elements.assistantExtraResponse.textContent = 'El Asistente Pedagógico está estructurando tu respuesta...';

    try {
      const response = await fetch('/api/assistant/explain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question_id: q.id,
          query_type: queryType
        })
      });

      const data = await response.json();
      if (data.success) {
        elements.assistantExtraResponse.innerHTML = data.explanation.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      } else {
        elements.assistantExtraResponse.textContent = 'No fue posible generar la respuesta adicional en este momento.';
      }
    } catch (err) {
      elements.assistantExtraResponse.textContent = 'Error de conexión con el Asistente.';
    }
  }

  // =========================================================================
  // PASO AL SIGUIENTE REACTIVO O PANTALLA FINAL
  // =========================================================================
  function goToNextQuestion() {
    if (state.currentIndex < state.questions.length - 1) {
      state.currentIndex++;
      renderCurrentQuestion();
    } else {
      // Fin del examen de 30 reactivos
      showResultsScreen();
    }
  }

  // =========================================================================
  // PANTALLA DE RESULTADOS FINAL (Tras responder el reactivo 30)
  // =========================================================================
  function showResultsScreen() {
    switchView('results');

    const total = state.userAnswers.length;
    const correctCount = state.userAnswers.filter(a => a.isCorrect).length;
    const percentage = total > 0 ? ((correctCount / total) * 100).toFixed(1) : 0;

    elements.resultScoreNum.textContent = correctCount;
    elements.countFailedItems.textContent = state.failedQuestions.length;

    // Desactivar botón de revisar fallos si obtuvo 30 de 30
    if (state.failedQuestions.length === 0) {
      elements.btnReviewFailed.disabled = true;
      elements.btnReviewFailed.style.opacity = '0.5';
    } else {
      elements.btnReviewFailed.disabled = false;
      elements.btnReviewFailed.style.opacity = '1';
    }

    // Escala Oficial CENEVAL: Sobresaliente (>= 80%), Satisfactorio (>= 60%), Aún no satisfactorio (< 60%)
    if (percentage >= 80) {
      elements.resultTierBadge.className = 'performance-tier-badge sobresaliente';
      elements.resultTierBadge.innerHTML = '🌟 Nivel Sobresaliente (D-SS) • ' + percentage + '%';
      elements.resultSubtitle.textContent = '¡Felicidades! Tu dominio técnico cumple con el estándar de excelencia para alcanzar testimonio de desempeño sobresaliente.';
    } else if (percentage >= 60) {
      elements.resultTierBadge.className = 'performance-tier-badge satisfactorio';
      elements.resultTierBadge.innerHTML = '✅ Nivel Satisfactorio (D-S) • ' + percentage + '%';
      elements.resultSubtitle.textContent = 'Aprobado satisfactoriamente. Estás por encima del umbral de acreditación CENEVAL; repasa los reactivos fallados para consolidar temas clave.';
    } else {
      elements.resultTierBadge.className = 'performance-tier-badge no-satisfactorio';
      elements.resultTierBadge.innerHTML = '📚 Aún No Satisfactorio (ANS) • ' + percentage + '%';
      elements.resultSubtitle.textContent = 'Se identificaron oportunidades de mejora en conceptos fundamentales. Utiliza el botón de revisión para estudiar las justificaciones de cada fallo.';
    }

    // Desglose por Áreas y Subáreas con barras de progreso simples
    renderBreakdownStats();

    // Cargar Diagnóstico Pedagógico del Tutor CENEVAL ("Tienes que reforzar en estas áreas...")
    loadTutorDiagnostic();
  }

  function renderBreakdownStats() {
    const areaStats = {};

    state.userAnswers.forEach(ans => {
      const areaName = ans.question.area_name;
      if (!areaStats[areaName]) {
        areaStats[areaName] = { total: 0, correct: 0 };
      }
      areaStats[areaName].total++;
      if (ans.isCorrect) areaStats[areaName].correct++;
    });

    elements.resultsBreakdownList.innerHTML = '';

    Object.keys(areaStats).forEach(areaName => {
      const stat = areaStats[areaName];
      const pct = Math.round((stat.correct / stat.total) * 100);

      const itemDiv = document.createElement('div');
      itemDiv.className = 'area-progress-item';
      itemDiv.innerHTML = `
        <div class="area-progress-header">
          <span class="area-progress-name">${areaName}</span>
          <span class="area-progress-stat">${stat.correct} / ${stat.total} (${pct}%)</span>
        </div>
        <div class="area-bar-track">
          <div class="area-bar-fill" style="width: ${pct}%;"></div>
        </div>
      `;
      elements.resultsBreakdownList.appendChild(itemDiv);
    });
  }

  // =========================================================================
  // DIAGNÓSTICO DEL TUTOR PEDAGÓGICO CENEVAL (Áreas a Reforzar + Bibliografía)
  // =========================================================================
  async function loadTutorDiagnostic() {
    if (!elements.tutorDiagnosticContainer) return;

    elements.tutorDiagnosticContainer.innerHTML = `
      <div class="tutor-diagnostic-card">
        <div class="tutor-header-wrapper">
          <div class="tutor-avatar-icon">👨‍🏫</div>
          <div class="tutor-header-text">
            <h3>Tutor Pedagógico CENEVAL</h3>
            <p>Generando diagnóstico técnico y analizando áreas prioritarias de refuerzo...</p>
          </div>
        </div>
      </div>
    `;

    try {
      const response = await fetch('/api/exam/tutor-diagnostic', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          exam_id: state.examId,
          user_answers: state.userAnswers
        })
      });

      const data = await response.json();
      if (!data.success || !data.diagnostic) {
        elements.tutorDiagnosticContainer.innerHTML = '';
        return;
      }

      renderTutorDiagnostic(data.diagnostic);
    } catch (err) {
      console.error('Error al obtener diagnóstico del tutor:', err);
      elements.tutorDiagnosticContainer.innerHTML = '';
    }
  }

  function renderTutorDiagnostic(diag) {
    if (!elements.tutorDiagnosticContainer) return;

    const hasReinforce = diag.areas_to_reinforce && diag.areas_to_reinforce.length > 0;
    const hasMastered = diag.areas_mastered && diag.areas_mastered.length > 0;

    let reinforceHtml = '';
    if (hasReinforce) {
      reinforceHtml = `
        <div class="tutor-reinforce-section">
          <div style="font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🎯</span>
            <span>Tienes que reforzar en estas áreas:</span>
          </div>
          ${diag.areas_to_reinforce.map(area => {
            const subareasHtml = area.failed_subareas && area.failed_subareas.length > 0 ? `
              <div class="tutor-subareas-list">
                ${area.failed_subareas.map(sub => `
                  <div class="tutor-subarea-item">
                    <span>📌 <strong>${sub.name}</strong></span>
                    <span class="failed-tag">${sub.failed_count} ${sub.failed_count === 1 ? 'reactivo fallado' : 'reactivos fallados'}</span>
                  </div>
                `).join('')}
              </div>
            ` : '';

            const conceptsHtml = area.concepts_to_review && area.concepts_to_review.length > 0 ? `
              <div class="tutor-concepts-box">
                <strong style="color: var(--text-primary);">💡 Conceptos técnicos clave a repasar:</strong><br>
                ${area.concepts_to_review.map(c => `• ${c}`).join('<br>')}
              </div>
            ` : '';

            const booksHtml = area.recommended_reading && area.recommended_reading.length > 0 ? `
              <div class="tutor-reading-recommendation">
                <strong>📚 Bibliografía oficial recomendada por el CENEVAL para esta área:</strong>
                <ul style="margin: 0.4rem 0 0 1.25rem; padding: 0;">
                  ${area.recommended_reading.map(b => `<li style="margin-bottom: 0.25rem;">${b}</li>`).join('')}
                </ul>
              </div>
            ` : '';

            return `
              <div class="tutor-reinforce-card">
                <div class="tutor-reinforce-header">
                  <div class="tutor-reinforce-title">
                    <span>⚠️</span>
                    <span>${area.area_name}</span>
                  </div>
                  <span class="tutor-reinforce-badge">${area.failed_count} ${area.failed_count === 1 ? 'fallo' : 'fallos'} (${area.percentage}% acierto)</span>
                </div>
                ${subareasHtml}
                ${conceptsHtml}
                ${booksHtml}
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    let masteredHtml = '';
    if (hasMastered) {
      const names = diag.areas_mastered.map(m => m.area_name).join(', ');
      masteredHtml = `
        <div class="tutor-mastered-box">
          <span style="font-size: 1.35rem;">🏆</span>
          <div>
            <strong>Áreas con alto dominio acreditado:</strong> ${names}. ¡Excelente comprensión conceptual!
          </div>
        </div>
      `;
    }

    const formattedMsg = (diag.tutor_message || '')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    elements.tutorDiagnosticContainer.innerHTML = `
      <div class="tutor-diagnostic-card">
        <div class="tutor-header-wrapper">
          <div class="tutor-avatar-icon">👨‍🏫</div>
          <div class="tutor-header-text">
            <h3>Tutor Pedagógico CENEVAL</h3>
            <p>${formattedMsg}</p>
          </div>
        </div>
        ${reinforceHtml}
        ${masteredHtml}
      </div>
    `;
  }

  function restartExamSameModality() {
    startExam(state.currentModality, state.selectedAreaId);
  }

  function finishExamEarly() {
    if (state.userAnswers.length === 0) {
      alert('Por favor responde y comprueba al menos un reactivo para que el Tutor Pedagógico pueda analizar tu desempeño.');
      return;
    }
    showResultsScreen();
  }

  // =========================================================================
  // MODO REVISIÓN DE REACTIVOS FALLADOS (Sin estrés, paso a paso)
  // =========================================================================
  function startReviewMode() {
    if (state.failedQuestions.length === 0) return;
    state.reviewIndex = 0;
    switchView('review');
    renderCurrentReviewItem();
  }

  function renderCurrentReviewItem() {
    const item = state.failedQuestions[state.reviewIndex];
    if (!item) return;

    const q = item.question;
    const v = item.verificationData;
    const letters = ['A', 'B', 'C'];

    elements.reviewCounter.textContent = `Revisando reactivo fallado ${state.reviewIndex + 1} de ${state.failedQuestions.length}`;
    elements.revAreaTag.textContent = q.area_name;
    elements.revSubareaTag.textContent = q.subarea;

    if (q.text && q.text.trim().length > 0) {
      elements.revReadingContent.textContent = q.text;
      elements.revReadingPanel.style.display = 'block';
    } else {
      elements.revReadingPanel.style.display = 'none';
    }

    elements.revPrompt.textContent = q.question;

    // Renderizar opciones con indicadores
    elements.revOptionsContainer.innerHTML = '';
    q.options.forEach((optText, idx) => {
      const btn = document.createElement('div');
      btn.className = 'option-button';
      btn.style.cursor = 'default';

      if (idx === v.correct_index) {
        btn.classList.add('is-correct');
        btn.innerHTML = `
          <span class="option-letter">✓</span>
          <span class="option-text"><strong>${optText}</strong> (Respuesta Correcta)</span>
        `;
      } else if (idx === item.selectedIndex) {
        btn.classList.add('is-wrong');
        btn.innerHTML = `
          <span class="option-letter">✕</span>
          <span class="option-text"><strong>${optText}</strong> (Tu respuesta seleccionada)</span>
        `;
      } else {
        btn.classList.add('is-dimmed');
        btn.innerHTML = `
          <span class="option-letter">${letters[idx]}</span>
          <span class="option-text">${optText}</span>
        `;
      }
      elements.revOptionsContainer.appendChild(btn);
    });

    // Argumentaciones
    elements.revOptionsBreakdown.innerHTML = '';
    v.options_breakdown.forEach((b) => {
      const div = document.createElement('div');
      div.className = `arg-item ${b.status}`;
      div.innerHTML = `
        <strong>Opción ${b.letter}: ${b.text}</strong><br>
        <span>${b.explanation}</span>
      `;
      elements.revOptionsBreakdown.appendChild(div);
    });

    elements.revKeyConcept.textContent = v.key_concept;
    elements.revReference.textContent = v.reference;

    // Configurar botón siguiente
    if (state.reviewIndex === state.failedQuestions.length - 1) {
      elements.btnNextReview.innerHTML = `
        <span>Finalizar Revisión</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
      `;
    } else {
      elements.btnNextReview.innerHTML = `
        <span>Siguiente reactivo fallado</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      `;
    }
  }

  function goToNextReviewItem() {
    if (state.reviewIndex < state.failedQuestions.length - 1) {
      state.reviewIndex++;
      renderCurrentReviewItem();
    } else {
      exitReviewMode();
    }
  }

  function exitReviewMode() {
    switchView('results');
  }

  // =========================================================================
  // CONFIRMACIÓN PARA SALIR DEL EXAMEN
  // =========================================================================
  function confirmExitExam() {
    elements.exitModal.classList.add('active');
  }

  function cancelExitModal() {
    elements.exitModal.classList.remove('active');
  }

  function confirmExitNow() {
    elements.exitModal.classList.remove('active');
    goToHome();
  }

  // =========================================================================
  // GESTIÓN DEL MODAL DE BIBLIOGRAFÍA Y ESTRUCTURA OFICIAL CENEVAL
  // =========================================================================
  async function openBibliographyModal() {
    elements.bibModal.classList.add('active');
    if (!state.officialReferences) {
      await fetchOfficialReferences();
    }
    showBibTab(state.currentBibTab || 'standards');
  }

  function closeBibliographyModal() {
    elements.bibModal.classList.remove('active');
  }

  function closeBibliographyModalOnBackdrop(event) {
    if (event.target === elements.bibModal) {
      closeBibliographyModal();
    }
  }

  async function fetchOfficialReferences() {
    try {
      elements.bibTabContent.innerHTML = '<p style="color:var(--text-muted);">Cargando catálogo oficial CENEVAL...</p>';
      const res = await fetch('/api/official-references');
      const data = await res.json();
      if (data.success) {
        state.officialReferences = data;
      }
    } catch (err) {
      elements.bibTabContent.innerHTML = '<p style="color:var(--color-error);">Error al cargar las referencias oficiales.</p>';
    }
  }

  function showBibTab(tabName) {
    state.currentBibTab = tabName;
    if (!state.officialReferences) return;

    // Resaltar botón activo
    [elements.tabBtnStandards, elements.tabBtnStructure, elements.tabBtnBooks].forEach(btn => {
      btn.style.backgroundColor = 'var(--bg-secondary)';
      btn.style.borderColor = 'var(--border-subtle)';
    });

    if (tabName === 'standards') {
      elements.tabBtnStandards.style.backgroundColor = 'var(--accent-light)';
      elements.tabBtnStandards.style.borderColor = 'var(--accent-primary)';
      renderBibStandards();
    } else if (tabName === 'structure') {
      elements.tabBtnStructure.style.backgroundColor = 'var(--accent-light)';
      elements.tabBtnStructure.style.borderColor = 'var(--accent-primary)';
      renderBibStructure();
    } else if (tabName === 'books') {
      elements.tabBtnBooks.style.backgroundColor = 'var(--accent-light)';
      elements.tabBtnBooks.style.borderColor = 'var(--accent-primary)';
      renderBibBooks();
    }
  }

  function renderBibStandards() {
    const list = state.officialReferences.standards;
    let html = `
      <h4 style="font-size:1.05rem; margin-bottom:0.75rem; color:var(--text-primary);">
        🏛️ Referencias Normativas, Legales o de Estándares Oficiales
      </h4>
      <div style="display:flex; flex-direction:column; gap:0.85rem;">
    `;
    list.forEach(std => {
      html += `
        <div style="padding:1rem; border-radius:var(--radius-md); background:var(--bg-secondary); border:1px solid var(--border-subtle); border-left:4px solid var(--accent-primary);">
          <div style="font-weight:700; color:var(--accent-primary); font-size:0.95rem;">${std.code} (${std.year})</div>
          <div style="font-size:0.9rem; margin:0.35rem 0; color:var(--text-primary); font-weight:500;">${std.title}</div>
          <div style="font-size:0.825rem; color:var(--text-muted);">Ámbito de aplicación: ${std.scope}</div>
        </div>
      `;
    });
    html += '</div>';
    elements.bibTabContent.innerHTML = html;
  }

  function renderBibStructure() {
    const struct = state.officialReferences.exam_structure;
    let html = `
      <h4 style="font-size:1.05rem; margin-bottom:0.5rem; color:var(--text-primary);">
        📊 Estructura General del Examen (${struct.total_reactivos} reactivos)
      </h4>
      <p style="font-size:0.825rem; color:var(--text-muted); margin-bottom:1rem;">${struct.nota}</p>
    `;

    struct.secciones.forEach(sec => {
      html += `
        <div style="margin-bottom:1.5rem; background:var(--bg-secondary); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1rem 1.25rem;">
          <h5 style="font-size:1rem; color:var(--accent-primary); margin-bottom:0.75rem;">
            ${sec.name} (${sec.total_reactivos} reactivos)
          </h5>
          <div style="display:flex; flex-direction:column; gap:0.75rem;">
      `;

      sec.areas.forEach(ar => {
        html += `
          <div style="padding:0.75rem; background:var(--bg-tertiary); border-radius:var(--radius-sm);">
            <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.9rem;">
              <span>${ar.name}</span>
              <span style="color:var(--accent-primary);">${ar.total_reactivos} reactivos</span>
            </div>
            ${ar.definition ? `<p style="font-size:0.8rem; color:var(--text-secondary); margin:0.35rem 0;">${ar.definition}</p>` : ''}
            <ul style="margin-left:1.25rem; font-size:0.8rem; color:var(--text-muted); margin-top:0.35rem;">
              ${ar.subareas.map(s => `<li>${s.name} (${s.reactivos} reactivos)</li>`).join('')}
            </ul>
          </div>
        `;
      });

      html += '</div></div>';
    });

    elements.bibTabContent.innerHTML = html;
  }

  function renderBibBooks() {
    const bib = state.officialReferences.bibliography;
    const areaTitles = {
      "area_1": "Área 1: Análisis de Sistemas de Software",
      "area_2": "Área 2: Diseño de Sistemas de Software",
      "area_3": "Área 3: Desarrollo de Sistemas de Software",
      "area_4": "Área 4: Gestión de Proyectos de Software"
    };

    let html = `
      <h4 style="font-size:1.05rem; margin-bottom:0.75rem; color:var(--text-primary);">
        📖 Bibliografía Sugerida por Área Disciplinar (Guía Oficial)
      </h4>
      <div style="display:flex; flex-direction:column; gap:1.25rem;">
    `;

    Object.keys(bib).forEach(key => {
      html += `
        <div style="background:var(--bg-secondary); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1rem 1.25rem;">
          <h5 style="font-size:0.95rem; color:var(--accent-primary); margin-bottom:0.5rem; font-weight:700;">
            ${areaTitles[key]}
          </h5>
          <ol style="margin-left:1.25rem; font-size:0.825rem; line-height:1.6; color:var(--text-secondary);">
            ${bib[key].map(book => `<li style="margin-bottom:0.35rem;">${book}</li>`).join('')}
          </ol>
        </div>
      `;
    });

    html += '</div>';
    elements.bibTabContent.innerHTML = html;
  }

  // =========================================================================
  // NAVEGACIÓN POR TECLADO (Accesibilidad: teclas 1, 2, 3 o A, B, C y Enter)
  // =========================================================================
  function setupKeyboardNavigation() {
    window.addEventListener('keydown', (e) => {
      if (!elements.viewExam.classList.contains('active')) return;

      const key = e.key.toUpperCase();
      if (['1', 'A'].includes(key)) selectOption(0);
      else if (['2', 'B'].includes(key)) selectOption(1);
      else if (['3', 'C'].includes(key)) selectOption(2);
      else if (e.key === 'Enter') {
        if (!state.isAnswerChecked && state.selectedOptionIndex !== null) {
          checkCurrentAnswer();
        } else if (state.isAnswerChecked) {
          goToNextQuestion();
        }
      }
    });
  }

  // API Pública
  return {
    init,
    startExam,
    openAreaSelectorModal,
    closeAreaSelectorModal,
    closeAreaModalOnBackdrop,
    openBibliographyModal,
    closeBibliographyModal,
    closeBibliographyModalOnBackdrop,
    showBibTab,
    startAreaSpecificExam,
    toggleReadingVisibility,
    checkCurrentAnswer,
    goToNextQuestion,
    askAssistantExtra,
    restartExamSameModality,
    finishExamEarly,
    showResultsScreen,
    startReviewMode,
    goToNextReviewItem,
    exitReviewMode,
    confirmExitExam,
    cancelExitModal,
    confirmExitNow,
    goToHome
  };
})();

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', App.init);
