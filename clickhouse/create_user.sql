--- Este script SQL concede várias permissões ao usuário para permitir 
--- que ele realize operações essenciais no banco de dados. Isso garante 
--- que o usuário airbyte_user tenha os direitos necessários para
--- criar, modificar e gerenciar dados dentro do banco de dados

GRANT CREATE ON * TO airbyte_user;
GRANT CREATE ON default * TO airbyte_user;
GRANT DROP ON * TO airbyte_user;
GRANT TRUNCATE ON * TO airbyte_user;
GRANT INSERT ON * TO airbyte_user;
GRANT SELECT ON * TO airbyte_user;
GRANT CREATE DATABASE ON airbyte_internal.* TO airbyte_user;
GRANT CREATE TABLE ON airbyte_internal.* TO airbyte_user;
GRANT DROP ON airbyte_internal.* TO airbyte_user;
GRANT TRUNCATE ON airbyte_internal.* TO airbyte_user;
GRANT INSERT ON airbyte_internal.* TO airbyte_user;
GRANT SELECT ON airbyte_internal.* TO airbyte_user;