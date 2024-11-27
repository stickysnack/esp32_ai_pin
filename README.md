# esp32_ai_pin

DEV日志：
11/26
验证功能，完成esp32传输图像功能。存在存在色彩空间问题。目前使用jpeg依然存在照片偏绿且对焦困难的问题。并且esp32c3并不支持rgb666与888，wired.
但是似乎并不影响tesseract验证ocr,虽然效果不如openai(怀疑也是云端调用opencv),本地1m生成只需0.5s,很nice。
现在尝试处理图像（锐化，白平衡，对焦）并且尝试将其输出到移动端。

but why??为什么会一直是绿色？

DEV日志：
11/27
正在解决接入llm，尝试三种方法：ts，python以及curl.最后选择curl,因为免除后段flack框架以及服务器需求（并不存在高并发需求，并且预估esp32 S3理论应该足以handle case..
目前实现：ocr,识别物体，摄像保存。


