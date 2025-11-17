#!/usr/bin/env python3
"""
Demo script to show persona evolution in action
"""

from mythos_engine import MythosEngine

engine = MythosEngine()

print("🎭 SIMULATION: Persona evolution over time\n")

# Simulate ORION being used heavily for paper critiques
contexts = [
    "Critiquing theodicy paper structure",
    "Reviewing Husserl-Heidegger analysis",
    "Analyzing epistemology argument flow",
    "Checking logical coherence in intro",
    "Reviewing conclusion strength",
    "Examining counter-argument handling",
    "Assessing citation integration",
    "Evaluating philosophical rigor",
    "Checking premises in theodicy critique",
    "Reviewing empathy framework logic",
    "Analyzing recursive structure",
    "Checking phenomenology accuracy",
    "Reviewing systematic theology critique",
    "Examining applied empathy argument",
    "Final coherence check before submission"
]

for i, context in enumerate(contexts, 1):
    print(f"[{i}/15] Invoking ORION: {context}")
    engine.log_invocation("ORION", context, tags=["academic", "philosophy"], emotional_weight=7)

print("\n" + "="*60)
print("SIMULATION COMPLETE")
print("="*60)

# Generate report
report = engine.generate_mythological_report("ORION")
print(report)

# Show evolution trajectory
persona = engine.personas["ORION"]
print("\n🌟 EVOLUTION TRAJECTORY:")
print(f"   Invocations: {persona.invocation_count}")
print(f"   Stage: {persona.evolution_stage}")
print(f"   Developed Traits: {len(persona.developed_traits)}")
print(f"   Learned Phrases: {len(persona.learned_phrases)}")

if persona.learned_phrases:
    print("\n   Latest Learned Phrases:")
    for phrase in persona.learned_phrases[-3:]:
        print(f"      • {phrase}")
