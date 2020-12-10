import pyautogui as pag
import random, time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime

arr=[
    '정말 좋은 강의입니다~~~~~!', 
    '로봇과 함께 생활하는 세상',
    '지금은 학습을 잘 하는 사람이 살아 남는 시대 입니다.', 
    '모든게 자동화 되는 세상', 
    '댓글도 로봇이 작성해주는 세상',
    '사람은 학습하고 로봇은 일하고', 
    '시일사학', 
    '단순작업은 로봇이 짱이지!!!', 
    '혁신을 넘어서는 진화 LSElectric DT 성공을 기원합니다.', 
    'CT=PT=DT 꼭 성공합시다.',
    '단순 업무는 똘똘한 로봇이 ',
    'DT를 위해 데이터 문해력은 필수 입니다.',
    '야 너두 데이터 분석 할 수 있어 ',
    '생존을 위한 CT', 
    '야 너두 간단한 프로그램으로 업무 자동화 할 수 있어 '
]

link = 'https://lselectric.touchclass.com/lms/MyCourse?direction=asc&group=ALL&orderby=order&page=1&per=20&status=STUDYING&type=MY'
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.get(link)

driver.find_element_by_name('Mb_Mail').send_keys('~~~~') # 아이디 '입력'
sleep(2)
driver.find_element_by_name('Mb_Pw').send_keys('~~~~') # 패스워드 '입력' 
sleep(2)
# 로그인 버튼 누르기
driver.find_element_by_id('BTN_USER_LOGIN').click() 
sleep(6) # 좀 오래 쉬어줘야 됨 

# 팝업창 없애기 (마우스 클릭)
#pag.moveTo(870,200)

# 팝업창 없애기
driver.find_element_by_class_name('btn_pop_close').click()
sleep(4)

# 3개 중, 제일 좌측 코스 누르기
driver.find_element_by_class_name('image-wrap').click()
sleep(4)

# # 의견 클릭하기
# element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "from-now")))
# driver.execute_script("arguments[0].click();", element)
# sleep(4)

# 커리큘럼 1 클릭하기
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "t_big.cname.ViewerStart")))
driver.execute_script("arguments[0].click();", element)
sleep(4)
#driver.find_element_by_class_name('t_big.cname.ViewerStart').click()
#sleep(4)

RANK_NAME = ['조지훈', '편찬범']

temp_index = []
c = 1
write_c = 1
while True:
    # 다음(>) 버튼 누르기
    driver.find_element_by_class_name('next_nav').click()
    sleep(4)

    # 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    sleep(1)

    # 의견 말풍선 누르기
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "push_bottom.pull_opinion.js_right_view")))
    driver.execute_script("arguments[0].click();", element)
    sleep(4)

    
    # --------------------------------의견에 댓글 달기--------------------------------
    # 댓글 스크롤 할 수 있게 마우스 이동하기
    pag.click(900, 300)
    # 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    sleep(1)

    total = 0
    num = 6
    while total<3 and num<13:
        # 인덱스 구하기
        index = random.randint(0, len(arr)-1) # 랜덤 인덱스 
        while True:
            if index in temp_index:
                if index == len(arr)-1: #마지막 인덱스라면
                    index = 0
                index += 1
            else:
                break
        if len(temp_index) == 3:
            temp_index = temp_index[1:]
        temp_index.append(index)

        # name구하기
        target_name = driver.find_element_by_css_selector('.js_opinion.item:nth-child(' + str(num) + ') .name').text
        print('target_name = ', target_name)

        if target_name not in RANK_NAME:
            driver.find_element_by_css_selector('.js_opinion.item:nth-child(' + str(num) + ')').click() # 의견 박스 클릭
            print(str(num) + '의견박스 클릭됨')
            sleep(2)
            driver.find_element_by_css_selector('.cont.Cm_Desc').send_keys(arr[index]) # 댓글 적는 칸 클릭
            print(str(num) + '댓글 적기 완료')
            sleep(2)
            driver.find_element_by_css_selector('#BTN_COMMENT_ADD').click() # 댓글 업로드
            print(str(num) + '댓글 업로드 완료')
            sleep(2)

            print('(20초간 휴식...)')
            sleep(20)
            
            print('총 ' + str(c) + '개의 자동 댓글 작성 완료!!')
            print()
            c += 1

            total += 1
        num += 1

    # --------------------------------글쓰기--------------------------------
    # print('글쓰기 위해 잠시 60초를 쉽니다...')
    # sleep(60)
    
    # index = random.randint(0, len(arr)-1) # 랜덤 인덱스 
    # while True:
    #     if index in temp_index:
    #         if index == len(arr)-1: #마지막 인덱스라면
    #             index = 0
    #         index += 1
    #     else:
    #         break
    # if len(temp_index) == 3:
    #     temp_index = temp_index[1:]
    # temp_index.append(index)

    # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inner")))
    # driver.execute_script("arguments[0].click();", element)
    # sleep(2)

    # driver.find_element_by_class_name('text_input_op').send_keys(arr[index])
    # sleep(4)

    # # 의견 올리기
    # driver.find_element_by_id('BTN_OPINION_ADD').click()
    # sleep(4)

    # print('총 ' + str(write_c) + '개의 의견 작성 완료!!')
    # write_c += 1

    # --------------------------------마무리 단계--------------------------------
    # 일정시간 학습활동 없는 오류 해결하기 위해...
    pag.click(300, 900) # 가운데 화면 클릭해서 의견창 나가기

    # 이전(<) 버튼 누르기
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "pre_nav")))
    driver.execute_script("arguments[0].click();", element)
    sleep(2)

    print('(다음 단계를 위해.. 30~40초 쉬기...)')
    time.sleep(random.uniform(30.0, 40.0)) # 30초 쉬기  


# # 오후 10시부터는 30초 간격으로...
# while True:
#     # 다음(>) 버튼 누르기
#     driver.find_element_by_class_name('next_nav').click()
#     sleep(4)

#     # 스크롤 끝까지 내리기
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
#     sleep(1)

#     # 의견 말풍선 누르기
#     element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "push_bottom.pull_opinion.js_right_view")))
#     driver.execute_script("arguments[0].click();", element)
#     sleep(4)

#     index = random.randint(0, len(arr)-1) # 랜덤 인덱스 
#     while True:
#         if index in temp_index:
#             if index == len(arr)-1: #마지막 인덱스라면
#                 index = 0
#             index += 1
#         else:
#             break
#     if len(temp_index) == 3:
#         temp_index = temp_index[1:]
#     temp_index.append(index)

#     element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inner")))
#     driver.execute_script("arguments[0].click();", element)
#     sleep(2)

#     driver.find_element_by_class_name('text_input_op').send_keys(arr[index])
#     sleep(4)

#     # 의견 올리기
#     driver.find_element_by_id('BTN_OPINION_ADD').click()
#     sleep(4)
#     print('지금은 오후10시...30초 간격으로 합니다!!')
#     print('총 ' + str(c) + '개의 자동 댓글 작성 완료!!')
#     c += 1

#     # 일정시간 학습활동 없는 오류 해결하기 위해...
#     pag.click(300, 900) # 가운데 화면 클릭해서 의견창 나가기

#     # 이전(<) 버튼 누르기
#     element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "pre_nav")))
#     driver.execute_script("arguments[0].click();", element)
#     sleep(2)

#     time.sleep(random.uniform(30.0, 40.0))  

