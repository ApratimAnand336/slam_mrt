from glob import glob

from setuptools import find_packages, setup

package_name = 'rover_gazebosim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/rover_gazebosim/launch', ['launch/spawn_rover.launch.py']),
        ('share/rover_gazebosim/world', ['world/rover.world']),
        # ('share/rover_gazebosim/urdf', ['urdf/rrbot.urdf']),
        # ('share/rover_gazebosim/config', ['config/parameter_bridge.yaml']),
        ('share/rover_gazebosim/config', ['config/joint_names_mobility urdf adaptation.yaml']),
        ('share/rover_gazebosim/urdf', ['urdf/rover.urdf']),
        ('share/rover_gazebosim/urdf', ['urdf/rover.gazebo']),
        ('share/rover_gazebosim/meshes', glob('meshes/*.STL')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='apratim',
    maintainer_email='anand.apratim336@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
