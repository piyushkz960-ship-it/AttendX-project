import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard, user_badge
from src.components.footer import footer_dashboard
from src.components.stat_card import stat_row
from src.components.empty_state import empty_state
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    with st.container(border=True, key="ax_card_topbar"):
        c1, c2, c3 = st.columns([2.2, 2, 1], vertical_alignment='center')
        with c1:
            header_dashboard()
        with c2:
            user_badge(student_data['name'], 'Student')
        with c3:
            if st.button(
                "Logout",
                type='secondary',
                key='loginbackbtn',
                width='stretch',
                shortcut="control+backspace"
            ):
                st.session_state['is_logged_in'] = False
                del st.session_state.student_data
                st.rerun()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    total_classes_logged = sum(s['total'] for s in stats_map.values())
    total_attended = sum(s['attended'] for s in stats_map.values())
    overall_pct = round(100 * total_attended / total_classes_logged) if total_classes_logged else 0

    stat_row([
        ("📚", "Enrolled Subjects", len(subjects)),
        ("✅", "Classes Attended", total_attended),
        ("📊", "Attendance Rate", f"{overall_pct}%"),
    ])

    c1, c2 =st.columns(2)
    with c1:
        st.markdown(
            "<h2>Your Enrolled Subjects</h2>",
            unsafe_allow_html=True
        )
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()


    st.divider()

    if not subjects:
        empty_state(
            "📚", "No enrolled subjects yet",
            "Click ‘Enroll in Subject’ above using a code from your teacher to get started.",
            key="student_no_subjects"
        )
        footer_dashboard()
        return

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']


        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        progress = round(100 * stats['attended'] / stats['total']) if stats['total'] else None

        def unenroll_button(sid, sub):
            if st.button(
                "Unenroll from this course",
                key=f"unenroll_{sid}",
                type="tertiary",
                width="stretch",
                icon=":material/delete_forever:",
            ):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f"Unenrolled from {sub['name']} successfully!")
                st.rerun()

        with cols[i % 2]:

            subject_card(
                name = sub['name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=lambda sid=sid, sub=sub: unenroll_button(sid, sub),
                accent_index=i,
                progress=progress,
            )
    footer_dashboard()


def student_screen():


    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.space()

    show_registration = False

    _, mid, _ = st.columns([1, 1.6, 1])
    with mid:
        with st.container(border=True, key="ax_card_login"):
            st.header('Login using FaceID', text_alignment='center')
            st.space()

            photo_source = st.camera_input("Position your face in the center")

            if photo_source:
                img = np.array(Image.open(photo_source))

                with st.spinner('AI is scanning..'):
                    detected, all_ids, num_faces = predict_attendance(img)

                    if num_faces == 0:
                        st.warning('Face not found!')
                    elif num_faces >1:
                        st.warning('Multiple faces found')
                    else:
                        if detected:
                            student_id = list(detected.keys())[0]
                            all_students = get_all_students()
                            student = next((s for s in all_students if s['student_id']==student_id), None)

                            if student:
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = student
                                st.toast(f"Welcome Back {student['name']}")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.info('Face not recognized! You might be a new student!')
                            show_registration = True

    if show_registration:
        _, mid, _ = st.columns([1, 1.6, 1])
        with mid:
            with st.container(border=True, key="ax_card_register"):
                st.header('Register new Profile', text_alignment='center')
                new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

                st.subheader('Optional : Voice Enrollment')
                st.info("Enroll your for voice only attendance")


                audio_data = None

                try:
                    audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
                except Exception:
                    st.error('Audio Data failed!')

                if st.button('Create Account', type='primary', width='stretch'):
                    if new_name:
                        with st.spinner('Creating profile..'):
                            img = np.array(Image.open(photo_source))
                            encodings= get_face_embeddings(img)
                            if encodings:
                                face_emb = encodings[0].tolist()

                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_data = response_data[0]
                                    st.toast(f'Profile Created! Hi {new_name}!')
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.error('Couldnt capture your facial features for registration')

                    else:
                        st.warning('Please enter your name!')


    footer_dashboard()
