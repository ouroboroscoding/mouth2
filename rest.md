# Mouth
Service for outgoing communication

## Requests
- [E-Mail](#e-mail)
- [SMS](#sms)
- [Locale create](#locale-create)
- [Locale delete](#locale-delete)
- [Locale Exists](#locale-exists)
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

## E-Mail
Sends out an email to the requested email address given the correct             locale and template, or content

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'email' 
).then(data => {}, error => {});
```

## SMS
Sends out an SMS to the requested phone number given the correct                locale and template, or content

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'sms' 
).then(data => {}, error => {});
```

## Locale create
Creates a new locale record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'locale' 
).then(data => {}, error => {});
```

## Locale delete
Deletes (or archives) an existing locale record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.delete(
  'locale' 
).then(data => {}, error => {});
```

## Locale Exists
Returns if the requested locale exists (True) or not (False)

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'locale/exists' 
).then(data => {}, error => {});
```

## Locale read
Returns an existing locale record instance or all records

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'locale' 
).then(data => {}, error => {});
```

## Locale update
Updates an existing locale record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.update(
  'locale' 
).then(data => {}, error => {});
```

## Locales read
Returns the list of valid locales without any requirement for being
signed in

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'locales' 
).then(data => {}, error => {});
```

## Template create
Creates a new template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'template' 
).then(data => {}, error => {});
```

## Template delete
Deletes an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.delete(
  'template' 
).then(data => {}, error => {});
```

## Template read
Fetches and returns the template with the associated content records

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'template' 
).then(data => {}, error => {});
```

## Template update
Updates an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.update(
  'template' 
).then(data => {}, error => {});
```

## Template Contents read
Returns all the content records for a single template

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'template/contents' 
).then(data => {}, error => {});
```

## Template Email create
Adds an email content record to an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'template/email' 
).then(data => {}, error => {});
```

## Template Email delete
Deletes email content from an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.delete(
  'template/email' 
).then(data => {}, error => {});
```

## Template Email update
Updated email content of an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.update(
  'template/email' 
).then(data => {}, error => {});
```

## Template Email Generate create
Generates a template from the base variable data for the purposes of            testing / validating

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'template/email/generate' 
).then(data => {}, error => {});
```

## Template SMS create
Adds an sms content record to an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'template/sms' 
).then(data => {}, error => {});
```

## Template SMS delete
Deletes sms content from an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.delete(
  'template/sms' 
).then(data => {}, error => {});
```

## Template SMS update
Updated sms content of an existing template record instance

```javascript
import mouth from '@ouroboros/mouth';
mouth.update(
  'template/sms' 
).then(data => {}, error => {});
```

## Template SMS Generate create
Generates a template from the base variable data for the purposes of
testing / validating

```javascript
import mouth from '@ouroboros/mouth';
mouth.create(
  'template/sms/generate' 
).then(data => {}, error => {});
```

## Templates read
Returns all templates in the system

```javascript
import mouth from '@ouroboros/mouth';
mouth.read(
  'templates' 
).then(data => {}, error => {});
```
