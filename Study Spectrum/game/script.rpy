transform fit_screen:
    xsize 1280  
    ysize 720
label splashscreen:
    scene bg_classroom:
        xsize config.screen_width   
        ysize config.screen_height 
        anchor (0.5, 0.5) 
        pos (0.5, 0.5)   
        zoom 1.5          
    
    show student neutral at center
    with fade
    
    "แอดธีรดนย์" "คุณอาจจะงงว่าผมเป็นใคร ผมชื่อ แอดธีรดนย์"
    "แอดธีรดนย์" "ยินดีต้อนรับเข้าสู่เกมของพวกเรา 2 คน"
    "แอดธีรดนย์" "แนวเกมหลักเป็นเพียงการอธํิบายวิธีที่ใช้ในการเรียนรู้เฉยๆ"
    "แอดธีรดนย์" "ไม่ได้ลงลึกเท่าไหร่เกี่ยวกับการทำ Puzzle"
    "แอดธีรดนย์" "เราก็มีกันแค่นี้แหละน้องรัก"

    return
screen main_menu():
    tag menu

    window:
        style "mm_root"
    
    add "gui/main_menu.png":
        xysize (config.screen_width, config.screen_height)          
    frame:
        background Frame("images/frame.png", 10, 10) 
        xalign 0.5
        ypos 80          
       
        xsize 600        
        ysize 150         
        padding (20, 10)  
        text "Study Spectrum":
            size 60       # ลดขนาดตัวอักษรลงจาก 80 เหลือ 60
            xalign 0.5 
            yalign 0.5    # จัดให้อยู่กลางกรอบพอดี
            color "#ffffff"
            outlines [ (2, "#232ad3", 0, 0) ]

    # --- ส่วนที่ 2: ปุ่ม (ถ้าปุ่มใหญ่ไปก็แก้ที่ style ด้านล่างได้) ---
    vbox:
        xalign 0.5
        yalign 0.75       # ขยับแผงปุ่มลงมาข้างล่างอีกหน่อย
        spacing 12        # ลดระยะห่างระหว่างปุ่ม
        
        textbutton "Start Game" action Start() style "my_button"
        textbutton "Load Game" action ShowMenu("load") style "my_button"
        textbutton "Options" action ShowMenu("preferences") style "my_button"
        textbutton "Exit" action Quit(confirm=True) style "my_button"
style my_button:
    xsize 300       # ความกว้างของปุ่ม
    ysize 80       # ความสูงของปุ่ม
    background Frame("images/btn_base.png", 10, 10) # เอาปุ่มน้ำเงินมาทำเป็นพื้นหลัง
    padding (10, 10)
    xalign 0.5

style my_button_text:
    idle_color "#ffffff"    # สีตัวหนังสือตอนปกติ
    hover_color "#ffcc00"   # สีตัวหนังสือตอนเอาเมาส์ไปชี้
    size 30
    xalign 0.5
    yalign 0.5

# กำหนดค่าความมืด (0.5 คือลดแสงลงครึ่งหนึ่ง)
define char_dim = BrightnessMatrix(-0.5)
# กำหนดค่าปกติ
define char_normal = BrightnessMatrix(0.0)

label start:
    scene classroom_scene1:
        xsize config.screen_width 
        ysize config.screen_height
    
    with fade
    show student neutral as p1 at right:
        matrixcolor char_normal
    show student neutral as p2 at left:
        matrixcolor char_dim
    "นักเรียน" "เรื่องจริงของคาบูโต๊ะ คือนายใช่ไหม"
    show student neutral as p1 at right:
        matrixcolor char_dim
    show student neutral as p2 at left:
        matrixcolor char_normal
    "แอดธีรดนย์" "ถามอะไรโง่วๆ เหมือนหันไปถามพระอาทิตย์ว่าใช่พระอาทิตย์รีเปล่า"
    show student neutral as p1 at right:
        matrixcolor char_normal
    show student neutral as p2 at left:
        matrixcolor char_dim
    "นักเรียน" "ทำไมเข็มขัดคาบูโต๊ะถึงอยู่กับนายได้หล่ะ!"
    show student neutral as p1 at right:
        matrixcolor char_dim
    show student neutral as p2 at left:
        matrixcolor char_normal
    "แอดธีรดนย์" "ถามอะไรโง่วๆอีกแล้ว เหมือนหันไปถามพระอาทิตย์ว่าทำไมถึงส่องแสงนั่นแหละ"
    show student neutral as p1 at right
    show student neutral as p2 at left
    menu:
        "1.Focused & Diffuse Mode":
            jump scene_FDM

        "2. Active Recall":
            jump scene_AR

        "3. Spaced Repetition":
            jump scene_SR

        "4. Pomodoro Technique":
            jump scene_PT

        "5. Metacognition":
            jump scene_MC

        "6. Meditation":
            jump scene_MID
    label scene_FDM:
    scene classroom_option1:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    
    "ยินดีต้อนรับสู่คาบคณิตศาสตร์... เตรียมสูตรคูณให้พร้อม!"
    # เขียนเนื้อเรื่องต่อตรงนี้
    return

label scene_AR:
    scene classroom_option2:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    
    "คาบวิทย์เริ่มแล้ว อย่าทำหลอดทดลองแตกนะ"
    return

label scene_SR:
    scene classroom_option3:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    
    "Welcome to English Class!"
    return

label scene_PT:
    scene classroom_option4:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    "ได้เวลาปลดปล่อยจินตนาการในคาบศิลปะ"
    return

label scene_MC:
    scene classroom_option5:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    "ไปที่สนามบาสเพื่อเรียนพละกันเถอะ"
    return

label scene_MID:
    scene classroom_option6:
        xysize (config.screen_width, config.screen_height) # บังคับเต็มจอ
    "คาบดนตรีเริ่มขึ้นแล้ว... ฟังเสียงเปียโนนั่นสิ"
    return





