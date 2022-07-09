import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube,com/channel/UCxppsdkNilX4u6PADQFnQA" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#2EFE9A", "#2EFEC8"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "조성걸")
write("description", "설명")
write("button", "유튜브")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "1": "동물 좋아함",
  "2": "손으로 뭔가 하는 걸 좋아함",
  "3": "그런데 손재주가 좋지는 않음",
  "4": "사교성 별로 안 좋은 편"
}
information(informations)