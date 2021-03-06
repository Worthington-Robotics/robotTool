from setuptools import setup

package_name = 'diagnostics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='worbots',
    maintainer_email='boring.someone@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'diagnostics = diagnostics.diagnostics:main',
            'limelight_indicator = diagnostics.limelight_indicator:main'
        ],
    },
)
