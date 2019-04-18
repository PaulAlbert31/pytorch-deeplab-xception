class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return '/data/semseg/samples/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        elif dataset == 'sbd':
            return '/data/semseg/samples/benchmark_RELEASE/'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/data/semseg/samples/'     # foler that contains leftImg8bit/
        elif dataset == 'coco':
            return '/data/semseg/samples/coco/'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
