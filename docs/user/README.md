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
    id='ce6c5561-46c3-4e25-8fb0-08c42e141aac',
)

res = s.user.get_user(req)

if res.user is not None:
    # handle response
```
