#  Code Example with All 5 Anthropic Patterns

import threading
from colorama import init, Fore, Style

init(autoreset=True) # Auto resets color after each print


# 🧠 Base Agent class
class Agent:
    def __init__(self, name):
        self.name = name
        # self.lock = threading.Lock()

    def run(self, data):
        raise NotImplementedError
    

# 🎯 1. Orchestrator-Workers Pattern
class Orchestrator(Agent):
    def run(self, task):
        print(Style.BRIGHT + Fore.BLUE + f"\n 🧑‍🏫 {self.name}: Received task '{task}' ")

        # Step 1: Routing - Send task to the right worker
        if "article" in task:
            return self.handoff(WriterAgent("WriterAgent"), task)
        else:
            return self.handoff(GeneralAgent("GeneralAgent"), task)
        
    def handoff(self, agent, task):
        return agent.run(task)
    

# ✍️ 2. Writer Agent (Worker for Orchestrator)
class WriterAgent(Agent):
    def run(self, task):
        print(Style.BRIGHT + Fore.GREEN + f"📜 {self.name}: Writing article on '{task}'...")
        content = f"AI in education is transforming the way students learn..."

           
        # 3. Prompt Chaining - Pass to summarizer
        return self.handoff(SummarizerAgent("SummarizerAgent"), content)
    
    def handoff(self, agent, content):
        return agent.run(content)
    

    
# 🧾 3. Summarizer Agent (Prompt Chaining)
class SummarizerAgent(Agent):
    def run(self, content): 
        print(Style.BRIGHT + Fore.YELLOW + f"📃 {self.name}: Summarizing content...")
        # print(f"📃 {self.name}: Summarizing content...")
        summary = "AI makes education more personalized and efficient."

        # 4. Evaluator-Optimizer
        return self.handoff(EvaluatorAgent("EvaluatorAgent"), summary)
    
    def handoff(self, agent, summary):
        return agent.run(summary)
    
# 4. Evaluator-Optimizer pattern
class EvaluatorAgent(Agent):
    def run(self, summary):
        print(Style.BRIGHT + Fore.MAGENTA + f"🔍 {self.name}: Evaluating summary...")
        # print(f"🔍 {self.name}: Evaluating summary...")
        if "efficient" in summary:
            feedback = "Looks good. No changes needed."
        else:
            feedback = "Add more detail."

        return self.handoff(OptimizerAgent("OptimizerAgent"), (summary, feedback))
    
    def handoff(self, agent, data):
        return agent.run(data)
    
class OptimizerAgent(Agent):
    def run(self, data):
        summary, feedback = data
        print(Style.BRIGHT + Fore.RED + f"🔧 {self.name}: Feedback received - {feedback}")
        # print(f"🔧 {self.name}: Feedback received - {feedback}")
        improved = summary + " This helps both students and teachers."
        print(f"✅ Final Optimized Summary: {improved}")
        return improved

# 5. Parallelization - Additional processing
class GeneralAgent(Agent):
    def run(self, task):
        print(Style.BRIGHT + Fore.CYAN + f"🛠️ {self.name}: Performing general task: {task}")
        # print(f"🛠️ {self.name}: Performing general task: {task}")
        return f"General task done: {task}"
    
    # 🧪 Parallel Example (Not needed for final output, just shown)

    def parallel_tasks():
        def summarize():
            # print("🔁 Running summarizer in parallel...")
            print(Style.BRIGHT + Fore.YELLOW + "🔁 Running summarizer in parallel...")


        def translate():
            # print("🌐 Running translator in parallel...")
            print(Style.BRIGHT + Fore.GREEN + "🌐 Running translator in parallel...")

        # Run both tasks at the same time
        t1 = threading.Thread(target=summarize)
        t2 = threading.Thread(target=translate)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        
# 🚀 Main Program
if __name__ == "__main__":
    print(Style.BRIGHT + Fore.BLUE + "🧠 Starting Anthropic Pattern Simulation...\n")

    orchestrator = Orchestrator("MainOrchestrator")
    final_output = orchestrator.run("Write an article about AI in education")

    print(Style.BRIGHT + Fore.BLUE + "\n---\nNow demonstrating Parallelization:\n")
    GeneralAgent.parallel_tasks()