from flask import Blueprint

test_module = Blueprint('saved_content', __name__, url_prefix='/saved_content')

@test_module.route('/test/')
def test_method():
    print('logging from saved_content')
    return 'testing123'