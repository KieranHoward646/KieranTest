"""
幽灵城堡 - 剧本内容数据
The Ghost Castle - Play Content Data
包含完整的五幕剧本和角色设定，中英双语
"""

# 剧本基本信息
PLAY_INFO = {
    "zh": {
        "title": "幽灵城堡",
        "subtitle": "五幕悲剧",
        "author": "仿莎士比亚风格创作",
        "footer": "一部五幕悲剧，仿莎士比亚风格"
    },
    "en": {
        "title": "The Ghost Castle",
        "subtitle": "A Tragedy in Five Acts",
        "author": "In the Style of William Shakespeare",
        "footer": "A tragedy in five acts, in the style of Shakespeare"
    }
}

# 角色列表
CHARACTERS = {
    "zh": {
        "Lord Blackwood": "Blackwood城堡的贵族主人，深受诅咒之苦",
        "Lady Blackwood": "他备受折磨的妻子",
        "The Ghost": "复仇的幽灵",
        "Father Benedict": "睿智的神父和顾问",
        "Thomas": "忠诚的仆人",
        "Lady Elara": "神秘的访客"
    },
    "en": {
        "Lord Blackwood": "The noble but cursed lord of the castle",
        "Lady Blackwood": "His tormented wife",
        "The Ghost": "The vengeful spirit of the castle",
        "Father Benedict": "The wise priest and counselor",
        "Thomas": "The loyal servant",
        "Lady Elara": "A mysterious visitor"
    }
}

# 导航和按钮文本
NAV_TEXT = {
    "zh": {
        "home": "首页",
        "home_sub": "HOME",
        "characters": "角色",
        "characters_sub": "CHARACTERS",
        "back": "返回首页",
        "previous_act": "上一幕",
        "next_act": "下一幕",
        "language_switch": "EN",
        "scene": "场"
    },
    "en": {
        "home": "Home",
        "home_sub": "HOME",
        "characters": "Characters",
        "characters_sub": "CHARACTERS",
        "back": "Back to Home",
        "previous_act": "Previous Act",
        "next_act": "Next Act",
        "language_switch": "中",
        "scene": "Scene"
    }
}

# 第一幕
ACT_1 = {
    "zh": {
        "title": "古堡之阴",
        "subtitle": "Act I: The Shadows of the Castle"
    },
    "en": {
        "title": "The Shadows of the Castle",
        "subtitle": "Act I: The Shadows of the Castle"
    },
    "scenes": [
        {
            "zh": {
                "title": "黄昏的降临",
                "subtitle": "Scene 1: The Fall of Evening",
                "stage_direction": "黑暗笼罩着Blackwood城堡，风雨欲来。",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "这古老的墙壁啊，你见证了多少罪恶，",
                            "多少秘密在你阴暗的角落中腐烂！",
                            "我感到一阵寒意，非是夜晚的风寒，",
                            "而是某种更黑暗的存在在逼近。"
                        ]
                    },
                    {
                        "character": "Thomas",
                        "text": [
                            "大人，暴风雨即将来临，",
                            "风在城垛间发出不祥的哀号。",
                            "今夜最好还是紧闭门窗，",
                            "不要让任何东西进来，也不要让任何东西出去。"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "你说得对，我的朋友。",
                            "但有些门一旦打开，就再也无法关闭，",
                            "有些秘密一旦唤醒，就再也无法沉睡。"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["灯光闪烁，远处传来一声凄厉的尖叫。"],
                        "is_stage_direction": True
                    }
                ]
            },
            "en": {
                "title": "The Fall of Evening",
                "subtitle": "Scene 1: The Fall of Evening",
                "stage_direction": "Darkness descends upon Blackwood Castle, a storm approaches.",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "O ancient walls, how many sins have you witnessed,",
                            "How many secrets rotting in your dark corners!",
                            "I feel a chill, not from the night's cold,",
                            "But from some darker presence drawing near."
                        ]
                    },
                    {
                        "character": "Thomas",
                        "text": [
                            "My lord, the storm approaches,",
                            "The wind wails ominously through the battlements.",
                            "Tonight we should bar all doors and windows,",
                            "Let nothing in, and nothing out."
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "You speak true, my friend.",
                            "But some doors, once opened, cannot be closed,",
                            "Some secrets, once awakened, cannot sleep again."
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["Lights flicker; a distant, mournful scream echoes."],
                        "is_stage_direction": True
                    }
                ]
            }
        },
        {
            "zh": {
                "title": "幽灵的低语",
                "subtitle": "Scene 2: The Whispers of the Dead",
                "stage_direction": "",
                "dialogue": [
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "我听到了声音，在墙壁中低语，",
                            "它们诉说着被遗忘的罪行。",
                            "那声音，我认得——是他！",
                            "那个我们以为早已消失的人！"
                        ]
                    },
                    {
                        "character": "Father Benedict",
                        "text": [
                            "镇定，我的孩子，镇定。",
                            "这只是你的恐惧在作祟，",
                            "这只是那被诅咒的想象力",
                            "在黑暗中描绘出的幻象。"
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "不！他回来了！",
                            "从那个我们送他去的地方回来了！",
                            "他要复仇了——向我们所有人！"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["突然，镜子中出现了一个苍白的身影。"],
                        "is_stage_direction": True
                    }
                ]
            },
            "en": {
                "title": "The Whispers of the Dead",
                "subtitle": "Scene 2: The Whispers of the Dead",
                "stage_direction": "",
                "dialogue": [
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "I hear voices, whispering within these walls,",
                            "Speaking of forgotten sins.",
                            "That voice, I know it — it is him!",
                            "The one we thought had long disappeared!"
                        ]
                    },
                    {
                        "character": "Father Benedict",
                        "text": [
                            "Be calm, my child, be calm.",
                            "This is but your fear at work,",
                            "This is but cursed imagination",
                            "Painting phantoms in the darkness."
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "No! He has returned!",
                            "From the place we sent him, he has returned!",
                            "He will have his revenge — on us all!"
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["Suddenly, a pale figure appears in the mirror."],
                        "is_stage_direction": True
                    }
                ]
            }
        }
    ]
}

