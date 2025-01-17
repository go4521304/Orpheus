﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('모르페우스', color="#353ec5")
define o = Character('오르페우스', color="#f1df3e")
define a = Character('관객', color="#da4a26")
define ma = Character('매곳', color="#916915")
define he = Character('헬리오스', color="#ff6600")
define ap = Character('아폴론', color="#ff0040")
define q = Character('???', color="#666666")
define cha = Character('카론', color="#666666")
define tele = Character('방송국', color="#da1111")

# 여기에서부터 게임이 시작합니다.
label start:
    transform slightleft:
        xalign 0.25
        yalign 0.5

    transform slightright:
        xalign 0.75
        yalign 0.5

    scene btv1 with fade 
    "0. Eschatos"
    "..."
    show tele with dissolve
    "지지지직"
    show teles1 with dissolve
    "텔레비전이 켜진다. 이후 소음이 들려온다."
    a "비웃음, 웃음소리, 비명 소리, 깨지는 소리가 들려온다"
    "텔레비전 클로즈 업"
    show sample_tv opening_1 at truecenter with dissolve
    "(DEVIL TV)"
    "새빨간 텔레비전에서 흥겨운 아나운서가 이야기를 전하고 있다"
    show sample_th opening_3 at truecenter with dissolve
    show ch_morpheus_2 at truecenter with dissolve
    m "하하하, 안녕하세요 지옥의 주민 여러분! 하이고! 600년만에 방송이네요!"
    m "안방 극장, 에스카토스! 시즌 666이 이제 곧 시작하려고 합니다!"
    a "(환호성)"
    m "영원히 기다리고 기다리시던 축제, 아니 고통의 시간이 돌아왔습니다!"
    m "발은 열심히 닦으셨나요? 이젠 뜨끈히 지질 때죠! 아, 잠깐만, 이 말을 하려 한게 아닌데?"
    "(무언가 스태프가 말을 하자 알아들으며)"
    m "음음! 그렇죠, 그래도 새로운 시즌의 시작이니 지옥의 유일무이한 엔터테인먼트를 잊어버리신 친구 모두를 위해서"
    m "다시 한 번 에스카토스에 대해서 설명해드리겠습니다."
    hide ch_morpheus_2 with dissolve
    show sample_th opening_2 with dissolve
    show ch_morpheus_4 at truecenter with dissolve
    m "영상 보고 오시죠"
    "에스카토스, 지옥 여러분들의 크고 작은 소망과 염원을 영원의 잠에 취하신 하데스님에게 전달하고"
    "그 특별한 역할을 맡게 된 전달자의 소원을 이루어 주는 굉장히 아름답고 설레이는 축제입니다."
    hide ch_morpheus_4 with dissolve
    show ch_morpheus_1 at truecenter with dissolve
    m "그리고 그 전달의 고난과 역경의 순간들을 여러분들에게 보여주는 것이 저와 우리 데빌 티비 스태프의 역할이죠."
    a "(야유하는 소리)"
    hide ch_morpheus_1 with dissolve
    show ch_morpheus_4 at truecenter with dissolve
    m "네? 틀렸다고요? 전혀 아니야? 사실 여러분들이 맞습니다. 아름다운거 그런거 전혀 필요없죠! 우리가 원하는건 뭐?"
    a "(고통!)"
    m "뭐라고?"
    a "(살육!)"
    m "마지막으로!"
    a "죽음!!"
    m "역시, 여러분. 전 여러분들이, 지옥이, 너무 좋습니다. 언제나 두근두근하거든요!"
    "(다시 스태프가 말을 하자 놀란 눈치로)"
    m "예? 벌써요? 서론은 여기까지 하고, 여러분! 도착했다고 합니다!"
    hide ch_morpheus_4 with dissolve
    show ch_morpheus_1 at truecenter with dissolve
    m "오래 기다리셨습니다!"
    m "우리의 새로운 스타, 독사 따위에 물려 죽은 아내를 구하기 위해! (흑흑흑!)"
    m "어머 너~ 무 로맨틱! 무려 이곳 지옥까지 행차하신~ 그 이름은 바로~~"
    scene bg1 with fade
    show ch_morpheus_5 at truecenter with dissolve
    "아나운서가 텔레비전 속에서 당신을 가리킨다"
    m "(조용하면서 멋있는 목소리로) 오르페우스, 당신이야."
    a "하하하하핳ㅎ하ㅏㅏ하하ㅏ하ㅏ하하"
    a "(비웃음, 웃음소리, 비명 소리, 깨지는 소리, 기타 등등)"
    hide ch_morpheus_5 with dissolve
    show ch_morpheus_2 at truecenter with dissolve
    m "(아나운서 톤으로) 에스카토스 시즌 666, 오르페우스 극장은 박하콜라, 에우레얄레 잡화점과 함께합니다."
    m "광고 보고 오시죠!"

    "(광고)"

    scene btv1 with fade
    "1. Avernus (아베르누스: 지옥 입구)"

    "어둠이다."
    "눈을 뜨니 슬며시 빛이 드는 불편한 어둠이 나를 찾는 것 같았다."
    q "어이.."
    "머리가 띵하다. 어딘가 부딪힌 걸까, 그런 생각을 하던 찰나에 목소리가 깨지듯이 들려왔다."
    q "어이, 정신이 드냐? 흐헤헿.."
    "하지만 그런 것을 신경 쓸 시간은 없다고 판단한 나는 자리에서 일어났다."
    q "어이, 무시하는 거냐? 이 구더기의 왕을?"
    show ch_maggot_2 at truecenter with dissolve
    "옆을 슬쩍 바라보자 작은 짐승만한 구더기 한 마리가 같은 길을 기어가고 있었다."
    "아무런 옷가지도 걸치지 않은, 벌거벗은 구더기였다. 애초에 무언가를 걸친 구더기가 있을 리가 없지만"
    "어찌되었든 왕의 지위에 걸맞는 행색은 아니었다."
    hide ch_maggot_2 with dissolve
    show ch_maggot_3 at truecenter with dissolve
    q "뭘 그리 골똘히 생각하나 그래, 응? 가슴이 절망으로 가득 찰 생각을 하니 두근두근 거리는구나, 그렇지? 흐헤헤헤헿헤"
    o "조용히 해."
    "그래, 조용히 해라. 나는 시답지 않은 농담을 주고받을 정도로 시간이 있는 것이 아니었다."
    q "그래, 조용히 하지… 그런다고 죽은 사람이 돌아올 것 같아? 흐헤헿"
    "나는 천천히 발걸음을 멈췄다. 말하는 구더기는 무언가를 더 아는 눈치였기 때문이었다."
    q "뭐야 그 눈빛은.. 설마, 내가, 아니, 지옥의 모든 쓰래기들이 너를 모른다고 생각하는 건 아니겠지?"
    "구더기는 고개를 절레절레 흔들었다. 그 짤막한 몸뚱어리에서 흘러나온 기분 나쁜 누런 액체가 나의 얼굴에 튀었다."
    q "하! 죽은 아내를 되찾으러 단신으로 지옥에 뛰어든 미친놈아, 잘들어."
    hide ch_maggot_3 with dissolve
    show ch_maggot_1 at truecenter with dissolve
    q "넌 이미 유명인이야. 내 이름은 매곳! 지옥은 널 환영한다! 그리고 너의 선택을 후회하게 만들 자신이 있지."
    o "그래, 여기가 시험대란 말인가?"
    "그 말을 들은 구더기가 나불거리던 입을 싹 닫았다. 구더기는 정말 모르겠냐? 라는 표정을 짓고 있었다."
    "그리고 그것을 확신을 한 구더기는."
    ma "시험대? 흐흫, 흐헤헤헤헿, 하하하핳하핳ㅎ하ㅏㅏㅏ하하하하"
    "포복절도를 하며 크게 웃었다."
    ma "이봐, 여긴 지옥이야, 시험대? 장난하냐? 그냥 널 죽일거야. 그게 다야. 미리 죽을 걸 축하해 줄 뿐이라고. 알겠어? 멍청아?"
    "그저 시간 낭비였다. 그것을 깨달은 나는 빠르게 앞을 향해 나아가기로 했다."
    ma "어이어이, 잠깐만, 잠깐만 기다려봐!"

    "이번이 이 구더기를 만나는 마지막이 될지도 모른다. 말을 들어볼까?"

    "그래, 마지막으로 이야기를 들어본다 (튜토리얼) / 아니다, 빨리 앞으로 나아가야한다 (건너뛰기)"

    "그래, 마지막으로 이야기를 들어본다"
    ma "뭐야, 아직 뭣도 몰라서 햇병아리처럼 구는게 참 귀엽네."
    ma "아직도 지옥 입구조차도 찾지 못한 모습이 안쓰러워서 얘기해준다. 강을 건너기 전에 금화 두 닢. 알겠지? 흐헤헿."
    "그 말을 끝으로 구더기는 어둠속으로 사라졌다. 금화 두 닢, 스틱스 강을 건널 때 필요한 뱃삯이다. 그걸 구해서 가자."

    "아니다, 빨리 앞으로 나아가야한다"
    "나는 구더기를 뒤로 하고 앞으로 나아갔다."

    scene sample_th opening_2 with fade

    "다시 텔레비전"

    show ch_morpheus_2 at truecenter with dissolve
    m "태양신 아폴론님과 뮤즈 칼리오페 사이에서 태어난 젊은 악사 오르페우스는"
    m "신의 재능을 이어받아 세계에서 제일 아름다운 리라 연주를 선보이곤 했습니다."
    m "아르고호 대원정에서 세이렌을 리라 연주로 잠재웠을 만큼 굉장한 실력의 소유자!"
    m "원정에서 무사히 귀환한 그는 아리따운 아내 에우리디케와 함께 행복한 나날들을 보내고 있었습니다."
    m "그런데 어느 날, 누군가의 음모인지, 마침 따분했던 어떤 신의 장난인지!"
    m "아내 에우리디케는 독사에 물려 그만 우리의 품으로 돌아왔습니다."
    m "아내를 잊을 수 없었던 오르페우스는 살아있는 몸으로 지옥에, 그녀를 찾으려는 염원을 품고 마침내 도착한 것입니다."

    m "정말 슬픕니다. (흑흑) 하지만 이 정도의 사랑과 의지가 있어야 에스카토스에 어울리는 멍청한 전달자라고 할 수 있겠죠!"
    m "(점잖은 목소리로) 여러분, 오래 기다리셨습니다. 오르페우스 극장, 그 어리석은 시작을 알리는 대망의 첫 곡은.."
    "슈베르트의 송어."
    hide ch_morpheus_2 with dissolve
    "(튜토리얼 시작)"
    "(곡이 끝나고)"

    show ch_morpheus_1 at truecenter with dissolve
    m "멋집니다, 그의 사랑을 위한 도전! 몇 번을 죽어도 다시 한 번!"
    scene sample_roulette_1 with fade
    m "그런 당신을 위해 룰렛! 아 룰렛 빠질 수 없죠! 바로 돌립니다! 고고고~"
    m "아이고 이게 뭐람! 이러면 망했죠! 오르페우스, 좀 더 잘 돌렸어야죠!"

    scene btv1 with fade
    "1-1. 스틱스 강 (건너뛰기)"

    show ch_or_std_1 at truecenter with dissolve
    "지옥의 입구에서 얼마나 나아갔을까"
    "지쳐 나가 떨어질 만큼 어둠을 헤집고 나오자 보인 것은 바다 같이 끝없이 펼쳐진 검은 물이었다."
    "소름이 끼칠 정도로 두려움이 엄습하는 것을 알 수 있었다."
    "본능적으로 느낄 수 있었다. 이곳이 죽음을 맞이하는 관문이라는 것을."
    show ch_or_std_1 at slightleft
    with move
    "물가에는 작은 배와 거대한 뱃사공, 그리고 배에 탑승하려는 죽은 이들로 넘쳐났다."
    "어느 쪽이건 흉물스러운 몰골, 악취, 스산한 기운이 이곳은 오로지 망자의 길이라고 말하는 것 같았다."
    show ch_charon_2 at slightright
    with move
    cha "너. 못 탄다."
    "망자에 어울려 배에 탑승하려던 나를 뱃사공이 막아섰다. 카론, 죽음을 인도하는 지옥의 뱃사공이었다."
    o "아니, 타겠습니다."
    cha "금화, 있나?"
    "그가 뱃삯을 바라며 검은 손을 내밀었다. 하지만 내게는 아무것도 없었다."
    cha "금화, 없다."
    hide ch_charon_2 with dissolve
    "고개를 좌우로 흔들자 뱃사공은 얼굴을 찌뿌리며 배에서 노를 집어 들었다. 그때 나는."

    "리라로 공격을 막으며 반격태세를 갖추었다 (보스 배틀) / 리라로 아름다운 선율을 연주했다 (건너뛰기)"

    "리라로 공격을 막으며 반격태세를 갖추었다 (보스 배틀)"
    "배틀 이후"
    show ch_charon_1 at truecenter with dissolve
    cha "나약하다. 하지만 의지 있다. 타라."
    "리라로 아름다운 선율을 연주했다 (건너뛰기)"
    cha "금화만큼 좋다. 타라."


    scene btv1 with fade
    "1-1. 스틱스 강 (튜토리얼)"

    show ch_or_std_1 at truecenter with dissolve
    "지옥의 입구에서 얼마나 나아갔을까"
    "지쳐 나가 떨어질 만큼 어둠을 헤집고 나오자 보인 것은 바다 같이 끝없이 펼쳐진 검은 물이었다."
    "소름이 끼칠 정도로 두려움이 엄습하는 것을 알 수 있었다."
    hide ch_or_std_1 with dissolve
    "본능적으로 느낄 수 있었다. 이곳이 죽음을 맞이하는 관문이라는 것을."
    "물가에는 작은 배와 거대한 뱃사공, 그리고 배에 탑승하려는 죽은 이들로 넘쳐났다." 
    "어느 쪽이건 흉물스러운 몰골, 악취, 스산한 기운이 이곳은 오로지 망자의 길이라고 말하는 것 같았다."
    show ch_charon_2 at truecenter with dissolve
    cha "너. 못 탄다."
    "망자에 어울려 배에 탑승하려던 나를 뱃사공이 막아섰다. 카론, 죽음을 인도하는 지옥의 뱃사공이었다."
    o "아니, 타겠습니다."
    cha "금화, 있나?"
    "그가 뱃삯을 바라며 검은 손을 내밀었다. 내가 금화 두 닢을 내려고 하자 뱃사공은 획 하고 금화를 낚아채 갔다."
    cha "금화라니, 기쁘구나."


    scene btv1 with fade
    o "이건 뭐지?"
    "아무것도 모른 체 앞으로 나아가던 나는 문득 이상한 점을 느꼈다."
    show tv_main_1 at truecenter with dissolve
    "시선이 느껴졌다. 굉장히 기분 나쁜 시선들."
    "정육면체의 물체에서는 그림이 계속 바뀌며 흥미를 유발하고 있었다."
    hide tv_main_1 with dissolve
    show ch_maggot_4 at truecenter with dissolve
    ma "뭐야, 텔레비전 몰라? 아, 그래. 지옥은 처음이었지."
    ma "간단히 말하자면, 미래의 물건이다. 지옥은 시간의 개념이 희박하지. 뒤틀려 있거든."
    hide ch_maggot_4 with dissolve
    show ch_maggot_1 at truecenter with dissolve
    ma "오늘 죽은 사람이나, 미래에 죽은 사람이나 모두 같은 공간에 있는 거다. 만들어지는 것도 비슷하지."
    o "그렇군.."
    ma "그리고 너가 멍청하게 시련이다 뭐다 하는건"
    ma "전부 연극이다. 모든 것은 계획되어 유흥으로 쓰여지는 거야."
    ma "넌 지금 지옥 최고의 장난감이야! 하하하하하하!"


    scene bg1 with fade
    show ch_morpheus_1 at truecenter with dissolve
    m "아, 벌써 하데스님께 향하는 튜토리얼을 겨우 통과한 오르페우스! 역시 최강 최흉의 머저리군요!"
    m "투철한 사랑의 힘으로 어디까지 가는겁니까! 이런 멋진 날에는 인터뷰를 빼놓을 수 없겠죠. 그럼 바로 불러보도록 하겠습니다."
    hide ch_morpheus_1 with dissolve
    show ch_or_std_1 at truecenter with dissolve
    "모르페우스가 손가락을 튕기자 무대가 회전하더니 게임을 막 통과해 기진맥진한 오르페우스가 보인다."
    "갑작스런 환경의 변화에 경계를 하듯 무기를 움켜쥐는 오르페우스." 
    hide ch_or_std_1 with dissolve
    show ch_morpheus_2 at truecenter with dissolve
    m "아아, 가여운 것. 아직도 이러고 있군요."
    m "지옥 여러분, 에스카토스 시즌 666의 주인공 오르페우스에게 따뜻한 동정의 박수 부탁드립니다!"
    a "괴물들의 비웃음, 박수, 야유"
    o "…?"




    #레이트 나잇 쇼
    scene world with fade
    tele "지옥에서 제일 멋진 빌딩!"
    tele "지옥에서 가장 재밌는 데빌TV!"
    scene sample_th opening_3
    tele "지옥에서 최고로 잔혹한 쇼! 에스카토스에서 보내드립니다!"
    show ch_morpheus_1 at truecenter with dissolve
    m "안녕하세요, 여러분의 꿈을 짓밟아주는 사랑의 지옥 버라이어티 쇼"
    m "오늘의 메뉴는 '질투의 인터뷰', '음욕의 콘서트', 그리고 '나태의 이세계"
    scene sample_curtain call_1 with fade
    m "아들래미 하나 때문에 모든걸 빼앗기고 추락한 엄청난 바보가 나오구요"
    m "3만년만의 신곡을 들고 나온 3인조와"
    m "최초의 무언가! 이건 스포일러 금지라고 하네요"
    scene sample_th opening_3 with fade
    show ch_morpheus_2 at truecenter with dissolve
    a "환호"
    m "모두들 감사합니다!"
    ma "에스카토스에 오신걸 환영해요"
    m "에스카토스의 귀여운 미친 놈! 당신의 영원한 쇼 호스트 모르페우스 입니다❤"
    hide ch_morpheus_2 with dissolve
    show ch_maggot_1 at truecenter with dissolve
    ma "저는 쇼 어시스턴트 '매곳'(구더기) 입니다"
    m "이거 정말 멋진 관객이군요"
    ma "지옥에는 정말 최고의 관객분들만 모여있군요"
    ma "그런 최고의 관객분들을 위해 제가 멋진 개그 하나 준비해왔습니다"
    m "오 매곳, 지금요? 이제 막 시작했는데.. 전혀 좋은 타이밍이 아니에요"
    ma "한 번만 믿어주세요 모르페우스. 우리 천년동안 여기 같이 갇혀있었잖아요"
    m "그래요 매곳 내 사랑, 제게는 당신 밖엔 없죠. 한 번 멋지게 웃겨봐요!"
    ma "이건 떨리네요.. 그럼 갑니다."
    ma "지옥에서 도움을 청할 때 뭐라고 해야 할까요!"
    ma "정답은 헬 프미!"
    cha "(드럼치는 모습을 보여주며 두둥탁)"
    a "..."
    m "..."
    ma "왜 왜 그래요 다들 헬 프미..."
    ma "모르페우스 헬 프미.."
    m "매곳, 10년간 개그 금지에요. 정말 봐줄 수가 없네요."
    m "아, 죄송합니다 관객 여러분. 못들은 척 하고 오늘의 첫번째 뉴스 보고 오시죠"
    m "매곳, 오늘 중요한 뉴스는 뭐가 있죠?"
    ma "몇가지 있긴 한데 가장 중요한건 이거네요"
    m "어디보자.. 저런! 제 666회 에스카토스의 히어로 오르페우스가 아직도 첫번째 경기 통과를 못했다고 합니다"
    ma "와이프 별로 안사랑하나 본데요?"
    m "그러게요. 솔직히 이제와서지만 별로 중요하지도 않은 것 같아요."
    ma "아니 모르페우스, 이번 주인공 쟤라면서요"
    m "매곳, 솔직히 에스카토스건 뭐건 시청률만 올라가면 그만이에요"
    ma "오, 반박할 수 없네요"
    m "그리고 요즘 트렌드는 짧고 굵게 재밌는거죠!"
    m "금방금방 넘어가야 질리지 않으니까요"
    m "그럼 첫번째 코너죠! 조금 덜 멋진 게스트 분의 부끄러운 과거사와 함께하는 최고로 멋진 인터뷰!"
    m "질투의 인터뷰! 오늘의 게스트는.. "
    #게스트 목록: 헬리오스 인터뷰 하다가 아폴로 깜짝 출현 및 쌍방 디스전
    #케르 베 루스 신곡 콘서트
    #지옥 최초 버튜버 스킬라쨩과 버츄얼 방송
    m "밝은 미래의 상징이었던 것! 그래도 아직은 뜨거운 심장의 소유자!"
    m "태양 마차로 우리 지옥은 못비추고 지상만 비춰줬죠!"
    m "그러니까 나락으로 떨어진겁니다!"
    ma "이거 다~ 업보에요!"
    m "소개합니다! 헬~리오스!"

    he "하, 정말 저급한 설명뿐이군"
    he "이봐 가짜, 어디까지 입을 놀릴 셈이냐"
    he "네놈, 그러고도 올림포스가 너를 용서할 것 같더냐"
    m "아아~ 우리 '전직' 태양신님께서, 마차에서 떨어지셔서 머리를 크~게 다치신 것 같습니다!"
    m "여기가 어디?"
    a "관객: 지옥!"
    m "누구의 지옥?"
    a "하데스님!"
    m "그렇죠, 이곳은 영원한 죽음의 신 하데스님의 신역. 올림포스의 그 누구도 간섭할 수 없습니다"
    m "힘을 빼앗겨서 별 것도 아니게된 당신은 더더욱. 캬캬캬캬캬컄"
    m "뭐 발끈하지 마시고 앉으시죠, 헬리오스. 과거는 오락이에요. 그 추억을 되감으면서 한 번 재밌게 웃을 수 있다면"
    m "그걸로 충분하지 않을까요?"
    m "아, 미안해요 네 과거는 우리만 재밌죠"
    m "넌 재미 없죠 캬캬캬캬컄"
    he "이곳을 불바다로 만들어주마, 모르페우스"
    m "엥?"
    m "이미 불바다인데 무슨 소리신지.. 공격을 하시려면 좀 더 맛있는 걸로 부탁드립니다."
    m "별거 없으니까 시청률 떨어지잖아요"
    "(떨어지는 실시간 시청자 수를 보여주며)"
    m "아무튼, 스몰토크는 이 정도로 하고 인터뷰 진행해보도록 하겠습니다"

    m "모두 모르셨겠지만 저희가 괜히 헬리오스님을 모신게 아닙니다"
    ma "에스카토스의 주인공은 오르페우스만 있는게 아니죠!"
    m "더블 주인공 캬~ 이거죠"
    m "그래서 오늘 우리는 헬리오스님에 대해서 조금 더 알아보는 시간을 가져보려고 합니다"
    m "그러려면! 즐거운 게임 한번 하는게 좋겠죠?"
    m "그래서 준비했습니다! 레이스 오브 러브❤"
    ma "레이스 오브 러브! 1대1로 레이스를 펼쳐 사랑을 쟁취하면 되는 쉬운 게임인데요"
    m "헬리오스님?"
    he "뭐냐, 천박한 것의 아이야"
    m "호오, 최초의 태양은 역시 모든 것을 꿰뚫어 보는군요. 아주 멋집니다!"
    he "본론을 말하거라."
    m "그러죠! 소개합니다! 석양을 죽일 눈부신 아침 햇살! 아폴론님 이십니다!"
    ap "짐은 태양이니라!"
    m "정말 오만하기 짝이 없군요, 헬리오스님, 어떻게 생각하십니까?"
    he "올림포스의 이름에 먹칠을 하는군"
    ap "누구인가? 잘 보이지도 않는구나. 성냥 한개비가 그대보다 밝겠구나."
    ap "어리석은 것. 가서 아들래미 기저귀나 갈아주고 오거라"
    he "오만방자한 것, 뒤로 여색이나 밝히는 더러운 것이 태양신이라니, 이제 진실은 전부 썩어 문드러졌구나"
    m "워워, 두 분 진정하시고~ 싸움은 레이스에서 보여주시면 되죠!"
    ma "그래서 아폴론님은 왜 여기 오신거죠?"
    m "아 매곳, 이번에 신곡 내는 걔네 있잖아요"
    ma "아 개세마리요?"
    m "매곳, 그래도 멋있게 3DOGS 라고 해주세요"
    ma "그게 그 말이잖아요"
    m "... 어쨌든! 심사위원으로 초청했더니 흔쾌히 와주셨습니다! 감사합니다, 아폴론님!"
    "(작게 따봉을 날리는 아폴론)"
    ap "썩어도 태초의 아이라더니, 지옥도 나름 활기차고 좋구나."
    m "네, 그러면 게임 시작해볼까요? 레이스~ 스타트!"
    #레이스 오브 러브 - 태양마차를 타고 사랑하는 사람에게 먼저 도달하자! 지면 사랑하는 사람은 지옥 끝으로 떨어져요~ 
    #ZX 연타를 통해 스피드 업! 스페이스바로 점프! 누구보다도 빠르게 결승선에 도달하자!

    m "아폴론님, 생각해보니 오르페우스가 아폴론님 아드님이셨네요."
    ap "어리석은 나의 아이 말이로구나" #머리를 짚으며
    m "그래도 아폴론님을 쏙 빼닮아서 아주 사랑꾼이에요"
    ap "올림포스 또한 아이의 애절함을 부러워 하더구나"
    m "오, 마치 나이 먹은 고약한 할아버지가 멜로 드라마를 보고 말하는 것 같네요!"
    "(발끈)"


    m "아아 이거 두 멍청이들을 보니 너무 분위기가 올라갔네요."
    m "조금 쉬는 타임을 가져볼까요? 쉬어가는 뉴스! 뉴스 타임~"
    ma "모르페우스, 뉴스 전에 당신이라면 어떤 개그를 쳤을지 정말 궁금해요"
    m "매곳 매곳 매곳.. 과거에 연연해 하면 안돼요 지금 방송 중이잖아요"
    ma "하지만 여기서 웃기면 시청률이 급상승할거에요!"
    m "음! 일리가 있네요, 그럼 한 번 해보겠습니다."
    m "세상에서 가장 크고! 가장 야한 종족은?"
    m "티탄! ('Tit'an)"
    a "...."
    ma "...."
    m "매 매곳 티탄족이라구요 완전 크고 쌔끈하고.."
    ma "모르페우스. 우리 쇼, 개그는 하면 안될 것 같아요"
    m "아..."
    ma "넘어가서! 모르페우스? 그런데 제가 먼저 후루룩 하고 읽어보았습니다만.."
    ma "상황이 너무 좋지 않습니다"#엄근진
    ma "전 세계적으로 결혼률이 급감했다는 소식입니다"
    m "아니 매곳! 도대체 왜 그렇죠?"
    ma "아, 여기 통계가 써있군요"
    m "어디 줘 보세요. 3위가 어디보자.. 아 돈이 부족해서!"
    m "(모르페우스 웃음소리)"
    m "풉..  이건 좀 불쌍하네요. 돈 없어서 뒤졌을텐데 지옥에서도 돈이 없다니! 정말 잘~하는 짓입니다"
    m "그런 당신을 위한 멋진 장소가 있습니다!" #도박시설 '골든 샤워 오브 미다스!' 금이 비처럼 떨어진다는 뜻이지만 "18금 뜻"도 맞음
    m "그건 바로 황금빛으로 당신의 하트를 가득 매워줄 원더랜드!"
    m "데빌TV 방송국 바로 옆건물에 위치한 꿈의 나라 '골든 샤워 오브 미다스'죠!"
    ma "모르페우스, 나 거기서 금화 3억개정도 잃은 것 같아요"
    m "괜찮아 매곳, 나도 그래."
    m "아! 그 어... 여러분은 저희 스택 빨아가시라는 소리죠! 하하하하!!"
    ma "그쵸그쵸 이번에 새로운 기기도 들여왔다면서요?"
    m "아, 지상에서는 꽤나 롱런하고 있는 제품이라고 하더군요"
    m "어디보자.. 기기명이 '빠칭코'군요"
    m "설명서에는 이렇게 써있군요"
    m "'원하는 만큼 금화를 넣고 레버를 당기세요'"
    ma "그게 다에요?"
    m "네 매곳, 그게 답니다"
    ma "쓰레기같네요"
    m "만들기 제일 쉬운걸로 들고와서 그래요 뭐라하지 말아요"
    m "아아 잠시 다른 이야기로 세어버렸네요! '골든 샤워 오브 미다스'! 많은 관심 부탁드립니다."
    m "이제 2위로 넘어가죠"
    m "2위가 결혼을 안해도 XX만 하면 그만이야"
    ma "와 모르페우스, 다들 쓰레기네요?"
    m "뭐 그다지 틀린 말도 아니죠, 매곳. 어차피 결혼이라는건 얽매이는거니까요."
    m "우리가 만들어진대로 번식에 목적을 둔다면 결혼같은건 필요 없어요"
    ma "그렇죠."
    m "물론 월 3천도 못버는 베타메일들은 다 죽어버리지만요"
    ma "하하하! 굉장히 웃겼어요 모르페우스. 방금 발언으로 이 게임 끄는 사람도 있겠는걸요?"
    m "걱정 말아요 매곳, 여기 두 시간 구간이어서 환불도 못해요."
    ma "아, 다 계획된거군요?"
    m "이 게임, 아니 방송에 계획이 안된게 없습니다"
    ma "오오.."
    m "이제 대망의 1위만을 남겨놓고 있는데요"
    ma "이건..."
    m "광고 보고 오시죠!"

    tele "'골든 샤워 오브 미다스'"
    tele "황금의 나라로 오세요~ 황홀한 금화 쏟아지는 곳!"
    tele "황천의 나라로 오세요~ 끝없는 나락의 나라 '골든 샤워 오브 미다스'!"


    m "네, 잘 돌아오셨습니다!"
    m "이제 결혼율 급감의 원인 1위만을 남겨두고 있는데요!"
    ma "과연 뭘까요?"
    m "대망의 1위! 그것은 바로! 데빌티비를 보면 딱히 결혼 생각 안들어서!"
    m "캬, 역시 지옥 최고의 엔터테인먼트!"
    ma "아, 모르페우스 이거 그건데요?"
    m "뭐죠 매곳?"
    ma "최근에 나온 논문 결과에 따르면 돈이 부족할수록 모니터 속을 들여다 보는 시간이 증가하고 생활 반경이 축소한다는 이야기가 있는데"
    m "매곳, 아주 정확해요! 이딴걸 보고 즐거움을 느낄 정도면 어지간히 망한 인생이에요!"
    ma "빨리 나가서 누구 하나 말 걸어서 네 인생 좀 살라구요"
    m "아 그렇다고 진짜 나가서 누구 하나 붙잡아서 말 걸지 마세요, 경찰서로 출두할겁니다 변태씨" # ok? you'll freak everyone out there.
    m "그런데 데빌티비 은근 재밌지 않나요?"
    ma "그렇죠, 우리가 여러가지 많이 준비 했으니까요"
    m "아직 못다한 이야기들도 많죠!"
    ma "쌔끈한 악마 아가씨들도 많죠!" 






