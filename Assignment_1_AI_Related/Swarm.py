"""
We have 3 agents:

AgentA: Writes a topic

AgentB: Expands it into a paragraph

AgentC: Summarizes the paragraph

Each agent performs a task, then hands off to the next.
"""

#  Swarm-Style Agent Code (Concept)
# Base Agent class
class Agent:
    def __init__(self, name):
        self.name = name 

    def run(self, input_data):
        raise NotImplementedError
    
    def handoff(self, next_agent, output_data):
        print(f"{self.name} ➡️ Hnadoff to  {next_agent.name}")
        return next_agent.run(output_data)        
    


    # Agent A: Writes a topic
class TopicAgent(Agent):
    def run(self, input_data=None):
        topic = "The Benefits of using AI in Eductaion"
        print(f"{self.name} created topic: {topic}")
        return self.handoff(WriterAgent("WriterAgent"), topic)
    

# Agent B: Expands topic into paragraph
class WriterAgent(Agent):
    def run(self, topic):
        paragraph = f"{topic}. AI helps students learn faster  by providing personalized content and instant feedback."
        print(f"{self.name} wrote paragraph:\n {paragraph}")
        return self.handoff(SummarizerAgent("SummarizerAgent"), paragraph)
    
# Agent C: Summarizes the paragraph
class SummarizerAgent(Agent):
    def run (self, paragraph):
        summary = "AI Improves education through personalization and speed."
        print(f"{self.name} summarized:\n{summary}")
        return summary
    

#start the swarm process
if __name__=="__main__":
    swarm = TopicAgent("TopicAgent")
    final_output = swarm.run()
    print("\n✅ Final Output:", final_output)