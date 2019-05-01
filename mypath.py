class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return '/data/semseg/samples/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        if dataset == 'pascal-scribbles':
            return '/data/semseg/samples/VOCdevkit/VOC2012/pascal_scribble/' # contains .png scribble annotations
        elif dataset == 'sbd':
            return '/data/semseg/samples/benchmark_RELEASE/'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/data/semseg/samples/'     # folder that contains leftImg8bit/
        elif dataset == 'coco':
            return '/data/semseg/samples/coco/'
        elif dataset == 'ade20k':
            return '/data/semseg/samples/ADEChallengeData2016/' # download from data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
