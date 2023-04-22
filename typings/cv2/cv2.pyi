from collections.abc import Sequence
from typing import ClassVar, Union, overload

from _typeshed import Incomplete
from cv2 import Mat, _MatF
from cv2.gapi.streaming import queue_capacity
from typing_extensions import TypeAlias

# Y047 & Y018 (Unused TypeAlias and TypeVar): Helper types reused everywhere.
# The noqa comments won't be necessary when types in this module are more complete and use the aliases

# Function argument types
# Convertable to boolean
_Boolean: TypeAlias = bool | int | None
# "a scalar"
_NumericScalar: TypeAlias = float | bool | None
# cv::Scalar
_Scalar: TypeAlias = Mat | _NumericScalar | Sequence[_NumericScalar]
# cv::TermCriteria
_TermCriteria: TypeAlias = Union[tuple[int, int, float], Sequence[float]]  # noqa: Y047
# cv::Point<int>
_Point: TypeAlias = Union[tuple[int, int], Sequence[int]]
# cv::Size<int>
_Size: TypeAlias = Union[tuple[int, int], Sequence[int]]
# cv::Range<int>
_Range: TypeAlias = Union[tuple[int, int], Sequence[int]]
# cv::Point<float>
_PointFloat: TypeAlias = Union[tuple[float, float], Sequence[float]]
# cv::Size<float>
_SizeFloat: TypeAlias = Union[tuple[float, float], Sequence[float]]
# cv::Rect<int>
_Rect: TypeAlias = Union[tuple[int, int, int, int], Sequence[int]]
# cv::Rect<float>
_RectFloat: TypeAlias = Union[tuple[int, int, int, int], Sequence[int]]  # noqa: Y047
# cv::RotatedRect
_RotatedRect: TypeAlias = Union[tuple[_PointFloat, _SizeFloat, float], Sequence[_PointFloat | _SizeFloat | float]]  # noqa: Y047
_RotatedRectResult: TypeAlias = tuple[tuple[float, float], tuple[float, float], float]
# cv:UMat, cv::InputArray, cv::OutputArray and cv::InputOutputArray
_UMat: TypeAlias = UMat | _MatF | _NumericScalar

# TODO: Complete types until all the aliases below are gone!
# These are temporary placeholder return types, as were in the docstrings signatures from microsoft/python-type-stubs
# This is often (but not always) a sign that a TypeVar should be used to return the same type as a param.
# retval is equivalent to Unknown
_flow: TypeAlias = Incomplete  # noqa: Y042
_image: TypeAlias = Incomplete  # noqa: Y042
_edgeList: TypeAlias = Incomplete  # noqa: Y042
_leadingEdgeList: TypeAlias = Incomplete  # noqa: Y042
_triangleList: TypeAlias = Incomplete  # noqa: Y042
_matches_info: TypeAlias = Incomplete  # noqa: Y042
_arg3: TypeAlias = Incomplete  # noqa: Y042
_outputBlobs: TypeAlias = Incomplete  # noqa: Y042
_layersTypes: TypeAlias = Incomplete  # noqa: Y042
_detections: TypeAlias = Incomplete  # noqa: Y042
_results: TypeAlias = Incomplete  # noqa: Y042
_corners: TypeAlias = Incomplete  # noqa: Y042
_pts: TypeAlias = Incomplete  # noqa: Y042
_dst: TypeAlias = Incomplete  # noqa: Y042
_markers: TypeAlias = Incomplete  # noqa: Y042
_masks: TypeAlias = Incomplete  # noqa: Y042
_window: TypeAlias = Incomplete  # noqa: Y042
_edges: TypeAlias = Incomplete  # noqa: Y042
_lowerBound: TypeAlias = Incomplete  # noqa: Y042
_circles: TypeAlias = Incomplete  # noqa: Y042
_lines: TypeAlias = Incomplete  # noqa: Y042
_hu: TypeAlias = Incomplete  # noqa: Y042
_points2f: TypeAlias = Incomplete  # noqa: Y042
_keypoints: TypeAlias = Incomplete  # noqa: Y042
_mean: TypeAlias = Incomplete  # noqa: Y042
_eigenvectors: TypeAlias = Incomplete  # noqa: Y042
_eigenvalues: TypeAlias = Incomplete  # noqa: Y042
_result: TypeAlias = Incomplete  # noqa: Y042
_mtxR: TypeAlias = Incomplete  # noqa: Y042
_mtxQ: TypeAlias = Incomplete  # noqa: Y042
_Qx: TypeAlias = Incomplete
_Qy: TypeAlias = Incomplete
_Qz: TypeAlias = Incomplete
_jacobian: TypeAlias = Incomplete  # noqa: Y042
_w: TypeAlias = Incomplete  # noqa: Y042
_u: TypeAlias = Incomplete  # noqa: Y042
_vt: TypeAlias = Incomplete  # noqa: Y042
_approxCurve: TypeAlias = Incomplete  # noqa: Y042
_img: TypeAlias = Incomplete  # noqa: Y042
_dist: TypeAlias = Incomplete  # noqa: Y042
_nidx: TypeAlias = Incomplete  # noqa: Y042
_points: TypeAlias = Incomplete  # noqa: Y042
_pyramid: TypeAlias = Incomplete  # noqa: Y042
_covar: TypeAlias = Incomplete  # noqa: Y042
_nextPts: TypeAlias = Incomplete  # noqa: Y042
_status: TypeAlias = Incomplete  # noqa: Y042
_err: TypeAlias = Incomplete  # noqa: Y042
_cameraMatrix: TypeAlias = Incomplete  # noqa: Y042
_distCoeffs: TypeAlias = Incomplete  # noqa: Y042
_rvecs: TypeAlias = Incomplete  # noqa: Y042
_tvecs: TypeAlias = Incomplete  # noqa: Y042
_stdDeviationsIntrinsics: TypeAlias = Incomplete  # noqa: Y042
_stdDeviationsExtrinsics: TypeAlias = Incomplete  # noqa: Y042
_perViewErrors: TypeAlias = Incomplete  # noqa: Y042
_newObjPoints: TypeAlias = Incomplete  # noqa: Y042
_stdDeviationsObjPoints: TypeAlias = Incomplete  # noqa: Y042
_R_cam2gripper: TypeAlias = Incomplete
_t_cam2gripper: TypeAlias = Incomplete  # noqa: Y042
_fovx: TypeAlias = Incomplete  # noqa: Y042
_fovy: TypeAlias = Incomplete  # noqa: Y042
_focalLength: TypeAlias = Incomplete  # noqa: Y042
_principalPoint: TypeAlias = Incomplete  # noqa: Y042
_aspectRatio: TypeAlias = Incomplete  # noqa: Y042
_magnitude: TypeAlias = Incomplete  # noqa: Y042
_angle: TypeAlias = Incomplete  # noqa: Y042
_pt1: TypeAlias = Incomplete  # noqa: Y042
_pt2: TypeAlias = Incomplete  # noqa: Y042
_pos: TypeAlias = Incomplete  # noqa: Y042
_m: TypeAlias = Incomplete  # noqa: Y042
_rvec3: TypeAlias = Incomplete  # noqa: Y042
_tvec3: TypeAlias = Incomplete  # noqa: Y042
_dr3dr1: TypeAlias = Incomplete  # noqa: Y042
_dr3dt1: TypeAlias = Incomplete  # noqa: Y042
_dr3dr2: TypeAlias = Incomplete  # noqa: Y042
_dr3dt2: TypeAlias = Incomplete  # noqa: Y042
_dt3dr1: TypeAlias = Incomplete  # noqa: Y042
_dt3dt1: TypeAlias = Incomplete  # noqa: Y042
_dt3dr2: TypeAlias = Incomplete  # noqa: Y042
_dt3dt2: TypeAlias = Incomplete  # noqa: Y042
_labels: TypeAlias = Incomplete  # noqa: Y042
_stats: TypeAlias = Incomplete  # noqa: Y042
_centroids: TypeAlias = Incomplete  # noqa: Y042
_dstmap1: TypeAlias = Incomplete  # noqa: Y042
_dstmap2: TypeAlias = Incomplete  # noqa: Y042
_hull: TypeAlias = Incomplete  # noqa: Y042
_convexityDefects: TypeAlias = Incomplete  # noqa: Y042
_newPoints1: TypeAlias = Incomplete  # noqa: Y042
_newPoints2: TypeAlias = Incomplete  # noqa: Y042
_grayscale: TypeAlias = Incomplete  # noqa: Y042
_color_boost: TypeAlias = Incomplete  # noqa: Y042
_R1: TypeAlias = Incomplete
_R2: TypeAlias = Incomplete
_t: TypeAlias = Incomplete  # noqa: Y042
_rotations: TypeAlias = Incomplete  # noqa: Y042
_translations: TypeAlias = Incomplete  # noqa: Y042
_normals: TypeAlias = Incomplete  # noqa: Y042
_rotMatrix: TypeAlias = Incomplete  # noqa: Y042
_transVect: TypeAlias = Incomplete  # noqa: Y042
_rotMatrixX: TypeAlias = Incomplete  # noqa: Y042
_rotMatrixY: TypeAlias = Incomplete  # noqa: Y042
_rotMatrixZ: TypeAlias = Incomplete  # noqa: Y042
_eulerAngles: TypeAlias = Incomplete  # noqa: Y042
_outImage: TypeAlias = Incomplete  # noqa: Y042
_outImg: TypeAlias = Incomplete  # noqa: Y042
_inliers: TypeAlias = Incomplete  # noqa: Y042
_out: TypeAlias = Incomplete  # noqa: Y042
_sharpness: TypeAlias = Incomplete  # noqa: Y042
_possibleSolutions: TypeAlias = Incomplete  # noqa: Y042
_buf: TypeAlias = Incomplete  # noqa: Y042
_meta: TypeAlias = Incomplete  # noqa: Y042
_centers: TypeAlias = Incomplete  # noqa: Y042
_contours: TypeAlias = Incomplete  # noqa: Y042
_hierarchy: TypeAlias = Incomplete  # noqa: Y042
_mask: TypeAlias = Incomplete  # noqa: Y042
_idx: TypeAlias = Incomplete  # noqa: Y042
_warpMatrix: TypeAlias = Incomplete  # noqa: Y042
_line: TypeAlias = Incomplete  # noqa: Y042
_rect: TypeAlias = Incomplete  # noqa: Y042
_kx: TypeAlias = Incomplete  # noqa: Y042
_ky: TypeAlias = Incomplete  # noqa: Y042
_validPixROI: TypeAlias = Incomplete  # noqa: Y042
_patch: TypeAlias = Incomplete  # noqa: Y042
_baseLine: TypeAlias = Incomplete  # noqa: Y042
_bgdModel: TypeAlias = Incomplete  # noqa: Y042
_fgdModel: TypeAlias = Incomplete  # noqa: Y042
_rectList: TypeAlias = Incomplete  # noqa: Y042
_weights: TypeAlias = Incomplete  # noqa: Y042
_mats: TypeAlias = Incomplete  # noqa: Y042
_map1: TypeAlias = Incomplete  # noqa: Y042
_map2: TypeAlias = Incomplete  # noqa: Y042
_sum: TypeAlias = Incomplete  # noqa: Y042
_sqsum: TypeAlias = Incomplete  # noqa: Y042
_tilted: TypeAlias = Incomplete  # noqa: Y042
_p12: TypeAlias = Incomplete  # noqa: Y042
_iM: TypeAlias = Incomplete  # noqa: Y042
_bestLabels: TypeAlias = Incomplete  # noqa: Y042
_dABdA: TypeAlias = Incomplete  # noqa: Y042
_dABdB: TypeAlias = Incomplete  # noqa: Y042
_stddev: TypeAlias = Incomplete  # noqa: Y042
_center: TypeAlias = Incomplete  # noqa: Y042
_radius: TypeAlias = Incomplete  # noqa: Y042
_triangle: TypeAlias = Incomplete  # noqa: Y042
_c: TypeAlias = Incomplete  # noqa: Y042
_a: TypeAlias = Incomplete  # noqa: Y042
_dst1: TypeAlias = Incomplete  # noqa: Y042
_dst2: TypeAlias = Incomplete  # noqa: Y042
_response: TypeAlias = Incomplete  # noqa: Y042
_x: TypeAlias = Incomplete  # noqa: Y042
_y: TypeAlias = Incomplete  # noqa: Y042
_imagePoints: TypeAlias = Incomplete  # noqa: Y042
_R: TypeAlias = Incomplete
_R3: TypeAlias = Incomplete
_P1: TypeAlias = Incomplete
_P2: TypeAlias = Incomplete
_P3: TypeAlias = Incomplete
_Q: TypeAlias = Incomplete
_roi1: TypeAlias = Incomplete  # noqa: Y042
_roi2: TypeAlias = Incomplete  # noqa: Y042
_3dImage: TypeAlias = Incomplete
_intersectingRegion: TypeAlias = Incomplete  # noqa: Y042
_blend: TypeAlias = Incomplete  # noqa: Y042
_boundingBoxes: TypeAlias = Incomplete  # noqa: Y042
_mtx: TypeAlias = Incomplete  # noqa: Y042
_roots: TypeAlias = Incomplete  # noqa: Y042
_z: TypeAlias = Incomplete  # noqa: Y042
_rvec: TypeAlias = Incomplete  # noqa: Y042
_tvec: TypeAlias = Incomplete  # noqa: Y042
_reprojectionError: TypeAlias = Incomplete  # noqa: Y042
_dx: TypeAlias = Incomplete  # noqa: Y042
_dy: TypeAlias = Incomplete  # noqa: Y042
_mv: TypeAlias = Incomplete  # noqa: Y042
_cameraMatrix1: TypeAlias = Incomplete  # noqa: Y042
_distCoeffs1: TypeAlias = Incomplete  # noqa: Y042
_cameraMatrix2: TypeAlias = Incomplete  # noqa: Y042
_distCoeffs2: TypeAlias = Incomplete  # noqa: Y042
_T: TypeAlias = Incomplete
_E: TypeAlias = Incomplete
_F: TypeAlias = Incomplete
_validPixROI1: TypeAlias = Incomplete  # noqa: Y042
_validPixROI2: TypeAlias = Incomplete  # noqa: Y042
_H1: TypeAlias = Incomplete
_H2: TypeAlias = Incomplete
_points4D: TypeAlias = Incomplete  # noqa: Y042
_disparity: TypeAlias = Incomplete  # noqa: Y042
_triangulatedPoints: TypeAlias = Incomplete  # noqa: Y042

__version__: str

