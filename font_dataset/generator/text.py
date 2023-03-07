import random
from ..loader.font import DSFont
from .helper import char_in_font

__all__ = ['random_char']

# https://zh.wikipedia.org/zh-hans/%E5%B9%B3%E5%81%87%E5%90%8D
hiragana = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわをん'

# https://zh.wikipedia.org/zh-hans/%E7%89%87%E5%81%87%E5%90%8D
katakana = 'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヲンヵヶ'

# https://ja.wiktionary.org/wiki/%E4%BB%98%E9%8C%B2:%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97%E3%81%AE%E4%B8%80%E8%A6%A7
common_kanji = '亜哀挨愛曖悪握圧扱宛嵐安案暗以衣位囲医依委威為畏胃尉異移萎偉椅彙意違維慰遺緯域育一壱逸茨芋引印因咽姻員院淫陰飲隠韻右宇羽雨唄鬱畝浦運雲永泳英映栄営詠影鋭衛易疫益液駅悦越謁閲円延沿炎怨宴媛援園煙猿遠鉛塩演縁艶汚王凹央応往押旺欧殴桜翁奥横岡屋億憶臆虞乙俺卸音恩温穏下化火加可仮何花佳価果河苛科架夏家荷華菓貨渦過嫁暇禍靴寡歌箇稼課蚊牙瓦我画芽賀雅餓介回灰会快戒改怪拐悔海界皆械絵開階塊楷解潰壊懐諧貝外劾害崖涯街慨蓋該概骸垣柿各角拡革格核殻郭覚較隔閣確獲嚇穫学岳楽額顎掛潟括活喝渇割葛滑褐轄且株釜鎌刈干刊甘汗缶完肝官冠巻看陥乾勘患貫寒喚堪換敢棺款間閑勧寛幹感漢慣管関歓監緩憾還館環簡観韓艦鑑丸含岸岩玩眼頑顔願企伎危机気岐希忌汽奇祈季紀軌既記起飢鬼帰基寄規亀喜幾揮期棋貴棄毀旗器畿輝機騎技宜偽欺義疑儀戯擬犠議菊吉喫詰却客脚逆虐九久及弓丘旧休吸朽臼求究泣急級糾宮救球給嗅窮牛去巨居拒拠挙虚許距魚御漁凶共叫狂京享供協況峡挟狭恐恭胸脅強教郷境橋矯鏡競響驚仰暁業凝曲局極玉巾斤均近金菌勤琴筋僅禁緊錦謹襟吟銀区句苦駆具惧愚空偶遇隅串屈掘窟熊繰君訓勲薫軍郡群兄刑形系径茎係型契計恵啓掲渓経蛍敬景軽傾携継詣慶憬稽憩警鶏芸迎鯨隙劇撃激桁欠穴血決結傑潔月犬件見券肩建研県倹兼剣拳軒健険圏堅検嫌献絹遣権憲賢謙鍵繭顕験懸元幻玄言弦限原現舷減源厳己戸古呼固股虎孤弧故枯個庫湖雇誇鼓錮顧五互午呉後娯悟碁語誤護口工公勾孔功巧広甲交光向后好江考行坑孝抗攻更効幸拘肯侯厚恒洪皇紅荒郊香候校耕航貢降高康控梗黄喉慌港硬絞項溝鉱構綱酵稿興衡鋼講購乞号合拷剛傲豪克告谷刻国黒穀酷獄骨駒込頃今困昆恨根婚混痕紺魂墾懇左佐沙査砂唆差詐鎖座挫才再災妻采砕宰栽彩採済祭斎細菜最裁債催塞歳載際埼在材剤財罪崎作削昨柵索策酢搾錯咲冊札刷刹拶殺察撮擦雑皿三山参桟蚕惨産傘散算酸賛残斬暫士子支止氏仕史司四市矢旨死糸至伺志私使刺始姉枝祉肢姿思指施師恣紙脂視紫詞歯嗣試詩資飼誌雌摯賜諮示字寺次耳自似児事侍治持時滋慈辞磁餌璽鹿式識軸七叱失室疾執湿嫉漆質実芝写社車舎者射捨赦斜煮遮謝邪蛇尺借酌釈爵若弱寂手主守朱取狩首殊珠酒腫種趣寿受呪授需儒樹収囚州舟秀周宗拾秋臭修袖終羞習週就衆集愁酬醜蹴襲十汁充住柔重従渋銃獣縦叔祝宿淑粛縮塾熟出述術俊春瞬旬巡盾准殉純循順準潤遵処初所書庶暑署緒諸女如助序叙徐除小升少召匠床抄肖尚招承昇松沼昭宵将消症祥称笑唱商渉章紹訟勝掌晶焼焦硝粧詔証象傷奨照詳彰障憧衝賞償礁鐘上丈冗条状乗城浄剰常情場畳蒸縄壌嬢錠譲醸色拭食植殖飾触嘱織職辱尻心申伸臣芯身辛侵信津神唇娠振浸真針深紳進森診寝慎新審震薪親人刃仁尽迅甚陣尋腎須図水吹垂炊帥粋衰推酔遂睡穂随髄枢崇数据杉裾寸瀬是井世正生成西声制姓征性青斉政星牲省凄逝清盛婿晴勢聖誠精製誓静請整醒税夕斥石赤昔析席脊隻惜戚責跡積績籍切折拙窃接設雪摂節説舌絶千川仙占先宣専泉浅洗染扇栓旋船戦煎羨腺詮践箋銭潜線遷選薦繊鮮全前善然禅漸膳繕狙阻祖租素措粗組疎訴塑遡礎双壮早争走奏相荘草送倉捜挿桑巣掃曹曽爽窓創喪痩葬装僧想層総遭槽踪操燥霜騒藻造像増憎蔵贈臓即束足促則息捉速側測俗族属賊続卒率存村孫尊損遜他多汰打妥唾堕惰駄太対体耐待怠胎退帯泰堆袋逮替貸隊滞態戴大代台第題滝宅択沢卓拓託濯諾濁但達脱奪棚誰丹旦担単炭胆探淡短嘆端綻誕鍛団男段断弾暖談壇地池知値恥致遅痴稚置緻竹畜逐蓄築秩窒茶着嫡中仲虫沖宙忠抽注昼柱衷酎鋳駐著貯丁弔庁兆町長挑帳張彫眺釣頂鳥朝貼超腸跳徴嘲潮澄調聴懲直勅捗沈珍朕陳賃鎮追椎墜通痛塚漬坪爪鶴低呈廷弟定底抵邸亭貞帝訂庭逓停偵堤提程艇締諦泥的笛摘滴適敵溺迭哲鉄徹撤天典店点展添転填田伝殿電斗吐妬徒途都渡塗賭土奴努度怒刀冬灯当投豆東到逃倒凍唐島桃討透党悼盗陶塔搭棟湯痘登答等筒統稲踏糖頭謄藤闘騰同洞胴動堂童道働銅導瞳峠匿特得督徳篤毒独読栃凸突届屯豚頓貪鈍曇丼那奈内梨謎鍋南軟難二尼弐匂肉虹日入乳尿任妊忍認寧熱年念捻粘燃悩納能脳農濃把波派破覇馬婆罵拝杯背肺俳配排敗廃輩売倍梅培陪媒買賠白伯拍泊迫剥舶博薄麦漠縛爆箱箸畑肌八鉢発髪伐抜罰閥反半氾犯帆汎伴判坂阪板版班畔般販斑飯搬煩頒範繁藩晩番蛮盤比皮妃否批彼披肥非卑飛疲秘被悲扉費碑罷避尾眉美備微鼻膝肘匹必泌筆姫百氷表俵票評漂標苗秒病描猫品浜貧賓頻敏瓶不夫父付布扶府怖阜附訃負赴浮婦符富普腐敷膚賦譜侮武部舞封風伏服副幅復福腹複覆払沸仏物粉紛雰噴墳憤奮分文聞丙平兵併並柄陛閉塀幣弊蔽餅米壁璧癖別蔑片辺返変偏遍編弁便勉歩保哺捕補舗母募墓慕暮簿方包芳邦奉宝抱放法泡胞俸倣峰砲崩訪報蜂豊飽褒縫亡乏忙坊妨忘防房肪某冒剖紡望傍帽棒貿貌暴膨謀頬北木朴牧睦僕墨撲没勃堀本奔翻凡盆麻摩磨魔毎妹枚昧埋幕膜枕又末抹万満慢漫未味魅岬密蜜脈妙民眠矛務無夢霧娘名命明迷冥盟銘鳴滅免面綿麺茂模毛妄盲耗猛網目黙門紋問冶夜野弥厄役約訳薬躍闇由油喩愉諭輸癒唯友有勇幽悠郵湧猶裕遊雄誘憂融優与予余誉預幼用羊妖洋要容庸揚揺葉陽溶腰様瘍踊窯養擁謡曜抑沃浴欲翌翼拉裸羅来雷頼絡落酪辣乱卵覧濫藍欄吏利里理痢裏履璃離陸立律慄略柳流留竜粒隆硫侶旅虜慮了両良料涼猟陵量僚領寮療瞭糧力緑林厘倫輪隣臨瑠涙累塁類令礼冷励戻例鈴零霊隷齢麗暦歴列劣烈裂恋連廉練錬呂炉賂路露老労弄郎朗浪廊楼漏籠六録麓論和話賄脇惑枠湾腕'

