# SUBMISSION - Exit Exam MVC 1/2569 (เสาร์บ่าย)

## 1. วิธีเปิดโปรแกรม
- ภาษา/เฟรมเวิร์ก: Python / Flask
- Entry point / คำสั่งเปิดโปรแกรม: 
  python app.py
- หมายเหตุที่จำเป็น (ถ้ามี): เปิดเบราว์เซอร์เข้าใช้งานจาก termianl

## 2. ตารางเชื่อมโยง Requirements
| Requirement | Model / Domain | Controller / Action | View / Screen |
|---|---|---|---|
| R1 | Member, ChangeRequest, Decision | RequestController | templates/index.html |
| R2 | Member, ChangeRequest | RequestController.create_request() | templates/index.html |
| R3 | Member, ChangeRequest, Decision | RequestController.vote_request() | templates/index.html |
| R4 | Member, ChangeRequest, Decision | RequestController.vote_request() | templates/index.html |
| R5 | ChangeRequest, Decision | RequestController.cancel_request() | templates/index.html |

## 3. ผลการทดสอบ
| กรณี | ผ่าน/ไม่ผ่าน | หมายเหตุ (เฉพาะที่จำเป็น) |
|---|---|---|
| T1 | ผ่าน | |
| T2 | ผ่าน | pass with con สร้างจากคนที่ไม่ได้อยู่ในรายชื่อได้ เช่น M1 แทน M01 ไม่ได้ดักในจุดนี้ |
| T3 | ผ่าน | |
| T4 | ผ่าน | |
| T5 | ผ่าน | |
| T6 | ผ่าน | |

## 4. ความแตกต่างระหว่างแบบที่ออกกับโปรแกรมจริง (ถ้ามี)
ระบุไม่เกิน 3 ข้อ
1. 
2. 
3. 

## 5. บันทึกการใช้ Generative AI
13.30, gemini, ขอสรุป req เป็นข้อๆสั้น, เอาไปเขียนคลาส
14.00, gemini, ส่งที่จะทำ+feedbackจากสอบรอบนหน้าให้ดู, แก้คลาสตามแนะนำ
15.00, gemini, แก้ terminal ไม่โชว์ภาษาไทย, พยามยามทำตาม แต่ไม่สำเร็จ 
15.00, clade, ขอวิธีเปลี่ยนเป็น web ส่งไฟล์ให้อิงจากสอบรอบก่อน, เอาที่เปลี่ยนมาแก้
16.20, clade, ส่งโค้ดกับreqให้ช่วยเช็คว่าตรงรึยัง, แก้ตามจุดที่บอก