# 第二幕
ACT_2 = {
    "zh": {
        "title": "致命的秘密",
        "subtitle": "Act II: The Deadly Secret"
    },
    "en": {
        "title": "The Deadly Secret",
        "subtitle": "Act II: The Deadly Secret"
    },
    "scenes": [
        {
            "zh": {
                "title": "尘封的往事",
                "subtitle": "Scene 1: The Buried Past",
                "stage_direction": "在城堡的地下密室中，Lord Blackwood面对着一件尘封已久的遗物。",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "这个戒指，我认识它！",
                            "是属于我兄弟的——那个我以为早已失踪的兄弟！",
                            "它怎么会在这里？",
                            "难道那个晚上发生的事情，并不像我记忆中那样？"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "回忆吧，哥哥，回忆那个夜晚...",
                            "当嫉妒蒙蔽了你的双眼，",
                            "当贪婪吞噬了你的良知，",
                            "你做了什么！"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "不可能！我只是...我只是...",
                            "那是一场意外！一场可怕的意外！"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["幽灵缓缓显现，正是他兄弟的面容。"],
                        "is_stage_direction": True
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "意外？",
                            "当你举起那沉重的烛台时，",
                            "当你看着我倒下时，",
                            "当你把我扔进那个黑暗的地窖时——",
                            "那也是意外吗？"
                        ]
                    }
                ]
            },
            "en": {
                "title": "The Buried Past",
                "subtitle": "Scene 1: The Buried Past",
                "stage_direction": "In the castle's underground chamber, Lord Blackwood faces a long-buried relic.",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "This ring, I know it!",
                            "It belonged to my brother — the one I thought had vanished long ago!",
                            "How can it be here?",
                            "Could what happened that night not be as I remember?"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "Remember, brother, remember that night...",
                            "When jealousy blinded your eyes,",
                            "When greed devoured your conscience,",
                            "What did you do!"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "Impossible! I only... I only...",
                            "It was an accident! A terrible accident!"
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["The ghost slowly materializes — it is his brother's face."],
                        "is_stage_direction": True
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "An accident?",
                            "When you raised that heavy candlestick,",
                            "When you watched me fall,",
                            "When you threw me into that dark cellar —",
                            "Was that also an accident?"
                        ]
                    }
                ]
            }
        }
    ]
}

