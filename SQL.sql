-- 1. SELECT básico: listar todos os funcionários
SELECT * FROM funcionarios;

-- 2. SELECT com filtro WHERE e condição AND
SELECT nome, salario, setor
FROM funcionarios
WHERE salario > 5000 AND setor = 'Marketing';

-- 3. JOIN básico entre a tabela funcionarios e uma hipotética tabela departamentos (exemplo conceitual)
-- (Na prática usamos JOIN entre funcionarios e media_setor)
SELECT f.nome, d.nome_departamento
FROM funcionarios f
JOIN departamentos d ON f.setor = d.setor;

-- 4. JOIN com alias e filtro salario maior que 5000
SELECT f.nome, f.salario, d.nome_departamento
FROM funcionarios f
JOIN departamentos d ON f.setor = d.setor
WHERE f.salario > 5000;

-- 5. Agrupamento com GROUP BY e função agregada AVG
SELECT setor, AVG(salario) AS media_salario
FROM funcionarios
GROUP BY setor;

-- 6. HAVING para filtrar grupos após o agrupamento
SELECT setor, AVG(salario) AS media_salario
FROM funcionarios
GROUP BY setor
HAVING AVG(salario) > 4000;

-- 7. ORDER BY para ordenar resultados
SELECT nome, salario
FROM funcionarios
ORDER BY salario DESC;

-- 8. Subquery simples para encontrar funcionários com salario acima da média geral
SELECT nome, salario
FROM funcionarios
WHERE salario > (SELECT AVG(salario) FROM funcionarios);

-- 9. CTE (Common Table Expression) para calcular média salarial por setor e filtrar funcionários acima da média
WITH media_setor AS (
  SELECT setor, AVG(salario) AS media_salario
  FROM funcionarios
  GROUP BY setor
)
SELECT f.nome, f.salario, m.media_salario
FROM funcionarios f
JOIN media_setor m ON f.setor = m.setor
WHERE f.salario > m.media_salario;

-- 10. Funções analíticas: AVG OVER e RANK OVER
SELECT nome, setor, salario,
       AVG(salario) OVER (PARTITION BY setor) AS media_setor,
       RANK() OVER (PARTITION BY setor ORDER BY salario DESC) AS rank_setor
FROM funcionarios;

-- 11. Uso de alias para colunas e tabelas
SELECT f.nome AS funcionario_nome, f.salario AS salario_funcionario
FROM funcionarios f;

-- 12. Limitar resultado com ROWNUM (Oracle)
SELECT *
FROM funcionarios
WHERE ROWNUM <= 5;

-- 13. Exemplo de DELETE com bind variable (exemplo prático para segurança)
-- DELETE FROM funcionarios WHERE id = :id_funcionario;

-- 14. Exemplo de UPDATE usando alias e filtro por salário 
UPDATE funcionarios
SET salario = salario * 1.1
WHERE salario < (
  SELECT AVG(salario) FROM funcionarios
);

-- 15. Exemplo de INSERT simples (sem dados reais)
-- INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
-- VALUES (11, 'Novo Funcionário', 30, 'Curitiba', 5000, 'RH');

-- 16. Exemplo básico de criação de tabela (conceito)
-- CREATE TABLE funcionarios_novo (
--   id NUMBER PRIMARY KEY,
--   nome VARCHAR2(100) NOT NULL,
--   idade NUMBER,
--   cidade VARCHAR2(50),
--   salario NUMBER,
--   setor VARCHAR2(50)
--);

-- Observações:
-- Ainda não estudamos na prática criação e uso de PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL.
-- Não houve exercícios práticos com subqueries aninhadas complexas ou procedimentos/stored procedures.
-- Exemplos comentados indicam comandos que devem ser rodados em ambiente controlado.