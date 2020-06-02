import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-fleet",
    description="Meta package for oca-fleet Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-fleet_vehicle_category',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)