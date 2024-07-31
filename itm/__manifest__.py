# Copyright (C) 2021,2022 TREVI Software
# Copyright (C) 2014 Leandro Ezequiel Baldi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "IT Infrastructure Management",
    "version": "16.2.2",
    "license": "AGPL-3",
    "category": "IT Infrastructure Management",
    "summary": """IT Assets, Credentials, Backups, Applications.""",
    "author": """TREVI Software,
        Leandro Ezequiel Baldi""",
    "website": "https://github.com/trevi-software/trevi-misc",
    "images": [
        "static/src/img/main_screenshot.png",
        "static/src/img/default_image_equipment.png",
    ],
    "depends": ["mail", "product", "web"],
    "data": [
        "security/it_security.xml",
        "security/ir.model.access.csv",
        "data/migration.xml",
        "data/application_license_data.xml",
        "data/equipment_brand_data.xml",
        "data/equipment_db_engine_data.xml",
        "data/equipment_function.xml",
        "data/equipment_mapping_data.xml",
        "data/equipment_component_data.xml",
        "data/equipment_component_cpu_data.xml",
        "data/equipment_component_net_data.xml",
        "data/equipment_component_ram_data.xml",
        "data/equipment_component_storage_data.xml",
        "data/equipment_type_data.xml",
        "wizard/create_credential_view.xml",
        "views/it_menu_view.xml",
        "views/equipment_view.xml",
        "views/equipment_worklog_view.xml",
        "views/equipment_network_view.xml",
        "views/equipment_partition_view.xml",
        "views/equipment_component_view.xml",
        "views/component_view.xml",
        "views/access_view.xml",
        "views/partner_view.xml",
        "views/backup_view.xml",
        "views/equipment_function_view.xml",
        "views/equipment_mapping_view.xml",
        "views/equipment_type_view.xml",
        "views/application_view.xml",
        "views/application_license_view.xml",
        "views/brand_view.xml",
        "views/site_view.xml",
        "views/service_ad_view.xml",
        "views/service_dhcp_view.xml",
        "views/service_wireless_view.xml",
    ],
    "demo": [],
    "test": [],
    "assets": {
        "web.assets_backend": [
            "/itm/static/src/js/itm_password_char_field.esm.js",
            "/itm/static/src/js/itm_password_char_field.xml",
        ],
    },
    "external_dependencies": {
        "python": ["cryptography"],
    },
    "installable": True,
    "application": True,
}
