/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("yux12ixx5zn1vk4")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qbryxdzw",
    "name": "_id",
    "type": "number",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "noDecimal": false
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("yux12ixx5zn1vk4")

  // remove
  collection.schema.removeField("qbryxdzw")

  return dao.saveCollection(collection)
})
