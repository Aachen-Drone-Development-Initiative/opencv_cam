import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

import os

def generate_launch_description():
    camera_info_path = 'info.ini'

    config = os.path.join(
      os.getcwd(),
      'calibration',
      'opencv_cam_bottom.yaml'
      )
    
    container = ComposableNodeContainer(
        name='my_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher',
                parameters=[config],
                extra_arguments=[{'use_intra_process_comms': True}],
                remappings=[
                ('image', 'image_raw'),
                ],
            )
        ]
    )

    return launch.LaunchDescription([container])
