# 이 파일에 게임 스크립트를 입력합니다.

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
    "아 먼저 뉴스부터 듣고 오시죠"
    "매곳, 오늘 중요한 뉴스는 뭐가 있죠?"
    "몇가지 있긴 한데 가장 중요한건 이거네요"
    "어디보자.. 저런! 제 666회 에스카토스의 히어로 오르페우스가 아직도 첫번째 경기 통과를 못했다고 합니다"
    "와이프 별로 안사랑하나 본데요?"
    "그러게요. 솔직히 이제와서지만 별로 중요하지도 않은 것 같아요."
    "아니 모르페우스, 이번 주인공 쟤라면서요"
    "매곳, 솔직히 에스카토스건 뭐건 시청률만 올라가면 그만이에요"
    "오, 반박할 수 없네요"
    "그리고 요즘 트렌드는 짧고 굵게 재밌는거죠!"
    "금방금방 넘어가야 질리지 않으니까요"
    "그럼 첫번째 코너죠! 조금 덜 멋진 게스트 분의 부끄러운 과거사와 함께하는 최고로 멋진 인터뷰!"
    "질투의 인터뷰! 오늘의 게스트는.. "
    #게스트 목록: 헬리오스 인터뷰 하다가 아폴로 깜짝 출현 및 쌍방 디스전
    #케르 베 루스 신곡 콘서트
    #지옥 최초 버튜버 스킬라쨩과 버츄얼 방송
    "밝은 미래의 상징이자 뜨거운 심장의 소유자!"
    "태양 마차로 우리 지옥은 못비추고 지상만 비춰줬죠!"
    "그러니까 나락으로 떨어진겁니다!"
    "이거 다~ 업보에요!"
    "소개합니다! 헬~리오스!"

    "하, 정말 저급한 설명뿐이군"
    "이봐 가짜, 어디까지 입을 놀릴 셈이냐"
    "네놈, 그러고도 올림포스가 너를 용서할 것 같더냐"
    "아아~ 우리 '전직' 태양신님께서, 마차에서 떨어지셔서 머리를 크~게 다치신 것 같습니다!"
    "여기가 어디?"
    "관객: 지옥!"
    "누구의 지옥?"
    "하데스님!"
    "그렇죠, 이곳은 영원한 죽음의 신 하데스님의 신역. 올림포스의 그 누구도 간섭할 수 없습니다"
    "힘을 빼앗겨서 별 것도 아니게된 당신은 더더욱. 캬캬캬캬캬컄"
    "뭐 발끈하지 마시고 앉으시죠, 헬리오스. 과거는 오락이에요. 그 추억을 되감으면서 한 번 재밌게 웃을 수 있다면"
    "그걸로 충분하지 않을까요?"
    "아, 미안해요 네 과거는 우리만 재밌죠"
    "넌 재미 없죠 캬캬캬캬컄"
    "이곳을 불바다로 만들어주마, 모르페우스"
    "엥?"
    "이미 불바다인데 무슨 소리신지.. 공격을 하시려면 좀 더 맛있는 걸로 부탁드립니다. 별거 없으니까 시청률 떨어지잖아요"
    "(떨어지는 실시간 시청자 수를 보여주며)"
    "아무튼, 스몰토크는 이 정도로 하고 인터뷰 진행해보도록 하겠습니다"

    "모두 모르셨겠지만 저희가 괜히 헬리오스님을 모신게 아닙니다"
    "에스카토스의 주인공은 오르페우스만 있는게 아니죠!"
    "더블 주인공 캬~ 이거죠"
    "오늘 우리는 헬리오스님에 대해서 조금 더 알아보는 시간을 가져보려고 합니다"
    "그러려면! 즐거운 게임 한번 하는게 좋겠죠?"
    "그래서 준비했습니다! 레이스 오브 러브❤"
    "레이스 오브 러브! 1대1로 레이스를 펼쳐 사랑을 쟁취하면 되는 쉬운 게임인데요"
    "헬리오스님?"
    "뭐냐, 천박한 것의 아이야"
    "호오, 최초의 태양은 역시 모든 것을 꿰뚫어 보는군요. 아주 멋집니다!"
    "본론을 말하거라."
    "그러죠! 소개합니다! 석양을 죽일 눈부신 아침 햇살! 아폴론님 이십니다!"
    "짐은 태양이니라!"
    "정말 오만하기 짝이 없군요, 헬리오스님, 어떻게 생각하십니까?"
    "올림포스의 이름에 먹칠을 하는군"
    "누구인가? 잘 보이지도 않는구나. 성냥 한개비가 그대보다 밝겠구나. 어리석은 것. 가서 아들래미 기저귀나 갈아주고 오거라"
    "오만방자한 것, 뒤로 여색이나 밝히는 더러운 것이 태양신이라니, 이제 진실은 전부 썩어 문드러졌구나"
    "워워, 두 분 진정하시고~ 싸움은 레이스에서 보여주시면 되죠!"
    "아, 그래서 아폴론님은 왜 여기 오신거죠?"
    "이번에 신곡 내는 걔네 있잖아요"
    "아 개세마리요?"
    "매곳, 그래도 멋있게 3DOGS 라고 해주세요"
    "그게 그 말이잖아요"
    "... 어쨌든! 심사위원으로 초청했더니 흔쾌히 와주셨습니다! 감사합니다, 아폴론님!"
    "썩어도 태초의 아이라더니, 지옥도 나름 활기차고 좋구나."
    "네, 그러면 게임 시작해볼까요? 레이스~ 스타트!"
    #레이스 오브 러브 - 태양마차를 타고 사랑하는 사람에게 먼저 도달하자! 지면 사랑하는 사람은 지옥 끝으로 떨어져요~ 
    #ZX 연타를 통해 스피드 업! 스페이스바로 점프! 누구보다도 빠르게 결승선에 도달하자!

    "아폴론님, 생각해보니 오르페우스가 아폴론님 아드님이셨네요."
    "어리석은 나의 아이 말이로구나"
    "그래도 아폴론님을 쏙 빼닮아서 "



    
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
    "쓰레기같네요"
    "만들기 제일 쉬운걸로 들고와서 그래요 뭐라하지 말아요"
    "아아 잠시 다른 이야기로 세어버렸네요! '골든 샤워 오브 미다스'! 많은 관심 부탁드립니다."
    "이제 2위로 넘어가죠"
    "2위가 결혼을 안해도 XX만 하면 그만이야"
    "와 모르페우스, 다들 쓰레기네요?"
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



    "그리고 대망의 1위가 데빌티비를 보면 딱히 생각 안들어서"
    "캬, 역시 지옥 최고의 엔터테인먼트!"
    "아, 모르페우스 이거 그건데요?"
    "뭐죠 매곳?"
    "행복감을 느끼는 분야"





