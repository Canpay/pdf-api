def print_comments(pdf):
    j = 562
    while j > 300:
        comment = pdf.pq('LTTextLineHorizontal:in_bbox("0,'+str(j)+',612,'+str(j+20)+'")')
        text_elements = [t.layout for t in comment]
        t = ''.join([str(x) for x in text_elements])
        if t != "":
            print(t)
        j = j-9


def print_page(pdf):
    # Obtén las coordenadas del primer cuadro
    name = pdf.pq('LTTextBoxHorizontal:in_bbox("0,720,306,792")')
    age_gender = pdf.pq('LTTextBoxHorizontal:in_bbox("0,710,306,730")')
    uhid = pdf.pq('LTTextBoxHorizontal:in_bbox("0,690,306,710")')
    visit_id = pdf.pq('LTTextBoxHorizontal:in_bbox("0,670,306,690")')
    ref_doctor = pdf.pq('LTTextBoxHorizontal:in_bbox("0,650,306,670")')

    text_elements = [t.text for t in name]
    for t in text_elements[1:]:
        print("Patient Name " + t)

    text_elements = [t.text for t in age_gender]
    for t in text_elements[1:]:
        print("Age/Gender " + t)

    text_elements = [t.text for t in uhid]
    for t in text_elements[1:]:
        print("UHID/MR No " + t)

    text_elements = [t.text for t in visit_id]
    for t in text_elements[1:]:
        print("Ref Doctor " + t)

    text_elements = [t.text for t in ref_doctor]
    for t in text_elements[1:]:
        print("IP/OP NO " + t)
    
    # Obtén las coordenadas del segundo cuadro
    name = pdf.pq('LTTextBoxHorizontal:in_bbox("250,720,612,792")')
    age_gender = pdf.pq('LTTextBoxHorizontal:in_bbox("250,710,612,730")')
    uhid = pdf.pq('LTTextBoxHorizontal:in_bbox("250,690,612,710")')
    visit_id = pdf.pq('LTTextBoxHorizontal:in_bbox("250,670,612,690")')
    ref_doctor = pdf.pq('LTTextBoxHorizontal:in_bbox("250,650,612,670")')
    patient_location = pdf.pq('LTTextBoxHorizontal:in_bbox("250,630,612,650")')

    text_elements = [t.text for t in name]
    for t in text_elements[1:]:
        print("Collected " + t)

    text_elements = [t.text for t in age_gender]
    for t in text_elements[1:]:
        print("Received " + t)

    text_elements = [t.text for t in uhid]
    for t in text_elements[1:]:
        print("Reported " + t)

    text_elements = [t.text for t in visit_id]
    for t in text_elements[1:]:
        print("Status " + t)

    text_elements = [t.text for t in ref_doctor]
    for t in text_elements[1:]:
        print("Client Name " + t)

    text_elements = [t.text for t in patient_location]
    for t in text_elements[1:]:
        print("Patient Location " + t)

    test_name = pdf.pq('LTTextBoxHorizontal:in_bbox("0,500,250,630")')
    text_elements = [t.text for t in test_name]
    for t in text_elements:
        print("test_name " + t)

    result = pdf.pq('LTTextBoxHorizontal:in_bbox("150,500,306,630")')
    text_elements = [t.text for t in result]
    for t in text_elements:
        print("result " + t)

    unit = pdf.pq('LTTextBoxHorizontal:in_bbox("306,500,406,630")')
    text_elements = [t.text for t in unit]
    for t in text_elements:
        print("unit " + t)

    bio_ref_range = pdf.pq('LTTextBoxHorizontal:in_bbox("350,500,450,630")')
    text_elements = [t.text for t in bio_ref_range]
    for t in text_elements:
        print("bio_ref_range " + t)

    method = pdf.pq('LTTextBoxHorizontal:in_bbox("406,500,612,630")')
    text_elements = [t.text for t in method]
    for t in text_elements:
        print("method " + t)

    print_comments(pdf)

