python ./externals/yolov7_seg/seg/train.py --workers 8 --batch-size 2 --data ./data/leaf_seg/data.yaml --img 640 --cfg ./externals/yolov7/cfg/training/yolov7-leaf_seg.yaml --name yolov7-leaf_seg --hyp ./externals/yolov7/data/hyp.scratch.leaf_seg.yaml