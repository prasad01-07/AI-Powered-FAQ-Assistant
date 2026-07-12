from sentence_transformers import SentenceTransformer, util

# Load AI Model
model = SentenceTransformer("all-MiniLM-L6-v2")


class SemanticEngine:

    def __init__(self, faq_data):

        self.faq_data = faq_data

        self.questions = [
            item["question"]
            for item in faq_data
        ]

        self.answers = [
            item["answer"]
            for item in faq_data
        ]

        self.embeddings = model.encode(
            self.questions,
            convert_to_tensor=True
        )

    def search(self, query):

        query_embedding = model.encode(
            query,
            convert_to_tensor=True
        )

        similarity = util.cos_sim(
            query_embedding,
            self.embeddings
        )

        best_index = similarity.argmax().item()

        confidence = similarity[0][best_index].item()

        return {
            "question": self.questions[best_index],
            "answer": self.answers[best_index],
            "confidence": confidence
        }