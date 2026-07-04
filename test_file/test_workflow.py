from workflow.workflow_manager import WorkflowManager
from models.content import Content


content = Content(

    topic="Nifty 50 Today",

    content_type="Shorts",

    script="""
नमस्कार दोस्तों।

आज भारतीय शेयर बाजार में शानदार तेजी देखने को मिली।

निफ्टी 50 ने 24,000 का स्तर पार किया।

ऐसी ही जानकारी के लिए चैनल को सब्सक्राइब करें।
""",

    title="Test",

    description="",

    tags="",

    thumbnail_prompt="",

    status="Approved",

    page_id=""

)

workflow = WorkflowManager()

result = workflow.run(content)

print("\n===================================")
print("Workflow Completed")
print("===================================\n")

print(result)