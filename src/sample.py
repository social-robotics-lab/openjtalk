import jtalk

path = jtalk.make_wav("今日はいい天気ですね。こんな日はどこかに出かけたくなりますね。", speed=0.8, emotion='happy')
print(path)