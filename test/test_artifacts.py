import numpy as np
import pandas as pd
import unittest


class LogSpecialArtifacts(unittest.TestCase):
    """docstring for log_images."""

    def setUp(self):
        pass
        # from segmind_track import set_experiment
        # set_experiment('f5082153-3ed2-40b6-a4c6-f4cd96b6cedc')

    def test_LogImage(self):
        from segmind_track import log_image

        log_image(
            key='panda.jpg',
            image='test_data/Kung_fu_panda_poster.jpg',
            step=0)

    def test_LogObjectdetection(self):
        from segmind_track import log_bbox_prediction

        bboxes = [[
            1358.99999999904, 573.00000000021, 1570.9999999996799,
            620.00000000019
        ],
                  [
                      535.9999999999679, 473.999999999472, 622.0000000000321,
                      511.999999999488
                  ],
                  [
                      1193.9999999993279, 675.0000000003779, 1270.999999999392,
                      712.000000000422
                  ],
                  [
                      1188.0000000006721, 774.000000000252, 1237.000000000608,
                      852.0000000002279
                  ],
                  [
                      1700.9999999993279, 581.0000000003639, 1783.999999999392,
                      616.000000000356
                  ],
                  [
                      1603.000000000032, 584.000000000496, 1681.999999999968,
                      616.000000000464
                  ],
                  [
                      1523.00000000064, 644.000000000004, 1595.00000000064,
                      678.999999999996
                  ]]

        log_bbox_prediction(
            key='DJI_0005-0151bbox_only.jpg',
            image='test_data/object_detection/DJI_0005-0151.jpg',
            bbox_pred=bboxes,
            bbox_gt=None,
            bbox_type='pascal_voc',
            step=None)

    def test_LogSemanticMask(self):
        from segmind_track import log_mask_prediction  # noqa: F401


class LogTables(unittest.TestCase):
    """docstring for log_tables."""

    def setUp(self):
        pass
        # from segmind_track import set_experiment
        # set_experiment('f5082153-3ed2-40b6-a4c6-f4cd96b6cedc')

    def test_Pandas(self):

        from segmind_track import log_table

        data = {
            'Int-Col': np.random.randint(low=2, size=10),
            'Float-Col': np.random.rand(10)
        }

        dataframe = pd.DataFrame.from_dict(data)

        log_table(key='test_table', table=dataframe, step=10)


if __name__ == '__main__':
    unittest.main()
