import spacy
from spacytextblob.spacytextblob import SpacyTextBlob


def predict(text):
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    doc = nlp(text)
    polar = doc._.sentiment.polarity

    def sentiment(polarity):
        if doc._.sentiment.polarity > 0:
            return 'Positive'
        if doc._.sentiment.polarity == 0:
            return 'Neutral'
        if doc._.sentiment.polarity < 0:
            return 'Negative'
        

    return(sentiment(polar))



