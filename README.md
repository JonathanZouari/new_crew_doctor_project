# Professional CrewAI Medical Diagnostic Team

A comprehensive 3-agent CrewAI system for medical symptom analysis and diagnostic guidance.

## System Architecture

- **Platform**: CrewAI with sequential process
- **Memory**: Short-term and long-term enabled
- **Agent Count**: 3 optimized agents
- **Process Flow**: Sequential task execution

## Agent Overview

### 1. Medical Intake Coordinator
**Role**: Chief Triage Officer and Patient Interview Specialist

**Responsibilities**:
- Conducts comprehensive patient interviews using OPQRST framework
- Gathers demographics, symptoms, medical history, and vital signs
- Identifies red flags requiring emergency attention
- Creates structured intake reports for diagnostic analysis

### 2. Senior Diagnostic Physician
**Role**: Multi-Specialty Medical Diagnostician and Clinical Reasoning Expert

**Responsibilities**:
- Analyzes patient data from multiple specialty perspectives
- Generates evidence-based differential diagnoses (5-7 conditions)
- Applies advanced diagnostic reasoning and Bayesian analysis
- Identifies critical red flags and recommends diagnostic workup

### 3. Patient Communication Specialist
**Role**: Medical Translator and Patient Education Expert

**Responsibilities**:
- Translates complex medical analysis into patient-friendly language
- Provides clear, actionable next steps
- Explains warning signs and when to seek care
- Maintains 8th-grade reading level for accessibility

## Installation

### Prerequisites
- Python 3.10 or higher
- OpenAI API key (or compatible LLM API)

### Setup Steps

1. **Clone or download this project**
   ```bash
   cd new_crew_doctor_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL_NAME=gpt-4o
   ```

## Usage

### Basic Usage

Run the example built into the script:

```bash
python crew.py
```

This will analyze a sample patient case and display the diagnostic guidance.

### Custom Analysis

Create your own script or modify the example in `crew.py`:

```python
from crew import analyze_symptoms

patient_input = """
I'm a 28-year-old female. I've had a severe headache for 2 days
that's getting worse. It's on the right side of my head and feels
like throbbing pain. I also feel nauseous and light bothers my eyes.
I've never had headaches like this before.
"""

result = analyze_symptoms(patient_input)
print(result)
```

### Interactive Mode

You can create an interactive version:

```python
from crew import analyze_symptoms

def interactive_medical_assistant():
    print("🏥 Medical Diagnostic Assistant")
    print("=" * 60)
    print("Please describe your symptoms in detail.")
    print("Include: age, gender, symptoms, duration, severity, medical history")
    print("=" * 60)

    patient_input = input("\nYour symptoms: ")

    if patient_input.strip():
        print("\n🔄 Analyzing symptoms...\n")
        result = analyze_symptoms(patient_input)
        print("\n📄 DIAGNOSTIC GUIDANCE:")
        print("=" * 60)
        print(result)
    else:
        print("No input provided.")

if __name__ == "__main__":
    interactive_medical_assistant()
```

## Expected Output Format

The system provides a comprehensive patient-friendly report including:

1. **Summary Overview** - Brief synthesis of findings
2. **Possible Conditions** - Top 3-5 diagnoses explained in plain language
3. **When to Seek Emergency Care** - Specific red flag symptoms
4. **Next Steps** - Prioritized action items
5. **Doctor Visit Preparation** - What to bring and ask
6. **Home Monitoring** - What symptoms to track
7. **Medical Disclaimer** - Clear limitations of the analysis

## Key Features

- **Comprehensive**: Full diagnostic workflow from intake to patient communication
- **Multi-specialty**: Integrates perspectives from cardiology, neurology, GI, and more
- **Patient-centered**: Clear, accessible language at 8th-grade reading level
- **Safe**: Built-in red flag identification and emergency guidance
- **Actionable**: Specific next steps and recommendations
- **Efficient**: Streamlined 3-agent architecture without redundancy

## Task Flow

1. **Patient Interview** (Medical Intake Coordinator)
   - Systematic symptom gathering
   - Medical history collection
   - Red flag identification