"From studio  b

                   
in rockefeller center,

                   
the national broadcasting

                   
company presents...

                   
tonight's guests are...

                   
and featuring
the legendary roots crew.

                   
And here he is...

                   
Jimmy Fallon!

                   
 

                   
 

                  
Thank you, everybody!

                   
Welcome to the show.

                   
Thank you for being here!

                   
That is a great crowd.

                   
New York City has the best

                   
crowds.

                  
Welcome.

                   
Thank you.

                  
Welcome to  late night with

                    
Jimmy Fallon,  everybody.

                     
Let's get right to the news

                     
here.

                     
I read this.

                     
This is not good.

                     
I read that some teenagers are

                     
getting pregnant on purpose so

                     
they can audition for MTV's show

                     
    and pregnant. 

                     
Isn't that unbelievable?

                     
Not only that, I heard that some

                     
adults are running for president

                     
on purpose so they can audition

                     
for a show about killing moose.

                     
I read about this.

                     
Hey, this is huge.

                     
President Obama has reached a

                    
deal with Republicans to extend

                     
the bush tax cuts in exchange

                     
for extending jobless benefits.

                     
The Republicans in congress say

                     
they're thrilled with the tax

                     
cuts, while democrats leaving

                    
congress say they're thrilled

                     
with the jobless benefits.

                     
That's just the way it works

                     
out.

                     
I'm not sure what to think of

                     
this.

                     
A new study found that one-third

                     
of men between the ages of

                     
   and    are still sexually

                     
active.

                     
The survey had two boxes...

                     
 yes  and  please say no. 

                     
Just, come on, you know.

                     
Check this out.

                   
A woman in the u.K. Called

                     
police to report someone stole

                     
her snowman.

                     
Police have released this sketch

                     
of the suspect.

                     
This is pretty crazy.

                     
A man in Canada just moved out

                     
of his college dorm after living

                     
there for    years.

                     
You could tell he was getting

                     
old.

                     
When he puts a sock on the

                     
doorknob, that means he's

                     
getting a prostate exam.

                     
 Don't bother me, eh. 

                     
Get me some Mac and cheese.

                     
 Shut the door. 

                     
I just saw this.

                     
A woman in California just

                     
published a medical marijuana

                     
cookbook.

                     
Yeah.

                     
'Cause if there's one thing

                     
stoners are great at, it's

                     
following directions.

                     
Step one.

                     
Melt butter.

                     
Melt, melt... tuna melt.

                    
Maybe we should get some tuna

                     
melts and just smoke this pot

                     
and eat tuna melts.

                     
Bake at    .

                     
Very nice.

                     
Bake at     for    minutes?

                     
Yeah.

                     
Hey, the department of

                     
homeland security is bringing

                     
the  if you see something, say

                     
something  campaign to Walmart,

                     
reminding shoppers to report

                     
suspicious activity.

                     
I'm sorry, you want me to notice

                     
if there's any suspicious

                     
activity at a Walmart?

                    
You mean the place where I can

                     
go to one aisle and get a rifle,

                     
an iPod and some sunny  d ?

                     
Yeah, I'll let you know if

                     
there's anything weird happening

                    
there.

                     
Anything's possible.

                     
Yeah, I'll let you know.

                     
Nothing weird.

                     
Get this.

                    
Justin Bieber said that his mom

                     
recently canceled his cell phone

                     
plan after they had an argument.

                     
Yeah, his mom was like,  Justin,

                     
you will follow my rules as long

                     
 as I'm living under your roof. 

                     
You...

                     
Hey, police in London are

                     
looking for thieves who stole a

                     
$  million stradivarius violin

                     
from a musician while she was

                     
eating a sandwich.

                     
When asked to describe it, the

                     
woman was like,  I don't know,

                     
turkey, mayo, some tomatoes. 

                     
 Why does that matter? 

                     
That one's for Frank Drebin.

                     
Yeah.

                     
He would have liked that joke.

                     
And finally, I don't know if you

                     
saw this.

                    
A Chinese passenger train just

                     
broke a record by hitting

                     
    miles per hour.

                     
Yeah, passengers called it a

                     
thrilling experience, while the

                     
guy in the bathroom called it

                     
the worst day of my life.

                     
Ladies and gentlemen, we have a

                     
great show!

                     
Give it up for the roots!

                     
♪

                     
♪ I don't remember

                     
what time it is

                     
I can't remember

                    
what day it was ♪

                     
♪ all I know is that

                     
I fell in love with you

                     
and if all my dreams

                     
come true ♪

                     
♪ I'll be spending

                     
time with you ♪

                     
♪

                    
Hey!

                     
That's new Orleans trumpeter

                     
Kermit Ruffins sitting in with

                     
the roots tonight.

                     
You may have seen Kermit playing

                     
himself on the hit hbo series

                     
 Treme. 

                     
Here's his new album,  happy

                     
talk. 

                     
Thanks for being here, Kermit.

                     
I appreciate it, buddy.

                    
Oh, thank you, man.

                     
Looking good, buddy.

                     
Looking good.

                     
That sounded great.

                     
We've got something over here

                     
too, as well.

                    
Look at this.

                     
It's the new issue of  rolling

                     
stone  magazine, right here, the

                     
playlist issue.

                    
Just came out.

                     
It's called the playlist issue,

                     
and right there in the inside,

                     
it's our very own questlove.

                     
There he is right there.

                     
Are you sleeping?

                     
What are you doing?

                     
Are you taking a nap?

                     
I think I'm sort

                    
of vibing out.

                     
You're vibing out.

                     
 Rolling stone  credits

                     
questlove with the idea for this

                     
issue.

                     
What is the playlist issue?

                     
You know,  rolling

                     
stone  is always asking, like,

                     
for your top ten favorite songs

                     
or whatever.

                     
And I told them, like,  why

                     
don't you do, like, the real

                     
 list? 

                     
