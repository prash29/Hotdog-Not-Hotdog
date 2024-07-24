import tensorflow as tf
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

input_layer = 'DecodeJpeg/contents:0'
output_layer = 'final_result:0'

#Reading Image data from command line argument
image = tf.oi.gfile.FastGFile(sys.argv[1], 'rb').read()

#Reading labels file
labels = [line.rstrip() for line in tf.gfile.GFile("labels_hotdog.txt")]
with tf.gfile.FastGFile("graph_hotdog.pb", 'rb') as f:
    g_def = tf.GraphDef()
    g_def.ParseFromString(f.read())
    tf.import_graph_def(g_def, name='')

with tf.Session() as sess:
    soft_tensor=sess.graph.get_tensor_by_name(output_layer)
    predict, = sess.run(soft_tensor, {input_layer: image})
    top = predict.argsort()[-2:][::-1]
    for x in top:
        result = labels[x]
        score = predict[x]
        print('%s  =  %.5f ' % (result, score))
