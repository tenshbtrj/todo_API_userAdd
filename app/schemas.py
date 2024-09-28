from marshmallow import Schema, fields

class ExampleSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    # その他のフィールドを定義