You know, not just name all the

                    
Bob Dylan hits, but all the

                     
stuff that really defines an

                     
artist.

                     
So, they made that issue.

                     
That was awesome.

                    
And you got a lot of records,

                     
man.

                     
This was is in Philly, right?

                     
  ,  .

                     
  ,   records.

                     
That's why we

                     
haven't moved to New York just

                     
yet.

                     
You've got to wait...

                     
you got to wait... exactly.

                     
Well, congrats on this, man.

                     
Pick up this issue.

                     
It's a really cool issue.

                     
 Rolling stone. 

                     
Good man, quest.

                     
You're a good man.

                     
We've got a fantastic show

                     
tonight, you guys.

                     
A very talented actor from the

                     
hit show  Dexter, 

                     
Michael c. Hall is here!

                     
Love  Dexter. 

                     
From the popular show

                    
 cougar town,  the lovely

                     
Busy Philipps is joining us!

                     
She's super nice.

                     
And oh, my God, did this guy

                     
kick ass last night!

                     
Can I say that even?

                     
Oh, sorry.

                     
This guy was unbelievable.

                     
R. Kelly is back to perform

                     
another song.

                     
He was so good.

                     
He's got a record out called

                     
 love letter. 

                     
Last night it was just... it was

                     
almost like it was something out

                    
of the '  s, early '  s,

                     
something like that.

                     
Wouldn't you say?

                     
Sam Cooke.

                     
He was doing his inner Sam Cooke

                     
thing.

                     
Sam Cooke.

                     
Oh, my gosh, it was just

                     
absolutely mind-blowing,

                     
standing ovation.

                     
Man, I'm just so happy he's

                     
here.

                     
And he's going to kick butt

                     
again tonight.

                     
You guys, we pride ourselves on

                     
being a positive show here,

                     
always looking on the bright

                     
side of things.

                     
But of course, there's two sides

                     
to every story.

                     
So tonight, we'll take a look at

                     
those stories making issues,

                     
headlines today in the papers...

                     
whatever this says.

                     
And we're going to weigh the

                     
good with the bad in a segment

                     
we call  pros and cons. 

                     
There it is.

                     
Headlining any issue,

                     
any issue of  rolling stone. 

                     
Anything, headlines, issues,

                     
everything.

                     
It's great.

                     
 Pros and cons. 

                     
 Pros and cons. 

                     
Tonight's  pros and

                     
cons  topic is being a mall

                     
Santa.

                     
A lot of parents... a lot of

                     
parents are taking their kids to

                     
see Santa at the mall right now.

                     
It's a big part of Christmas.

                    
So let's take a look at the pros

                     
and cons of being a mall Santa.

                     
Here we go.

                    
Pro... you get to wear a cool

                     
red suit.

                     
Con... it still smells like the

                     
dude who wore it last year.

                     
Yeah, that's not good.

                     
That's not good.

                     
Pro... being a mall Santa is a

                     
big responsibility.

                     
Con... this time last year, you

                     
were a vice president at

                     
citibank.

                     
Pro... you'll get hired if you

                     
work hard.

                     
Con... you'll get fired if you

                     
work  hard. 

                     
What does that mean?

                    
I don't know.

                     
Is that what the sound effect

                     
was for?

                     
You're fired.

                     
Pro... the warm

                     
feeling of kids snuggled on your

                     
lap.

                     
Con... the warm feeling of kids

                     
peeing down your leg.

                     
That's what Christmas is all

                     
about, isn't it?

                     
 $  an hour for this? 

                     
Pro... you get to hear kids ask

                     
where your reindeer are.

                     
Con... you'll have to explain

                     
that Sarah Palin shot them all.

                     
Why would you do that?

                     
You don't have to do that.

                     
You don't have to.

                     
Pro... your cheeks are

                     
like roses, your nose like a

                    
cherry.

                     
Con... you're drunk.

                     
You are...

                     
 Santa's got to get another four

                     
loko. 

                     
Pro... you get to work near

                     
frosty the snowman.

                     
Con... that's the name of the

                     
guy who deals cocaine by the

                     
dippin' dots stand.

                     
He's not a good

                     
fellow.

                     
Dippin' dots, the

                     
future of ice cream.

                     
Or  the ice cream of the

                     
future. 

                     
Yeah, yeah.

                     
Unless you're dealing with

                     
frosty.

                     
It's both, I guess,

                     
yeah.

                     
Pro... before your break, they

                     
put up a sign that says,  gone

                     
to feed the reindeer. 

                     
Con... after you've left, they

                     
put up another sign that says,

                     
 if you know what I mean. 

                    
What does that mean?

                     
I don't know what you

                     
mean.

                     
I don't know what it

                     
means, either.

                     
And finally, pro... ho, ho, ho.

                     
Con... that's Charlie sheen's

                     
Christmas list.

                     
There you go!

                     
That's the  pros and cons, 

                    
everybody.

                     
We'll be right back with more

                     
 late night! 

                     
Welcome back.

                     
Sounding good, buddy.

                     
Welcome back.

                     
It's time to announce this

                     
week's  late night  hashtag, you

                     
guys.

                     
Today I went on Twitter and I

                     
started a hashtag called  keep

                     
your pants on. 

                     
For example, I tweeted out,

                     
 waiter at outback keeps asking 

                     
if I'm still working.

                     
I've got half a bloomin' onion

                     
left.

                     
 Keep your pants on! 

                     
So, this is where you guys come

                     
in.

                     
Go on Twitter.

                     
Tweet out something that makes

                     
someone want to tell someone,

                     
 hey, relax, keep your pants on,

                     
buddy. 

                     
Be sure to include the hashtag

                     
 keep your pants on. 

                     
I'll look at all of them and put

                     
some of my favorites on the show

                     
tomorrow night.

                     
So tune in.

                     
You might want to see your

                     
tweets on the show tomorrow

                     
night.

                    
It'll be fun.

                     
Hey, everybody, is that right?

                     
It's time once again to play

                     
 competitive spit takes. 

                     
Here we go!

                     
♪

                     
Welcome to

                     
 competitive spit takes,  the

                     
