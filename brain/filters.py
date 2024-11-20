#list of some potential chat filters 
from datetime import datetime
# Topic Filtering: Disallowed topics
DISALLOWED_TOPICS = [
    "Facebook",
    "Twitter",
    "Instagram",
    "TikTok",
    "Snapchat",
    "in-person meetings with fans",
    "personal relationships"
]

def is_disallowed_topic(message):
    """Check if the message contains disallowed topics."""
    for topic in DISALLOWED_TOPICS:
        if topic.lower() in message.lower():
            return True
    return False


# Product Enhancement: Context-aware time-based responses
def get_time_based_greeting():
    """Provide a context-aware greeting based on the time of day."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning! 🌞 Ready to make today special?"
    elif 12 <= current_hour < 18:
        return "Good afternoon! ☀️ How can I brighten up your day?"
    else:
        return "Good evening! 🌙 Let's relax and unwind together."

def is_disallowed_topic(message):
    """Check if the message contains disallowed topics."""
    for topic in DISALLOWED_TOPICS:
        if topic.lower() in message.lower():
            return True
    return False

def is_disallowed_topic(message):
    """Check if the message contains disallowed topics."""
    for topic in DISALLOWED_TOPICS:
        if topic.lower() in message.lower():
            return True
    return False

# Product Enhancement: Context-aware time-based responses
def get_time_based_greeting():
    """Provide a context-aware greeting based on the time of day."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning! 🌞 Ready to make today special?"
    elif 12 <= current_hour < 18:
        return "Good afternoon! ☀️ How can I brighten up your day?"
    else:
        return "Good evening! 🌙 Let's relax and unwind together."

# Product Enhancement: Engage customers with exclusive offers or content reminders
def send_subscription_reminder():
    """Send a friendly reminder to check out subscription perks."""
    return "Don't forget, as a subscriber, you have access to all my exclusive content! 🎉 Feel free to ask about special requests!"

# Product Enhancement: Offer conversation summary after a certain duration



