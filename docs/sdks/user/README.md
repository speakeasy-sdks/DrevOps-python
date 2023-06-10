# user

### Available Operations

* [get_collaborations](#get_collaborations) - Collaborations
* [get_current_user](#get_current_user) - User Information
* [get_user](#get_user) - User Information

## get_collaborations

Provides the set of organizations of which a user is a member or a collaborator.

The set of organizations that a user can collaborate on is composed of:

* Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
* The parent organization of repository that the user can collaborate on, but is not necessarily a member of
* The organization of the current user's account

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)


res = s.user.get_collaborations()

if res.collaborations is not None:
    # handle response
```


### Response

**[operations.GetCollaborationsResponse](../../models/operations/getcollaborationsresponse.md)**


## get_current_user

Provides information about the user that is currently signed in.

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)


res = s.user.get_current_user()

if res.user is not None:
    # handle response
```


### Response

**[operations.GetCurrentUserResponse](../../models/operations/getcurrentuserresponse.md)**


## get_user

Provides information about the user with the given ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetUserRequest(
    id='0f5d2cff-7c70-4a45-a26d-436813f16d9f',
)

res = s.user.get_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**