game where we get audience

                     
members to tell a punch line to

                     
a joke, and their friends

                     
respond by spraying them with a

                     
mist of Luke-warm backwash.

                    
And then you, the audience,

                     
votes on which team performs the

                     
best.

                    
Let's meet our first pair of

                     
audience volunteers.

                     
Come on up.

                     
Nice to see you, pal.

                     
What are your names?

                     
Peter.

                     
Peter?

                     
Andres.

                     
Andres?

                    
Andres.

                     
Peter and Andres, how

                    
do you know each other?

                     
High School.

                     
Oh, yeah?

                     
Yeah.

                     
You go there now?

                     
No, we graduated.

                     
You graduated.

                     
Okay, yeah.

                     
So you've been friends for a

                     
while.

                     
Yes.

                     
Okay, good.

                    
And you realize that one of you

                     
will be spitting and the other

                     
person will be receiving?

                     
Yeah.

                     
Okay, good.

                     
All right.

                     
It still has not been decided

                     
who will be doing what.

                   
Does that make you nervous?

                     
No, not at all.

                     
It makes me nervous.

                     
Let's see.

                     
You guys know what a spit take

                     
is, right?

                     
Yeah.

                     
This is when someone

                     
tells something shocking or

                     
funny while you're drinking

                     
water and you...

                     
You spit it out.

                     
All right?

                     
And let's find out who will be

                     
doing the spitting and who will

                     
be doing the taking.

                     
Let's bring out the die.

                     
Here we go right here... look at

                     
this.

                     
All right.

                     
Beautiful die, says

                     
 spit  on three sides,  take  on

                     
the other sides.

                     
I need a representative from the

                     
team to roll the die to see who

                    
will be doing what.

                     
My calling.

                     
It's your calling?

                     
Oh, you're doing the spit!

                     
Very good!

                    
♪

                     
That's good.

                     
No, that's a good thing.

                     
That's a good thing, yeah.

                     
So you'll be standing over here.

                     
You're over here.

                     
I like your sneakers.

                     
Thank you, thank you.

                     
Gilligan called.

                     
Here you go.

                     
I got this water for you right

                     
here.

                     
And here's your joke.

                     
He didn't leave a message, by

                     
the way.

                     
Audience, please keep in mind

                     
that you will be voting on both

                    
the delivery of the punch line

                    
and the spit take as well.

                     
So...

                     
go take a large sip of that

                     
water there, as much as you can.

                     
Go for it.

                     
More.

                     
Come on, you can do it.

                     
You can fit more in there.

                     
Yeah, yeah, that's what I'm

                     
talking about.

                     
All right.

                     
There you go.

                     
Wait until you hear the full

                    
punch line, please.

                     
Are you ready?

                     
Deliver your punch line.

                     
Deck the halls?

                     
I thought you said inspect my

                     
balls.

                     
♪

                     
Very nice.

                     
It's all right.

                     
Nicely done.

                     
Are you okay?

                     
I'm fine.

                     
All right, very good.

                     
What did you think he said?

                     
No, don't... never mind.

                     
Hey, let's take a look at that

                     
one more time in slow motion,

                     
you guys.

                     
Whoa!

                     
Yes.

                     
Very, very nice.

                     
Thank you very much for playing.

                   
Let's bring in our next

                    
contestants.

                     
All right.

                     
See you guys soon.

                     
Come on over, buddy.

                     
How you doing?

                    
How are you doing,

                     
man?

                     
What are your names?

                     
My name's Brian.

                     
Brian.

                     
My name's Ares.

                     
Erics?

                     
Ares.

                     
Oh, Ares.

                     
I thought it was Eric, plural.

                     
No.

                     
I was like, Erics?

                     
All right, Brian and Ares, how

                     
long have you guys known each

                     
other?

                     
Since we were kids.

                     
Oh, yeah?

                     
Yeah.

                     
Friends since kids.

                     
Grew up together?

                     
Yeah.

                     
We went to, like, church

                     
camps and went to... yeah.

                     
Now, did they ever

                    
play this type of game in church

                     
camps?

                     
I'm not going to say I'm the

                     
best spitter in here, 'cause

                     
that's Mr. black thought, but

                     
I'm... I'm pretty good.

                     
Oh, very good, very

                     
good, man.

                     
I'm pretty good.

                     
A little hip hop

                     
reference there.

                     
I get that.

                     
Hey, all right, so here's the

                     
deal.

                     
Let's find out who will be doing

                     
the spitting, who will be doing

                     
the taking.

                     
Bring the die in, please.

                     
All right, here we go.

                     
Very, very good.

                     
Big fan of Pixar, huh?

                     
Yeah.

                     
Which one's your

                     
favorite one?

                     
 Toy story   ?

                     
Oh, I agree.

                    
Even surprised yourself there,

                     
yes?

                    
You did it, buddy, you said it.

                     
That's good.

                     
You got it out.

                     
You finally got it out.

                     
We knew you could do it, buddy!

                     
I love that movie.

                     
Is that Stan Lee?

                     
Very, very nice.

                     
Stan Lee, the greatest

                     
American.

                     
We know Stan Lee.

                     
Absolutely lovely.

                     
Here we go.

                     
I need you... one of you guys to

                     
roll this die.

                    
I'm assuming that's you?

                     
Yes, sir.

                     
All right, do it.

                     
All right, look, I've been

                     
through this many times.

                     
Neither of you are on steroids,

                    
are you?

                     
We have to ask.

                    
All right, maybe you should do

                     
the rolling this time, okay,

                     
Mr.  toy story  . 

                     
Here we go.

                     
Come on, buddy, give it a good

                     
roll.

                     
Keep it on the board.

                     
Oh, there you go!

                     
♪

                     
That's what you got.

                     
That's good news, see?

                     
Good luck.

                     
Sorry, buddy.

                     
It's all right.

                     
All right, let's do

                     
this.

                     
Here is your punch line, and

                     
here is your water.

                     
Take a good gulp there, buddy.

                     
And get your punch line ready to

                     
go.

                     
Wait till he's filled with

                     
water.

                     
You got enough in there?

                     
Yeah, yeah, you can fit.

                    
There you go.

                     
That's good right there.

                     
It's leaking.

                     
He's leaking.

                     
He's leaking.

                     
All right, stop it.

                     
Don't... what are you doing?

                     
All right.

                     
Stop it.

                     
All right.

                     
The eight days of hanukkah?

                    
I thought you said I ate Dave's

                     
yarmulke!

                     
♪

                     
Wow.

                     
That was one of the best ones

                    
I've ever seen.

                     
I thought you were ready to

                     
explode before it even happened.

                     
And your mouth was open the

                     
whole time.

                     
Let's look at that in slow

                     
motion, if you want to.

                     
♪

                     
Whoa!

                    
Is that true?

                    
Whoa!

                     
Is that true?

                     
We have time for one more.

                     
All right.

                     
Let's switch it up.

                     
Thank you so much.

                     
Payback is so fantastic.

                     
Yeah.

                     
Yeah, yeah, this is

                    
very, very good.

                     
Here you go.

                     
Here you go.

                     
Take a good gulp.

                     
There you go.

                     
Man, oh, man.

                     
He's got half the glass of water

                     
in there.

                     
All right.

                     
Whenever you're ready, say the

                    
punch line.

                     
I saw mommy kissing Santa

                     
claus?

                     
I thought you said I saw daddy

                     
kissing Santa claus!

                     
♪

                     
What happened at the

                     
end?

                     
I got really excited, Jimmy.

                     
Let's see that in slow

                     
motion.

                     
You really got him.

                     
That's terrible.

                     
♪

                     
Very good.

                     
Very, very good.

                     
It was that last burst of water.

                     
It wasn't... very interesting

                     
how you kept that in your mouth

                    
that whole time.

                     
It's something I do well.

                     
Yes, very good.

                     
Truly amazing.

                     
Step in.

                     
Team number one, we missed you

                     
guys.

                     
Come on over.

                     
Time for the audience to choose

                     
who did it best.

                     
Was it team number one?

                     
Or was it team number two?

                     
Team number two is the winner!

                     
♪

                     
You win a set of  late night

                     
with Jimmy Fallon  towels so you

                     
can dry off in style.

                     
There you go right there.

                     
Congratulations.

                    
And since no one goes home empty

                     
handed, for the losers, we have

                     
 late night with Jimmy Fallon 

                     
