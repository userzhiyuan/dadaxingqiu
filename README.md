# dadaxingqiu


支付宝答答星球自动答题
python,adb,Android，baidu-aip

启动程序<br>
python ddxq.py<br>
strlist #为答案列表，现在答答星球到lv6时题库更新，没有lv6的题库，如果自己有收集的答案可以统计加入到列表中，正确率在90%，<br>

原理是将所有答案对图片中识别出的每行做对比，如果作案包含在识别出的文字中就云点击这个文字的坐标。有可能会了出现相同的答案，但是选项不一，这时可能会错。<br>

最好的作法是<br>
1,对每lv中的题库正确案答做统计<br>
2,按答案坐标识别

test one
test two
