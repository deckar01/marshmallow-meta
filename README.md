# marshmallow-meta

*decorator syntax for marshmallow meta attributes (with inheritance)*

Decorators communicate that the behavior of a class is being modified and are more concise when only a few meta attributes are needed. Making inheritance the default further reduces the boilerplate needed to make minor changes to a subclass.

## Install

```sh
pip install marshmallow-meta
```

```py
from marshmallow_meta import meta
```

## API

### `@meta(*kwargs)`

Build a meta class that inherits attributes from the base schema's meta class.

```py
@meta(unknown=INCLUDE)
class Test(Schema):
    foo = fields.String()
```

### `@meta.new(*kwargs)`

Build a new meta class without inherited attributes.

```py
@meta.new(fields=('bar', 'baz'))
class Fresh(Test):
   pass
```

### `@meta.use(*classes, **kwargs)`

Build a meta class that inherits attributes from certain meta classes.

```py
@meta.use(Test.Meta)
class CopyCat(Schema):
   buzz = fields.String()
```
