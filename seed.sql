INSERT INTO public.autores_autor(id, nome, data_criacao, criado_em, atualizado_em)
	VALUES ('04dc4932-24b5-4a00-ae66-ff71efb2c0ec', 'Sir Arthur Conan Doyle', '1859-05-22 12:00:21-00', '1859-05-22 12:00:21-00', '1930-07-07 21:00:12-00');

INSERT INTO public.livros_livro(
	id, nome, data_criacao, numero_pagina, produtora, criado_em, atualizado_em)
	VALUES ('589dde09-2ab3-4f3f-bb94-d94ee49b7865', 'The adventures of Sherlock Holmes', '1892-01-01 00:00:00-00', 292, 'Abril', '1892-01-01 00:00:00-00', '9999-12-31 23:59:59-00');
INSERT INTO public.livros_livro(id, nome, data_criacao, numero_pagina, produtora, criado_em, atualizado_em)
	VALUES ('8d169860-b8d7-4caf-b0a0-9f87864fbb5f', 'Dogs of baskerville', '1902-01-01 00:00:00-00', 202, 'Abril', '1902-01-01 00:00:00-00', '9999-12-31 23:59:59-00');

INSERT INTO public.autores_autorlivro(
	id, atualizado_em, autor_id, livro_id, criado_em)
	VALUES ('c3aa24b2-f001-4331-9030-52a86f0350b9', '2022-06-12 16:00:00-03', '04dc4932-24b5-4a00-ae66-ff71efb2c0ec', '589dde09-2ab3-4f3f-bb94-d94ee49b7865', '2022-06-09 16:00:00-03');
INSERT INTO public.autores_autorlivro(
	id, atualizado_em, autor_id, livro_id, criado_em)
	VALUES ('5af31b4f-a7b1-4a1f-9671-c27f2cefb8e2', '2022-06-12 16:00:00-03', '04dc4932-24b5-4a00-ae66-ff71efb2c0ec', '8d169860-b8d7-4caf-b0a0-9f87864fbb5f', '2022-06-09 16:00:00-03');
