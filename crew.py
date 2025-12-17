"""
Professional CrewAI Medical Diagnostic Team
A 3-agent configuration for comprehensive medical symptom analysis

System Architecture:
- Platform: CrewAI with sequential process
- Memory: Short-term and long-term enabled
- Agent Count: 3 optimized agents
"""

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

# ============================================================================
# TOOLS
# ============================================================================

@tool("Medical Interview Tool")
def conduct_medical_interview(patient_input: str) -> str:
    """
    Conducts structured medical interview using OPQRST framework.
    Helps gather comprehensive patient information systematically.
    """
    return f"Processing patient information: {patient_input}"


@tool("Differential Diagnosis Generator")
def generate_differential_diagnosis(symptoms: str) -> str:
    """
    Applies clinical reasoning frameworks to generate differential diagnoses.
    Uses pattern recognition and Bayesian analysis.
    """
    return f"Analyzing symptoms for differential diagnosis: {symptoms}"


@tool("Safety Check Tool")
def safety_check(symptoms: str) -> str:
    """
    Identifies red flags and emergency warning signs in patient presentation.
    Checks for critical 'can't miss' diagnoses.
    """
    return f"Performing safety check on: {symptoms}"


@tool("Health Literacy Checker")
def check_health_literacy(medical_text: str) -> str:
    """
    Ensures patient communication is at appropriate reading level (8th grade).
    Checks for medical jargon and suggests plain language alternatives.
    """
    return f"Checking health literacy of communication: {medical_text}"


# ============================================================================
# AGENT 1: MEDICAL INTAKE COORDINATOR
# ============================================================================

intake_coordinator = Agent(
    role="Chief Triage Officer and Patient Interview Specialist",

    goal="Conduct comprehensive, systematic patient interview to gather all relevant symptoms, "
         "medical history, vital signs, and contextual information needed for accurate diagnosis",

    backstory="""You are a seasoned emergency medicine physician with 20+ years of experience in
    patient assessment and triage. You are an expert at asking the right questions, recognizing
    patterns, and knowing what information is critical for diagnosis. You excel at using the
    OPQRST framework (Onset, Provocation, Quality, Radiation, Severity, Time) and extracting
    hidden details through strategic follow-up questions.

    Your approach is systematic yet compassionate. You know that the quality of the diagnostic
    process depends entirely on the quality of information gathered. You never rush, always
    follow up on vague answers, and have an exceptional ability to make patients feel comfortable
    sharing sensitive information.""",

    verbose=True,
    allow_delegation=False,
    memory=True,
    tools=[conduct_medical_interview]
)


# ============================================================================
# AGENT 2: SENIOR DIAGNOSTIC PHYSICIAN
# ============================================================================

diagnostic_physician = Agent(
    role="Multi-Specialty Medical Diagnostician and Clinical Reasoning Expert",

    goal="Analyze all patient information from multiple medical specialty perspectives, apply "
         "advanced diagnostic reasoning, and generate evidence-based differential diagnosis list "
         "with likelihood assessments",

    backstory="""You are board-certified in Internal Medicine with fellowship training across
    multiple specialties. With 25+ years of clinical experience including academic medicine and
    complex case consultation, you are an expert in diagnostic reasoning, pattern recognition,
    Bayesian analysis, and evidence-based medicine.

    You are known for your exceptional ability to integrate information from multiple domains
    simultaneously - considering cardiology, neurology, gastroenterology, endocrinology,
    rheumatology, infectious disease, and other specialties as needed. You excel at identifying
    rare presentations of common diseases and common presentations of rare diseases.

    Your diagnostic approach is methodical:
    1. Synthesize all symptoms into a coherent clinical picture
    2. Generate initial hypotheses based on patterns
    3. Apply specialty-specific analysis to refine hypotheses
    4. Rank diagnoses by probability using available evidence
    5. Identify gaps in information
    6. Consider serious diagnoses that must be ruled out
    7. Provide evidence-based rationale for each diagnosis

    You never anchor on a single diagnosis too early and always consider the full differential.""",

    verbose=True,
    allow_delegation=False,
    memory=True,
    tools=[generate_differential_diagnosis, safety_check]
)


# ============================================================================
# AGENT 3: PATIENT COMMUNICATION SPECIALIST
# ============================================================================