ACCESS_FAST: int
ACCESS_MASK: int
ACCESS_READ: int
ACCESS_RW: int
ACCESS_WRITE: int
ADAPTIVE_THRESH_GAUSSIAN_C: int
ADAPTIVE_THRESH_MEAN_C: int
AGAST_FEATURE_DETECTOR_AGAST_5_8: int
AGAST_FEATURE_DETECTOR_AGAST_7_12D: int
AGAST_FEATURE_DETECTOR_AGAST_7_12S: int
AGAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION: int
AGAST_FEATURE_DETECTOR_OAST_9_16: int
AGAST_FEATURE_DETECTOR_THRESHOLD: int
AKAZE_DESCRIPTOR_KAZE: int
AKAZE_DESCRIPTOR_KAZE_UPRIGHT: int
AKAZE_DESCRIPTOR_MLDB: int
AKAZE_DESCRIPTOR_MLDB_UPRIGHT: int
AgastFeatureDetector_AGAST_5_8: int
AgastFeatureDetector_AGAST_7_12d: int
AgastFeatureDetector_AGAST_7_12s: int
AgastFeatureDetector_NONMAX_SUPPRESSION: int
AgastFeatureDetector_OAST_9_16: int
AgastFeatureDetector_THRESHOLD: int
BORDER_CONSTANT: int
BORDER_DEFAULT: int
BORDER_ISOLATED: int
BORDER_REFLECT: int
BORDER_REFLECT101: int
BORDER_REFLECT_101: int
BORDER_REPLICATE: int
BORDER_TRANSPARENT: int
BORDER_WRAP: int
CALIB_CB_ACCURACY: int
CALIB_CB_ADAPTIVE_THRESH: int
CALIB_CB_ASYMMETRIC_GRID: int
CALIB_CB_CLUSTERING: int
CALIB_CB_EXHAUSTIVE: int
CALIB_CB_FAST_CHECK: int
CALIB_CB_FILTER_QUADS: int
CALIB_CB_LARGER: int
CALIB_CB_MARKER: int
CALIB_CB_NORMALIZE_IMAGE: int
CALIB_CB_SYMMETRIC_GRID: int
CALIB_FIX_ASPECT_RATIO: int
CALIB_FIX_FOCAL_LENGTH: int
CALIB_FIX_INTRINSIC: int
CALIB_FIX_K1: int
CALIB_FIX_K2: int
CALIB_FIX_K3: int
CALIB_FIX_K4: int
CALIB_FIX_K5: int
CALIB_FIX_K6: int
CALIB_FIX_PRINCIPAL_POINT: int
CALIB_FIX_S1_S2_S3_S4: int
CALIB_FIX_TANGENT_DIST: int
CALIB_FIX_TAUX_TAUY: int
CALIB_HAND_EYE_ANDREFF: int
CALIB_HAND_EYE_DANIILIDIS: int
CALIB_HAND_EYE_HORAUD: int
CALIB_HAND_EYE_PARK: int
CALIB_HAND_EYE_TSAI: int
CALIB_NINTRINSIC: int
CALIB_RATIONAL_MODEL: int
CALIB_ROBOT_WORLD_HAND_EYE_LI: int
CALIB_ROBOT_WORLD_HAND_EYE_SHAH: int
CALIB_SAME_FOCAL_LENGTH: int
CALIB_THIN_PRISM_MODEL: int
CALIB_TILTED_MODEL: int
CALIB_USE_EXTRINSIC_GUESS: int
CALIB_USE_INTRINSIC_GUESS: int
CALIB_USE_LU: int
CALIB_USE_QR: int
CALIB_ZERO_DISPARITY: int
CALIB_ZERO_TANGENT_DIST: int
CAP_ANDROID: int
CAP_ANY: int
CAP_ARAVIS: int
CAP_AVFOUNDATION: int
CAP_CMU1394: int
CAP_DC1394: int
CAP_DSHOW: int
CAP_FFMPEG: int
CAP_FIREWARE: int
CAP_FIREWIRE: int
CAP_GIGANETIX: int
CAP_GPHOTO2: int
CAP_GSTREAMER: int
CAP_IEEE1394: int
CAP_IMAGES: int
CAP_INTELPERC: int
CAP_INTELPERC_DEPTH_GENERATOR: int
CAP_INTELPERC_DEPTH_MAP: int
CAP_INTELPERC_GENERATORS_MASK: int
CAP_INTELPERC_IMAGE: int
CAP_INTELPERC_IMAGE_GENERATOR: int
CAP_INTELPERC_IR_GENERATOR: int
CAP_INTELPERC_IR_MAP: int
CAP_INTELPERC_UVDEPTH_MAP: int
CAP_INTEL_MFX: int
CAP_MSMF: int
CAP_OPENCV_MJPEG: int
CAP_OPENNI: int
CAP_OPENNI2: int
CAP_OPENNI2_ASTRA: int
CAP_OPENNI2_ASUS: int
CAP_OPENNI_ASUS: int
CAP_OPENNI_BGR_IMAGE: int
CAP_OPENNI_DEPTH_GENERATOR: int
CAP_OPENNI_DEPTH_GENERATOR_BASELINE: int
CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH: int
CAP_OPENNI_DEPTH_GENERATOR_PRESENT: int
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION: int
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION_ON: int
CAP_OPENNI_DEPTH_MAP: int
CAP_OPENNI_DISPARITY_MAP: int
CAP_OPENNI_DISPARITY_MAP_32F: int
CAP_OPENNI_GENERATORS_MASK: int
CAP_OPENNI_GRAY_IMAGE: int
CAP_OPENNI_IMAGE_GENERATOR: int
CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE: int
CAP_OPENNI_IMAGE_GENERATOR_PRESENT: int
CAP_OPENNI_IR_GENERATOR: int
CAP_OPENNI_IR_GENERATOR_PRESENT: int
CAP_OPENNI_IR_IMAGE: int
CAP_OPENNI_POINT_CLOUD_MAP: int
CAP_OPENNI_QVGA_30HZ: int
CAP_OPENNI_QVGA_60HZ: int
CAP_OPENNI_SXGA_15HZ: int
CAP_OPENNI_SXGA_30HZ: int
CAP_OPENNI_VALID_DEPTH_MASK: int
CAP_OPENNI_VGA_30HZ: int
CAP_PROP_APERTURE: int
CAP_PROP_ARAVIS_AUTOTRIGGER: int
CAP_PROP_AUDIO_BASE_INDEX: int
CAP_PROP_AUDIO_DATA_DEPTH: int
CAP_PROP_AUDIO_POS: int
CAP_PROP_AUDIO_SAMPLES_PER_SECOND: int
CAP_PROP_AUDIO_SHIFT_NSEC: int
CAP_PROP_AUDIO_STREAM: int
CAP_PROP_AUDIO_SYNCHRONIZE: int
CAP_PROP_AUDIO_TOTAL_CHANNELS: int
CAP_PROP_AUDIO_TOTAL_STREAMS: int
CAP_PROP_AUTOFOCUS: int
CAP_PROP_AUTO_EXPOSURE: int
CAP_PROP_AUTO_WB: int
CAP_PROP_BACKEND: int
CAP_PROP_BACKLIGHT: int
CAP_PROP_BITRATE: int
CAP_PROP_BRIGHTNESS: int
CAP_PROP_BUFFERSIZE: int
CAP_PROP_CHANNEL: int
CAP_PROP_CODEC_EXTRADATA_INDEX: int
CAP_PROP_CODEC_PIXEL_FORMAT: int
CAP_PROP_CONTRAST: int
CAP_PROP_CONVERT_RGB: int
CAP_PROP_DC1394_MAX: int
CAP_PROP_DC1394_MODE_AUTO: int
CAP_PROP_DC1394_MODE_MANUAL: int
CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO: int
CAP_PROP_DC1394_OFF: int
CAP_PROP_EXPOSURE: int
CAP_PROP_EXPOSUREPROGRAM: int
CAP_PROP_FOCUS: int
CAP_PROP_FORMAT: int
CAP_PROP_FOURCC: int
CAP_PROP_FPS: int
CAP_PROP_FRAME_COUNT: int
CAP_PROP_FRAME_HEIGHT: int
CAP_PROP_FRAME_WIDTH: int
CAP_PROP_GAIN: int
CAP_PROP_GAMMA: int
CAP_PROP_GIGA_FRAME_HEIGH_MAX: int
CAP_PROP_GIGA_FRAME_OFFSET_X: int
CAP_PROP_GIGA_FRAME_OFFSET_Y: int
CAP_PROP_GIGA_FRAME_SENS_HEIGH: int
CAP_PROP_GIGA_FRAME_SENS_WIDTH: int
CAP_PROP_GIGA_FRAME_WIDTH_MAX: int
CAP_PROP_GPHOTO2_COLLECT_MSGS: int
CAP_PROP_GPHOTO2_FLUSH_MSGS: int
CAP_PROP_GPHOTO2_PREVIEW: int
CAP_PROP_GPHOTO2_RELOAD_CONFIG: int
CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE: int
CAP_PROP_GPHOTO2_WIDGET_ENUMERATE: int
CAP_PROP_GSTREAMER_QUEUE_LENGTH: int
CAP_PROP_GUID: int
CAP_PROP_HUE: int
CAP_PROP_HW_ACCELERATION: int
CAP_PROP_HW_ACCELERATION_USE_OPENCL: int
CAP_PROP_HW_DEVICE: int
CAP_PROP_IMAGES_BASE: int
CAP_PROP_IMAGES_LAST: int
CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD: int
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ: int
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT: int
CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE: int
CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE: int
CAP_PROP_INTELPERC_PROFILE_COUNT: int
CAP_PROP_INTELPERC_PROFILE_IDX: int
CAP_PROP_IOS_DEVICE_EXPOSURE: int
CAP_PROP_IOS_DEVICE_FLASH: int
CAP_PROP_IOS_DEVICE_FOCUS: int
CAP_PROP_IOS_DEVICE_TORCH: int
CAP_PROP_IOS_DEVICE_WHITEBALANCE: int
CAP_PROP_IRIS: int
CAP_PROP_ISO_SPEED: int
CAP_PROP_LRF_HAS_KEY_FRAME: int
CAP_PROP_MODE: int
CAP_PROP_MONOCHROME: int
CAP_PROP_OPENNI2_MIRROR: int
CAP_PROP_OPENNI2_SYNC: int
CAP_PROP_OPENNI_APPROX_FRAME_SYNC: int
CAP_PROP_OPENNI_BASELINE: int
CAP_PROP_OPENNI_CIRCLE_BUFFER: int
CAP_PROP_OPENNI_FOCAL_LENGTH: int
CAP_PROP_OPENNI_FRAME_MAX_DEPTH: int
CAP_PROP_OPENNI_GENERATOR_PRESENT: int
CAP_PROP_OPENNI_MAX_BUFFER_SIZE: int
CAP_PROP_OPENNI_MAX_TIME_DURATION: int
CAP_PROP_OPENNI_OUTPUT_MODE: int
CAP_PROP_OPENNI_REGISTRATION: int
CAP_PROP_OPENNI_REGISTRATION_ON: int
CAP_PROP_OPEN_TIMEOUT_MSEC: int
CAP_PROP_ORIENTATION_AUTO: int
CAP_PROP_ORIENTATION_META: int
CAP_PROP_PAN: int
CAP_PROP_POS_AVI_RATIO: int
CAP_PROP_POS_FRAMES: int
CAP_PROP_POS_MSEC: int
CAP_PROP_PVAPI_BINNINGX: int
CAP_PROP_PVAPI_BINNINGY: int
CAP_PROP_PVAPI_DECIMATIONHORIZONTAL: int
CAP_PROP_PVAPI_DECIMATIONVERTICAL: int
CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE: int
CAP_PROP_PVAPI_MULTICASTIP: int
CAP_PROP_PVAPI_PIXELFORMAT: int
CAP_PROP_READ_TIMEOUT_MSEC: int
CAP_PROP_RECTIFICATION: int
CAP_PROP_ROLL: int
CAP_PROP_SAR_DEN: int
CAP_PROP_SAR_NUM: int
CAP_PROP_SATURATION: int
CAP_PROP_SETTINGS: int
CAP_PROP_SHARPNESS: int
CAP_PROP_SPEED: int
CAP_PROP_STREAM_OPEN_TIME_USEC: int
CAP_PROP_TEMPERATURE: int
CAP_PROP_TILT: int
CAP_PROP_TRIGGER: int
CAP_PROP_TRIGGER_DELAY: int
CAP_PROP_VIDEO_STREAM: int
CAP_PROP_VIDEO_TOTAL_CHANNELS: int
CAP_PROP_VIEWFINDER: int
CAP_PROP_WB_TEMPERATURE: int
CAP_PROP_WHITE_BALANCE_BLUE_U: int
CAP_PROP_WHITE_BALANCE_RED_V: int
CAP_PROP_XI_ACQ_BUFFER_SIZE: int
CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT: int
CAP_PROP_XI_ACQ_FRAME_BURST_COUNT: int
CAP_PROP_XI_ACQ_TIMING_MODE: int
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT: int
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE: int
CAP_PROP_XI_AEAG: int
CAP_PROP_XI_AEAG_LEVEL: int
CAP_PROP_XI_AEAG_ROI_HEIGHT: int
CAP_PROP_XI_AEAG_ROI_OFFSET_X: int
CAP_PROP_XI_AEAG_ROI_OFFSET_Y: int
CAP_PROP_XI_AEAG_ROI_WIDTH: int
CAP_PROP_XI_AE_MAX_LIMIT: int
CAP_PROP_XI_AG_MAX_LIMIT: int
CAP_PROP_XI_APPLY_CMS: int
CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION: int
CAP_PROP_XI_AUTO_WB: int
CAP_PROP_XI_AVAILABLE_BANDWIDTH: int
CAP_PROP_XI_BINNING_HORIZONTAL: int
CAP_PROP_XI_BINNING_PATTERN: int
CAP_PROP_XI_BINNING_SELECTOR: int
CAP_PROP_XI_BINNING_VERTICAL: int
CAP_PROP_XI_BPC: int
CAP_PROP_XI_BUFFERS_QUEUE_SIZE: int
CAP_PROP_XI_BUFFER_POLICY: int
CAP_PROP_XI_CC_MATRIX_00: int
CAP_PROP_XI_CC_MATRIX_01: int
CAP_PROP_XI_CC_MATRIX_02: int
CAP_PROP_XI_CC_MATRIX_03: int
CAP_PROP_XI_CC_MATRIX_10: int
CAP_PROP_XI_CC_MATRIX_11: int
CAP_PROP_XI_CC_MATRIX_12: int
CAP_PROP_XI_CC_MATRIX_13: int
CAP_PROP_XI_CC_MATRIX_20: int
CAP_PROP_XI_CC_MATRIX_21: int
CAP_PROP_XI_CC_MATRIX_22: int
CAP_PROP_XI_CC_MATRIX_23: int
CAP_PROP_XI_CC_MATRIX_30: int
CAP_PROP_XI_CC_MATRIX_31: int
CAP_PROP_XI_CC_MATRIX_32: int
CAP_PROP_XI_CC_MATRIX_33: int
CAP_PROP_XI_CHIP_TEMP: int
CAP_PROP_XI_CMS: int
CAP_PROP_XI_COLOR_FILTER_ARRAY: int
CAP_PROP_XI_COLUMN_FPN_CORRECTION: int
CAP_PROP_XI_COOLING: int
CAP_PROP_XI_COUNTER_SELECTOR: int
CAP_PROP_XI_COUNTER_VALUE: int
CAP_PROP_XI_DATA_FORMAT: int
CAP_PROP_XI_DEBOUNCE_EN: int
CAP_PROP_XI_DEBOUNCE_POL: int
CAP_PROP_XI_DEBOUNCE_T0: int
CAP_PROP_XI_DEBOUNCE_T1: int
CAP_PROP_XI_DEBUG_LEVEL: int
CAP_PROP_XI_DECIMATION_HORIZONTAL: int
CAP_PROP_XI_DECIMATION_PATTERN: int
CAP_PROP_XI_DECIMATION_SELECTOR: int
CAP_PROP_XI_DECIMATION_VERTICAL: int
CAP_PROP_XI_DEFAULT_CC_MATRIX: int
CAP_PROP_XI_DEVICE_MODEL_ID: int
CAP_PROP_XI_DEVICE_RESET: int
CAP_PROP_XI_DEVICE_SN: int
CAP_PROP_XI_DOWNSAMPLING: int
CAP_PROP_XI_DOWNSAMPLING_TYPE: int
CAP_PROP_XI_EXPOSURE: int
CAP_PROP_XI_EXPOSURE_BURST_COUNT: int
CAP_PROP_XI_EXP_PRIORITY: int
CAP_PROP_XI_FFS_ACCESS_KEY: int
CAP_PROP_XI_FFS_FILE_ID: int
CAP_PROP_XI_FFS_FILE_SIZE: int
CAP_PROP_XI_FRAMERATE: int
CAP_PROP_XI_FREE_FFS_SIZE: int
CAP_PROP_XI_GAIN: int
CAP_PROP_XI_GAIN_SELECTOR: int
CAP_PROP_XI_GAMMAC: int
CAP_PROP_XI_GAMMAY: int
CAP_PROP_XI_GPI_LEVEL: int
CAP_PROP_XI_GPI_MODE: int
CAP_PROP_XI_GPI_SELECTOR: int
CAP_PROP_XI_GPO_MODE: int
CAP_PROP_XI_GPO_SELECTOR: int
CAP_PROP_XI_HDR: int
CAP_PROP_XI_HDR_KNEEPOINT_COUNT: int
CAP_PROP_XI_HDR_T1: int
CAP_PROP_XI_HDR_T2: int
CAP_PROP_XI_HEIGHT: int
CAP_PROP_XI_HOUS_BACK_SIDE_TEMP: int
CAP_PROP_XI_HOUS_TEMP: int
CAP_PROP_XI_HW_REVISION: int
CAP_PROP_XI_IMAGE_BLACK_LEVEL: int
CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH: int
CAP_PROP_XI_IMAGE_DATA_FORMAT: int
CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA: int
CAP_PROP_XI_IMAGE_IS_COLOR: int
CAP_PROP_XI_IMAGE_PAYLOAD_SIZE: int
CAP_PROP_XI_IS_COOLED: int
CAP_PROP_XI_IS_DEVICE_EXIST: int
CAP_PROP_XI_KNEEPOINT1: int
CAP_PROP_XI_KNEEPOINT2: int
CAP_PROP_XI_LED_MODE: int
CAP_PROP_XI_LED_SELECTOR: int
CAP_PROP_XI_LENS_APERTURE_VALUE: int
CAP_PROP_XI_LENS_FEATURE: int
CAP_PROP_XI_LENS_FEATURE_SELECTOR: int
CAP_PROP_XI_LENS_FOCAL_LENGTH: int
CAP_PROP_XI_LENS_FOCUS_DISTANCE: int
CAP_PROP_XI_LENS_FOCUS_MOVE: int
CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE: int
CAP_PROP_XI_LENS_MODE: int
CAP_PROP_XI_LIMIT_BANDWIDTH: int
CAP_PROP_XI_LUT_EN: int
CAP_PROP_XI_LUT_INDEX: int
CAP_PROP_XI_LUT_VALUE: int
CAP_PROP_XI_MANUAL_WB: int
CAP_PROP_XI_OFFSET_X: int
CAP_PROP_XI_OFFSET_Y: int
CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH: int
CAP_PROP_XI_OUTPUT_DATA_PACKING: int
CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE: int
CAP_PROP_XI_RECENT_FRAME: int
CAP_PROP_XI_REGION_MODE: int
CAP_PROP_XI_REGION_SELECTOR: int
CAP_PROP_XI_ROW_FPN_CORRECTION: int
CAP_PROP_XI_SENSOR_BOARD_TEMP: int
CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ: int
CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX: int
CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH: int
CAP_PROP_XI_SENSOR_FEATURE_SELECTOR: int
CAP_PROP_XI_SENSOR_FEATURE_VALUE: int
CAP_PROP_XI_SENSOR_MODE: int
CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT: int
CAP_PROP_XI_SENSOR_TAPS: int
CAP_PROP_XI_SHARPNESS: int
CAP_PROP_XI_SHUTTER_TYPE: int
CAP_PROP_XI_TARGET_TEMP: int
CAP_PROP_XI_TEST_PATTERN: int
CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR: int
CAP_PROP_XI_TIMEOUT: int
CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT: int
CAP_PROP_XI_TRG_DELAY: int
CAP_PROP_XI_TRG_SELECTOR: int
CAP_PROP_XI_TRG_SOFTWARE: int
CAP_PROP_XI_TRG_SOURCE: int
CAP_PROP_XI_TS_RST_MODE: int
CAP_PROP_XI_TS_RST_SOURCE: int
CAP_PROP_XI_USED_FFS_SIZE: int
CAP_PROP_XI_WB_KB: int
CAP_PROP_XI_WB_KG: int
CAP_PROP_XI_WB_KR: int
CAP_PROP_XI_WIDTH: int
CAP_PROP_ZOOM: int
CAP_PVAPI: int
CAP_PVAPI_DECIMATION_2OUTOF16: int
CAP_PVAPI_DECIMATION_2OUTOF4: int
CAP_PVAPI_DECIMATION_2OUTOF8: int
CAP_PVAPI_DECIMATION_OFF: int
CAP_PVAPI_FSTRIGMODE_FIXEDRATE: int
CAP_PVAPI_FSTRIGMODE_FREERUN: int
CAP_PVAPI_FSTRIGMODE_SOFTWARE: int
CAP_PVAPI_FSTRIGMODE_SYNCIN1: int
CAP_PVAPI_FSTRIGMODE_SYNCIN2: int
CAP_PVAPI_PIXELFORMAT_BAYER16: int
CAP_PVAPI_PIXELFORMAT_BAYER8: int
CAP_PVAPI_PIXELFORMAT_BGR24: int
CAP_PVAPI_PIXELFORMAT_BGRA32: int
CAP_PVAPI_PIXELFORMAT_MONO16: int
CAP_PVAPI_PIXELFORMAT_MONO8: int
CAP_PVAPI_PIXELFORMAT_RGB24: int
CAP_PVAPI_PIXELFORMAT_RGBA32: int
CAP_QT: int
CAP_REALSENSE: int
CAP_UEYE: int
CAP_UNICAP: int
CAP_V4L: int
CAP_V4L2: int
CAP_VFW: int
CAP_WINRT: int
CAP_XIAPI: int
CAP_XINE: int
CASCADE_DO_CANNY_PRUNING: int
CASCADE_DO_ROUGH_SEARCH: int
CASCADE_FIND_BIGGEST_OBJECT: int
CASCADE_SCALE_IMAGE: int
CCL_BBDT: int
CCL_BOLELLI: int
CCL_DEFAULT: int
CCL_GRANA: int
CCL_SAUF: int
CCL_SPAGHETTI: int
CCL_WU: int
CC_STAT_AREA: int
CC_STAT_HEIGHT: int
CC_STAT_LEFT: int
CC_STAT_MAX: int
CC_STAT_TOP: int
CC_STAT_WIDTH: int
CHAIN_APPROX_NONE: int
CHAIN_APPROX_SIMPLE: int
CHAIN_APPROX_TC89_KCOS: int
CHAIN_APPROX_TC89_L1: int
CIRCLES_GRID_FINDER_PARAMETERS_ASYMMETRIC_GRID: int
CIRCLES_GRID_FINDER_PARAMETERS_SYMMETRIC_GRID: int
CMP_EQ: int
CMP_GE: int
CMP_GT: int
CMP_LE: int
CMP_LT: int
CMP_NE: int
COLORMAP_AUTUMN: int
COLORMAP_BONE: int
COLORMAP_CIVIDIS: int
COLORMAP_COOL: int
COLORMAP_DEEPGREEN: int
COLORMAP_HOT: int
COLORMAP_HSV: int
COLORMAP_INFERNO: int
COLORMAP_JET: int
COLORMAP_MAGMA: int
COLORMAP_OCEAN: int
COLORMAP_PARULA: int
COLORMAP_PINK: int
COLORMAP_PLASMA: int
COLORMAP_RAINBOW: int
COLORMAP_SPRING: int
COLORMAP_SUMMER: int
COLORMAP_TURBO: int
COLORMAP_TWILIGHT: int
COLORMAP_TWILIGHT_SHIFTED: int
COLORMAP_VIRIDIS: int
COLORMAP_WINTER: int
COLOR_BAYER_BG2BGR: int
COLOR_BAYER_BG2BGRA: int
COLOR_BAYER_BG2BGR_EA: int
COLOR_BAYER_BG2BGR_VNG: int
COLOR_BAYER_BG2GRAY: int
COLOR_BAYER_BG2RGB: int
COLOR_BAYER_BG2RGBA: int
COLOR_BAYER_BG2RGB_EA: int
COLOR_BAYER_BG2RGB_VNG: int
COLOR_BAYER_BGGR2BGR: int
COLOR_BAYER_BGGR2BGRA: int
COLOR_BAYER_BGGR2BGR_EA: int
COLOR_BAYER_BGGR2BGR_VNG: int
COLOR_BAYER_BGGR2GRAY: int
COLOR_BAYER_BGGR2RGB: int
COLOR_BAYER_BGGR2RGBA: int
COLOR_BAYER_BGGR2RGB_EA: int
COLOR_BAYER_BGGR2RGB_VNG: int
COLOR_BAYER_GB2BGR: int
COLOR_BAYER_GB2BGRA: int
COLOR_BAYER_GB2BGR_EA: int
COLOR_BAYER_GB2BGR_VNG: int
COLOR_BAYER_GB2GRAY: int
COLOR_BAYER_GB2RGB: int
COLOR_BAYER_GB2RGBA: int
COLOR_BAYER_GB2RGB_EA: int
COLOR_BAYER_GB2RGB_VNG: int
COLOR_BAYER_GBRG2BGR: int
COLOR_BAYER_GBRG2BGRA: int
COLOR_BAYER_GBRG2BGR_EA: int
COLOR_BAYER_GBRG2BGR_VNG: int
COLOR_BAYER_GBRG2GRAY: int
COLOR_BAYER_GBRG2RGB: int
COLOR_BAYER_GBRG2RGBA: int
COLOR_BAYER_GBRG2RGB_EA: int
COLOR_BAYER_GBRG2RGB_VNG: int
COLOR_BAYER_GR2BGR: int
COLOR_BAYER_GR2BGRA: int
COLOR_BAYER_GR2BGR_EA: int
COLOR_BAYER_GR2BGR_VNG: int
COLOR_BAYER_GR2GRAY: int
COLOR_BAYER_GR2RGB: int
COLOR_BAYER_GR2RGBA: int
COLOR_BAYER_GR2RGB_EA: int
COLOR_BAYER_GR2RGB_VNG: int
COLOR_BAYER_GRBG2BGR: int
COLOR_BAYER_GRBG2BGRA: int
COLOR_BAYER_GRBG2BGR_EA: int
COLOR_BAYER_GRBG2BGR_VNG: int
COLOR_BAYER_GRBG2GRAY: int
COLOR_BAYER_GRBG2RGB: int
COLOR_BAYER_GRBG2RGBA: int
COLOR_BAYER_GRBG2RGB_EA: int
COLOR_BAYER_GRBG2RGB_VNG: int
COLOR_BAYER_RG2BGR: int
COLOR_BAYER_RG2BGRA: int
COLOR_BAYER_RG2BGR_EA: int
COLOR_BAYER_RG2BGR_VNG: int
COLOR_BAYER_RG2GRAY: int
COLOR_BAYER_RG2RGB: int
COLOR_BAYER_RG2RGBA: int
COLOR_BAYER_RG2RGB_EA: int
COLOR_BAYER_RG2RGB_VNG: int
COLOR_BAYER_RGGB2BGR: int
COLOR_BAYER_RGGB2BGRA: int
COLOR_BAYER_RGGB2BGR_EA: int
COLOR_BAYER_RGGB2BGR_VNG: int
COLOR_BAYER_RGGB2GRAY: int
COLOR_BAYER_RGGB2RGB: int
COLOR_BAYER_RGGB2RGBA: int
COLOR_BAYER_RGGB2RGB_EA: int
COLOR_BAYER_RGGB2RGB_VNG: int
COLOR_BGR2BGR555: int
COLOR_BGR2BGR565: int
COLOR_BGR2BGRA: int
COLOR_BGR2GRAY: int
COLOR_BGR2HLS: int
COLOR_BGR2HLS_FULL: int
COLOR_BGR2HSV: int
COLOR_BGR2HSV_FULL: int
COLOR_BGR2LAB: int
COLOR_BGR2LUV: int
COLOR_BGR2Lab: int
COLOR_BGR2Luv: int
COLOR_BGR2RGB: int
COLOR_BGR2RGBA: int
COLOR_BGR2XYZ: int
COLOR_BGR2YCR_CB: int
COLOR_BGR2YCrCb: int
COLOR_BGR2YUV: int
COLOR_BGR2YUV_I420: int
COLOR_BGR2YUV_IYUV: int
COLOR_BGR2YUV_YV12: int
COLOR_BGR5552BGR: int
COLOR_BGR5552BGRA: int
COLOR_BGR5552GRAY: int
COLOR_BGR5552RGB: int
COLOR_BGR5552RGBA: int
COLOR_BGR5652BGR: int
COLOR_BGR5652BGRA: int
COLOR_BGR5652GRAY: int
COLOR_BGR5652RGB: int
COLOR_BGR5652RGBA: int
COLOR_BGRA2BGR: int
COLOR_BGRA2BGR555: int
COLOR_BGRA2BGR565: int
COLOR_BGRA2GRAY: int
COLOR_BGRA2RGB: int
COLOR_BGRA2RGBA: int
COLOR_BGRA2YUV_I420: int
COLOR_BGRA2YUV_IYUV: int
COLOR_BGRA2YUV_YV12: int
COLOR_BayerBG2BGR: int
COLOR_BayerBG2BGRA: int
COLOR_BayerBG2BGR_EA: int
COLOR_BayerBG2BGR_VNG: int
COLOR_BayerBG2GRAY: int
COLOR_BayerBG2RGB: int
COLOR_BayerBG2RGBA: int
COLOR_BayerBG2RGB_EA: int
COLOR_BayerBG2RGB_VNG: int
COLOR_BayerBGGR2BGR: int
COLOR_BayerBGGR2BGRA: int
COLOR_BayerBGGR2BGR_EA: int
COLOR_BayerBGGR2BGR_VNG: int
COLOR_BayerBGGR2GRAY: int
COLOR_BayerBGGR2RGB: int
COLOR_BayerBGGR2RGBA: int
COLOR_BayerBGGR2RGB_EA: int
COLOR_BayerBGGR2RGB_VNG: int
COLOR_BayerGB2BGR: int
COLOR_BayerGB2BGRA: int
COLOR_BayerGB2BGR_EA: int
COLOR_BayerGB2BGR_VNG: int
COLOR_BayerGB2GRAY: int
COLOR_BayerGB2RGB: int
COLOR_BayerGB2RGBA: int
COLOR_BayerGB2RGB_EA: int
COLOR_BayerGB2RGB_VNG: int
COLOR_BayerGBRG2BGR: int
COLOR_BayerGBRG2BGRA: int
COLOR_BayerGBRG2BGR_EA: int
COLOR_BayerGBRG2BGR_VNG: int
COLOR_BayerGBRG2GRAY: int
COLOR_BayerGBRG2RGB: int
COLOR_BayerGBRG2RGBA: int
COLOR_BayerGBRG2RGB_EA: int
COLOR_BayerGBRG2RGB_VNG: int
COLOR_BayerGR2BGR: int
COLOR_BayerGR2BGRA: int
COLOR_BayerGR2BGR_EA: int
COLOR_BayerGR2BGR_VNG: int
COLOR_BayerGR2GRAY: int
COLOR_BayerGR2RGB: int
COLOR_BayerGR2RGBA: int
COLOR_BayerGR2RGB_EA: int
COLOR_BayerGR2RGB_VNG: int
COLOR_BayerGRBG2BGR: int
COLOR_BayerGRBG2BGRA: int
COLOR_BayerGRBG2BGR_EA: int
COLOR_BayerGRBG2BGR_VNG: int
COLOR_BayerGRBG2GRAY: int
COLOR_BayerGRBG2RGB: int
COLOR_BayerGRBG2RGBA: int
COLOR_BayerGRBG2RGB_EA: int
COLOR_BayerGRBG2RGB_VNG: int
COLOR_BayerRG2BGR: int
COLOR_BayerRG2BGRA: int
COLOR_BayerRG2BGR_EA: int
COLOR_BayerRG2BGR_VNG: int
COLOR_BayerRG2GRAY: int
COLOR_BayerRG2RGB: int
COLOR_BayerRG2RGBA: int
COLOR_BayerRG2RGB_EA: int
COLOR_BayerRG2RGB_VNG: int
COLOR_BayerRGGB2BGR: int
COLOR_BayerRGGB2BGRA: int
COLOR_BayerRGGB2BGR_EA: int
COLOR_BayerRGGB2BGR_VNG: int
COLOR_BayerRGGB2GRAY: int
COLOR_BayerRGGB2RGB: int
COLOR_BayerRGGB2RGBA: int
COLOR_BayerRGGB2RGB_EA: int
COLOR_BayerRGGB2RGB_VNG: int
COLOR_COLORCVT_MAX: int
COLOR_GRAY2BGR: int
COLOR_GRAY2BGR555: int
COLOR_GRAY2BGR565: int
COLOR_GRAY2BGRA: int
COLOR_GRAY2RGB: int
COLOR_GRAY2RGBA: int
COLOR_HLS2BGR: int
COLOR_HLS2BGR_FULL: int
COLOR_HLS2RGB: int
COLOR_HLS2RGB_FULL: int
COLOR_HSV2BGR: int
COLOR_HSV2BGR_FULL: int
COLOR_HSV2RGB: int
COLOR_HSV2RGB_FULL: int
COLOR_LAB2BGR: int
COLOR_LAB2LBGR: int
COLOR_LAB2LRGB: int
COLOR_LAB2RGB: int
COLOR_LBGR2LAB: int
COLOR_LBGR2LUV: int
COLOR_LBGR2Lab: int
COLOR_LBGR2Luv: int
COLOR_LRGB2LAB: int
COLOR_LRGB2LUV: int
COLOR_LRGB2Lab: int
COLOR_LRGB2Luv: int
COLOR_LUV2BGR: int
COLOR_LUV2LBGR: int
COLOR_LUV2LRGB: int
COLOR_LUV2RGB: int
COLOR_Lab2BGR: int
COLOR_Lab2LBGR: int
COLOR_Lab2LRGB: int
COLOR_Lab2RGB: int
COLOR_Luv2BGR: int
COLOR_Luv2LBGR: int
COLOR_Luv2LRGB: int
COLOR_Luv2RGB: int
COLOR_M_RGBA2RGBA: int
COLOR_RGB2BGR: int
COLOR_RGB2BGR555: int
COLOR_RGB2BGR565: int
COLOR_RGB2BGRA: int
COLOR_RGB2GRAY: int
COLOR_RGB2HLS: int
COLOR_RGB2HLS_FULL: int
COLOR_RGB2HSV: int
COLOR_RGB2HSV_FULL: int
COLOR_RGB2LAB: int
COLOR_RGB2LUV: int
COLOR_RGB2Lab: int
COLOR_RGB2Luv: int
COLOR_RGB2RGBA: int
COLOR_RGB2XYZ: int
COLOR_RGB2YCR_CB: int
COLOR_RGB2YCrCb: int
COLOR_RGB2YUV: int
COLOR_RGB2YUV_I420: int
COLOR_RGB2YUV_IYUV: int
COLOR_RGB2YUV_YV12: int
COLOR_RGBA2BGR: int
COLOR_RGBA2BGR555: int
COLOR_RGBA2BGR565: int
COLOR_RGBA2BGRA: int
COLOR_RGBA2GRAY: int
COLOR_RGBA2M_RGBA: int
COLOR_RGBA2RGB: int
COLOR_RGBA2YUV_I420: int
COLOR_RGBA2YUV_IYUV: int
COLOR_RGBA2YUV_YV12: int
COLOR_RGBA2mRGBA: int
COLOR_XYZ2BGR: int
COLOR_XYZ2RGB: int
COLOR_YCR_CB2BGR: int
COLOR_YCR_CB2RGB: int
COLOR_YCrCb2BGR: int
COLOR_YCrCb2RGB: int
COLOR_YUV2BGR: int
COLOR_YUV2BGRA_I420: int
COLOR_YUV2BGRA_IYUV: int
COLOR_YUV2BGRA_NV12: int
COLOR_YUV2BGRA_NV21: int
COLOR_YUV2BGRA_UYNV: int
COLOR_YUV2BGRA_UYVY: int
COLOR_YUV2BGRA_Y422: int
COLOR_YUV2BGRA_YUNV: int
COLOR_YUV2BGRA_YUY2: int
COLOR_YUV2BGRA_YUYV: int
COLOR_YUV2BGRA_YV12: int
COLOR_YUV2BGRA_YVYU: int
COLOR_YUV2BGR_I420: int
COLOR_YUV2BGR_IYUV: int
COLOR_YUV2BGR_NV12: int
COLOR_YUV2BGR_NV21: int
COLOR_YUV2BGR_UYNV: int
COLOR_YUV2BGR_UYVY: int
COLOR_YUV2BGR_Y422: int
COLOR_YUV2BGR_YUNV: int
COLOR_YUV2BGR_YUY2: int
COLOR_YUV2BGR_YUYV: int
COLOR_YUV2BGR_YV12: int
COLOR_YUV2BGR_YVYU: int
COLOR_YUV2GRAY_420: int
COLOR_YUV2GRAY_I420: int
COLOR_YUV2GRAY_IYUV: int
COLOR_YUV2GRAY_NV12: int
COLOR_YUV2GRAY_NV21: int
COLOR_YUV2GRAY_UYNV: int
COLOR_YUV2GRAY_UYVY: int
COLOR_YUV2GRAY_Y422: int
COLOR_YUV2GRAY_YUNV: int
COLOR_YUV2GRAY_YUY2: int
COLOR_YUV2GRAY_YUYV: int
COLOR_YUV2GRAY_YV12: int
COLOR_YUV2GRAY_YVYU: int
COLOR_YUV2RGB: int
COLOR_YUV2RGBA_I420: int
COLOR_YUV2RGBA_IYUV: int
COLOR_YUV2RGBA_NV12: int
COLOR_YUV2RGBA_NV21: int
COLOR_YUV2RGBA_UYNV: int
COLOR_YUV2RGBA_UYVY: int
COLOR_YUV2RGBA_Y422: int
COLOR_YUV2RGBA_YUNV: int
COLOR_YUV2RGBA_YUY2: int
COLOR_YUV2RGBA_YUYV: int
COLOR_YUV2RGBA_YV12: int
COLOR_YUV2RGBA_YVYU: int
COLOR_YUV2RGB_I420: int
COLOR_YUV2RGB_IYUV: int
COLOR_YUV2RGB_NV12: int
COLOR_YUV2RGB_NV21: int
COLOR_YUV2RGB_UYNV: int
COLOR_YUV2RGB_UYVY: int
COLOR_YUV2RGB_Y422: int
COLOR_YUV2RGB_YUNV: int
COLOR_YUV2RGB_YUY2: int
COLOR_YUV2RGB_YUYV: int
COLOR_YUV2RGB_YV12: int
COLOR_YUV2RGB_YVYU: int
COLOR_YUV420P2BGR: int
COLOR_YUV420P2BGRA: int
COLOR_YUV420P2GRAY: int
COLOR_YUV420P2RGB: int
COLOR_YUV420P2RGBA: int
COLOR_YUV420SP2BGR: int
COLOR_YUV420SP2BGRA: int
COLOR_YUV420SP2GRAY: int
COLOR_YUV420SP2RGB: int
COLOR_YUV420SP2RGBA: int
COLOR_YUV420p2BGR: int
COLOR_YUV420p2BGRA: int
COLOR_YUV420p2GRAY: int
COLOR_YUV420p2RGB: int
COLOR_YUV420p2RGBA: int
COLOR_YUV420sp2BGR: int
COLOR_YUV420sp2BGRA: int
COLOR_YUV420sp2GRAY: int
COLOR_YUV420sp2RGB: int
COLOR_YUV420sp2RGBA: int
COLOR_mRGBA2RGBA: int
CONTOURS_MATCH_I1: int
CONTOURS_MATCH_I2: int
CONTOURS_MATCH_I3: int
COVAR_COLS: int
COVAR_NORMAL: int
COVAR_ROWS: int
COVAR_SCALE: int
COVAR_SCRAMBLED: int
COVAR_USE_AVG: int
CV_16S: int
CV_16SC1: int
CV_16SC2: int
CV_16SC3: int
CV_16SC4: int
CV_16U: int
CV_16UC1: int
CV_16UC2: int
CV_16UC3: int
CV_16UC4: int
CV_32F: int
CV_32FC1: int
CV_32FC2: int
CV_32FC3: int
CV_32FC4: int
CV_32S: int
CV_32SC1: int
CV_32SC2: int
CV_32SC3: int
CV_32SC4: int
CV_64F: int
CV_64FC1: int
CV_64FC2: int
CV_64FC3: int
CV_64FC4: int
CV_8S: int
CV_8SC1: int
CV_8SC2: int
CV_8SC3: int
CV_8SC4: int
CV_8U: int
CV_8UC1: int
CV_8UC2: int
CV_8UC3: int
CV_8UC4: int
CirclesGridFinderParameters_ASYMMETRIC_GRID: int
CirclesGridFinderParameters_SYMMETRIC_GRID: int
DCT_INVERSE: int
DCT_ROWS: int
DECOMP_CHOLESKY: int
DECOMP_EIG: int
DECOMP_LU: int
DECOMP_NORMAL: int
DECOMP_QR: int
DECOMP_SVD: int
DESCRIPTOR_MATCHER_BRUTEFORCE: int
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING: int
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMINGLUT: int
DESCRIPTOR_MATCHER_BRUTEFORCE_L1: int
DESCRIPTOR_MATCHER_BRUTEFORCE_SL2: int
DESCRIPTOR_MATCHER_FLANNBASED: int
DFT_COMPLEX_INPUT: int
DFT_COMPLEX_OUTPUT: int
DFT_INVERSE: int
DFT_REAL_OUTPUT: int
DFT_ROWS: int
DFT_SCALE: int
DISOPTICAL_FLOW_PRESET_FAST: int
DISOPTICAL_FLOW_PRESET_MEDIUM: int
DISOPTICAL_FLOW_PRESET_ULTRAFAST: int
DISOpticalFlow_PRESET_FAST: int
DISOpticalFlow_PRESET_MEDIUM: int
DISOpticalFlow_PRESET_ULTRAFAST: int
DIST_C: int
DIST_FAIR: int
DIST_HUBER: int
DIST_L1: int
DIST_L12: int
DIST_L2: int
DIST_LABEL_CCOMP: int
DIST_LABEL_PIXEL: int
DIST_MASK_3: int
DIST_MASK_5: int
DIST_MASK_PRECISE: int
DIST_USER: int
DIST_WELSCH: int
DRAW_MATCHES_FLAGS_DEFAULT: int
DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG: int
DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS: int
DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS: int
DescriptorMatcher_BRUTEFORCE: int
DescriptorMatcher_BRUTEFORCE_HAMMING: int
DescriptorMatcher_BRUTEFORCE_HAMMINGLUT: int
DescriptorMatcher_BRUTEFORCE_L1: int
DescriptorMatcher_BRUTEFORCE_SL2: int
DescriptorMatcher_FLANNBASED: int
DrawMatchesFlags_DEFAULT: int
DrawMatchesFlags_DRAW_OVER_OUTIMG: int
DrawMatchesFlags_DRAW_RICH_KEYPOINTS: int
DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS: int
EVENT_FLAG_ALTKEY: int
EVENT_FLAG_CTRLKEY: int
EVENT_FLAG_LBUTTON: int
EVENT_FLAG_MBUTTON: int
EVENT_FLAG_RBUTTON: int
EVENT_FLAG_SHIFTKEY: int
EVENT_LBUTTONDBLCLK: int
EVENT_LBUTTONDOWN: int
EVENT_LBUTTONUP: int
EVENT_MBUTTONDBLCLK: int
EVENT_MBUTTONDOWN: int
EVENT_MBUTTONUP: int
EVENT_MOUSEHWHEEL: int
EVENT_MOUSEMOVE: int
EVENT_MOUSEWHEEL: int
EVENT_RBUTTONDBLCLK: int
EVENT_RBUTTONDOWN: int
EVENT_RBUTTONUP: int
FACE_RECOGNIZER_SF_FR_COSINE: int
FACE_RECOGNIZER_SF_FR_NORM_L2: int
FAST_FEATURE_DETECTOR_FAST_N: int
FAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION: int
FAST_FEATURE_DETECTOR_THRESHOLD: int
FAST_FEATURE_DETECTOR_TYPE_5_8: int
FAST_FEATURE_DETECTOR_TYPE_7_12: int
FAST_FEATURE_DETECTOR_TYPE_9_16: int
FILE_NODE_EMPTY: int
FILE_NODE_FLOAT: int
FILE_NODE_FLOW: int
FILE_NODE_INT: int
FILE_NODE_MAP: int
FILE_NODE_NAMED: int
FILE_NODE_NONE: int
FILE_NODE_REAL: int
FILE_NODE_SEQ: int
FILE_NODE_STR: int
FILE_NODE_STRING: int
FILE_NODE_TYPE_MASK: int
FILE_NODE_UNIFORM: int
FILE_STORAGE_APPEND: int
FILE_STORAGE_BASE64: int
FILE_STORAGE_FORMAT_AUTO: int
FILE_STORAGE_FORMAT_JSON: int
FILE_STORAGE_FORMAT_MASK: int
FILE_STORAGE_FORMAT_XML: int
FILE_STORAGE_FORMAT_YAML: int
FILE_STORAGE_INSIDE_MAP: int
FILE_STORAGE_MEMORY: int
FILE_STORAGE_NAME_EXPECTED: int
FILE_STORAGE_READ: int
FILE_STORAGE_UNDEFINED: int
FILE_STORAGE_VALUE_EXPECTED: int
FILE_STORAGE_WRITE: int
FILE_STORAGE_WRITE_BASE64: int
FILLED: int
FILTER_SCHARR: int
FLOODFILL_FIXED_RANGE: int
FLOODFILL_MASK_ONLY: int
FM_7POINT: int
FM_8POINT: int
FM_LMEDS: int
FM_RANSAC: int
FONT_HERSHEY_COMPLEX: int
FONT_HERSHEY_COMPLEX_SMALL: int
FONT_HERSHEY_DUPLEX: int
FONT_HERSHEY_PLAIN: int
FONT_HERSHEY_SCRIPT_COMPLEX: int
FONT_HERSHEY_SCRIPT_SIMPLEX: int
FONT_HERSHEY_SIMPLEX: int
FONT_HERSHEY_TRIPLEX: int
FONT_ITALIC: int
FORMATTER_FMT_C: int
FORMATTER_FMT_CSV: int
FORMATTER_FMT_DEFAULT: int
FORMATTER_FMT_MATLAB: int
FORMATTER_FMT_NUMPY: int
FORMATTER_FMT_PYTHON: int
FaceRecognizerSF_FR_COSINE: int
FaceRecognizerSF_FR_NORM_L2: int
FastFeatureDetector_FAST_N: int
FastFeatureDetector_NONMAX_SUPPRESSION: int
FastFeatureDetector_THRESHOLD: int
FastFeatureDetector_TYPE_5_8: int
FastFeatureDetector_TYPE_7_12: int
FastFeatureDetector_TYPE_9_16: int
FileNode_EMPTY: int
FileNode_FLOAT: int
FileNode_FLOW: int
FileNode_INT: int
FileNode_MAP: int
FileNode_NAMED: int
FileNode_NONE: int
FileNode_REAL: int
FileNode_SEQ: int
FileNode_STR: int
FileNode_STRING: int
FileNode_TYPE_MASK: int
FileNode_UNIFORM: int
FileStorage_APPEND: int
FileStorage_BASE64: int
FileStorage_FORMAT_AUTO: int
FileStorage_FORMAT_JSON: int
FileStorage_FORMAT_MASK: int
FileStorage_FORMAT_XML: int
FileStorage_FORMAT_YAML: int
FileStorage_INSIDE_MAP: int
FileStorage_MEMORY: int
FileStorage_NAME_EXPECTED: int
FileStorage_READ: int
FileStorage_UNDEFINED: int
FileStorage_VALUE_EXPECTED: int
FileStorage_WRITE: int
FileStorage_WRITE_BASE64: int
Formatter_FMT_C: int
Formatter_FMT_CSV: int
Formatter_FMT_DEFAULT: int
Formatter_FMT_MATLAB: int
Formatter_FMT_NUMPY: int
Formatter_FMT_PYTHON: int
GC_BGD: int
GC_EVAL: int
GC_EVAL_FREEZE_MODEL: int
GC_FGD: int
GC_INIT_WITH_MASK: int
GC_INIT_WITH_RECT: int
GC_PR_BGD: int
GC_PR_FGD: int
GEMM_1_T: int
GEMM_2_T: int
GEMM_3_T: int
GFLUID_KERNEL_KIND_FILTER: int
GFLUID_KERNEL_KIND_RESIZE: int
GFLUID_KERNEL_KIND_YUV420TO_RGB: int
GFluidKernel_Kind_Filter: int
GFluidKernel_Kind_Resize: int
GFluidKernel_Kind_YUV420toRGB: int
GSHAPE_GARRAY: int
GSHAPE_GFRAME: int
GSHAPE_GMAT: int
GSHAPE_GOPAQUE: int
GSHAPE_GSCALAR: int
GShape_GARRAY: int
GShape_GFRAME: int
GShape_GMAT: int
GShape_GOPAQUE: int
GShape_GSCALAR: int
HISTCMP_BHATTACHARYYA: int
HISTCMP_CHISQR: int
HISTCMP_CHISQR_ALT: int
HISTCMP_CORREL: int
HISTCMP_HELLINGER: int
HISTCMP_INTERSECT: int
HISTCMP_KL_DIV: int
HOGDESCRIPTOR_DEFAULT_NLEVELS: int
HOGDESCRIPTOR_DESCR_FORMAT_COL_BY_COL: int
HOGDESCRIPTOR_DESCR_FORMAT_ROW_BY_ROW: int
HOGDESCRIPTOR_L2HYS: int
HOGDescriptor_DEFAULT_NLEVELS: int
HOGDescriptor_DESCR_FORMAT_COL_BY_COL: int
HOGDescriptor_DESCR_FORMAT_ROW_BY_ROW: int
HOGDescriptor_L2Hys: int
HOUGH_GRADIENT: int
HOUGH_GRADIENT_ALT: int
HOUGH_MULTI_SCALE: int
HOUGH_PROBABILISTIC: int
HOUGH_STANDARD: int
IMREAD_ANYCOLOR: int
IMREAD_ANYDEPTH: int
IMREAD_COLOR: int
IMREAD_GRAYSCALE: int
IMREAD_IGNORE_ORIENTATION: int
IMREAD_LOAD_GDAL: int
IMREAD_REDUCED_COLOR_2: int
IMREAD_REDUCED_COLOR_4: int
IMREAD_REDUCED_COLOR_8: int
IMREAD_REDUCED_GRAYSCALE_2: int
IMREAD_REDUCED_GRAYSCALE_4: int
IMREAD_REDUCED_GRAYSCALE_8: int
IMREAD_UNCHANGED: int
IMWRITE_EXR_COMPRESSION: int
IMWRITE_EXR_COMPRESSION_B44: int
IMWRITE_EXR_COMPRESSION_B44A: int
IMWRITE_EXR_COMPRESSION_DWAA: int
IMWRITE_EXR_COMPRESSION_DWAB: int
IMWRITE_EXR_COMPRESSION_NO: int
IMWRITE_EXR_COMPRESSION_PIZ: int
IMWRITE_EXR_COMPRESSION_PXR24: int
IMWRITE_EXR_COMPRESSION_RLE: int
IMWRITE_EXR_COMPRESSION_ZIP: int
IMWRITE_EXR_COMPRESSION_ZIPS: int
IMWRITE_EXR_TYPE: int
IMWRITE_EXR_TYPE_FLOAT: int
IMWRITE_EXR_TYPE_HALF: int
IMWRITE_JPEG2000_COMPRESSION_X1000: int
IMWRITE_JPEG_CHROMA_QUALITY: int
IMWRITE_JPEG_LUMA_QUALITY: int
IMWRITE_JPEG_OPTIMIZE: int
IMWRITE_JPEG_PROGRESSIVE: int
IMWRITE_JPEG_QUALITY: int
IMWRITE_JPEG_RST_INTERVAL: int
IMWRITE_PAM_FORMAT_BLACKANDWHITE: int
IMWRITE_PAM_FORMAT_GRAYSCALE: int
IMWRITE_PAM_FORMAT_GRAYSCALE_ALPHA: int
IMWRITE_PAM_FORMAT_NULL: int
IMWRITE_PAM_FORMAT_RGB: int
IMWRITE_PAM_FORMAT_RGB_ALPHA: int
IMWRITE_PAM_TUPLETYPE: int
IMWRITE_PNG_BILEVEL: int
IMWRITE_PNG_COMPRESSION: int
IMWRITE_PNG_STRATEGY: int
IMWRITE_PNG_STRATEGY_DEFAULT: int
IMWRITE_PNG_STRATEGY_FILTERED: int
IMWRITE_PNG_STRATEGY_FIXED: int
IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY: int
IMWRITE_PNG_STRATEGY_RLE: int
IMWRITE_PXM_BINARY: int
IMWRITE_TIFF_COMPRESSION: int
IMWRITE_TIFF_RESUNIT: int
IMWRITE_TIFF_XDPI: int
IMWRITE_TIFF_YDPI: int
IMWRITE_WEBP_QUALITY: int
INPAINT_NS: int
INPAINT_TELEA: int
INTERSECT_FULL: int
INTERSECT_NONE: int
INTERSECT_PARTIAL: int
INTER_AREA: int
INTER_BITS: int
INTER_BITS2: int
INTER_CUBIC: int
INTER_LANCZOS4: int
INTER_LINEAR: int
INTER_LINEAR_EXACT: int
INTER_MAX: int
INTER_NEAREST: int
INTER_NEAREST_EXACT: int
INTER_TAB_SIZE: int
INTER_TAB_SIZE2: int
KAZE_DIFF_CHARBONNIER: int
KAZE_DIFF_PM_G1: int
KAZE_DIFF_PM_G2: int
KAZE_DIFF_WEICKERT: int
KMEANS_PP_CENTERS: int
KMEANS_RANDOM_CENTERS: int
KMEANS_USE_INITIAL_LABELS: int
LDR_SIZE: int
LINE_4: int
LINE_8: int
LINE_AA: int
LMEDS: int
LOCAL_OPTIM_GC: int
LOCAL_OPTIM_INNER_AND_ITER_LO: int
LOCAL_OPTIM_INNER_LO: int
LOCAL_OPTIM_NULL: int
LOCAL_OPTIM_SIGMA: int
LSD_REFINE_ADV: int
LSD_REFINE_NONE: int
LSD_REFINE_STD: int
MARKER_CROSS: int
MARKER_DIAMOND: int
MARKER_SQUARE: int
MARKER_STAR: int
MARKER_TILTED_CROSS: int
MARKER_TRIANGLE_DOWN: int
MARKER_TRIANGLE_UP: int
MAT_AUTO_STEP: int
MAT_CONTINUOUS_FLAG: int
MAT_DEPTH_MASK: int
MAT_MAGIC_MASK: int
MAT_MAGIC_VAL: int
MAT_SUBMATRIX_FLAG: int
MAT_TYPE_MASK: int
MEDIA_FORMAT_BGR: int
MEDIA_FORMAT_NV12: int
MEDIA_FRAME_ACCESS_R: int
MEDIA_FRAME_ACCESS_W: int
MIXED_CLONE: int
MONOCHROME_TRANSFER: int
MORPH_BLACKHAT: int
MORPH_CLOSE: int
MORPH_CROSS: int
MORPH_DILATE: int
MORPH_ELLIPSE: int
MORPH_ERODE: int
MORPH_GRADIENT: int
MORPH_HITMISS: int
MORPH_OPEN: int
MORPH_RECT: int
MORPH_TOPHAT: int
MOTION_AFFINE: int
MOTION_EUCLIDEAN: int
MOTION_HOMOGRAPHY: int
MOTION_TRANSLATION: int
Mat_AUTO_STEP: int
Mat_CONTINUOUS_FLAG: int
Mat_DEPTH_MASK: int
Mat_MAGIC_MASK: int
Mat_MAGIC_VAL: int
Mat_SUBMATRIX_FLAG: int
Mat_TYPE_MASK: int
MediaFormat_BGR: int
MediaFormat_NV12: int
MediaFrame_Access_R: int
MediaFrame_Access_W: int
NEIGH_FLANN_KNN: int
NEIGH_FLANN_RADIUS: int
NEIGH_GRID: int
NORMAL_CLONE: int
NORMCONV_FILTER: int
NORM_HAMMING: int
NORM_HAMMING2: int
NORM_INF: int
NORM_L1: int
NORM_L2: int
NORM_L2SQR: int
NORM_MINMAX: int
NORM_RELATIVE: int
NORM_TYPE_MASK: int
OPTFLOW_FARNEBACK_GAUSSIAN: int
OPTFLOW_LK_GET_MIN_EIGENVALS: int
OPTFLOW_USE_INITIAL_FLOW: int
ORB_FAST_SCORE: int
ORB_HARRIS_SCORE: int
PARAM_ALGORITHM: int
PARAM_BOOLEAN: int
PARAM_FLOAT: int
PARAM_INT: int
PARAM_MAT: int
PARAM_MAT_VECTOR: int
PARAM_REAL: int
PARAM_SCALAR: int
PARAM_STRING: int
PARAM_UCHAR: int
PARAM_UINT64: int
PARAM_UNSIGNED_INT: int
PCA_DATA_AS_COL: int
PCA_DATA_AS_ROW: int
PCA_USE_AVG: int
PROJ_SPHERICAL_EQRECT: int
PROJ_SPHERICAL_ORTHO: int
Param_ALGORITHM: int
Param_BOOLEAN: int
Param_FLOAT: int
Param_INT: int
Param_MAT: int
Param_MAT_VECTOR: int
Param_REAL: int
Param_SCALAR: int
Param_STRING: int
Param_UCHAR: int
Param_UINT64: int
Param_UNSIGNED_INT: int
QRCODE_ENCODER_CORRECT_LEVEL_H: int
QRCODE_ENCODER_CORRECT_LEVEL_L: int
QRCODE_ENCODER_CORRECT_LEVEL_M: int
QRCODE_ENCODER_CORRECT_LEVEL_Q: int
QRCODE_ENCODER_ECI_UTF8: int
QRCODE_ENCODER_MODE_ALPHANUMERIC: int
QRCODE_ENCODER_MODE_AUTO: int
QRCODE_ENCODER_MODE_BYTE: int
QRCODE_ENCODER_MODE_ECI: int
QRCODE_ENCODER_MODE_KANJI: int
QRCODE_ENCODER_MODE_NUMERIC: int
QRCODE_ENCODER_MODE_STRUCTURED_APPEND: int
QRCodeEncoder_CORRECT_LEVEL_H: int
QRCodeEncoder_CORRECT_LEVEL_L: int
QRCodeEncoder_CORRECT_LEVEL_M: int
QRCodeEncoder_CORRECT_LEVEL_Q: int
QRCodeEncoder_ECI_UTF8: int
QRCodeEncoder_MODE_ALPHANUMERIC: int
QRCodeEncoder_MODE_AUTO: int
QRCodeEncoder_MODE_BYTE: int
QRCodeEncoder_MODE_ECI: int
QRCodeEncoder_MODE_KANJI: int
QRCodeEncoder_MODE_NUMERIC: int
QRCodeEncoder_MODE_STRUCTURED_APPEND: int
QT_CHECKBOX: int
QT_FONT_BLACK: int
QT_FONT_BOLD: int
QT_FONT_DEMIBOLD: int
QT_FONT_LIGHT: int
QT_FONT_NORMAL: int
QT_NEW_BUTTONBAR: int
QT_PUSH_BUTTON: int
QT_RADIOBOX: int
QT_STYLE_ITALIC: int
QT_STYLE_NORMAL: int
QT_STYLE_OBLIQUE: int
QUAT_ASSUME_NOT_UNIT: int
QUAT_ASSUME_UNIT: int
QUAT_ENUM_EULER_ANGLES_MAX_VALUE: int
QUAT_ENUM_EXT_XYX: int
QUAT_ENUM_EXT_XYZ: int
QUAT_ENUM_EXT_XZX: int
QUAT_ENUM_EXT_XZY: int
QUAT_ENUM_EXT_YXY: int
QUAT_ENUM_EXT_YXZ: int
QUAT_ENUM_EXT_YZX: int
QUAT_ENUM_EXT_YZY: int
QUAT_ENUM_EXT_ZXY: int
QUAT_ENUM_EXT_ZXZ: int
QUAT_ENUM_EXT_ZYX: int
QUAT_ENUM_EXT_ZYZ: int
QUAT_ENUM_INT_XYX: int
QUAT_ENUM_INT_XYZ: int
QUAT_ENUM_INT_XZX: int
QUAT_ENUM_INT_XZY: int
QUAT_ENUM_INT_YXY: int
QUAT_ENUM_INT_YXZ: int
QUAT_ENUM_INT_YZX: int
QUAT_ENUM_INT_YZY: int
QUAT_ENUM_INT_ZXY: int
QUAT_ENUM_INT_ZXZ: int
QUAT_ENUM_INT_ZYX: int
QUAT_ENUM_INT_ZYZ: int
QuatEnum_EULER_ANGLES_MAX_VALUE: int
QuatEnum_EXT_XYX: int
QuatEnum_EXT_XYZ: int
QuatEnum_EXT_XZX: int
QuatEnum_EXT_XZY: int
QuatEnum_EXT_YXY: int
QuatEnum_EXT_YXZ: int
QuatEnum_EXT_YZX: int
QuatEnum_EXT_YZY: int
QuatEnum_EXT_ZXY: int
QuatEnum_EXT_ZXZ: int
QuatEnum_EXT_ZYX: int
QuatEnum_EXT_ZYZ: int
QuatEnum_INT_XYX: int
QuatEnum_INT_XYZ: int
QuatEnum_INT_XZX: int
QuatEnum_INT_XZY: int
QuatEnum_INT_YXY: int
QuatEnum_INT_YXZ: int
QuatEnum_INT_YZX: int
QuatEnum_INT_YZY: int
QuatEnum_INT_ZXY: int
QuatEnum_INT_ZXZ: int
QuatEnum_INT_ZYX: int
QuatEnum_INT_ZYZ: int
RANSAC: int
RECURS_FILTER: int
REDUCE_AVG: int
REDUCE_MAX: int
REDUCE_MIN: int
REDUCE_SUM: int
RETR_CCOMP: int
RETR_EXTERNAL: int
RETR_FLOODFILL: int
RETR_LIST: int
RETR_TREE: int
RHO: int
RMAT_ACCESS_R: int
RMAT_ACCESS_W: int
RMat_Access_R: int
RMat_Access_W: int
RNG_NORMAL: int
RNG_UNIFORM: int
ROTATE_180: int
ROTATE_90_CLOCKWISE: int
ROTATE_90_COUNTERCLOCKWISE: int
SAMPLING_NAPSAC: int
SAMPLING_PROGRESSIVE_NAPSAC: int
SAMPLING_PROSAC: int
SAMPLING_UNIFORM: int
SCORE_METHOD_LMEDS: int
SCORE_METHOD_MAGSAC: int
SCORE_METHOD_MSAC: int
SCORE_METHOD_RANSAC: int
SOLVELP_MULTI: int
SOLVELP_SINGLE: int
SOLVELP_UNBOUNDED: int
SOLVELP_UNFEASIBLE: int
SOLVEPNP_AP3P: int
SOLVEPNP_DLS: int
SOLVEPNP_EPNP: int
SOLVEPNP_IPPE: int
SOLVEPNP_IPPE_SQUARE: int
SOLVEPNP_ITERATIVE: int
SOLVEPNP_MAX_COUNT: int
SOLVEPNP_P3P: int
SOLVEPNP_SQPNP: int
SOLVEPNP_UPNP: int
SORT_ASCENDING: int
SORT_DESCENDING: int
SORT_EVERY_COLUMN: int
SORT_EVERY_ROW: int
SPARSE_MAT_HASH_BIT: int
SPARSE_MAT_HASH_SCALE: int
SPARSE_MAT_MAGIC_VAL: int
SPARSE_MAT_MAX_DIM: int
STEREO_BM_PREFILTER_NORMALIZED_RESPONSE: int
STEREO_BM_PREFILTER_XSOBEL: int
STEREO_MATCHER_DISP_SCALE: int
STEREO_MATCHER_DISP_SHIFT: int
STEREO_SGBM_MODE_HH: int
STEREO_SGBM_MODE_HH4: int
STEREO_SGBM_MODE_SGBM: int
STEREO_SGBM_MODE_SGBM_3WAY: int
STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL: int
STITCHER_ERR_HOMOGRAPHY_EST_FAIL: int
STITCHER_ERR_NEED_MORE_IMGS: int
STITCHER_OK: int
STITCHER_PANORAMA: int
STITCHER_SCANS: int
SUBDIV2D_NEXT_AROUND_DST: int
SUBDIV2D_NEXT_AROUND_LEFT: int
SUBDIV2D_NEXT_AROUND_ORG: int
SUBDIV2D_NEXT_AROUND_RIGHT: int
SUBDIV2D_PREV_AROUND_DST: int
SUBDIV2D_PREV_AROUND_LEFT: int
SUBDIV2D_PREV_AROUND_ORG: int
SUBDIV2D_PREV_AROUND_RIGHT: int
SUBDIV2D_PTLOC_ERROR: int
SUBDIV2D_PTLOC_INSIDE: int
SUBDIV2D_PTLOC_ON_EDGE: int
SUBDIV2D_PTLOC_OUTSIDE_RECT: int
SUBDIV2D_PTLOC_VERTEX: int
SVD_FULL_UV: int
SVD_MODIFY_A: int
SVD_NO_UV: int
SparseMat_HASH_BIT: int
SparseMat_HASH_SCALE: int
SparseMat_MAGIC_VAL: int
SparseMat_MAX_DIM: int
StereoBM_PREFILTER_NORMALIZED_RESPONSE: int
StereoBM_PREFILTER_XSOBEL: int
StereoMatcher_DISP_SCALE: int
StereoMatcher_DISP_SHIFT: int
StereoSGBM_MODE_HH: int
StereoSGBM_MODE_HH4: int
StereoSGBM_MODE_SGBM: int
StereoSGBM_MODE_SGBM_3WAY: int
Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL: int
Stitcher_ERR_HOMOGRAPHY_EST_FAIL: int
Stitcher_ERR_NEED_MORE_IMGS: int
Stitcher_OK: int
Stitcher_PANORAMA: int
Stitcher_SCANS: int
Subdiv2D_NEXT_AROUND_DST: int
Subdiv2D_NEXT_AROUND_LEFT: int
Subdiv2D_NEXT_AROUND_ORG: int
Subdiv2D_NEXT_AROUND_RIGHT: int
Subdiv2D_PREV_AROUND_DST: int
Subdiv2D_PREV_AROUND_LEFT: int
Subdiv2D_PREV_AROUND_ORG: int
Subdiv2D_PREV_AROUND_RIGHT: int
Subdiv2D_PTLOC_ERROR: int
Subdiv2D_PTLOC_INSIDE: int
Subdiv2D_PTLOC_ON_EDGE: int
Subdiv2D_PTLOC_OUTSIDE_RECT: int
Subdiv2D_PTLOC_VERTEX: int
TERM_CRITERIA_COUNT: int
TERM_CRITERIA_EPS: int
TERM_CRITERIA_MAX_ITER: int
THRESH_BINARY: int
THRESH_BINARY_INV: int
THRESH_MASK: int
THRESH_OTSU: int
THRESH_TOZERO: int
THRESH_TOZERO_INV: int
THRESH_TRIANGLE: int
THRESH_TRUNC: int
TM_CCOEFF: int
TM_CCOEFF_NORMED: int
TM_CCORR: int
TM_CCORR_NORMED: int
TM_SQDIFF: int
TM_SQDIFF_NORMED: int
TermCriteria_COUNT: int
TermCriteria_EPS: int
TermCriteria_MAX_ITER: int
UMAT_AUTO_STEP: int
UMAT_CONTINUOUS_FLAG: int
UMAT_DATA_ASYNC_CLEANUP: int
UMAT_DATA_COPY_ON_MAP: int
UMAT_DATA_DEVICE_COPY_OBSOLETE: int
UMAT_DATA_DEVICE_MEM_MAPPED: int
UMAT_DATA_HOST_COPY_OBSOLETE: int
UMAT_DATA_TEMP_COPIED_UMAT: int
UMAT_DATA_TEMP_UMAT: int
UMAT_DATA_USER_ALLOCATED: int
UMAT_DEPTH_MASK: int
UMAT_MAGIC_MASK: int
UMAT_MAGIC_VAL: int
UMAT_SUBMATRIX_FLAG: int
UMAT_TYPE_MASK: int
UMatData_ASYNC_CLEANUP: int
UMatData_COPY_ON_MAP: int
UMatData_DEVICE_COPY_OBSOLETE: int
UMatData_DEVICE_MEM_MAPPED: int
UMatData_HOST_COPY_OBSOLETE: int
UMatData_TEMP_COPIED_UMAT: int
UMatData_TEMP_UMAT: int
UMatData_USER_ALLOCATED: int
UMat_AUTO_STEP: int
UMat_CONTINUOUS_FLAG: int
UMat_DEPTH_MASK: int
UMat_MAGIC_MASK: int
UMat_MAGIC_VAL: int
UMat_SUBMATRIX_FLAG: int
UMat_TYPE_MASK: int
USAC_ACCURATE: int
USAC_DEFAULT: int
USAC_FAST: int
USAC_FM_8PTS: int
USAC_MAGSAC: int
USAC_PARALLEL: int
USAC_PROSAC: int
USAGE_ALLOCATE_DEVICE_MEMORY: int
USAGE_ALLOCATE_HOST_MEMORY: int
USAGE_ALLOCATE_SHARED_MEMORY: int
USAGE_DEFAULT: int
VIDEOWRITER_PROP_DEPTH: int
VIDEOWRITER_PROP_FRAMEBYTES: int
VIDEOWRITER_PROP_HW_ACCELERATION: int
VIDEOWRITER_PROP_HW_ACCELERATION_USE_OPENCL: int
VIDEOWRITER_PROP_HW_DEVICE: int
VIDEOWRITER_PROP_IS_COLOR: int
VIDEOWRITER_PROP_NSTRIPES: int
VIDEOWRITER_PROP_QUALITY: int
VIDEO_ACCELERATION_ANY: int
VIDEO_ACCELERATION_D3D11: int
VIDEO_ACCELERATION_MFX: int
VIDEO_ACCELERATION_NONE: int
VIDEO_ACCELERATION_VAAPI: int
WARP_FILL_OUTLIERS: int
WARP_INVERSE_MAP: int
WARP_POLAR_LINEAR: int
WARP_POLAR_LOG: int
WINDOW_AUTOSIZE: int
WINDOW_FREERATIO: int
WINDOW_FULLSCREEN: int
WINDOW_GUI_EXPANDED: int
WINDOW_GUI_NORMAL: int
WINDOW_KEEPRATIO: int
WINDOW_NORMAL: int
WINDOW_OPENGL: int
WND_PROP_ASPECT_RATIO: int
WND_PROP_AUTOSIZE: int
WND_PROP_FULLSCREEN: int
WND_PROP_OPENGL: int
WND_PROP_TOPMOST: int
WND_PROP_VISIBLE: int
WND_PROP_VSYNC: int