2. **Diagnostic Analysis** (Senior Diagnostic Physician)
   - Multi-specialty evaluation
   - Differential diagnosis generation
   - Evidence-based reasoning
   - Diagnostic recommendations

3. **Patient Communication** (Patient Communication Specialist)
   - Plain language translation
   - Actionable guidance
   - Safety instructions
   - Appropriate disclaimers

## Important Disclaimers

- **NOT A SUBSTITUTE FOR MEDICAL CARE**: This system provides educational information only
- **REQUIRES PROFESSIONAL EVALUATION**: All symptoms require assessment by licensed healthcare providers
- **NO DEFINITIVE DIAGNOSIS**: Only in-person examination and testing can provide diagnosis
- **EMERGENCY SITUATIONS**: Call 911 or go to ER for severe symptoms
- **EDUCATIONAL PURPOSE**: Designed to help users prepare for medical appointments

## Configuration Options

### Adjusting Agent Behavior

You can modify agent characteristics in [crew.py](crew.py):

- **Verbosity**: Set `verbose=True/False` for detailed logging
- **Memory**: Enable/disable with `memory=True/False`
- **Delegation**: Control with `allow_delegation=True/False`

### Changing LLM Model

In your `.env` file:
```env
OPENAI_MODEL_NAME=gpt-4o          # More capable, higher cost
OPENAI_MODEL_NAME=gpt-4o-mini     # Faster, lower cost
```

### Crew Configuration

In the `create_medical_diagnostic_crew()` function:

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,  # Or Process.hierarchical
    memory=True,
    verbose=True,
    max_rpm=10  # Rate limit: max requests per minute
)
```

## Troubleshooting

### Import Errors
```bash
# Ensure crewai is installed
pip install --upgrade crewai crewai-tools
```

### API Key Issues
```bash
# Verify .env file exists and contains valid key
cat .env

# Or check environment variable
echo $OPENAI_API_KEY  # Linux/Mac
echo %OPENAI_API_KEY%  # Windows
```

### Rate Limiting
If you encounter rate limits, adjust `max_rpm` in crew configuration or upgrade your OpenAI plan.

## Project Structure

```
new_crew_doctor_project/
├── crew.py              # Main application with agents, tasks, and crew
├── requirements.txt     # Python dependencies
├── README.md           # Documentation
├── .env                # Environment variables (create this)
└── example_usage.py    # Interactive usage example (optional)
```

## Advanced Usage

### Custom Tools

Add custom tools to enhance agent capabilities:

```python
from crewai.tools import tool

@tool("Symptom Database Lookup")
def lookup_symptom_database(symptom: str) -> str:
    """Looks up symptom in medical database"""
    # Implementation here
    return f"Database info for: {symptom}"

# Add to agent
diagnostic_physician = Agent(
    ...,
    tools=[generate_differential_diagnosis, safety_check, lookup_symptom_database]
)
```

### Adding More Agents

You can extend the crew with specialists:

```python
specialist_agent = Agent(
    role="Specialist Consultant",
    goal="Provide expert opinion on specific conditions",
    backstory="...",
    tools=[...]
)

# Add to crew
crew = Crew(
    agents=[intake_coordinator, diagnostic_physician, specialist_agent, communication_specialist],
    tasks=[...],
    ...
)
```

## Performance Tips

1. **Use appropriate models**: gpt-4o-mini for faster, cheaper processing
2. **Adjust verbosity**: Set `verbose=False` in production
3. **Monitor rate limits**: Adjust `max_rpm` based on your API tier
4. **Cache results**: Implement caching for similar queries
5. **Batch processing**: Process multiple patients in sequence

## Contributing

Suggestions for improvement:
- Additional specialty perspectives
- Enhanced medical reasoning frameworks
- Integration with medical databases
- Support for multiple languages
- Enhanced patient education materials

## License

This is an educational demonstration project. Consult legal and medical professionals before deploying in any clinical context.

## Support

For CrewAI framework issues: https://github.com/joaomdmoura/crewAI
For this project: Create an issue in your repository

## Version History

- **v1.0.0** - Initial release with 3-agent configuration
  - Medical Intake Coordinator
  - Senior Diagnostic Physician
  - Patient Communication Specialist

---

**Remember**: This is an educational tool. Always seek professional medical care for health concerns.