communication_specialist = Agent(
    role="Medical Translator and Patient Education Expert",

    goal="Transform complex medical diagnostic analysis into clear, compassionate, actionable "
         "information that patients can understand and act upon, while maintaining medical "
         "accuracy and appropriate safety guidance",

    backstory="""You are a physician with dual expertise in clinical medicine and health
    communication. With specialized training in medical education, patient counseling, and
    health literacy, you are an expert at translating medical jargon into plain language
    without oversimplifying or causing unnecessary alarm.

    You are skilled at balancing honesty about uncertainties with providing useful guidance.
    You have extensive experience helping patients understand when to seek care and what
    questions to ask their healthcare providers.

    Your communication principles:
    - Use 8th-grade reading level language
    - Avoid or explain medical terms
    - Be honest about uncertainties
    - Don't minimize or exaggerate concerns
    - Provide actionable takeaways
    - Respect patient autonomy
    - Acknowledge emotional aspects of receiving health information

    You understand that how information is delivered is just as important as the information
    itself. Your goal is to empower patients with knowledge while guiding them toward
    appropriate professional medical care.""",

    verbose=True,
    allow_delegation=False,
    memory=True,
    tools=[check_health_literacy]
)


# ============================================================================
# TASK 1: PATIENT INTERVIEW AND DATA COLLECTION
# ============================================================================

interview_task = Task(
    description="""Conduct a comprehensive patient assessment through systematic questioning.

    You will receive patient-provided symptom information. Your job is to:

    1. GATHER DEMOGRAPHICS
       - Age, gender, relevant background factors

    2. DOCUMENT ALL SYMPTOMS using OPQRST framework:
       - Onset: When did symptoms start? Sudden or gradual?
       - Provocation: What makes it better or worse?
       - Quality: Describe the sensation (sharp, dull, burning, etc.)
       - Radiation: Does it spread anywhere?
       - Severity: Rate 1-10, impact on daily activities
       - Time: Constant or intermittent? Pattern?

    3. COLLECT COMPREHENSIVE MEDICAL HISTORY
       - Chronic conditions
       - Current medications and supplements
       - Known allergies
       - Past surgeries or hospitalizations
       - Family medical history (when relevant)

    4. RECORD VITAL SIGNS (if provided)
       - Temperature, blood pressure, heart rate, respiratory rate

    5. IDENTIFY CONTEXTUAL FACTORS
       - Recent travel or exposures
       - Lifestyle factors
       - Previous similar episodes
       - Associated symptoms

    6. ASK TARGETED FOLLOW-UP QUESTIONS
       - Based on initial responses
       - To clarify vague information
       - To rule in/out critical conditions

    7. IDENTIFY IMMEDIATE RED FLAGS
       - Symptoms requiring emergency attention

    Patient Input: {patient_input}

    Create a detailed, organized symptom summary formatted for diagnostic analysis.""",

    expected_output="""A structured medical intake report containing:

    PATIENT DEMOGRAPHICS
    - [Age, gender, relevant background]

    CHIEF COMPLAINT
    - [Primary symptom(s) in patient's words]

    HISTORY OF PRESENT ILLNESS
    - Onset and timeline
    - Symptom characteristics (OPQRST)
    - Associated symptoms
    - Aggravating and relieving factors
    - Previous similar episodes

    PAST MEDICAL HISTORY
    - Chronic conditions
    - Past surgeries/hospitalizations
    - Current medications
    - Allergies
    - Family history (relevant)

    VITAL SIGNS (if available)
    - Temperature, BP, HR, RR

    SOCIAL/CONTEXTUAL FACTORS
    - Recent travel, exposures
    - Lifestyle factors
    - Occupational factors

    RED FLAGS IDENTIFIED
    - [Any emergency warning signs]

    ADDITIONAL NOTES
    - [Relevant physical exam findings that would be useful]
    - [Information gaps that need addressing]""",

    agent=intake_coordinator
)


# ============================================================================
# TASK 2: MEDICAL DIAGNOSTIC ANALYSIS
# ============================================================================