class AKAZE(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getDescriptorChannels(self, *args, **kwargs): ...  # incomplete
    def getDescriptorSize(self, *args, **kwargs): ...  # incomplete
    def getDescriptorType(self, *args, **kwargs): ...  # incomplete
    def getDiffusivity(self, *args, **kwargs): ...  # incomplete
    def getNOctaveLayers(self, *args, **kwargs): ...  # incomplete
    def getNOctaves(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def setDescriptorChannels(self, dch) -> None: ...
    def setDescriptorSize(self, dsize) -> None: ...
    def setDescriptorType(self, dtype) -> None: ...
    def setDiffusivity(self, diff) -> None: ...
    def setNOctaveLayers(self, octaveLayers) -> None: ...
    def setNOctaves(self, octaves) -> None: ...
    def setThreshold(self, threshold) -> None: ...


class AffineFeature(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getViewParams(self, tilts, rolls) -> None: ...
    def setViewParams(self, tilts, rolls) -> None: ...


class AgastFeatureDetector(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getNonmaxSuppression(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def getType(self, *args, **kwargs): ...  # incomplete
    def setNonmaxSuppression(self, f) -> None: ...
    def setThreshold(self, threshold) -> None: ...
    def setType(self, type) -> None: ...


class Algorithm:
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def empty(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def read(self, fn) -> None: ...
    def save(self, filename) -> None: ...
    def write(self, *args, **kwargs): ...  # incomplete


class AlignExposures(Algorithm):
    def process(self, src, dst, times, response) -> None: ...


class AlignMTB(AlignExposures):
    def calculateShift(self, *args, **kwargs): ...  # incomplete
    def computeBitmaps(self, *args, **kwargs): ...  # incomplete
    def getCut(self, *args, **kwargs): ...  # incomplete
    def getExcludeRange(self, *args, **kwargs): ...  # incomplete
    def getMaxBits(self, *args, **kwargs): ...  # incomplete
    @overload
    def process(self, src, dst, times, response) -> None: ...
    @overload
    def process(self, src, dst) -> None: ...
    def setCut(self, value) -> None: ...
    def setExcludeRange(self, exclude_range) -> None: ...
    def setMaxBits(self, max_bits) -> None: ...
    def shiftMat(self, *args, **kwargs): ...  # incomplete


class AsyncArray:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def get(self, *args, **kwargs): ...  # incomplete
    def release(self) -> None: ...
    def valid(self, *args, **kwargs): ...  # incomplete
    def wait_for(self, *args, **kwargs): ...  # incomplete


class BFMatcher(DescriptorMatcher):
    def __init__(self, normType: int | None = ..., crossCheck: _Boolean = ...) -> None: ...
    def create(self, *args, **kwargs): ...  # incomplete


class BOWImgDescriptorExtractor:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def compute(self, *args, **kwargs): ...  # incomplete
    def descriptorSize(self, *args, **kwargs): ...  # incomplete
    def descriptorType(self, *args, **kwargs): ...  # incomplete
    def getVocabulary(self, *args, **kwargs): ...  # incomplete
    def setVocabulary(self, vocabulary) -> None: ...


class BOWKMeansTrainer(BOWTrainer):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def cluster(self, *args, **kwargs): ...  # incomplete


class BOWTrainer:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def add(self, descriptors) -> None: ...
    def clear(self) -> None: ...
    def cluster(self, *args, **kwargs): ...  # incomplete
    def descriptorsCount(self, *args, **kwargs): ...  # incomplete
    def getDescriptors(self, *args, **kwargs): ...  # incomplete


class BRISK(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getOctaves(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def setOctaves(self, octaves) -> None: ...
    def setThreshold(self, threshold) -> None: ...


class BackgroundSubtractor(Algorithm):
    def apply(self, *args, **kwargs): ...  # incomplete
    def getBackgroundImage(self, *args, **kwargs): ...  # incomplete


class BackgroundSubtractorKNN(BackgroundSubtractor):
    def getDetectShadows(self, *args, **kwargs): ...  # incomplete
    def getDist2Threshold(self, *args, **kwargs): ...  # incomplete
    def getHistory(self, *args, **kwargs): ...  # incomplete
    def getNSamples(self, *args, **kwargs): ...  # incomplete
    def getShadowThreshold(self, *args, **kwargs): ...  # incomplete
    def getShadowValue(self, *args, **kwargs): ...  # incomplete
    def getkNNSamples(self, *args, **kwargs): ...  # incomplete
    def setDetectShadows(self, detectShadows) -> None: ...
    def setDist2Threshold(self, _dist2Threshold) -> None: ...
    def setHistory(self, history) -> None: ...
    def setNSamples(self, _nN) -> None: ...
    def setShadowThreshold(self, threshold) -> None: ...
    def setShadowValue(self, value) -> None: ...
    def setkNNSamples(self, _nkNN) -> None: ...


class BackgroundSubtractorMOG2(BackgroundSubtractor):
    def apply(self, *args, **kwargs): ...  # incomplete
    def getBackgroundRatio(self, *args, **kwargs): ...  # incomplete
    def getComplexityReductionThreshold(self, *args, **kwargs): ...  # incomplete
    def getDetectShadows(self, *args, **kwargs): ...  # incomplete
    def getHistory(self, *args, **kwargs): ...  # incomplete
    def getNMixtures(self, *args, **kwargs): ...  # incomplete
    def getShadowThreshold(self, *args, **kwargs): ...  # incomplete
    def getShadowValue(self, *args, **kwargs): ...  # incomplete
    def getVarInit(self, *args, **kwargs): ...  # incomplete
    def getVarMax(self, *args, **kwargs): ...  # incomplete
    def getVarMin(self, *args, **kwargs): ...  # incomplete
    def getVarThreshold(self, *args, **kwargs): ...  # incomplete
    def getVarThresholdGen(self, *args, **kwargs): ...  # incomplete
    def setBackgroundRatio(self, ratio) -> None: ...
    def setComplexityReductionThreshold(self, ct) -> None: ...
    def setDetectShadows(self, detectShadows) -> None: ...
    def setHistory(self, history) -> None: ...
    def setNMixtures(self, nmixtures) -> None: ...
    def setShadowThreshold(self, threshold) -> None: ...
    def setShadowValue(self, value) -> None: ...
    def setVarInit(self, varInit) -> None: ...
    def setVarMax(self, varMax) -> None: ...
    def setVarMin(self, varMin) -> None: ...
    def setVarThreshold(self, varThreshold) -> None: ...
    def setVarThresholdGen(self, varThresholdGen) -> None: ...


class BaseCascadeClassifier(Algorithm): ...


class CLAHE(Algorithm):
    def apply(self, *args, **kwargs): ...  # incomplete
    def collectGarbage(self) -> None: ...
    def getClipLimit(self, *args, **kwargs): ...  # incomplete
    def getTilesGridSize(self, *args, **kwargs): ...  # incomplete
    def setClipLimit(self, clipLimit) -> None: ...
    def setTilesGridSize(self, tileGridSize) -> None: ...


class CalibrateCRF(Algorithm):
    def process(self, *args, **kwargs): ...  # incomplete


class CalibrateDebevec(CalibrateCRF):
    def getLambda(self, *args, **kwargs): ...  # incomplete
    def getRandom(self, *args, **kwargs): ...  # incomplete
    def getSamples(self, *args, **kwargs): ...  # incomplete
    def setLambda(self, lambda_) -> None: ...
    def setRandom(self, random) -> None: ...
    def setSamples(self, samples) -> None: ...


class CalibrateRobertson(CalibrateCRF):
    def getMaxIter(self, *args, **kwargs): ...  # incomplete
    def getRadiance(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def setMaxIter(self, max_iter) -> None: ...
    def setThreshold(self, threshold) -> None: ...


class CascadeClassifier:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def convert(self, *args, **kwargs): ...  # incomplete
    def detectMultiScale(self, *args, **kwargs): ...  # incomplete
    def detectMultiScale2(self, *args, **kwargs): ...  # incomplete
    def detectMultiScale3(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def getFeatureType(self, *args, **kwargs): ...  # incomplete
    def getOriginalWindowSize(self, *args, **kwargs): ...  # incomplete
    def isOldFormatCascade(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def read(self, *args, **kwargs): ...  # incomplete


class CirclesGridFinderParameters:
    convexHullFactor: Incomplete
    densityNeighborhoodSize: Incomplete
    edgeGain: Incomplete
    edgePenalty: Incomplete
    existingVertexGain: Incomplete
    keypointScale: Incomplete
    kmeansAttempts: Incomplete
    maxRectifiedDistance: Incomplete
    minDensity: Incomplete
    minDistanceToAddKeypoint: Incomplete
    minGraphConfidence: Incomplete
    minRNGEdgeSwitchDist: Incomplete
    squareSize: Incomplete
    vertexGain: Incomplete
    vertexPenalty: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class DISOpticalFlow(DenseOpticalFlow):
    def create(self, *args, **kwargs): ...  # incomplete
    def getFinestScale(self, *args, **kwargs): ...  # incomplete
    def getGradientDescentIterations(self, *args, **kwargs): ...  # incomplete
    def getPatchSize(self, *args, **kwargs): ...  # incomplete
    def getPatchStride(self, *args, **kwargs): ...  # incomplete
    def getUseMeanNormalization(self, *args, **kwargs): ...  # incomplete
    def getUseSpatialPropagation(self, *args, **kwargs): ...  # incomplete
    def getVariationalRefinementAlpha(self, *args, **kwargs): ...  # incomplete
    def getVariationalRefinementDelta(self, *args, **kwargs): ...  # incomplete
    def getVariationalRefinementGamma(self, *args, **kwargs): ...  # incomplete
    def getVariationalRefinementIterations(self, *args, **kwargs): ...  # incomplete
    def setFinestScale(self, val) -> None: ...
    def setGradientDescentIterations(self, val) -> None: ...
    def setPatchSize(self, val) -> None: ...
    def setPatchStride(self, val) -> None: ...
    def setUseMeanNormalization(self, val) -> None: ...
    def setUseSpatialPropagation(self, val) -> None: ...
    def setVariationalRefinementAlpha(self, val) -> None: ...
    def setVariationalRefinementDelta(self, val) -> None: ...
    def setVariationalRefinementGamma(self, val) -> None: ...
    def setVariationalRefinementIterations(self, val) -> None: ...


class DMatch:
    distance: Incomplete
    imgIdx: Incomplete
    queryIdx: Incomplete
    trainIdx: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class DenseOpticalFlow(Algorithm):
    def calc(self, I0, I1, flow) -> _flow: ...
    def collectGarbage(self) -> None: ...


class DescriptorMatcher(Algorithm):
    def add(self, descriptors) -> None: ...
    def clear(self) -> None: ...
    def clone(self, *args, **kwargs): ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def getTrainDescriptors(self, *args, **kwargs): ...  # incomplete
    def isMaskSupported(self, *args, **kwargs): ...  # incomplete
    def knnMatch(self, *args, **kwargs): ...  # incomplete
    def match(self, *args, **kwargs): ...  # incomplete
    def radiusMatch(self, *args, **kwargs): ...  # incomplete
    def read(self, fileName) -> None: ...
    def train(self) -> None: ...
    def write(self, fileName) -> None: ...


class FaceDetectorYN:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def getInputSize(self, *args, **kwargs): ...  # incomplete
    def getNMSThreshold(self, *args, **kwargs): ...  # incomplete
    def getScoreThreshold(self, *args, **kwargs): ...  # incomplete
    def getTopK(self, *args, **kwargs): ...  # incomplete
    def setInputSize(self, input_size) -> None: ...
    def setNMSThreshold(self, nms_threshold) -> None: ...
    def setScoreThreshold(self, score_threshold) -> None: ...
    def setTopK(self, top_k) -> None: ...


class FaceRecognizerSF:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def alignCrop(self, *args, **kwargs): ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def feature(self, *args, **kwargs): ...  # incomplete
    def match(self, *args, **kwargs): ...  # incomplete


class FarnebackOpticalFlow(DenseOpticalFlow):
    def create(self, *args, **kwargs): ...  # incomplete
    def getFastPyramids(self, *args, **kwargs): ...  # incomplete
    def getFlags(self, *args, **kwargs): ...  # incomplete
    def getNumIters(self, *args, **kwargs): ...  # incomplete
    def getNumLevels(self, *args, **kwargs): ...  # incomplete
    def getPolyN(self, *args, **kwargs): ...  # incomplete
    def getPolySigma(self, *args, **kwargs): ...  # incomplete
    def getPyrScale(self, *args, **kwargs): ...  # incomplete
    def getWinSize(self, *args, **kwargs): ...  # incomplete
    def setFastPyramids(self, fastPyramids) -> None: ...
    def setFlags(self, flags: int | None) -> None: ...
    def setNumIters(self, numIters) -> None: ...
    def setNumLevels(self, numLevels) -> None: ...
    def setPolyN(self, polyN) -> None: ...
    def setPolySigma(self, polySigma) -> None: ...
    def setPyrScale(self, pyrScale) -> None: ...
    def setWinSize(self, winSize) -> None: ...


class FastFeatureDetector(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getNonmaxSuppression(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def getType(self, *args, **kwargs): ...  # incomplete
    def setNonmaxSuppression(self, f) -> None: ...
    def setThreshold(self, threshold) -> None: ...
    def setType(self, type) -> None: ...


class Feature2D:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def compute(self, *args, **kwargs): ...  # incomplete
    def defaultNorm(self, *args, **kwargs): ...  # incomplete
    def descriptorSize(self, *args, **kwargs): ...  # incomplete
    def descriptorType(self, *args, **kwargs): ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def detectAndCompute(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    @overload
    def read(self, fileName) -> None: ...
    @overload
    def read(self, arg1) -> None: ...
    def write(self, fileName) -> None: ...


class FileNode:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def at(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def getNode(self, *args, **kwargs): ...  # incomplete
    def isInt(self, *args, **kwargs): ...  # incomplete
    def isMap(self, *args, **kwargs): ...  # incomplete
    def isNamed(self, *args, **kwargs): ...  # incomplete
    def isNone(self, *args, **kwargs): ...  # incomplete
    def isReal(self, *args, **kwargs): ...  # incomplete
    def isSeq(self, *args, **kwargs): ...  # incomplete
    def isString(self, *args, **kwargs): ...  # incomplete
    def keys(self, *args, **kwargs): ...  # incomplete
    def mat(self, *args, **kwargs): ...  # incomplete
    def name(self, *args, **kwargs): ...  # incomplete
    def rawSize(self, *args, **kwargs): ...  # incomplete
    def real(self, *args, **kwargs): ...  # incomplete
    def size(self, *args, **kwargs): ...  # incomplete
    def string(self, *args, **kwargs): ...  # incomplete
    def type(self, *args, **kwargs): ...  # incomplete


class FileStorage:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def endWriteStruct(self) -> None: ...
    def getFirstTopLevelNode(self, *args, **kwargs): ...  # incomplete
    def getFormat(self, *args, **kwargs): ...  # incomplete
    def getNode(self, *args, **kwargs): ...  # incomplete
    def isOpened(self, *args, **kwargs): ...  # incomplete
    def open(self, *args, **kwargs): ...  # incomplete
    def release(self) -> None: ...
    def releaseAndGetString(self, *args, **kwargs): ...  # incomplete
    def root(self, *args, **kwargs): ...  # incomplete
    def startWriteStruct(self, *args, **kwargs): ...  # incomplete
    def write(self, name, val) -> None: ...
    def writeComment(self, *args, **kwargs): ...  # incomplete


class FlannBasedMatcher(DescriptorMatcher):
    def __init__(self, indexParams=..., searchParams=...) -> None: ...
    def create(self, *args, **kwargs): ...  # incomplete


class GArrayDesc:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GArrayT:
    def __init__(self, type: int) -> None: ...
    def type(self) -> int: ...


class GCompileArg:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GComputation:
    def __init__(self, arg: gapi_GKernelPackage | gapi_GNetPackage | queue_capacity) -> None: ...
    def apply(self): ...
    def compileStreaming(self, *args, **kwargs): ...  # incomplete


class GFTTDetector(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getBlockSize(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getHarrisDetector(self, *args, **kwargs): ...  # incomplete
    def getK(self, *args, **kwargs): ...  # incomplete
    def getMaxFeatures(self, *args, **kwargs): ...  # incomplete
    def getMinDistance(self, *args, **kwargs): ...  # incomplete
    def getQualityLevel(self, *args, **kwargs): ...  # incomplete
    def setBlockSize(self, blockSize) -> None: ...
    def setHarrisDetector(self, val) -> None: ...
    def setK(self, k) -> None: ...
    def setMaxFeatures(self, maxFeatures) -> None: ...
    def setMinDistance(self, minDistance) -> None: ...
    def setQualityLevel(self, qlevel) -> None: ...


class GFrame:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GInferInputs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def setInput(self, *args, **kwargs): ...  # incomplete


class GInferListInputs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def setInput(self, *args, **kwargs): ...  # incomplete


class GInferListOutputs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def at(self, *args, **kwargs): ...  # incomplete


class GInferOutputs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def at(self, *args, **kwargs): ...  # incomplete


class GMat:
    def __init__(self) -> None: ...


class GMatDesc:
    chan: Incomplete
    depth: Incomplete
    dims: Incomplete
    planar: Incomplete
    size: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def asInterleaved(self, *args, **kwargs): ...  # incomplete
    def asPlanar(self, *args, **kwargs): ...  # incomplete
    def withDepth(self, *args, **kwargs): ...  # incomplete
    def withSize(self, *args, **kwargs): ...  # incomplete
    def withSizeDelta(self, *args, **kwargs): ...  # incomplete
    def withType(self, *args, **kwargs): ...  # incomplete


class GOpaqueDesc:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GOpaqueT:
    def __init__(self, type: int) -> None: ...
    def type(self) -> int: ...


class GScalar:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GScalarDesc:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class GStreamingCompiled:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def pull(self, *args, **kwargs): ...  # incomplete
    def running(self, *args, **kwargs): ...  # incomplete
    def setSource(self, callback) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


class GeneralizedHough(Algorithm):
    def detect(self, *args, **kwargs): ...  # incomplete
    def getCannyHighThresh(self, *args, **kwargs): ...  # incomplete
    def getCannyLowThresh(self, *args, **kwargs): ...  # incomplete
    def getDp(self, *args, **kwargs): ...  # incomplete
    def getMaxBufferSize(self, *args, **kwargs): ...  # incomplete
    def getMinDist(self, *args, **kwargs): ...  # incomplete
    def setCannyHighThresh(self, cannyHighThresh) -> None: ...
    def setCannyLowThresh(self, cannyLowThresh) -> None: ...
    def setDp(self, dp) -> None: ...
    def setMaxBufferSize(self, maxBufferSize) -> None: ...
    def setMinDist(self, minDist) -> None: ...
    def setTemplate(self, *args, **kwargs): ...  # incomplete


class GeneralizedHoughBallard(GeneralizedHough):
    def getLevels(self, *args, **kwargs): ...  # incomplete
    def getVotesThreshold(self, *args, **kwargs): ...  # incomplete
    def setLevels(self, levels) -> None: ...
    def setVotesThreshold(self, votesThreshold) -> None: ...


class GeneralizedHoughGuil(GeneralizedHough):
    def getAngleEpsilon(self, *args, **kwargs): ...  # incomplete
    def getAngleStep(self, *args, **kwargs): ...  # incomplete
    def getAngleThresh(self, *args, **kwargs): ...  # incomplete
    def getLevels(self, *args, **kwargs): ...  # incomplete
    def getMaxAngle(self, *args, **kwargs): ...  # incomplete
    def getMaxScale(self, *args, **kwargs): ...  # incomplete
    def getMinAngle(self, *args, **kwargs): ...  # incomplete
    def getMinScale(self, *args, **kwargs): ...  # incomplete
    def getPosThresh(self, *args, **kwargs): ...  # incomplete
    def getScaleStep(self, *args, **kwargs): ...  # incomplete
    def getScaleThresh(self, *args, **kwargs): ...  # incomplete
    def getXi(self, *args, **kwargs): ...  # incomplete
    def setAngleEpsilon(self, angleEpsilon) -> None: ...
    def setAngleStep(self, angleStep) -> None: ...
    def setAngleThresh(self, angleThresh) -> None: ...
    def setLevels(self, levels) -> None: ...
    def setMaxAngle(self, maxAngle) -> None: ...
    def setMaxScale(self, maxScale) -> None: ...
    def setMinAngle(self, minAngle) -> None: ...
    def setMinScale(self, minScale) -> None: ...
    def setPosThresh(self, posThresh) -> None: ...
    def setScaleStep(self, scaleStep) -> None: ...
    def setScaleThresh(self, scaleThresh) -> None: ...
    def setXi(self, xi) -> None: ...


class HOGDescriptor:
    L2HysThreshold: Incomplete
    blockSize: Incomplete
    blockStride: Incomplete
    cellSize: Incomplete
    derivAperture: Incomplete
    gammaCorrection: Incomplete
    histogramNormType: Incomplete
    nbins: Incomplete
    nlevels: Incomplete
    signedGradient: Incomplete
    svmDetector: Incomplete
    winSigma: Incomplete
    winSize: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def checkDetectorSize(self, *args, **kwargs): ...  # incomplete
    def compute(self, *args, **kwargs): ...  # incomplete
    def computeGradient(self, *args, **kwargs): ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def detectMultiScale(self, *args, **kwargs): ...  # incomplete
    def getDaimlerPeopleDetector(self, *args, **kwargs): ...  # incomplete
    def getDefaultPeopleDetector(self, *args, **kwargs): ...  # incomplete
    def getDescriptorSize(self, *args, **kwargs): ...  # incomplete
    def getWinSigma(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def save(self, *args, **kwargs): ...  # incomplete
    def setSVMDetector(self, svmdetector) -> None: ...


class KAZE(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getDiffusivity(self, *args, **kwargs): ...  # incomplete
    def getExtended(self, *args, **kwargs): ...  # incomplete
    def getNOctaveLayers(self, *args, **kwargs): ...  # incomplete
    def getNOctaves(self, *args, **kwargs): ...  # incomplete
    def getThreshold(self, *args, **kwargs): ...  # incomplete
    def getUpright(self, *args, **kwargs): ...  # incomplete
    def setDiffusivity(self, diff) -> None: ...
    def setExtended(self, extended) -> None: ...
    def setNOctaveLayers(self, octaveLayers) -> None: ...
    def setNOctaves(self, octaves) -> None: ...
    def setThreshold(self, threshold) -> None: ...
    def setUpright(self, upright) -> None: ...


class KalmanFilter:
    controlMatrix: Incomplete
    errorCovPost: Incomplete
    errorCovPre: Incomplete
    gain: Incomplete
    measurementMatrix: Incomplete
    measurementNoiseCov: Incomplete
    processNoiseCov: Incomplete
    statePost: Incomplete
    statePre: Incomplete
    transitionMatrix: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def correct(self, *args, **kwargs): ...  # incomplete
    def predict(self, *args, **kwargs): ...  # incomplete


class KeyPoint:
    angle: Incomplete
    class_id: Incomplete
    octave: Incomplete
    pt: Incomplete
    response: Incomplete
    size: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def convert(self, *args, **kwargs): ...  # incomplete
    def overlap(self, *args, **kwargs): ...  # incomplete


class LineSegmentDetector(Algorithm):
    def compareSegments(self, *args, **kwargs): ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def drawSegments(self, image, lines) -> _image: ...


class MSER(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def detectRegions(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getDelta(self, *args, **kwargs): ...  # incomplete
    def getMaxArea(self, *args, **kwargs): ...  # incomplete
    def getMinArea(self, *args, **kwargs): ...  # incomplete
    def getPass2Only(self, *args, **kwargs): ...  # incomplete
    def setDelta(self, delta) -> None: ...
    def setMaxArea(self, maxArea) -> None: ...
    def setMinArea(self, minArea) -> None: ...
    def setPass2Only(self, f) -> None: ...


class MergeDebevec(MergeExposures):
    def process(self, *args, **kwargs): ...  # incomplete


class MergeExposures(Algorithm):
    def process(self, *args, **kwargs): ...  # incomplete


class MergeMertens(MergeExposures):
    def getContrastWeight(self, *args, **kwargs): ...  # incomplete
    def getExposureWeight(self, *args, **kwargs): ...  # incomplete
    def getSaturationWeight(self, *args, **kwargs): ...  # incomplete
    def process(self, *args, **kwargs): ...  # incomplete
    def setContrastWeight(self, contrast_weiht) -> None: ...
    def setExposureWeight(self, exposure_weight) -> None: ...
    def setSaturationWeight(self, saturation_weight) -> None: ...


class MergeRobertson(MergeExposures):
    def process(self, *args, **kwargs): ...  # incomplete


class ORB(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete
    def getEdgeThreshold(self, *args, **kwargs): ...  # incomplete
    def getFastThreshold(self, *args, **kwargs): ...  # incomplete
    def getFirstLevel(self, *args, **kwargs): ...  # incomplete
    def getMaxFeatures(self, *args, **kwargs): ...  # incomplete
    def getNLevels(self, *args, **kwargs): ...  # incomplete
    def getPatchSize(self, *args, **kwargs): ...  # incomplete
    def getScaleFactor(self, *args, **kwargs): ...  # incomplete
    def getScoreType(self, *args, **kwargs): ...  # incomplete
    def getWTA_K(self, *args, **kwargs): ...  # incomplete
    def setEdgeThreshold(self, edgeThreshold) -> None: ...
    def setFastThreshold(self, fastThreshold) -> None: ...
    def setFirstLevel(self, firstLevel) -> None: ...
    def setMaxFeatures(self, maxFeatures) -> None: ...
    def setNLevels(self, nlevels) -> None: ...
    def setPatchSize(self, patchSize) -> None: ...
    def setScaleFactor(self, scaleFactor) -> None: ...
    def setScoreType(self, scoreType) -> None: ...
    def setWTA_K(self, wta_k) -> None: ...


class PyRotationWarper:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def buildMaps(self, *args, **kwargs): ...  # incomplete
    def getScale(self, *args, **kwargs): ...  # incomplete
    def setScale(self, arg1) -> None: ...
    def warp(self, *args, **kwargs): ...  # incomplete
    def warpBackward(self, *args, **kwargs): ...  # incomplete
    def warpPoint(self, *args, **kwargs): ...  # incomplete
    def warpPointBackward(self, *args, **kwargs): ...  # incomplete
    def warpRoi(self, *args, **kwargs): ...  # incomplete


class QRCodeDetector:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def decode(self, *args, **kwargs): ...  # incomplete
    def decodeCurved(self, *args, **kwargs): ...  # incomplete
    def decodeMulti(self, *args, **kwargs): ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def detectAndDecode(self, *args, **kwargs): ...  # incomplete
    def detectAndDecodeCurved(self, *args, **kwargs): ...  # incomplete
    def detectAndDecodeMulti(self, *args, **kwargs): ...  # incomplete
    def detectMulti(self, *args, **kwargs): ...  # incomplete
    def setEpsX(self, epsX) -> None: ...
    def setEpsY(self, epsY) -> None: ...


class QRCodeEncoder:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def encode(self, *args, **kwargs): ...  # incomplete
    def encodeStructuredAppend(self, *args, **kwargs): ...  # incomplete


class QRCodeEncoder_Params:
    correction_level: Incomplete
    mode: Incomplete
    structure_number: Incomplete
    version: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class SIFT(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete


class SimpleBlobDetector(Feature2D):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getDefaultName(self, *args, **kwargs): ...  # incomplete


class SimpleBlobDetector_Params:
    blobColor: Incomplete
    filterByArea: Incomplete
    filterByCircularity: Incomplete
    filterByColor: Incomplete
    filterByConvexity: Incomplete
    filterByInertia: Incomplete
    maxArea: Incomplete
    maxCircularity: Incomplete
    maxConvexity: Incomplete
    maxInertiaRatio: Incomplete
    maxThreshold: Incomplete
    minArea: Incomplete
    minCircularity: Incomplete
    minConvexity: Incomplete
    minDistBetweenBlobs: Incomplete
    minInertiaRatio: Incomplete
    minRepeatability: Incomplete
    minThreshold: Incomplete
    thresholdStep: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class SparseOpticalFlow(Algorithm):
    def calc(self, *args, **kwargs): ...  # incomplete


class SparsePyrLKOpticalFlow(SparseOpticalFlow):
    def create(self, *args, **kwargs): ...  # incomplete
    def getFlags(self, *args, **kwargs): ...  # incomplete
    def getMaxLevel(self, *args, **kwargs): ...  # incomplete
    def getMinEigThreshold(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getWinSize(self, *args, **kwargs): ...  # incomplete
    def setFlags(self, flags: int | None) -> None: ...
    def setMaxLevel(self, maxLevel) -> None: ...
    def setMinEigThreshold(self, minEigThreshold) -> None: ...
    def setTermCriteria(self, crit) -> None: ...
    def setWinSize(self, winSize) -> None: ...


class StereoBM(StereoMatcher):
    def create(self, *args, **kwargs): ...  # incomplete
    def getPreFilterCap(self, *args, **kwargs): ...  # incomplete
    def getPreFilterSize(self, *args, **kwargs): ...  # incomplete
    def getPreFilterType(self, *args, **kwargs): ...  # incomplete
    def getROI1(self, *args, **kwargs): ...  # incomplete
    def getROI2(self, *args, **kwargs): ...  # incomplete
    def getSmallerBlockSize(self, *args, **kwargs): ...  # incomplete
    def getTextureThreshold(self, *args, **kwargs): ...  # incomplete
    def getUniquenessRatio(self, *args, **kwargs): ...  # incomplete
    def setPreFilterCap(self, preFilterCap) -> None: ...
    def setPreFilterSize(self, preFilterSize) -> None: ...
    def setPreFilterType(self, preFilterType) -> None: ...
    def setROI1(self, roi1) -> None: ...
    def setROI2(self, roi2) -> None: ...
    def setSmallerBlockSize(self, blockSize) -> None: ...
    def setTextureThreshold(self, textureThreshold) -> None: ...
    def setUniquenessRatio(self, uniquenessRatio) -> None: ...


class StereoMatcher(Algorithm):
    def compute(self, *args, **kwargs): ...  # incomplete
    def getBlockSize(self, *args, **kwargs): ...  # incomplete
    def getDisp12MaxDiff(self, *args, **kwargs): ...  # incomplete
    def getMinDisparity(self, *args, **kwargs): ...  # incomplete
    def getNumDisparities(self, *args, **kwargs): ...  # incomplete
    def getSpeckleRange(self, *args, **kwargs): ...  # incomplete
    def getSpeckleWindowSize(self, *args, **kwargs): ...  # incomplete
    def setBlockSize(self, blockSize) -> None: ...
    def setDisp12MaxDiff(self, disp12MaxDiff) -> None: ...
    def setMinDisparity(self, minDisparity) -> None: ...
    def setNumDisparities(self, numDisparities) -> None: ...
    def setSpeckleRange(self, speckleRange) -> None: ...
    def setSpeckleWindowSize(self, speckleWindowSize) -> None: ...


class StereoSGBM(StereoMatcher):
    def create(self, *args, **kwargs): ...  # incomplete
    def getMode(self, *args, **kwargs): ...  # incomplete
    def getP1(self, *args, **kwargs): ...  # incomplete
    def getP2(self, *args, **kwargs): ...  # incomplete
    def getPreFilterCap(self, *args, **kwargs): ...  # incomplete
    def getUniquenessRatio(self, *args, **kwargs): ...  # incomplete
    def setMode(self, mode) -> None: ...
    def setP1(self, P1) -> None: ...
    def setP2(self, P2) -> None: ...
    def setPreFilterCap(self, preFilterCap) -> None: ...
    def setUniquenessRatio(self, uniquenessRatio) -> None: ...


class Stitcher:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def composePanorama(self, *args, **kwargs): ...  # incomplete
    def compositingResol(self, *args, **kwargs): ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def estimateTransform(self, *args, **kwargs): ...  # incomplete
    def interpolationFlags(self, *args, **kwargs): ...  # incomplete
    def panoConfidenceThresh(self, *args, **kwargs): ...  # incomplete
    def registrationResol(self, *args, **kwargs): ...  # incomplete
    def seamEstimationResol(self, *args, **kwargs): ...  # incomplete
    def setCompositingResol(self, resol_mpx) -> None: ...
    def setInterpolationFlags(self, interp_flags: int | None) -> None: ...
    def setPanoConfidenceThresh(self, conf_thresh) -> None: ...
    def setRegistrationResol(self, resol_mpx) -> None: ...
    def setSeamEstimationResol(self, resol_mpx) -> None: ...
    def setWaveCorrection(self, flag) -> None: ...
    def stitch(self, *args, **kwargs): ...  # incomplete
    def waveCorrection(self, *args, **kwargs): ...  # incomplete
    def workScale(self, *args, **kwargs): ...  # incomplete


class Subdiv2D:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def edgeDst(self, *args, **kwargs): ...  # incomplete
    def edgeOrg(self, *args, **kwargs): ...  # incomplete
    def findNearest(self, *args, **kwargs): ...  # incomplete
    def getEdge(self, *args, **kwargs): ...  # incomplete
    def getEdgeList(self) -> _edgeList: ...
    def getLeadingEdgeList(self) -> _leadingEdgeList: ...
    def getTriangleList(self) -> _triangleList: ...
    def getVertex(self, *args, **kwargs): ...  # incomplete
    def getVoronoiFacetList(self, *args, **kwargs): ...  # incomplete
    def initDelaunay(self, rect) -> None: ...
    def insert(self, ptvec) -> None: ...
    def locate(self, *args, **kwargs): ...  # incomplete
    def nextEdge(self, *args, **kwargs): ...  # incomplete
    def rotateEdge(self, *args, **kwargs): ...  # incomplete
    def symEdge(self, *args, **kwargs): ...  # incomplete


class TickMeter:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getAvgTimeMilli(self, *args, **kwargs): ...  # incomplete
    def getAvgTimeSec(self, *args, **kwargs): ...  # incomplete
    def getCounter(self, *args, **kwargs): ...  # incomplete
    def getFPS(self, *args, **kwargs): ...  # incomplete
    def getTimeMicro(self, *args, **kwargs): ...  # incomplete
    def getTimeMilli(self, *args, **kwargs): ...  # incomplete
    def getTimeSec(self, *args, **kwargs): ...  # incomplete
    def getTimeTicks(self, *args, **kwargs): ...  # incomplete
    def reset(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


class Tonemap(Algorithm):
    def getGamma(self, *args, **kwargs): ...  # incomplete
    def process(self, *args, **kwargs): ...  # incomplete
    def setGamma(self, gamma) -> None: ...


class TonemapDrago(Tonemap):
    def getBias(self, *args, **kwargs): ...  # incomplete
    def getSaturation(self, *args, **kwargs): ...  # incomplete
    def setBias(self, bias) -> None: ...
    def setSaturation(self, saturation) -> None: ...


class TonemapMantiuk(Tonemap):
    def getSaturation(self, *args, **kwargs): ...  # incomplete
    def getScale(self, *args, **kwargs): ...  # incomplete
    def setSaturation(self, saturation) -> None: ...
    def setScale(self, scale) -> None: ...


class TonemapReinhard(Tonemap):
    def getColorAdaptation(self, *args, **kwargs): ...  # incomplete
    def getIntensity(self, *args, **kwargs): ...  # incomplete
    def getLightAdaptation(self, *args, **kwargs): ...  # incomplete
    def setColorAdaptation(self, color_adapt) -> None: ...
    def setIntensity(self, intensity) -> None: ...
    def setLightAdaptation(self, light_adapt) -> None: ...


class Tracker:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def init(self, image, boundingBox) -> None: ...
    def update(self, *args, **kwargs): ...  # incomplete


class TrackerDaSiamRPN(Tracker):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getTrackingScore(self, *args, **kwargs): ...  # incomplete


class TrackerDaSiamRPN_Params:
    backend: Incomplete
    kernel_cls1: Incomplete
    kernel_r1: Incomplete
    model: Incomplete
    target: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class TrackerGOTURN(Tracker):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete


class TrackerGOTURN_Params:
    modelBin: Incomplete
    modelTxt: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class TrackerMIL(Tracker):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete


class TrackerMIL_Params:
    featureSetNumFeatures: Incomplete
    samplerInitInRadius: Incomplete
    samplerInitMaxNegNum: Incomplete
    samplerSearchWinSize: Incomplete
    samplerTrackInRadius: Incomplete
    samplerTrackMaxNegNum: Incomplete
    samplerTrackMaxPosNum: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class UMat:
    offset: Incomplete
    @overload
    def __init__(self, usageFlags: int | None = ...) -> None: ...
    @overload
    def __init__(self, rows: int | None, cols: int | None, type: int | None, usageFlags: int | None = ...) -> None: ...
    @overload
    def __init__(self, size: _Size | None, type: int | None, usageFlags: int | None = ...) -> None: ...

    @overload
    def __init__(
        self, rows: int | None, cols: int | None, type: int | None, s: _Scalar, usageFlags: int | None = ...,
    ) -> None: ...
    @overload
    def __init__(self, size: _Size | None, type: int | None, s: _Scalar, usageFlags: int | None = ...) -> None: ...
    @overload
    def __init__(self, m: _UMat) -> None: ...
    @overload
    def __init__(self, m: _UMat, rowRange: _Range | None, colRange: _Range | None = ...) -> None: ...
    @overload
    def __init__(self, m: _UMat, roi: _Rect | None) -> None: ...
    @overload
    def __init__(self, m: _UMat, ranges: Sequence[_Range | None] | None) -> None: ...
    @staticmethod
    def context(): ...
    def get(self): ...
    def handle(self, accessFlags): ...
    def isContinuous(self): ...
    def isSubmatrix(self): ...
    @staticmethod
    def queue(): ...


class UsacParams:
    confidence: Incomplete
    isParallel: Incomplete
    loIterations: Incomplete
    loMethod: Incomplete
    loSampleSize: Incomplete
    maxIterations: Incomplete
    neighborsSearch: Incomplete
    randomGeneratorState: Incomplete
    sampler: Incomplete
    score: Incomplete
    threshold: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class VariationalRefinement(DenseOpticalFlow):
    def calcUV(self, *args, **kwargs): ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getAlpha(self, *args, **kwargs): ...  # incomplete
    def getDelta(self, *args, **kwargs): ...  # incomplete
    def getFixedPointIterations(self, *args, **kwargs): ...  # incomplete
    def getGamma(self, *args, **kwargs): ...  # incomplete
    def getOmega(self, *args, **kwargs): ...  # incomplete
    def getSorIterations(self, *args, **kwargs): ...  # incomplete
    def setAlpha(self, val) -> None: ...
    def setDelta(self, val) -> None: ...
    def setFixedPointIterations(self, val) -> None: ...
    def setGamma(self, val) -> None: ...
    def setOmega(self, val) -> None: ...
    def setSorIterations(self, val) -> None: ...


class VideoCapture:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    @overload
    def __init__(self, filename: str, apiPreference: int | None, params: Sequence[int] = ...) -> None: ...
    @overload
    def __init__(self, index: int) -> None: ...
    @overload
    def __init__(self, index: int, apiPreference: int | None, params: Sequence[int] = ...) -> None: ...
    def get(self, propId: int) -> float: ...
    def getBackendName(self) -> str: ...
    def getExceptionMode(self) -> bool: ...
    def grab(self) -> bool: ...
    def isOpened(self) -> bool: ...
    @overload
    def open(self, filename: str, apiPreference: int = ...) -> bool: ...
    @overload
    def open(self, filename: str, apiPreference: int, params: Sequence[int]) -> bool: ...
    @overload
    def open(self, index: int, apiPreference: int = ...) -> bool: ...
    @overload
    def open(self, index: int, apiPreference: int, params: Sequence[int]) -> bool: ...
    @overload
    def read(self, image: Mat | None = ...) -> tuple[bool, Mat]: ...
    @overload
    def read(self, image: _UMat) -> tuple[bool, UMat]: ...
    def release(self) -> None: ...
    @overload
    def retrieve(self, image: Mat | None = ..., flag: int = ...) -> tuple[bool, Mat]: ...
    @overload
    def retrieve(self, image: _UMat, flag: int = ...) -> tuple[bool, UMat]: ...
    def set(self, propId: int, value: float) -> bool: ...
    def setExceptionMode(self, enable: bool) -> None: ...


class VideoWriter:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def fourcc(self, *args, **kwargs): ...  # incomplete
    def get(self, *args, **kwargs): ...  # incomplete
    def getBackendName(self, *args, **kwargs): ...  # incomplete
    def isOpened(self, *args, **kwargs): ...  # incomplete
    def open(self, *args, **kwargs): ...  # incomplete
    def release(self) -> None: ...
    def set(self, *args, **kwargs): ...  # incomplete
    def write(self, image) -> None: ...


class WarperCreator:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class cuda_BufferPool:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getAllocator(self, *args, **kwargs): ...  # incomplete
    def getBuffer(self, *args, **kwargs): ...  # incomplete


class cuda_DeviceInfo:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def ECCEnabled(self, *args, **kwargs): ...  # incomplete
    def asyncEngineCount(self, *args, **kwargs): ...  # incomplete
    def canMapHostMemory(self, *args, **kwargs): ...  # incomplete
    def clockRate(self, *args, **kwargs): ...  # incomplete
    def computeMode(self, *args, **kwargs): ...  # incomplete
    def concurrentKernels(self, *args, **kwargs): ...  # incomplete
    def deviceID(self, *args, **kwargs): ...  # incomplete
    def freeMemory(self, *args, **kwargs): ...  # incomplete
    def integrated(self, *args, **kwargs): ...  # incomplete
    def isCompatible(self, *args, **kwargs): ...  # incomplete
    def kernelExecTimeoutEnabled(self, *args, **kwargs): ...  # incomplete
    def l2CacheSize(self, *args, **kwargs): ...  # incomplete
    def majorVersion(self, *args, **kwargs): ...  # incomplete
    def maxGridSize(self, *args, **kwargs): ...  # incomplete
    def maxSurface1D(self, *args, **kwargs): ...  # incomplete
    def maxSurface1DLayered(self, *args, **kwargs): ...  # incomplete
    def maxSurface2D(self, *args, **kwargs): ...  # incomplete
    def maxSurface2DLayered(self, *args, **kwargs): ...  # incomplete
    def maxSurface3D(self, *args, **kwargs): ...  # incomplete
    def maxSurfaceCubemap(self, *args, **kwargs): ...  # incomplete
    def maxSurfaceCubemapLayered(self, *args, **kwargs): ...  # incomplete
    def maxTexture1D(self, *args, **kwargs): ...  # incomplete
    def maxTexture1DLayered(self, *args, **kwargs): ...  # incomplete
    def maxTexture1DLinear(self, *args, **kwargs): ...  # incomplete
    def maxTexture1DMipmap(self, *args, **kwargs): ...  # incomplete
    def maxTexture2D(self, *args, **kwargs): ...  # incomplete
    def maxTexture2DGather(self, *args, **kwargs): ...  # incomplete
    def maxTexture2DLayered(self, *args, **kwargs): ...  # incomplete
    def maxTexture2DLinear(self, *args, **kwargs): ...  # incomplete
    def maxTexture2DMipmap(self, *args, **kwargs): ...  # incomplete
    def maxTexture3D(self, *args, **kwargs): ...  # incomplete
    def maxTextureCubemap(self, *args, **kwargs): ...  # incomplete
    def maxTextureCubemapLayered(self, *args, **kwargs): ...  # incomplete
    def maxThreadsDim(self, *args, **kwargs): ...  # incomplete
    def maxThreadsPerBlock(self, *args, **kwargs): ...  # incomplete
    def maxThreadsPerMultiProcessor(self, *args, **kwargs): ...  # incomplete
    def memPitch(self, *args, **kwargs): ...  # incomplete
    def memoryBusWidth(self, *args, **kwargs): ...  # incomplete
    def memoryClockRate(self, *args, **kwargs): ...  # incomplete
    def minorVersion(self, *args, **kwargs): ...  # incomplete
    def multiProcessorCount(self, *args, **kwargs): ...  # incomplete
    def pciBusID(self, *args, **kwargs): ...  # incomplete
    def pciDeviceID(self, *args, **kwargs): ...  # incomplete
    def pciDomainID(self, *args, **kwargs): ...  # incomplete
    def queryMemory(self, totalMemory, freeMemory) -> None: ...
    def regsPerBlock(self, *args, **kwargs): ...  # incomplete
    def sharedMemPerBlock(self, *args, **kwargs): ...  # incomplete
    def surfaceAlignment(self, *args, **kwargs): ...  # incomplete
    def tccDriver(self, *args, **kwargs): ...  # incomplete
    def textureAlignment(self, *args, **kwargs): ...  # incomplete
    def texturePitchAlignment(self, *args, **kwargs): ...  # incomplete
    def totalConstMem(self, *args, **kwargs): ...  # incomplete
    def totalGlobalMem(self, *args, **kwargs): ...  # incomplete
    def totalMemory(self, *args, **kwargs): ...  # incomplete
    def unifiedAddressing(self, *args, **kwargs): ...  # incomplete
    def warpSize(self, *args, **kwargs): ...  # incomplete


class cuda_Event:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def elapsedTime(self, *args, **kwargs): ...  # incomplete
    def queryIfComplete(self, *args, **kwargs): ...  # incomplete
    def record(self, *args, **kwargs): ...  # incomplete
    def waitForCompletion(self) -> None: ...


class cuda_GpuData:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class cuda_GpuMat:
    step: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def adjustROI(self, *args, **kwargs): ...  # incomplete
    def assignTo(self, *args, **kwargs): ...  # incomplete
    def channels(self, *args, **kwargs): ...  # incomplete
    def clone(self, *args, **kwargs): ...  # incomplete
    def col(self, *args, **kwargs): ...  # incomplete
    def colRange(self, *args, **kwargs): ...  # incomplete
    def convertTo(self, *args, **kwargs): ...  # incomplete
    def copyTo(self, *args, **kwargs): ...  # incomplete
    @overload
    def create(self, rows, cols, type) -> None: ...
    @overload
    def create(self, size, type) -> None: ...
    def cudaPtr(self, *args, **kwargs): ...  # incomplete
    def defaultAllocator(self, *args, **kwargs): ...  # incomplete
    def depth(self, *args, **kwargs): ...  # incomplete
    def download(self, *args, **kwargs): ...  # incomplete
    def elemSize(self, *args, **kwargs): ...  # incomplete
    def elemSize1(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def isContinuous(self, *args, **kwargs): ...  # incomplete
    def locateROI(self, wholeSize, ofs) -> None: ...
    def reshape(self, *args, **kwargs): ...  # incomplete
    def row(self, *args, **kwargs): ...  # incomplete
    def rowRange(self, *args, **kwargs): ...  # incomplete
    def setDefaultAllocator(self, *args, **kwargs): ...  # incomplete
    def setTo(self, *args, **kwargs): ...  # incomplete
    def size(self, *args, **kwargs): ...  # incomplete
    def step1(self, *args, **kwargs): ...  # incomplete
    def swap(self, mat) -> None: ...
    def type(self, *args, **kwargs): ...  # incomplete
    def updateContinuityFlag(self) -> None: ...
    @overload
    def upload(self, arr) -> None: ...
    @overload
    def upload(self, arr, stream) -> None: ...


class cuda_GpuMatND:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class cuda_GpuMat_Allocator:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class cuda_HostMem:
    step: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def channels(self, *args, **kwargs): ...  # incomplete
    def clone(self, *args, **kwargs): ...  # incomplete
    def create(self, rows, cols, type) -> None: ...
    def createMatHeader(self, *args, **kwargs): ...  # incomplete
    def depth(self, *args, **kwargs): ...  # incomplete
    def elemSize(self, *args, **kwargs): ...  # incomplete
    def elemSize1(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def isContinuous(self, *args, **kwargs): ...  # incomplete
    def reshape(self, *args, **kwargs): ...  # incomplete
    def size(self, *args, **kwargs): ...  # incomplete
    def step1(self, *args, **kwargs): ...  # incomplete
    def swap(self, b) -> None: ...
    def type(self, *args, **kwargs): ...  # incomplete


class cuda_Stream:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    @staticmethod
    def Null() -> cuda_Stream: ...
    def cudaPtr(self, *args, **kwargs): ...  # incomplete
    def queryIfComplete(self, *args, **kwargs): ...  # incomplete
    def waitEvent(self, event) -> None: ...
    def waitForCompletion(self) -> None: ...


class cuda_TargetArchs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def has(self, *args, **kwargs): ...  # incomplete
    def hasBin(self, *args, **kwargs): ...  # incomplete
    def hasEqualOrGreater(self, *args, **kwargs): ...  # incomplete
    def hasEqualOrGreaterBin(self, *args, **kwargs): ...  # incomplete
    def hasEqualOrGreaterPtx(self, *args, **kwargs): ...  # incomplete
    def hasEqualOrLessPtx(self, *args, **kwargs): ...  # incomplete
    def hasPtx(self, *args, **kwargs): ...  # incomplete


class detail_AffineBasedEstimator(detail_Estimator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_AffineBestOf2NearestMatcher(detail_BestOf2NearestMatcher):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_BestOf2NearestMatcher(detail_FeaturesMatcher):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def collectGarbage(self) -> None: ...
    def create(self, *args, **kwargs): ...  # incomplete


class detail_BestOf2NearestRangeMatcher(detail_BestOf2NearestMatcher):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_Blender:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def blend(self, *args, **kwargs): ...  # incomplete
    def createDefault(self, *args, **kwargs): ...  # incomplete
    def feed(self, img, mask, tl) -> None: ...
    @overload
    def prepare(self, corners, sizes) -> None: ...
    @overload
    def prepare(self, dst_roi) -> None: ...


class detail_BlocksChannelsCompensator(detail_BlocksCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_BlocksCompensator(detail_ExposureCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, index, corner, image, mask) -> _image: ...
    def getBlockSize(self, *args, **kwargs): ...  # incomplete
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def getNrFeeds(self, *args, **kwargs): ...  # incomplete
    def getNrGainsFilteringIterations(self, *args, **kwargs): ...  # incomplete
    def getSimilarityThreshold(self, *args, **kwargs): ...  # incomplete
    @overload
    def setBlockSize(self, width, height) -> None: ...
    @overload
    def setBlockSize(self, size) -> None: ...
    def setMatGains(self, umv) -> None: ...
    def setNrFeeds(self, nr_feeds) -> None: ...
    def setNrGainsFilteringIterations(self, nr_iterations) -> None: ...
    def setSimilarityThreshold(self, similarity_threshold) -> None: ...


class detail_BlocksGainCompensator(detail_BlocksCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, index, corner, image, mask) -> _image: ...
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def setMatGains(self, umv) -> None: ...


class detail_BundleAdjusterAffine(detail_BundleAdjusterBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_BundleAdjusterAffinePartial(detail_BundleAdjusterBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_BundleAdjusterBase(detail_Estimator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def confThresh(self, *args, **kwargs): ...  # incomplete
    def refinementMask(self, *args, **kwargs): ...  # incomplete
    def setConfThresh(self, conf_thresh) -> None: ...
    def setRefinementMask(self, mask) -> None: ...
    def setTermCriteria(self, term_criteria) -> None: ...
    def termCriteria(self, *args, **kwargs): ...  # incomplete


class detail_BundleAdjusterRay(detail_BundleAdjusterBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_BundleAdjusterReproj(detail_BundleAdjusterBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_CameraParams:
    R: Incomplete
    aspect: Incomplete
    focal: Incomplete
    ppx: Incomplete
    ppy: Incomplete
    t: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def K(self, *args, **kwargs): ...  # incomplete


class detail_ChannelsCompensator(detail_ExposureCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, index, corner, image, mask) -> _image: ...
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def getNrFeeds(self, *args, **kwargs): ...  # incomplete
    def getSimilarityThreshold(self, *args, **kwargs): ...  # incomplete
    def setMatGains(self, umv) -> None: ...
    def setNrFeeds(self, nr_feeds) -> None: ...
    def setSimilarityThreshold(self, similarity_threshold) -> None: ...


class detail_DpSeamFinder(detail_SeamFinder):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def setCostFunction(self, val) -> None: ...


class detail_Estimator:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, *args, **kwargs): ...  # incomplete


class detail_ExposureCompensator:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, index, corner, image, mask) -> _image: ...
    def createDefault(self, *args, **kwargs): ...  # incomplete
    def feed(self, corners, images, masks) -> None: ...
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def getUpdateGain(self, *args, **kwargs): ...  # incomplete
    def setMatGains(self, arg1) -> None: ...
    def setUpdateGain(self, b) -> None: ...


class detail_FeatherBlender(detail_Blender):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def blend(self, *args, **kwargs): ...  # incomplete
    def createWeightMaps(self, *args, **kwargs): ...  # incomplete
    def feed(self, img, mask, tl) -> None: ...
    def prepare(self, dst_roi) -> None: ...  # type: ignore[override]
    def setSharpness(self, val) -> None: ...
    def sharpness(self, *args, **kwargs): ...  # incomplete


class detail_FeaturesMatcher:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, features1, features2) -> _matches_info: ...
    def apply2(self, *args, **kwargs): ...  # incomplete
    def collectGarbage(self) -> None: ...
    def isThreadSafe(self, *args, **kwargs): ...  # incomplete


class detail_GainCompensator(detail_ExposureCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, index, corner, image, mask) -> _image: ...
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def getNrFeeds(self, *args, **kwargs): ...  # incomplete
    def getSimilarityThreshold(self, *args, **kwargs): ...  # incomplete
    def setMatGains(self, umv) -> None: ...
    def setNrFeeds(self, nr_feeds) -> None: ...
    def setSimilarityThreshold(self, similarity_threshold) -> None: ...


class detail_GraphCutSeamFinder:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def find(self, src, corners, masks) -> None: ...


class detail_HomographyBasedEstimator(detail_Estimator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_ImageFeatures:
    descriptors: Incomplete
    img_idx: Incomplete
    img_size: Incomplete
    keypoints: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getKeypoints(self, *args, **kwargs): ...  # incomplete


class detail_MatchesInfo:
    H: Incomplete
    confidence: Incomplete
    dst_img_idx: Incomplete
    num_inliers: Incomplete
    src_img_idx: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getInliers(self, *args, **kwargs): ...  # incomplete
    def getMatches(self, *args, **kwargs): ...  # incomplete


class detail_MultiBandBlender(detail_Blender):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def blend(self, *args, **kwargs): ...  # incomplete
    def feed(self, img, mask, tl) -> None: ...
    def numBands(self, *args, **kwargs): ...  # incomplete
    def prepare(self, dst_roi) -> None: ...  # type: ignore[override]
    def setNumBands(self, val) -> None: ...


class detail_NoBundleAdjuster(detail_BundleAdjusterBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_NoExposureCompensator(detail_ExposureCompensator):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def apply(self, arg1, arg2, arg3, arg4) -> _arg3: ...
    def getMatGains(self, *args, **kwargs): ...  # incomplete
    def setMatGains(self, umv) -> None: ...


class detail_NoSeamFinder(detail_SeamFinder):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def find(self, arg1, arg2, arg3) -> _arg3: ...


class detail_PairwiseSeamFinder(detail_SeamFinder):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def find(self, src, corners, masks) -> _masks: ...


class detail_ProjectorBase:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_SeamFinder:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def createDefault(self, *args, **kwargs): ...  # incomplete
    def find(self, src, corners, masks) -> _masks: ...


class detail_SphericalProjector(detail_ProjectorBase):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def mapBackward(self, u, v, x, y) -> None: ...
    def mapForward(self, x, y, u, v) -> None: ...


class detail_Timelapser:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def createDefault(self, *args, **kwargs): ...  # incomplete
    def getDst(self, *args, **kwargs): ...  # incomplete
    def initialize(self, corners, sizes) -> None: ...
    def process(self, img, mask, tl) -> None: ...


class detail_TimelapserCrop(detail_Timelapser):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class detail_VoronoiSeamFinder(detail_PairwiseSeamFinder):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def find(self, src, corners, masks) -> _masks: ...


class dnn_ClassificationModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def classify(self, *args, **kwargs): ...  # incomplete


class dnn_DetectionModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def detect(self, *args, **kwargs): ...  # incomplete
    def getNmsAcrossClasses(self, *args, **kwargs): ...  # incomplete
    def setNmsAcrossClasses(self, *args, **kwargs): ...  # incomplete


class dnn_DictValue:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getIntValue(self, *args, **kwargs): ...  # incomplete
    def getRealValue(self, *args, **kwargs): ...  # incomplete
    def getStringValue(self, *args, **kwargs): ...  # incomplete
    def isInt(self, *args, **kwargs): ...  # incomplete
    def isReal(self, *args, **kwargs): ...  # incomplete
    def isString(self, *args, **kwargs): ...  # incomplete


class dnn_KeypointsModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def estimate(self, *args, **kwargs): ...  # incomplete


class dnn_Layer(Algorithm):
    blobs: Incomplete
    name: Incomplete
    preferableTarget: Incomplete
    type: Incomplete
    def finalize(self, *args, **kwargs): ...  # incomplete
    def outputNameToIndex(self, *args, **kwargs): ...  # incomplete
    def run(self, *args, **kwargs): ...  # incomplete


class dnn_Model:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def predict(self, *args, **kwargs): ...  # incomplete
    def setInputCrop(self, *args, **kwargs): ...  # incomplete
    def setInputMean(self, *args, **kwargs): ...  # incomplete
    def setInputParams(self, *args, **kwargs): ...  # incomplete
    def setInputScale(self, *args, **kwargs): ...  # incomplete
    def setInputSize(self, *args, **kwargs): ...  # incomplete
    def setInputSwapRB(self, *args, **kwargs): ...  # incomplete
    def setPreferableBackend(self, *args, **kwargs): ...  # incomplete
    def setPreferableTarget(self, *args, **kwargs): ...  # incomplete


class dnn_Net:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def connect(self, outPin, inpPin) -> None: ...
    def dump(self, *args, **kwargs): ...  # incomplete
    def dumpToFile(self, path) -> None: ...
    def empty(self, *args, **kwargs): ...  # incomplete
    def enableFusion(self, fusion) -> None: ...
    def forward(self, *args, **kwargs): ...  # incomplete
    def forwardAndRetrieve(self, outBlobNames) -> _outputBlobs: ...
    def forwardAsync(self, *args, **kwargs): ...  # incomplete
    def getFLOPS(self, *args, **kwargs): ...  # incomplete
    def getInputDetails(self, *args, **kwargs): ...  # incomplete
    def getLayer(self, *args, **kwargs): ...  # incomplete
    def getLayerId(self, *args, **kwargs): ...  # incomplete
    def getLayerNames(self, *args, **kwargs): ...  # incomplete
    def getLayerTypes(self) -> _layersTypes: ...
    def getLayersCount(self, *args, **kwargs): ...  # incomplete
    def getLayersShapes(self, *args, **kwargs): ...  # incomplete
    def getMemoryConsumption(self, *args, **kwargs): ...  # incomplete
    def getOutputDetails(self, *args, **kwargs): ...  # incomplete
    def getParam(self, *args, **kwargs): ...  # incomplete
    def getPerfProfile(self, *args, **kwargs): ...  # incomplete
    def getUnconnectedOutLayers(self, *args, **kwargs): ...  # incomplete
    def getUnconnectedOutLayersNames(self, *args, **kwargs): ...  # incomplete
    def quantize(self, *args, **kwargs): ...  # incomplete
    def readFromModelOptimizer(self, *args, **kwargs): ...  # incomplete
    def setHalideScheduler(self, scheduler) -> None: ...
    def setInput(self, *args, **kwargs): ...  # incomplete
    def setInputShape(self, inputName, shape) -> None: ...
    def setInputsNames(self, inputBlobNames) -> None: ...
    def setParam(self, layer, numParam, blob) -> None: ...
    def setPreferableBackend(self, backendId) -> None: ...
    def setPreferableTarget(self, targetId) -> None: ...


class dnn_SegmentationModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def segment(self, *args, **kwargs): ...  # incomplete


class dnn_TextDetectionModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def detect(self, frame) -> _detections: ...
    def detectTextRectangles(self, frame) -> _detections: ...


class dnn_TextDetectionModel_DB(dnn_TextDetectionModel):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getBinaryThreshold(self, *args, **kwargs): ...  # incomplete
    def getMaxCandidates(self, *args, **kwargs): ...  # incomplete
    def getPolygonThreshold(self, *args, **kwargs): ...  # incomplete
    def getUnclipRatio(self, *args, **kwargs): ...  # incomplete
    def setBinaryThreshold(self, *args, **kwargs): ...  # incomplete
    def setMaxCandidates(self, *args, **kwargs): ...  # incomplete
    def setPolygonThreshold(self, *args, **kwargs): ...  # incomplete
    def setUnclipRatio(self, *args, **kwargs): ...  # incomplete


class dnn_TextDetectionModel_EAST(dnn_TextDetectionModel):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getConfidenceThreshold(self, *args, **kwargs): ...  # incomplete
    def getNMSThreshold(self, *args, **kwargs): ...  # incomplete
    def setConfidenceThreshold(self, *args, **kwargs): ...  # incomplete
    def setNMSThreshold(self, *args, **kwargs): ...  # incomplete


class dnn_TextRecognitionModel(dnn_Model):
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getDecodeType(self, *args, **kwargs): ...  # incomplete
    def getVocabulary(self, *args, **kwargs): ...  # incomplete
    def recognize(self, frame, roiRects) -> _results: ...
    def setDecodeOptsCTCPrefixBeamSearch(self, *args, **kwargs): ...  # incomplete
    def setDecodeType(self, *args, **kwargs): ...  # incomplete
    def setVocabulary(self, *args, **kwargs): ...  # incomplete


class error(Exception):
    code: ClassVar[int]
    err: ClassVar[str]
    file: ClassVar[str]
    func: ClassVar[str]
    line: ClassVar[int]
    msg: ClassVar[str]


class flann_Index:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def build(self, *args, **kwargs): ...  # incomplete
    def getAlgorithm(self, *args, **kwargs): ...  # incomplete
    def getDistance(self, *args, **kwargs): ...  # incomplete
    def knnSearch(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def radiusSearch(self, *args, **kwargs): ...  # incomplete
    def release(self) -> None: ...
    def save(self, filename) -> None: ...


class gapi_GKernelPackage:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_GNetPackage:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_GNetParam:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_ie_PyParams:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, tag: str, model: str, device: str) -> None: ...
    @overload
    def __init__(self, tag: str, model: str, weights: str, device: str) -> None: ...
    def cfgBatchSize(self, size): ...
    def cfgNumRequests(self, nireq): ...
    def constInput(self, layer_name, data, hint=...): ...


class gapi_streaming_queue_capacity:
    capacity: int
    def __init__(self, cap: int = ...) -> None: ...


class gapi_wip_GOutputs:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def getGArray(self, *args, **kwargs): ...  # incomplete
    def getGMat(self, *args, **kwargs): ...  # incomplete
    def getGOpaque(self, *args, **kwargs): ...  # incomplete
    def getGScalar(self, *args, **kwargs): ...  # incomplete


class gapi_wip_IStreamSource:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Circle:
    center: Incomplete
    color: Incomplete
    lt: Incomplete
    radius: Incomplete
    shift: Incomplete
    thick: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Image:
    alpha: Incomplete
    img: Incomplete
    org: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Line:
    color: Incomplete
    lt: Incomplete
    pt1: Incomplete
    pt2: Incomplete
    shift: Incomplete
    thick: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Mosaic:
    cellSz: Incomplete
    decim: Incomplete
    mos: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Poly:
    color: Incomplete
    lt: Incomplete
    points: Incomplete
    shift: Incomplete
    thick: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Rect:
    color: Incomplete
    lt: Incomplete
    rect: Incomplete
    shift: Incomplete
    thick: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class gapi_wip_draw_Text:
    bottom_left_origin: bool
    color: tuple[float, float, float, float]
    ff: int
    fs: float
    lt: int
    org: _Point
    text: str
    thick: int
    def __init__(self, text_: str, org_: _Point, ff_: int, fs_: float, color_: _Scalar) -> None: ...


class ml_ANN_MLP(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getAnnealCoolingRatio(self, *args, **kwargs): ...  # incomplete
    def getAnnealFinalT(self, *args, **kwargs): ...  # incomplete
    def getAnnealInitialT(self, *args, **kwargs): ...  # incomplete
    def getAnnealItePerStep(self, *args, **kwargs): ...  # incomplete
    def getBackpropMomentumScale(self, *args, **kwargs): ...  # incomplete
    def getBackpropWeightScale(self, *args, **kwargs): ...  # incomplete
    def getLayerSizes(self, *args, **kwargs): ...  # incomplete
    def getRpropDW0(self, *args, **kwargs): ...  # incomplete
    def getRpropDWMax(self, *args, **kwargs): ...  # incomplete
    def getRpropDWMin(self, *args, **kwargs): ...  # incomplete
    def getRpropDWMinus(self, *args, **kwargs): ...  # incomplete
    def getRpropDWPlus(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getTrainMethod(self, *args, **kwargs): ...  # incomplete
    def getWeights(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setActivationFunction(self, *args, **kwargs): ...  # incomplete
    def setAnnealCoolingRatio(self, val) -> None: ...
    def setAnnealFinalT(self, val) -> None: ...
    def setAnnealInitialT(self, val) -> None: ...
    def setAnnealItePerStep(self, val) -> None: ...
    def setBackpropMomentumScale(self, val) -> None: ...
    def setBackpropWeightScale(self, val) -> None: ...
    def setLayerSizes(self, _layer_sizes) -> None: ...
    def setRpropDW0(self, val) -> None: ...
    def setRpropDWMax(self, val) -> None: ...
    def setRpropDWMin(self, val) -> None: ...
    def setRpropDWMinus(self, val) -> None: ...
    def setRpropDWPlus(self, val) -> None: ...
    def setTermCriteria(self, val) -> None: ...
    def setTrainMethod(self, *args, **kwargs): ...  # incomplete


class ml_Boost(ml_DTrees):
    def create(self, *args, **kwargs): ...  # incomplete
    def getBoostType(self, *args, **kwargs): ...  # incomplete
    def getWeakCount(self, *args, **kwargs): ...  # incomplete
    def getWeightTrimRate(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setBoostType(self, val) -> None: ...
    def setWeakCount(self, val) -> None: ...
    def setWeightTrimRate(self, val) -> None: ...


class ml_DTrees(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getCVFolds(self, *args, **kwargs): ...  # incomplete
    def getMaxCategories(self, *args, **kwargs): ...  # incomplete
    def getMaxDepth(self, *args, **kwargs): ...  # incomplete
    def getMinSampleCount(self, *args, **kwargs): ...  # incomplete
    def getPriors(self, *args, **kwargs): ...  # incomplete
    def getRegressionAccuracy(self, *args, **kwargs): ...  # incomplete
    def getTruncatePrunedTree(self, *args, **kwargs): ...  # incomplete
    def getUse1SERule(self, *args, **kwargs): ...  # incomplete
    def getUseSurrogates(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setCVFolds(self, val) -> None: ...
    def setMaxCategories(self, val) -> None: ...
    def setMaxDepth(self, val) -> None: ...
    def setMinSampleCount(self, val) -> None: ...
    def setPriors(self, val) -> None: ...
    def setRegressionAccuracy(self, val) -> None: ...
    def setTruncatePrunedTree(self, val) -> None: ...
    def setUse1SERule(self, val) -> None: ...
    def setUseSurrogates(self, val) -> None: ...


class ml_EM(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getClustersNumber(self, *args, **kwargs): ...  # incomplete
    def getCovarianceMatrixType(self, *args, **kwargs): ...  # incomplete
    def getCovs(self, *args, **kwargs): ...  # incomplete
    def getMeans(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getWeights(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def predict(self, *args, **kwargs): ...  # incomplete
    def predict2(self, *args, **kwargs): ...  # incomplete
    def setClustersNumber(self, val) -> None: ...
    def setCovarianceMatrixType(self, val) -> None: ...
    def setTermCriteria(self, val) -> None: ...
    def trainE(self, *args, **kwargs): ...  # incomplete
    def trainEM(self, *args, **kwargs): ...  # incomplete
    def trainM(self, *args, **kwargs): ...  # incomplete


class ml_KNearest(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def findNearest(self, *args, **kwargs): ...  # incomplete
    def getAlgorithmType(self, *args, **kwargs): ...  # incomplete
    def getDefaultK(self, *args, **kwargs): ...  # incomplete
    def getEmax(self, *args, **kwargs): ...  # incomplete
    def getIsClassifier(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setAlgorithmType(self, val) -> None: ...
    def setDefaultK(self, val) -> None: ...
    def setEmax(self, val) -> None: ...
    def setIsClassifier(self, val) -> None: ...


class ml_LogisticRegression(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getIterations(self, *args, **kwargs): ...  # incomplete
    def getLearningRate(self, *args, **kwargs): ...  # incomplete
    def getMiniBatchSize(self, *args, **kwargs): ...  # incomplete
    def getRegularization(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getTrainMethod(self, *args, **kwargs): ...  # incomplete
    def get_learnt_thetas(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def predict(self, *args, **kwargs): ...  # incomplete
    def setIterations(self, val) -> None: ...
    def setLearningRate(self, val) -> None: ...
    def setMiniBatchSize(self, val) -> None: ...
    def setRegularization(self, val) -> None: ...
    def setTermCriteria(self, val) -> None: ...
    def setTrainMethod(self, val) -> None: ...


class ml_NormalBayesClassifier(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def predictProb(self, *args, **kwargs): ...  # incomplete


class ml_ParamGrid:
    logStep: Incomplete
    maxVal: Incomplete
    minVal: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete


class ml_RTrees(ml_DTrees):
    def create(self, *args, **kwargs): ...  # incomplete
    def getActiveVarCount(self, *args, **kwargs): ...  # incomplete
    def getCalculateVarImportance(self, *args, **kwargs): ...  # incomplete
    def getOOBError(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getVarImportance(self, *args, **kwargs): ...  # incomplete
    def getVotes(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setActiveVarCount(self, val) -> None: ...
    def setCalculateVarImportance(self, val) -> None: ...
    def setTermCriteria(self, val) -> None: ...


class ml_SVM(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getC(self, *args, **kwargs): ...  # incomplete
    def getClassWeights(self, *args, **kwargs): ...  # incomplete
    def getCoef0(self, *args, **kwargs): ...  # incomplete
    def getDecisionFunction(self, *args, **kwargs): ...  # incomplete
    def getDefaultGridPtr(self, *args, **kwargs): ...  # incomplete
    def getDegree(self, *args, **kwargs): ...  # incomplete
    def getGamma(self, *args, **kwargs): ...  # incomplete
    def getKernelType(self, *args, **kwargs): ...  # incomplete
    def getNu(self, *args, **kwargs): ...  # incomplete
    def getP(self, *args, **kwargs): ...  # incomplete
    def getSupportVectors(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getType(self, *args, **kwargs): ...  # incomplete
    def getUncompressedSupportVectors(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setC(self, val) -> None: ...
    def setClassWeights(self, val) -> None: ...
    def setCoef0(self, val) -> None: ...
    def setDegree(self, val) -> None: ...
    def setGamma(self, val) -> None: ...
    def setKernel(self, kernelType) -> None: ...
    def setNu(self, val) -> None: ...
    def setP(self, val) -> None: ...
    def setTermCriteria(self, val) -> None: ...
    def setType(self, val) -> None: ...
    def trainAuto(self, *args, **kwargs): ...  # incomplete


class ml_SVMSGD(ml_StatModel):
    def create(self, *args, **kwargs): ...  # incomplete
    def getInitialStepSize(self, *args, **kwargs): ...  # incomplete
    def getMarginRegularization(self, *args, **kwargs): ...  # incomplete
    def getMarginType(self, *args, **kwargs): ...  # incomplete
    def getShift(self, *args, **kwargs): ...  # incomplete
    def getStepDecreasingPower(self, *args, **kwargs): ...  # incomplete
    def getSvmsgdType(self, *args, **kwargs): ...  # incomplete
    def getTermCriteria(self, *args, **kwargs): ...  # incomplete
    def getWeights(self, *args, **kwargs): ...  # incomplete
    def load(self, *args, **kwargs): ...  # incomplete
    def setInitialStepSize(self, InitialStepSize) -> None: ...
    def setMarginRegularization(self, marginRegularization) -> None: ...
    def setMarginType(self, marginType) -> None: ...
    def setOptimalParameters(self, *args, **kwargs): ...  # incomplete
    def setStepDecreasingPower(self, stepDecreasingPower) -> None: ...
    def setSvmsgdType(self, svmsgdType) -> None: ...
    def setTermCriteria(self, val) -> None: ...


class ml_StatModel(Algorithm):
    def calcError(self, *args, **kwargs): ...  # incomplete
    def empty(self, *args, **kwargs): ...  # incomplete
    def getVarCount(self, *args, **kwargs): ...  # incomplete
    def isClassifier(self, *args, **kwargs): ...  # incomplete
    def isTrained(self, *args, **kwargs): ...  # incomplete
    def predict(self, *args, **kwargs): ...  # incomplete
    def train(self, *args, **kwargs): ...  # incomplete


class ml_TrainData:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def create(self, *args, **kwargs): ...  # incomplete
    def getCatCount(self, *args, **kwargs): ...  # incomplete
    def getCatMap(self, *args, **kwargs): ...  # incomplete
    def getCatOfs(self, *args, **kwargs): ...  # incomplete
    def getClassLabels(self, *args, **kwargs): ...  # incomplete
    def getDefaultSubstValues(self, *args, **kwargs): ...  # incomplete
    def getLayout(self, *args, **kwargs): ...  # incomplete
    def getMissing(self, *args, **kwargs): ...  # incomplete
    def getNAllVars(self, *args, **kwargs): ...  # incomplete
    def getNSamples(self, *args, **kwargs): ...  # incomplete
    def getNTestSamples(self, *args, **kwargs): ...  # incomplete
    def getNTrainSamples(self, *args, **kwargs): ...  # incomplete
    def getNVars(self, *args, **kwargs): ...  # incomplete
    def getNames(self, names) -> None: ...
    def getNormCatResponses(self, *args, **kwargs): ...  # incomplete
    def getResponseType(self, *args, **kwargs): ...  # incomplete
    def getResponses(self, *args, **kwargs): ...  # incomplete
    def getSample(self, varIdx, sidx, buf) -> None: ...
    def getSampleWeights(self, *args, **kwargs): ...  # incomplete
    def getSamples(self, *args, **kwargs): ...  # incomplete
    def getSubMatrix(self, *args, **kwargs): ...  # incomplete
    def getSubVector(self, *args, **kwargs): ...  # incomplete
    def getTestNormCatResponses(self, *args, **kwargs): ...  # incomplete
    def getTestResponses(self, *args, **kwargs): ...  # incomplete
    def getTestSampleIdx(self, *args, **kwargs): ...  # incomplete
    def getTestSampleWeights(self, *args, **kwargs): ...  # incomplete
    def getTestSamples(self, *args, **kwargs): ...  # incomplete
    def getTrainNormCatResponses(self, *args, **kwargs): ...  # incomplete
    def getTrainResponses(self, *args, **kwargs): ...  # incomplete
    def getTrainSampleIdx(self, *args, **kwargs): ...  # incomplete
    def getTrainSampleWeights(self, *args, **kwargs): ...  # incomplete
    def getTrainSamples(self, *args, **kwargs): ...  # incomplete
    def getValues(self, vi, sidx, values) -> None: ...
    def getVarIdx(self, *args, **kwargs): ...  # incomplete
    def getVarSymbolFlags(self, *args, **kwargs): ...  # incomplete
    def getVarType(self, *args, **kwargs): ...  # incomplete
    def setTrainTestSplit(self, *args, **kwargs): ...  # incomplete
    def setTrainTestSplitRatio(self, *args, **kwargs): ...  # incomplete
    def shuffleTrainTest(self) -> None: ...


class ocl_Device:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def OpenCLVersion(self, *args, **kwargs): ...  # incomplete
    def OpenCL_C_Version(self, *args, **kwargs): ...  # incomplete
    def addressBits(self, *args, **kwargs): ...  # incomplete
    def available(self, *args, **kwargs): ...  # incomplete
    def compilerAvailable(self, *args, **kwargs): ...  # incomplete
    def deviceVersionMajor(self, *args, **kwargs): ...  # incomplete
    def deviceVersionMinor(self, *args, **kwargs): ...  # incomplete
    def doubleFPConfig(self, *args, **kwargs): ...  # incomplete
    def driverVersion(self, *args, **kwargs): ...  # incomplete
    def endianLittle(self, *args, **kwargs): ...  # incomplete
    def errorCorrectionSupport(self, *args, **kwargs): ...  # incomplete
    def executionCapabilities(self, *args, **kwargs): ...  # incomplete
    def extensions(self, *args, **kwargs): ...  # incomplete
    def getDefault(self, *args, **kwargs): ...  # incomplete
    def globalMemCacheLineSize(self, *args, **kwargs): ...  # incomplete
    def globalMemCacheSize(self, *args, **kwargs): ...  # incomplete
    def globalMemCacheType(self, *args, **kwargs): ...  # incomplete
    def globalMemSize(self, *args, **kwargs): ...  # incomplete
    def halfFPConfig(self, *args, **kwargs): ...  # incomplete
    def hostUnifiedMemory(self, *args, **kwargs): ...  # incomplete
    def image2DMaxHeight(self, *args, **kwargs): ...  # incomplete
    def image2DMaxWidth(self, *args, **kwargs): ...  # incomplete
    def image3DMaxDepth(self, *args, **kwargs): ...  # incomplete
    def image3DMaxHeight(self, *args, **kwargs): ...  # incomplete
    def image3DMaxWidth(self, *args, **kwargs): ...  # incomplete
    def imageFromBufferSupport(self, *args, **kwargs): ...  # incomplete
    def imageMaxArraySize(self, *args, **kwargs): ...  # incomplete
    def imageMaxBufferSize(self, *args, **kwargs): ...  # incomplete
    def imageSupport(self, *args, **kwargs): ...  # incomplete
    def intelSubgroupsSupport(self, *args, **kwargs): ...  # incomplete
    def isAMD(self, *args, **kwargs): ...  # incomplete
    def isExtensionSupported(self, *args, **kwargs): ...  # incomplete
    def isIntel(self, *args, **kwargs): ...  # incomplete
    def isNVidia(self, *args, **kwargs): ...  # incomplete
    def linkerAvailable(self, *args, **kwargs): ...  # incomplete
    def localMemSize(self, *args, **kwargs): ...  # incomplete
    def localMemType(self, *args, **kwargs): ...  # incomplete
    def maxClockFrequency(self, *args, **kwargs): ...  # incomplete
    def maxComputeUnits(self, *args, **kwargs): ...  # incomplete
    def maxConstantArgs(self, *args, **kwargs): ...  # incomplete
    def maxConstantBufferSize(self, *args, **kwargs): ...  # incomplete
    def maxMemAllocSize(self, *args, **kwargs): ...  # incomplete
    def maxParameterSize(self, *args, **kwargs): ...  # incomplete
    def maxReadImageArgs(self, *args, **kwargs): ...  # incomplete
    def maxSamplers(self, *args, **kwargs): ...  # incomplete
    def maxWorkGroupSize(self, *args, **kwargs): ...  # incomplete
    def maxWorkItemDims(self, *args, **kwargs): ...  # incomplete
    def maxWriteImageArgs(self, *args, **kwargs): ...  # incomplete
    def memBaseAddrAlign(self, *args, **kwargs): ...  # incomplete
    def name(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthChar(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthDouble(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthFloat(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthHalf(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthInt(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthLong(self, *args, **kwargs): ...  # incomplete
    def nativeVectorWidthShort(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthChar(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthDouble(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthFloat(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthHalf(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthInt(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthLong(self, *args, **kwargs): ...  # incomplete
    def preferredVectorWidthShort(self, *args, **kwargs): ...  # incomplete
    def printfBufferSize(self, *args, **kwargs): ...  # incomplete
    def profilingTimerResolution(self, *args, **kwargs): ...  # incomplete
    def singleFPConfig(self, *args, **kwargs): ...  # incomplete
    def type(self, *args, **kwargs): ...  # incomplete
    def vendorID(self, *args, **kwargs): ...  # incomplete
    def vendorName(self, *args, **kwargs): ...  # incomplete
    def version(self, *args, **kwargs): ...  # incomplete


class ocl_OpenCLExecutionContext:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete


class segmentation_IntelligentScissorsMB:
    def __init__(self, *args, **kwargs) -> None: ...  # incomplete
    def applyImage(self, *args, **kwargs): ...  # incomplete
    def applyImageFeatures(self, *args, **kwargs): ...  # incomplete
    def buildMap(self, sourcePt) -> None: ...
    def getContour(self, *args, **kwargs): ...  # incomplete
    def setEdgeFeatureCannyParameters(self, *args, **kwargs): ...  # incomplete
    def setEdgeFeatureZeroCrossingParameters(self, *args, **kwargs): ...  # incomplete
    def setGradientMagnitudeMaxLimit(self, *args, **kwargs): ...  # incomplete
    def setWeights(self, *args, **kwargs): ...  # incomplete


def AKAZE_create(
    descriptor_type=...,
    descriptor_size=...,
    descriptor_channels=...,
    threshold=...,
    nOctaves=...,
    nOctaveLayers=...,
    diffusivity=...,
): ...
def AffineFeature_create(*args, **kwargs): ...  # incomplete
def AgastFeatureDetector_create(threshold=..., nonmaxSuppression=..., type=...): ...
def BFMatcher_create(normType: int = ..., crossCheck=...): ...
@overload
def BRISK_create(thresh=..., octaves=..., patternScale=...): ...
@overload
def BRISK_create(radiusList, numberList, dMax=..., dMin=..., indexChange=...): ...
@overload
def BRISK_create(thresh, octaves, radiusList, numberList, dMax=..., dMin=..., indexChange=...): ...
def CamShift(probImage, window, criteria) -> tuple[_RotatedRectResult, _window]: ...
@overload
def Canny(image: Mat, threshold1, threshold2, edges=..., apertureSize=..., L2gradient=...) -> _edges: ...
@overload
def Canny(dx, dy, threshold1, threshold2, edges=..., L2gradient=...) -> _edges: ...
def CascadeClassifier_convert(oldcascade, newcascade): ...
def DISOpticalFlow_create(preset=...): ...
@overload
def DescriptorMatcher_create(descriptorMatcherType: str) -> DescriptorMatcher: ...
@overload
def DescriptorMatcher_create(matcherType: int) -> DescriptorMatcher: ...


def EMD(
    signature1,
    signature2,
    distType,
    cost=...,
    lowerBound=...,
    flow=...,
) -> tuple[
    tuple[
        Incomplete,
        _lowerBound,
        _flow,
    ]
]: ...


def FaceDetectorYN_create(*args, **kwargs): ...  # incomplete
def FaceRecognizerSF_create(*args, **kwargs): ...  # incomplete


def FarnebackOpticalFlow_create(
    numLevels=...,
    pyrScale=...,
    fastPyramids=...,
    winSize=...,
    numIters=...,
    polyN=...,
    polySigma=...,
    flags: int | None = ...,
): ...


def FastFeatureDetector_create(threshold=..., nonmaxSuppression=..., type=...): ...
def FlannBasedMatcher_create(): ...


@overload
def GFTTDetector_create(
    maxCorners=...,
    qualityLevel=...,
    minDistance=...,
    blockSize=...,
    useHarrisDetector=...,
    k=...,
): ...


@overload
def GFTTDetector_create(
    maxCorners,
    qualityLevel,
    minDistance,
    blockSize,
    gradiantSize,
    useHarrisDetector=...,
    k=...,
): ...


def GaussianBlur(src: Mat, ksize, sigmaX, dst: Mat = ..., sigmaY=..., borderType=...) -> _dst: ...
def HOGDescriptor_getDaimlerPeopleDetector(): ...
def HOGDescriptor_getDefaultPeopleDetector(): ...


def HoughCircles(
    image: Mat, method: int, dp, minDist, circles=..., param1=..., param2=..., minRadius=..., maxRadius=...,
) -> _circles: ...


def HoughLines(
    image: Mat, rho, theta, threshold, lines=..., srn=...,
    stn=..., min_theta=..., max_theta=...,
) -> _lines: ...


def HoughLinesP(image: Mat, rho, theta, threshold, lines=..., minLineLength=..., maxLineGap=...) -> _lines: ...


def HoughLinesPointSet(
    _point, lines_max, threshold, min_rho, max_rho, rho_step, min_theta, max_theta, theta_step, _lines=...,
) -> _lines: ...
def HoughLinesWithAccumulator(*args, **kwargs): ...  # incomplete
def HuMoments(m, hu=...) -> _hu: ...
def KAZE_create(extended=..., upright=..., threshold=..., nOctaves=..., nOctaveLayers=..., diffusivity=...): ...
@overload
def KeyPoint_convert(keypoints, keypointIndexes=...) -> _points2f: ...
@overload
def KeyPoint_convert(points2f, size=..., response=..., octave=..., class_id=...) -> _keypoints: ...
def KeyPoint_overlap(kp1, kp2): ...
def LUT(src: Mat, lut, dst: Mat = ...) -> _dst: ...
def Laplacian(src: Mat, ddepth, dst: Mat = ..., ksize=..., scale=..., delta=..., borderType=...) -> _dst: ...


def MSER_create(
    _delta=...,
    _min_area=...,
    _max_area=...,
    _max_variation=...,
    _min_diversity=...,
    _max_evolution=...,
    _area_threshold=...,
    _min_margin=...,
    _edge_blur_size=...,
): ...
def Mahalanobis(v1, v2, icovar): ...


def ORB_create(
    nfeatures=...,
    scaleFactor=...,
    nlevels=...,
    edgeThreshold=...,
    firstLevel=...,
    WTA_K=...,
    scoreType=...,
    patchSize=...,
    fastThreshold=...,
): ...
def PCABackProject(data, mean, eigenvectors, result=...): ...
@overload
def PCACompute(data, mean, eigenvectors=..., maxComponents=...) -> tuple[tuple[_mean, _eigenvectors]]: ...
@overload
def PCACompute(data, mean, retainedVariance, eigenvectors=...) -> tuple[tuple[_mean, _eigenvectors]]: ...


@overload
def PCACompute2(
    data, mean, eigenvectors=..., eigenvalues=..., maxComponents=...,
) -> tuple[tuple[_mean, _eigenvectors, _eigenvalues]]: ...


@overload
def PCACompute2(
    data, mean, retainedVariance, eigenvectors=..., eigenvalues=...,
) -> tuple[tuple[_mean, _eigenvectors, _eigenvalues]]: ...
def PCAProject(data, mean, eigenvectors, result=...) -> _result: ...
def PSNR(src1: Mat, src2: Mat, R=...): ...
def QRCodeEncoder_create(*args, **kwargs): ...  # incomplete


def RQDecomp3x3(
    src: Mat, mtxR=..., mtxQ=..., Qx=..., Qy=..., Qz=...,
) -> tuple[tuple[Incomplete, _mtxR, _mtxQ, _Qx, _Qy, _Qz]]: ...
def Rodrigues(src: Mat, dst: Mat = ..., jacobian=...) -> tuple[tuple[_dst, _jacobian]]: ...
def SIFT_create(nfeatures=..., nOctaveLayers=..., contrastThreshold=..., edgeThreshold=..., sigma=...): ...
def SVBackSubst(w, u, vt, rhs, dst: Mat = ...) -> _dst: ...
def SVDecomp(src: Mat, w=..., u=..., vt=..., flags: int | None = ...) -> tuple[tuple[_w, _u, _vt]]: ...
def Scharr(src: Mat, ddepth, dx, dy, dst: Mat = ..., scale=..., delta=..., borderType=...) -> _dst: ...
def SimpleBlobDetector_create(parameters=...): ...
def Sobel(src: Mat, ddepth, dx, dy, dst: Mat = ..., ksize=..., scale=..., delta=..., borderType=...) -> _dst: ...


def SparsePyrLKOpticalFlow_create(
    winSize=...,
    maxLevel=...,
    crit=...,
    flags: int | None = ...,
    minEigThreshold=...,
): ...


def StereoBM_create(numDisparities=..., blockSize=...): ...


def StereoSGBM_create(
    minDisparity=...,
    numDisparities=...,
    blockSize=...,
    P1=...,
    P2=...,
    disp12MaxDiff=...,
    preFilterCap=...,
    uniquenessRatio=...,
    speckleWindowSize=...,
    speckleRange=...,
    mode=...,
): ...
def Stitcher_create(mode=...): ...
def TrackerDaSiamRPN_create(*args, **kwargs): ...  # incomplete
def TrackerGOTURN_create(*args, **kwargs): ...  # incomplete
def TrackerMIL_create(*args, **kwargs): ...  # incomplete
def UMat_context(): ...
def UMat_queue(): ...
def VariationalRefinement_create(): ...
def VideoWriter_fourcc(c1, c2, c3, c4): ...
def _registerMatType(*args, **kwargs): ...  # incomplete
def absdiff(src1: Mat, src2: Mat, dst: Mat = ...) -> _dst: ...
def accumulate(src: Mat, dst: Mat, mask: Mat = ...) -> _dst: ...
def accumulateProduct(src1: Mat, src2: Mat, dst: Mat, mask: Mat = ...) -> _dst: ...
def accumulateSquare(src: Mat, dst: Mat, mask: Mat = ...) -> _dst: ...
def accumulateWeighted(src: Mat, dst: Mat, alpha, mask: Mat = ...) -> _dst: ...
def adaptiveThreshold(src: Mat, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst: Mat = ...) -> _dst: ...
def add(src1: Mat | _NumericScalar, src2: Mat | _NumericScalar, dst: Mat = ..., mask: Mat = ..., dtype=...) -> _dst: ...
def addText(img: Mat, text, org, nameFont, pointSize=..., color=..., weight=..., style=..., spacing=...) -> None: ...
def addWeighted(src1: Mat, alpha, src2: Mat, beta, gamma, dst: Mat = ..., dtype=...) -> _dst: ...
@overload
def applyColorMap(src: Mat, colormap, dst: Mat = ...) -> _dst: ...
@overload
def applyColorMap(src, userColor, dst=...) -> _dst: ...
def approxPolyDP(curve, epsilon, closed, approxCurve=...) -> _approxCurve: ...
def arcLength(curve, closed): ...
def arrowedLine(img: Mat, pt1, pt2, color, thickness=..., line_type=..., shift=..., tipLength=...) -> _img: ...


def batchDistance(
    src1: Mat,
    src2: Mat,
    dtype,
    dist=...,
    nidx=...,
    normType: int = ...,
    K=...,
    mask: Mat = ...,
    update=...,
    crosscheck=...,
) -> tuple[
    _dist,
    _nidx,
]: ...


def bilateralFilter(src: Mat, d, sigmaColor, sigmaSpace, dst: Mat = ..., borderType=...) -> _dst: ...
def bitwise_and(src1: Mat, src2: Mat, dst: Mat = ..., mask: Mat = ...) -> _dst: ...
def bitwise_not(src: Mat, dst: Mat = ..., mask: Mat = ...) -> _dst: ...
def bitwise_or(src1: Mat, src2: Mat, dst: Mat = ..., mask: Mat = ...) -> _dst: ...
def bitwise_xor(src1: Mat, src2: Mat, dst: Mat = ..., mask: Mat = ...) -> _dst: ...
def blendLinear(*args, **kwargs): ...  # incomplete
def blur(src: Mat, ksize, dst: Mat = ..., anchor=..., borderType=...) -> _dst: ...
def borderInterpolate(p, len, borderType): ...
def boundingRect(array): ...
def boxFilter(src: Mat, ddepth, ksize, dst: Mat = ..., anchor=..., normalize=..., borderType=...) -> _dst: ...
def boxPoints(box, points=...) -> _points: ...


def buildOpticalFlowPyramid(
    img: Mat,
    winSize,
    maxLevel,
    pyramid=...,
    withDerivatives=...,
    pyrBorder=...,
    derivBorder=...,
    tryReuseInputImage=...,
) -> tuple[
    Incomplete,
    _pyramid,
]: ...


def calcBackProject(
    images: Sequence[Mat], channels: Sequence[int], hist, ranges: Sequence[int], scale, dst: Mat = ...,
) -> _dst: ...
def calcCovarMatrix(samples, mean, flags: int | None, covar=..., ctype=...) -> tuple[_covar, _mean]: ...


def calcHist(
    images: Sequence[Mat],
    channels: Sequence[int],
    mask: Mat | None,
    histSize: Sequence[int],
    ranges: Sequence[int],
    hist: Mat = ...,
    accumulate=...,
) -> Mat: ...


def calcOpticalFlowFarneback(
    prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags: int | None,
) -> _flow: ...


def calcOpticalFlowPyrLK(
    prevImg,
    nextImg,
    prevPts,
    nextPts,
    status=...,
    err=...,
    winSize=...,
    maxLevel=...,
    criteria=...,
    flags: int | None = ...,
    minEigThreshold=...,
) -> tuple[_nextPts, _status, _err]: ...


def calibrateCamera(
    objectPoints,
    imagePoints,
    imageSize,
    cameraMatrix,
    distCoeffs,
    rvecs=...,
    tvecs=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[
    Incomplete,
    _cameraMatrix,
    _distCoeffs,
    _rvecs,
    _tvecs,
]: ...


def calibrateCameraExtended(
    objectPoints,
    imagePoints,
    imageSize,
    cameraMatrix,
    distCoeffs,
    rvecs=...,
    tvecs=...,
    stdDeviationsIntrinsics=...,
    stdDeviationsExtrinsics=...,
    perViewErrors=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[
    Incomplete,
    _cameraMatrix,
    _distCoeffs,
    _rvecs,
    _tvecs,
    _stdDeviationsIntrinsics,
    _stdDeviationsExtrinsics,
    _perViewErrors,
]: ...


def calibrateCameraRO(
    objectPoints,
    imagePoints,
    imageSize,
    iFixedPoint,
    cameraMatrix,
    distCoeffs,
    rvecs=...,
    tvecs=...,
    newObjPoints=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[Incomplete, _cameraMatrix, _distCoeffs, _rvecs, _tvecs, _newObjPoints]: ...


def calibrateCameraROExtended(
    objectPoints,
    imagePoints,
    imageSize,
    iFixedPoint,
    cameraMatrix,
    distCoeffs,
    rvecs=...,
    tvecs=...,
    newObjPoints=...,
    stdDeviationsIntrinsics=...,
    stdDeviationsExtrinsics=...,
    stdDeviationsObjPoints=...,
    perViewErrors=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[
    Incomplete,
    _cameraMatrix,
    _distCoeffs,
    _rvecs,
    _tvecs,
    _newObjPoints,
    _stdDeviationsIntrinsics,
    _stdDeviationsExtrinsics,
    _stdDeviationsObjPoints,
    _perViewErrors,
]: ...


def calibrateHandEye(
    R_gripper2base, t_gripper2base, R_target2cam, t_target2cam, R_cam2gripper=..., t_cam2gripper=..., method: int = ...,
) -> tuple[_R_cam2gripper, _t_cam2gripper]: ...
def calibrateRobotWorldHandEye(*args, **kwargs): ...  # incomplete


def calibrationMatrixValues(
    cameraMatrix, imageSize, apertureWidth, apertureHeight,
) -> tuple[_fovx, _fovy, _focalLength, _principalPoint, _aspectRatio]: ...
def cartToPolar(x, y, magnitude=..., angle=..., angleInDegrees=...) -> tuple[_magnitude, _angle]: ...
def checkChessboard(img: Mat, size): ...
def checkHardwareSupport(feature): ...
def checkRange(a, quiet=..., minVal=..., maxVal=...) -> tuple[Incomplete, _pos]: ...
def circle(img: Mat, center, radius, color, thickness=..., lineType=..., shift=...) -> _img: ...
def clipLine(imgRect, pt1, pt2) -> tuple[Incomplete, _pt1, _pt2]: ...
def colorChange(src: Mat, mask: Mat, dst: Mat = ..., red_mul=..., green_mul=..., blue_mul=...) -> _dst: ...
def compare(src1: Mat, src2: Mat, cmpop, dst: Mat = ...) -> _dst: ...
def compareHist(H1: Mat, H2: Mat, method: int) -> float: ...
def completeSymm(m, lowerToUpper=...) -> _m: ...


def composeRT(
    rvec1,
    tvec1,
    rvec2,
    tvec2,
    rvec3=...,
    tvec3=...,
    dr3dr1=...,
    dr3dt1=...,
    dr3dr2=...,
    dr3dt2=...,
    dt3dr1=...,
    dt3dt1=...,
    dt3dr2=...,
    dt3dt2=...,
) -> tuple[_rvec3, _tvec3, _dr3dr1, _dr3dt1, _dr3dr2, _dr3dt2, _dt3dr1, _dt3dt1, _dt3dr2, _dt3dt2]: ...
def computeCorrespondEpilines(points, whichImage, F, lines=...) -> _lines: ...
def computeECC(templateImage, inputImage, inputMask=...): ...
def connectedComponents(image: Mat, labels=..., connectivity=..., ltype=...) -> tuple[Incomplete, _labels]: ...


def connectedComponentsWithAlgorithm(
    image: Mat,
    connectivity,
    ltype,
    ccltype,
    labels=...,
) -> tuple[
    Incomplete,
    _labels,
]: ...


def connectedComponentsWithStats(
    image: Mat, labels=..., stats=..., centroids=..., connectivity=..., ltype=...,
) -> tuple[Incomplete, _labels, _stats, _centroids]: ...


def connectedComponentsWithStatsWithAlgorithm(
    image: Mat, connectivity, ltype, ccltype, labels=..., stats=..., centroids=...,
) -> tuple[Incomplete, _labels, _stats, _centroids]: ...
@overload
def contourArea(approx): ...
@overload
def contourArea(contour, oriented=...): ...
def convertFp16(src: Mat, dst: Mat = ...) -> _dst: ...


def convertMaps(
    map1,
    map2,
    dstmap1type,
    dstmap1=...,
    dstmap2=...,
    nninterpolation=...,
) -> tuple[
    _dstmap1,
    _dstmap2,
]: ...


def convertPointsFromHomogeneous(src: Mat, dst: Mat = ...) -> _dst: ...
def convertPointsToHomogeneous(src: Mat, dst: Mat = ...) -> _dst: ...
def convertScaleAbs(src: Mat, dst: Mat = ..., alpha=..., beta=...) -> _dst: ...
def convexHull(points, hull=..., clockwise=..., returnPoints=...) -> _hull: ...
def convexityDefects(contour, convexhull, convexityDefects=...) -> _convexityDefects: ...
def copyMakeBorder(src: Mat, top, bottom, left, right, borderType, dst: Mat = ..., value=...) -> _dst: ...
def copyTo(src: Mat, mask: Mat, dst: Mat = ...) -> _dst: ...
def cornerEigenValsAndVecs(src: Mat, blockSize, ksize, dst: Mat = ..., borderType=...) -> _dst: ...
def cornerHarris(src: Mat, blockSize, ksize, k, dst: Mat = ..., borderType=...) -> _dst: ...
def cornerMinEigenVal(src: Mat, blockSize, dst: Mat = ..., ksize=..., borderType=...) -> _dst: ...
def cornerSubPix(image: Mat, corners, winSize, zeroZone, criteria) -> _corners: ...
def correctMatches(F, points1, points2, newPoints1=..., newPoints2=...) -> tuple[_newPoints1, _newPoints2]: ...
def countNonZero(src: Mat | _NumericScalar) -> int: ...
def createAlignMTB(max_bits=..., exclude_range=..., cut=...): ...
def createBackgroundSubtractorKNN(history=..., dist2Threshold=..., detectShadows=...): ...
def createBackgroundSubtractorMOG2(history=..., varThreshold=..., detectShadows=...): ...
def createButton(buttonName, onChange, userData=..., buttonType=..., initialButtonState=...) -> None: ...
def createCLAHE(clipLimit=..., tileGridSize=...): ...
def createCalibrateDebevec(samples=..., lambda_=..., random=...): ...
def createCalibrateRobertson(max_iter=..., threshold=...): ...
def createGeneralizedHoughBallard(): ...
def createGeneralizedHoughGuil(): ...
def createHanningWindow(winSize, type, dst: Mat = ...) -> _dst: ...


def createLineSegmentDetector(
    _refine=..., _scale=..., _sigma_scale=..., _quant=..., _ang_th=..., _log_eps=..., _density_th=..., _n_bins=...,
): ...
def createMergeDebevec(): ...
def createMergeMertens(contrast_weight=..., saturation_weight=..., exposure_weight=...): ...
def createMergeRobertson(): ...
def createTonemap(gamma=...): ...
def createTonemapDrago(gamma=..., saturation=..., bias=...): ...
def createTonemapMantiuk(gamma=..., scale=..., saturation=...): ...
def createTonemapReinhard(gamma=..., intensity=..., light_adapt=..., color_adapt=...): ...
def createTrackbar(trackbarName, windowName, value, count, onChange) -> None: ...
def cubeRoot(val): ...
def cvtColor(src: Mat, code: int, dst: Mat = ..., dstCn: int = ...) -> Mat: ...
def cvtColorTwoPlane(src1: Mat, src2: Mat, code: int, dst: Mat = ...) -> _dst: ...
def dct(src: Mat, dst: Mat = ..., flags: int | None = ...) -> _dst: ...
def decolor(src: Mat, grayscale=..., color_boost=...) -> tuple[_grayscale, _color_boost]: ...
def decomposeEssentialMat(E, R1=..., R2=..., t=...) -> tuple[_R1, _R2, _t]: ...


def decomposeHomographyMat(
    H, K, rotations=..., translations=..., normals=...,
) -> tuple[Incomplete, _rotations, _translations, _normals]: ...


def decomposeProjectionMatrix(
    projMatrix,
    cameraMatrix=...,
    rotMatrix=...,
    transVect=...,
    rotMatrixX=...,
    rotMatrixY=...,
    rotMatrixZ=...,
    eulerAngles=...,
) -> tuple[
    _cameraMatrix,
    _rotMatrix,
    _transVect,
    _rotMatrixX,
    _rotMatrixY,
    _rotMatrixZ,
    _eulerAngles,
]: ...


def demosaicing(src: Mat, code: int, dst: Mat = ..., dstCn: int = ...) -> _dst: ...
def denoise_TVL1(observations, result, lambda_=..., niters=...) -> None: ...
def destroyAllWindows() -> None: ...
def destroyWindow(winname) -> None: ...
def detailEnhance(src: Mat, dst: Mat = ..., sigma_s=..., sigma_r=...) -> _dst: ...
def determinant(mtx): ...
def dft(src: Mat, dst: Mat = ..., flags: int | None = ..., nonzeroRows=...) -> _dst: ...
def dilate(src: Mat, kernel, dst: Mat = ..., anchor=..., iterations=..., borderType=..., borderValue=...) -> _dst: ...
def displayOverlay(winname, text, delayms=...) -> None: ...
def displayStatusBar(winname, text, delayms=...) -> None: ...
def distanceTransform(src: Mat, distanceType, maskSize, dst: Mat = ..., dstType=...) -> _dst: ...


def distanceTransformWithLabels(
    src: Mat, distanceType, maskSize, dst: Mat = ..., labels=..., labelType=...,
) -> tuple[_dst, _labels]: ...
def divSpectrums(*args, **kwargs): ...  # incomplete
@overload
def divide(src1: Mat, src2: Mat, dst: Mat = ..., scale=..., dtype=...) -> _dst: ...
@overload
def divide(scale, src2, dst=..., dtype=...) -> _dst: ...
def dnn_registerLayer() -> None: ...
def dnn_unregisterLayer() -> None: ...
def drawChessboardCorners(image: Mat, patternSize, corners, patternWasFound) -> _image: ...


def drawContours(
    image: Mat, contours, contourIdx, color, thickness=..., lineType=..., hierarchy=..., maxLevel=..., offset=...,
) -> _image: ...
def drawFrameAxes(image: Mat, cameraMatrix, distCoeffs, rvec, tvec, length, thickness=...) -> _image: ...
def drawKeypoints(image: Mat, keypoints, outImage, color=..., flags: int | None = ...) -> _outImage: ...
def drawMarker(img: Mat, position, color, markerType=..., markerSize=..., thickness=..., line_type=...) -> _img: ...


def drawMatches(
    img1,
    keypoints1,
    img2,
    keypoints2,
    matches1to2,
    outImg,
    matchColor=...,
    singlePointColor=...,
    matchesMask=...,
    flags: int | None = ...,
) -> _outImg: ...


def drawMatchesKnn(
    img1,
    keypoints1,
    img2,
    keypoints2,
    matches1to2,
    outImg,
    matchColor=...,
    singlePointColor=...,
    matchesMask=...,
    flags: int | None = ...,
) -> _outImg: ...
def edgePreservingFilter(src: Mat, dst: Mat = ..., flags: int | None = ..., sigma_s=..., sigma_r=...) -> _dst: ...
def eigen(src: Mat, eigenvalues=..., eigenvectors=...) -> tuple[Incomplete, _eigenvalues, _eigenvectors]: ...
def eigenNonSymmetric(src: Mat, eigenvalues=..., eigenvectors=...) -> tuple[_eigenvalues, _eigenvectors]: ...


@overload
def ellipse(
    img: Mat,
    center,
    axes,
    angle,
    startAngle,
    endAngle,
    color,
    thickness=...,
    lineType=...,
    shift=...,
) -> _img: ...


@overload
def ellipse(img, box, color, thickness=..., lineType=...) -> _img: ...
def ellipse2Poly(center, axes, angle, arcStart, arcEnd, delta) -> _pts: ...
def empty_array_desc(*args, **kwargs): ...  # incomplete
def empty_gopaque_desc(*args, **kwargs): ...  # incomplete
def empty_scalar_desc(*args, **kwargs): ...  # incomplete
def equalizeHist(src: Mat, dst: Mat = ...) -> _dst: ...
def erode(src: Mat, kernel, dst: Mat = ..., anchor=..., iterations=..., borderType=..., borderValue=...) -> _dst: ...


def estimateAffine2D(
    from_, to, inliers=..., method: int = ..., ransacReprojThreshold=..., maxIters=..., confidence=..., refineIters=...,
) -> tuple[Incomplete, _inliers]: ...


def estimateAffine3D(
    src: Mat, dst: Mat, out=..., inliers=..., ransacThreshold=..., confidence=...,
) -> tuple[Incomplete, _out, _inliers]: ...


def estimateAffinePartial2D(
    from_, to, inliers=..., method: int = ..., ransacReprojThreshold=..., maxIters=..., confidence=..., refineIters=...,
) -> tuple[Incomplete, _inliers]: ...


def estimateChessboardSharpness(
    image: Mat, patternSize, corners, rise_distance=..., vertical=..., sharpness=...,
) -> tuple[Incomplete, _sharpness]: ...


def estimateTranslation3D(
    src: Mat, dst: Mat, out=..., inliers=..., ransacThreshold=..., confidence=...,
) -> tuple[Incomplete, _out, _inliers]: ...
def exp(src: Mat, dst: Mat = ...) -> _dst: ...
def extractChannel(src: Mat, coi, dst: Mat = ...) -> _dst: ...
def fastAtan2(y, x): ...
@overload
def fastNlMeansDenoising(src: Mat, dst: Mat = ..., h=..., templateWindowSize=..., searchWindowSize=...) -> _dst: ...
@overload
def fastNlMeansDenoising(src, h, dst=..., templateWindowSize=..., searchWindowSize=..., normType=...) -> _dst: ...


def fastNlMeansDenoisingColored(
    src: Mat, dst: Mat = ..., h=..., hColor=..., templateWindowSize=..., searchWindowSize=...,
) -> _dst: ...


def fastNlMeansDenoisingColoredMulti(
    srcImgs,
    imgToDenoiseIndex,
    temporalWindowSize,
    dst: Mat = ...,
    h=...,
    hColor=...,
    templateWindowSize=...,
    searchWindowSize=...,
) -> _dst: ...


@overload
def fastNlMeansDenoisingMulti(
    srcImgs, imgToDenoiseIndex, temporalWindowSize, dst: Mat = ..., h=..., templateWindowSize=..., searchWindowSize=...,
) -> _dst: ...


@overload
def fastNlMeansDenoisingMulti(
    srcImgs,
    imgToDenoiseIndex,
    temporalWindowSize,
    h,
    dst=...,
    templateWindowSize=...,
    searchWindowSize=...,
    normType=...,
) -> _dst: ...


def fillConvexPoly(img: Mat, points, color, lineType=..., shift=...) -> _img: ...
def fillPoly(img: Mat, pts, color, lineType=..., shift=..., offset=...) -> _img: ...
def filter2D(src: Mat, ddepth, kernel, dst: Mat = ..., anchor=..., delta=..., borderType=...) -> _dst: ...


def filterHomographyDecompByVisibleRefpoints(
    rotations, normals, beforePoints, afterPoints, possibleSolutions=..., pointsMask=...,
) -> _possibleSolutions: ...
def filterSpeckles(img: Mat, newVal, maxSpeckleSize, maxDiff, buf=...) -> tuple[_img, _buf]: ...
def find4QuadCornerSubpix(img: Mat, corners, region_size) -> tuple[Incomplete, _corners]: ...


def findChessboardCorners(
    image: Mat,
    patternSize,
    corners=...,
    flags: int | None = ...,
) -> tuple[
    Incomplete,
    _corners,
]: ...


def findChessboardCornersSB(
    image: Mat,
    patternSize,
    corners=...,
    flags: int | None = ...,
) -> tuple[
    Incomplete,
    _corners,
]: ...


def findChessboardCornersSBWithMeta(
    image: Mat, patternSize, flags: int | None, corners=..., meta=...,
) -> tuple[Incomplete, _corners, _meta]: ...


@overload
def findCirclesGrid(
    image: Mat, patternSize, flags: int | None, blobDetector, parameters, centers=...,
) -> tuple[Incomplete, _centers]: ...
@overload
def findCirclesGrid(image, patternSize, centers=..., flags=..., blobDetector=...) -> tuple[Incomplete, _centers]: ...


def findContours(
    image: Mat,
    mode,
    method: int,
    contours=...,
    hierarchy=...,
    offset=...,
) -> tuple[
    _contours,
    _hierarchy,
]: ...


@overload
def findEssentialMat(
    points1, points2, cameraMatrix, method: int = ..., prob=..., threshold=..., mask: Mat = ...,
) -> tuple[Incomplete, _mask]: ...


@overload
def findEssentialMat(
    points1, points2, focal=..., pp=..., method=..., prob=..., threshold=..., mask=...,
) -> tuple[Incomplete, _mask]: ...


@overload
def findFundamentalMat(
    points1, points2, method: int, ransacReprojThreshold, confidence, maxIters, mask: Mat = ...,
) -> tuple[Incomplete, _mask]: ...


@overload
def findFundamentalMat(
    points1, points2, method=..., ransacReprojThreshold=..., confidence=..., mask=...,
) -> tuple[Incomplete, _mask]: ...


def findHomography(
    srcPoints, dstPoints, method: int = ..., ransacReprojThreshold=..., mask: Mat = ..., maxIters=..., confidence=...,
) -> tuple[Incomplete, _mask]: ...
def findNonZero(src: Mat, idx=...) -> _idx: ...


def findTransformECC(
    templateImage, inputImage, warpMatrix, motionType, criteria, inputMask, gaussFiltSize,
) -> tuple[Incomplete, _warpMatrix]: ...
def fitEllipse(points): ...
def fitEllipseAMS(points): ...
def fitEllipseDirect(points): ...
def fitLine(points, distType, param, reps, aeps, line=...) -> _line: ...
def flip(src: Mat, flipCode, dst: Mat = ...) -> _dst: ...


def floodFill(
    image: Mat, mask: Mat | None, seedPoint, newVal, loDiff=..., upDiff=..., flags: int | None = ...,
) -> tuple[Incomplete, _image, _mask, _rect]: ...
def gemm(src1: Mat, src2: Mat, alpha, src3, beta, dst: Mat = ..., flags: int | None = ...) -> _dst: ...
def getAffineTransform(src: Mat, dst: Mat): ...
def getBuildInformation(): ...
def getCPUFeaturesLine(): ...
def getCPUTickCount(): ...
def getDefaultNewCameraMatrix(cameraMatrix, imgsize=..., centerPrincipalPoint=...): ...
def getDerivKernels(dx, dy, ksize, kx=..., ky=..., normalize=..., ktype=...) -> tuple[_kx, _ky]: ...
def getFontScaleFromHeight(fontFace, pixelHeight, thickness=...): ...
def getGaborKernel(ksize, sigma, theta, lambd, gamma, psi=..., ktype=...): ...
def getGaussianKernel(ksize, sigma, ktype=...): ...
def getHardwareFeatureName(feature): ...
def getLogLevel(*args, **kwargs): ...  # incomplete
def getNumThreads(): ...
def getNumberOfCPUs(): ...
def getOptimalDFTSize(vecsize): ...


def getOptimalNewCameraMatrix(
    cameraMatrix, distCoeffs, imageSize, alpha, newImgSize=..., centerPrincipalPoint=...,
) -> tuple[Incomplete, _validPixROI]: ...
def getPerspectiveTransform(src: Mat, dst: Mat, solveMethod=...): ...
def getRectSubPix(image: Mat, patchSize, center, patch=..., patchType=...) -> _patch: ...
def getRotationMatrix2D(center, angle, scale): ...
def getStructuringElement(shape, ksize, anchor=...): ...
def getTextSize(text, fontFace, fontScale, thickness) -> tuple[Incomplete, _baseLine]: ...
def getThreadNum(): ...
def getTickCount(): ...
def getTickFrequency(): ...
def getTrackbarPos(trackbarname, winname): ...
def getValidDisparityROI(roi1, roi2, minDisparity, numberOfDisparities, blockSize): ...
def getVersionMajor(): ...
def getVersionMinor(): ...
def getVersionRevision(): ...
def getVersionString(): ...
def getWindowImageRect(winname): ...
def getWindowProperty(winname, prop_id): ...


@overload
def goodFeaturesToTrack(
    image: Mat,
    maxCorners,
    qualityLevel,
    minDistance,
    corners=...,
    mask: Mat = ...,
    blockSize=...,
    useHarrisDetector=...,
    k=...,
) -> _corners: ...


@overload
def goodFeaturesToTrack(
    image,
    maxCorners,
    qualityLevel,
    minDistance,
    mask,
    blockSize,
    gradientSize,
    corners=...,
    useHarrisDetector=...,
    k=...,
) -> _corners: ...


def goodFeaturesToTrackWithQuality(*args, **kwargs): ...  # incomplete


def grabCut(
    img: Mat,
    mask: Mat | None,
    rect,
    bgdModel,
    fgdModel,
    iterCount,
    mode=...,
) -> tuple[
    _mask,
    _bgdModel,
    _fgdModel,
]: ...


def groupRectangles(rectList, groupThreshold, eps=...) -> tuple[_rectList, _weights]: ...
def haveImageReader(filename: str): ...
def haveImageWriter(filename: str): ...
def haveOpenVX(): ...
def hconcat(src: Mat | Sequence[Mat], dst: Mat = ...) -> _dst: ...
def idct(src: Mat, dst: Mat = ..., flags: int | None = ...) -> _dst: ...
def idft(src: Mat, dst: Mat = ..., flags: int | None = ..., nonzeroRows=...) -> _dst: ...
def illuminationChange(src: Mat, mask: Mat, dst: Mat = ..., alpha=..., beta=...) -> _dst: ...
def imcount(*args, **kwargs): ...  # incomplete
def imdecode(buf, flags: int | None): ...
def imencode(ext, img: Mat, params=...) -> tuple[Incomplete, _buf]: ...
def imread(filename: str, flags: int | None = ...) -> Mat: ...
def imreadmulti(filename: str, mats=..., flags: int | None = ...) -> tuple[Incomplete, _mats]: ...
def imshow(winname, mat) -> None: ...
def imwrite(filename: str, img: Mat, params: Sequence[int] = ...) -> bool: ...
def imwritemulti(*args, **kwargs): ...  # incomplete
def inRange(src: Mat, lowerBound: Mat, upperbBound: Mat, dst: Mat = ...) -> Mat: ...
def initCameraMatrix2D(objectPoints, imagePoints, imageSize, aspectRatio=...): ...
def initInverseRectificationMap(*args, **kwargs): ...  # incomplete


def initUndistortRectifyMap(
    cameraMatrix, distCoeffs, R, newCameraMatrix, size, m1type, map1=..., map2=...,
) -> tuple[_map1, _map2]: ...
def inpaint(src: Mat, inpaintMask, inpaintRadius, flags: int | None, dst: Mat = ...) -> _dst: ...
def insertChannel(src: Mat, dst: Mat, coi) -> _dst: ...
def integral(src: Mat, sum=..., sdepth=...) -> _sum: ...
def integral2(src: Mat, sum=..., sqsum=..., sdepth=..., sqdepth=...) -> tuple[_sum, _sqsum]: ...
def integral3(src: Mat, sum=..., sqsum=..., tilted=..., sdepth=..., sqdepth=...) -> tuple[_sum, _sqsum, _tilted]: ...
def intersectConvexConvex(_p1, _p2, _p12=..., handleNested=...) -> tuple[Incomplete, _p12]: ...
def invert(src: Mat, dst: Mat = ..., flags: int | None = ...) -> tuple[Incomplete, _dst]: ...
def invertAffineTransform(M, iM=...) -> _iM: ...
def isContourConvex(contour): ...


def kmeans(
    data, K, bestLabels, criteria, attempts, flags: int | None, centers=...,
) -> tuple[Incomplete, _bestLabels, _centers]: ...
def line(img: Mat, pt1, pt2, color, thickness=..., lineType=..., shift=...) -> _img: ...
def linearPolar(src: Mat, center, maxRadius, flags: int | None, dst: Mat = ...) -> _dst: ...
def log(src: Mat, dst: Mat = ...) -> _dst: ...
def logPolar(src: Mat, center, M, flags: int | None, dst: Mat = ...) -> _dst: ...
def magnitude(x, y, magnitude=...) -> _magnitude: ...
def matMulDeriv(A, B, dABdA=..., dABdB=...) -> tuple[_dABdA, _dABdB]: ...
def matchShapes(contour1, contour2, method: int, parameter): ...
def matchTemplate(image: Mat, templ: Mat, method: int, result: Mat = ..., mask: Mat | None = ...) -> Mat: ...
def max(src1: Mat, src2: Mat, dst: Mat = ...) -> _dst: ...
def mean(src: Mat, mask: Mat = ...): ...
def meanShift(probImage, window, criteria) -> tuple[Incomplete, _window]: ...
def meanStdDev(src: Mat, mean=..., stddev=..., mask: Mat = ...) -> tuple[_mean, _stddev]: ...
def medianBlur(src: Mat, ksize, dst: Mat = ...) -> _dst: ...
def merge(mv, dst: Mat = ...) -> _dst: ...
def min(src1: Mat, src2: Mat, dst: Mat = ...) -> _dst: ...
def minAreaRect(points): ...
def minEnclosingCircle(points) -> tuple[_center, _radius]: ...
def minEnclosingTriangle(points, triangle=...) -> tuple[Incomplete, _triangle]: ...
def minMaxLoc(src: Mat, mask: Mat = ...) -> tuple[float, float, tuple[int, int], tuple[int, int]]: ...
def mixChannels(src: Mat, dst: Mat, fromTo) -> _dst: ...
def moments(array, binaryImage=...): ...


def morphologyEx(
    src: Mat,
    op,
    kernel,
    dst: Mat = ...,
    anchor=...,
    iterations=...,
    borderType=...,
    borderValue=...,
) -> _dst: ...


def moveWindow(winname, x, y) -> None: ...
def mulSpectrums(a, b, flags: int | None, c=..., conjB=...) -> _c: ...
def mulTransposed(src: Mat, aTa, dst: Mat = ..., delta=..., scale=..., dtype=...) -> _dst: ...
def multiply(src1: Mat, src2: Mat, dst: Mat = ..., scale=..., dtype=...) -> _dst: ...
def namedWindow(winname, flags: int | None = ...) -> None: ...
@overload
def norm(src1: Mat, src2: Mat, normType: int = ..., mask: Mat | None = ...) -> float: ...
@overload
def norm(src1: Mat, src2: Mat, mask: Mat | None = ...) -> float: ...
def normalize(src: Mat, dst: Mat, alpha=..., beta=..., norm_type: int = ..., dtype=..., mask: Mat = ...) -> Mat: ...
def patchNaNs(a, val=...) -> _a: ...


def pencilSketch(
    src: Mat, dst1: Mat = ..., dst2: Mat = ..., sigma_s=..., sigma_r=..., shade_factor=...,
) -> tuple[_dst1, _dst2]: ...
def perspectiveTransform(src: Mat, m, dst: Mat = ...) -> _dst: ...
def phase(x, y, angle=..., angleInDegrees=...) -> _angle: ...
def phaseCorrelate(src1: Mat, src2: Mat, window=...) -> tuple[Incomplete, _response]: ...
def pointPolygonTest(contour, pt, measureDist): ...
def polarToCart(magnitude, angle, x=..., y=..., angleInDegrees=...) -> tuple[_x, _y]: ...
def pollKey(*args, **kwargs): ...  # incomplete
def polylines(img: Mat, pts, isClosed, color, thickness=..., lineType=..., shift=...) -> _img: ...
def pow(src: Mat, power, dst: Mat = ...) -> _dst: ...
def preCornerDetect(src: Mat, ksize, dst: Mat = ..., borderType=...) -> _dst: ...


def projectPoints(
    objectPoints, rvec, tvec, cameraMatrix, distCoeffs, imagePoints=..., jacobian=..., aspectRatio=...,
) -> tuple[_imagePoints, _jacobian]: ...


def putText(
    img: Mat,
    text,
    org,
    fontFace,
    fontScale,
    color,
    thickness=...,
    lineType=...,
    bottomLeftOrigin=...,
) -> _img: ...


def pyrDown(src: Mat, dst: Mat = ..., dstsize=..., borderType=...) -> _dst: ...
def pyrMeanShiftFiltering(src: Mat, sp, sr, dst: Mat = ..., maxLevel=..., termcrit=...) -> _dst: ...
def pyrUp(src: Mat, dst: Mat = ..., dstsize=..., borderType=...) -> _dst: ...
def randShuffle(dst: Mat, iterFactor=...) -> _dst: ...
def randn(dst: Mat, mean, stddev) -> _dst: ...
def randu(dst: Mat, low, high) -> _dst: ...
def readOpticalFlow(path): ...
@overload
def recoverPose(points1, points2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, E, R, t, mask): ...


@overload
def recoverPose(
    E,
    points1,
    points2,
    cameraMatrix,
    R=...,
    t=...,
    mask: Mat = ...,
) -> tuple[
    Incomplete,
    _R,
    _t,
    _mask,
]: ...


@overload
def recoverPose(E, points1, points2, R=..., t=..., focal=..., pp=..., mask=...) -> tuple[Incomplete, _R, _t, _mask]: ...


@overload
def recoverPose(
    E, points1, points2, cameraMatrix, distanceThresh, R=..., t=..., mask=..., triangulatedPoints=...,
) -> tuple[Incomplete, _R, _t, _mask, _triangulatedPoints]: ...
@overload
def rectangle(img: Mat, pt1: _Point, pt2: _Point, color, thickness=..., lineType=..., shift=...) -> Mat: ...
@overload
def rectangle(img: Mat, rec: _Rect, color, thickness=..., lineType=..., shift=...) -> Mat: ...


def rectify3Collinear(
    cameraMatrix1,
    distCoeffs1,
    cameraMatrix2,
    distCoeffs2,
    cameraMatrix3,
    distCoeffs3,
    imgpt1,
    imgpt3,
    imageSize,
    R12,
    T12,
    R13,
    T13,
    alpha,
    newImgSize,
    flags: int | None,
    R1=...,
    R2=...,
    R3=...,
    P1=...,
    P2=...,
    P3=...,
    Q=...,
) -> tuple[Incomplete, _R1, _R2, _R3, _P1, _P2, _P3, _Q, _roi1, _roi2]: ...
def redirectError(onError) -> None: ...
def reduce(src: Mat, dim, rtype, dst: Mat = ..., dtype=...) -> _dst: ...
def reduceArgMax(*args, **kwargs): ...  # incomplete
def reduceArgMin(*args, **kwargs): ...  # incomplete
def remap(src: Mat, map1, map2, interpolation: int, dst: Mat = ..., borderMode=..., borderValue=...) -> _dst: ...
def repeat(src: Mat, ny, nx, dst: Mat = ...) -> _dst: ...
def reprojectImageTo3D(disparity, Q, _3dImage=..., handleMissingValues=..., ddepth=...) -> _3dImage: ...


def resize(
    src: Mat | int | bool,
    dsize: _Size | None,
    dst: Mat | _NumericScalar = ...,
    fx: float = ...,
    fy: float = ...,
    interpolation: int = ...,
) -> Mat: ...
@overload
def resizeWindow(winname, width, height) -> None: ...
@overload
def resizeWindow(winname, size) -> None: ...
def rotate(src: Mat, rotateCode, dst: Mat = ...) -> _dst: ...
def rotatedRectangleIntersection(rect1, rect2, intersectingRegion=...) -> tuple[Incomplete, _intersectingRegion]: ...
def sampsonDistance(pt1, pt2, F): ...
def scaleAdd(src1: Mat, alpha, src2: Mat, dst: Mat = ...) -> _dst: ...
def seamlessClone(src: Mat, dst: Mat, mask: Mat | None, p, flags: int | None, blend=...) -> _blend: ...
@overload
def selectROI(windowName, img: Mat, showCrosshair=..., fromCenter=...): ...
@overload
def selectROI(img: Mat, showCrosshair=..., fromCenter=...): ...
def selectROIs(windowName, img: Mat, showCrosshair=..., fromCenter=...) -> _boundingBoxes: ...
def sepFilter2D(src: Mat, ddepth, kernelX, kernelY, dst: Mat = ..., anchor=..., delta=..., borderType=...) -> _dst: ...
def setIdentity(mtx, s=...) -> _mtx: ...
def setLogLevel(*args, **kwargs): ...  # incomplete
def setMouseCallback(windowName, onMouse, param=...) -> None: ...
def setNumThreads(nthreads) -> None: ...
def setRNGSeed(seed) -> None: ...
def setTrackbarMax(trackbarname, winname, maxval) -> None: ...
def setTrackbarMin(trackbarname, winname, minval) -> None: ...
def setTrackbarPos(trackbarname, winname, pos) -> None: ...
def setUseOpenVX(flag) -> None: ...
def setUseOptimized(onoff) -> None: ...
def setWindowProperty(winname, prop_id, prop_value) -> None: ...
def setWindowTitle(winname, title) -> None: ...
def solve(src1: Mat, src2: Mat, dst: Mat = ..., flags: int | None = ...) -> tuple[Incomplete, _dst]: ...
def solveCubic(coeffs, roots=...) -> tuple[Incomplete, _roots]: ...
def solveLP(Func, Constr, z=...) -> tuple[Incomplete, _z]: ...


def solveP3P(
    objectPoints, imagePoints, cameraMatrix, distCoeffs, flags: int | None, rvecs=..., tvecs=...,
) -> tuple[Incomplete, _rvecs, _tvecs]: ...


def solvePnP(
    objectPoints,
    imagePoints,
    cameraMatrix,
    distCoeffs,
    rvec=...,
    tvec=...,
    useExtrinsicGuess=...,
    flags: int | None = ...,
) -> tuple[
    Incomplete,
    _rvec,
    _tvec,
]: ...


def solvePnPGeneric(
    objectPoints,
    imagePoints,
    cameraMatrix,
    distCoeffs,
    rvecs=...,
    tvecs=...,
    useExtrinsicGuess=...,
    flags: int | None = ...,
    rvec=...,
    tvec=...,
    reprojectionError=...,
) -> tuple[Incomplete, _rvecs, _tvecs, _reprojectionError]: ...


def solvePnPRansac(
    objectPoints,
    imagePoints,
    cameraMatrix,
    distCoeffs,
    rvec=...,
    tvec=...,
    useExtrinsicGuess=...,
    iterationsCount=...,
    reprojectionError=...,
    confidence=...,
    inliers=...,
    flags: int | None = ...,
) -> tuple[Incomplete, _rvec, _tvec, _inliers]: ...


def solvePnPRefineLM(
    objectPoints,
    imagePoints,
    cameraMatrix,
    distCoeffs,
    rvec,
    tvec,
    criteria=...,
) -> tuple[
    _rvec,
    _tvec,
]: ...


def solvePnPRefineVVS(
    objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec, criteria=..., VVSlambda=...,
) -> tuple[_rvec, _tvec]: ...
def solvePoly(coeffs, roots=..., maxIters=...) -> tuple[Incomplete, _roots]: ...
def sort(src: Mat, flags: int | None, dst: Mat = ...) -> _dst: ...
def sortIdx(src: Mat, flags: int | None, dst: Mat = ...) -> _dst: ...
def spatialGradient(src: Mat, dx=..., dy=..., ksize=..., borderType=...) -> tuple[_dx, _dy]: ...
def split(m, mv=...) -> _mv: ...
def sqrBoxFilter(src: Mat, ddepth, ksize, dst: Mat = ..., anchor=..., normalize=..., borderType=...) -> _dst: ...
def sqrt(src: Mat, dst: Mat = ...) -> _dst: ...
def startWindowThread(): ...


def stereoCalibrate(
    objectPoints,
    imagePoints1,
    imagePoints2,
    cameraMatrix1,
    distCoeffs1,
    cameraMatrix2,
    distCoeffs2,
    imageSize,
    R=...,
    T=...,
    E=...,
    F=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[Incomplete, _cameraMatrix1, _distCoeffs1, _cameraMatrix2, _distCoeffs2, _R, _T, _E, _F]: ...


def stereoCalibrateExtended(
    objectPoints,
    imagePoints1,
    imagePoints2,
    cameraMatrix1,
    distCoeffs1,
    cameraMatrix2,
    distCoeffs2,
    imageSize,
    R,
    T,
    E=...,
    F=...,
    perViewErrors=...,
    flags: int | None = ...,
    criteria=...,
) -> tuple[Incomplete, _cameraMatrix1, _distCoeffs1, _cameraMatrix2, _distCoeffs2, _R, _T, _E, _F, _perViewErrors]: ...


def stereoRectify(
    cameraMatrix1,
    distCoeffs1,
    cameraMatrix2,
    distCoeffs2,
    imageSize,
    R,
    T,
    R1=...,
    R2=...,
    P1=...,
    P2=...,
    Q=...,
    flags: int | None = ...,
    alpha=...,
    newImageSize=...,
) -> tuple[_R1, _R2, _P1, _P2, _Q, _validPixROI1, _validPixROI2]: ...


def stereoRectifyUncalibrated(
    points1,
    points2,
    F,
    imgSize,
    H1=...,
    H2=...,
    threshold=...,
) -> tuple[
    Incomplete,
    _H1,
    _H2,
]: ...


def stylization(src: Mat, dst: Mat = ..., sigma_s=..., sigma_r=...) -> _dst: ...


def subtract(
    src1: Mat | _NumericScalar,
    src2: Mat | _NumericScalar,
    dst: Mat = ...,
    mask: Mat = ...,
    dtype=...,
) -> _dst: ...


def sumElems(src): ...


def textureFlattening(
    src: Mat,
    mask: Mat,
    dst: Mat = ...,
    low_threshold=...,
    high_threshold=...,
    kernel_size=...,
) -> _dst: ...


def threshold(src: Mat, thresh, maxval, type, dst: Mat = ...) -> tuple[Incomplete, _dst]: ...
def trace(mtx): ...
def transform(src: Mat, m, dst: Mat = ...) -> _dst: ...
def transpose(src: Mat, dst: Mat = ...) -> _dst: ...
def triangulatePoints(projMatr1, projMatr2, projPoints1, projPoints2, points4D=...) -> _points4D: ...
def undistort(src: Mat, cameraMatrix, distCoeffs, dst: Mat = ..., newCameraMatrix=...) -> _dst: ...
def undistortPoints(src: Mat, cameraMatrix, distCoeffs, dst: Mat = ..., R=..., P=...) -> _dst: ...
def undistortPointsIter(src: Mat, cameraMatrix, distCoeffs, R, P, criteria, dst: Mat = ...) -> _dst: ...
def useOpenVX(): ...
def useOptimized(): ...
def validateDisparity(disparity, cost, minDisparity, numberOfDisparities, disp12MaxDisp=...) -> _disparity: ...
def vconcat(src: Mat | Sequence[Mat], dst: Mat = ...) -> Mat: ...
def waitKey(delay=...): ...
def waitKeyEx(delay=...): ...


def warpAffine(
    src: Mat, M, dsize: _Size, _dst: Mat = ..., _flags: int | None = ..., _borderMode=..., _borderValue=...,
) -> _dst: ...


def warpPerspective(
    src: Mat, M, dsize: _Size, _dst: Mat = ..., _flags: int | None = ..., _borderMode=..., _borderValue=...,
) -> _dst: ...
def warpPolar(src: Mat, dsize: _Size, _center, _maxRadius, _flags: int | None, _dst: Mat = ...) -> _dst: ...
def watershed(image: Mat, markers) -> _markers: ...
def writeOpticalFlow(path, flow): ...
