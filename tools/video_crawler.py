from zeeguu.core.content_retriever.video_dowloader import crawl
from zeeguu.logging import log

from zeeguu.api.app import create_app
from datetime import datetime


app = create_app()
app.app_context().push()

start = datetime.now()
crawl(3)
end = datetime.now()
log(f"done at: {end}")
log(f"total duration: {end - start}")
