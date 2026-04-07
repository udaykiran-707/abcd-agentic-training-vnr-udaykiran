import logging
import sys
from agents.research import ResearchAgent
from agents.filter import FilterAgent
from agents.writer import WriterAgent
from utils.memory import Memory
from utils.pdf_generator import PDFGenerator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class ResearchOrchestrator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.filter_agent = FilterAgent()
        self.writer_agent = WriterAgent()
        self.memory = Memory()
        self.pdf_gen = PDFGenerator()

    def run_research_pipeline(self, topic: str):
        if not topic or len(topic.strip()) == 0:
            raise ValueError("Topic cannot be empty.")

        print(f"\n=== Starting Research Pipeline for: {topic} ===\n")

        try:
            raw_data = self.research_agent.run(topic)
        except Exception as e:
            logging.error(f"Research failed: {e}")
            return None, None

        try:
            clean_data = self.filter_agent.run(raw_data)
        except Exception as e:
            logging.error(f"Filtering failed: {e}")
            return None, None

        # 🔥 NO SUMMARIZER (FIXED)
        summary = clean_data

        try:
            report = self.writer_agent.run(topic, clean_data, summary)
        except Exception as e:
            logging.error(f"Writing failed: {e}")
            return None, None

        self.memory.save_search(topic, report)
        pdf_path = self.pdf_gen.generate(report)

        print("\n=== Pipeline Completed Successfully ===\n")
        return report, pdf_path


if __name__ == "__main__":
    orchestrator = ResearchOrchestrator()
    topic = input("Enter topic: ")
    report, pdf = orchestrator.run_research_pipeline(topic)

    if report:
        print("Summary:", report['key_insights'])
        print("PDF saved at:", pdf)