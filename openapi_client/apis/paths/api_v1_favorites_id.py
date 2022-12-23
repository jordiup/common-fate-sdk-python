from openapi_client.paths.api_v1_favorites_id.get import ApiForget
from openapi_client.paths.api_v1_favorites_id.put import ApiForput
from openapi_client.paths.api_v1_favorites_id.delete import ApiFordelete


class ApiV1FavoritesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
