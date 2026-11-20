from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import CreateUserRequestSchema, get_public_users_client
from clients.users import private_users_client
from clients.users.users_schema import GetUserResponseSchema
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = private_users_client.get_private_users_client(user=authentication_user)
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
print("Get user data:", get_user_response.json())
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)