# BEP-014: Modelagem e Normalização de Dados

## 📋 Sobre a Aula

Esta aula aborda os conceitos fundamentais de **modelagem e normalização de dados**, essenciais para criar bancos de dados eficientes e confiáveis. Os alunos aprenderão a estruturar dados de forma otimizada para evitar redundância e inconsistência.

## 🎯 Objetivos

- Compreender os conceitos de modelagem de dados
- Aplicar a 1ª, 2ª e 3ª formas normais
- Identificar problemas de redundância e inconsistência
- Normalizar tabelas de banco de dados
- Avaliar o impacto da modelagem na performance
- Resolver exercícios práticos de normalização

## 📚 Conteúdo

### Slides da Aula
- **Slide 01**: Introdução à Modelagem de Dados
- **Slide 02**: 1ª Forma Normal (1FN)
- **Slide 03**: 2ª Forma Normal (2FN)
- **Slide 04**: 3ª Forma Normal (3FN)
- **Slide 05**: Impacto na Performance e Integridade
- **Slide 06**: Exercícios Práticos
- **Slide 07**: Soluções dos Exercícios
- **Slide 08**: Resumo e Conclusão

### Arquivos Disponíveis
- `index.html` - Página principal de navegação
- `slide01.html` a `slide08.html` - Slides da aula
- `CONTEUDO_MARKDOWN.md` - Conteúdo completo em Markdown
- `EXERCICIOS_PRATICOS.md` - Exercícios adicionais
- `README.md` - Este arquivo

## 🔗 Pré-requisitos

Para aproveitar melhor esta aula, é importante ter conhecimento em:
- **BEP-011**: Conceitos de banco de dados relacionais
- **BEP-012**: Comandos SQL básicos (SELECT, INSERT)
- **BEP-013**: Comandos de atualização (UPDATE, DELETE)

## 🚀 Como Usar

1. **Acesse** o arquivo `index.html` para navegação
2. **Siga** a ordem sequencial dos slides
3. **Pratique** com os exercícios fornecidos
4. **Consulte** o conteúdo em Markdown para referência
5. **Complete** os exercícios práticos adicionais

## 📖 Conceitos Principais

### 1ª Forma Normal (1FN)
- Valores atômicos (indivisíveis)
- Sem grupos repetitivos
- Cada célula contém apenas um valor

### 2ª Forma Normal (2FN)
- Já está na 1FN
- Elimina dependências parciais
- Atributos dependem da chave completa

### 3ª Forma Normal (3FN)
- Já está na 2FN
- Elimina dependências transitivas
- Atributos dependem diretamente da chave

## 🛠️ Processo de Normalização

1. **Identificar** a chave primária
2. **Aplicar 1FN** - Eliminar grupos repetitivos
3. **Aplicar 2FN** - Eliminar dependências parciais
4. **Aplicar 3FN** - Eliminar dependências transitivas
5. **Verificar** integridade e performance

## 💡 Benefícios da Normalização

- **Eliminação de Redundância**: Dados únicos e consistentes
- **Integridade dos Dados**: Consistência e confiabilidade
- **Performance Otimizada**: Consultas mais rápidas
- **Facilidade de Manutenção**: Alterações simplificadas

## ⚠️ Quando NÃO Normalizar

Em alguns casos específicos, a desnormalização pode ser necessária:
- **Data Warehouses**: Dados históricos para análise
- **Relatórios Complexos**: Quando performance é crítica
- **Cache Temporário**: Dados de sessão ou temporários
- **Sistemas Legados**: Migração gradual necessária

## 🎯 Exercício Final

**Desafio**: Projete um sistema de e-commerce normalizado considerando:
- Clientes com endereços
- Produtos com categorias e fornecedores
- Pedidos com múltiplos itens
- Pagamentos e entregas

**Objetivo**: Aplicar todas as formas normais e justificar suas decisões de modelagem.

## 🔄 Próximos Passos

Após dominar a normalização, você estará pronto para:
- **BEP-015**: Joins e Consultas Avançadas
- **BEP-016**: Conectando Python com Banco de Dados

## 📝 Recursos Adicionais

### Comandos SQL Úteis
```sql
-- Verificar estrutura de tabela
DESCRIBE nome_da_tabela;

-- Verificar chaves estrangeiras
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_SCHEMA = 'nome_do_banco';
```

### Checklist de Normalização
- [ ] Tabela está na 1FN? (valores atômicos, sem grupos repetitivos)
- [ ] Tabela está na 2FN? (sem dependências parciais)
- [ ] Tabela está na 3FN? (sem dependências transitivas)
- [ ] Chaves primárias definidas corretamente?
- [ ] Chaves estrangeiras estabelecidas?
- [ ] Integridade referencial garantida?
- [ ] Performance considerada?
- [ ] Manutenibilidade assegurada?

## 🏆 Conquistas da Aula

Ao final desta aula, você terá:
- ✅ Dominado os conceitos de 1FN, 2FN e 3FN
- ✅ Desenvolvido habilidades para identificar problemas de normalização
- ✅ Aprendido a resolver exercícios práticos
- ✅ Desenvolvido pensamento crítico sobre trade-offs
- ✅ Estará pronto para consultas avançadas e joins

## 📞 Suporte

Para dúvidas ou sugestões sobre esta aula, consulte:
- Conteúdo em Markdown para referência completa
- Exercícios práticos para reforço
- Próximas aulas para continuidade do aprendizado

---

**© 2025 - IFBA CEPEDI - Conteúdo Educacional**
