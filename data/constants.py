# CARD ID
CARD_ID_CREATE_STAMP: str = 'stamp.create'
CARD_ID_HOME: str = 'home.main'
CARD_ID_REGISTRATION = 'get-started.registration'
CARD_ID_STAMP_APPLY: str = 'stamp.apply'
CARD_ID_WELCOME = 'get-started.welcome'

# CARD_SUBTITLES
SUBTITLE_CARD_CREATE_STAMP: str = 'add stamp > templates > enter details'

# CLOUDINARY
CLOUDINARY_TEMPLATES_FOLDER: str = 'vs_templates'
CLOUDINARY_STAMPS_FOLDER: str = 'stamps'

# URI
ADD_STAMP_URI: str = '/api/addon/templates/stamps'
ADD_USERS_URI: str = '/api/addon/users'
DASHBOARD_URI: str = '/api/addon/dashboard'
HOME_URI: str = '/api/addon/home'
STAMPS_URI: str = '/api/addon/stamps'
STAMPS_APPLY_CARD_URI: str = '/api/addon/stamps/apply-screen'
STAMPS_APPLY_URI: str = '/api/addon/stamps/apply'
STAMPS_PREVIEW_URI: str = '/api/addon/stamps/preview'
STAMPS_WEB_PREVIEW_URI: str  = '/stamp/preview'
TEMPLATES_CARD_URI: str = '/api/addon/templates'
USERS_URI: str = '/api/addon/admin/users'
USER_REGISTRATION_FORM_URI = '/api/addon/user/onboard'

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
        'name': 'light blue',
        'code': '#84AFF3',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366441/blue_light_cpsflb.png',
    },
    {
        'name': 'black',
        'code': '#000000',
        'icon_url': 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744366441/black_pga3jw.png',
    },
    {
        'name': 'neon green',
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
