import torch
from torchvision.models.detection import faster_rcnn, fasterrcnn_resnet50_fpn


def get_model_instance_segmentation(num_classes):
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = faster_rcnn.FastRCNNPredictor(in_features, num_classes)

    return model


def save_model(model):
    torch.save(model.state_dict(), 'rcnn.pt')


def load_model(num_classes, device):
    model = get_model_instance_segmentation(num_classes)
    model.load_state_dict(torch.load('model.pt'))
    model.eval()
    model.to(device)
    return model