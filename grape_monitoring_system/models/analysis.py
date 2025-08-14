from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Analysis:
    id: Optional[int] = None
    user_id: Optional[int] = None
    image_path: Optional[str] = None
    disease_detected: Optional[str] = None
    confidence_score: Optional[float] = None
    analysis_date: Optional[datetime] = None
    gemini_response: Optional[str] = None
    explanation: Optional[str] = None # Brief explanation from Gemini
    symptoms: Optional[str] = None # New/renamed from detailed_description
    possible_causes: Optional[str] = None
    recommended_actions: Optional[str] = None # New/renamed from immediate_actions
    prevention_strategies: Optional[str] = None # New

