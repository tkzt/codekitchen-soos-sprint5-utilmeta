from datetime import datetime
from utilmeta.core import api, orm
from domain.note.models import Note


class NoteSchema(orm.Schema[Note]):
    id: int
    title: str
    content: str
    create_time: datetime
    updated_time: datetime


class NoteQuery(orm.Query[Note]):
    id: int


class NoteCreation(orm.Schema[Note]):
    create_time: datetime = orm.Field(no_input=True)
    updated_time: datetime = orm.Field(no_input=True)


class NoteUpdate(orm.Schema):
    title: str | None = None
    content: str | None = None


@api.CORS(allow_origin="*")
class RootAPI(api.API):
    @api.get("/notes/{note_id}")
    def retrieve_note(self, note_id: int):
        note = Note.objects.filter(id=note_id).exists()
        if note:
            return NoteSchema.init(Note.objects.get(pk=note_id))
        return None

    @api.post("/notes")
    def create_note(self, note: NoteCreation):
        note.save()
        return note.pk

    @api.put("/notes/{note_id}")
    def update_note(self, note_id: int, note: NoteUpdate):
        exist_note = Note.objects.get(pk=note_id)
        if note.title and note.title != exist_note.title:
            exist_note.title = note.title
        if note.content and note.content != exist_note.content:
            exist_note.content = note.content
        exist_note.save()
        return NoteSchema.init(exist_note)

    @api.delete("/notes/{note_id}")
    def delete_note(self, note_id: int):
        exist_note = Note.objects.get(pk=note_id)
        if exist_note:
            exist_note.delete()