moist towelettes.

                    
There you go.

                     
Thank you so much, you guys.

                     
Thanks for playing.

                     
That's it for  competitive spit

                    
takes. 

                     
We'll be right back with

                     
Michael c. Hall.

                     
Come on!

                     
Welcome back,

                     
everybody!

                     
That was great.

                     
Our first guest is an

                     
emmy-nominated, golden globe and

                     
s.A.G. Award-winning actor for

                     
his title role in critically the

                     
acclaimed showtime series

                    
 Dexter,  which has its fifth

                     
season finale this Sunday night.

                     
Say hello to Michael c. Hall!

                     
♪

                     
There you are.

                     
Wow!

                     
I think they like you.

                     
We enjoy your presence.

                     
Yeah.

                     
We enjoy you here.

                     
Michael c. Hall,  Dexter. 

                     
Gosh, you play a creepy,

                     
awesome, great... killer in the

                     
show.

                     
Thank you.

                     
You're fantastic at

                     
it.

                     
Yeah, it's fun.

                     
I mean, who would have thunk it,

                     
you know?

                     
We made the pilot episode and

                     
thought maybe a few people would

                     
be interested, but it's like,

                     
yeah.

                     
Worldwide.

                     
Fifth season.

                    
How did this show come about?

                     
Who pitched this show?

                     
Like,  I have an idea for a

                     
serial killer who just kills

                     
 other serial killers. 

                     
Well, it's based on a book.

                     
The first season is based on a

                     
book.

                     
Okay.

                     
A book... the rights of which

                    
was purchased by independent

                    
producers who took it to

                     
showtime and Bob Greenblatt.

                     
And it was the first thing he

                     
really pushed for as head of

                    
original programming at

                     
showtime.

                     
'Cause you're a cop...

                     
right.

                     
But also, you murder

                     
people.

                     
If you haven't seen the show, he

                     
murders people.

                     
Bad people.

                     
Bad people.

                    
Whoever's bad, he just murders

                     
them.

                     
Yeah.

                     
It's like case... case

                     
closed.

                     
It's fantastic.

                     
It's cathartic, you know?

                     
People say,  does it creep you

                     
out when you do those scenes? 

                     
And actually, those are the

                     
scenes where I really leave

                     
just, you know, like walking on

                    
air.

                     
It's...

                     
Really?

                     
Yeah, it's nice to be able to

                     
go to work and...

                     
Well, let's go to

                     
commercial, and then we'll be

                     
back...

                     
no.

                    
But thought of the saran

                     
wrapping?

                     
That, I mean, a lot of that

                     
is taken from the book.

                    
As far as the specifics, we kind

                    
of fine tuned it and tweaked it

                     
and perfected it.

                     
And early on, I would be on set

                     
and, you know, in terms of where

                     
he'd put up the pictures and

                     
just how he'd strap people down.

                     
We figured that all out.

                     
It's insane.

                     
Did you ever think

                     
that you'd be playing a

                     
character this dark?

                     
I mean, you came... did you come

                     
from musical theater or...

                     
I did, I did.

                     
I did a lot of musicals here in

                     
New York.

                     
Why aren't you on

                     
 glee ?

                     