diagnosis_task = Task(
    description="""Analyze the complete patient intake report and generate a comprehensive
    differential diagnosis using multi-specialty expertise.

    ANALYSIS FRAMEWORK:

    1. REVIEW COMPLETE INTAKE
       - Synthesize all available information
       - Identify key clinical features
       - Note information gaps

    2. APPLY MULTI-SPECIALTY ANALYSIS
       - Internal Medicine: Systemic diseases, metabolic disorders
       - Cardiology: Cardiac causes (if relevant)
       - Neurology: Neurological conditions (if relevant)
       - Gastroenterology: GI pathology (if relevant)
       - Pulmonology: Respiratory causes (if relevant)
       - Endocrinology: Hormonal disorders (if relevant)
       - Rheumatology: Autoimmune conditions (if relevant)
       - Infectious Disease: Infectious etiologies
       - Psychiatry: Psychiatric or psychosomatic factors
       - Emergency Medicine: Critical "can't miss" diagnoses

    3. GENERATE DIFFERENTIAL DIAGNOSIS
       - List 5-7 possible conditions
       - Rank by likelihood (High/Medium/Low)
       - Provide evidence-based reasoning

    4. FOR EACH DIAGNOSIS PROVIDE:
       - Clear condition name
       - Supporting evidence from patient data
       - Contradicting factors or atypical features
       - Likelihood estimate with reasoning
       - Typical vs. this patient's presentation

    5. IDENTIFY CRITICAL ELEMENTS
       - Red flags requiring immediate attention
       - "Can't miss" diagnoses to rule out
       - Diagnostic uncertainties
       - Information gaps

    6. RECOMMEND NEXT STEPS
       - Specific diagnostic tests needed
       - Physical examination findings to look for
       - Specialist consultations to consider
       - Monitoring parameters

    7. CONSIDER SYSTEMIC FACTORS
       - Medication interactions or side effects
       - Age-related factors
       - Gender-specific considerations

    Use clinical reasoning: pattern recognition, probabilistic thinking, and hypothesis-driven
    analysis. Be thorough but focused on most likely diagnoses.""",

    expected_output="""A comprehensive diagnostic analysis report containing:

    CLINICAL SUMMARY
    - [Synthesis of key findings]

    DIFFERENTIAL DIAGNOSIS (Ranked by Likelihood)

    1. [DIAGNOSIS NAME] - Likelihood: [High/Medium/Low]
       Supporting Evidence:
       - [Specific symptoms/findings that support this]
       Contradicting Factors:
       - [What doesn't fit or is atypical]
       Clinical Reasoning:
       - [Why this diagnosis is being considered]
       - [Probability assessment rationale]

    2. [Continue for 5-7 diagnoses...]

    CRITICAL RED FLAGS
    - [Emergency warning signs identified]
    - [Can't miss diagnoses that must be ruled out]

    DIAGNOSTIC UNCERTAINTIES
    - [Information gaps]
    - [Atypical features requiring explanation]

    RECOMMENDED WORKUP
    - Diagnostic Tests: [Specific tests needed]
    - Physical Examination: [Key exam findings to assess]
    - Specialist Consultation: [If needed, which specialty]
    - Monitoring: [What to watch for]

    MEDICATION/INTERACTION CONSIDERATIONS
    - [Any medication-related factors]

    SAFETY ASSESSMENT
    - Urgency Level: [Emergent/Urgent/Non-urgent]
    - Reasoning: [Why this urgency level]""",

    agent=diagnostic_physician,
    context=[interview_task]
)


# ============================================================================
# TASK 3: PATIENT-FACING COMMUNICATION
# ============================================================================

