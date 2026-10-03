from typing import List

from pydantic import BaseModel, Field, field_validator


# --------------------------------------------------
# COMMON VALIDATION
# --------------------------------------------------

def validate_text(value: str) -> str:

    value = value.strip()

    if not value:
        raise ValueError(
            "Input cannot be empty."
        )

    return value


# --------------------------------------------------
# TEXT REQUEST
# --------------------------------------------------

class TextRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=1,
        max_length=12000
    )

    @field_validator("text")
    @classmethod
    def clean_text(cls, value: str):

        return validate_text(value)


# --------------------------------------------------
# EXPLANATION REQUEST
# --------------------------------------------------

class ExplainRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=1000
    )

    @field_validator("topic")
    @classmethod
    def clean_topic(cls, value: str):

        return validate_text(value)


# --------------------------------------------------
# QUIZ REQUEST
# --------------------------------------------------

class QuizRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=1,
        max_length=12000
    )

    count: int = Field(
        default=3,
        ge=1,
        le=10
    )

    @field_validator("text")
    @classmethod
    def clean_text(cls, value: str):

        return validate_text(value)


# --------------------------------------------------
# LEARNING PATH REQUEST
# --------------------------------------------------

class LearnRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=1000
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    @field_validator("topic", "level")
    @classmethod
    def clean_fields(cls, value: str):

        return validate_text(value)


# --------------------------------------------------
# TEXT RESPONSE
# --------------------------------------------------

class TextResponse(BaseModel):

    result: str


# --------------------------------------------------
# Q&A RESPONSE
# --------------------------------------------------

class QAResponse(BaseModel):

    answer: str


# --------------------------------------------------
# QUIZ QUESTION
# --------------------------------------------------

class QuizQuestion(BaseModel):

    question: str

    options: List[str] = Field(
        min_length=4,
        max_length=4
    )

    answer: str

    explanation: str = ""


# --------------------------------------------------
# QUIZ RESPONSE
# --------------------------------------------------

class QuizResponse(BaseModel):

    questions: List[QuizQuestion]


# --------------------------------------------------
# HEALTH RESPONSE
# --------------------------------------------------

class HealthResponse(BaseModel):

    status: str

    service: str