# https://gist.github.com/simongfxu/13accd501f6c91e7a423ddc43e674c0f
common_simplified_chinese = '一乙二十丁厂七卜人入八九几儿了力乃刀又三于干亏士工土才寸下大丈与万上小口巾山千乞川亿个勺久凡及夕丸么广亡门义之尸弓己已子卫也女飞刃习叉马乡丰王井开夫天无元专云扎艺木五支厅不太犬区历尤友匹车巨牙屯比互切瓦止少日中冈贝内水见午牛手毛气升长仁什片仆化仇币仍仅斤爪反介父从今凶分乏公仓月氏勿欠风丹匀乌凤勾文六方火为斗忆订计户认心尺引丑巴孔队办以允予劝双书幻玉刊示末未击打巧正扑扒功扔去甘世古节本术可丙左厉右石布龙平灭轧东卡北占业旧帅归且旦目叶甲申叮电号田由史只央兄叼叫另叨叹四生失禾丘付仗代仙们仪白仔他斥瓜乎丛令用甩印乐句匆册犯外处冬鸟务包饥主市立闪兰半汁汇头汉宁穴它讨写让礼训必议讯记永司尼民出辽奶奴加召皮边发孕圣对台矛纠母幼丝式刑动扛寺吉扣考托老执巩圾扩扫地扬场耳共芒亚芝朽朴机权过臣再协西压厌在有百存而页匠夸夺灰达列死成夹轨邪划迈毕至此贞师尘尖劣光当早吐吓虫曲团同吊吃因吸吗屿帆岁回岂刚则肉网年朱先丢舌竹迁乔伟传乒乓休伍伏优伐延件任伤价份华仰仿伙伪自血向似后行舟全会杀合兆企众爷伞创肌朵杂危旬旨负各名多争色壮冲冰庄庆亦刘齐交次衣产决充妄闭问闯羊并关米灯州汗污江池汤忙兴宇守宅字安讲军许论农讽设访寻那迅尽导异孙阵阳收阶阴防奸如妇好她妈戏羽观欢买红纤级约纪驰巡寿弄麦形进戒吞远违运扶抚坛技坏扰拒找批扯址走抄坝贡攻赤折抓扮抢孝均抛投坟抗坑坊抖护壳志扭块声把报却劫芽花芹芬苍芳严芦劳克苏杆杠杜材村杏极李杨求更束豆两丽医辰励否还歼来连步坚旱盯呈时吴助县里呆园旷围呀吨足邮男困吵串员听吩吹呜吧吼别岗帐财针钉告我乱利秃秀私每兵估体何但伸作伯伶佣低你住位伴身皂佛近彻役返余希坐谷妥含邻岔肝肚肠龟免狂犹角删条卵岛迎饭饮系言冻状亩况床库疗应冷这序辛弃冶忘闲间闷判灶灿弟汪沙汽沃泛沟没沈沉怀忧快完宋宏牢究穷灾良证启评补初社识诉诊词译君灵即层尿尾迟局改张忌际陆阿陈阻附妙妖妨努忍劲鸡驱纯纱纳纲驳纵纷纸纹纺驴纽奉玩环武青责现表规抹拢拔拣担坦押抽拐拖拍者顶拆拥抵拘势抱垃拉拦拌幸招坡披拨择抬其取苦若茂苹苗英范直茄茎茅林枝杯柜析板松枪构杰述枕丧或画卧事刺枣雨卖矿码厕奔奇奋态欧垄妻轰顷转斩轮软到非叔肯齿些虎虏肾贤尚旺具果味昆国昌畅明易昂典固忠咐呼鸣咏呢岸岩帖罗帜岭凯败贩购图钓制知垂牧物乖刮秆和季委佳侍供使例版侄侦侧凭侨佩货依的迫质欣征往爬彼径所舍金命斧爸采受乳贪念贫肤肺肢肿胀朋股肥服胁周昏鱼兔狐忽狗备饰饱饲变京享店夜庙府底剂郊废净盲放刻育闸闹郑券卷单炒炊炕炎炉沫浅法泄河沾泪油泊沿泡注泻泳泥沸波泼泽治怖性怕怜怪学宝宗定宜审宙官空帘实试郎诗肩房诚衬衫视话诞询该详建肃录隶居届刷屈弦承孟孤陕降限妹姑姐姓始驾参艰线练组细驶织终驻驼绍经贯奏春帮珍玻毒型挂封持项垮挎城挠政赴赵挡挺括拴拾挑指垫挣挤拼挖按挥挪某甚革荐巷带草茧茶荒茫荡荣故胡南药标枯柄栋相查柏柳柱柿栏树要咸威歪研砖厘厚砌砍面耐耍牵残殃轻鸦皆背战点临览竖省削尝是盼眨哄显哑冒映星昨畏趴胃贵界虹虾蚁思蚂虽品咽骂哗咱响哈咬咳哪炭峡罚贱贴骨钞钟钢钥钩卸缸拜看矩怎牲选适秒香种秋科重复竿段便俩贷顺修保促侮俭俗俘信皇泉鬼侵追俊盾待律很须叙剑逃食盆胆胜胞胖脉勉狭狮独狡狱狠贸怨急饶蚀饺饼弯将奖哀亭亮度迹庭疮疯疫疤姿亲音帝施闻阀阁差养美姜叛送类迷前首逆总炼炸炮烂剃洁洪洒浇浊洞测洗活派洽染济洋洲浑浓津恒恢恰恼恨举觉宣室宫宪突穿窃客冠语扁袄祖神祝误诱说诵垦退既屋昼费陡眉孩除险院娃姥姨姻娇怒架贺盈勇怠柔垒绑绒结绕骄绘给络骆绝绞统耕耗艳泰珠班素蚕顽盏匪捞栽捕振载赶起盐捎捏埋捉捆捐损都哲逝捡换挽热恐壶挨耻耽恭莲莫荷获晋恶真框桂档桐株桥桃格校核样根索哥速逗栗配翅辱唇夏础破原套逐烈殊顾轿较顿毙致柴桌虑监紧党晒眠晓鸭晃晌晕蚊哨哭恩唤啊唉罢峰圆贼贿钱钳钻铁铃铅缺氧特牺造乘敌秤租积秧秩称秘透笔笑笋债借值倚倾倒倘俱倡候俯倍倦健臭射躬息徒徐舰舱般航途拿爹爱颂翁脆脂胸胳脏胶脑狸狼逢留皱饿恋桨浆衰高席准座脊症病疾疼疲效离唐资凉站剖竞部旁旅畜阅羞瓶拳粉料益兼烤烘烦烧烛烟递涛浙涝酒涉消浩海涂浴浮流润浪浸涨烫涌悟悄悔悦害宽家宵宴宾窄容宰案请朗诸读扇袜袖袍被祥课谁调冤谅谈谊剥恳展剧屑弱陵陶陷陪娱娘通能难预桑绢绣验继球理捧堵描域掩捷排掉堆推掀授教掏掠培接控探据掘职基著勒黄萌萝菌菜萄菊萍菠营械梦梢梅检梳梯桶救副票戚爽聋袭盛雪辅辆虚雀堂常匙晨睁眯眼悬野啦晚啄距跃略蛇累唱患唯崖崭崇圈铜铲银甜梨犁移笨笼笛符第敏做袋悠偿偶偷您售停偏假得衔盘船斜盒鸽悉欲彩领脚脖脸脱象够猜猪猎猫猛馅馆凑减毫麻痒痕廊康庸鹿盗章竟商族旋望率着盖粘粗粒断剪兽清添淋淹渠渐混渔淘液淡深婆梁渗情惜惭悼惧惕惊惨惯寇寄宿窑密谋谎祸谜逮敢屠弹随蛋隆隐婚婶颈绩绪续骑绳维绵绸绿琴斑替款堪搭塔越趁趋超提堤博揭喜插揪搜煮援裁搁搂搅握揉斯期欺联散惹葬葛董葡敬葱落朝辜葵棒棋植森椅椒棵棍棉棚棕惠惑逼厨厦硬确雁殖裂雄暂雅辈悲紫辉敞赏掌晴暑最量喷晶喇遇喊景践跌跑遗蛙蛛蜓喝喂喘喉幅帽赌赔黑铸铺链销锁锄锅锈锋锐短智毯鹅剩稍程稀税筐等筑策筛筒答筋筝傲傅牌堡集焦傍储奥街惩御循艇舒番释禽腊脾腔鲁猾猴然馋装蛮就痛童阔善羡普粪尊道曾焰港湖渣湿温渴滑湾渡游滋溉愤慌惰愧愉慨割寒富窜窝窗遍裕裤裙谢谣谦属屡强粥疏隔隙絮嫂登缎缓编骗缘瑞魂肆摄摸填搏塌鼓摆携搬摇搞塘摊蒜勤鹊蓝墓幕蓬蓄蒙蒸献禁楚想槐榆楼概赖酬感碍碑碎碰碗碌雷零雾雹输督龄鉴睛睡睬鄙愚暖盟歇暗照跨跳跪路跟遣蛾蜂嗓置罪罩错锡锣锤锦键锯矮辞稠愁筹签简毁舅鼠催傻像躲微愈遥腰腥腹腾腿触解酱痰廉新韵意粮数煎塑慈煤煌满漠源滤滥滔溪溜滚滨粱滩慎誉塞谨福群殿辟障嫌嫁叠缝缠静碧璃墙撇嘉摧截誓境摘摔聚蔽慕暮蔑模榴榜榨歌遭酷酿酸磁愿需弊裳颗嗽蜻蜡蝇蜘赚锹锻舞稳算箩管僚鼻魄貌膜膊膀鲜疑馒裹敲豪膏遮腐瘦辣竭端旗精歉熄熔漆漂漫滴演漏慢寨赛察蜜谱嫩翠熊凳骡缩慧撕撒趣趟撑播撞撤增聪鞋蕉蔬横槽樱橡飘醋醉震霉瞒题暴瞎影踢踏踩踪蝶蝴嘱墨镇靠稻黎稿稼箱箭篇僵躺僻德艘膝膛熟摩颜毅糊遵潜潮懂额慰劈操燕薯薪薄颠橘整融醒餐嘴蹄器赠默镜赞篮邀衡膨雕磨凝辨辩糖糕燃澡激懒壁避缴戴擦鞠藏霜霞瞧蹈螺穗繁辫赢糟糠燥臂翼骤鞭覆蹦镰翻鹰警攀蹲颤瓣爆疆壤耀躁嚼嚷籍魔灌蠢霸露囊罐匕刁丐歹戈夭仑讥冗邓艾夯凸卢叭叽皿凹囚矢乍尔冯玄邦迂邢芋芍吏夷吁吕吆屹廷迄臼仲伦伊肋旭匈凫妆亥汛讳讶讹讼诀弛阱驮驯纫玖玛韧抠扼汞扳抡坎坞抑拟抒芙芜苇芥芯芭杖杉巫杈甫匣轩卤肖吱吠呕呐吟呛吻吭邑囤吮岖牡佑佃伺囱肛肘甸狈鸠彤灸刨庇吝庐闰兑灼沐沛汰沥沦汹沧沪忱诅诈罕屁坠妓姊妒纬玫卦坷坯拓坪坤拄拧拂拙拇拗茉昔苛苫苟苞茁苔枉枢枚枫杭郁矾奈奄殴歧卓昙哎咕呵咙呻咒咆咖帕账贬贮氛秉岳侠侥侣侈卑刽刹肴觅忿瓮肮肪狞庞疟疙疚卒氓炬沽沮泣泞泌沼怔怯宠宛衩祈诡帚屉弧弥陋陌函姆虱叁绅驹绊绎契贰玷玲珊拭拷拱挟垢垛拯荆茸茬荚茵茴荞荠荤荧荔栈柑栅柠枷勃柬砂泵砚鸥轴韭虐昧盹咧昵昭盅勋哆咪哟幽钙钝钠钦钧钮毡氢秕俏俄俐侯徊衍胚胧胎狰饵峦奕咨飒闺闽籽娄烁炫洼柒涎洛恃恍恬恤宦诫诬祠诲屏屎逊陨姚娜蚤骇耘耙秦匿埂捂捍袁捌挫挚捣捅埃耿聂荸莽莱莉莹莺梆栖桦栓桅桩贾酌砸砰砾殉逞哮唠哺剔蚌蚜畔蚣蚪蚓哩圃鸯唁哼唆峭唧峻赂赃钾铆氨秫笆俺赁倔殷耸舀豺豹颁胯胰脐脓逛卿鸵鸳馁凌凄衷郭斋疹紊瓷羔烙浦涡涣涤涧涕涩悍悯窍诺诽袒谆祟恕娩骏琐麸琉琅措捺捶赦埠捻掐掂掖掷掸掺勘聊娶菱菲萎菩萤乾萧萨菇彬梗梧梭曹酝酗厢硅硕奢盔匾颅彪眶晤曼晦冕啡畦趾啃蛆蚯蛉蛀唬啰唾啤啥啸崎逻崔崩婴赊铐铛铝铡铣铭矫秸秽笙笤偎傀躯兜衅徘徙舶舷舵敛翎脯逸凰猖祭烹庶庵痊阎阐眷焊焕鸿涯淑淌淮淆渊淫淳淤淀涮涵惦悴惋寂窒谍谐裆袱祷谒谓谚尉堕隅婉颇绰绷综绽缀巢琳琢琼揍堰揩揽揖彭揣搀搓壹搔葫募蒋蒂韩棱椰焚椎棺榔椭粟棘酣酥硝硫颊雳翘凿棠晰鼎喳遏晾畴跋跛蛔蜒蛤鹃喻啼喧嵌赋赎赐锉锌甥掰氮氯黍筏牍粤逾腌腋腕猩猬惫敦痘痢痪竣翔奠遂焙滞湘渤渺溃溅湃愕惶寓窖窘雇谤犀隘媒媚婿缅缆缔缕骚瑟鹉瑰搪聘斟靴靶蓖蒿蒲蓉楔椿楷榄楞楣酪碘硼碉辐辑频睹睦瞄嗜嗦暇畸跷跺蜈蜗蜕蛹嗅嗡嗤署蜀幌锚锥锨锭锰稚颓筷魁衙腻腮腺鹏肄猿颖煞雏馍馏禀痹廓痴靖誊漓溢溯溶滓溺寞窥窟寝褂裸谬媳嫉缚缤剿赘熬赫蔫摹蔓蔗蔼熙蔚兢榛榕酵碟碴碱碳辕辖雌墅嘁踊蝉嘀幔镀舔熏箍箕箫舆僧孵瘩瘟彰粹漱漩漾慷寡寥谭褐褪隧嫡缨撵撩撮撬擒墩撰鞍蕊蕴樊樟橄敷豌醇磕磅碾憋嘶嘲嘹蝠蝎蝌蝗蝙嘿幢镊镐稽篓膘鲤鲫褒瘪瘤瘫凛澎潭潦澳潘澈澜澄憔懊憎翩褥谴鹤憨履嬉豫缭撼擂擅蕾薛薇擎翰噩橱橙瓢蟥霍霎辙冀踱蹂蟆螃螟噪鹦黔穆篡篷篙篱儒膳鲸瘾瘸糙燎濒憾懈窿缰壕藐檬檐檩檀礁磷瞭瞬瞳瞪曙蹋蟋蟀嚎赡镣魏簇儡徽爵朦臊鳄糜癌懦豁臀藕藤瞻嚣鳍癞瀑襟璧戳攒孽蘑藻鳖蹭蹬簸簿蟹靡癣羹鬓攘蠕巍鳞糯譬霹躏髓蘸镶瓤矗'