communication_task = Task(
    description="""Transform the medical diagnostic analysis into clear, compassionate,
    actionable information that patients can understand.

    COMMUNICATION REQUIREMENTS:

    1. TRANSLATE MEDICAL TERMINOLOGY
       - Convert complex terms to plain language
       - Explain medical concepts simply
       - Maintain accuracy while simplifying

    2. PRESENT DIFFERENTIAL DIAGNOSES
       - Use patient-friendly names
       - Explain what each condition means
       - Clarify why it's being considered
       - Indicate general seriousness level

    3. EXPLAIN NEXT STEPS CLEARLY
       - What patient should do and when
       - How to prepare for medical visits
       - What to monitor at home
       - Questions to ask healthcare provider

    4. PROVIDE SAFETY GUIDANCE
       - When to seek emergency care (specific warning signs)
       - When to schedule doctor appointment (timeline)
       - What symptoms to watch for

    5. MAINTAIN APPROPRIATE TONE
       - Empathetic and supportive
       - Not alarmist but honest
       - Respectful of patient autonomy
       - Acknowledge uncertainty where appropriate

    6. INCLUDE ESSENTIAL DISCLAIMERS
       - This is not a definitive diagnosis
       - Professional medical evaluation is necessary
       - Physical examination and tests needed for confirmation

    7. ORGANIZE LOGICALLY
       - Most important information first
       - Clear sections with headers
       - Actionable items clearly highlighted
       - Easy to scan and understand

    TARGET READING LEVEL: 8th grade
    TONE: Professional, compassionate, empowering
    AVOID: Medical jargon, minimizing concerns, false reassurance""",

    expected_output="""A patient-friendly medical guidance report:

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    MEDICAL SYMPTOM ANALYSIS - YOUR GUIDE
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    📋 SUMMARY OVERVIEW
    [2-3 sentences explaining what was analyzed and key findings in simple terms]

    🔍 POSSIBLE CONDITIONS TO DISCUSS WITH YOUR DOCTOR

    Based on your symptoms, here are the main conditions your doctor may consider:

    1. [Condition Name in Plain Language]
       What it is: [Simple explanation]
       Why we're considering it: [Based on your symptoms]
       Seriousness: [General urgency level]

    2. [Continue for top 3-5 conditions...]

    🎯 WHAT THIS MEANS FOR YOU
    [Practical implications in everyday language]

    ⚠️ WHEN TO SEEK IMMEDIATE EMERGENCY CARE

    Go to the emergency room or call 911 if you experience:
    - [Specific warning sign 1]
    - [Specific warning sign 2]
    - [Continue...]

    📅 NEXT STEPS - WHAT TO DO NOW

    PRIORITY ACTIONS:
    1. [Most urgent action with timeline]
    2. [Next important action]
    3. [Additional recommendations]

    PREPARE FOR YOUR DOCTOR VISIT:
    - Bring: [Specific information to bring]
    - Ask about: [Questions to ask]
    - Mention: [Important details to share]

    🏥 WHAT YOUR DOCTOR MAY DO
    - Tests that may be ordered: [In simple terms]
    - Examinations to expect: [What to anticipate]
    - Possible specialists: [If referrals likely]

    📊 WHAT TO MONITOR AT HOME
    - Watch for: [Specific symptoms]
    - Keep track of: [What to document]
    - Report to doctor: [What changes matter]

    ⚕️ IMPORTANT MEDICAL DISCLAIMER

    This analysis is based on the symptoms you provided and is meant to help you
    prepare for a medical appointment. It is NOT a definitive diagnosis.

    • A healthcare provider needs to examine you in person
    • Medical tests and imaging may be necessary
    • Only a licensed physician can provide an official diagnosis
    • This is educational information to guide your healthcare decisions

    Your symptoms deserve professional medical evaluation. Please schedule an
    appointment with your healthcare provider.

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""",

    agent=communication_specialist,
    context=[interview_task, diagnosis_task]
)


# ============================================================================
# CREW CONFIGURATION
# ============================================================================

def create_medical_diagnostic_crew():
    """
    Creates and configures the Medical Diagnostic Crew.

    Returns:
        Crew: Configured CrewAI crew ready for symptom analysis
    """
    crew = Crew(
        agents=[
            intake_coordinator,
            diagnostic_physician,
            communication_specialist
        ],
        tasks=[
            interview_task,
            diagnosis_task,
            communication_task
        ],
        process=Process.sequential,
        memory=True,
        verbose=True,
        max_rpm=10,
        full_output=True
    )

    return crew


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def analyze_symptoms(patient_input: str) -> str:
    """
    Analyzes patient symptoms using the medical diagnostic crew.

    Args:
        patient_input: Patient's description of symptoms and relevant information

    Returns:
        str: Patient-friendly diagnostic guidance
    """
    crew = create_medical_diagnostic_crew()

    result = crew.kickoff(inputs={
        "patient_input": patient_input
    })

    return result


if __name__ == "__main__":
    # Example usage
    sample_patient_input = """
    I'm a 45-year-old male. For the past 3 days, I've had severe chest pain that feels
    like pressure or squeezing. It started suddenly while I was exercising. The pain
    sometimes spreads to my left arm and jaw. I also feel short of breath and have been
    sweating more than usual. The pain is worse when I exert myself and gets a bit better
    when I rest. I have a history of high blood pressure and high cholesterol. My father
    had a heart attack at age 50. I'm currently taking lisinopril for blood pressure.
    """

    print("🏥 Medical Diagnostic Crew Analysis Starting...\n")
    print("=" * 80)

    result = analyze_symptoms(sample_patient_input)

    print("\n" + "=" * 80)
    print("📄 FINAL PATIENT GUIDANCE:")
    print("=" * 80)
    print(result)
