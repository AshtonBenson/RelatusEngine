import RelatusEngine.nlp as nlp

class NPC:
    def __init__(self, name, personality, attributes, mood="neutral"):
        self.name = name
        self.personality = personality
        self.mood = mood
        self.attributes = attributes
        
    def get_suggested_action(self):
        if self.mood == "friendly":
            return f"{self.name} is in a friendly mood. You can ask for help or favors."
        elif self.mood == "aggressive":
            return f"{self.name} is feeling aggressive. Proceed with caution or prepare for a confrontation."
        elif self.mood == "neutral":
            return f"{self.name} is neutral. You may be able to influence them with further dialogue."
        else:
            return f"{self.name}'s mood is unclear. More interaction is needed."

    def interpret_sentiment(self, sentiment):
        kindness = self.personality.get('kindness', 0)
        aggression = self.personality.get('aggression', 0)
        trust = self.personality.get('trust', 0)
        cynicism = self.personality.get('cynicism', 0)
        empathy = self.personality.get('empathy', 0)
        loyalty = self.personality.get('loyalty', 0)
        patience = self.personality.get('patience', 0)

        mood_modifier = 0

        if sentiment > 0:
            mood_modifier += sentiment * (kindness + trust * 0.5 + empathy * 0.3)
            if cynicism > 0.7:
                mood_modifier -= sentiment * cynicism * 0.4

            if mood_modifier > 0.3:
                self.mood = "friendly"
            else:
                self.mood = "neutral"

        elif sentiment < 0:
            mood_modifier += sentiment * (aggression * 0.9 - cynicism * 0.4) 
            mood_modifier += empathy * 0.1 
            mood_modifier += patience * 0.05 

            if mood_modifier < -0.3:
                self.mood = "angry" 
            elif mood_modifier > 0:
                self.mood = "neutral"
            else:
                self.mood = "neutral"

        else: 
            mood_modifier += trust * 0.4 + loyalty * 0.3 - cynicism * 0.3
            if mood_modifier > 0.3:
                self.mood = "friendly"
            else:
                self.mood = "neutral"

        return {
            'mood': self.mood,
            'mood_modifier': mood_modifier
        }

    def sayTo(self, dialogue, sentiment_modifier=0):
        ogSentiment = nlp.analyze_sentiment(dialogue)
        response = self.interpret_sentiment(ogSentiment)
        boostedSentiment = ogSentiment + response['mood_modifier'] + sentiment_modifier
        boostedSentiment = max(-1, min(1, boostedSentiment))

        if boostedSentiment > 0:
            self.personality['trust'] = min(self.personality.get('trust', 0) + 0.1, 1.0)
            self.personality['loyalty'] = min(self.personality.get('loyalty', 0) + 0.1, 1.0)
            self.personality['kindness'] = min(self.personality.get('kindness', 0) + 0.05, 1.0)
        elif boostedSentiment <= 0:
            self.personality['trust'] = max(self.personality.get('trust', 0) - 0.1, 0)
            self.personality['loyalty'] = max(self.personality.get('loyalty', 0) - 0.1, 0)
            self.personality['aggression'] = min(self.personality.get('aggression', 0) + 0.1, 1.0)
            self.personality['cynicism'] = min(self.personality.get('cynicism', 0) + 0.1, 1.0)

        return {
            'mood': self.mood,
            'personality': self.personality,
            'suggested_action': self.get_suggested_action(),
            'mood_modifier': response['mood_modifier']
        }