# 第三幕
ACT_3 = {
    "zh": {
        "title": "疯狂的边缘",
        "subtitle": "Act III: The Brink of Madness"
    },
    "en": {
        "title": "The Brink of Madness",
        "subtitle": "Act III: The Brink of Madness"
    },
    "scenes": [
        {
            "zh": {
                "title": "盛宴上的幽灵",
                "subtitle": "Scene 1: The Ghost at the Feast",
                "stage_direction": "城堡大厅中正在举行一场阴郁的宴会。客人是Lady Elara，一位神秘的远方亲戚。",
                "dialogue": [
                    {
                        "character": "Lady Elara",
                        "text": [
                            "这座城堡真是壮观，",
                            "但空气中似乎弥漫着...悲伤。",
                            "这里发生过什么事吗？"
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "过去的事，最好让它过去，",
                            "有些回忆太沉重，无法承受。"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["突然，Lord Blackwood猛地站起来，盯着空荡荡的门口。"],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "你！你怎么敢！",
                            "我不是已经把你送走了吗？",
                            "从我的眼前消失！",
                            "从这所房子里消失！"
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "我亲爱的，你在和谁说话？",
                            "那里什么都没有。"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "什么都没有？你看不见他吗？",
                            "他就站在那里！浑身是血！",
                            "指着我！控诉我！"
                        ]
                    }
                ]
            },
            "en": {
                "title": "The Ghost at the Feast",
                "subtitle": "Scene 1: The Ghost at the Feast",
                "stage_direction": "A somber feast is held in the castle hall. The guest is Lady Elara, a mysterious distant relative.",
                "dialogue": [
                    {
                        "character": "Lady Elara",
                        "text": [
                            "This castle is truly magnificent,",
                            "But the air seems filled with... sorrow.",
                            "Has something happened here?"
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "What's past is best left in the past,",
                            "Some memories are too heavy to bear."
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["Suddenly, Lord Blackwood leaps to his feet, staring at the empty doorway."],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "You! How dare you!",
                            "Did I not send you away?",
                            "Disappear from my sight!",
                            "Leave this house!"
                        ]
                    },
                    {
                        "character": "Lady Blackwood",
                        "text": [
                            "My dear, who are you speaking to?",
                            "There is no one there."
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "No one? You cannot see him?",
                            "He stands right there! Covered in blood!",
                            "Pointing at me! Accusing me!"
                        ]
                    }
                ]
            }
        }
    ]
}

# 第四幕
ACT_4 = {
    "zh": {
        "title": "命运的陷阱",
        "subtitle": "Act IV: The Trap of Fate"
    },
    "en": {
        "title": "The Trap of Fate",
        "subtitle": "Act IV: The Trap of Fate"
    },
    "scenes": [
        {
            "zh": {
                "title": "神父的警告",
                "subtitle": "Scene 1: The Priest's Warning",
                "stage_direction": "",
                "dialogue": [
                    {
                        "character": "Father Benedict",
                        "text": [
                            "听我说，Lord Blackwood，听我说！",
                            "那恶灵不会满足于简单的恐吓，",
                            "它要的是你的灵魂，还有你全家的灵魂。",
                            "你必须忏悔！必须赎罪！"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "忏悔？在一切已经太晚之后？",
                            "我曾试图忘记，但它不让我忘记，",
                            "它在我的梦中纠缠，在我的酒中显形，",
                            "甚至在这神圣的地方也不放过我！"
                        ]
                    },
                    {
                        "character": "Father Benedict",
                        "text": [
                            "那么就离开吧！",
                            "离开这座被诅咒的城堡，",
                            "再也不要回来！",
                            "让时间来治愈这一切。"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "太迟了，神父，太迟了！",
                            "命运的罗网已经织就，",
                            "没有出口，没有逃脱，",
                            "只有...报应！"
                        ]
                    }
                ]
            },
            "en": {
                "title": "The Priest's Warning",
                "subtitle": "Scene 1: The Priest's Warning",
                "stage_direction": "",
                "dialogue": [
                    {
                        "character": "Father Benedict",
                        "text": [
                            "Listen to me, Lord Blackwood, listen!",
                            "That vengeful spirit will not be satisfied with mere intimidation,",
                            "It wants your soul, and the souls of your entire house.",
                            "You must confess! You must atone!"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "Confess? After everything is already too late?",
                            "I tried to forget, but it will not let me forget,",
                            "It haunts my dreams, appears in my wine,",
                            "And even in this holy place it will not release me!"
                        ]
                    },
                    {
                        "character": "Father Benedict",
                        "text": [
                            "Then leave!",
                            "Leave this cursed castle,",
                            "Never return!",
                            "Let time heal all."
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "Too late, father, too late!",
                            "Fate's web has already been woven,",
                            "There is no exit, no escape,",
                            "Only... retribution!"
                        ]
                    }
                ]
            }
        }
    ]
}

