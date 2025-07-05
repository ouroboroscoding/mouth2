# Mouth
Service for outgoing communication

## Requests
- [E-Mail create](#e-mail-create)
- [SMS create](#sms-create)
- [Locale create](#locale-create)
- [Locale delete](#locale-delete)
- [Locale Exists read](#locale-exists-read)
- [Locale read](#locale-read)
- [Locale update](#locale-update)
- [Locales read](#locales-read)
- [Template create](#template-create)
- [Template delete](#template-delete)
- [Template read](#template-read)
- [Template update](#template-update)
- [Template Contents read](#template-contents-read)
- [Template Email create](#template-email-create)
- [Template Email delete](#template-email-delete)
- [Template Email update](#template-email-update)
- [Template Email Generate create](#template-email-generate-create)
- [Template SMS create](#template-sms-create)
- [Template SMS delete](#template-sms-delete)
- [Template SMS update](#template-sms-update)
- [Template SMS Generate create](#template-sms-generate-create)
- [Templates read](#templates-read)

## E-Mail create
Sends out an email to the requested email address given the correct
locale and template, or content. This request can only be called
wrapped in an internal key.

```python
from body import create
from brain.helpers import access

create('mouth', 'email', access.generate_key({ 'data': {
  'to': 'chris@somedomain.com',
  'template': {
    'name': 'setup',
    'locale': 'en-US',
    'variables': {
      'name': 'Chris',
      'key': '123456',
      'other': '...'
    }
  }
} }))
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| to | string | no | The address to send the email to |
| attachments | array | yes | The optional list of files to attach to the email |
| attachments[].body | base64 | no | The body of the attachment, required for each attachment |
| attachments[].filename | string | no | The filename of the attachment, required for each attachment |
| content | object | yes | The raw content to send, required if not using `template` |
| content.subject | string | no | The subject if sending raw content |
| content.text | string | yes | The text/plain content of the email, one of this or `content.html` must be set |
| content.html | string | yes | The text/html content of the email, one of this or `content.text` must be set |
| template | object | yes | The template to send, required if not using `content` |
| template._id | string | yes | The ID of the template, required if `template.name` is not passed |
| template.name | string | yes | The name of the template, required if `template._id` is not passed |
| template.locale | string | no | The locale used to generate the template |
| template.variables | object | no | The variables required for the template |

### Response example
```json
{
  "data": {
    "success": true
  }
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| success | bool | The result of sending the email via SMTP |
| error | string | Only passed if success is `false` |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1001 | DATA_FIELDS | Data sent to the request is missing or invalid |
| 1100 | DB_NO_RECORD | Failed to find the template by name or locale |
| 1203 | INTERNAL_KEY | Failed to find or decode the internal key |

[ [requests](#requests) ]

## SMS create
Sends out an SMS to the requested phone number given the correct locale
and template, or content. This request can only be called wrapped in an
internal key.

```python
from body import create
from brain.helpers import access

create('mouth', 'sms', access.generate_key({ 'data': {
  'to': '+15145551289',
  'template': {
    'name': 'setup',
    'locale': 'en-US',
    'variables': {
      'name': 'Chris',
      'key': '123456',
      'other': '...'
    }
  }
} }))
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| to | string | no | The phone number to send the SMS to |
| content | string | yes | The raw content to send, required if not using `template` |
| template | object | yes | The template to send, required if not using `content` |
| template._id | string | yes | The ID of the template, required if `template.name` is not passed |
| template.name | string | yes | The name of the template, required if `template._id` is not passed |
| template.locale | string | no | The locale used to generate the template |
| template.variables | object | no | The variables required for the template |

### Response example
```json
{
  "data": {
    "success": true,
    "sid": "7d2c3cac52c711f0a922236bb031e5e7"
  }
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| success | bool | The result of sending the email via SMTP, |
| sid | string | The ID of the sms, only passed if success is `true` |
| error | string | Only passed if success is `false` |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1001 | DATA_FIELDS | Data sent to the request is missing or invalid |
| 1100 | DB_NO_RECORD | Failed to find the template by name or locale |
| 1203 | INTERNAL_KEY | Failed to find or decode the internal key |

[ [requests](#requests) ]

## Locale create
Creates a new Locale record instance in the system.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "en-CA",
  "name": "English (Canada)"
};
mouth.create(
  'locale', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the locale in the format [a-z]{2}-[A-Z]{2}, i.e. en-US, fr-CA, sp-ES |
| name | string | no | The name of the locale to identify it |

### Response example
```json
{ "data": true }
```

### Response
`true` on success, else an error.

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to create a locale |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1101 | DB_DUPLICATE | The ID or name has already been used |

[ [requests](#requests) ]

## Locale delete
Deletes (or archives) an existing locale record instance.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "en-CA"
};
mouth.delete(
  'locale', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the locale to delete |
| archive | bool | yes | Set to true to archive the locale instead of deleting it |

### Response example
```json
{ "data": true }
```

### Response
`true` | `false` on DB success, else an error code

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to delete a locale |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The request template does not exist |
| 1105 | DB_KEY_BEING_USED | The template can't be deleted due to existing child locale templates |

[ [requests](#requests) ]

## Locale Exists read
Returns true if one or all locales exists.

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "en-CA" };
mouth.read(
  'locale/exists', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | str \| str[] | no | The ID(s) of the locale(s) to check for |

### Response example
```json
{ "data": true }
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| `true` if the locale(s) exist | else | `false` |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1001 | DATA_FIELDS | Missing or invalid data passed |

[ [requests](#requests) ]

## Locale read
Returns an existing locale record, all active locales, or all locales.

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "en-CA" };
mouth.read(
  'locale', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | yes | The ID of the specific locale to get |
| archived | bool | yes | Set to true to return all locales instead of just the active (non-archived) ones |

### Response example
```json
{
  "data": {
    "_id": "en-CA",
    "_archived": false,
    "_created": 1750969986,
    "name": "English (Canada)",
  }
}
```

### Response
One or more locale objects

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to read locales |
| 1100 | DB_NO_RECORD | The specific locale requested does not exist |

[ [requests](#requests) ]

## Locale update
Updates an existing locale record instance, though technically the only
field that can be updated is the name.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "en-CA",
  "name": "Canadian / English"
};
mouth.update(
  'locale', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the locale to update |
| name | string | no | The new name of the locale |

### Response example
```json
{ "data": true }
```

### Response
`true` on success, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to update locales |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID request doesn't exist |
| 1101 | DB_DUPLICATE | The name conflicts with another record |
| 1106 | DB_ARCHIVED | The record exists but is archived |

[ [requests](#requests) ]

## Locales read
Returns the list of valid locales without any requirement for being
signed in.

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'locales', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| archived | bool | yes | Optionally set this to `true` to include archived locales |

### Response example
```json
{
  "data": [ {
    "_id": "en-CA",
    "name": "Canadian / English"
  } ]
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| _id | string | The ID of the locale |
| name | string | The name of the locale |

[ [requests](#requests) ]

## Template create
Creates a new Template record instance in the DB.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "name": "forgot password",
  "variables": {
    "email": "first.last@test.com",
    "name": "First Last",
    "url": "https://test.com/forgot/reset/a247e"
  }
};
mouth.create(
  'template', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| name | string | no | The name of the new Template |
| variables | object | no | A key / example store of the acceptable variables for the template |

### Response example
```json
{ "data": "3369bc9c536f11f086f7c1bd71fea541" }
```

### Response
Returns the new trimmed UUID of the Template on success, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to create a Template |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1101 | DB_DUPLICATE | The name conflicts with an existing Template |

[ [requests](#requests) ]

## Template delete
Deletes an existing template record instance and all locale instances
associated with it. Be very careful doing this, as this service has no
way of knowing what other services require templates.

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "3369bc9c536f11f086f7c1bd71fea541" };
mouth.delete(
  'template', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the template to delete |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to delete Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested doesn't exist |

[ [requests](#requests) ]

## Template read
Fetches and returns the template with the associated content records

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "3369bc9c536f11f086f7c1bd71fea541" };
mouth.read(
  'template', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the Template to fetch |

### Response example
```json
{
  "data": {
    "_id": "3369bc9c536f11f086f7c1bd71fea541",
    "_created": 1751041150,
    "_updated": 1751041150,
    "name": "forgot password",
    "variables": {
      "email": "first.last@test.com",
      "name": "First Last",
      "url": "https://test.com/forgot/reset/a247e"
    },
    "contents": [ {
      "_id": "71539ff5537411f086f7c1bd71fea541",
      "_created": 1751041296,
      "_updated": 1751041296,
      "template": "3369bc9c536f11f086f7c1bd71fea541",
      "locale": "en-CA",
      "subject": "Password Reset Request",
      "text": "Hi {name}, click this {url}",
      "html": "<p>Hi {name}, <a href=\"{url}\">click here</a> to reset your password</p>",
      "type": "email"
    } ]
  }
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| _id | string | The ID of the Template |
| _created | timestamp | The second in time the Template was created |
| _updated | timestamp | The second in time the Template was last updated |
| name | string | The name of the Template |
| variables | object | The key / example values available for the Template |
| contents | array | The list of locale content sub-Template objects available for the Template (See individual types for an idea of the expected data) |
| contents[]._id | string | The ID of the locale sub-Template |
| contents[]._created | timestamp | The second in time the sub-Template was created |
| contents[]._updated | timestamp | The second in time the sub-Template was last updated |
| contents[].template | string | The ID you requested originally |
| contents[].locale | string | The locale associated with the sub-Template |
| contents[].type | string | The type of sub-Template |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to read Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested does not exist |

[ [requests](#requests) ]

## Template update
Updates an existing Template record instance. In the example we are
removing the "email" variable since it is not being used.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "",
  "name": "forgot password",
  "variables": {
    "name": "First Last",
    "url": "https://test.com/forgot/reset/a247e"
  }
};
mouth.update(
  'template', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the Template to update |
| name | string | yes | The name of the new Template |
| variables | object | yes | A key / example store of the acceptable variables for the template |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to update Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested does not exist |
| 1101 | DB_DUPLICATE | The new name conflicts with an existing Template |

[ [requests](#requests) ]

## Template Contents read
Returns all the content records for a single template. The response
variables listed below should be consider only the list of mandatory
variables, as each Template type will contain it's own variables which
will be included alongside the listed ones.

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "3369bc9c536f11f086f7c1bd71fea541" };
mouth.read(
  'template/contents', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the template to find contents for |

### Response example
```json
{
  "data": [ {
    "_id": "71539ff5537411f086f7c1bd71fea541",
    "_created": 1751041296,
    "_updated": 1751041296,
    "template": "3369bc9c536f11f086f7c1bd71fea541",
    "locale": "en-CA",
    "subject": "Password Reset Request",
    "text": "Hi {name}, click this {url}",
    "html": "<p>Hi {name}, <a href=\"{url}\">click here</a> to reset your password</p>",
    "type": "email"
  } ]
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| []._id | string | The ID of the locale sub-Template |
| []._created | timestamp | The second in time the sub-Template was created |
| []._updated | timestamp | The second in time the sub-Template was last updated |
| [].template | string | The ID you requested originally |
| [].locale | string | The locale associated with the sub-Template |
| [].type | string | The type of sub-Template |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to read Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested does not exist |

[ [requests](#requests) ]

## Template Email create
Adds an email content record to an existing template record instance by
locale.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "template": "3369bc9c536f11f086f7c1bd71fea541",
  "locale": "en-CA",
  "subject": "Password Reset Request",
  "text": "Hi {name}, click this {url}",
  "html": "<p>Hi {name}, <a href=\"{url}\">click here</a> to reset your password</p>"
};
mouth.create(
  'template/email', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| template | string | no | The ID of the Template to add to |
| locale | string | no | The locale associated |
| subject | string | no | The subject of the email |
| text | string | no | The text/plain version of the email |
| html | string | no | The text/html version of the email |

### Response example
```json
{ "data": "71539ff5537411f086f7c1bd71fea541" }
```

### Response
Returns the ID of the new email content record, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to create sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The template or locale requested does not exist |
| 1101 | DB_DUPLICATE | The locale is already used in the template |
| 1300 | TEMPLATE_CONTENT_ERROR | The template has errors related to variables or imports |

[ [requests](#requests) ]

## Template Email delete
Deletes email content from an existing template record instance.

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "71539ff5537411f086f7c1bd71fea541" };
mouth.delete(
  'template/email', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the email content record to delete |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to delete sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested doesn't exist |

[ [requests](#requests) ]

## Template Email update
Updated email content of an existing template record instance by locale.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "71539ff5537411f086f7c1bd71fea541",
  "subject": "Password forgot request"
};
mouth.update(
  'template/email', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the sub-Template to update |
| subject | string | yes | The subject of the email |
| text | string | yes | The text/plain version of the email |
| html | string | yes | The text/html version of the email |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to update Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested does not exist |
| 1300 | TEMPLATE_CONTENT_ERROR | The template has errors related to variables or imports |

[ [requests](#requests) ]

## Template Email Generate create
Generates and returns a template from the base variable data for the
purposes of testing and / or validating.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "template": "3369bc9c536f11f086f7c1bd71fea541",
  "locale": "en-CA",
  "subject": "Password Reset Request",
  "text": "Hi {name}, click this {url}",
  "html": "<p>Hi {name}, <a href=\"{url}\">click here</a> to reset your password</p>"
};
mouth.create(
  'template/email/generate', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| template | string | no | The ID of the template to generate |
| locale | string | no | The locale to generate the template in |
| subject | string | yes | The subject of the email to test |
| text | string | no | The text/plain version of the email to test |
| html | string | no | The text/html version of the email to test |

### Response example
```json
{
  "data": {
    "subject": "Forgot Password Request",
    "text": "Hi First Last, click this https://test.com/forgot/reset/a247e",
    "html": "<p>Hi First Last, <a href=\"https://test.com/forgot/reset/a247e\">click here</a> to reset your password</p>"
  }
}
```

### Response variables
| name | type | description |
| ---- | ---- | ----------- |
| subject | str | The generated subject |
| text | str | The generated text/plain |
| html | str | The generated text/html |

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks rights to read sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The template or locale does not exist |

[ [requests](#requests) ]

## Template SMS create
Adds an sms content record to an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "template": "f63b6cba538011f086f7c1bd71fea541",
  "locale": "en-US",
  "content": "You have {count} new notifications!"
};
mouth.create(
  'template/sms', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| template | string | no | The ID of the Template to add to |
| locale | string | no | The locale associated |
| content | string | no | The content of the sms |

### Response example
```json
{ "data": "00114302538111f086f7c1bd71fea541" }
```

### Response
Returns the ID of the new sms content record, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to create sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The template or locale requested does not exist |
| 1101 | DB_DUPLICATE | The locale is already used in the template |
| 1300 | TEMPLATE_CONTENT_ERROR | The template has errors related to variables or imports |

[ [requests](#requests) ]

## Template SMS delete
Deletes sms content from an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
const request = { "_id": "00114302538111f086f7c1bd71fea541" };
mouth.delete(
  'template/sms', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the sms content record to delete |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to delete sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested doesn't exist |

[ [requests](#requests) ]

## Template SMS update
Updated sms content of an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "_id": "00114302538111f086f7c1bd71fea541",
  "content": "You have {count} notification(s) waiting for you!"
};
mouth.update(
  'template/sms', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| _id | string | no | The ID of the sub-Template to update |
| content | string | yes | The content of the sms |

### Response example
```json
{ "data": true }
```

### Response
Returns `true` | `false` on DB result, else an error

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to update Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The ID requested does not exist |
| 1300 | TEMPLATE_CONTENT_ERROR | The template has errors related to variables or imports |

[ [requests](#requests) ]

## Template SMS Generate create
Generates and returns a template from the base variable data for the
purposes of testing and / or validating.

```javascript
import mouth from '@ouroboros/mouth';
const request = {
  "template": "00114302538111f086f7c1bd71fea541",
  "locale": "en-US",
  "content": "You have {count} new notifications!"
};
mouth.create(
  'template/sms/generate', request 
).then(data => {}, error => {});
```

### Request variables
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| template | string | no | The ID of the template to generate |
| locale | string | no | The locale to generate the template in |
| content | string | yes | The content of the sms to test |

### Response example
```json
{ "data": "You have 5 new notifications!" }
```

### Response
A string of the generated content

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks rights to read sub-Templates |
| 1001 | DATA_FIELDS | Missing or invalid data passed |
| 1100 | DB_NO_RECORD | The template or locale does not exist |

[ [requests](#requests) ]

## Templates read
Returns all templates in the system

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'templates' 
).then(data => {}, error => {});
```

### Response example
```json
{
  "data": [ {
    "_id": "3369bc9c536f11f086f7c1bd71fea541",
    "_created": 1751041150,
    "_updated": 1751041150,
    "name": "forgot password",
    "variables": {
      "email": "first.last@test.com",
      "name": "First Last",
      "url": "https://test.com/forgot/reset/a247e"
    }
  } ]
}
```

### Response
Returns an array of Template objects ordered by name

### Error codes
| code | constant | description |
| ---- | -------- | ----------- |
| 1000 | RIGHTS | The user lacks the rights to read Templates |

[ [requests](#requests) ]
