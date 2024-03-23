from random import choice
import time as tm

#The original enchantments of Minecraft
enchants = ['水下速掘', '节肢杀手', '爆炸保护', '引雷', '绑定诅咒', '消失诅咒', '深海探索者', '效率', '摔落缓冲',
            '火焰附加', '火焰保护', '火矢', '时运', '冰霜行者', '穿刺', '无限', '击退', '抢夺', '忠诚', '海之眷顾',
            '饵钓', '经验修补', '多重射击', '穿透', '力量', '弹射物保护', '保护', '冲击', '快速装填', '水下呼吸',
            '激流', '锋利', '精准采集', '亡灵杀手', '灵魂疾行', '迅捷潜行', '横扫之刃', '荆棘', '耐久']
#The enchantments from a plugin of minecraft
enchants_special = ['aquaman', 'autoreel', 'baneofnetherspawn', 'blastmining', 'blindness', 'bomber', 'bunnyhop',
                    'coldsteel', 'confusingarrows', 'confusion', 'cure', 'curseofbreaking', 'curseofdeath',
                    'curseofdrownedzombie', 'curseoffragility', 'curseofmediocrity', 'curseofmisfortune', 'cutter',
                    'darknessarrows', 'daknesscloak', 'decapitator', 'divinetouch', 'doublecatch', 'doublestrike',
                    'dragonfirearrows', 'elementalpprotection', 'enderbow', 'exhaust', 'exphunter', 'explosivearrows',
                    'fireshield', 'flamewalker', 'flare', 'ghast', 'hardened', 'haste', 'hover', 'iceaspect',
                    'iceshield', 'infernus', 'luckyminer', 'nightvision', 'nimble', 'paralyze', 'poisonedarrows',
                    'rage', 'regrowth', 'replayer', ';restore', 'rivermaster', 'rocket', 'saturation', 'scavenger',
                    'seasonedangler', 'selfdestruction', 'silkchest', 'smelter', 'sniper', 'sonic', 'soulbound',
                    'stoppingforce', 'surprse', 'survivalist', 'swiper', 'telekinesis', 'temper', 'thrifty', 'thunder',
                    'treasures', 'tunnel', 'vampire', 'vampiricarrows', 'veinminer', 'venom', 'villagedefender',
                    'wither', 'witheredarrows']
global choice_


def special():
    specialy = int(input("\n请问是否需要将特殊附魔加入附魔池中?(是: 1,否: 0)"))
    global choice_
    tm.sleep(0.5)
    if specialy == 1:
        print("成功将特殊附魔加入附魔池中")
        choice_ = enchants + enchants_special
    elif specialy == 0:
        print("将仅抽取原版附魔")
        choice_ = enchants
    else:
        print("输入错误，请重新输入！@sky_ming Mar.24 2024")
        respe()


def respe():
    special()


def chou():
    print("\n下面进入抽取环节! ")
    tm.sleep(0.5)
    name = input("请输入您的昵称：")
    tm.sleep(0.5)
    rd = int(input("请输入抽取附魔的数量："))
    i = 1
    while i <= rd:
        enchant = choice(choice_)
        print(name + "抽到的第" + str(i) + "个附魔为：" + enchant)
        i = i + 1
        tm.sleep(0.5)
    print("附魔抽取已完成！@sky_ming Mar.24 2024\n")
    re()
    return 1


def re():
    repeat = input("继续抽取请输入1，退出请输入其他")
    if repeat == "1":
        chou()
    else:
        print("再见！@sky_ming Mar.24 2024")
        exit()


print("目前嵌入附魔库内共有: " + str(len(enchants)) + " 个原版附魔和 " + str(
    len(enchants_special)) + " 个特殊附魔(枕梦插件)\n**暂不支持使用自建附魔库**")
tm.sleep(0.5)
special()
tm.sleep(0.5)
chou()
