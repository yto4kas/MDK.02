import fastapi
import peewee
from src.server.database.models import BaseModel
from src.server.database.pydantic_models import BaseModelModify
from typing import Type


class RouterManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[BaseModelModify], prefix: str,
                 tags: [str]) -> None:
        self.database_model: Type[BaseModel] = database_model
        self.pydantic_model: Type[BaseModelModify] = pydantic_model
        self.fastapi_router: fastapi.APIRouter = fastapi.APIRouter(prefix=prefix, tags=tags)
        self.resolver_manager = ResolverManager(self.database_model, self.pydantic_model)
        self.init_routers()

    def init_routers(self):
        t = self.pydantic_model

        @self.fastapi_router.get('/get_all', response_model=list[t])
        def generate_get_all_router():
            return self.resolver_manager.get_all()

        @self.fastapi_router.get('/get/{id}', response_model=t)
        def get(id: int):
            return self.resolver_manager.get(id)

        @self.fastapi_router.post('/create/', response_model=t)
        def create(new_model: t):
            return self.resolver_manager.create(new_model)

        @self.fastapi_router.delete('/delete/{id}', response_model=None)
        def delete(id: int):
            return self.resolver_manager.delete(id)

        @self.fastapi_router.put('/update/{id}', response_model=t)
        def update(id: int, new_model: t):
            return self.resolver_manager.update(id, new_model)


class ResolverManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[BaseModelModify]):
        self.database_model: Type[BaseModel] = database_model
        self.pydantic_model: Type[BaseModelModify] = pydantic_model

    def get_all(self):
        models_list = []
        for model in self.database_model.select():
            new_model = {}

            for atr in model.__data__:
                get_atr = getattr(model, atr)

                new_model[atr] = get_atr.id if isinstance(get_atr, peewee.Model) else get_atr

            models_list.append(new_model)

        return models_list

    def get(self, id: int):
        return self.database_model.get(self.database_model.id == id).__data__

    def create(self, new_model: Type[BaseModelModify]):
        new_database_model: Type[BaseModel] = self.database_model.create()
        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue

            setattr(new_database_model, atr, getattr(new_model, atr))

        new_database_model.save()

        return self.get(new_database_model.id)

    def delete(self, id: int):
        self.database_model.get(self.database_model.id == id).delete_instance()

    def update(self, id: int, new_model: Type[BaseModelModify]):
        model: Type[BaseModel] = self.database_model.get(self.database_model.id == id)

        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue

            setattr(model, atr, getattr(new_model, atr))

        model.save()

        return self.get(model.id)
