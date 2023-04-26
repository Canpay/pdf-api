from fastapi import FastAPI, File, UploadFile
import fitz
from pydantic import BaseModel
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class PageInfo(BaseModel):
    patient_name: str
    age_gender: str
    uhidmr_no: str
    visit_id: str
    ref_doctor: str
    ipop_no: str
    collected: str
    received: str
    reported: str
    status: str
    client_name: str
    patient_location: str
    test_name: str
    result: str
    unit: str
    bio_ref_range: str
    method: str
    comment: str

@app.post("/upload_pdf")
async def upload_pdf(uploaded_file: UploadFile = File(...)):
    if os.path.exists("temp_file.pdf"):
        os.remove("temp_file.pdf")
    file_location = f"temp_file.pdf"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    doc = fitz.open("temp_file.pdf")
    list_page_info = []
    for page_number in range(doc.page_count):
        page = doc[page_number]

        patient_name = page.get_text("text", clip = fitz.Rect(115,0,300,120)).replace("\n","")
        print("patient_name: " + patient_name)
        age_gender = page.get_text("text", clip = fitz.Rect(115,120,300,130)).replace("\n","")
        print("age_gender: " + age_gender)
        uhid = page.get_text("text", clip = fitz.Rect(115,130,300,140)).replace("\n","")
        print("uhid: " + uhid)
        visit_id = page.get_text("text", clip = fitz.Rect(115,145,300,150)).replace("\n","")
        print("visit_id: " + visit_id)
        ref_doctor = page.get_text("text", clip = fitz.Rect(115,160,300,170)).replace("\n","")
        print("ref_doctor: " + ref_doctor)
        ipop_no = page.get_text("text", clip = fitz.Rect(115,170,300,180)).replace("\n","")
        print("ipop_no: " + ipop_no)
        
        collected = page.get_text("text", clip = fitz.Rect(390,0,612,120)).replace("\n","")
        print("collected: " + collected)
        received = page.get_text("text", clip = fitz.Rect(390,120,612,130)).replace("\n","")
        print("received: " + received)
        reported = page.get_text("text", clip = fitz.Rect(390,130,612,140)).replace("\n","")
        print("reported: " + reported)
        status = page.get_text("text", clip = fitz.Rect(390,145,612,150)).replace("\n","")
        print("status: " + status)
        client_name = page.get_text("text", clip = fitz.Rect(390,160,612,170)).replace("\n","")
        print("client_name: " + client_name)
        patient_location = page.get_text("text", clip = fitz.Rect(390,170,612,180)).replace("\n","")
        print("patient_location: " + patient_location)

        test_name = page.get_text("text", clip = fitz.Rect(0,220,220,240)).replace("\n","")
        print("test_name: " + test_name)
        result = page.get_text("text", clip = fitz.Rect(220,220,306,240)).replace("\n","")
        print("result: " + result)
        unit = page.get_text("text", clip = fitz.Rect(306,220,360,240)).replace("\n","")
        print("unit: " + unit)
        bio_ref_range = page.get_text("text", clip = fitz.Rect(360,220,450,240)).replace("\n","")
        print("bio_ref_range: " + bio_ref_range)
        method = page.get_text("text", clip = fitz.Rect(450,220,612,240)).replace("\n","")
        print("method: " + method)
        comment = page.get_text("text", clip = fitz.Rect(0,280,612,690)).replace("*** End Of Report ***","")
        print("comment: " + comment)
        page_info = PageInfo(patient_name=patient_name,age_gender=age_gender,uhidmr_no=uhid,visit_id=visit_id,ref_doctor=ref_doctor,ipop_no=ipop_no,
            collected=collected,received=received,reported=reported,status=status,client_name=client_name,patient_location=patient_location,
            test_name=test_name,result=result,unit=unit,bio_ref_range=bio_ref_range,method=method,comment=comment.replace("\n",""))
        list_page_info.append(page_info)

    return {"data": list_page_info}