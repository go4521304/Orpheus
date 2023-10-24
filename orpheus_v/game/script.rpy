﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('모르페우스', color="#353ec5")
define o = Character('오르페우스', color="#f1df3e")
define a = Character('관객', color="#da4a26")



# 여기에서부터 게임이 시작합니다.
label start:

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
    show sample_tv opening_2 at truecenter with dissolve
    m "하하하, 안녕하세요 지옥의 주민 여러분! 하이고! 600년만에 방송이네요!"
    m "안방 극장, 에스카토스! 시즌 666이 이제 곧 시작하려고 합니다!"
    a "(환호성)"
    m "영원히 기다리고 기다리시던 축제, 아니 고통의 시간이 돌아왔습니다!"
    m "발은 열심히 닦으셨나요? 이젠 뜨끈히 지질 때죠! 아, 잠깐만, 이 말을 하려 한게 아닌데?"
    "(무언가 스태프가 말을 하자 알아들으며)"
    m "음음! 그렇죠, 그래도 새로운 시즌의 시작이니 지옥의 유일무이한 엔터테인먼트를 잊어버리신 친구 모두를 위해서 다시 한 번 에스카토스에 대해서 설명해드리겠습니다."
    m "영상 보고 오시죠"
    "에스카토스, 지옥 여러분들의 크고 작은 소망과 염원을 영원의 잠에 취하신 하데스님에게 전달하고 그 특별한 역할을 맡게 된 전달자의 소원을 이루어 주는 굉장히 아름답고 설레이는 축제입니다."
    m "그리고 그 전달의 고난과 역경의 순간들을 여러분들에게 보여주는 것이 저와 우리 데빌 티비 스태프의 역할이죠."
    a "(야유하는 소리)"
    m "네? 틀렸다고요? 전혀 아니야? 사실 여러분들이 맞습니다. 아름다운거 그런거 전혀 필요없죠! 우리가 원하는건 뭐?"
    a "(고통!)"
    m "뭐라고?"
    a "(살육!)"
    m "마지막으로!"
    a "죽음!!"
    m "역시, 여러분. 전 여러분들이, 지옥이, 너무 좋습니다. 언제나 두근두근하거든요!"
    "(다시 스태프가 말을 하자 놀란 눈치로)"
    m "예? 벌써요? 서론은 여기까지 하고, 여러분! 도착했다고 합니다!"
    m "오래 기다리셨습니다!"
    m "우리의 새로운 스타, 독사 따위에 물려 죽은 아내를 구하기 위해! (흑흑흑!)"
    m "어머 너~ 무 로맨틱! 무려 이곳 지옥까지 행차하신~ 그 이름은 바로~~"

    "아나운서가 텔레비전 속에서 당신을 가리킨다"
    m "(조용하면서 멋있는 목소리로) 오르페우스, 당신이야."
    a "하하하하핳ㅎ하ㅏㅏ하하ㅏ하ㅏ하하"
    a "(비웃음, 웃음소리, 비명 소리, 깨지는 소리, 기타 등등)"
    m "(아나운서 톤으로) 에스카토스 시즌 666, 오르페우스 극장은 박하콜라, 에우레얄레 잡화점과 함께합니다."
    m "광고 보고 오시죠!"

    "(광고)"


    "1. Avernus (아베르누스: 지옥 입구)"

    "어둠이다."
    "눈을 뜨니 슬며시 빛이 드는 불편한 어둠이 나를 찾는 것 같았다."
    "어이.."
    "머리가 띵하다. 어딘가 부딪힌 걸까, 그런 생각을 하던 찰나에 목소리가 깨지듯이 들려왔다."
    "어이, 정신이 드냐? 흐헤헿.."
    "하지만 그런 것을 신경 쓸 시간은 없다고 판단한 나는 자리에서 일어났다."
    "어이, 무시하는 거냐? 이 구더기의 왕을?"
    "옆을 슬쩍 바라보자 작은 짐승만한 구더기 한 마리가 같은 길을 기어가고 있었다."
    "아무런 옷가지도 걸치지 않은, 벌거벗은 구더기였다. 애초에 무언가를 걸친 구더기가 있을 리가 없지만, 어찌되었든 왕의 지위에 걸맞는 행색은 아니었다."
    "뭘 그리 골똘히 생각하나 그래, 응? 가슴이 절망으로 가득 찰 생각을 하니 두근두근 거리는구나, 그렇지? 흐헤헤헤헿헤"
    "조용히 해."
    "그래, 조용히 해라. 나는 시답지 않은 농담을 주고받을 정도로 시간이 있는 것이 아니었다."
    "그래, 조용히 하지… 그런다고 죽은 사람이 돌아올 것 같아? 흐헤헿"
    "나는 천천히 발걸음을 멈췄다. 말하는 구더기는 무언가를 더 아는 눈치였기 때문이었다."
    "뭐야 그 눈빛은.. 설마, 내가, 아니, 지옥의 모든 쓰래기들이 너를 모른다고 생각하는 건 아니겠지?"
    "구더기는 고개를 절레절레 흔들었다. 그 짤막한 몸뚱어리에서 흘러나온 기분 나쁜 누런 액체가 나의 얼굴에 튀었다."
    "하! 죽은 아내를 되찾으러 단신으로 지옥에 뛰어든 미친놈아, 잘들어. 넌 이미 유명인이야. 지옥은 널 환영한다! 그리고 너의 선택을 후회하게 만들 자신이 있지."
    "그래, 여기가 시험대란 말인가?"
    "그 말을 들은 구더기가 나불거리던 입을 싹 닫았다. 구더기는 정말 모르겠냐? 라는 표정을 짓고 있었다. 그리고 그것을 확신을 한 구더기는."
    "시험대? 흐흫, 흐헤헤헤헿, 하하하핳하핳ㅎ하ㅏㅏㅏ하하하하"
    "포복절도를 하며 크게 웃었다."
    "이봐, 여긴 지옥이야, 시험대? 장난하냐? 그냥 널 죽일거야. 그게 다야. 미리 죽을 걸 축하해 줄 뿐이라고. 알겠어? 멍청아?"
    "그저 시간 낭비였다. 그것을 깨달은 나는 빠르게 앞을 향해 나아가기로 했다."
    "어이어이, 잠깐만, 잠깐만 기다려봐!"

    "이번이 이 구더기를 만나는 마지막이 될지도 모른다. 말을 들어볼까?"

    "그래, 마지막으로 이야기를 들어본다 (튜토리얼) / 아니다, 빨리 앞으로 나아가야한다 (건너뛰기)"

    "그래, 마지막으로 이야기를 들어본다"
    "뭐야, 아직 뭣도 몰라서 햇병아리처럼 구는게 참 귀엽네. 아직도 지옥 입구조차도 찾지 못한 모습이 안쓰러워서 얘기해준다. 강을 건너기 전에 금화 두 닢. 알겠지? 흐헤헿."
    "그 말을 끝으로 구더기는 어둠속으로 사라졌다. 금화 두 닢, 스틱스 강을 건널 때 필요한 뱃삯이다. 그걸 구해서 가자."

    "아니다, 빨리 앞으로 나아가야한다"
    "나는 구더기를 뒤로 하고 앞으로 나아갔다."


    "다시 텔레비전"

    "태양신 아폴론님과 뮤즈 칼리오페 사이에서 태어난 젊은 악사 오르페우스는 신의 재능을 이어받아 세계에서 제일 아름다운 리라 연주를 선보이곤 했습니다. 아르고호 대원정에서 세이렌을 리라 연주로 잠재웠을 만큼 굉장한 실력의 소유자! 원정에서 무사히 귀환한 그는 아리따운 아내 에우리디케와 함께 행복한 나날들을 보내고 있었습니다. 그런데 어느 날, 누군가의 음모인지, 마침 따분했던 어떤 신의 장난인지! 아내 에우리디케는 독사에 물려 그만 우리의 품으로 돌아왔습니다. 아내를 잊을 수 없었던 오르페우스는 살아있는 몸으로 지옥에, 그녀를 찾으려는 염원을 품고 마침내 도착한 것입니다."

    "정말 슬픕니다. (흑흑) 하지만 이 정도의 사랑과 의지가 있어야 에스카토스에 어울리는 멍청한 전달자라고 할 수 있겠죠! (점잖은 목소리로) 여러분, 오래 기다리셨습니다. 오르페우스 극장, 그 어리석은 시작을 알리는 대망의 첫 곡은.."
    "슈베르트의 송어."

    "(튜토리얼 시작)"
    "(곡이 끝나고)"

    "멋집니다, 그의 사랑을 위한 도전! 몇 번을 죽어도 다시 한 번!"
    "그런 당신을 위해 룰렛! 아 룰렛 빠질 수 없죠! 바로 돌립니다! 고고고~"
    "아이고 이게 뭐람! 이러면 망했죠! 오르페우스, 좀 더 잘 돌렸어야죠!"

    "1-1. 스틱스 강 (건너뛰기)"

    "지옥의 입구에서 얼마나 나아갔을까"
    "지쳐 나가 떨어질 만큼 어둠을 헤집고 나오자 보인 것은 바다 같이 끝없이 펼쳐진 검은 물이었다."
    "소름이 끼칠 정도로 두려움이 엄습하는 것을 알 수 있었다."
    "본능적으로 느낄 수 있었다. 이곳이 죽음을 맞이하는 관문이라는 것을." 
    "물가에는 작은 배와 거대한 뱃사공, 그리고 배에 탑승하려는 죽은 이들로 넘쳐났다. 어느 쪽이건 흉물스러운 몰골, 악취, 스산한 기운이 이곳은 오로지 망자의 길이라고 말하는 것 같았다."
    "너. 못 탄다."
    "망자에 어울려 배에 탑승하려던 나를 뱃사공이 막아섰다. 카론, 죽음을 인도하는 지옥의 뱃사공이었다."
    "아니, 타겠습니다."
    "금화, 있나?"
    "그가 뱃삯을 바라며 검은 손을 내밀었다. 하지만 내게는 아무것도 없었다."
    "금화, 없다."
    "고개를 좌우로 흔들자 뱃사공은 얼굴을 찌뿌리며 배에서 노를 집어 들었다. 그때 나는."

    "리라로 공격을 막으며 반격태세를 갖추었다 (보스 배틀) / 리라로 아름다운 선율을 연주했다 (건너뛰기)"

    "리라로 공격을 막으며 반격태세를 갖추었다 (보스 배틀)"
    "배틀 이후"
    "나약하다. 하지만 의지 있다. 타라."
    "리라로 아름다운 선율을 연주했다 (건너뛰기)"
    "금화만큼 좋다. 타라."


    "1-1. 스틱스 강 (튜토리얼)"

    "지옥의 입구에서 얼마나 나아갔을까"
    "지쳐 나가 떨어질 만큼 어둠을 헤집고 나오자 보인 것은 바다 같이 끝없이 펼쳐진 검은 물이었다."
    "소름이 끼칠 정도로 두려움이 엄습하는 것을 알 수 있었다."
    "본능적으로 느낄 수 있었다. 이곳이 죽음을 맞이하는 관문이라는 것을."
    "물가에는 작은 배와 거대한 뱃사공, 그리고 배에 탑승하려는 죽은 이들로 넘쳐났다. 어느 쪽이건 흉물스러운 몰골, 악취, 스산한 기운이 이곳은 오로지 망자의 길이라고 말하는 것 같았다."
    "너. 못 탄다."
    "망자에 어울려 배에 탑승하려던 나를 뱃사공이 막아섰다. 카론, 죽음을 인도하는 지옥의 뱃사공이었다."
    "아니, 타겠습니다."
    "금화, 있나?"
    "그가 뱃삯을 바라며 검은 손을 내밀었다. 내가 금화 두 닢을 내려고 하자 뱃사공은 획 하고 금화를 낚아채 갔다."
    "금화라니, 기쁘구나."


    "이건 뭐지?"
    "아무것도 모른 체 앞으로 나아가던 나는 문득 이상한 점을 느꼈다."
    "시선이 느껴졌다. 굉장히 기분 나쁜 시선들."
    "정육면체의 물체에서는 그림이 계속 바뀌며 흥미를 유발하고 있었다."
    "뭐야, 텔레비전 몰라? 아, 그래. 지옥은 처음이었지."
    "간단히 말하자면, 미래의 물건이다. 지옥은 시간의 개념이 희박하지. 뒤틀려 있거든. 오늘 죽은 사람이나, 미래에 죽은 사람이나 모두 같은 공간에 있는 거다. 만들어지는 것도 비슷하지."
    "그렇군.."
    "그리고 너가 멍청하게 시련이다 뭐다 하는건"
    "전부 연극이다. 모든 것은 계획되어 유흥으로 쓰여지는 거야."
    "넌 지금 지옥 최고의 장난감이야! 하하하하하하!"


    "아, 벌써 하데스님께 향하는 첫번째 관문을 통과한 오르페우스! 역시 최강 최흉의 머저리군요! 투철한 사랑의 힘으로 어디까지 가는겁니까! 이런 멋진 날에는 인터뷰를 빼놓을 수 없겠죠. 그럼 바로 불러보도록 하겠습니다."
    "모르페우스가 손가락을 튕기자 무대가 회전하더니 게임을 막 통과해 기진맥진한 오르페우스가 보인다."
    "갑작스런 환경의 변화에 경계를 하듯 무기를 움켜쥐는 오르페우스." 
    "아아, 가여운 것. 아직도 이러고 있군요. 지옥 여러분, 에스카토스 시즌 666의 주인공 오르페우스에게 따뜻한 동정의 박수 부탁드립니다!"
    "괴물들의 비웃음, 박수, 야유"
    "…?"




    #레이트 나잇 쇼 
    "지옥에서 제일 멋진 빌딩!"
    "지옥에서 가장 재밌는 데빌TV!"
    "지옥에서 최고로 잔혹한 쇼! 에스카토스에서 보내드립니다!"
    "안녕하세요, 여러분의 꿈을 짓밟아주는 사랑의 지옥 버라이어티 쇼"
    "오늘의 메뉴는 '질투의 인터뷰', '음욕의 콘서트', 그리고 '나태의 버츄얼"
    "아들래미 하나 때문에 모든걸 빼앗기고 추락한 엄청난 바보가 나오구요"
    "3만년만의 신곡을 들고 나온 3인조와"
    "최초의 무언가! 이건 스포일러 금지라고 하네요"
    "환호"
    "모두들 감사합니다!"
    "에스카토스에 오신걸 환영해요"
    "에스카토스의 귀여운 미친 놈! 당신의 영원한 쇼 호스트 모르페우스 입니다❤"
    "저는 쇼 어시스턴트 '매곳'(구더기) 입니다"
    "이거 정말 멋진 관객이군요"
    "지옥에는 정말 최고의 관객분들만 모여있군요"
    "아 먼저 뉴스부터 "
    
    "그럼 첫번째 코너죠! 덜 멋진 게스트 분과 함께하는 최고로 멋진 인터뷰!"
    "질투의 인터뷰, 오늘의 게스트는.. "
    #게스트 목록: 헬리오스 인터뷰 하다가 아폴로 깜짝 출현 및 쌍방 디스전
    #케르 베 루스 신곡 콘서트
    #지옥 최초 버튜버 스킬라쨩과 버츄얼 방송
    
    "아아 이거 두 멍청이들을 보니 너무 분위기가 올라갔네요."
    "조금 쉬는 타임을 가져볼까요? 쉬어가는 뉴스! 뉴스 타임~"
    "아 모르페우스? 그런데 제가 먼저 후루룩 하고 읽어보았습니다만.."
    "상황이 너무 좋지 않습니다"#엄근진
    "전 세계적으로 결혼률이 급감했다는 소식입니다"
    "아니 매곳!, 도대체 왜 그렇죠?"
    "아, 여기 통계가 써있군요"
    "어디 줘 보세요. 3위가 어디보자.. 아 돈이 부족해서!"
    "(모르페우스 웃음소리)"
    "풉..  이건 좀 불쌍하네요. 돈 없어서 뒤졌을텐데 지옥에서도 돈이 없다니! 정말 잘~하는 짓입니다"
    "그런 당신을 위한 멋진 장소가 있습니다!" #도박시설 '골든 샤워 오브 미다스!' 금이 비처럼 떨어진다는 뜻이지만 "18금 뜻"도 맞음
    "그건 바로 황금빛으로 당신의 하트를 가득 매워줄 원더랜드!"
    "데빌TV 방송국 바로 옆건물에 위치한 꿈의 나라 '골든 샤워 오브 미다스'죠!"
    "모르페우스, 나 거기서 금화 3억개정도 잃은 것 같아요"
    "괜찮아 매곳, 나도 그래."
    "아! 그 어... 여러분은 저희 스택 빨아가시라는 소리죠! 하하하하!!"
    "그쵸그쵸 이번에 새로운 기기도 들여왔다면서요?"
    "아, 지상에서는 꽤나 롱런하고 있는 제품이라고 하더군요"
    "어디보자.. 기기명이 '빠칭코'군요"
    "설명서에는 이렇게 써있군요"
    "'원하는 만큼 금화를 넣고 레버를 당기세요'"
    "그게 다에요?"
    "네 매곳, 그게 답니다"
    "쓰래기같네요"
    "만들기 제일 쉬운걸로 들고와서 그래요 뭐라하지 말아요"
    "아아 잠시 다른 이야기로 세어버렸네요! '골든 샤워 오브 미다스'! 많은 관심 부탁드립니다."
    "이제 2위로 넘어가죠"
    "2위가 결혼을 안해도 XX만 하면 그만이야"
    "와 모르페우스, 다들 쓰래기네요?"
    "뭐 그다지 틀린 말도 아니죠, 매곳. 어차피 결혼이라는건 얽매이는거니까요. 우리가 만들어진대로 번식에 목적을 둔다면 결혼같은건 필요 없어요"
    "그렇죠."
    "물론 월 3천도 못버는 베타메일들은 다 죽어버리지만요"
    "하하하! 굉장히 웃겼어요 모르페우스. 방금 발언으로 이 게임 끄는 사람도 있겠는걸요?"
    "걱정 말아요 매곳, 여기 두 시간 구간이어서 환불도 못해요."
    "아, 다 계획된거군요?"
    "이 게임, 아니 방송에 계획이 안된게 없습니다"
    "오오.."
    "이제 대망의 1위만을 남겨놓고 있는데요"
    "이건..."
    "광고 보고 오시죠!"

    "'골든 샤워 오브 미다스'"
    "황금의 나라로 오세요~ 황홀한 금화 쏟아지는 곳!"
    "황천의 나라로 오세요~ 끝없는 나락의 나라 '골든 샤워 오브 미다스'!"

    

    "그리고 대망의 1위가 결혼을 안해도 행복감을 느낄 수 있는 분야가 늘어나서"




