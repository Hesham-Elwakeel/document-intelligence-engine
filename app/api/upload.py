from fastapi import APIRouter, HTTPException
from fastapi import UploadFile
from fastapi import File

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    allowed_types = ["application/pdf", "image/jpeg", "image/png"]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=415,
            detail="Unsupported file type. only PDF, JPEG, JPG, and PNG files are allowed."
        )

    # هنا ممكن تعمل أي حاجة بالملف اللي اتبعت، زي تخزينه أو معالجته
    return {"filename": file.filename, 
            "content_type": file.content_type,
            
            } 
            