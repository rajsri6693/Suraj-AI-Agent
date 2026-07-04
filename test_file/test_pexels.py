from config import Config
from services.pexels_service import PexelsService


service = PexelsService(

    Config.PEXELS_API_KEY

)

result = service.search(

    "Indian stock market"

)

print(result.keys())