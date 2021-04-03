import spacy
from spacytextblob.spacytextblob import SpacyTextBlob


def predict(text):
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    doc = nlp(text)
    polar = doc._.sentiment.polarity

    def sentiment(polarity):  # Setting a threshold on polarity.
        if doc._.sentiment.polarity > 0:
            return 'Positive'
        elif doc._.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'
        

    return(sentiment(polar))