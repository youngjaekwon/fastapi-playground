from typing import Annotated

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/ch-22", tags=["ch.22"])

"""
UploadFile의 이점
- "스풀 파일"을 사용
    - 최대 크기 제한까지만 메모리에 저장되며, 이를 초과하는 경우 디스크에 저장됩니다.
- 이미지, 동영상, 큰 이진코드와 같은 대용량 파일들을 많은 메모리를 소모하지 않고 처리하기에 적합합니다.
- 업로드 된 파일의 메타데이터를 얻을 수 있습니다.
- file-like async 인터페이스를 갖고 있습니다.
- file-like object를 필요로 하는 다른 라이브러리에 직접적으로 전달할 수 있는 파이썬 SpooledTemporaryFile 객체를 반환합니다.
"""
"""
UploadFile의 어트리뷰트
- filename: 업로드 된 파일명 (예: myimage.jpg)
- content_type: 파일 형식(MIME type / media type) (예: image/jpeg)
- file: SpooledTemporaryFile (파일류 객체)
"""


@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@router.post("/uploadfile/read/")
async def read_upload_file(file: UploadFile):
    contents = await file.read()
    return {
        "filename": file.filename,
        "file_size_with_property": file.size,
        "file_size_with_contents": len(contents),
    }


@router.post("/multiple-files/")
async def create_multiple_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/multiple-uploadfiles")
async def create_multiple_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@router.get("/")
async def main():
    content = """
<body>
    <form action="/ch-22/multiple-files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
    <form action="/ch-22/multiple-uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)
