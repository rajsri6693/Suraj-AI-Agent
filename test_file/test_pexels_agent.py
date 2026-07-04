from agents.pexels_agent import PexelsAgent
from models.scene import Scene


scenes = [

    Scene(

        scene=1,

        sentence="आज बाजार में तेजी आई।",

        keyword="Indian Stock Market",

        search_query="Indian stock market trading screen",

        video_type="Stock Market",

        mood="Positive",

        duration=3

    ),

    Scene(

        scene=2,

        sentence="निवेशकों में खुशी है।",

        keyword="Happy Investor",

        search_query="Indian investor smiling with laptop",

        video_type="People",

        mood="Positive",

        duration=3

    )

]

agent = PexelsAgent()

result = agent.generate(

    scenes

)

print()

for scene in result:

    print(scene)