from copy import deepcopy
from functools import wraps
from typing import Any, Dict

from flask import Blueprint, Flask, jsonify, render_template, url_for
from flask_smorest import Api

REDOC_TEMPLATE = 'redoc.html'
REDOC_URL = 'https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js'


def _collect_components(paths: Dict[str, Any], components: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return all OpenAPI components referenced by a given set of OpenAPI paths. Will resolve $refs
    and follow them recursively, looking for nested $refs.
    """
    refs = []
    filtered_components: Dict[str, Any] = {}
    stack = list(paths.values())
    while stack:
        val = stack.pop()
        if isinstance(val, dict):
            stack.extend(val.values())
        if isinstance(val, list):
            stack.extend(val)
        if isinstance(val, str) and val.startswith('#/component') and val not in refs:
            refs.append(val)
            component_type, component_name = val.split('/')[-2:]
            component = components[component_type][component_name]
            stack.extend(component.values())
            filtered_components.setdefault(component_type, {})[component_name] = component

    return filtered_components


def _build_public_spec(internal_spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Given a full OpenAPI v3 spec with both public and internal endpoints, return a version with all
    the internal endpoints and schemas removed.
    """
    public_spec = {
        'openapi': internal_spec['openapi'],
        'info': internal_spec['info'],
        'servers': internal_spec.get('servers', []),
        'tags': [],
        'paths': {},
        'components': {},
    }

    public_tags = set()

    # Copy public paths and parameters from internal spec to public spec
    for path, methods in internal_spec['paths'].items():
        for method, spec in methods.items():
            if method != 'parameters' and spec.get('x-public'):
                public_spec['paths'].setdefault(path, {})[method] = spec
                public_tags.update(spec['tags'])
                if 'parameters' in methods and 'parameters' not in public_spec['paths'][path]:
                    public_spec['paths'][path]['parameters'] = internal_spec['paths'][path][
                        'parameters'
                    ]

    # Copy components for the above paths
    public_spec['components'] = _collect_components(
        public_spec['paths'], internal_spec['components']
    )

    # Copy tags for the above paths
    public_spec['tags'] = [tag for tag in internal_spec['tags'] if tag['name'] in public_tags]

    return public_spec


def register_api_docs_blueprint(app: Flask, api: Api) -> None:
    """
    Register Flask blueprint containing routes for public and private OpenAPI docs.

    All endpoints will be documented at `/docs/internal` and endpoints annotated with
    `@potluck.public_docs` will be documented at `/docs/public`.
    """
    blueprint = Blueprint(
        'openapi-docs', __name__, url_prefix='/docs', template_folder='./templates'
    )

    @blueprint.route('/public/openapi.json', methods=['GET'])
    def get_public_openapi_spec():
        """
        Post-process the full OpenAPI spec generated by flask-smorest, and return the paths with
        'x-public'
        """
        internal_spec = api.spec.to_dict()
        public_spec = _build_public_spec(internal_spec)
        return jsonify(public_spec)

    @blueprint.route('/internal/openapi.json', methods=['GET'])
    def get_internal_openapi_spec():
        return jsonify(api.spec.to_dict())

    @blueprint.route('/public/', methods=['GET'])
    def get_public_redoc():
        return render_template(
            REDOC_TEMPLATE,
            title=api.spec.title,
            spec_url=url_for('openapi-docs.get_public_openapi_spec'),
            redoc_url=REDOC_URL,
        )

    @blueprint.route('/internal/', methods=['GET'])
    def get_internal_redoc():
        return render_template(
            REDOC_TEMPLATE,
            title=api.spec.title,
            spec_url=url_for('openapi-docs.get_internal_openapi_spec'),
            redoc_url=REDOC_URL,
        )

    app.register_blueprint(blueprint)


def public_docs(func):
    """
    Decorator that will mark an endpoint for display in our customer-facing API docs

    Usage:

    from my_backend.extensions import potluck

    @blueprint.route('/some/public/endpoint', methods=['GET'])
    @blueprint.response(HTTPStatus.OK, public_schema)
    @potluck.public_docs
    def get_items():
        return [...]
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper._apidoc = deepcopy(getattr(wrapper, '_apidoc', {}))
    wrapper._apidoc.setdefault('manual_doc', {})['x-public'] = True

    return wrapper
