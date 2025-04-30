# CARD ID
CARD_ID_CREATE_STAMP: str = 'stamp.create'
CARD_ID_HOME: str = 'home.main'

# CARD_SUBTITLES
SUBTITLE_CARD_CREATE_STAMP: str = 'add stamp > templates > enter details'

# CLOUDINARY
CLOUDINARY_TEMPLATES_FOLDER: str = 'vs_templates'
CLOUDINARY_STAMPS_FOLDER: str = 'stamps'

# URI
ADD_STAMP_URI: str = '/api/addon/templates/stamps'
DASHBOARD_URI: str = '/api/addon/dashboard'
HOME_URI: str = '/api/addon/home'
STAMPS_URI: str = '/api/addon/stamps'
STAMPS_PREVIEW_URI: str = '/api/addon/stamps/preview'
STAMPS_WEB_PREVIEW_URI: str  = '/stamp/preview'
TEMPLATES_CARD_URI: str = '/api/addon/templates'
ADD_USERS_URI: str = '/api/addon/users'
USERS_URI: str = '/api/addon/admin/users'

# TEMPLATES
CARD_ID_TEMPLATES: str = 'templates.main'
SUBTITLE_CARD_TEMPLATES: str = 'add stamp > templates'

COLOR_CODES: list[dict[str, str]]= [
    {
        'name': 'blue',
        'code': '#35446D',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366441/blue_zehuxb.png',
    },
    {
        'name': 'blue_light',
        'code': '#84AFF3',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366441/blue_light_cpsflb.png',
    },
    {
        'name': 'black',
        'code': '#000000',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366441/black_pga3jw.png',
    },
    {
        'name': 'green',
        'code': '#66F068',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366442/green_zcus6w.png',
    },
    {
        'name': 'red',
        'code': '#E60012',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366442/red_thkyop.png',
    },
    {
        'name': 'orange',
        'code': '#F3B72B',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366442/orange_sfuhmv.png',
    },
    {
        'name': 'purple',
        'code': '#C62BF3',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366442/purple_tpjzdd.png',
    },
    {
        'name': 'grey',
        'code': '#737373',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366442/grey_smyvyk.png',
    }
]

# DIRECTORIES
TEMPLATES_DIR: str = './static/templates'
