"""
Database Schemas for the Fashion Brand site

Each Pydantic model represents a MongoDB collection.
Collection name is the lowercase class name.

- NewsletterSubscriber -> "newslettersubscriber"
- ContactMessage -> "contactmessage"
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class NewsletterSubscriber(BaseModel):
    """Newsletter subscribers collection"""
    name: str = Field(..., min_length=2, max_length=80, description="Subscriber name")
    email: EmailStr = Field(..., description="Subscriber email")
    source: Optional[str] = Field(default="website", description="Acquisition source")


class ContactMessage(BaseModel):
    """Contact form submissions collection"""
    name: str = Field(..., min_length=2, max_length=80, description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    subject: str = Field(..., min_length=2, max_length=120, description="Subject")
    message: str = Field(..., min_length=5, max_length=2000, description="Message body")
    consent: bool = Field(..., description="User consent to be contacted")
    source: Optional[str] = Field(default="website", description="Submission source")
