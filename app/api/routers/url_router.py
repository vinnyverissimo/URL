from datetime import datetime
import hashlib
from app.db.db import get_table
from app.schemas.util import URLRequest
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, Request
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"message": "UP"}

@router.post("/shorten")
async def shorten_url(url_data: URLRequest, table=Depends(get_table)):

    key = hashlib.md5(str(url_data.long_url).encode()).hexdigest()[:7]

    table.put_item(Item={
        'short_key': key, 
        'long_url': str(url_data.long_url),
        'creation_date': datetime.now().isoformat()
    })
    
    shortened_url = f"http://localhost:8001/{key}"

    return {"shortened_url": shortened_url}

@router.get("/ListAllUrls")
async def list_all_urls(table=Depends(get_table)):
    response = table.scan()
    items = response.get('Items', [])
    return items

@router.get("/{short_key}")
async def redirect(background_tasks: BackgroundTasks, short_key: str, table=Depends(get_table) ):

    #cached = await redis.get(short_key)
    #if cached: 
    #    long_url = cached  
    #else:
        
    item = table.get_item(Key={'short_key': short_key}).get('Item')
    if not item:
        raise HTTPException(status_code=404, detail="URL not found")
    
    #print(f"Redirecting to {item['long_url']}") 
    
    background_tasks.add_task(print, f"redirecting to {item['long_url']}")
    #background_tasks.add_task(kafka_service.send_event, "url_clicks", click_event)  
    
    long_url = item['long_url']

    return RedirectResponse(url=long_url)
