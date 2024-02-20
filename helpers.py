import requests
from youtube_search import YoutubeSearch

API_URL = "https://api-inference.huggingface.co/models/Danroy/MamaFrontida"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json={
	"inputs": f"therapy: {payload}",
	})
	return response.json(), response.status_code


def extract_keywords(text):
    # Define a list of stop words
    stop_words = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
                    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
                    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
                    "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
                    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
                    "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                    "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any",
                    "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
                                ])

    # Tokenize and filter out stop words and punctuation
    words = text.split()
    keywords = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]

    return keywords

def searchYT(input,max_results=5):
    results = YoutubeSearch(f'postpartum,depression,{input}', max_results=max_results).to_dict()

    # Keywords that might indicate triggering content
    triggering_keywords = ['sad', 'dies by suicide', 'death by suicide', 'self-harm', 'triggering']

    # Filter out potentially triggering results
    filtered_results = []
    for result in results:
        title = result['title'].lower()
        # Check if any triggering keyword is in the title or description
        if not any(keyword in title  for keyword in triggering_keywords):
            filtered_results.append(result)

    links = []
    for v in filtered_results:
        links.append('https://www.youtube.com' + v['url_suffix'])
    
    return links

if __name__ == '__main__':
    print(searchYT(input='postpartum - i feel sad after giving birth'))