I mean, why are you doing this?

                     
It's timing.

                     
I mean, you know, I'm open to

                     
that.

                     
Yeah, exactly.

                     
You could be, like, a new

                     
teacher or something.

                     
I think maybe next season

                     
we're going to do an all-musical

                     
episode of  Dexter. 

                     
You are not.

                     
No.

                    
You are not.

                     
No.

                     
Because  six feet

                     
under  was kind of dark as well.

                     
It was.

                     
I mean, yeah, in one way or

                     
another, I have managed to be

                     
surrounded by dead bodies...

                     
Yeah.

                    
Whether embalming them or

                     
making them...

                    
You're like...

                     
♪ I can sing ♪

                     
Yeah... I don't know.

                     
That didn't help

                     
anything, yeah.

                     
No.

                     
The season finale coming up.

                     
Yeah.

                     
I've got to say, with

                     
the way  Dexter  works is,

                     
you... oh, man.

                     
If you haven't seen this show,

                     
you've got get it on DVD, and

                     
you watch the whole thing.

                    
You don't know what's going to

                   
happen.

                     
The season finale is always a

                     
shocker.

                     
Right.

                     
And last season, oh,

                     
man, this is one of the best...

                     
I mean, John Lithgow was off the

                     
charts.

                     
Yes, he's insanely good.

                     
He was so great.

                    
Oh, man, you were both insane.

                     
It's like watching two great

                     
tennis people play tennis.

                     
They call them tennis people,

                     
right?

                     
Tennis... yeah.

                     
Tennis people?

                     
Players.

                     
Or players.

                     
Tennis people.

                     
People is good.

                     
Yeah... players.

                     
It was amazing.

                     
And then right before the finale

                     
aired...

                     
I didn't see it.

                     
I had it on TiVo.

                     
I came into work and my second

                     
producer Lepis comes in and he

                     
goes,  oh, my God, I can't

                     
believe it was so great. 

                     
And he says what happened.

                     
Spoiled it entirely for you.

                     
That ruined my month.

                     
Yeah.

                     
I didn't... to this

                     
day, I haven't watched it.

                     
You still haven't watched it?

                     
I'm upset about the

                     
whole thing.

                     
You're kidding.

                     
Yeah.

                     
I have it... I have it still on

                     
my TiVo.

                     
I think if you watched it, by

                     
the time you get to the end,

                     
you'll be so engrossed that

                     
you'll have forgotten that you

                     
know what's going to happen.

                     
I can't ruin it for

                     
anyone, but that was... I'm

                     
shocked from hearing what

                     
happened.

                     
Yeah.

                     
It was the most

                     
shocking...

                     
jaw-dropping.

                     
Jimmy ... Happenings on tv.

                     
Yeah, no, people were

                     
literally grabbing me by the

                     
shoulder...

                     
You murdered Sam and

                     
Diane.

                     
Yeah.

                     
No, I'm just kidding.

                     
A little  cheers  reference.

                     
Yeah.

                     
This season finale's

                     
got another shocker.

                     
Can you give us little hints and

                     
tricks into what's happening in

                     
this season finale?

                     
Someone will die.

                     
There you go!

                     
Yes.

                     
There you go.

                     
You guarantee it.

                     
I guarantee it.

                     
People will pay good

                     
money for that.

                     
Yeah.

                     
You have good guest

                     
stars on the show.

                     
Yeah.

                     
This year you have

                     
Julia stiles.

                     
Julia stiles.

                     
I love her.

                     
She's a great.

                     
She's gorgeous and a

                     
great actor.

                     
And Johnny Lee Miller.

                     
Johnny Lee Miller.

                     
I think that Johnny Lee Miller

                     
is probably going to die.

                     
I can't tell you.

                     
Well, that's what

                     
you're hoping.

                     
You're hoping...

                     
Peter weller is on the show

                     
this year.

                     
Peter weller... yeah,

                     
 Robocop. 

                     
Absolutely.

                     
We all know you can't

                     
kill  Robocop. 

                     
Well...

                     
He's half robot.

                     
Yeah.

                     
That's a hint?

                     
You can kill the human part.

                     
You can kill the human

                     
part.

                     
Not the  Robocop  part.

                    
Yeah, his right arm... still.

                     
We do have a clip of

                     
the finale.

                     
Would you like to set it up?

                    
I think I'm driving in a car,

                    
as is Johnny Lee Miller, and

                     
we're having a heated exchange.

                     
That's not very specific.

                     
Here's a hint.

                     
All right, let's look.

                     
Here's  Dexter, 

                     
Michael c. Hall.

                     
She really means a lot to

                    
you,

                     
doesn't she?

                     
Yes.

                     
Must be terrible going

                     
through this again.

                     
Losing your wife, the woman you

                     
loved, and now lumen.

                     
I imagine it seems to you like

                     
some kind of terrible curse.

                     
Think whatever you want.

                    
Just listen to me.

                     
I'll turn myself over to you.

                     
I appreciate the offer, but

                     
I'm afraid I must decline.

                     
Then tell me what you want!

                     
I have what I want.

                     
And the longer I stay on the

                    
phone, the better your chances

                     
of finding me.

                     
So this conversation's over.

                     
Jordan...

                    
tick, tick, tick, Dexter.

                     
That's the sound of Lumen's

                     
life running out.

                    
Ooh!

                     
Wow.

                     
I think he's going to

                     
get saran wrapped, myself.

                     
Yeah.

                     
Jordan should be careful.

                     
Here we go.

                     
That's what I'm talking about.

                     
More with Michael c. Hall when

                     
we come back, you guys.

                     
♪

                     
We're back with

                     
Michael c. Hall from  Dexter 

                     
right here.

                     
I have a great picture of you

                     
here.

                     
Is this from next season of

                     
 Dexter ?

                     
What is this?

                     
Holy moly!

                     
There you go, there.

                     
Hey!

                     
This is you in  cabaret ?

                     
Yeah, I played the emcee in

                     
 cabaret  on Broadway about

                     
  ,    years ago.

                     
Yeah, my God, this

                     
is...

                    
and you did an amazing job.

                     
Thank you.

                     
Did mom and dad come

                     
see this?

                    
Mom came.

                     
Mom came, and I didn't have a

                     
chance to warn her about...

                     
About the glittery

                     
nipples?

                     
About what she was gonna

                     
see.

                     
The first act ended with me

                     
revealing my ass in a pin spot

                     
to the audience, and I had a

                    
swastika painted on it.

                     
She was horrified.

                     
 My dreams have come

                     
true! 

                     
Yeah, yeah.

                     
So it's all been kind of been

                    
downhill from there.

                    
There's been shocking things

                     
she's seen since, but she

                     
doesn't have to be in the room

                     
now.

                     
Yeah, yeah.

                     
Now she's like,  you're a great

                     
serial killer.

                     
 This is fantastic! 

                    
Yeah.

                     
Yeah, in fact, my family... you

                     
know, I was doing  six feet

                     
under  and I was playing a gay

                     
character, and I, you know, had

                     
some love scenes that I did on

                     
that show.

                     
I would go home and they'd be

                     
like,  yeah, we've seen the

                     
show.

                     
We've seen the show.

                     
 It's good, it's good. 

                     
And I got home after doing

                     
 Dexter  and people were just,

                     