# https://gist.github.com/simongfxu/13accd501f6c91e7a423ddc43e674c0f
common_traditional_chinese = '一乙二十丁廠七蔔人入八九幾兒了力乃刀又三於幹虧士工土才寸下大丈與萬上小口巾山千乞川億個勺久凡及夕丸麽廣亡門義之屍弓己已子衛也女飛刃習叉馬鄉豐王井開夫天無元專雲紮藝木五支廳不太犬区歷尤友匹車巨牙屯比互切瓦止少日中岡貝內水見午牛手毛氣升長仁什片仆化仇幣仍僅斤爪反介父從今兇分乏公倉月氏勿欠風丹勻烏鳳勾文六方火為鬥憶訂計戶認心尺引醜巴孔隊辦以允予勸雙書幻玉刊示末未擊打巧正撲扒功扔去甘世古節本術可丙左厲右石布龍平滅軋東卡北占業舊帥歸且旦目葉甲申叮电號田由史只央兄叼叫另叨嘆四生失禾丘付仗代仙們儀白仔他斥瓜乎叢令用甩印樂句匆冊犯外處冬鳥务包饑主市立閃蘭半汁匯頭漢寧穴它討寫讓禮訓必議訊記永司尼民出遼奶奴加召皮邊發孕聖對臺矛糾母幼絲式刑動扛寺吉扣考托老執鞏圾擴掃地揚場耳共芒亞芝朽樸機權過臣再協西壓厭在有百存而頁匠夸奪灰達列死成夾軌邪劃邁畢至此貞師塵尖劣光當早吐嚇蟲曲團同吊吃因吸嗎嶼帆歲回豈剛則肉網年朱先丟舌竹遷喬偉傳乒乓休伍伏優伐延件任傷價份華仰仿夥偽自血向似後行舟全會殺合兆企眾爺傘創肌朵雜危旬旨負各名多爭色壯沖冰莊慶亦劉齊交次衣產決充妄閉問闖羊並關米燈州汗汙江池湯忙興宇守宅字安講軍許論農諷設訪尋那迅盡導異孫陣陽收階陰防奸如婦好她媽戲羽觀歡買紅纖級約紀馳巡壽弄麥形進戒吞遠違運扶撫壇技壞擾拒找批扯址走抄壩貢攻赤折抓扮搶孝均拋投墳抗坑坊抖護殼誌扭塊声把報卻劫芽花芹芬蒼芳嚴蘆勞克蘇桿杠杜材村杏極李楊求更束豆兩麗醫辰勵否還殲來連步堅旱盯呈时吳助縣裏呆園曠圍呀噸足郵男困吵串員聽吩吹嗚吧吼別崗帳財針釘告我亂利禿秀私每兵估體何但伸作伯伶傭低你住位伴身皂佛近徹役返余希坐谷妥含鄰岔肝肚腸龜免狂猶角刪條卵島迎飯飲系言凍狀畝况床庫療應冷這序辛棄冶忘閑間悶判竈燦弟汪沙汽沃泛溝沒沈沈懷憂快完宋宏牢究窮災良證啟評補初社識訴診詞譯君靈即層尿尾遲局改張忌際陸阿陳阻附妙妖妨努忍勁雞驅純紗納綱駁縱紛紙紋紡驢紐奉玩環武青責現表規抹攏拔揀擔坦押抽拐拖拍者頂拆擁抵拘勢抱垃拉攔拌幸招坡披撥擇擡其取苦若茂蘋苗英範直茄莖茅林枝杯櫃析板松槍構傑述枕喪或畫臥事刺棗雨賣礦碼廁奔奇奮態歐壟妻轟頃轉斬輪軟到非叔肯齒些虎虜腎賢尚旺具果味昆國昌暢明易昂典固忠咐呼鳴詠呢岸巖帖羅幟嶺凱敗販購圖釣制知垂牧物乖刮稈和季委佳侍供使例版侄偵側憑僑佩貨依的迫質欣征往爬彼徑所舍金命斧爸采受乳貪念貧肤肺肢腫脹朋股肥服脅周昏魚兔狐忽狗備飾飽飼變京享店夜廟府底劑郊廢凈盲放刻育閘鬧鄭券卷單炒炊炕炎爐沫淺法泄河沾淚油泊沿泡註瀉泳泥沸波潑澤治怖性怕憐怪學寶宗定宜審宙官空簾實試郎詩肩房誠襯衫視話誕詢該詳建肅錄隸居屆刷屈弦承孟孤陜降限妹姑姐姓始駕參艱線練組細駛織終駐駝紹經贯奏春幫珍玻毒型掛封持項垮挎城撓政赴趙擋挺括拴拾挑指墊掙擠拼挖按揮挪某甚革薦巷帶草繭茶荒茫蕩榮故胡南藥標枯柄棟相查柏柳柱柿欄樹要鹹威歪研磚厘厚砌砍面耐耍牽殘殃輕鴉皆背戰點臨覽豎省削嘗是盼眨哄顯啞冒映星昨畏趴胃貴界虹蝦蟻思螞雖品咽罵嘩咱響哈咬咳哪炭峽罰賤貼骨鈔鐘鋼鑰钩卸缸拜看矩怎牲選適秒香種秋科重復竿段便倆貸順修保促侮儉俗俘信皇泉鬼侵追俊盾待律很須敘劍逃食盆膽勝胞胖脈勉狹獅獨狡獄狠貿怨急饒蝕餃餅彎將獎哀亭亮度跡庭瘡瘋疫疤姿親音帝施聞閥閣差养美姜叛送類迷前首逆總煉炸炮爛剃潔洪灑澆濁洞測洗活派洽染濟洋洲渾濃津恒恢恰惱恨舉覺宣室宮宪突穿竊客冠語扁襖祖神祝誤誘說誦墾退既屋晝費陡眉孩除險院娃姥姨姻嬌怒架賀盈勇怠柔壘綁絨結绕驕繪給絡駱絕絞統耕耗艷泰珠班素蠶頑盞匪撈栽捕振載趕起鹽捎捏埋捉捆捐損都哲逝撿換挽熱恐壺挨恥耽恭蓮莫荷獲晉惡真框桂檔桐株橋桃格校核樣根索哥速逗栗配翅辱唇夏礎破原套逐烈殊顧轎較頓毙致柴桌慮監緊黨曬眠曉鴨晃晌暈蚊哨哭恩喚啊唉罷峰圓賊賄錢鉗鉆鐵鈴鉛缺氧特犧造乘敵秤租積秧秩稱秘透筆笑筍債借值倚傾倒倘俱倡候俯倍倦健臭射躬息徒徐艦艙般航途拿爹愛頌翁脆脂胸胳臟膠腦狸狼逢留皺餓戀槳漿衰高席準座脊癥病疾疼疲效離唐資涼站剖競部旁旅畜閱羞瓶拳粉料益兼烤烘煩燒烛煙遞濤浙澇酒涉消浩海塗浴浮流潤浪浸漲燙湧悟悄悔悅害寬家宵宴賓窄容宰案請朗諸讀扇襪袖袍被祥課誰調冤諒談誼剝懇展劇屑弱陵陶陷陪娛娘通能難預桑絹繡驗繼球理捧堵描域掩捷排掉堆推掀授教掏掠培接控探據掘職基著勒黃萌蘿菌菜萄菊萍菠營械夢梢梅檢梳梯桶救副票戚爽聾襲盛雪輔輛虛雀堂常匙晨睜瞇眼懸野啦晚啄距躍略蛇累唱患唯崖嶄崇圈銅鏟銀甜梨犁移笨籠笛符第敏做袋悠償偶偷您售停偏假得銜盤船斜盒鴿悉欲彩領腳脖臉脫象夠猜豬獵貓猛餡館湊減毫麻癢痕廊康庸鹿盜章竟商族旋望率著蓋粘粗粒斷剪獸清添淋淹渠漸混漁淘液淡深婆梁滲情惜慚悼懼惕驚慘慣寇寄宿窯密謀謊禍謎逮敢屠彈隨蛋隆隱婚嬸頸績緒續騎繩維綿綢綠琴斑替款堪搭塔越趁趨超提堤博揭喜插揪搜煮援裁擱摟攪握揉斯期欺聯散惹葬葛董葡敬蔥落朝辜葵棒棋植森椅椒棵棍棉棚棕惠惑逼廚廈硬確雁殖裂雄暫雅輩悲紫辉敞賞掌晴暑最量噴晶喇遇喊景踐跌跑遺蛙蛛蜓喝餵喘喉幅帽賭賠黑鑄鋪鏈銷鎖鋤鍋銹鋒銳短智毯鵝剩稍程稀稅筐等築策篩筒答筋箏傲傅牌堡集焦傍儲奧街懲禦循艇舒番釋禽臘脾腔魯猾猴然饞裝蠻就痛童闊善羨普糞尊道曾焰港湖渣濕溫渴滑灣渡遊滋溉憤慌惰愧愉慨割寒富竄窩窗遍裕褲裙謝謠謙屬屢強粥疏隔隙絮嫂登緞緩編騙緣瑞魂肆攝摸填搏塌鼓擺攜搬搖搞塘攤蒜勤鵲藍墓幕蓬蓄蒙蒸獻禁楚想槐榆楼概賴酬感礙碑碎碰碗碌雷零霧雹輸督齡鑒睛睡睬鄙愚暖盟歇暗照跨跳跪路跟遣蛾蜂嗓置罪罩錯錫鑼锤錦鍵鋸矮辭稠愁籌簽簡毀舅鼠催傻像躲微愈遙腰腥腹騰腿觸解醬痰廉新韻意糧數煎塑慈煤煌滿漠源滤濫滔溪溜滾濱粱灘慎譽塞謹福群殿辟障嫌嫁叠縫纏靜碧璃墻撇嘉摧截誓境摘摔聚蔽慕暮蔑模榴榜榨歌遭酷釀酸磁願需弊裳顆嗽蜻蠟蠅蜘賺鍬鍛舞穩算籮管僚鼻魄貌膜膊膀鮮疑饅裹敲豪膏遮腐瘦辣竭端旗精歉熄熔漆漂漫滴演漏慢寨賽察蜜譜嫩翠熊凳騾縮慧撕撒趣趟撐播撞撤增聰鞋蕉蔬橫槽櫻橡飄醋醉震黴瞞題暴瞎影踢踏踩蹤蝶蝴囑墨鎮靠稻黎稿稼箱箭篇僵躺僻德艘膝膛熟摩顏毅糊遵潛潮懂額慰劈操燕薯薪薄顛橘整融醒餐嘴蹄器贈默鏡贊籃邀衡膨雕磨凝辨辯糖糕燃澡激懶壁避繳戴擦鞠藏霜霞瞧蹈螺穗繁辮贏糟糠燥臂翼驟鞭覆蹦鐮翻鷹警攀蹲顫瓣爆疆壤耀躁嚼嚷籍魔灌蠢霸露囊罐匕刁丐歹戈夭侖譏冗鄧艾夯凸盧叭嘰皿凹囚矢乍爾馮玄邦迂邢芋芍吏夷籲呂吆屹廷迄臼仲倫伊肋旭匈鳧妝亥汛諱訝訛訟诀弛阱馱馴紉玖瑪韌摳扼汞扳掄坎塢抑擬抒芙蕪葦芥芯芭杖杉巫杈甫匣軒鹵肖吱吠嘔吶吟嗆吻吭邑囤吮嶇牡佑佃伺囪肛肘甸狽鳩彤灸刨庇吝廬閏兌灼沐沛汰瀝淪洶滄滬忱詛詐罕屁墜妓姊妒緯玫卦坷坯拓坪坤拄擰拂拙拇拗茉昔苛苫茍苞茁苔枉樞枚楓杭郁礬奈奄毆歧卓曇哎咕呵嚨呻咒咆咖帕賬貶貯氛秉嶽侠僥侶侈卑劊剎肴覓忿甕骯肪獰龐瘧疙疚卒氓炬沽沮泣濘泌沼怔怯寵宛衩祈詭帚屜弧彌陋陌函姆虱叁绅駒絆繹契貳玷玲珊拭拷拱挾垢垛拯荊茸茬莢茵茴蕎薺葷熒荔棧柑柵檸枷勃柬砂泵硯鷗軸韭虐昧盹咧昵昭盅勛哆咪喲幽鈣鈍鈉欽鈞鈕氈氫秕俏俄俐侯徊衍胚朧胎猙餌巒奕咨颯閨閩籽婁爍炫窪柒涎洛恃恍恬恤宦誡誣祠誨屏屎遜隕姚娜蚤駭耘耙秦匿埂捂捍袁捌挫摯搗捅埃耿聶荸莽萊莉瑩鶯梆棲樺栓桅樁賈酌砸砰礫殉逞哮嘮哺剔蚌蚜畔蚣蚪蚓哩圃鴦唁哼唆峭唧峻賂贓鉀鉚氨秫笆俺賃倔殷聳舀豺豹頒胯胰臍脓逛卿鴕鴛餒淩淒衷郭齋疹紊瓷羔烙浦渦渙滌澗涕澀悍憫竅諾誹袒諄祟恕娩駿瑣麩琉瑯措捺捶赦埠撚掐掂掖擲撣摻勘聊娶菱菲萎菩螢乾蕭薩菇彬梗梧梭曹醞酗廂矽碩奢盔匾顱彪眶晤曼晦冕啡畦趾啃蛆蚯蛉蛀唬啰唾啤啥嘯崎邏崔崩嬰賒銬鐺鋁鍘銑銘矯稭穢笙笤偎傀軀兜釁徘徙舶舷舵斂翎脯逸凰猖祭烹庶庵痊閻闡眷焊煥鴻涯淑淌淮淆淵淫淳淤澱涮涵惦悴惋寂窒諜諧襠袱禱謁謂諺尉墮隅婉頗綽繃綜綻綴巢琳琢瓊揍堰揩攬揖彭揣攙搓壹搔葫募蔣蒂韓棱椰焚椎棺榔橢粟棘酣酥硝硫頰靂翹鑿棠晰鼎喳遏晾疇跋跛蛔蜒蛤鵑喻啼喧嵌賦贖賜銼鋅甥掰氮氯黍筏牘粵逾腌腋腕猩猬憊敦痘痢瘓竣翔奠遂焙滯湘渤渺潰濺湃愕惶寓窖窘雇謗犀隘媒媚婿緬纜締縷騷瑟鵡瑰搪聘斟靴靶蓖蒿蒲蓉楔椿楷欖楞楣酪碘硼碉輻輯頻睹睦瞄嗜嗦暇畸蹺跺蜈蝸蛻蛹嗅嗡嗤署蜀幌錨錐鍁錠錳稚頹筷魁衙膩腮腺鵬肄猿穎煞雛饃餾稟痹廓癡靖誊漓溢溯溶滓溺寞窺窟寢褂裸謬媳嫉縛繽剿贅熬赫蔫摹蔓蔗藹熙蔚兢榛榕酵碟碴堿碳轅轄雌墅嘁踴蟬嘀幔鍍舔熏箍箕簫輿僧孵瘩瘟彰粹漱漩漾慷寡寥譚褐褪隧嫡纓攆撩撮撬擒墩撰鞍蕊蘊樊樟橄敷豌醇磕磅碾憋嘶嘲嘹蝠蠍蝌蝗蝙嘿幢鑷鎬稽簍膘鯉鯽褒癟瘤癱凜澎潭潦澳潘澈瀾澄憔懊憎翩褥譴鶴憨履嬉豫缭撼擂擅蕾薛薇擎翰噩櫥橙瓢蟥霍霎轍冀踱蹂蟆螃螟噪鸚黔穆篡篷篙籬儒膳鯨癮瘸糙燎瀕憾懈窿韁壕藐檬檐檁檀礁磷瞭瞬瞳瞪曙蹋蟋蟀嚎贍鐐魏簇儡徽爵朦臊鱷糜癌懦豁臀藕藤瞻囂鰭癩瀑襟璧戳攢孽蘑藻鱉蹭蹬簸簿蟹靡癬羹鬢攘蠕巍鱗糯譬霹躪髓蘸鑲瓤矗'


def random_char(length: int, font: DSFont, char_set: str) -> str:
    assert length > 0
    assert len(char_set) > 0

    ret = ''
    while len(ret) < length:
        char = random_char_from_set(char_set)
        if char_in_font(char, font.path):
            ret += char

    return char_set[random.randint(0, len(char_set) - 1)]


def generate_jp_line(length: int, font_path) -> str:
    pass


def generate_sc_line(length: int, font_path) -> str:
    pass


def generate_tc_line(length: int, font_path) -> str:
    pass