# 第五幕
ACT_5 = {
    "zh": {
        "title": "最终的审判",
        "subtitle": "Act V: The Final Judgment"
    },
    "en": {
        "title": "The Final Judgment",
        "subtitle": "Act V: The Final Judgment"
    },
    "scenes": [
        {
            "zh": {
                "title": "塔楼的结局",
                "subtitle": "Scene 1: The Tower's End",
                "stage_direction": "暴风雨夜，城堡最高的塔楼。雷声轰鸣，闪电照亮了黑暗的天空。",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "来吧！来吧，你这该死的幽灵！",
                            "我就在这里！你想要什么？",
                            "我的灵魂？拿去吧！",
                            "我已经厌倦了无休止的恐惧！"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "我要的不只是你的灵魂，哥哥，",
                            "我要的是真相大白！",
                            "我要你亲口承认你做了什么！"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "好！好！我承认！",
                            "是我杀了你！",
                            "因为我嫉妒你，嫉妒你的一切！",
                            "嫉妒父亲更爱你，嫉妒人们更尊敬你！"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["突然，一道闪电击中了塔楼，Lord Blackwood站在边缘，摇摇欲坠。"],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "现在你满意了吗？",
                            "我认罪了！你还想要什么？"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "我要的已经得到了——",
                            "你的良心已经醒来，",
                            "这才是最残酷的惩罚。",
                            "现在，愿你找到...安宁。"
                        ]
                    },
                    {
                        "character": "[舞台指示]",
                        "text": ["幽灵缓缓消散在晨曦中，Lord Blackwood独自一人站在塔楼上，望着远处的地平线。"],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": ["上帝啊，怜悯我这个罪人吧。"]
                    },
                    {
                        "character": "[剧终]",
                        "text": [],
                        "is_stage_direction": True
                    }
                ]
            },
            "en": {
                "title": "The Tower's End",
                "subtitle": "Scene 1: The Tower's End",
                "stage_direction": "A stormy night, atop the castle's highest tower. Thunder rumbles; lightning illuminates the dark sky.",
                "dialogue": [
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "Come! Come, you damned ghost!",
                            "Here I am! What do you want?",
                            "My soul? Take it!",
                            "I am weary of this endless fear!"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "It is not just your soul I want, brother,",
                            "I want the truth to be known!",
                            "I want you to confess with your own lips what you did!"
                        ]
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "Fine! Fine! I confess!",
                            "I killed you!",
                            "Because I envied you, envied everything about you!",
                            "Envied that Father loved you more, that people respected you more!"
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["Suddenly, lightning strikes the tower. Lord Blackwood stands at the edge, tottering."],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": [
                            "Are you satisfied now?",
                            "I have confessed! What more do you want?"
                        ]
                    },
                    {
                        "character": "The Ghost",
                        "text": [
                            "What I wanted has been obtained —",
                            "Your conscience has awakened,",
                            "This is the cruelest punishment.",
                            "Now, may you find... peace."
                        ]
                    },
                    {
                        "character": "[Stage Direction]",
                        "text": ["The ghost slowly fades in the dawn light. Lord Blackwood stands alone on the tower, gazing at the distant horizon."],
                        "is_stage_direction": True
                    },
                    {
                        "character": "Lord Blackwood",
                        "text": ["God, have mercy on this sinner."]
                    },
                    {
                        "character": "[THE END]",
                        "text": [],
                        "is_stage_direction": True
                    }
                ]
            }
        }
    ]
}

# 所有幕的列表
ALL_ACTS = [ACT_1, ACT_2, ACT_3, ACT_4, ACT_5]
