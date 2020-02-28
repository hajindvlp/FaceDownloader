import cv2
import face_recognition as fr
import multiprocessing
from multiprocessing import Process

FPS = 0
LENGTH = 0
SEGMENT = 10
margin = (50, 15, 40, 15)
W = 110
H = 110
procs = []


def frame2sec(frame):
    global FPS
    sec = int(frame / FPS)
    return sec


def sec2frame(sec):
    global FPS
    frame = sec * FPS
    return frame


def capture_face(start, end, window_name):
    global margin

    cap = cv2.VideoCapture("./videos/Test1.mp4")
    cap.set(1, start)
    frame_count = 0

    while frame_count < end - start:
        frame_count += 1
        ret, frame = cap.read()
        face_landmarks = fr.face_landmarks(face_image=frame, model="small")
        for landmark in face_landmarks:
            if landmark['right_eye'][0][0] - landmark['left_eye'][0][0] >= 70:
                mY = int((landmark['right_eye'][1][1] + landmark['left_eye'][1][1])/2)
                mX = int((landmark['right_eye'][1][0] + landmark['left_eye'][1][0])/2)
                croped_image = frame[mY - W - margin[0]:mY + W + margin[2],
                                     mX - H - margin[3]:mX + H + margin[1]]
                image_name = f"./faces/{start}_{start + frame_count}_{end}.png"
                cv2.imwrite(image_name, croped_image)
                print(f"[*] On {window_name} window : Image {image_name} saved")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def exit_proc():
    global procs

    cv2.namedWindow("quit")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        for proc in procs:
            proc.join()


def init():
    global FPS, LENGTH

    cap = cv2.VideoCapture("./videos/Test1.mp4")
    FPS = cap.get(cv2.CAP_PROP_FPS)
    LENGTH = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"CPU Number : {multiprocessing.cpu_count()}")

    print(f"[*] Test1.mp4 fps: {FPS}, length: {LENGTH}")


def main():
    global SEGMENT, procs

    init()
    try:
        for i in range(SEGMENT):
            print(int(LENGTH / SEGMENT) * i, int(LENGTH / SEGMENT) * (i + 1) - 1, f"{i} cam")
            proc = Process(target=capture_face,
                           args=(int(LENGTH / SEGMENT) * i,
                                 int(LENGTH / SEGMENT) * (i + 1) - 1,
                                 f"{i} cam"))
            procs.append(proc)
            print(f"[*] Starting {i}'th process")
            proc.start()

        print(f"[*] Starting Exit process")
        proc = Process(target=exit_proc)
        procs.append(proc)
        proc.start()
    except:
        print("error on threading")

    for proc in procs:
        proc.join()


if __name__ == "__main__":
    main()
