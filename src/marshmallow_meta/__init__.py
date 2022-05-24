def __meta(base):
    def decorator(**kwargs):
        def wrapper(schema):
            meta = type(schema.Meta.__name__, base(schema.Meta), kwargs)
            return type(schema.__name__, (schema,), {'Meta': meta})
        return wrapper
    return decorator

meta = __meta(lambda cls: (cls,))
meta.new = __meta(lambda _: ())
meta.use = lambda *mro, **kwargs: __meta(lambda _: mro)(**kwargs)