like, jumping out of their skin.

                    
They were, like, so much more

                     
comfortable with me killing

                     
people than kissing men.

                     
Isn't that weird?

                     
Yeah.

                     
Well, it's not that surprising,

                     
I guess.

                     
Sad.

                     
You did do a lot of

                     
singing here, and I was

                     
wondering if Dexter did have a

                     
good favorite holiday song,

                     
maybe?

                     
If Dexter had a favorite

                     
holiday song?

                     
Can you give us a

                     
taste of a little something,

                     
maybe?

                     
'Cause we're in the holiday

                     
spirit here.

                     
I would guess maybe  Santa

                    
claus is coming to town. 

                     
You know, there's something

                     
about those lyrics that I would

                     
imagine would resonate with him.

                     
I can imagine Harry singing it

                     
to Dexter when he was little.

                     
You know?

                    
Can you maybe give us

                    
a taste of that, please?

                     
Come on.

                     
Sure.

                     
It's the holiday

                     
season.

                     
♪

                     
♪ you better watch out

                     
you better not cry

                     
you better not pout

                     
I'm telling you why ♪

                     
♪ Santa claus

                     
is coming to town ♪

                     
♪ He's making a list

                     
he's checking it twice

                     
he's gonna find out whose

                     
cheek he should slice ♪

                     
♪ Santa claus

                     
is coming to town ♪

                     
♪ he sees you

                     
when you're sleeping ♪

                     
I'm scared right now.

                     
♪ He knows when you're awake

                     
he knows if you've

                     
been bad or good ♪

                     
♪ so be good

                     
for goodness sake ♪

                     
♪ oh, you better watch out

                     
you better not cry ♪

                     
He's talking to

                     
everybody.

                     
♪ You better not pout

                     
I'm telling you why

                    
Santa claus will kill you

                     
if you're bad ♪

                     
No, hey!

                     
No, hey!

                     
Those aren't the lyrics?

                     
Michael c. Hall!

                     
The season finale of  Dexter  is

                    
this Sunday at     P.M. on

                     
showtime.

                     
Michael c. Hall, everybody!

                     
Busy Philipps joins us next.

                     
There she is in the bud light

                     
lime green room!

                     
Hey, Busy!

                     
♪

                     
Welcome back,

                     
everybody!

                     
Our next guest is a very

                     
talented actress who stars in

                     
the popular abc show

                     
 cougar town,  which airs

                     
Wednesday at      P.M.

                     
Please welcome Busy Philipps!

                     
♪

                     
Busy, Busy, Busy,

                     
Busy!

                    
Hi!

                   
You look very pretty.

                    
Thank you for coming on the

                     
show.

                     
Thanks for having me, Jimmy.

                     
We've met a few times.

                    
Yes, we have.

                     
With your husband,

                     
very talented writer.

                     
My husband and your wife...

                    
Yes, work together.

                     
Work together quite a bit.

                     
I feel like they've worked

                     
together nonstop for years.

                     
They have.

                     
He wrote with his partner,  he's

                     
just not that into you. 

                     
And their very first movie

                     
was  never been kissed  with

                     
Nancy.

                     
That's right.

                     
So that was, like, ten years

                     
ago.

                     
Absolutely.

                     
Now, are you guys enjoying...

                     
are you in New York for the

                     
holiday or no?

                     
No, no, no.

                    
We're in L.A.

                     
I'm just here for the day.

                     
Just to see you.

                     
Hey, thank you so

                     
much.

                     
And then I'm going home to

                     
see my family.

                     
Yeah.

                     
Oh, I appreciate that.

                    
Did you get away or do anything

                     
while you have time off?

                     
Yeah.

                     
For Thanksgiving, we went,

                     
actually, my husband and I had

                     
our first, like, romantic

                     
getaway without our kid.

                     
And we went to Mexico for the

                     
weekend.

                     
That's nice.

                     
You would think.

                     
Well, no, it was nice.

                    
What happened?

                     
It was nice, but it was sort

                     
of, like, kind of a bad omen

                     
when at the airport... we

                     
dropped my kid off in Phoenix

                     
with her grandparents.

                     
And at the Phoenix airport, we

                     
saw this guy at     in the

                    
morning get into a fight with

                    
the chili's bartender, like, at

                     
chili's to go.

                     
This guy wearing, like, full-on

                     
tevas, cargo shorts, like,

                     
patagonia, and he just starts

                     
yelling,  you want a piece

                     
of me? 

                     
No!

                     
Which is, like, not something

                     
that you ever expect to see in

                    
real life.

                     
His reading glasses on his head,

                     
 you want a piece of me? 

                     
And the bartender at chili's to

                     
go was like,  no, no, I don't. 

                     
 Like, I absolutely do not want

                     
a piece of you. 

                     
He's like,  I am

                     
Michael c. Hall and I want a

                     
 drink! 

                     
No.

                     
It was intense.

                     
And then we get there, and we

                    
were staying at this place which

                     
looked really beautiful.

                     
We were with some friends.

                     
But you have to, like, you fly

                     
into Puerto Vallarta and then

                     
you drive for an hour and a

                     
half.

                     
And then you take a boat

                     
   minutes to, like, a secluded

                     
island in the jungle.

                    
Whoa.

                     
And so, you're really cut off

                    
from civilization.

                     
Remote, yeah.

                     
And your phone gets spotty

                     
reception.

                     
And as we're hiking up into the

                     
resort, I'm like,  guys, I have

                     
a bad feeling about this.

                    
I just think something's gonna

                     
 happen. 

                     
And the resort was kind of

                     
terrorized by a jaguar that

                    
weekend that we were there.

                     
I'm sorry.

                     
I'm so sorry.

                     
Yes.

                     
Terrorized by a

                     
jaguar?

                     
Yeah.

                     
Well, it's all open rooms.

                     
And there was a jaguar that had

                     
come down from the mountains,

                     
and it was in my friend's room.

                     
Okay.

                     
In the middle of the night.

                     
And the people at the resort

                     
were trying... this is true.

                     
This is a romantic

                     
getaway?

                     
Yes, our romantic getaway.

                     
And the people in the resort

                     
were trying to pass it off.

                     
They kept telling us it was just

                     
a Mexican raccoon.

                     
Which is so crazy.

                     
Does that even exist?

                     
Is that real?

                     
I don't think so!

                     
I don't think so!

                     
I think they're just... no.

                     
It was a jaguar.

                     
And so then, my friend switched

                     
rooms.

                     
And this Australian couple

                     
stayed there.

                     
And then, the guy was, like,

                     
super burly and covered in tats

                     
and, like, really a hardcore

                     
Australian dude.

                     
And the next morning, he woke up

                     
and he was like...

                     
 Chased a jaguar out of my room

                     
