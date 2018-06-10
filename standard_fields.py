class InputDataFields(object):

  image = 'image'
  original_image = 'original_image'
  key = 'key'
  source_id = 'source_id'
  filename = 'filename'
  groundtruth_image_classes = 'groundtruth_image_classes'
  groundtruth_boxes = 'groundtruth_boxes'
  groundtruth_classes = 'groundtruth_classes'
  groundtruth_label_types = 'groundtruth_label_types'
  groundtruth_is_crowd = 'groundtruth_is_crowd'
  groundtruth_area = 'groundtruth_area'
  groundtruth_difficult = 'groundtruth_difficult'
  groundtruth_group_of = 'groundtruth_group_of'
  proposal_boxes = 'proposal_boxes'
  proposal_objectness = 'proposal_objectness'
  groundtruth_instance_masks = 'groundtruth_instance_masks'
  groundtruth_instance_boundaries = 'groundtruth_instance_boundaries'
  groundtruth_instance_classes = 'groundtruth_instance_classes'
  groundtruth_keypoints = 'groundtruth_keypoints'
  groundtruth_keypoint_visibilities = 'groundtruth_keypoint_visibilities'
  groundtruth_label_scores = 'groundtruth_label_scores'
  groundtruth_weights = 'groundtruth_weights'
  num_groundtruth_boxes = 'num_groundtruth_boxes'
  true_image_shape = 'true_image_shape'
  verified_labels = 'verified_labels'
  multiclass_scores = 'multiclass_scores'


class DetectionResultFields(object):

  source_id = 'source_id'
  key = 'key'
  detection_boxes = 'detection_boxes'
  detection_scores = 'detection_scores'
  detection_classes = 'detection_classes'
  detection_masks = 'detection_masks'
  detection_boundaries = 'detection_boundaries'
  detection_keypoints = 'detection_keypoints'
  num_detections = 'num_detections'


class BoxListFields(object):

  boxes = 'boxes'
  classes = 'classes'
  scores = 'scores'
  weights = 'weights'
  objectness = 'objectness'
  masks = 'masks'
  boundaries = 'boundaries'
  keypoints = 'keypoints'
  keypoint_heatmaps = 'keypoint_heatmaps'


class TfExampleFields(object):

  image_encoded = 'image/encoded'
  image_format = 'image/format'
  filename = 'image/filename'
  channels = 'image/channels'
  colorspace = 'image/colorspace'
  height = 'image/height'
  width = 'image/width'
  source_id = 'image/source_id'
  object_class_text = 'image/object/class/text'
  object_class_label = 'image/object/class/label'
  object_bbox_ymin = 'image/object/bbox/ymin'
  object_bbox_xmin = 'image/object/bbox/xmin'
  object_bbox_ymax = 'image/object/bbox/ymax'
  object_bbox_xmax = 'image/object/bbox/xmax'
  object_view = 'image/object/view'
  object_truncated = 'image/object/truncated'
  object_occluded = 'image/object/occluded'
  object_difficult = 'image/object/difficult'
  object_group_of = 'image/object/group_of'
  object_depiction = 'image/object/depiction'
  object_is_crowd = 'image/object/is_crowd'
  object_segment_area = 'image/object/segment/area'
  object_weight = 'image/object/weight'
  instance_masks = 'image/segmentation/object'
  instance_boundaries = 'image/boundaries/object'
  instance_classes = 'image/segmentation/object/class'
  detection_class_label = 'image/detection/label'
  detection_bbox_ymin = 'image/detection/bbox/ymin'
  detection_bbox_xmin = 'image/detection/bbox/xmin'
  detection_bbox_ymax = 'image/detection/bbox/ymax'
  detection_bbox_xmax = 'image/detection/bbox/xmax'
  detection_score = 'image/detection/score'
