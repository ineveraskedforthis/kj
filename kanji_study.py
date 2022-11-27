import random

kanji_grade_1 = '一 九 七 二 人 入 八 力 十 下 三 千 上 口 土 夕 大 女 子 小 山 川 五 天 中 六 円 手 文 日 月 木 水 火 犬 王 正 出 本 右 四 左 玉 生 田 白 目 石 立 百 年 休 先 名 字 早 気 竹 糸 耳 虫 村 男 町 花 見 貝 赤 足 車 学 林 空 金 雨 青 草 音 校 森'.split(' ')

kanji_grade_2 = '刀 万 丸 才 工 弓 内 午 少 元 今 公 分 切 友 太 引 心 戸 方 止 毛 父 牛 半 市 北 古 台 兄 冬 外 広 母 用 矢 交 会 合 同 回 寺 地 多 光 当 毎 池 米 羽 考 肉 自 色 行 西 来 何 作 体 弟 図 声 売 形 汽 社 角 言 谷 走 近 里 麦 画 東 京 夜 直 国 姉 妹 岩 店 明 歩 知 長 門 昼 '.split(' ')
number = int(input('Amount of kanji: '))
print(random.sample(kanji_grade_1 + kanji_grade_2, number))

input('Press any Enter to close')