last night, broke a bottle. 

                     
And chased him, like, down the

                     
stairs, out of their open-air

                     
room.

                     
What is going on?

                     
I'm not kidding.

                    
He broke a bottle and

                     
attacked and showed the

                     
jaguar...

                     
it jumped over their bed and

                     
he, like, broke a bottle and

                     
chased after the jaguar.

                    
With a jagged bottle?

                    
I guess.

                     
That would be so not

                     
what I would do.

                     
I would pretend I'm dead while

                     
my wife would scream.

                     
 Don't talk to me!

                     
Don't talk to me! 

                     
You read the rules.

                     
There's a wild animal in here, I

                     
pretend I'm dead.

                     
And then my wife... we both have

                     
to have a pact.

                     
I've got to call her.

                    
I've got to talk to her tonight

                     
and make sure if there's ever a

                     
wild animal.

                     
I mean, what would you do?

                     
No one is doing anything.

                     
Who switched rooms?

                     
That would be the worst idea.

                     
My friend Irene.

                     
What do you mean?

                     
She switched rooms with the

                     
Australian.

                     
With the one that's

                     
already been attacked by the

                     
jaguar?

                     
She was the one that

                     
originally saw and heard the

                     
jaguar the night before.

                     
Switched rooms with the

                     
Australians, 'cause they're

                     
like,  we're not afraid, we're

                     
Australian! 

                     
They're tough people.

                     
They're tough people.

                     
They are.

                     
They are a tough people.

                     
And then, the jaguar got them,

                     
and then they were a little

                     
afraid.

                    
Yeah.

                     
Yeah, it was crazy.

                     
Oh, my gosh.

                     
Amazing.

                     
Well, thank you for that.

                     
I know you have  cougar town  is

                     
a huge hit.

                     
But a lot of people might

                    
remember you from your first tv

                    
show,  freaks and geeks. 

                    
Look at this.

                     
Oh, look at those pictures.

                     
Look at the babies.

                     
Look at those babies!

                     
Look how well you've

                     
all done.

                     
I mean, a lot of familiar faces

                     
here, James Franco, Seth Rogen.

                     
Jason Segel right there.

                     
Linda Cardellini, John

                     
Francis daley, who's, like, the

                     
tiniest baby in that picture and

                     
now is like  ' tall.

                     
Yeah, Samm levine.

                     
Yeah.

                     
I mean, I feel like it's pretty

                     
crazy that everyone, like half

                     
of the cast, are basically

                     
running Hollywood right now.

                     
Like, the biggest comedy movie

                     
stars.

                     
Yeah, they are.

                     
It's super fun.

                     
That must have been a blast

                     
working on that.

                     
I was a big fan of the show.

                     
Yeah.

                     
It was a blast.

                     
It was such a great time.

                     
But we all still have a very,

                     
you know, fond remembrance of

                     
the time.

                     
We keep in touch, and I love my

                     
buddies.

                     
I'm so happy.

                     
That was like your

                     
freshman class.

                     
And now you're doing

                     
 Cougarton. 

                     
 Cougarton,  that's how we

                     
pronounce it!

                     
Is that right?

                     
Yes, the  Cougartons. 

                     
We should be best

                     
friends.

                     
Oh, we should.

                     
Cougarton.

                     
Yeah,  cougar town,  with

                    
Courtney Cox.

                     
It's a huge hit, and it's a

                    
super funny premise, but I love

                     
that... this is a quote from

                    
 the New York times. 

                     
They said, they called the

                     
show... they called you guys

                     
 vegan yoga babes at a spa

                     
getaway. 

                     
So strange, because never in

                   
my life have I been described as

                     
a  vegan yoga babe. 

                    
People are always like,  I like

                     
that there's a real girl on tv, 

                     
like...

                     
it's so strange, because their

                     
point, I guess, was that we

                     
booze a lot on the show, we

                     
drink a lot of red wine, but we

                     
always look like sort of dewy

                     
and wonderful.

                     
But we actually make a concerted

                     
effort, at least on my

                     
character's part, to make her

                     
look like a floozy.

                     
Like, we always, I'm always

                     
like,  and the lipstick should

                     
be a little bit smeared right

                     
 here. 

                     
So, I guess that's maybe the

                     
person from  the New York times 

                     
is not following the show as

                     
closely...

                     
As closely, yeah.

                     
Maybe they need to be.

                     
Was it... oh, my God,

                     
what's that character?

                     
That's old lady glamour,

                     
right there.

                     
I don't know who that is!

                     
Old lady glamour?

                     
But she's terrible and should

                    
never come back!

                    
We do have a clip of

                     
you being very funny on

                     
 cougar town. 

                     
I'm pretending to be in a

                     
sorority, yes.

                     
I overheard Kyle, that

                     
douchey

                     
sigma kai who is always wearing

                    
the Jester hat, say that he

                     
hooked up with missy here, even

                     
though he dates a kappa.

                     
Missy, did you?

                     
Laugh!

                     
She totally did.

                     
Laugh!

                     
But sisters, this is a real

                    
teaching moment.

                     
The only way not to be labeled a

                     
tramp is to not sleep with guys

                     
who talk so much.

                     
Laugh!

                     
No, Deborah, I'm dead

                     
serious.

                     
Laurie?

                     
Trav!

                     
Hey!

                     
Zeta!

                     
Zeta!

                     
No, not laugh.

                     
Busy Phillips!

                     
 Cougar town  airs wednesdays at

                     
     P.M. on abc.

                     
R. Kelly performs next.

                     
Come on back!

                     
♪

                     
Oh, I'm so excited

                     
about our next guest.

                     
He's a music superstar whose new

                     
album,  love letter,  will be

                     
out next week.

                     
He's back again tonight to

                     
perform the track  number one

                     
hit. 

                     
Please welcome r. Kelly!

                     
♪

                     
♪ I wanna bring a love song

                    
thank you!

                    
Come on, look at you.

                     
Come back whenever, buddy.

                     
R. Kelly!

                     
That's the way to do it.

                     
Check out his new album,

                     
 love letter. 

                     
Visit

                     
latenightwithjimmyfallon. Com for

                     
an exclusive performance right

                     
now from r. Kelly with

                     
the roots.

                     
My thanks to Michael c. Hall,

                     
Busy Philipps, r. Kelly, once

                     
again!

                     
Kermit Ruffins over there.

                     
And the greatest band in

                     
late night, the roots!

                     
Stay tuned for  Carson Daly. 

                     
Thank you for watching.

                     
Have a good night!

                     
I hope to see you tomorrow.

                     
Good night, everybody!

                     
♪

                     
 

                     
 

<end subtitles>"



