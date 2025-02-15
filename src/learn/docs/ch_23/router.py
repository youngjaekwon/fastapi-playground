# 폼 및 파일 요청
from typing import Annotated

from fastapi import APIRouter, File, UploadFile, Form

router = APIRouter(prefix="/ch-23", tags=["ch.23"])


@router.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
