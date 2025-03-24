from dotenv import load_dotenv
from hatchet_sdk import Hatchet

load_dotenv()

hatchet = Hatchet(debug=True)


@hatchet.workflow(name="first-python-workflow", on_events=["user:create"])
class MyWorkflow:
    @hatchet.step()
    def step1(self, context):
        return {"result": "success"}


if __name__ == "__main__":
    worker = hatchet.worker("first-worker")
    worker.register_workflow(MyWorkflow())

    worker.start()
